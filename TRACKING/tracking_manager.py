"""
Unwind Visual Cortex - AI Agent Tracking Manager
Utility for AI agents to read and update the tracking database

This module provides simple functions for AI agents to:
- Load current system state
- Update task status
- Log sessions
- Create debriefs
- Check next priority task
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any


class TrackingManager:
    """Manages the AI-native tracking database for Unwind Visual Cortex"""
    
    def __init__(self, db_path: str = "/home/ubuntu/unwind_visual_cortex/tracking_database.json"):
        """
        Initialize the tracking manager
        
        Args:
            db_path: Path to the tracking database JSON file
        """
        self.db_path = db_path
        self.db = self._load_database()
    
    def _load_database(self) -> Dict[str, Any]:
        """Load the tracking database from JSON file"""
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Tracking database not found at {self.db_path}")
        
        with open(self.db_path, 'r') as f:
            return json.load(f)
    
    def _save_database(self) -> None:
        """Save the tracking database to JSON file"""
        self.db['system_metadata']['last_updated'] = datetime.utcnow().isoformat() + 'Z'
        
        with open(self.db_path, 'w') as f:
            json.dump(self.db, f, indent=2)
    
    def get_system_status(self) -> Dict[str, Any]:
        """
        Get current system status overview
        
        Returns:
            Dictionary with system metadata and health
        """
        return {
            'metadata': self.db['system_metadata'],
            'health': self.db['system_health'],
            'current_phase': self.db['system_metadata']['current_phase'],
            'overall_progress': self.db['system_metadata']['overall_progress_percent']
        }
    
    def get_next_task(self) -> Optional[Dict[str, Any]]:
        """
        Get the next highest priority task that is queued
        
        Returns:
            Task dictionary or None if no queued tasks
        """
        queued_tasks = []
        
        for task_id, task in self.db['task_queue'].items():
            if task['status'] == 'queued':
                # Check if dependencies are met
                deps_met = all(
                    self.db['task_queue'].get(dep, {}).get('status') == 'done'
                    for dep in task.get('dependencies', [])
                )
                
                if deps_met:
                    queued_tasks.append(task)
        
        if not queued_tasks:
            return None
        
        # Sort by priority (critical > high > medium > low)
        priority_order = {'critical': 0, 'high': 1, 'medium': 2, 'low': 3}
        queued_tasks.sort(key=lambda t: priority_order.get(t['priority'], 99))
        
        return queued_tasks[0]
    
    def start_task(self, task_id: str, agent_id: str) -> None:
        """
        Mark a task as in progress
        
        Args:
            task_id: The task ID to start
            agent_id: The agent working on the task
        """
        if task_id not in self.db['task_queue']:
            raise ValueError(f"Task {task_id} not found in queue")
        
        self.db['task_queue'][task_id]['status'] = 'in_progress'
        self.db['task_queue'][task_id]['assigned_to'] = agent_id
        
        # Update phase current task
        phase = self.db['task_queue'][task_id]['phase']
        phase_key = f"phase_{phase}"
        if phase_key in self.db['master_roadmap']:
            self.db['master_roadmap'][phase_key]['current_task'] = task_id
            self.db['master_roadmap'][phase_key]['assigned_agent'] = agent_id
            
            if self.db['master_roadmap'][phase_key]['status'] == 'not_started':
                self.db['master_roadmap'][phase_key]['status'] = 'in_progress'
                self.db['master_roadmap'][phase_key]['start_date'] = datetime.now().strftime('%Y-%m-%d')
        
        self._save_database()
    
    def complete_task(self, task_id: str, actual_hours: float, notes: Optional[str] = None) -> None:
        """
        Mark a task as completed
        
        Args:
            task_id: The task ID to complete
            actual_hours: Actual time spent on task
            notes: Optional completion notes
        """
        if task_id not in self.db['task_queue']:
            raise ValueError(f"Task {task_id} not found in queue")
        
        self.db['task_queue'][task_id]['status'] = 'done'
        self.db['task_queue'][task_id]['actual_hours'] = actual_hours
        self.db['task_queue'][task_id]['completion_date'] = datetime.now().strftime('%Y-%m-%d')
        
        if notes:
            self.db['task_queue'][task_id]['notes'] = notes
        
        # Update system metadata
        self.db['system_metadata']['total_tasks_completed'] += 1
        
        # Update phase progress
        phase = self.db['task_queue'][task_id]['phase']
        phase_key = f"phase_{phase}"
        if phase_key in self.db['master_roadmap']:
            phase_tasks = self.db['master_roadmap'][phase_key]['tasks']
            completed = sum(1 for tid in phase_tasks if self.db['task_queue'].get(tid, {}).get('status') == 'done')
            progress = int((completed / len(phase_tasks)) * 100)
            self.db['master_roadmap'][phase_key]['progress_percent'] = progress
            
            if progress == 100:
                self.db['master_roadmap'][phase_key]['status'] = 'completed'
                self.db['master_roadmap'][phase_key]['completion_date'] = datetime.now().strftime('%Y-%m-%d')
        
        # Calculate overall progress
        total_tasks = len(self.db['task_queue'])
        completed_tasks = sum(1 for t in self.db['task_queue'].values() if t['status'] == 'done')
        self.db['system_metadata']['overall_progress_percent'] = int((completed_tasks / total_tasks) * 100)
        
        self._save_database()
    
    def log_session(self, agent_id: str, phase: int, task_id: str, 
                   duration_minutes: int, notes: str, debrief_path: str) -> str:
        """
        Log a completed session
        
        Args:
            agent_id: Agent identifier
            phase: Phase number worked on
            task_id: Task ID completed
            duration_minutes: Session duration
            notes: Session notes
            debrief_path: Path to debrief file
        
        Returns:
            Session ID
        """
        session_id = datetime.now().strftime('%Y%m%d-%H%M')
        
        session = {
            'session_id': session_id,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M'),
            'agent_id': agent_id,
            'phase_worked_on': phase,
            'task_completed': task_id,
            'duration_minutes': duration_minutes,
            'notes': notes,
            'debrief_path': debrief_path
        }
        
        self.db['session_history'].append(session)
        self.db['system_metadata']['total_sessions'] += 1
        
        self._save_database()
        
        return session_id
    
    def add_blocker(self, task_id: str, description: str, severity: str = 'medium') -> None:
        """
        Add a blocker to the active blockers list
        
        Args:
            task_id: Task that is blocked
            description: Description of the blocker
            severity: low, medium, high, critical
        """
        blocker = {
            'blocker_id': f"BLK-{datetime.now().strftime('%Y%m%d-%H%M')}",
            'task_id': task_id,
            'description': description,
            'severity': severity,
            'created_date': datetime.now().strftime('%Y-%m-%d'),
            'resolved': False
        }
        
        self.db['active_blockers'].append(blocker)
        
        # Mark task as blocked
        if task_id in self.db['task_queue']:
            self.db['task_queue'][task_id]['status'] = 'blocked'
        
        # Update system health
        if severity in ['high', 'critical']:
            self.db['system_health']['status'] = 'needs_attention'
            self.db['system_health']['issues'].append(f"Blocker on {task_id}: {description}")
        
        self._save_database()
    
    def resolve_blocker(self, blocker_id: str, resolution_notes: str) -> None:
        """
        Mark a blocker as resolved
        
        Args:
            blocker_id: The blocker ID to resolve
            resolution_notes: How it was resolved
        """
        for blocker in self.db['active_blockers']:
            if blocker['blocker_id'] == blocker_id:
                blocker['resolved'] = True
                blocker['resolution_date'] = datetime.now().strftime('%Y-%m-%d')
                blocker['resolution_notes'] = resolution_notes
                
                # Unblock the task
                task_id = blocker['task_id']
                if task_id in self.db['task_queue']:
                    self.db['task_queue'][task_id]['status'] = 'queued'
                
                break
        
        # Update system health if no more critical blockers
        critical_blockers = [b for b in self.db['active_blockers'] 
                           if not b['resolved'] and b['severity'] in ['high', 'critical']]
        
        if not critical_blockers:
            self.db['system_health']['status'] = 'healthy'
            self.db['system_health']['issues'] = []
        
        self._save_database()
    
    def get_phase_status(self, phase: int) -> Dict[str, Any]:
        """
        Get detailed status of a specific phase
        
        Args:
            phase: Phase number
        
        Returns:
            Phase status dictionary
        """
        phase_key = f"phase_{phase}"
        if phase_key not in self.db['master_roadmap']:
            raise ValueError(f"Phase {phase} not found")
        
        phase_data = self.db['master_roadmap'][phase_key]
        
        # Get task details
        tasks = []
        for task_id in phase_data['tasks']:
            if task_id in self.db['task_queue']:
                tasks.append(self.db['task_queue'][task_id])
        
        return {
            'phase_info': phase_data,
            'tasks': tasks,
            'total_tasks': len(tasks),
            'completed_tasks': sum(1 for t in tasks if t['status'] == 'done'),
            'in_progress_tasks': sum(1 for t in tasks if t['status'] == 'in_progress'),
            'blocked_tasks': sum(1 for t in tasks if t['status'] == 'blocked')
        }
    
    def update_integration_status(self, integration_name: str, status: str, 
                                 code_location: Optional[str] = None,
                                 test_status: Optional[str] = None,
                                 notes: Optional[str] = None) -> None:
        """
        Update the status of an integration
        
        Args:
            integration_name: Name of the integration
            status: planned, in_progress, integrated, tested
            code_location: Optional path to code
            test_status: Optional test status
            notes: Optional notes
        """
        if integration_name not in self.db['integration_registry']:
            raise ValueError(f"Integration {integration_name} not found")
        
        self.db['integration_registry'][integration_name]['status'] = status
        
        if code_location:
            self.db['integration_registry'][integration_name]['code_location'] = code_location
        
        if test_status:
            self.db['integration_registry'][integration_name]['test_status'] = test_status
        
        if notes:
            self.db['integration_registry'][integration_name]['notes'] = notes
        
        self._save_database()
    
    def get_recent_sessions(self, count: int = 5) -> List[Dict[str, Any]]:
        """
        Get the most recent sessions
        
        Args:
            count: Number of sessions to retrieve
        
        Returns:
            List of session dictionaries
        """
        return self.db['session_history'][-count:]
    
    def export_status_report(self) -> str:
        """
        Generate a human-readable status report
        
        Returns:
            Formatted status report string
        """
        report = []
        report.append("=" * 60)
        report.append("UNWIND VISUAL CORTEX - DEVELOPMENT STATUS REPORT")
        report.append("=" * 60)
        report.append("")
        
        # System overview
        meta = self.db['system_metadata']
        report.append(f"Overall Progress: {meta['overall_progress_percent']}%")
        report.append(f"Current Phase: {meta['current_phase']}")
        report.append(f"Total Sessions: {meta['total_sessions']}")
        report.append(f"Tasks Completed: {meta['total_tasks_completed']}")
        report.append(f"System Health: {self.db['system_health']['status'].upper()}")
        report.append("")
        
        # Phase status
        report.append("PHASE STATUS:")
        report.append("-" * 60)
        for phase_key in sorted(self.db['master_roadmap'].keys()):
            phase = self.db['master_roadmap'][phase_key]
            report.append(f"Phase {phase['phase_id']}: {phase['phase_name']}")
            report.append(f"  Status: {phase['status'].upper()}")
            report.append(f"  Progress: {phase['progress_percent']}%")
            report.append(f"  Current Task: {phase['current_task'] or 'None'}")
            report.append("")
        
        # Active blockers
        if self.db['active_blockers']:
            report.append("ACTIVE BLOCKERS:")
            report.append("-" * 60)
            for blocker in self.db['active_blockers']:
                if not blocker['resolved']:
                    report.append(f"[{blocker['severity'].upper()}] {blocker['task_id']}")
                    report.append(f"  {blocker['description']}")
                    report.append("")
        
        # Next task
        next_task = self.get_next_task()
        if next_task:
            report.append("NEXT PRIORITY TASK:")
            report.append("-" * 60)
            report.append(f"Task ID: {next_task['task_id']}")
            report.append(f"Name: {next_task['task_name']}")
            report.append(f"Priority: {next_task['priority'].upper()}")
            report.append(f"Estimated Hours: {next_task['estimated_hours']}")
            report.append(f"Details: {next_task['task_details']}")
        
        return "\n".join(report)


# Convenience functions for AI agents
def get_next_task() -> Optional[Dict[str, Any]]:
    """Quick function to get next task"""
    manager = TrackingManager()
    return manager.get_next_task()


def start_task(task_id: str, agent_id: str) -> None:
    """Quick function to start a task"""
    manager = TrackingManager()
    manager.start_task(task_id, agent_id)


def complete_task(task_id: str, actual_hours: float, notes: Optional[str] = None) -> None:
    """Quick function to complete a task"""
    manager = TrackingManager()
    manager.complete_task(task_id, actual_hours, notes)


def get_status_report() -> str:
    """Quick function to get status report"""
    manager = TrackingManager()
    return manager.export_status_report()


if __name__ == "__main__":
    # Test the tracking manager
    manager = TrackingManager()
    print(manager.export_status_report())

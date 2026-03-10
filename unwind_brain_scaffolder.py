'''
Unwind Brain Scaffolder

This script automates the setup of a new Unwind Brain cell, creating the entire
directory structure and generating all necessary coordination and tracking files.

Usage:
  python3.11 unwind_brain_scaffolder.py --name "Unwind Audio Brain" --purpose "Automated voiceover and music generation"
'''

import os
import json
import argparse
from datetime import datetime

# --- TEMPLATES --- #

TRACKING_DB_TEMPLATE = {
  "system_metadata": {
    "brain_name": "",
    "version": "1.0",
    "created_date": "",
    "last_updated": "",
    "total_sessions": 0,
    "total_tasks_completed": 0,
    "current_phase": 0,
    "overall_progress_percent": 0
  },
  "master_roadmap": {
    "phase_0": {
      "phase_id": 0,
      "phase_name": "System Setup",
      "status": "not_started",
      "start_date": None,
      "target_date": None,
      "completion_date": None,
      "progress_percent": 0,
      "current_task": None,
      "assigned_agent": None,
      "notes": "Setting up coordination system and scheduled tasks",
      "tasks": [
        "SETUP-001",
        "SETUP-002",
        "SETUP-003",
        "SETUP-004"
      ]
    }
  },
  "task_queue": {
    "SETUP-001": {
      "task_id": "SETUP-001", "priority": "critical", "phase": 0, "task_name": "Create Tracking Database",
      "task_details": "Build AI-native JSON tracking database.", "status": "queued", "assigned_to": None,
      "dependencies": [], "estimated_hours": 1, "actual_hours": 0, "completion_date": None, "notes": ""
    },
    "SETUP-002": {
      "task_id": "SETUP-002", "priority": "critical", "phase": 0, "task_name": "Initialize Debrief System",
      "task_details": "Create debrief template and folder structure.", "status": "queued", "assigned_to": None,
      "dependencies": [], "estimated_hours": 0.5, "actual_hours": 0, "completion_date": None, "notes": ""
    },
    "SETUP-003": {
      "task_id": "SETUP-003", "priority": "critical", "phase": 0, "task_name": "Configure Scheduled Task",
      "task_details": "Set up daily 6 AM recurring task.", "status": "queued", "assigned_to": None,
      "dependencies": ["SETUP-001", "SETUP-002"], "estimated_hours": 1, "actual_hours": 0, "completion_date": None, "notes": ""
    },
    "SETUP-004": {
      "task_id": "SETUP-004", "priority": "high", "phase": 0, "task_name": "Test First Automated Session",
      "task_details": "Run first scheduled session manually to verify system.", "status": "queued", "assigned_to": None,
      "dependencies": ["SETUP-003"], "estimated_hours": 1, "actual_hours": 0, "completion_date": None, "notes": ""
    }
  },
  "session_history": [],
  "active_blockers": [],
  "system_health": {
    "status": "healthy",
    "last_check": "",
    "issues": []
  }
}

# --- SCAFFOLDER CLASS --- #

class BrainScaffolder:
    def __init__(self, brain_name, brain_purpose):
        self.brain_name = brain_name
        self.brain_purpose = brain_purpose
        self.brain_folder_name = brain_name.lower().replace(" ", "_")
        self.root_path = os.path.join("/home/ubuntu", self.brain_folder_name)

    def run(self):
        print(f"🚀 Starting scaffold for: {self.brain_name}")
        self._create_directories()
        self._generate_tracking_db()
        self._copy_tracking_manager()
        self._generate_coordination_system_doc()
        self._generate_debrief_template()
        self._generate_roadmap_index()
        self._generate_readme()
        print(f"✅ Scaffold complete! Project created at: {self.root_path}")

    def _create_directories(self):
        print("  - Creating directory structure...")
        os.makedirs(os.path.join(self.root_path, "TRACKING"), exist_ok=True)
        os.makedirs(os.path.join(self.root_path, "ROADMAP_V2", "DEBRIEFS"), exist_ok=True)
        os.makedirs(os.path.join(self.root_path, "ROADMAP_V2", "PHASES"), exist_ok=True)

    def _generate_tracking_db(self):
        print("  - Generating tracking_database.json...")
        db_path = os.path.join(self.root_path, "TRACKING", "tracking_database.json")
        db_data = TRACKING_DB_TEMPLATE
        now = datetime.utcnow()
        db_data["system_metadata"]["brain_name"] = self.brain_name
        db_data["system_metadata"]["created_date"] = now.strftime("%Y-%m-%d")
        db_data["system_metadata"]["last_updated"] = now.isoformat() + "Z"
        db_data["system_health"]["last_check"] = now.isoformat() + "Z"
        with open(db_path, "w") as f:
            json.dump(db_data, f, indent=2)

    def _copy_tracking_manager(self):
        print("  - Copying tracking_manager.py...")
        # In a real scenario, this would copy from a central location.
        # For this task, I will copy it from the unwind_visual_cortex project.
        source_path = "/home/ubuntu/unwind_visual_cortex/tracking_manager.py"
        dest_path = os.path.join(self.root_path, "TRACKING", "tracking_manager.py")
        with open(source_path, "r") as src, open(dest_path, "w") as dest:
            dest.write(src.read().replace('/home/ubuntu/unwind_visual_cortex', f'/home/ubuntu/{self.brain_folder_name}'))

    def _generate_coordination_system_doc(self):
        print("  - Generating AGENT_COORDINATION_SYSTEM.md...")
        # This would also be copied from a master template
        source_path = "/home/ubuntu/unwind_visual_cortex/AGENT_COORDINATION_SYSTEM.md"
        dest_path = os.path.join(self.root_path, "ROADMAP_V2", "AGENT_COORDINATION_SYSTEM.md")
        with open(source_path, "r") as src, open(dest_path, "w") as dest:
            dest.write(src.read().replace("Unwind Visual Cortex", self.brain_name))

    def _generate_debrief_template(self):
        print("  - Generating debrief_template.md...")
        source_path = "/home/ubuntu/unwind_visual_cortex/debrief_template.md"
        dest_path = os.path.join(self.root_path, "ROADMAP_V2", "DEBRIEFS", "debrief_template.md")
        with open(source_path, "r") as src, open(dest_path, "w") as dest:
            dest.write(src.read())

    def _generate_roadmap_index(self):
        print("  - Generating ROADMAP_INDEX.md...")
        content = f"# {self.brain_name} - Roadmap Index\n\n**Purpose:** {self.brain_purpose}\n\n## Phase 1: Foundation\n- **P1-T001:** ...\n- **P1-T002:** ...\n\n## Phase 2: Core Functionality\n- **P2-T001:** ...\n"
        with open(os.path.join(self.root_path, "ROADMAP_V2", "ROADMAP_INDEX.md"), "w") as f:
            f.write(content)

    def _generate_readme(self):
        print("  - Generating README.md...")
        content = f"# {self.brain_name}\n\n{self.brain_purpose}\n\nThis brain cell is part of the Unwind ecosystem and follows the standard multi-agent coordination protocol.\n"
        with open(os.path.join(self.root_path, "README.md"), "w") as f:
            f.write(content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scaffold a new Unwind Brain cell.")
    parser.add_argument("--name", required=True, help="The name of the new brain cell (e.g., 'Unwind Audio Brain')")
    parser.add_argument("--purpose", required=True, help="A brief description of the brain's purpose.")
    args = parser.parse_args()

    scaffolder = BrainScaffolder(brain_name=args.name, brain_purpose=args.purpose)
    scaffolder.run()

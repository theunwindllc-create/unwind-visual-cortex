#!/usr/bin/env python3
"""
Start Task Script
Marks a task as started in the tracking system
"""

import sys
sys.path.append('/home/ubuntu/unwind_visual_cortex')
from tracking_manager import TrackingManager

def main():
    manager = TrackingManager()
    
    # Start P2-T002
    task_id = "P2-T002"
    agent_id = "Manus-AutoDaily-20260113"
    
    manager.start_task(task_id, agent_id)
    print(f"✅ Task {task_id} marked as started by {agent_id}")

if __name__ == "__main__":
    main()

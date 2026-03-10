#!/usr/bin/env python3
"""
Get Next Task Script
Retrieves the next priority task from the tracking system
"""

import sys
sys.path.append('/home/ubuntu/unwind_visual_cortex')
from tracking_manager import TrackingManager

def main():
    manager = TrackingManager()
    next_task = manager.get_next_task()
    
    if next_task:
        print("=" * 60)
        print("YOUR TASK:")
        print("=" * 60)
        print(f"Task ID: {next_task['task_id']}")
        print(f"Name: {next_task['task_name']}")
        print(f"Priority: {next_task['priority']}")
        print(f"Phase: {next_task['phase']}")
        print(f"Details: {next_task['task_details']}")
        print(f"Dependencies: {next_task['dependencies']}")
        print(f"Estimated Hours: {next_task['estimated_hours']}")
        print("=" * 60)
    else:
        print("No tasks available. Check for blockers.")
        print("You may need to review the tracking database.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Complete Task Script
Marks a task as complete in the tracking system
"""

import sys
sys.path.append('/home/ubuntu/unwind_visual_cortex')
from tracking_manager import TrackingManager

def main():
    manager = TrackingManager()
    
    # Complete P2-T002
    task_id = "P2-T002"
    actual_hours = 0.75  # 45 minutes
    notes = "Created Python WebSocket server and complete UXP plugin scaffold with TypeScript. Includes command handler, Premiere API wrapper, and UI. Basic communication architecture tested successfully."
    
    manager.complete_task(task_id, actual_hours, notes)
    print(f"✅ Task {task_id} marked as complete")
    print(f"   Actual hours: {actual_hours}")
    print(f"   Notes: {notes}")

if __name__ == "__main__":
    main()

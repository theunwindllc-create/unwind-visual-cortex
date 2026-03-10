#!/usr/bin/env python3
"""
Log Session Script
Records the session in the tracking database
"""

import sys
sys.path.append('/home/ubuntu/unwind_visual_cortex')
from tracking_manager import TrackingManager

def main():
    manager = TrackingManager()
    
    # Log session
    session_id = manager.log_session(
        agent_id='Manus-AutoDaily-20260113',
        phase=2,
        task_id='P2-T002',
        duration_minutes=45,
        notes='Built complete Premiere Pro integration scaffold: Python WebSocket server, UXP plugin with TypeScript, command handler, and comprehensive documentation. Communication architecture tested successfully.',
        debrief_path='ROADMAP_V2/DEBRIEFS/debrief_20260113-0600.md'
    )
    
    print(f"✅ Session logged with ID: {session_id}")

if __name__ == "__main__":
    main()

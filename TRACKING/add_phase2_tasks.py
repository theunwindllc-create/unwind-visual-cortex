#!/usr/bin/env python3
"""
Script to add Phase 2 task definitions to the tracking database.
Based on ROADMAP_INDEX.md Phase 2 objectives.
"""
import sys
sys.path.append('/home/ubuntu/unwind_visual_cortex')
from tracking_manager import TrackingManager
import json

# Load the tracking database directly
with open('/home/ubuntu/unwind_visual_cortex/tracking_database.json', 'r') as f:
    db = json.load(f)

# Define Phase 2 tasks based on ROADMAP_INDEX.md
phase2_tasks = {
    "P2-T001": {
        "task_id": "P2-T001",
        "priority": "critical",
        "phase": 2,
        "task_name": "Research Premiere Pro UXP API",
        "task_details": "Research Adobe Premiere Pro UXP (Unified Extensibility Platform) API. Document capabilities, authentication methods, and Python integration approaches. Create technical specification document.",
        "status": "queued",
        "assigned_to": None,
        "dependencies": [],
        "estimated_hours": 3,
        "actual_hours": 0,
        "completion_date": None,
        "notes": ""
    },
    "P2-T002": {
        "task_id": "P2-T002",
        "priority": "critical",
        "phase": 2,
        "task_name": "Build Premiere Pro Project Generator",
        "task_details": "Create Python module to generate Premiere Pro project files programmatically. Include sequence creation, bin organization, and basic timeline structure.",
        "status": "queued",
        "assigned_to": None,
        "dependencies": ["P2-T001"],
        "estimated_hours": 5,
        "actual_hours": 0,
        "completion_date": None,
        "notes": ""
    },
    "P2-T003": {
        "task_id": "P2-T003",
        "priority": "high",
        "phase": 2,
        "task_name": "Implement Asset Import Automation",
        "task_details": "Build function to automatically import B-roll footage and assets into Premiere Pro project. Organize by bins based on shot list categories.",
        "status": "queued",
        "assigned_to": None,
        "dependencies": ["P2-T002"],
        "estimated_hours": 4,
        "actual_hours": 0,
        "completion_date": None,
        "notes": ""
    },
    "P2-T004": {
        "task_id": "P2-T004",
        "priority": "high",
        "phase": 2,
        "task_name": "Create Marker System for CTAs",
        "task_details": "Develop automated marker placement system for Call-to-Action overlays. Markers should be placed at strategic points based on Unwind Visual Cortex recommendations.",
        "status": "queued",
        "assigned_to": None,
        "dependencies": ["P2-T002"],
        "estimated_hours": 3,
        "actual_hours": 0,
        "completion_date": None,
        "notes": ""
    },
    "P2-T005": {
        "task_id": "P2-T005",
        "priority": "medium",
        "phase": 2,
        "task_name": "Develop Sequence Template System",
        "task_details": "Create reusable sequence templates for different video types (explainer, testimonial, product demo). Templates should include standard transitions and effects.",
        "status": "queued",
        "assigned_to": None,
        "dependencies": ["P2-T002"],
        "estimated_hours": 4,
        "actual_hours": 0,
        "completion_date": None,
        "notes": ""
    },
    "P2-T006": {
        "task_id": "P2-T006",
        "priority": "medium",
        "phase": 2,
        "task_name": "Test Full Premiere Integration Workflow",
        "task_details": "End-to-end testing of Premiere Pro integration. Generate a complete project from Unwind blueprint, verify all assets import correctly, and validate marker placement.",
        "status": "queued",
        "assigned_to": None,
        "dependencies": ["P2-T003", "P2-T004", "P2-T005"],
        "estimated_hours": 3,
        "actual_hours": 0,
        "completion_date": None,
        "notes": ""
    }
}

# Add tasks to the database
for task_id, task_data in phase2_tasks.items():
    db['task_queue'][task_id] = task_data
    print(f"✓ Added {task_id}: {task_data['task_name']}")

# Update the last_updated timestamp
from datetime import datetime
db['system_metadata']['last_updated'] = datetime.utcnow().isoformat() + 'Z'

# Save the updated database
with open('/home/ubuntu/unwind_visual_cortex/tracking_database.json', 'w') as f:
    json.dump(db, f, indent=2)

print("\n✓ Phase 2 tasks successfully added to tracking database")
print(f"✓ Total tasks in queue: {len(db['task_queue'])}")

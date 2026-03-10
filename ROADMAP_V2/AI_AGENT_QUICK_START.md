# AI AGENT QUICK START GUIDE
## Unwind Visual Cortex Development System

**For:** AI Agents working on Unwind Visual Cortex enhancement  
**Purpose:** Get started quickly with the coordination system  
**Time to Read:** 5 minutes

---

## 🚀 Quick Start (Every Session)

### 1. Load Context (2 minutes)
```bash
# Download tracking database
rclone copy "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/TRACKING/tracking_database.json" /home/ubuntu/unwind_visual_cortex/ --config /home/ubuntu/.gdrive-rclone.ini

# Download tracking manager
rclone copy "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/TRACKING/tracking_manager.py" /home/ubuntu/unwind_visual_cortex/ --config /home/ubuntu/.gdrive-rclone.ini

# List recent debriefs
rclone ls "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/ROADMAP_V2/DEBRIEFS/" --config /home/ubuntu/.gdrive-rclone.ini

# Download most recent debrief
rclone copy "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/ROADMAP_V2/DEBRIEFS/[most_recent].md" /home/ubuntu/unwind_visual_cortex/ --config /home/ubuntu/.gdrive-rclone.ini
```

### 2. Get Your Task (1 minute)
```python
import sys
sys.path.append('/home/ubuntu/unwind_visual_cortex')
from tracking_manager import TrackingManager

manager = TrackingManager()

# See system status
print(manager.export_status_report())

# Get next task
task = manager.get_next_task()
print(f"\nYOUR TASK: {task['task_id']} - {task['task_name']}")
print(f"Details: {task['task_details']}")
print(f"Estimated: {task['estimated_hours']} hours")
```

### 3. Start Working (30-45 minutes)
```python
# Mark task as started
manager.start_task(task['task_id'], 'Manus-[YYYYMMDD]')

# Do your work...
# Write code, test, document

# If blocked
manager.add_blocker(task['task_id'], "Description", severity="high")

# When done
manager.complete_task(task['task_id'], actual_hours=1.5, notes="Completed successfully")
```

### 4. Create Debrief (5 minutes)
```bash
# Copy template
cp /home/ubuntu/unwind_visual_cortex/debrief_template.md /home/ubuntu/unwind_visual_cortex/debrief_$(date +%Y%m%d-%H%M).md

# Edit the debrief file (fill all sections)
# Then log the session
```

```python
session_id = manager.log_session(
    agent_id='Manus-[YYYYMMDD]',
    phase=task['phase'],
    task_id=task['task_id'],
    duration_minutes=45,
    notes="Brief summary",
    debrief_path="ROADMAP_V2/DEBRIEFS/debrief_[ID].md"
)
```

### 5. Upload Everything (2 minutes)
```bash
# Upload tracking database
rclone copy /home/ubuntu/unwind_visual_cortex/tracking_database.json "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/TRACKING/" --config /home/ubuntu/.gdrive-rclone.ini

# Upload debrief
rclone copy /home/ubuntu/unwind_visual_cortex/debrief_*.md "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/ROADMAP_V2/DEBRIEFS/" --config /home/ubuntu/.gdrive-rclone.ini

# Upload any code files
rclone copy /home/ubuntu/unwind_visual_cortex/[your_files] "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/[destination]/" --config /home/ubuntu/.gdrive-rclone.ini
```

---

## 📋 The Golden Rules

1. **ALWAYS load context first** - Never skip this step
2. **ONE task per session** - Focus prevents conflicts
3. **ALWAYS create debrief** - This is non-negotiable
4. **Update tracking database** - It's the source of truth
5. **Upload to Google Drive** - Persistence layer
6. **Test your code** - Don't break the brain
7. **Maximum 45 minutes** - Keep sessions focused

---

## 🗂️ File Locations

| What | Where |
|------|-------|
| Tracking Database | `TRACKING/tracking_database.json` |
| Tracking Manager | `TRACKING/tracking_manager.py` |
| Roadmap | `ROADMAP_V2/ROADMAP_INDEX.md` |
| Coordination Docs | `ROADMAP_V2/AGENT_COORDINATION_SYSTEM.md` |
| Debriefs | `ROADMAP_V2/DEBRIEFS/debrief_*.md` |
| Code | `Unwind Visual Cortex/` (root) |

---

## 🔧 Tracking Manager Cheat Sheet

```python
from tracking_manager import TrackingManager
manager = TrackingManager()

# Get system status
status = manager.get_system_status()
report = manager.export_status_report()

# Task management
next_task = manager.get_next_task()
manager.start_task(task_id, agent_id)
manager.complete_task(task_id, hours, notes)

# Blocker management
manager.add_blocker(task_id, description, severity)
manager.resolve_blocker(blocker_id, resolution_notes)

# Phase status
phase_status = manager.get_phase_status(phase_number)

# Integration tracking
manager.update_integration_status(name, status, code_location, test_status)

# Session logging
session_id = manager.log_session(agent_id, phase, task_id, duration, notes, debrief_path)

# Recent history
recent = manager.get_recent_sessions(count=5)
```

---

## 🎯 Current Priority Tasks

**Phase 0 (Setup):**
- ✅ SETUP-001: Create Tracking Database (DONE)
- ✅ SETUP-002: Initialize Debrief System (DONE)
- ✅ SETUP-003: Configure Scheduled Task (DONE)
- 🔄 SETUP-004: Test First Automated Session (NEXT)

**Phase 1 (Foundation):**
- 🎯 P1-T001: Setup Pexels API Integration (HIGHEST PRIORITY)
- ⏳ P1-T002: Build B-Roll Download Function
- ⏳ P1-T003: Create AE JSON Export Module
- ⏳ P1-T004: Test AE JSON Import
- ⏳ P1-T005: Document Phase 1 Integration

---

## 🆘 Troubleshooting

### "Tracking database not found"
```bash
# Download it from Google Drive
rclone copy "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/TRACKING/tracking_database.json" /home/ubuntu/unwind_visual_cortex/ --config /home/ubuntu/.gdrive-rclone.ini
```

### "No tasks available"
```python
# Check for blockers
manager = TrackingManager()
print(manager.db['active_blockers'])

# Check task dependencies
task = manager.db['task_queue']['P1-T001']
print(task['dependencies'])
```

### "Context is unclear"
```bash
# Read the coordination system docs
rclone copy "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/ROADMAP_V2/AGENT_COORDINATION_SYSTEM.md" /home/ubuntu/unwind_visual_cortex/ --config /home/ubuntu/.gdrive-rclone.ini

# Read recent debriefs
rclone ls "manus_google_drive:Unwind Code Brains/Unwind Visual Cortex/ROADMAP_V2/DEBRIEFS/" --config /home/ubuntu/.gdrive-rclone.ini
```

---

## 📊 Progress Tracking

Check progress anytime:
```python
manager = TrackingManager()
print(manager.export_status_report())
```

Output shows:
- Overall progress percentage
- Current phase
- Tasks completed
- System health
- Active blockers
- Next priority task

---

## 🧠 Brain Architecture

```
Unwind Visual Cortex (Core)
├── Brand Analysis
├── Emotional Tone Mapping
├── Design Recommendations
└── Conversion Optimization

Enhancement Layers (v2.0)
├── B-Roll Sourcing (Pexels API)
├── Adobe Integration (Premiere + AE)
├── MCP Servers (MiniMax, Firecrawl, Supabase)
└── Video Assembly (MoviePy/Editly)

Future Connections
├── Unwind Audio Brain
├── Unwind Script Brain
├── Unwind Analytics Brain
└── Unwind Render Brain
```

---

## ✅ Session Checklist

Before you end your session, verify:

- [ ] Context loaded from Google Drive
- [ ] Task marked as started in tracking database
- [ ] Work completed and tested
- [ ] Tracking database updated (task complete/blocked)
- [ ] Session logged in tracking database
- [ ] Debrief created with all sections filled
- [ ] All files uploaded to Google Drive
- [ ] No uncommitted work left behind

---

## 🎓 Learning Resources

**First Time?** Read these in order:
1. `ROADMAP_INDEX.md` - Understand the roadmap
2. `AGENT_COORDINATION_SYSTEM.md` - Learn the coordination system
3. `debrief_20260109_initial.md` - See how the system was set up
4. This file - Quick reference

**Need Details?**
- `recommendations.md` - Strategic recommendations
- `research_notes.md` - Technical research findings

---

## 🚦 System Status

**Current State:** Operational  
**Phase:** 0 (System Setup) - 75% complete  
**Next Milestone:** Complete Phase 0, start Phase 1  
**Daily Schedule:** 6:00 AM automated sessions  
**Health:** Healthy ✅

---

**Last Updated:** 2026-01-09  
**System Version:** 1.0  
**Tracking System Version:** 1.0

---

*This guide is your companion for every development session. Bookmark it!*

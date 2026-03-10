# UNWIND BRAIN MASTER PROMPT TEMPLATE
## Multi-Agent Coordination System for Any Brain Cell

**Version:** 1.0  
**Created:** 2026-01-14  
**Purpose:** Standardized template for spinning up new Unwind Brain cells with automated daily development

---

## 🧠 QUICK START - Copy This Prompt

```
I need you to create a new Unwind Brain cell called "[BRAIN_NAME]" with automated daily development sessions.

BRAIN PURPOSE: [Brief description of what this brain does]

BRAIN LOCATION: Unwind Code Brains/[BRAIN_NAME]/

CORE FUNCTIONALITY:
- [Feature 1]
- [Feature 2]
- [Feature 3]

INTEGRATIONS NEEDED:
- [Integration 1]
- [Integration 2]

Use the Unwind Brain Master Prompt system from "Unwind Code Brains/Unwind Visual Cortex/UNWIND_BRAIN_MASTER_PROMPT.md" to set up:
1. Multi-agent coordination system
2. Tracking database
3. Daily automated sessions at 6:00 AM
4. Debrief system
5. Phase-based roadmap

START WITH: Initial setup and Phase 1 planning
```

---

## 📋 SYSTEM ARCHITECTURE

Every Unwind Brain cell follows this standardized structure:

```
Unwind Code Brains/[BRAIN_NAME]/
├── TRACKING/
│   ├── tracking_database.json
│   ├── tracking_manager.py
│   └── [utility scripts]
├── ROADMAP_V2/
│   ├── AGENT_COORDINATION_SYSTEM.md
│   ├── ROADMAP_INDEX.md
│   ├── DEBRIEFS/
│   │   ├── debrief_template.md
│   │   └── debrief_[YYYYMMDD-HHMM].md
│   └── PHASES/
│       ├── PHASE_1_[NAME].md
│       ├── PHASE_2_[NAME].md
│       └── ...
├── [brain_core_file].py
├── [integration_files].py
├── README.md
└── [other project files]
```

---

## 🎯 PHASE 1: INITIAL SETUP (Automated)

When you provide the Quick Start prompt, the AI agent will automatically:

### Step 1: Create Directory Structure
- Set up Google Drive folder hierarchy
- Create TRACKING and ROADMAP_V2 folders
- Initialize DEBRIEFS folder

### Step 2: Generate Tracking Database
- Create `tracking_database.json` with:
  - System metadata
  - Master roadmap structure
  - Task queue
  - Session history
  - Active blockers
  - System health monitoring

### Step 3: Create Tracking Manager
- Generate `tracking_manager.py` utility
- Implement methods:
  - `get_next_task()`
  - `start_task()`
  - `complete_task()`
  - `log_session()`
  - `add_blocker()`

### Step 4: Set Up Coordination System
- Create `AGENT_COORDINATION_SYSTEM.md`
- Define multi-agent rules
- Document handoff protocols

### Step 5: Build Roadmap
- Create `ROADMAP_INDEX.md`
- Define phases (typically 4-6)
- Break down tasks per phase
- Set priorities and dependencies

### Step 6: Configure Scheduled Task
- Set up daily 6:00 AM recurring task
- Configure with proper context loading
- Test first automated session

---

## 📝 TRACKING DATABASE STRUCTURE

```json
{
  "system_metadata": {
    "brain_name": "[BRAIN_NAME]",
    "version": "1.0",
    "created_date": "YYYY-MM-DD",
    "last_updated": "ISO_TIMESTAMP",
    "total_sessions": 0,
    "total_tasks_completed": 0,
    "current_phase": 0,
    "overall_progress_percent": 0
  },
  "master_roadmap": {
    "phase_0": { /* Setup phase */ },
    "phase_1": { /* First development phase */ },
    "phase_2": { /* Second development phase */ }
  },
  "task_queue": {
    "SETUP-001": { /* Task details */ },
    "P1-T001": { /* Phase 1 task 1 */ }
  },
  "session_history": [],
  "active_blockers": [],
  "system_health": {
    "status": "healthy",
    "last_check": "ISO_TIMESTAMP",
    "issues": []
  }
}
```

---

## 🤖 DAILY AUTOMATED SESSION PROMPT

This is the prompt that runs every day at 6:00 AM:

```markdown
You are an AI agent working on the [BRAIN_NAME] enhancement roadmap. This is your daily automated development session at 6:00 AM.

CRITICAL: This is a multi-agent coordinated system. You must maintain perfect coherence with previous sessions.

═══════════════════════════════════════════════════════════
STEP 1: CONTEXT LOADING (MANDATORY - DO NOT SKIP)
═══════════════════════════════════════════════════════════

1. Access Google Drive: "Unwind Code Brains/[BRAIN_NAME]/"

2. Load the tracking database:
   - Download: TRACKING/tracking_database.json
   - This contains the complete system state

3. Read the coordination system:
   - Read: ROADMAP_V2/AGENT_COORDINATION_SYSTEM.md
   - This explains how the multi-agent system works

4. Check the latest debrief:
   - List files in: ROADMAP_V2/DEBRIEFS/
   - Read the most recent debrief_*.md file
   - This tells you what the last agent did

5. Load the tracking manager utility:
   - Download: TRACKING/tracking_manager.py
   - Use this to interact with the tracking database

═══════════════════════════════════════════════════════════
STEP 2: DETERMINE YOUR TASK
═══════════════════════════════════════════════════════════

Run this Python code to get your task:

```python
import sys
sys.path.append('/home/ubuntu/[brain_folder]')
from tracking_manager import TrackingManager

manager = TrackingManager()
next_task = manager.get_next_task()

if next_task:
    print("YOUR TASK:")
    print(f"Task ID: {next_task['task_id']}")
    print(f"Name: {next_task['task_name']}")
    print(f"Details: {next_task['task_details']}")
    print(f"Estimated Hours: {next_task['estimated_hours']}")
else:
    print("No tasks available. Check for blockers.")
```

═══════════════════════════════════════════════════════════
STEP 3: EXECUTE YOUR TASK (30-45 MINUTES MAX)
═══════════════════════════════════════════════════════════

1. Mark task as started:
   ```python
   manager.start_task(next_task['task_id'], 'Manus-AutoDaily-[DATE]')
   ```

2. Work on the ONE task assigned to you
   - Follow implementation guidelines in ROADMAP_INDEX.md
   - Write clean, documented code
   - Test your work if applicable
   - Save all files to Google Drive

3. If you encounter a blocker:
   ```python
   manager.add_blocker(task_id, "Description of blocker", severity="high")
   ```
   Then move to the next available task

4. When complete:
   ```python
   manager.complete_task(task_id, actual_hours=X.X, notes="Brief completion note")
   ```

═══════════════════════════════════════════════════════════
STEP 4: CREATE SESSION DEBRIEF (MANDATORY)
═══════════════════════════════════════════════════════════

1. Use the debrief template: ROADMAP_V2/DEBRIEFS/debrief_template.md

2. Fill out ALL sections:
   - What was accomplished
   - Files modified/created
   - Challenges encountered
   - Key learnings
   - Next steps for next agent
   - System state

3. Save debrief as: debrief_[YYYYMMDD-HHMM].md

4. Upload debrief to: ROADMAP_V2/DEBRIEFS/

5. Log the session:
   ```python
   session_id = manager.log_session(
       agent_id='Manus-AutoDaily-[DATE]',
       phase=next_task['phase'],
       task_id=next_task['task_id'],
       duration_minutes=X,
       notes="Brief session summary",
       debrief_path="ROADMAP_V2/DEBRIEFS/debrief_[ID].md"
   )
   ```

═══════════════════════════════════════════════════════════
STEP 5: UPLOAD ALL CHANGES
═══════════════════════════════════════════════════════════

Upload to Google Drive:
1. Updated tracking_database.json → TRACKING/
2. Any new code files → appropriate location in brain
3. Session debrief → ROADMAP_V2/DEBRIEFS/
4. Any documentation updates

═══════════════════════════════════════════════════════════
CRITICAL RULES
═══════════════════════════════════════════════════════════

✓ ALWAYS load context first - never skip this
✓ Work on ONE task only per session
✓ ALWAYS create a debrief - this is non-negotiable
✓ Update tracking database after every change
✓ Upload everything to Google Drive
✓ If blocked, document it and move on
✓ Maximum 45 minutes of work
✓ Test your code before marking complete

✗ NEVER skip context loading
✗ NEVER work on multiple tasks at once
✗ NEVER end without a debrief
✗ NEVER leave uncommitted work
✗ NEVER duplicate work from previous sessions

═══════════════════════════════════════════════════════════

BEGIN YOUR DAILY DEVELOPMENT SESSION NOW.
```

---

## 🔧 CUSTOMIZATION VARIABLES

When creating a new brain cell, replace these variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `[BRAIN_NAME]` | Name of the brain cell | "Unwind Audio Brain" |
| `[brain_folder]` | Folder name in sandbox | "unwind_audio_brain" |
| `[BRAIN_PURPOSE]` | What this brain does | "Automated voiceover and music generation" |
| `[CORE_FUNCTIONALITY]` | Main features | "Text-to-speech, music selection, audio mixing" |
| `[INTEGRATIONS_NEEDED]` | External services | "ElevenLabs API, Spotify API, FFmpeg" |

---

## 📊 TYPICAL PHASE STRUCTURE

### Phase 0: System Setup (1-2 days)
- Create tracking database
- Initialize debrief system
- Configure scheduled task
- Test first automated session

### Phase 1: Foundation (1-2 weeks)
- Core functionality implementation
- Basic API integrations
- Initial testing
- Documentation

### Phase 2: Advanced Features (2-3 weeks)
- Complex integrations
- Optimization
- Error handling
- Advanced testing

### Phase 3: Enhancement (1-2 weeks)
- MCP integration
- Analytics
- Performance tuning
- User feedback implementation

### Phase 4: Full Automation (1-2 weeks)
- End-to-end pipeline
- Automated workflows
- Final testing
- Production deployment

---

## 🎨 EXAMPLE BRAIN CELLS

### Unwind Audio Brain
**Purpose:** Automated voiceover and music generation  
**Integrations:** ElevenLabs, Spotify, FFmpeg  
**Phases:**
1. Text-to-speech integration
2. Music selection and licensing
3. Audio mixing and mastering
4. Full audio pipeline automation

### Unwind Script Brain
**Purpose:** AI-powered script generation for videos  
**Integrations:** OpenAI, Claude, custom prompts  
**Phases:**
1. Script structure templates
2. Brand voice integration
3. Hook and CTA optimization
4. Multi-format script generation

### Unwind Analytics Brain
**Purpose:** Performance tracking and optimization  
**Integrations:** YouTube Analytics, TikTok API, Google Analytics  
**Phases:**
1. Data collection setup
2. Metrics dashboard
3. A/B testing framework
4. Automated reporting

### Unwind Asset Brain
**Purpose:** B-roll library management  
**Integrations:** Pexels, Pixabay, local storage  
**Phases:**
1. Multi-source asset search
2. Automated downloading
3. Categorization and tagging
4. Asset recommendation engine

### Unwind Render Brain
**Purpose:** Video assembly and export  
**Integrations:** FFmpeg, Adobe Media Encoder  
**Phases:**
1. Timeline assembly
2. Effects and transitions
3. Rendering optimization
4. Multi-format export

---

## 🚀 QUICK DEPLOYMENT CHECKLIST

When creating a new brain cell:

- [ ] Copy the Quick Start prompt
- [ ] Fill in [BRAIN_NAME] and purpose
- [ ] Define core functionality (3-5 items)
- [ ] List required integrations
- [ ] Submit prompt to AI agent
- [ ] Wait for initial setup (15-30 minutes)
- [ ] Review generated roadmap
- [ ] Approve scheduled task configuration
- [ ] Monitor first automated session
- [ ] Verify debrief creation

---

## 🔗 INTER-BRAIN COMMUNICATION

Brains can communicate with each other:

```python
# Example: Visual Cortex calling Audio Brain
from unwind_audio_brain import AudioBrain

audio_brain = AudioBrain()
voiceover = audio_brain.generate_voiceover(
    script=visual_cortex_script,
    voice_style=brand_voice,
    duration=video_duration
)
```

**Communication Protocol:**
1. Brain A generates request JSON
2. Request sent to Brain B's API endpoint
3. Brain B processes and returns result JSON
4. Brain A integrates result into workflow

---

## 📈 SUCCESS METRICS

Track these metrics for each brain cell:

**Development Velocity:**
- Tasks completed per week: Target 7-10
- Phase completion time: On track vs. delayed
- Blocker resolution time: <3 days

**System Health:**
- Debrief completion rate: 100%
- Task completion rate: >80%
- Integration test pass rate: >95%

**Code Quality:**
- Documentation coverage: 100%
- Error handling: Comprehensive
- Test coverage: >80%

---

## 🛠️ TROUBLESHOOTING

### Issue: Agent skips context loading
**Solution:** The prompt explicitly requires context loading first. Review the agent's first action and redirect if needed.

### Issue: Multiple tasks attempted in one session
**Solution:** Remind agent of the "ONE task only" rule. Update tracking database to reflect actual work done.

### Issue: No debrief created
**Solution:** Debrief is mandatory. Session is incomplete without it. Create debrief before proceeding.

### Issue: Tracking database not updated
**Solution:** Use tracking_manager.py utility functions. Never manually edit JSON.

### Issue: Files not uploaded to Google Drive
**Solution:** Verify rclone configuration. Re-upload missing files.

---

## 📚 RELATED DOCUMENTS

- `AGENT_COORDINATION_SYSTEM.md` - Detailed coordination rules
- `tracking_manager.py` - Python utility for database interaction
- `debrief_template.md` - Standard debrief format
- `ROADMAP_INDEX.md` - Phase and task definitions

---

## 🎓 BEST PRACTICES

1. **Always start with context loading** - This is non-negotiable
2. **One task per session** - Prevents conflicts and maintains focus
3. **Comprehensive debriefs** - Future agents depend on this
4. **Detailed logging** - Makes debugging easier
5. **Test before completing** - Catch issues early
6. **Document everything** - Knowledge transfer is critical
7. **Update tracking immediately** - Source of truth must be current
8. **Upload frequently** - Google Drive is persistent storage

---

## 🔄 VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-14 | Initial master prompt template created |

---

**Created by:** Manus AI  
**Based on:** Unwind Visual Cortex implementation  
**Status:** Production Ready

---

*This master prompt enables rapid deployment of new Unwind Brain cells with full multi-agent coordination, automated daily development, and perfect context handoff between sessions.*

# UNWIND VISUAL CORTEX - AI AGENT COORDINATION SYSTEM
## Multi-Agent Development & Tracking Architecture

**System Name:** Unwind Visual Cortex Development Coordination System  
**Version:** 1.0  
**Created:** January 9, 2026  
**Purpose:** Enable multiple AI agents to collaboratively develop the brain across sessions

---

## System Overview

This coordination system enables multiple AI agents to work on the Unwind Visual Cortex enhancement roadmap in a structured, coherent manner. Each agent can pick up where the previous one left off, maintain context, and contribute to the overall development without duplication or conflict.

---

## Architecture Components

### 1. **Google Sheets Tracking Database**
**Location:** `Unwind Code Brains/Unwind Visual Cortex/TRACKING/Development_Tracker.xlsx`

**Purpose:** Central source of truth for all development activities

**Sheets Structure:**

#### Sheet 1: MASTER_ROADMAP
Tracks overall progress across all phases

| Column | Description |
|--------|-------------|
| Phase_ID | Phase number (1-4) |
| Phase_Name | Name of the phase |
| Status | Not Started / In Progress / Completed / Blocked |
| Start_Date | When phase began |
| Target_Date | Expected completion |
| Completion_Date | Actual completion |
| Progress_Percent | 0-100% |
| Current_Task | What's being worked on now |
| Assigned_Agent | Last agent to work on this |
| Notes | Key insights or blockers |

#### Sheet 2: DAILY_SESSIONS
Logs every AI agent session

| Column | Description |
|--------|-------------|
| Session_ID | Unique identifier (YYYYMMDD-HHMM) |
| Date | Session date |
| Time | Session start time |
| Agent_ID | AI agent identifier |
| Phase_Worked_On | Which phase was addressed |
| Task_Completed | Specific task accomplished |
| Files_Modified | List of files changed |
| Duration_Minutes | How long the session took |
| Next_Steps | What should happen next |
| Blockers | Any issues encountered |
| Debrief_Link | Link to debrief document |

#### Sheet 3: TASK_QUEUE
Prioritized backlog of work items

| Column | Description |
|--------|-------------|
| Task_ID | Unique task identifier |
| Priority | Critical / High / Medium / Low |
| Phase | Which phase this belongs to |
| Task_Name | Short description |
| Task_Details | Full specification |
| Status | Queued / In Progress / Done / Blocked |
| Assigned_To | Agent working on it |
| Dependencies | What must be done first |
| Estimated_Hours | Time estimate |
| Actual_Hours | Time spent |
| Completion_Date | When finished |

#### Sheet 4: INTEGRATION_REGISTRY
Tracks all external integrations

| Column | Description |
|--------|-------------|
| Integration_Name | Tool/API/MCP name |
| Type | API / MCP Server / Library / Tool |
| Status | Planned / In Progress / Integrated / Tested |
| Priority | Critical / High / Medium / Low |
| Documentation_Link | Where to find docs |
| Code_Location | File path in brain |
| Test_Status | Pass / Fail / Not Tested |
| Notes | Implementation details |

#### Sheet 5: DEBRIEF_LOG
Session handoff summaries

| Column | Description |
|--------|-------------|
| Session_ID | Links to DAILY_SESSIONS |
| Agent_ID | Who wrote the debrief |
| Date | Debrief date |
| Summary | 2-3 sentence overview |
| Accomplishments | What was completed |
| Challenges | What was difficult |
| Learnings | Key insights |
| Next_Agent_Instructions | Clear handoff |
| Context_Files | Files to review |

---

### 2. **Session Debrief Protocol**

Every AI agent session MUST end with a structured debrief to maintain coherence.

**Debrief Template:**

```markdown
# SESSION DEBRIEF - [Session_ID]

**Date:** [YYYY-MM-DD]  
**Time:** [HH:MM AM/PM]  
**Agent ID:** [Agent identifier]  
**Phase:** [Phase number and name]  
**Duration:** [X minutes]

---

## What Was Accomplished

[Bullet list of completed tasks]

- Task 1
- Task 2
- Task 3

---

## Files Modified/Created

[List all files with brief description of changes]

- `file1.py` - Added Pexels API integration
- `file2.md` - Updated documentation
- `tracking_sheet` - Logged session data

---

## Challenges Encountered

[Any blockers, errors, or difficulties]

- Challenge 1: [Description and how it was resolved/not resolved]
- Challenge 2: [Description]

---

## Key Learnings & Insights

[Important discoveries or patterns]

- Learning 1
- Learning 2

---

## Next Steps (For Next Agent)

**Immediate Priority:**
[What should be done in the very next session]

**Context Required:**
[What files/docs the next agent should review first]

**Dependencies:**
[Anything that needs to happen before work can continue]

**Recommended Approach:**
[Suggested strategy or method]

---

## System State

**Current Phase Progress:** [X%]  
**Overall Roadmap Progress:** [Y%]  
**Blockers:** [None / List blockers]  
**Ready for Next Session:** [Yes / No - explain why]

---

## Agent Handoff Checklist

- [ ] Tracking sheet updated
- [ ] All code committed/saved
- [ ] Documentation updated
- [ ] Tests run (if applicable)
- [ ] Next steps clearly defined
- [ ] Context files identified
- [ ] Debrief uploaded to Drive

---

**Debrief File Location:** `ROADMAP_V2/DEBRIEFS/debrief_[Session_ID].md`
```

---

### 3. **Multi-Agent Coordination Rules**

#### Rule 1: Always Start with Context Loading
Every agent session MUST begin by:
1. Reading `ROADMAP_INDEX.md`
2. Checking `Development_Tracker.xlsx` (MASTER_ROADMAP sheet)
3. Reading the most recent debrief from `DEBRIEF_LOG`
4. Reviewing the `TASK_QUEUE` for next priority

#### Rule 2: Single Task Focus
Each session should focus on ONE clearly defined task from the queue. No task-switching mid-session.

#### Rule 3: Atomic Commits
All changes must be:
- Documented
- Tested (if code)
- Logged in tracking sheet
- Explained in debrief

#### Rule 4: Mandatory Debrief
No session ends without a complete debrief. This is non-negotiable for system coherence.

#### Rule 5: Conflict Resolution
If an agent encounters work that conflicts with previous sessions:
1. Document the conflict in debrief
2. Mark task as "Blocked" in tracking sheet
3. Propose resolution strategy
4. Do NOT proceed until resolved

---

### 4. **Daily Scheduled Task Configuration**

**Schedule:** Every day at 6:00 AM (user's timezone)  
**Task Type:** Recurring (cron)  
**Duration:** 30-45 minutes per session

**Task Prompt Template:**

```
You are an AI agent working on the Unwind Visual Cortex enhancement roadmap. This is an automated daily development session.

CONTEXT LOADING (REQUIRED):
1. Access Google Drive: "Unwind Code Brains/Unwind Visual Cortex/"
2. Read: ROADMAP_V2/ROADMAP_INDEX.md
3. Open tracking sheet: TRACKING/Development_Tracker.xlsx
4. Read latest debrief: ROADMAP_V2/DEBRIEFS/[most recent]

YOUR TASK:
1. Check TASK_QUEUE sheet for highest priority task marked "Queued"
2. Work on that ONE task for this session
3. Follow the implementation guidelines in ROADMAP_INDEX.md
4. Update tracking sheet as you progress
5. Create a session debrief when complete

DELIVERABLES:
- Updated code/documentation files
- Updated tracking sheet (DAILY_SESSIONS + TASK_QUEUE)
- Session debrief document
- Upload all changes to Google Drive

CONSTRAINTS:
- Focus on ONE task only
- Maximum 45 minutes of work
- If blocked, document and move to next task
- Always complete the debrief

CURRENT PHASE CONTEXT:
[This will be dynamically populated from tracking sheet]

BEGIN SESSION.
```

---

### 5. **Brain Expansion Architecture**

As the Unwind Visual Cortex grows, it will connect to multiple systems. This architecture supports that expansion.

#### Expansion Principles

**Modular Design:**
- Each integration is a separate module
- Modules communicate via standardized JSON
- Core brain remains unchanged

**Version Control:**
- All changes tracked in Git-style versioning
- Each module has its own version number
- Compatibility matrix maintained

**Inter-Brain Communication:**
- Unwind Visual Cortex can call other Unwind brains
- Standard API interface for brain-to-brain calls
- Shared knowledge base via Google Drive

#### Future Brain Connections

```
┌─────────────────────────────────────────────────────────┐
│           UNWIND VISUAL CORTEX (Core)                   │
│  - Brand Analysis                                        │
│  - Emotional Tone Mapping                                │
│  - Design Recommendations                                │
│  - Conversion Optimization                               │
└────────────┬────────────────────────────────────────────┘
             │
             ├─────► Unwind Audio Brain (voiceover, music)
             │
             ├─────► Unwind Script Brain (transcript generation)
             │
             ├─────► Unwind Analytics Brain (performance tracking)
             │
             ├─────► Unwind Asset Brain (B-roll library management)
             │
             └─────► Unwind Render Brain (video assembly & export)
```

**Connection Protocol:**
1. Brain A generates request JSON
2. Request routed through central coordinator
3. Brain B processes and returns result JSON
4. Brain A integrates result into workflow

---

## Implementation Checklist

### Setup Phase (One-Time)
- [ ] Create Google Sheets tracking database
- [ ] Set up ROADMAP_V2/DEBRIEFS/ folder
- [ ] Initialize TASK_QUEUE with Phase 1 tasks
- [ ] Configure daily scheduled task
- [ ] Test first automated session
- [ ] Document any setup issues

### Ongoing Operations
- [ ] Daily: Automated session runs at 6 AM
- [ ] Daily: Agent updates tracking sheet
- [ ] Daily: Agent creates debrief
- [ ] Weekly: Human review of progress
- [ ] Weekly: Adjust priorities if needed
- [ ] Monthly: System health check

---

## Success Metrics

**System Health Indicators:**
- Debrief completion rate: 100%
- Task completion rate: >80% of queued tasks
- Blocker resolution time: <3 days
- Context handoff quality: No duplicate work
- Integration test pass rate: >95%

**Development Velocity:**
- Tasks completed per week: Target 7-10
- Phase completion time: On track vs. delayed
- Code quality: No breaking changes
- Documentation coverage: 100% of new features

---

## Emergency Protocols

### If System Gets Stuck
1. Human intervention required
2. Review last 3 debriefs
3. Identify recurring blocker
4. Adjust task queue priorities
5. Provide explicit guidance to next agent

### If Tracking Sheet Corrupted
1. Restore from Google Drive version history
2. Reconstruct from debrief files
3. Mark all in-progress tasks as "Queued"
4. Resume from last known good state

### If Context Lost
1. Read ROADMAP_INDEX.md from scratch
2. Review last 5 debriefs
3. Check MASTER_ROADMAP for current phase
4. Start with small, safe task to rebuild context

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Jan 9, 2026 | Initial coordination system design |

---

**System Designer:** Manus AI  
**Brain Creator:** Jesus Casares, founder of Unwind Code  
**Status:** Ready for Implementation

---

*This coordination system ensures the Unwind Visual Cortex can be developed by multiple AI agents across many sessions while maintaining perfect coherence and avoiding conflicts.*

# Unwind Brain Quick Start Guide
## Spin Up a New Brain Cell in 5 Minutes

**Version:** 1.0  
**Created:** 2026-01-14  
**Purpose:** Step-by-step guide to create a new Unwind Brain cell with full automation

---

## 🎯 What You'll Get

By following this guide, you'll have:

✅ A fully structured brain cell with tracking system  
✅ Multi-agent coordination configured  
✅ Automated daily development sessions at 6:00 AM  
✅ Complete debrief and handoff system  
✅ Phase-based roadmap with task queue  
✅ Google Drive integration for persistence

**Time Required:** 5-10 minutes  
**Difficulty:** Easy (just copy and paste!)

---

## 📋 Prerequisites

Before you start, make sure you have:

- [ ] Google Drive access with "Unwind Code Brains" folder
- [ ] Manus AI with Google Drive integration enabled
- [ ] Basic understanding of what your brain cell should do

---

## 🚀 Method 1: Ultra-Quick (Copy-Paste Prompt)

**Best for:** When you just want to get started fast

### Step 1: Copy This Prompt

```
I need you to create a new Unwind Brain cell called "[YOUR_BRAIN_NAME]" with automated daily development sessions.

BRAIN PURPOSE: [What does this brain do? 1-2 sentences]

BRAIN LOCATION: Unwind Code Brains/[YOUR_BRAIN_NAME]/

CORE FUNCTIONALITY:
- [Feature 1 - be specific]
- [Feature 2 - be specific]
- [Feature 3 - be specific]

INTEGRATIONS NEEDED:
- [API/Service 1]
- [API/Service 2]

Use the Unwind Brain Master Prompt system from "Unwind Code Brains/Unwind Visual Cortex/UNWIND_BRAIN_MASTER_PROMPT.md" to set up:
1. Multi-agent coordination system
2. Tracking database
3. Daily automated sessions at 6:00 AM
4. Debrief system
5. Phase-based roadmap

START WITH: Initial setup and Phase 1 planning
```

### Step 2: Fill in the Blanks

Replace these placeholders:
- `[YOUR_BRAIN_NAME]` → e.g., "Unwind Audio Brain"
- `[What does this brain do?]` → e.g., "Automated voiceover and music generation for videos"
- `[Feature 1-3]` → e.g., "Text-to-speech with multiple voices"
- `[API/Service 1-2]` → e.g., "ElevenLabs API"

### Step 3: Send to Manus AI

Paste the filled prompt into Manus AI and wait 5-10 minutes for the setup to complete.

### Step 4: Done! 🎉

Your brain cell is now:
- Created on Google Drive
- Configured with tracking system
- Set up with daily automation
- Ready for first development session

---

## 🛠️ Method 2: Manual Setup (More Control)

**Best for:** When you want to customize the setup process

### Step 1: Define Your Brain

Create a specification document:

```markdown
# [Brain Name] Specification

## Purpose
[Detailed description of what this brain does]

## Core Functionality
1. [Feature 1 with details]
2. [Feature 2 with details]
3. [Feature 3 with details]

## Technical Requirements
- Programming Language: [Python/JavaScript/etc.]
- APIs/Services: [List all external dependencies]
- Data Storage: [Database/file system requirements]

## Integration Points
- Input: [What data/files does it receive?]
- Output: [What does it produce?]
- Dependencies: [Other brains it connects to]

## Success Criteria
- [Measurable goal 1]
- [Measurable goal 2]
```

### Step 2: Create Directory Structure

Ask Manus AI:

```
Create the directory structure for my new brain cell "[BRAIN_NAME]" following the Unwind Brain standard:

Unwind Code Brains/[BRAIN_NAME]/
├── TRACKING/
│   ├── tracking_database.json
│   ├── tracking_manager.py
├── ROADMAP_V2/
│   ├── AGENT_COORDINATION_SYSTEM.md
│   ├── ROADMAP_INDEX.md
│   ├── DEBRIEFS/
│   │   └── debrief_template.md
│   └── PHASES/
├── README.md
└── [brain_core_file].py

Use the templates from Unwind Visual Cortex as reference.
```

### Step 3: Generate Tracking Database

Ask Manus AI:

```
Generate the tracking_database.json for "[BRAIN_NAME]" with:
- System metadata
- Phase 0 (Setup) with 4 tasks
- Phase 1 (Foundation) with 5 tasks
- Empty session history
- System health monitoring

Base it on the structure from Unwind Visual Cortex.
```

### Step 4: Create Roadmap

Ask Manus AI:

```
Create a detailed roadmap for "[BRAIN_NAME]" with:
- 4-6 phases
- 5-7 tasks per phase
- Clear dependencies
- Time estimates
- Priority levels

Save as ROADMAP_INDEX.md
```

### Step 5: Configure Scheduled Task

Ask Manus AI:

```
Set up a daily scheduled task at 6:00 AM for "[BRAIN_NAME]" using the daily automated session prompt from the master template.

The task should:
1. Load context from Google Drive
2. Get next priority task
3. Execute task (30-45 min)
4. Create debrief
5. Upload changes
```

### Step 6: Test First Session

Ask Manus AI:

```
Run the first development session for "[BRAIN_NAME]" manually to verify:
- Context loading works
- Tracking system functions
- Task execution succeeds
- Debrief is created
- Files upload to Google Drive

Use SETUP-001 as the first task.
```

---

## 📝 Example: Creating "Unwind Audio Brain"

Here's a real example you can follow:

### The Prompt

```
I need you to create a new Unwind Brain cell called "Unwind Audio Brain" with automated daily development sessions.

BRAIN PURPOSE: Automated voiceover and music generation for video content. Converts scripts to natural-sounding speech and selects appropriate background music based on video mood and brand guidelines.

BRAIN LOCATION: Unwind Code Brains/Unwind Audio Brain/

CORE FUNCTIONALITY:
- Text-to-speech conversion with multiple voice options (ElevenLabs integration)
- Automatic music selection based on video mood and duration
- Audio mixing and mastering (normalize levels, add transitions)
- Multi-format export (MP3, WAV, AAC)
- Brand voice consistency across projects

INTEGRATIONS NEEDED:
- ElevenLabs API (text-to-speech)
- Spotify API or Epidemic Sound (music licensing)
- FFmpeg (audio processing)
- Google Drive (asset storage)

Use the Unwind Brain Master Prompt system from "Unwind Code Brains/Unwind Visual Cortex/UNWIND_BRAIN_MASTER_PROMPT.md" to set up:
1. Multi-agent coordination system
2. Tracking database
3. Daily automated sessions at 6:00 AM
4. Debrief system
5. Phase-based roadmap

START WITH: Initial setup and Phase 1 planning
```

### Expected Result

After 5-10 minutes, you'll have:

**Directory Structure:**
```
Unwind Code Brains/Unwind Audio Brain/
├── TRACKING/
│   ├── tracking_database.json
│   └── tracking_manager.py
├── ROADMAP_V2/
│   ├── AGENT_COORDINATION_SYSTEM.md
│   ├── ROADMAP_INDEX.md
│   ├── DEBRIEFS/
│   │   └── debrief_template.md
│   └── PHASES/
│       ├── PHASE_1_FOUNDATION.md
│       ├── PHASE_2_CORE_FEATURES.md
│       └── PHASE_3_INTEGRATION.md
├── README.md
└── audio_brain.py (placeholder)
```

**Roadmap:**
- **Phase 0:** System Setup (4 tasks)
- **Phase 1:** ElevenLabs Integration (5 tasks)
- **Phase 2:** Music Selection Engine (6 tasks)
- **Phase 3:** Audio Processing Pipeline (5 tasks)
- **Phase 4:** Full Automation (4 tasks)

**Scheduled Task:** Daily at 6:00 AM

---

## 🎨 More Examples

### Unwind Script Brain

```
I need you to create a new Unwind Brain cell called "Unwind Script Brain" with automated daily development sessions.

BRAIN PURPOSE: AI-powered script generation for video content. Creates engaging, brand-aligned scripts with optimized hooks, storytelling structure, and strong CTAs.

CORE FUNCTIONALITY:
- Script structure templates (hooks, body, CTA)
- Brand voice analysis and consistency
- A/B testing for different script variations
- Hook optimization for platform (YouTube, TikTok, Instagram)
- Automated script formatting for teleprompter

INTEGRATIONS NEEDED:
- OpenAI API (GPT-4)
- Anthropic Claude API
- Custom brand voice database
- Unwind Visual Cortex (for video context)

Use the Unwind Brain Master Prompt system...
```

### Unwind Analytics Brain

```
I need you to create a new Unwind Brain cell called "Unwind Analytics Brain" with automated daily development sessions.

BRAIN PURPOSE: Performance tracking and optimization for video content across platforms. Provides actionable insights and automated A/B testing recommendations.

CORE FUNCTIONALITY:
- Multi-platform data collection (YouTube, TikTok, Instagram)
- Performance metrics dashboard
- A/B testing framework
- Automated reporting (daily/weekly)
- Trend analysis and predictions

INTEGRATIONS NEEDED:
- YouTube Analytics API
- TikTok API
- Instagram Graph API
- Google Analytics
- Custom database (PostgreSQL)

Use the Unwind Brain Master Prompt system...
```

---

## ✅ Verification Checklist

After setup, verify these items:

- [ ] Google Drive folder created with correct structure
- [ ] `tracking_database.json` exists and is valid JSON
- [ ] `tracking_manager.py` is present
- [ ] `AGENT_COORDINATION_SYSTEM.md` is customized for your brain
- [ ] `ROADMAP_INDEX.md` has detailed phases and tasks
- [ ] `debrief_template.md` is in DEBRIEFS folder
- [ ] Scheduled task is configured for 6:00 AM
- [ ] First test session completes successfully
- [ ] Debrief is created and uploaded
- [ ] Tracking database updates correctly

---

## 🔧 Troubleshooting

### Issue: Setup takes longer than 10 minutes
**Solution:** This is normal for complex brains with many integrations. Wait up to 20 minutes.

### Issue: Tracking database not created
**Solution:** Check Google Drive permissions. Ensure the folder path is correct.

### Issue: Scheduled task not running
**Solution:** Verify the task is configured in Manus. Check the cron expression is correct (6:00 AM daily).

### Issue: First session fails
**Solution:** Review the error message. Common issues:
- Missing dependencies (install with pip)
- Incorrect file paths
- Google Drive connection issues

---

## 📚 Next Steps

After your brain cell is set up:

1. **Review the Roadmap:** Check `ROADMAP_INDEX.md` and adjust phases/tasks as needed
2. **Monitor First Week:** Watch the first 5-7 automated sessions to ensure smooth operation
3. **Customize as Needed:** Add brain-specific configuration files
4. **Connect to Other Brains:** Set up inter-brain communication if needed
5. **Document Learnings:** Update the roadmap based on what you discover

---

## 🎓 Best Practices

**DO:**
- Start with a clear, specific purpose
- List all integrations upfront
- Break functionality into small, testable features
- Review debriefs regularly
- Adjust roadmap based on learnings

**DON'T:**
- Try to build everything at once
- Skip the setup verification
- Ignore blockers or errors
- Forget to update tracking database
- Leave sessions incomplete

---

## 🔗 Related Resources

- **Master Prompt Template:** `UNWIND_BRAIN_MASTER_PROMPT.md`
- **Coordination System:** `AGENT_COORDINATION_SYSTEM.md`
- **Tracking Manager:** `tracking_manager.py`
- **Example Brain:** Unwind Visual Cortex (reference implementation)

---

## 💡 Pro Tips

1. **Start Simple:** Begin with core functionality, add advanced features later
2. **Use Mock Mode:** Test integrations in mock mode before connecting real APIs
3. **Document Everything:** Future agents depend on good documentation
4. **Monitor Progress:** Check tracking database weekly
5. **Iterate Quickly:** Small, frequent improvements beat big, rare updates

---

## 🆘 Need Help?

If you encounter issues:

1. Check the troubleshooting section above
2. Review the example implementations
3. Consult the master prompt template
4. Look at Unwind Visual Cortex for reference
5. Ask Manus AI for specific guidance

---

**Created by:** Manus AI  
**Last Updated:** 2026-01-14  
**Status:** Production Ready

---

*With this guide, you can create unlimited Unwind Brain cells, each with full automation and multi-agent coordination. Build your AI ecosystem one brain at a time!*

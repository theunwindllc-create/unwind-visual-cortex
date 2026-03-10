# AUTONOMOUS ASSEMBLY SOP: SCRIPT-TO-VIDEO PROTOCOL

**Author:** Unwind Code
**System:** Autonomous Video Assembly Engine (Phase 8)
**Purpose:** To define the step-by-step process for converting a Script Formula input into a final, rendered video file without human intervention.

---

## 1. Input Protocol: The Script Formula

The process begins with the **Script Formula**, a structured input file (JSON/YAML) containing all necessary variables.

### Protocol 1.1: Formula Validation
The system must validate the Formula before proceeding:
*   **Required Fields:** `avatar_id`, `topic_keywords`, `script_text` must be present.
*   **Tone Check:** `emotional_tone` must be one of the approved tones (e.g., Disciplined, Aspirational, Urgent).

## 2. Execution Protocol: The Three-Stage Pipeline

### Stage 2.1: Blueprint Generation (Intelligence)
1.  **Formula Parsing:** P8-T001 converts the Script Formula into the detailed **Unwind Blueprint** (internal JSON).
2.  **Strategic Tagging:** The existing intelligence agents (Brand Analyst, Sales Optimizer) enrich the Blueprint with CTA placements, brand color codes, and pacing markers.

### Stage 2.2: Parallel Asset Sourcing (Generation)
This stage executes two critical paths simultaneously:

| Path | Action | Tool/Integration | Output |
| :--- | :--- | :--- | :--- |
| **A: Avatar Performance** | Generate Avatar video and voiceover based on `script_text`. | MiniMax MCP (P3-T003, P8-T002) | `avatar_video.mp4`, `voiceover.mp3` |
| **B: B-Roll & Graphics** | Search and download B-roll based on `topic_keywords` and generate graphics based on Blueprint. | Pexels API (P1-T001), MiniMax MCP | `broll_assets/`, `graphics_assets/` |

### Stage 2.3: Autonomous Assembly (Execution)
This is the final, non-linear editing stage, executed by the Assembly Engine.

1.  **Track Initialization:** Initialize three primary tracks: Avatar, B-roll, and Graphics.
2.  **Avatar Placement:** Place `avatar_video.mp4` on the Avatar track.
3.  **B-Roll Sync (P8-T004):** The critical step. The system uses the `voiceover.mp3` timestamps to perfectly align B-roll cuts and transitions with the Avatar's speech rhythm and emotional tone markers.
4.  **Graphics Overlay:** Place graphics assets (lower thirds, text overlays) on the Graphics track according to the Blueprint's timing.
5.  **Final Render:** Execute the FFmpeg rendering command (P5-T002) to produce the final video file.

## 3. Output Protocol

The system outputs the following files to the designated project folder:
*   `final_video_[timestamp].mp4`
*   `unwind_blueprint_[timestamp].json`
*   `asset_manifest_[timestamp].txt` (list of all sourced assets)

**Next Action:** Update the master roadmap with Phase 8 tasks.

# AUTONOMOUS VIDEO ASSEMBLY ARCHITECTURE (PHASE 8)

**Goal:** To achieve true "Script-to-Video" autonomy, where the system takes a single **Script Formula** input and outputs a high-fidelity video file ready for final review and upload.

---

## 1. The Autonomous Assembly Pipeline: Avatar + Formula

The pipeline is defined by three stages, integrating the new Avatar and Script Formula concepts with the existing Unwind Brain architecture:

| Stage | Input | Core Process | Output |
| :--- | :--- | :--- | :--- |
| **1. Formula Ingestion** | **Script Formula** (JSON/YAML) + **Avatar ID** | The Creator OS's intelligence agents (Brand Analyst, Emotional Tone Expert) parse the formula into a detailed **Unwind Blueprint**. | **Unwind Blueprint** (Detailed JSON) |
| **2. Asset Generation & Sourcing** | **Unwind Blueprint** | **Parallel Execution:** 1. MiniMax MCP generates Avatar video/audio. 2. Pexels/MiniMax generates B-roll/graphics. | **Raw Assets** (Avatar Video, B-roll, Graphics, Voiceover) |
| **3. Autonomous Assembly** | **Raw Assets** + **Blueprint** | The new **Assembly Engine** (MoviePy/Editly) uses the Blueprint to automatically sequence, cut, apply transitions, and sync all assets. | **Draft Video File** (MP4/MOV) |

---

## 2. Integration of New Components

### A. The Script Formula (The New Input)
The Script Formula is a structured input that replaces the need for a full, traditional script. It contains the core variables needed for the AI to generate the final video:

| Field | Description | Source/Tool |
| :--- | :--- | :--- |
| `avatar_id` | Unique ID of the virtual presenter (e.g., "Invicta-V1"). | New Avatar Management System |
| `topic_keywords` | 3-5 keywords for B-roll and narrative focus. | Pexels/MiniMax Sourcing |
| `emotional_tone` | The desired feeling (e.g., "Disciplined," "Aspirational," "Urgent"). | Emotional Tone Expert |
| `cta_strategy` | The desired Call-to-Action (e.g., "Link in Bio," "Comment Below"). | Sales Optimizer |
| `script_text` | The raw text for the Avatar to speak. | MiniMax TTS/Avatar Lip-Sync |

### B. The Avatar Management System
This system is responsible for managing the virtual presenter assets and integrating them into the video.

*   **Function:** Stores and retrieves the Avatar's video assets, voice profile, and lip-sync parameters.
*   **Integration:** The **MiniMax MCP** (P3-T003) will be extended to handle the generation of the Avatar's performance based on the `script_text`.

### C. The Assembly Engine (Phase 4/5 Refinement)
The core of the autonomous process. This engine must be robust enough to handle the sequencing of the Avatar track, the B-roll track, and the graphics track simultaneously.

*   **Tools:** MoviePy/Editly (P5-T001) and FFmpeg (P5-T002).
*   **Process:** The engine reads the Unwind Blueprint's timeline data (cuts, transitions, effects) and executes the final video composition.

---

## 3. Proposed Future Tasks (Phase 8)

This new vision necessitates a dedicated phase to finalize the autonomous pipeline.

### Phase 8: Autonomous Video Assembly
**Objective:** Achieve true "Script-to-Video" autonomy by integrating the Avatar and Script Formula into the final rendering pipeline.

| Task ID | Task Name | Estimated Hours | Rationale |
| :--- | :--- | :--- | :--- |
| **P8-T001** | **Design Script Formula Parser** | 6 | Create a robust parser to convert the Script Formula input into the internal Unwind Blueprint JSON. |
| **P8-T002** | **Integrate Avatar Management System** | 8 | Build the module to manage Avatar assets and call the MiniMax MCP for video generation. |
| **P8-T003** | **Finalize Assembly Engine (MoviePy/Editly)** | 12 | Complete the P5-T001 task to fully implement the autonomous sequencing and cutting logic. |
| **P8-T004** | **Sync Avatar Track to B-Roll** | 10 | Develop the synchronization logic to perfectly match the Avatar's speech track with the B-roll cuts and transitions. |
| **P8-T005** | **End-to-End Autonomous Test** | 8 | Run a full test: Formula -> Avatar Gen -> Asset Sourcing -> Assembly -> Final Render. |

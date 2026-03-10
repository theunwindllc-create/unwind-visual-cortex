'''
# Unwind Brain Scaffolding System

**Version:** 1.0  
**Date:** 2026-01-14  
**Author: Unwind CodeAI

## 1. Overview

This document outlines the **Unwind Brain Scaffolding System**, a comprehensive solution for rapidly creating and deploying new "brain cells" within the Unwind ecosystem. The system is built upon the successful multi-agent coordination protocol developed for the Unwind Visual Cortex project.

Its primary purpose is to **standardize and automate** the setup of new AI development projects, ensuring that every brain cell adheres to the same principles of automated daily development, context handoff, and progress tracking.

## 2. Core Components

The system consists of three main components:

### 2.1. Master Prompt Template (`UNWIND_BRAIN_MASTER_PROMPT.md`)

This is the heart of the system. It's a comprehensive, reusable prompt that contains the complete instructions for an AI agent to build and manage a new brain cell. It includes:

-   **Quick Start Prompt:** A simple, fill-in-the-blanks template for users to initiate a new brain.
-   **System Architecture:** A standardized directory structure for all brain cells.
-   **Automated Setup Phases:** A step-by-step guide for the AI to create the tracking database, coordination files, and roadmap.
-   **Daily Session Prompt:** The exact prompt that runs every morning to guide the daily development work.
-   **Customization Guide:** Instructions on how to adapt the template for different types of brains.

### 2.2. Quick Start Guide (`UNWIND_BRAIN_QUICK_START_GUIDE.md`)

This user-facing guide provides two clear methods for creating a new brain cell:

1.  **Ultra-Quick Method:** A simple copy-paste prompt for immediate setup.
2.  **Manual Method:** A more detailed, step-by-step process for users who want more control over the setup.

It includes real-world examples, a verification checklist, and troubleshooting tips.

### 2.3. Scaffolding Script (`unwind_brain_scaffolder.py`)

This Python script automates the entire setup process. When executed, it:

-   Creates the complete Google Drive directory structure.
-   Generates a new `tracking_database.json` from a template.
-   Copies and customizes the `tracking_manager.py` utility.
-   Generates all necessary coordination documents (`AGENT_COORDINATION_SYSTEM.md`, `debrief_template.md`, etc.).
-   Initializes a `ROADMAP_INDEX.md` and `README.md`.

This script is designed to be executed by the AI agent when a user submits the "Quick Start" prompt.

## 3. How It Works: The Workflow

1.  **Initiation:** The user fills out the "Quick Start" prompt from the `UNWIND_BRAIN_QUICK_START_GUIDE.md` and submits it to Manus AI.

2.  **Scaffolding:** The AI agent uses the `unwind_brain_scaffolder.py` script to automatically create the entire project structure, tracking database, and coordination files in the specified Google Drive location.

3.  **Roadmap Generation:** The agent then generates a detailed, phase-based roadmap for the new brain cell, breaking down the required functionality into a prioritized task queue.

4.  **Scheduling:** A daily recurring task is scheduled for 6:00 AM, using the standardized "Daily Automated Session Prompt" from the master template.

5.  **Execution:** Every day, an AI agent is instantiated to:
    a.  **Load Context:** Read the tracking database and the latest debrief.
    b.  **Get Task:** Identify the next priority task from the queue.
    c.  **Execute:** Work on the single task for 30-45 minutes.
    d.  **Debrief:** Create a detailed debrief of the session.
    e.  **Upload:** Save all changes and the new debrief to Google Drive.

6.  **Handoff:** The system is now ready for the next agent on the following day, ensuring perfect context and continuity.

## 4. Key Benefits

-   **Standardization:** Every brain cell follows the same structure, making them easy to manage and understand.
-   **Speed:** A new, fully-configured brain cell can be created in under 10 minutes.
-   **Automation:** Daily development sessions run automatically, ensuring consistent progress.
-   **Coherence:** The debrief and tracking system guarantees perfect context handoff between AI agents.
-   **Scalability:** The system is designed to manage an entire ecosystem of interconnected brain cells.
-   **Reliability:** Based on the proven, battle-tested protocol from the Unwind Visual Cortex project.

## 5. Deliverables

This project has produced the following key assets:

-   **Master Prompt Template:** `UNWIND_BRAIN_MASTER_PROMPT.md`
-   **Quick Start Guide:** `UNWIND_BRAIN_QUICK_START_GUIDE.md`
-   **Scaffolding Script:** `unwind_brain_scaffolder.py`

These files provide everything needed to create and manage new Unwind Brain cells efficiently and effectively.
'''''

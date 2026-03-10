# PHASE 3: ENHANCED INTELLIGENCE - IMPLEMENTATION INSTRUCTIONS

**Phase Objective:** Transition from a structural automation system to a data-driven intelligence engine. This phase focuses on competitive analysis, performance tracking, and AI-powered asset generation using the Model Context Protocol (MCP) ecosystem.

---

## 📋 Phase 3 Task List

| Task ID | Task Name | Description | Priority |
| :--- | :--- | :--- | :--- |
| **P3-T001** | **Firecrawl MCP Integration** | Implement web scraping for competitive video analysis and trend detection. | Critical |
| **P3-T002** | **Supabase MCP Integration** | Set up a database for tracking video performance metrics and blueprint history. | Critical |
| **P3-T003** | **MiniMax MCP Integration** | Integrate AI asset generation for text-to-speech, custom images, and video clips. | High |
| **P3-T004** | **Competitive Analysis Module** | Build a Python module to analyze competitor videos using Firecrawl data. | High |
| **P3-T005** | **Performance Prediction Model** | Create a basic ML model to predict video success based on historical data. | Medium |
| **P3-T006** | **CLIP Intelligent Matching** | Implement OpenAI CLIP for semantic matching between script and B-roll. | Medium |
| **P3-T007** | **Phase 3 Validation & Debrief** | Conduct full system validation and document the intelligence enhancements. | Low |

---

## 🛠️ Detailed Implementation Instructions

### 1. Firecrawl MCP Integration (P3-T001)
*   **Goal:** Enable the system to "see" what is working on social platforms.
*   **Steps:**
    1.  Configure the `firecrawl` MCP server in the environment.
    2.  Create a Python wrapper `competitive_research.py`.
    3.  Implement functions to scrape YouTube/TikTok/Instagram metadata (views, likes, comments, hashtags).
    4.  Develop a "Trend Scraper" that identifies viral visual styles and audio tracks in specific niches.

### 2. Supabase MCP Integration (P3-T002)
*   **Goal:** Create a "memory" for the system to learn from past projects.
*   **Steps:**
    1.  Initialize a Supabase project and configure the `supabase` MCP server.
    2.  Design a schema for `blueprints`, `projects`, and `performance_metrics`.
    3.  Implement a "Sync" function in `tracking_manager.py` to backup the local JSON database to Supabase.
    4.  Create an API to query historical performance data for the prediction model.

### 3. MiniMax MCP Integration (P3-T003)
*   **Goal:** Fill gaps in stock footage with custom AI-generated assets.
*   **Steps:**
    1.  Configure the `minimax` MCP server.
    2.  Create an `asset_generator.py` module.
    3.  Implement `generate_voiceover(text, voice_id)` for automated narration.
    4.  Implement `generate_broll_clip(prompt)` for cases where Pexels lacks specific footage.

### 4. Competitive Analysis Module (P3-T004)
*   **Goal:** Turn raw scraped data into actionable editing recommendations.
*   **Steps:**
    1.  Build a logic engine that compares a new transcript against top-performing competitor videos.
    2.  Generate a "Competitive Edge" section in the Unwind Blueprint.
    3.  Recommend specific "Hook" styles based on current viral trends.

### 5. Performance Prediction Model (P3-T005)
*   **Goal:** Score a blueprint's potential success before production begins.
*   **Steps:**
    1.  Use historical data from Supabase to identify correlations between blueprint features and engagement.
    2.  Implement a simple scoring algorithm (0-100) for "Virality Potential."
    3.  Provide suggestions to improve the score (e.g., "Increase CTA frequency," "Shorten intro").

---

## 📈 Success Criteria for Phase 3
1.  **Data-Driven Blueprints:** Every blueprint includes a "Competitive Analysis" section derived from live web data.
2.  **Asset Diversity:** The system can provide a mix of stock footage (Pexels) and AI-generated assets (MiniMax).
3.  **Performance Memory:** All project data is stored in Supabase, allowing for cross-session learning.
4.  **Automated Research:** Competitive research that previously took 2 hours is completed in under 5 minutes.

---

## 🔗 Reference Documentation
*   [Firecrawl MCP Documentation](https://mcpservers.org/servers/github-com-firecrawl-firecrawl-mcp-server)
*   [Supabase MCP Documentation](https://mcpservers.org/servers/supabase-community/supabase-mcp)
*   [MiniMax MCP Documentation](https://mcpservers.org/servers/github-com-minimax-ai-minimax-mcp)
*   [Unwind Visual Cortex Roadmap Index](./ROADMAP_INDEX.md)

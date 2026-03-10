# Unwind Visual Cortex - Tool Enhancement Research Notes

## Adobe Integration Findings

### After Effects JSON Data-Driven Animation
**Source:** Adobe Official Documentation

**Key Capabilities:**
- After Effects natively supports importing standard JSON files as footage
- JSON data can drive animations through expressions
- Data is referenced using `sourceData` attribute in expressions
- Example: `var sampleData = footage("sample.json").sourceData;`
- JSON files can be replaced dynamically to change data being referenced
- Supports all standard JSON data types (Number, String, Boolean, Array, Object, Null)

**Workflow:**
1. Import JSON file: File > Import > File
2. Add JSON to composition
3. Create layers (solids, text, shapes)
4. Use expressions to reference JSON data
5. Expressions can access nested properties: `myData.engineData.RPM`

**Critical Note:** If using Adobe Media Encoder or linking to Premiere Pro, add the data source file to the Timeline rather than just using expressions.

### Adobe Premiere Pro API
**Source:** Adobe Developer Documentation

**Key Technologies:**
- **UXP (Unified Extensibility Platform)** - Modern API for Premiere Pro plugins
- **ExtendScript** - Legacy scripting (deprecated but still functional)
- **CEP (Common Extensibility Platform)** - HTML/CSS/JS panels

**Capabilities:**
- Automate complex tasks
- Communicate with external hardware
- Add support for new file formats
- Create custom panels and workflows
- Seamless tool integration

### Pexels API for B-Roll Sourcing
**Source:** Pexels API Documentation

**Key Features:**
- Free stock video and photo API
- RESTful JSON API
- Video search endpoint: `https://api.pexels.com/videos/search`
- Photo search endpoint: `https://api.pexels.com/v1/search`
- Rate limit: 200 requests per hour (free tier), can request higher limits
- Requires API key (instant approval)
- Returns video metadata including multiple quality URLs
- Pagination support (up to 80 results per page)

**Authentication:**
```bash
curl -H "Authorization: YOUR_API_KEY" \
  "https://api.pexels.com/videos/search?query=business meeting"
```

---

## Capability Gap Analysis

### Current Unwind Visual Cortex Capabilities
1. ✅ Brand compliance analysis
2. ✅ Emotional tone mapping
3. ✅ B-roll shot list generation (descriptions only)
4. ✅ Motion graphics recommendations
5. ✅ Platform-specific optimization
6. ✅ CTA strategy and conversion optimization
7. ✅ JSON blueprint output

### Identified Gaps
1. ❌ **B-roll asset sourcing** - Recommendations exist but no actual video files
2. ❌ **Direct Adobe integration** - JSON output not formatted for After Effects/Premiere
3. ❌ **Automated project file generation** - No .aep or .prproj creation
4. ❌ **Real-time trend data** - Platform trends are static, not live
5. ❌ **Performance prediction** - No ML model for success prediction
6. ❌ **Competitive analysis** - No competitor video analysis
7. ❌ **Multi-language support** - English-only transcript analysis
8. ❌ **Video generation** - No actual video rendering capability

---

## Recommended Tool Integrations

### Priority 1: Essential Integrations

#### 1. Pexels Video API
**Purpose:** Automated B-roll sourcing
**Implementation:** Python integration to search and download B-roll clips based on shot list
**Benefit:** Transforms abstract B-roll recommendations into actual downloadable video assets

#### 2. After Effects JSON Bridge
**Purpose:** Export Unwind blueprints as AE-compatible JSON
**Implementation:** Reformat output JSON to match AE data-driven animation schema
**Benefit:** Direct import of timing, text overlays, and motion graphics data into AE

#### 3. Adobe UXP/ExtendScript Integration
**Purpose:** Generate Premiere Pro project files programmatically
**Implementation:** Python script that generates .prproj XML or uses ExtendScript API
**Benefit:** Auto-create Premiere timelines with markers, B-roll placeholders, and CTA positions

### Priority 2: Enhanced Capabilities

#### 4. YouTube Data API
**Purpose:** Competitive analysis and trend detection
**Implementation:** Analyze top-performing videos in target niche
**Benefit:** Data-driven recommendations based on actual platform performance

#### 5. TikTok/Instagram Graph APIs
**Purpose:** Real-time trend integration
**Implementation:** Fetch trending audio, hashtags, and visual styles
**Benefit:** Keep recommendations current with platform trends

#### 6. OpenAI Vision API (GPT-4 Vision)
**Purpose:** Analyze competitor videos and style references
**Implementation:** Upload reference videos/screenshots for visual analysis
**Benefit:** "Make it look like this" capability for style matching

### Priority 3: Advanced Automation

#### 7. Remotion (React-based video generation)
**Purpose:** Programmatic video rendering
**Implementation:** Convert JSON blueprints to Remotion compositions
**Benefit:** End-to-end automation from transcript to rendered video

#### 8. FFmpeg Integration
**Purpose:** Video processing and assembly
**Implementation:** Automated B-roll cutting, color grading, and export
**Benefit:** Batch processing and format conversion

#### 9. Runway ML API
**Purpose:** AI-powered video effects and generation
**Implementation:** Generate custom B-roll when stock footage insufficient
**Benefit:** Unlimited creative assets without licensing concerns

---

## MCP Server Recommendations

### Existing MCP Servers to Consider

#### 1. Playwright MCP (Already Configured)
**Use Case:** Web scraping for competitor analysis
**Application:** Scrape viral videos, analyze thumbnails, extract engagement metrics

#### 2. ClickUp MCP (Already Configured)
**Use Case:** Project management integration
**Application:** Create tasks for each video project, assign B-roll sourcing, track revisions

#### 3. Gmail MCP (Already Configured)
**Use Case:** Client communication automation
**Application:** Send video blueprints, request approvals, deliver final assets

### Recommended New MCP Servers

#### 4. GitHub MCP
**Use Case:** Version control for video projects
**Application:** Store blueprints, track iterations, collaborate on scripts

#### 5. Airtable/Notion MCP
**Use Case:** Content calendar and asset library
**Application:** Track video performance, organize B-roll library, manage brand guidelines

#### 6. Slack MCP
**Use Case:** Team collaboration
**Application:** Notify team when blueprints ready, share feedback, coordinate revisions

---

## GitHub Tools and Libraries

### Video Editing Automation

#### 1. **Editly** (mifi/editly)
- Declarative command-line video editing
- JSON-based configuration
- Supports clips, images, audio, titles, transitions
- Perfect for programmatic video assembly
- **Integration Path:** Convert Unwind blueprint → Editly JSON → Rendered video

#### 2. **Ved** (ved-editor/ved)
- Video editing framework for algorithmic editing
- Python-based
- Machine learning integration support
- **Integration Path:** Use for advanced automation and ML-driven editing decisions

#### 3. **MoviePy** (Zulko/moviepy)
- Python video editing library
- Programmatic control over video composition
- Supports effects, transitions, text overlays
- **Integration Path:** Build custom video assembly pipeline

#### 4. **After Effects Automation** (jhd3197/after-effects-automation)
- Python tool for automating AE compositions
- Render automation
- **Integration Path:** Generate and render AE projects from Unwind blueprints

### Stock Footage Integration

#### 5. **Pexels Python Client** (pexels-api-py)
- Official/community Python wrapper for Pexels API
- Simplified video search and download
- **Integration Path:** Auto-download B-roll based on shot list descriptions

#### 6. **Pixabay API Client**
- Alternative free stock footage source
- Similar to Pexels with different content library
- **Integration Path:** Fallback when Pexels doesn't have suitable footage

### AI and ML Enhancement

#### 7. **Whisper** (OpenAI)
- Speech-to-text for transcript generation
- Multi-language support
- **Integration Path:** Auto-generate transcripts from raw video files

#### 8. **CLIP** (OpenAI)
- Image/video understanding
- Match B-roll to semantic descriptions
- **Integration Path:** Intelligent B-roll selection based on visual similarity

---

## Proposed Architecture Enhancement

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INPUT                                │
│  (Transcript + Brand Guidelines + Platform + Goal)           │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│              UNWIND VISUAL CORTEX (Core)                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Brand   │→ │ Emotional│→ │  Design  │→ │  Sales   │   │
│  │ Analyst  │  │   Tone   │  │Specialist│  │Optimizer │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ JSON BLUEPRINT│
                  └───────┬───────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   B-ROLL     │  │  ADOBE AE    │  │  PREMIERE    │
│  SOURCING    │  │  JSON EXPORT │  │  PROJECT GEN │
│              │  │              │  │              │
│ • Pexels API │  │ • Data-driven│  │ • UXP/Script │
│ • Pixabay    │  │   animation  │  │ • Markers    │
│ • CLIP match │  │ • Text layers│  │ • Sequences  │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────┐
│                  DELIVERABLES                                │
│  • Human-readable report (MD)                                │
│  • Technical blueprint (JSON)                                │
│  • Downloaded B-roll clips (MP4)                             │
│  • After Effects project (.aep)                              │
│  • Premiere Pro project (.prproj)                            │
│  • (Optional) Rendered preview video                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Next Steps for Implementation

### Phase 1: Foundation (Week 1-2)
1. Integrate Pexels API for B-roll sourcing
2. Create After Effects JSON export module
3. Test data-driven animation workflow

### Phase 2: Adobe Integration (Week 3-4)
4. Build Premiere Pro project generator (UXP/ExtendScript)
5. Create marker system for CTA placements
6. Develop sequence template system

### Phase 3: Enhanced Intelligence (Week 5-6)
7. Add YouTube API for competitive analysis
8. Implement CLIP for intelligent B-roll matching
9. Build performance prediction model

### Phase 4: Full Automation (Week 7-8)
10. Integrate Editly or MoviePy for video assembly
11. Create end-to-end pipeline: Transcript → Rendered Video
12. Build web interface for non-technical users

---

## Estimated ROI

### Time Savings
- **Manual B-roll sourcing:** 2-3 hours → 5 minutes (automated)
- **Project setup in Premiere:** 30-45 minutes → 2 minutes (automated)
- **After Effects text animation:** 1-2 hours → 10 minutes (data-driven)
- **Total per video:** 4-6 hours → 30-45 minutes

### Cost Savings
- **Stock footage subscriptions:** $200-500/month → Free (Pexels/Pixabay)
- **Junior editor time:** $25-50/hour × 4 hours = $100-200/video → $0 (automated)

### Quality Improvements
- **Brand consistency:** Manual (variable) → 100% compliant (AI-enforced)
- **Platform optimization:** Best guess → Data-driven (API insights)
- **Conversion optimization:** Ad-hoc → Systematic (psychological triggers)

---

*Research compiled: January 9, 2026*
*Next update: After Phase 1 implementation*


---

## MCP Server Ecosystem Analysis

### Already Configured (User's Current Setup)
1. **Playwright MCP** - Browser automation (official)
2. **ClickUp MCP** - Project management
3. **Gmail MCP** - Email communication

### Highly Relevant MCP Servers for Video Editing

#### Content Research & Competitive Analysis
- **Firecrawl MCP** (Official) - Web scraping for competitor video analysis
- **Exa MCP** (Official) - AI-powered search engine for trend research
- **Browserbase MCP** (Official) - Cloud browser automation for platform research

#### Media & Creative Tools
- **MiniMax MCP** (Official) - Text-to-Speech, image, and video generation APIs
  - **Use Case:** Generate voiceovers, create custom B-roll, produce motion graphics
  - **Integration:** Could generate assets directly from Unwind Visual Cortex recommendations

#### Data & Analytics
- **Kaggle MCP** (Official) - Access to datasets for ML model training
  - **Use Case:** Train performance prediction models on video engagement data
- **Alpha Vantage MCP** - Financial market data (if creating finance-related content)

#### Development & Automation
- **E2B MCP** (Official) - Secure code sandboxes
  - **Use Case:** Test video generation scripts safely
- **Chrome DevTools MCP** (Official) - Browser inspection and control
  - **Use Case:** Scrape platform-specific design trends from TikTok/Instagram/YouTube

#### Cloud & Storage
- **Cloudflare MCP** (Official) - Deploy and manage cloud resources
  - **Use Case:** Host video assets, CDN for B-roll library
- **Supabase MCP** (Official) - Database, auth, edge functions
  - **Use Case:** Store video blueprints, track performance metrics, manage asset library

### Recommended MCP Servers to Add

#### Priority 1: Immediate Value
1. **MiniMax MCP** - For AI-generated media assets
2. **Firecrawl MCP** - For competitive analysis and trend scraping
3. **Supabase MCP** - For blueprint storage and performance tracking

#### Priority 2: Enhanced Capabilities
4. **Browserbase MCP** - For automated platform research
5. **E2B MCP** - For safe script execution
6. **Kaggle MCP** - For ML model training data

### Custom MCP Server Opportunities

#### 1. Pexels/Pixabay MCP Server
**Purpose:** Unified stock footage search and download
**Tools:** 
- `search_videos(query, orientation, size)`
- `download_video(video_id, quality)`
- `get_video_metadata(video_id)`

#### 2. Adobe Creative Cloud MCP Server
**Purpose:** Bridge to Premiere Pro and After Effects
**Tools:**
- `create_premiere_project(blueprint_json)`
- `add_markers(timeline, cta_positions)`
- `export_ae_json(motion_graphics_plan)`
- `render_composition(project_path, output_format)`

#### 3. Video Analytics MCP Server
**Purpose:** Fetch performance data from platforms
**Tools:**
- `get_youtube_analytics(video_id)`
- `get_tiktok_metrics(video_url)`
- `get_instagram_insights(reel_id)`
- `compare_performance(video_ids[])`

#### 4. Trend Intelligence MCP Server
**Purpose:** Real-time platform trend detection
**Tools:**
- `get_trending_audio(platform, region)`
- `get_trending_hashtags(platform, niche)`
- `get_viral_formats(platform, timeframe)`
- `analyze_competitor_videos(channel_url)`

---

## Integration Architecture with MCP

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INPUT                                │
│  (Transcript + Brand Guidelines + Platform + Goal)           │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│         UNWIND VISUAL CORTEX (Core Analysis)                 │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Brand   │→ │ Emotional│→ │  Design  │→ │  Sales   │   │
│  │ Analyst  │  │   Tone   │  │Specialist│  │Optimizer │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
                  ┌───────────────┐
                  │ JSON BLUEPRINT│
                  └───────┬───────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ MCP SERVERS  │  │   ADOBE      │  │   STORAGE    │
│              │  │ INTEGRATION  │  │              │
│ • MiniMax    │  │              │  │ • Supabase   │
│   (Assets)   │  │ • AE JSON    │  │   (Database) │
│              │  │ • Premiere   │  │              │
│ • Firecrawl  │  │   Project    │  │ • Cloudflare │
│   (Research) │  │              │  │   (CDN)      │
│              │  │ • Markers    │  │              │
│ • Pexels MCP │  │ • Render     │  │ • ClickUp    │
│   (B-roll)   │  │              │  │   (Tasks)    │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                  FINAL DELIVERABLES                          │
│  • Human-readable report (MD)                                │
│  • Technical blueprint (JSON)                                │
│  • Downloaded B-roll clips (MP4) [via Pexels MCP]           │
│  • AI-generated assets (MP4/PNG) [via MiniMax MCP]          │
│  • After Effects project (.aep) [via Adobe Integration]     │
│  • Premiere Pro project (.prproj) [via Adobe Integration]   │
│  • Performance tracking dashboard [via Supabase MCP]        │
│  • Project tasks and timeline [via ClickUp MCP]             │
└─────────────────────────────────────────────────────────────┘
```

---

## Competitive Advantage Analysis

### Current State (Without Integrations)
- **Output:** JSON blueprint + Markdown report
- **Manual Steps Required:**
  1. Read blueprint
  2. Search for B-roll manually
  3. Download assets manually
  4. Open Premiere/AE manually
  5. Create project structure manually
  6. Import assets manually
  7. Add markers manually
  8. Apply recommendations manually
- **Time:** 4-6 hours per video
- **Error Rate:** High (human interpretation of recommendations)

### Enhanced State (With Integrations)
- **Output:** Complete production-ready package
- **Automated Steps:**
  1. Blueprint generated automatically ✅
  2. B-roll sourced and downloaded automatically ✅ (Pexels MCP)
  3. Assets generated automatically ✅ (MiniMax MCP)
  4. Premiere project created automatically ✅ (Adobe Integration)
  5. AE compositions created automatically ✅ (Adobe Integration)
  6. Markers placed automatically ✅ (Adobe Integration)
  7. Tasks created automatically ✅ (ClickUp MCP)
  8. Performance tracked automatically ✅ (Supabase MCP)
- **Time:** 30-45 minutes per video
- **Error Rate:** Low (direct API-to-API communication)

### Market Differentiation
**Competitors:**
- **Descript:** Video editing with AI transcription (no strategic intelligence)
- **Runway ML:** AI video generation (no editing intelligence)
- **Opus Clip:** AI video clipping (no brand/conversion optimization)
- **Pictory:** Text-to-video (limited customization)

**Unwind Visual Cortex Advantage:**
- ✅ Multi-agent strategic analysis
- ✅ Brand compliance enforcement
- ✅ Platform-specific optimization
- ✅ Conversion psychology integration
- ✅ Direct Adobe workflow integration
- ✅ End-to-end automation
- ✅ Performance tracking and learning

---

*Research updated: January 9, 2026*
*Next phase: Prioritize and implement top 3 integrations*

# MCP TOOLS RESEARCH: UNWIND BRAIN IMPLEMENTATION

**Research Date:** January 17, 2026
**Purpose:** Identify available MCP servers and tools for implementing the Unwind Brain system

---

## 1. Official MCP SDKs Available

| SDK | Language | Use Case |
| :--- | :--- | :--- |
| TypeScript MCP SDK | TypeScript/Node.js | Primary for UXP plugin integration |
| Python MCP SDK | Python | Core brain logic and ML modules |
| Go MCP SDK | Go | High-performance processing |
| Rust MCP SDK | Rust | Low-level video processing |

---

## 2. Reference Servers (Official)

| Server | Function | Unwind Integration |
| :--- | :--- | :--- |
| **Fetch** | Web content fetching and conversion | Firecrawl alternative for scraping |
| **Filesystem** | Secure file operations | Asset management |
| **Git** | Git repository manipulation | Code versioning |
| **Memory** | Knowledge graph-based persistent memory | Brain memory system |
| **Sequential Thinking** | Dynamic problem-solving | Conscious Evolution Engine |
| **Time** | Time and timezone conversion | Scheduling |

---

## 3. Critical Third-Party MCP Servers for Unwind Brain

### Video Generation & Editing
| Server | Function | Phase Integration |
| :--- | :--- | :--- |
| **mcp-veo2** | Google VEO2 video generation | P8: Avatar Generation |
| **video-editing-mcp** | Video Jungle API for editing | P8: Assembly Engine |
| **Invideo MCP** | AI script-to-video generation | P8: Autonomous Assembly |
| **RunwayML MCP** | AI video generation | P8: B-roll Generation |
| **Luma AI MCP** | Visual storytelling | P8: Graphics Generation |
| **ElevenLabs** | Voice synthesis and cloning | P8: Avatar Voice |
| **HeyGen** | AI avatar video generation | P8: Avatar System |

### Social Media & Distribution
| Server | Function | Phase Integration |
| :--- | :--- | :--- |
| **YouTube MCP** | YouTube API integration | P9: Distribution |
| **Instagram MCP** | Instagram Graph API | P9: Distribution |
| **TikTok MCP** | TikTok API integration | P9: Distribution |
| **Oktopost MCP** | Social media workflows | P9: Distribution |
| **Buffer MCP** | Social media scheduling | P9: Distribution |

### AI & Intelligence
| Server | Function | Phase Integration |
| :--- | :--- | :--- |
| **OpenAI MCP** | GPT integration | P11: Narrative Principle Engine |
| **Anthropic MCP** | Claude integration | P11: Conscious Tone Synthesis |
| **Google Gemini** | Multimodal AI | P10: Kinetic Analysis |
| **Perplexity MCP** | Research and analysis | P3: Competitive Intelligence |

### Data & Analytics
| Server | Function | Phase Integration |
| :--- | :--- | :--- |
| **Supabase MCP** | Database and auth | P3: Performance Tracking |
| **PostgreSQL MCP** | Database access | P3: Blueprint Storage |
| **Amplitude MCP** | Product analytics | P9: Performance Metrics |

### CRM & Sales
| Server | Function | Phase Integration |
| :--- | :--- | :--- |
| **HubSpot MCP** | CRM integration | P9: Lead Management |
| **Salesforce MCP** | Enterprise CRM | P9: Sales Funnel |
| **Pipedrive MCP** | Sales pipeline | P9: Prospecting |

### Automation & Workflows
| Server | Function | Phase Integration |
| :--- | :--- | :--- |
| **Puppeteer MCP** | Browser automation | P3: Web Scraping |
| **Playwright MCP** | Browser automation | P3: Competitive Analysis |
| **n8n MCP** | Workflow automation | P9: Distribution Automation |
| **Zapier MCP** | Integration automation | P9: Cross-platform Sync |

---

## 4. Google AI Studio / Gemini Integration

### Available Capabilities
- **Gemini 2.5 Flash** - Fast multimodal processing
- **Gemini Pro** - Advanced reasoning
- **Veo 2** - Video generation from text/images
- **Imagen 3** - Image generation
- **Code Assist** - Code generation and debugging

### Integration Points
- Use Gemini for Narrative Principle Engine (P11-T001)
- Use Veo 2 for Avatar video generation (P8-T002)
- Use Imagen 3 for graphics generation (P8)
- Use Code Assist for autonomous code refinement

---

## 5. Recommended Tool Stack for Unwind Brain

### Core Infrastructure
```
- Python 3.11+ (Core brain logic)
- TypeScript/Node.js (UXP plugin, MCP servers)
- PostgreSQL/Supabase (Data persistence)
- Redis (Caching and real-time data)
```

### AI/ML Layer
```
- OpenAI API (GPT-4.1-mini for text processing)
- Google Gemini API (Multimodal analysis)
- MiniMax API (Avatar generation)
- ElevenLabs API (Voice synthesis)
```

### Video Processing
```
- MoviePy (Python video editing)
- FFmpeg (Video encoding/decoding)
- MediaPipe (Pose estimation for P10)
- OpenCV (Computer vision)
```

### MCP Servers to Implement
```
- Custom Unwind Brain MCP Server
- Video Generation MCP (Veo2/Runway)
- Social Distribution MCP
- Analytics MCP
```


---

## 6. Google Veo 2 / Veo 3.1 Video Generation

### Capabilities
- **Veo 2:** Available via Gemini API and Google AI Studio
- **Veo 3.1:** Latest model with audio integration for filmmakers
- **Pricing:** $0.35 USD per second of generated video
- **Input:** Text prompts or image prompts

### API Integration
```python
# Veo 2 API via Vertex AI
from google.cloud import aiplatform

# Initialize
aiplatform.init(project="unwind-brain", location="us-central1")

# Generate video
video = aiplatform.VideoGenerationModel.from_pretrained("veo-2")
response = video.generate(prompt="Professional presenter speaking to camera...")
```

### Use Cases for Unwind Brain
- P8-T002: Avatar video generation
- P8-T003: B-roll generation
- P10: Style transfer reference generation

---

## 7. MediaPipe Pose Estimation (Phase 10)

### Capabilities
- 33 3D body landmarks detection
- Real-time pose tracking
- Background segmentation
- Cross-platform (Python, JavaScript, Android, iOS)

### Key Landmarks for Kinetic Replication
```
0: nose
11-12: shoulders
13-14: elbows
15-16: wrists
23-24: hips
25-26: knees
27-28: ankles
```

### Python Implementation
```python
import mediapipe as mp
import cv2

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Process video frame
results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
landmarks = results.pose_landmarks
```

### Kinetic Blueprint Data Model
```json
{
  "video_id": "source_viral_001",
  "duration_seconds": 60,
  "kinetic_data": {
    "gesture_frequency": 2.3,  // gestures per second
    "head_nod_rate": 0.8,      // nods per second
    "hand_movement_intensity": 0.75,  // 0-1 scale
    "body_sway_amplitude": 0.2,       // normalized
    "pacing_bpm": 120                 // beats per minute
  },
  "peak_moments": [
    {"timestamp": 5.2, "type": "emphatic_gesture"},
    {"timestamp": 12.8, "type": "head_nod"},
    {"timestamp": 23.1, "type": "hand_raise"}
  ]
}
```

---

## 8. Gemini 3 Pro Capabilities

### Multimodal Understanding
- Text, images, video, audio, documents
- State-of-the-art reasoning
- Agentic capabilities
- "Vibe coding" for rapid prototyping

### Integration Points
- P11-T001: Narrative Principle Engine (analyze video content)
- P11-T002: Conscious Tone Synthesis (generate tone shift strategies)
- P3-T004: Competitive Analysis (analyze competitor content)

### API Usage
```python
from openai import OpenAI

client = OpenAI()  # Pre-configured for Gemini

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {"role": "system", "content": "You are the Narrative Principle Engine..."},
        {"role": "user", "content": "Analyze this video transcript for viral principles..."}
    ]
)
```

---

## 9. Available MCP Servers (User's Current Setup)

Based on the user's MCP integration:
1. **Playwright MCP** - Browser automation for scraping
2. **ClickUp MCP** - Task management integration
3. **Gmail MCP** - Email automation for outreach

### Additional MCPs to Configure
- Supabase MCP (database)
- YouTube MCP (distribution)
- HeyGen/Synthesia MCP (avatar generation)
- ElevenLabs MCP (voice synthesis)

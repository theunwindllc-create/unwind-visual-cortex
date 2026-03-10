# UNWIND BRAIN: DEPENDENCY MAP & PARAMETERS

**Version:** 1.0
**Date:** January 17, 2026
**Author:** Unwind Engineering Team

---

## 1. System Architecture Overview

The Unwind Brain is a symbiotic, multi-layered system designed for autonomous content creation, distribution, and evolution. It consists of two primary "Lungs" (Creator OS and Infinite Mirror) and multiple specialized "Cells" that handle specific tasks.

![System Architecture Diagram](https://i.imgur.com/example.png)  *(Placeholder for diagram to be generated)*

---

## 2. Core Dependencies

| Dependency | Version | Purpose | Installation |
| :--- | :--- | :--- | :--- |
| **Python** | 3.11+ | Core brain logic, ML, video processing | `apt-get install python3.11` |
| **Node.js** | 22.13.0+ | UXP plugin, MCP servers | `nvm install 22.13.0` |
| **PostgreSQL** | 16+ | Data persistence | `apt-get install postgresql` |
| **Redis** | 7.2+ | Caching, real-time data | `apt-get install redis-server` |
| **FFmpeg** | 6.1+ | Video encoding/decoding | `apt-get install ffmpeg` |
| **Git** | 2.43+ | Version control | `apt-get install git` |

---

## 3. Python Package Dependencies (`requirements.txt`)

```
# Core
fastapi
uvicorn

# AI/ML
openai  # For Gemini API
google-cloud-aiplatform
mediapipe
tensorflow
torch
transformers

# Video
moviepy
opencv-python

# Data
psycopg2-binary
redis
pandas
numpy

# Web Scraping
beautifulsoup4
requests

# Social Media
google-api-python-client
facebook-business
tiktok-api
```

---

## 4. Node.js Package Dependencies (`package.json`)

```json
{
  "dependencies": {
    "@google-cloud/aiplatform": "^3.20.0",
    "@mcp/client": "^1.5.0",
    "@mcp/server": "^1.5.0",
    "@supabase/supabase-js": "^2.42.0",
    "@types/node": "^20.12.7",
    "express": "^4.19.2",
    "playwright": "^1.44.0",
    "typescript": "^5.4.5"
  }
}
```

---

## 5. MCP Server Configuration (`mcp-servers.json`)

```json
[
  {
    "name": "unwind-brain-main",
    "path": "./mcp/main.ts",
    "port": 8080
  },
  {
    "name": "unwind-video-gen",
    "path": "./mcp/video.ts",
    "port": 8081
  },
  {
    "name": "unwind-social-dist",
    "path": "./mcp/social.ts",
    "port": 8082
  }
]
```

---

## 6. Environment Variables (`.env`)

```
# Google Cloud
GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
GOOGLE_PROJECT_ID=unwind-brain

# OpenAI (for Gemini)
OPENAI_API_KEY=your_openai_api_key

# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your_supabase_anon_key

# Social Media APIs
YOUTUBE_API_KEY=your_youtube_api_key
INSTAGRAM_APP_ID=your_ig_app_id
INSTAGRAM_APP_SECRET=your_ig_app_secret
TIKTOK_CLIENT_KEY=your_tiktok_client_key

# Database
POSTGRES_USER=unwind
POSTGRES_PASSWORD=your_db_password
POSTGRES_DB=unwind_brain
POSTGRES_HOST=localhost

# Redis
REDIS_HOST=localhost
REDIS_PORT=6379
```

---

## 7. Phase-to-Tool Mapping

| Phase | Key Tools & APIs |
| :--- | :--- |
| **P3: Enhanced Intelligence** | Playwright, BeautifulSoup, Perplexity API, Supabase |
| **P5: Full Autonomy** | MoviePy, FFmpeg, OpenAI Whisper API |
| **P8: Autonomous Assembly** | Google Veo 2 API, HeyGen/Synthesia API, ElevenLabs API |
| **P9: Infinite Presence** | YouTube API, Instagram API, TikTok API, HubSpot/Salesforce API |
| **P10: Kinetic Mastery** | MediaPipe, OpenCV |
| **P11: Conscious Evolution** | Gemini API, Anthropic API |

---

## 8. Initial Code Structure

```
/unwind-brain
|-- /src
|   |-- /brain
|   |   |-- __init__.py
|   |   |-- main.py  # Core FastAPI app
|   |   |-- consciousness.py  # P11
|   |   |-- memory.py
|   |-- /creator_os
|   |   |-- __init__.py
|   |   |-- assembly.py  # P8
|   |   |-- distribution.py  # P9
|   |-- /infinite_mirror
|   |   |-- __init__.py
|   |   |-- audit.py  # P7
|   |   |-- analysis.py  # P3
|   |-- /kinetic_engine
|   |   |-- __init__.py
|   |   |-- replication.py  # P10
|   |-- /utils
|   |   |-- db.py
|   |   |-- video.py
|-- /mcp
|   |-- main.ts
|   |-- video.ts
|   |-- social.ts
|-- /scripts
|   |-- setup.sh
|   |-- run.sh
|-- Dockerfile
|-- docker-compose.yml
|-- requirements.txt
|-- package.json
|-- README.md
```

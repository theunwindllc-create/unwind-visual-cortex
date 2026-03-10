# Phase 1 Quick Reference
## Pexels + After Effects Integration Cheat Sheet

**Quick access guide for developers using Phase 1 integrations**

---

## 🚀 Quick Start

### Setup (One-Time)

```bash
# Set Pexels API key
export PEXELS_API_KEY='your_api_key_here'

# Add to shell profile for persistence
echo 'export PEXELS_API_KEY="your_key"' >> ~/.bashrc
source ~/.bashrc
```

### Download B-Roll (One-Liner)

```python
from pexels_integration import search_and_download_broll

video = search_and_download_broll("business meeting")
```

### Convert to AE JSON (One-Liner)

```python
from ae_json_exporter import convert_blueprint_to_ae_json

ae_json = convert_blueprint_to_ae_json("blueprint.json", "ae_data.json")
```

---

## 📦 Pexels Integration

### Import

```python
from pexels_integration import PexelsClient, search_and_download_broll
```

### Basic Usage

```python
# Simple download
video_path = search_and_download_broll("city skyline")

# With options
video_path = search_and_download_broll(
    shot_description="coffee shop interior",
    output_dir="./broll",
    orientation="landscape",  # or "portrait", "square"
    quality="hd"              # or "sd"
)
```

### Advanced Usage

```python
client = PexelsClient()

# Search
results = client.search_videos("business", per_page=15)

# Find best match with filters
video = client.find_best_match(
    query="ocean waves",
    orientation="landscape",
    min_duration=5,   # seconds
    max_duration=30   # seconds
)

# Get download URL
url = client.get_video_file_url(video, quality="hd")

# Download
path = client.download_video(url, "./output.mp4")
```

### Common Parameters

| Parameter | Options | Default |
|-----------|---------|---------|
| `orientation` | `"landscape"`, `"portrait"`, `"square"` | `"landscape"` |
| `quality` | `"hd"`, `"sd"`, or resolution like `"1920x1080"` | `"hd"` |
| `per_page` | 1-80 | 15 |
| `min_duration` | seconds (int) | None |
| `max_duration` | seconds (int) | None |

---

## 🎬 After Effects Integration

### Import

```python
from ae_json_exporter import AEJSONExporter, convert_blueprint_to_ae_json
```

### Basic Usage

```python
# Simple conversion
ae_json_path = convert_blueprint_to_ae_json(
    blueprint_path="blueprint.json",
    output_path="ae_data.json",
    pretty=True  # Pretty-print for debugging
)
```

### Advanced Usage

```python
import json

# Load blueprint
with open("blueprint.json", 'r') as f:
    blueprint = json.load(f)

# Create exporter
exporter = AEJSONExporter(blueprint)

# Convert
ae_data = exporter.convert()

# Add custom data
ae_data['custom_field'] = 'custom_value'

# Save
with open("ae_data.json", 'w') as f:
    json.dump(ae_data, f, indent=2)
```

### After Effects Expressions

```javascript
// Access JSON data
var unwindData = footage("ae_data.json").sourceData;

// Get primary color
var primaryColor = unwindData.color_palette.primary.rgb;

// Get text content
var textContent = unwindData.text_layers[0].content;

// Get timing
var startTime = unwindData.emotional_timing.intro.start_time;
```

---

## 🔄 Complete Workflow

### Full Pipeline Example

```python
from pexels_integration import search_and_download_broll
from ae_json_exporter import convert_blueprint_to_ae_json
import os
import json

# 1. Setup
project_dir = "./my_project"
os.makedirs(f"{project_dir}/broll", exist_ok=True)

# 2. Load blueprint (from AI Video Brain)
with open("blueprint.json", 'r') as f:
    blueprint = json.load(f)

# 3. Download B-roll
shot_list = blueprint['visual_recommendations']['shot_list']
for shot in shot_list:
    video_path = search_and_download_broll(
        shot['description'],
        output_dir=f"{project_dir}/broll"
    )
    shot['broll_asset'] = video_path

# 4. Update blueprint
with open(f"{project_dir}/blueprint.json", 'w') as f:
    json.dump(blueprint, f, indent=2)

# 5. Generate AE JSON
ae_json_path = convert_blueprint_to_ae_json(
    f"{project_dir}/blueprint.json",
    f"{project_dir}/ae_data.json"
)

print(f"✓ Project ready: {project_dir}")
```

---

## 📁 Project Structure

### Recommended Layout

```
project_name/
├── blueprint.json              # AI-generated blueprint
├── ae_data.json               # After Effects JSON
├── PROJECT_SUMMARY.json       # Project metadata
├── broll/                     # B-roll assets
│   ├── business_meeting_12345.mp4
│   ├── city_skyline_67890.mp4
│   └── ...
├── exports/                   # Rendered videos
│   └── final_v1.mp4
└── templates/                 # AE project files
    └── template_v1.aep
```

---

## 🐛 Troubleshooting

### Pexels Issues

| Error | Solution |
|-------|----------|
| "API key not provided" | `export PEXELS_API_KEY='your_key'` |
| "Rate limit exceeded" | Wait 1 hour or reduce requests |
| "No videos found" | Try broader search terms |
| Download fails | Check internet, disk space |

### After Effects Issues

| Error | Solution |
|-------|----------|
| JSON won't import | Validate JSON, check AE version (CC 2020+) |
| Colors wrong | Use exporter's hex_to_rgb() function |
| Expression errors | Verify footage name matches JSON filename |
| Data doesn't update | Reload footage in AE |

---

## ⚡ Performance Tips

### B-Roll Download

```python
# Parallel downloads (faster)
from concurrent.futures import ThreadPoolExecutor

def download_parallel(descriptions, output_dir):
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(
            lambda d: search_and_download_broll(d, output_dir),
            descriptions
        )
    return list(results)
```

### AE JSON

```python
# Minimize JSON size (faster AE import)
ae_json_path = convert_blueprint_to_ae_json(
    blueprint_path,
    output_path,
    pretty=False  # Compact JSON
)
```

---

## 📚 Common Code Snippets

### Validate Project Assets

```python
import os
import json

def validate_project(project_dir):
    checks = {
        'blueprint': os.path.exists(f"{project_dir}/blueprint.json"),
        'ae_json': os.path.exists(f"{project_dir}/ae_data.json"),
        'broll_dir': os.path.exists(f"{project_dir}/broll")
    }
    
    if checks['broll_dir']:
        videos = [f for f in os.listdir(f"{project_dir}/broll") 
                  if f.endswith('.mp4')]
        checks['broll_count'] = len(videos)
    
    return checks
```

### Batch Process Multiple Projects

```python
projects = [
    {'name': 'Project A', 'shots': ['shot1', 'shot2']},
    {'name': 'Project B', 'shots': ['shot3', 'shot4']}
]

for project in projects:
    print(f"Processing {project['name']}...")
    
    # Download B-roll
    for shot in project['shots']:
        search_and_download_broll(shot, f"./{project['name']}/broll")
    
    # Generate AE JSON
    convert_blueprint_to_ae_json(
        f"./{project['name']}/blueprint.json",
        f"./{project['name']}/ae_data.json"
    )
```

### Custom Search Filters

```python
client = PexelsClient()

# Portrait videos only
video = client.find_best_match(
    query="person talking",
    orientation="portrait",
    min_duration=10
)

# Short clips for social media
video = client.find_best_match(
    query="product showcase",
    orientation="square",
    max_duration=15
)
```

---

## 🔗 Links & Resources

### Documentation
- **Full Integration Guide:** `PHASE_1_INTEGRATION_GUIDE.md`
- **Pexels Module:** `PEXELS_INTEGRATION_GUIDE.md`
- **AE JSON Module:** `AE_JSON_INTEGRATION_GUIDE.md`
- **Code Examples:** `phase1_code_examples.py`

### External Resources
- **Pexels API Docs:** https://www.pexels.com/api/documentation/
- **AE Data-Driven Animation:** https://helpx.adobe.com/after-effects/using/data-driven-animations.html

### Get API Key
- **Pexels:** https://www.pexels.com/api/ (free, 200 req/hour)

---

## 📊 API Limits

### Pexels
- **Free Tier:** 200 requests/hour
- **Our Rate Limiter:** 180 requests/hour (conservative)
- **Automatic Handling:** Yes, waits when limit approached

### File Sizes
- **HD Video (10s):** ~5-15 MB
- **HD Video (30s):** ~15-50 MB
- **AE JSON:** ~5-50 KB (depending on blueprint size)

---

## ✅ Checklist

### Before Starting
- [ ] Pexels API key set in environment
- [ ] Python 3.11+ installed
- [ ] Modules imported successfully
- [ ] Project directory created

### After Completion
- [ ] Blueprint saved
- [ ] B-roll downloaded
- [ ] AE JSON generated
- [ ] Project validated
- [ ] Assets organized

---

## 🎯 Common Use Cases

### Use Case 1: Single Video Project
```python
# Download 5 B-roll clips
shots = ["intro scene", "main content", "transition", "detail shot", "outro"]
for shot in shots:
    search_and_download_broll(shot, "./broll")

# Generate AE JSON
convert_blueprint_to_ae_json("blueprint.json", "ae_data.json")
```

### Use Case 2: Batch Production
```python
# Process multiple videos
for video_id in range(1, 11):
    blueprint = f"./video_{video_id}/blueprint.json"
    ae_json = f"./video_{video_id}/ae_data.json"
    convert_blueprint_to_ae_json(blueprint, ae_json)
```

### Use Case 3: Custom Quality Selection
```python
# Preview quality (faster download)
preview = search_and_download_broll("scene", quality="sd")

# Final quality (for rendering)
final = search_and_download_broll("scene", quality="hd")
```

---

**Last Updated:** January 11, 2026  
**Phase 1 Status:** ✅ Complete and Production Ready  
**Maintained by:** Unwind Visual Cortex Development Team

---

*Keep this reference handy for quick access to Phase 1 integration commands and patterns.*

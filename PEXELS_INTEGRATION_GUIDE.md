# Pexels API Integration Guide
## Automated B-Roll Sourcing for Unwind Visual Cortex

**Module:** `pexels_integration.py`  
**Purpose:** Automatically search and download royalty-free B-roll footage from Pexels  
**Status:** ✅ Implemented and tested  
**Date:** January 9, 2026

---

## Overview

The Pexels integration allows the Unwind Visual Cortex to automatically source B-roll footage based on shot list descriptions generated during the video analysis phase. This eliminates the manual process of searching for and downloading stock footage.

---

## Features

### Core Functionality
- ✅ **Video Search** - Search Pexels library with natural language queries
- ✅ **Rate Limiting** - Automatic rate limiting (180 requests/hour, conservative)
- ✅ **Error Handling** - Comprehensive error handling with retry logic
- ✅ **Quality Selection** - Choose HD, SD, or specific resolutions
- ✅ **Orientation Filtering** - Landscape, portrait, or square videos
- ✅ **Duration Filtering** - Filter by minimum/maximum duration
- ✅ **Automatic Download** - Stream downloads with progress indicators
- ✅ **Best Match Selection** - Intelligent selection of most relevant videos

### Safety Features
- **Rate limiter** prevents API quota exhaustion
- **Exponential backoff** for failed requests
- **Timeout handling** for slow connections
- **Automatic directory creation** for downloads
- **Progress indicators** for large downloads

---

## Setup

### 1. Get API Key

1. Go to https://www.pexels.com/api/
2. Sign up for a free account
3. Generate an API key (free tier: 200 requests/hour)

### 2. Set Environment Variable

```bash
export PEXELS_API_KEY='your_api_key_here'
```

Or add to your shell profile (~/.bashrc or ~/.zshrc):
```bash
echo 'export PEXELS_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

---

## Usage

### Quick Start (Convenience Function)

```python
from pexels_integration import search_and_download_broll

# Simple search and download
video_path = search_and_download_broll("business meeting")
print(f"Downloaded: {video_path}")

# With options
video_path = search_and_download_broll(
    shot_description="city skyline at sunset",
    output_dir="/path/to/broll",
    orientation="landscape",
    quality="hd"
)
```

### Advanced Usage (Full Client)

```python
from pexels_integration import PexelsClient

# Initialize client
client = PexelsClient()  # Reads API key from environment

# Search for videos
results = client.search_videos(
    query="business meeting",
    orientation="landscape",
    size="medium",
    per_page=15
)

print(f"Found {results['total_results']} videos")

# Get best match with filters
video = client.find_best_match(
    query="coffee shop",
    orientation="landscape",
    min_duration=5,  # At least 5 seconds
    max_duration=30  # No longer than 30 seconds
)

# Get download URL
video_url = client.get_video_file_url(video, quality="hd")

# Download
output_path = client.download_video(
    video_url,
    "/path/to/output/video.mp4"
)
```

---

## Integration with Visual Cortex

### Workflow

1. **Visual Cortex generates shot list** with B-roll descriptions
2. **For each shot description:**
   - Search Pexels with the description
   - Select best matching video
   - Download to organized folder structure
   - Track downloaded assets in blueprint
3. **Assets ready for editing** in Premiere Pro/After Effects

### Example Integration

```python
from ai_video_brain import AIVideoBrain
from pexels_integration import search_and_download_broll

# Generate blueprint
brain = AIVideoBrain()
blueprint = brain.analyze(transcript, brand_input, platform, conversion_goal)

# Download B-roll for each shot
broll_assets = []
for shot in blueprint['visual_recommendations']['shot_list']:
    description = shot['description']
    video_path = search_and_download_broll(
        shot_description=description,
        output_dir=f"/home/ubuntu/projects/{project_name}/broll",
        orientation="landscape"
    )
    
    if video_path:
        shot['broll_asset'] = video_path
        broll_assets.append(video_path)

# Update blueprint with asset paths
blueprint['broll_assets'] = broll_assets
```

---

## API Reference

### PexelsClient Class

#### `__init__(api_key=None)`
Initialize the Pexels client.
- **api_key** (optional): API key. If None, reads from `PEXELS_API_KEY` env var.

#### `search_videos(query, orientation="landscape", size="medium", per_page=15, page=1)`
Search for videos on Pexels.
- **query**: Search query (e.g., "business meeting")
- **orientation**: "landscape", "portrait", or "square"
- **size**: "large", "medium", or "small"
- **per_page**: Results per page (max 80)
- **page**: Page number
- **Returns**: Dictionary with search results

#### `get_video_by_id(video_id)`
Get video details by ID.
- **video_id**: Pexels video ID
- **Returns**: Dictionary with video metadata

#### `download_video(video_url, output_path, chunk_size=8192)`
Download a video file.
- **video_url**: Direct URL to video file
- **output_path**: Where to save the video
- **chunk_size**: Download chunk size in bytes
- **Returns**: Path to downloaded file

#### `find_best_match(query, orientation="landscape", min_duration=None, max_duration=None)`
Find the best matching video for a query.
- **query**: Search query
- **orientation**: Video orientation
- **min_duration**: Minimum duration in seconds (optional)
- **max_duration**: Maximum duration in seconds (optional)
- **Returns**: Best matching video metadata or None

#### `get_video_file_url(video_metadata, quality="hd")`
Extract video file URL from metadata.
- **video_metadata**: Video metadata from search results
- **quality**: "hd", "sd", or specific resolution like "1920x1080"
- **Returns**: Direct URL to video file or None

---

## Rate Limiting

### Pexels API Limits
- **Free Tier:** 200 requests per hour
- **Our Implementation:** 180 requests per hour (conservative)
- **Automatic Handling:** Rate limiter waits when limit approached

### Rate Limiter Behavior
```python
# Tracks requests in a rolling 1-hour window
# Automatically waits if limit would be exceeded
# Example: If 180 requests made, waits until oldest request is >1 hour old
```

---

## Error Handling

### Exception Types

#### `PexelsAPIError`
Base exception for all Pexels API errors.

**Common Causes:**
- Invalid API key (401)
- Rate limit exceeded (429)
- Network errors
- Invalid parameters

**Example Handling:**
```python
from pexels_integration import PexelsClient, PexelsAPIError

try:
    client = PexelsClient()
    results = client.search_videos("business")
except PexelsAPIError as e:
    print(f"API Error: {e}")
    # Handle error (log, retry, use fallback, etc.)
```

---

## File Organization

### Recommended Structure

```
project_name/
├── broll/
│   ├── business_meeting_12345678.mp4
│   ├── city_skyline_87654321.mp4
│   └── coffee_shop_11223344.mp4
├── blueprint.json
└── final_video.mp4
```

### Filename Convention
`{description}_{pexels_id}.mp4`

Example: `business_meeting_12345678.mp4`

---

## Performance

### Typical Timings
- **Search:** 0.5-1 second
- **Download (HD 10s clip):** 2-5 seconds
- **Download (HD 30s clip):** 5-15 seconds

### Optimization Tips
1. **Batch searches** - Search for multiple shots at once
2. **Parallel downloads** - Download multiple videos simultaneously
3. **Cache results** - Store search results to avoid re-searching
4. **Quality selection** - Use SD for previews, HD for final

---

## Testing

### Unit Tests

```python
# Test search functionality
def test_search():
    client = PexelsClient()
    results = client.search_videos("business", per_page=5)
    assert results['total_results'] > 0
    assert len(results['videos']) <= 5

# Test rate limiting
def test_rate_limit():
    client = PexelsClient()
    # Make 180 requests (should work)
    for i in range(180):
        client.search_videos(f"test{i}", per_page=1)
    # 181st request should wait
    # (test timing to verify wait occurs)

# Test error handling
def test_invalid_api_key():
    client = PexelsClient(api_key="invalid")
    with pytest.raises(PexelsAPIError):
        client.search_videos("test")
```

---

## Troubleshooting

### "API key not provided"
**Solution:** Set `PEXELS_API_KEY` environment variable

### "Rate limit exceeded"
**Solution:** Wait 1 hour or reduce request frequency

### "No videos found"
**Solution:** Try broader search terms or different keywords

### "Download failed"
**Solution:** Check internet connection, try again, or use different quality

---

## Future Enhancements

### Planned Features
- [ ] **CLIP-based matching** - Use AI to match shots to descriptions
- [ ] **Caching layer** - Store search results locally
- [ ] **Pixabay fallback** - Use Pixabay if Pexels has no results
- [ ] **Metadata extraction** - Extract colors, subjects, mood from videos
- [ ] **Smart selection** - ML model to pick best video based on brand guidelines

---

## License & Attribution

### Pexels License
All videos on Pexels are free to use for:
- ✅ Commercial projects
- ✅ Personal projects
- ✅ Editing and modification
- ❌ Selling unmodified videos
- ❌ Creating competing stock services

**Attribution:** Not required but appreciated

### Integration License
This integration module is part of the Unwind Visual Cortex and follows the same license as the parent project.

---

## Support

### Resources
- **Pexels API Docs:** https://www.pexels.com/api/documentation/
- **Pexels Support:** https://help.pexels.com/
- **Visual Cortex Docs:** See `ROADMAP_INDEX.md`

### Common Issues
See **Troubleshooting** section above

---

**Module Status:** ✅ Production Ready  
**Last Updated:** January 9, 2026  
**Maintainer:** Unwind Visual Cortex Development Team  
**Created by:** Jesus Casares, founder of Unwind Code

# Phase 1 Integration Guide
## Complete B-Roll Sourcing & After Effects Integration

**Unwind Visual Cortex - Phase 1 Foundation**  
**Version:** 1.0  
**Date:** January 11, 2026  
**Status:** ✅ Complete and Production Ready

---

## Executive Summary

Phase 1 of the Unwind Visual Cortex establishes the foundation for automated video production by integrating two critical capabilities:

1. **Pexels API Integration** - Automated B-roll sourcing from royalty-free stock footage
2. **After Effects JSON Export** - Data-driven animation workflow for brand-consistent motion graphics

Together, these integrations enable the Visual Cortex to automatically source visual assets and prepare them for professional video editing workflows.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   UNWIND VISUAL CORTEX                       │
│                  (AI Video Brain Core)                       │
└────────────┬────────────────────────────┬───────────────────┘
             │                            │
             │                            │
    ┌────────▼────────┐         ┌────────▼────────┐
    │  Pexels API     │         │  AE JSON        │
    │  Integration    │         │  Exporter       │
    │                 │         │                 │
    │ • Search videos │         │ • Convert       │
    │ • Rate limiting │         │   blueprint     │
    │ • Download      │         │ • Color mapping │
    │ • Best match    │         │ • Timing data   │
    └────────┬────────┘         └────────┬────────┘
             │                            │
             │                            │
    ┌────────▼────────┐         ┌────────▼────────┐
    │   B-Roll        │         │  After Effects  │
    │   Assets        │         │  Project        │
    │   (MP4 files)   │         │  (Data-Driven)  │
    └─────────────────┘         └─────────────────┘
```

---

## Module Documentation

### 1. Pexels Integration Module

**File:** `pexels_integration.py`  
**Documentation:** `PEXELS_INTEGRATION_GUIDE.md`

#### Key Features
- ✅ Natural language video search
- ✅ Automatic rate limiting (180 req/hour)
- ✅ Quality selection (HD/SD)
- ✅ Orientation filtering (landscape/portrait/square)
- ✅ Duration filtering
- ✅ Best match selection algorithm
- ✅ Streaming downloads with progress

#### Quick Usage
```python
from pexels_integration import search_and_download_broll

# Simple one-liner
video_path = search_and_download_broll("business meeting")

# With options
video_path = search_and_download_broll(
    shot_description="city skyline at sunset",
    output_dir="/path/to/broll",
    orientation="landscape",
    quality="hd"
)
```

#### Setup Requirements
1. Get free API key from https://www.pexels.com/api/
2. Set environment variable: `export PEXELS_API_KEY='your_key'`
3. Import and use

---

### 2. After Effects JSON Exporter

**File:** `ae_json_exporter.py`  
**Documentation:** `AE_JSON_INTEGRATION_GUIDE.md`

#### Key Features
- ✅ Blueprint to AE JSON conversion
- ✅ Hex to RGB color conversion
- ✅ Brand color palette mapping
- ✅ Typography specifications
- ✅ Text layer content
- ✅ Emotional timing data
- ✅ B-roll asset references
- ✅ CTA and motion graphics specs

#### Quick Usage
```python
from ae_json_exporter import convert_blueprint_to_ae_json

# Convert blueprint
ae_json_path = convert_blueprint_to_ae_json(
    blueprint_path="/path/to/blueprint.json",
    output_path="/path/to/output_ae.json",
    pretty=True
)
```

#### After Effects Integration
1. Import JSON as footage in AE
2. Use expressions to access data:
```javascript
var unwindData = footage("output_ae.json").sourceData;
var primaryColor = unwindData.color_palette.primary.rgb;
```

---

## Complete Workflow Example

### End-to-End Video Production Pipeline

This example shows how to use both integrations together to go from transcript to ready-to-edit assets.

```python
#!/usr/bin/env python3
"""
Complete Phase 1 workflow example
Demonstrates Pexels + AE JSON integration
"""

from ai_video_brain import AIVideoBrain
from pexels_integration import search_and_download_broll
from ae_json_exporter import convert_blueprint_to_ae_json
import os
import json

def create_video_project(transcript, brand_input, platform="all", conversion_goal="leads"):
    """
    Complete workflow from transcript to ready-to-edit assets
    
    Args:
        transcript: Video transcript text
        brand_input: Brand guidelines and information
        platform: Target platform (all, instagram, youtube, tiktok)
        conversion_goal: leads, sales, awareness, engagement
    
    Returns:
        Dictionary with all project assets and paths
    """
    
    # Step 1: Generate blueprint with AI Video Brain
    print("Step 1: Analyzing transcript and generating blueprint...")
    brain = AIVideoBrain()
    blueprint = brain.analyze(transcript, brand_input, platform, conversion_goal)
    
    # Create project directory
    project_name = brand_input.get('brand_name', 'project').replace(' ', '_').lower()
    project_dir = f"/home/ubuntu/projects/{project_name}"
    os.makedirs(f"{project_dir}/broll", exist_ok=True)
    
    # Save blueprint
    blueprint_path = f"{project_dir}/blueprint.json"
    with open(blueprint_path, 'w') as f:
        json.dump(blueprint, f, indent=2)
    print(f"✓ Blueprint saved: {blueprint_path}")
    
    # Step 2: Download B-roll for each shot
    print("\nStep 2: Downloading B-roll assets from Pexels...")
    broll_assets = []
    shot_list = blueprint.get('visual_recommendations', {}).get('shot_list', [])
    
    for i, shot in enumerate(shot_list, 1):
        description = shot.get('description', '')
        if not description:
            continue
            
        print(f"  [{i}/{len(shot_list)}] Searching for: {description}")
        
        try:
            video_path = search_and_download_broll(
                shot_description=description,
                output_dir=f"{project_dir}/broll",
                orientation="landscape",
                quality="hd"
            )
            
            if video_path:
                shot['broll_asset'] = video_path
                broll_assets.append({
                    'shot_number': i,
                    'description': description,
                    'path': video_path
                })
                print(f"    ✓ Downloaded: {os.path.basename(video_path)}")
            else:
                print(f"    ⚠ No suitable video found")
                
        except Exception as e:
            print(f"    ✗ Error: {e}")
    
    # Update blueprint with asset paths
    blueprint['broll_assets'] = broll_assets
    with open(blueprint_path, 'w') as f:
        json.dump(blueprint, f, indent=2)
    
    print(f"\n✓ Downloaded {len(broll_assets)} B-roll assets")
    
    # Step 3: Generate After Effects JSON
    print("\nStep 3: Generating After Effects JSON...")
    ae_json_path = convert_blueprint_to_ae_json(
        blueprint_path=blueprint_path,
        output_path=f"{project_dir}/ae_data.json",
        pretty=True
    )
    print(f"✓ AE JSON saved: {ae_json_path}")
    
    # Step 4: Create project summary
    print("\nStep 4: Creating project summary...")
    summary = {
        'project_name': project_name,
        'project_dir': project_dir,
        'blueprint_path': blueprint_path,
        'ae_json_path': ae_json_path,
        'broll_count': len(broll_assets),
        'broll_assets': broll_assets,
        'platform': platform,
        'conversion_goal': conversion_goal,
        'status': 'ready_for_editing'
    }
    
    summary_path = f"{project_dir}/PROJECT_SUMMARY.json"
    with open(summary_path, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print("\n" + "="*60)
    print("PROJECT READY FOR EDITING")
    print("="*60)
    print(f"Project Directory: {project_dir}")
    print(f"Blueprint: {blueprint_path}")
    print(f"AE JSON: {ae_json_path}")
    print(f"B-roll Assets: {len(broll_assets)} videos in {project_dir}/broll/")
    print(f"Summary: {summary_path}")
    print("="*60)
    
    return summary


# Example usage
if __name__ == "__main__":
    # Example inputs
    transcript = """
    Welcome to our new product launch. Today we're excited to introduce 
    our revolutionary software that helps businesses automate their workflow.
    With our AI-powered platform, you can save hours every day and focus 
    on what really matters - growing your business.
    """
    
    brand_input = {
        'brand_name': 'TechFlow',
        'industry': 'SaaS',
        'target_audience': 'Small business owners and entrepreneurs',
        'brand_colors': {
            'primary': '#0066FF',
            'secondary': '#00CC88',
            'accent': '#FF6B00'
        },
        'brand_voice': 'Professional yet approachable, innovative, trustworthy'
    }
    
    # Run complete workflow
    project = create_video_project(
        transcript=transcript,
        brand_input=brand_input,
        platform="all",
        conversion_goal="leads"
    )
    
    print("\n✓ Workflow complete!")
    print(f"✓ All assets ready in: {project['project_dir']}")
```

---

## Integration Patterns

### Pattern 1: Batch B-Roll Download

Download multiple B-roll clips in parallel for faster processing:

```python
from pexels_integration import PexelsClient
from concurrent.futures import ThreadPoolExecutor
import os

def download_broll_batch(shot_descriptions, output_dir):
    """
    Download multiple B-roll clips in parallel
    
    Args:
        shot_descriptions: List of shot descriptions
        output_dir: Where to save videos
    
    Returns:
        List of downloaded video paths
    """
    client = PexelsClient()
    
    def download_single(description):
        try:
            # Find best match
            video = client.find_best_match(
                query=description,
                orientation="landscape",
                min_duration=5
            )
            
            if not video:
                return None
            
            # Get download URL
            video_url = client.get_video_file_url(video, quality="hd")
            if not video_url:
                return None
            
            # Download
            filename = f"{description[:30].replace(' ', '_')}_{video['id']}.mp4"
            output_path = os.path.join(output_dir, filename)
            
            return client.download_video(video_url, output_path)
            
        except Exception as e:
            print(f"Error downloading {description}: {e}")
            return None
    
    # Download in parallel (max 5 concurrent)
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(download_single, shot_descriptions))
    
    # Filter out None values
    return [r for r in results if r is not None]


# Usage
shots = [
    "business meeting in modern office",
    "person working on laptop",
    "city skyline at sunset",
    "handshake close up"
]

videos = download_broll_batch(shots, "/path/to/broll")
print(f"Downloaded {len(videos)} videos")
```

### Pattern 2: Dynamic AE Template Population

Use the AE JSON to dynamically populate After Effects templates:

```python
from ae_json_exporter import AEJSONExporter
import json

def create_branded_template(blueprint_path, template_name):
    """
    Create a branded AE template from blueprint
    
    Args:
        blueprint_path: Path to Unwind blueprint
        template_name: Name for the template
    
    Returns:
        Path to AE JSON file
    """
    # Load blueprint
    with open(blueprint_path, 'r') as f:
        blueprint = json.load(f)
    
    # Initialize exporter
    exporter = AEJSONExporter(blueprint)
    
    # Convert to AE JSON
    ae_data = exporter.convert()
    
    # Add template metadata
    ae_data['template_metadata'] = {
        'template_name': template_name,
        'created_date': exporter.ae_json['project_metadata']['generated_date'],
        'brand': blueprint.get('brand_analysis', {}).get('brand_name', 'Unknown'),
        'usage': 'Import this JSON into After Effects and link properties via expressions'
    }
    
    # Save
    output_path = f"/path/to/templates/{template_name}_ae_data.json"
    with open(output_path, 'w') as f:
        json.dump(ae_data, f, indent=2)
    
    return output_path


# Usage
template_path = create_branded_template(
    blueprint_path="/path/to/blueprint.json",
    template_name="TechFlow_Product_Launch"
)
```

### Pattern 3: Asset Validation

Validate that all required assets are available before editing:

```python
import os
import json

def validate_project_assets(project_dir):
    """
    Validate that all project assets are present and valid
    
    Args:
        project_dir: Project directory path
    
    Returns:
        Dictionary with validation results
    """
    results = {
        'valid': True,
        'errors': [],
        'warnings': [],
        'assets': {}
    }
    
    # Check blueprint exists
    blueprint_path = os.path.join(project_dir, 'blueprint.json')
    if not os.path.exists(blueprint_path):
        results['valid'] = False
        results['errors'].append("Blueprint file missing")
        return results
    
    results['assets']['blueprint'] = blueprint_path
    
    # Check AE JSON exists
    ae_json_path = os.path.join(project_dir, 'ae_data.json')
    if not os.path.exists(ae_json_path):
        results['valid'] = False
        results['errors'].append("AE JSON file missing")
    else:
        results['assets']['ae_json'] = ae_json_path
    
    # Check B-roll directory
    broll_dir = os.path.join(project_dir, 'broll')
    if not os.path.exists(broll_dir):
        results['warnings'].append("B-roll directory missing")
    else:
        # Count video files
        videos = [f for f in os.listdir(broll_dir) if f.endswith('.mp4')]
        results['assets']['broll_count'] = len(videos)
        results['assets']['broll_files'] = videos
        
        if len(videos) == 0:
            results['warnings'].append("No B-roll videos found")
    
    # Load and validate blueprint structure
    try:
        with open(blueprint_path, 'r') as f:
            blueprint = json.load(f)
        
        # Check required sections
        required_sections = [
            'brand_analysis',
            'visual_recommendations',
            'emotional_tone_mapping'
        ]
        
        for section in required_sections:
            if section not in blueprint:
                results['warnings'].append(f"Blueprint missing section: {section}")
        
    except json.JSONDecodeError:
        results['valid'] = False
        results['errors'].append("Blueprint JSON is invalid")
    
    return results


# Usage
validation = validate_project_assets("/home/ubuntu/projects/techflow")

if validation['valid']:
    print("✓ Project assets validated successfully")
    print(f"  - Blueprint: {validation['assets']['blueprint']}")
    print(f"  - AE JSON: {validation['assets']['ae_json']}")
    print(f"  - B-roll videos: {validation['assets']['broll_count']}")
else:
    print("✗ Project validation failed:")
    for error in validation['errors']:
        print(f"  - {error}")

if validation['warnings']:
    print("\n⚠ Warnings:")
    for warning in validation['warnings']:
        print(f"  - {warning}")
```

---

## Best Practices

### 1. B-Roll Sourcing

**DO:**
- ✅ Use descriptive, specific search terms
- ✅ Filter by orientation for consistency
- ✅ Set minimum duration (5-10 seconds recommended)
- ✅ Download HD quality for final production
- ✅ Organize files in project-specific directories
- ✅ Track downloaded assets in blueprint

**DON'T:**
- ❌ Use vague search terms like "video" or "footage"
- ❌ Mix orientations (landscape/portrait) in same project
- ❌ Download without rate limiting
- ❌ Ignore error handling
- ❌ Forget to set PEXELS_API_KEY environment variable

### 2. After Effects Integration

**DO:**
- ✅ Use pretty-printed JSON for debugging
- ✅ Validate JSON structure before importing to AE
- ✅ Use the provided expression examples
- ✅ Keep AE project and JSON in same directory
- ✅ Version your JSON files (v1, v2, etc.)

**DON'T:**
- ❌ Manually edit AE JSON (regenerate from blueprint instead)
- ❌ Hard-code values in AE expressions
- ❌ Import JSON without checking color format
- ❌ Forget to update JSON when blueprint changes

### 3. Project Organization

**Recommended Structure:**
```
project_name/
├── blueprint.json              # Core AI-generated blueprint
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

## Troubleshooting

### Pexels Integration Issues

#### "API key not provided"
**Cause:** Environment variable not set  
**Solution:**
```bash
export PEXELS_API_KEY='your_api_key_here'
# Or add to ~/.bashrc for persistence
```

#### "Rate limit exceeded"
**Cause:** Too many requests in 1 hour  
**Solution:** Wait for rate limit to reset, or reduce request frequency

#### "No videos found"
**Cause:** Search term too specific or no matches  
**Solution:** Try broader terms, remove filters, or use alternative keywords

#### Download fails
**Cause:** Network issues, invalid URL, or disk space  
**Solution:** Check internet connection, verify URL, ensure disk space available

### After Effects Integration Issues

#### JSON won't import to AE
**Cause:** Invalid JSON format or AE version too old  
**Solution:** Validate JSON with `json.load()`, ensure AE CC 2020+

#### Colors look wrong in AE
**Cause:** RGB values not normalized (0-1 range)  
**Solution:** Use the exporter's hex_to_rgb() function, don't manually convert

#### Expression errors
**Cause:** Incorrect footage name or data path  
**Solution:** Verify footage name matches JSON filename, check data structure

#### Data doesn't update
**Cause:** AE cached old JSON  
**Solution:** Reload footage in AE (right-click > Reload Footage)

---

## Performance Optimization

### B-Roll Download Optimization

1. **Parallel Downloads** - Use ThreadPoolExecutor for concurrent downloads
2. **Quality Selection** - Use SD for previews, HD for final
3. **Caching** - Store search results to avoid re-searching
4. **Batch Processing** - Download all assets at once, not one-by-one

### After Effects Optimization

1. **Minimize JSON Size** - Only include necessary data
2. **Expression Efficiency** - Cache frequently accessed values
3. **Template Reuse** - Create reusable templates for common formats
4. **Proxy Workflow** - Use low-res proxies during editing

---

## Testing

### Unit Tests

```python
import pytest
from pexels_integration import PexelsClient, search_and_download_broll
from ae_json_exporter import convert_blueprint_to_ae_json
import os
import json

def test_pexels_search():
    """Test Pexels video search"""
    client = PexelsClient()
    results = client.search_videos("business", per_page=5)
    assert results['total_results'] > 0
    assert len(results['videos']) <= 5

def test_broll_download():
    """Test B-roll download function"""
    video_path = search_and_download_broll(
        "test video",
        output_dir="/tmp/test_broll"
    )
    assert video_path is not None
    assert os.path.exists(video_path)
    assert video_path.endswith('.mp4')

def test_ae_json_conversion():
    """Test AE JSON conversion"""
    # Create test blueprint
    test_blueprint = {
        'brand_analysis': {'brand_name': 'Test Brand'},
        'visual_recommendations': {'shot_list': []},
        'emotional_tone_mapping': {}
    }
    
    blueprint_path = "/tmp/test_blueprint.json"
    with open(blueprint_path, 'w') as f:
        json.dump(test_blueprint, f)
    
    # Convert
    ae_json_path = convert_blueprint_to_ae_json(
        blueprint_path,
        "/tmp/test_ae.json"
    )
    
    assert os.path.exists(ae_json_path)
    
    # Validate JSON structure
    with open(ae_json_path, 'r') as f:
        ae_data = json.load(f)
    
    assert 'project_metadata' in ae_data
    assert 'color_palette' in ae_data
    assert 'text_layers' in ae_data
```

### Integration Tests

```python
def test_complete_workflow():
    """Test complete workflow from blueprint to assets"""
    # This would test the full pipeline
    # Blueprint -> Pexels download -> AE JSON export
    pass
```

---

## Future Enhancements

### Planned for Phase 2+

- [ ] **Premiere Pro Integration** - Direct import to Premiere timeline
- [ ] **CLIP-based matching** - AI-powered shot matching
- [ ] **Multi-source B-roll** - Pixabay, Unsplash fallbacks
- [ ] **Asset caching** - Local cache for frequently used clips
- [ ] **Smart selection** - ML model for best video selection
- [ ] **Metadata extraction** - Auto-tag videos with subjects, colors, mood
- [ ] **Template library** - Pre-built AE templates for common formats

---

## API Reference

### Quick Reference Links

- **Pexels Module:** See `PEXELS_INTEGRATION_GUIDE.md` for complete API reference
- **AE JSON Module:** See `AE_JSON_INTEGRATION_GUIDE.md` for complete API reference

### Key Functions

#### Pexels Integration

```python
# Convenience function
search_and_download_broll(shot_description, output_dir="./broll", 
                          orientation="landscape", quality="hd")

# Client methods
PexelsClient.search_videos(query, orientation, size, per_page, page)
PexelsClient.find_best_match(query, orientation, min_duration, max_duration)
PexelsClient.download_video(video_url, output_path)
PexelsClient.get_video_file_url(video_metadata, quality)
```

#### AE JSON Exporter

```python
# Convenience function
convert_blueprint_to_ae_json(blueprint_path, output_path, pretty=True)

# Class methods
AEJSONExporter.convert()
AEJSONExporter.hex_to_rgb(hex_color)
AEJSONExporter._extract_brand_colors()
AEJSONExporter._extract_typography()
AEJSONExporter._extract_text_layers()
```

---

## Support & Resources

### Documentation
- **Pexels API:** https://www.pexels.com/api/documentation/
- **After Effects Data-Driven Animation:** https://helpx.adobe.com/after-effects/using/data-driven-animations.html
- **Unwind Visual Cortex:** See `ROADMAP_INDEX.md`

### Getting Help
- Check troubleshooting sections in this guide
- Review individual module documentation
- Check tracking database for known issues

---

## License & Attribution

### Pexels Content
All Pexels videos are free for commercial and personal use. Attribution not required but appreciated.

### Module License
These integration modules are part of the Unwind Visual Cortex and follow the project's license.

---

## Conclusion

Phase 1 integration is complete and production-ready. The Pexels and After Effects integrations provide a solid foundation for automated video asset sourcing and data-driven motion graphics.

**Next Steps:**
- Phase 2: Premiere Pro automation
- Phase 3: MCP integration for enhanced intelligence
- Phase 4: Full end-to-end video assembly

---

**Status:** ✅ Phase 1 Complete  
**Last Updated:** January 11, 2026  
**Maintainer:** Unwind Visual Cortex Development Team  
**Created by:** Jesus Casares, founder of Unwind Code

---

*This documentation consolidates the Pexels and After Effects integrations into a unified workflow guide for Phase 1 of the Unwind Visual Cortex development roadmap.*

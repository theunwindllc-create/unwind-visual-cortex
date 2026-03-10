# Unwind Visual Cortex - After Effects JSON Integration Guide

**Version:** 1.0  
**Created:** January 10, 2026  
**Author:** Unwind Code - Jesus Casares

---

## Overview

The **AE JSON Exporter** module converts Unwind Visual Cortex blueprints into After Effects compatible JSON format. This enables data-driven animation workflows where video content is automatically populated from the AI-generated blueprint.

### What This Enables

- **Automated Text Updates**: Text layers pull content directly from JSON
- **Brand Color Consistency**: Colors are automatically applied from brand palette
- **Dynamic Timing**: Element timing is driven by emotional arc data
- **Scalable Production**: Change the JSON file to update all text/timing without touching AE
- **Template Reusability**: One AE template can be used for multiple videos

---

## Installation & Setup

### Prerequisites

- Python 3.11+
- After Effects CC 2020 or later (with data-driven animation support)
- Unwind Visual Cortex blueprint JSON file

### Module Location

```
/home/ubuntu/unwind_visual_cortex/ae_json_exporter.py
```

---

## Quick Start

### 1. Convert Blueprint to AE JSON

```python
from ae_json_exporter import convert_blueprint_to_ae_json

# Convert blueprint
ae_json_path = convert_blueprint_to_ae_json(
    blueprint_path="/path/to/blueprint.json",
    output_path="/path/to/output_ae.json",
    pretty=True
)

print(f"AE JSON saved to: {ae_json_path}")
```

### 2. Import JSON into After Effects

1. Open After Effects
2. Go to **File > Import > File**
3. Select your `output_ae.json` file
4. Click **Open**
5. The JSON file appears in your Project panel as footage

### 3. Use JSON Data in Expressions

Add this expression to any property to access the data:

```javascript
var unwindData = footage("output_ae.json").sourceData;
```

---

## JSON Structure

The exported AE JSON contains these sections:

### 1. Project Metadata

```json
{
  "project_metadata": {
    "project_name": "Brand name and description",
    "platform": "all",
    "conversion_goal": "leads",
    "target_audience": "Description of target audience",
    "generated_date": "2026-01-10T09:10:01.710731",
    "unwind_version": "1.0"
  }
}
```

### 2. Color Palette

Colors are provided in both hex and normalized RGB (0-1 range for AE):

```json
{
  "color_palette": {
    "primary": {
      "hex": "#0066FF",
      "rgb": [0.0, 0.4, 1.0],
      "name": "Primary"
    },
    "secondary": {
      "hex": "#00CCFF",
      "rgb": [0.0, 0.8, 1.0],
      "name": "Secondary"
    },
    "accent": {
      "hex": "#FF6B35",
      "rgb": [1.0, 0.42, 0.208],
      "name": "Accent"
    }
  }
}
```

### 3. Text Layers

Each text layer includes:

```json
{
  "text_layers": [
    {
      "layer_id": "text_01",
      "layer_name": "Text Layer 1",
      "text_content": "Your headline text here",
      "font_family": "Montserrat Bold",
      "font_size": 48,
      "color_hex": "#0066FF",
      "color_rgb": [0.0, 0.4, 1.0],
      "position": "top_third",
      "in_time": 0,
      "out_time": 10.0,
      "duration": 10.0,
      "style_notes": "Additional styling information"
    }
  ]
}
```

**Position Values:**
- `"top_third"` - Upper third of composition
- `"bottom_third"` - Lower third of composition
- `"center"` - Center of composition

### 4. B-Roll Clips

```json
{
  "broll_clips": [
    {
      "clip_id": "broll_01",
      "clip_name": "B-Roll 1",
      "description": "Detailed shot description",
      "shot_type": "Specific",
      "composition_rule": "Rule of Thirds",
      "emotion_alignment": "Frustration/Anger",
      "in_time": 0,
      "out_time": 10,
      "duration": 10,
      "file_path": "",
      "search_query": "Description for Pexels search"
    }
  ]
}
```

### 5. Motion Graphics

```json
{
  "motion_graphics": [
    {
      "element_id": "mg_01",
      "element_name": "Motion Graphics 1",
      "type": "animation",
      "description": "Animation description",
      "style": "Style notes",
      "in_time": 10,
      "out_time": 20,
      "duration": 10
    }
  ]
}
```

### 6. Emotional Timing

```json
{
  "timing": {
    "overall_tone": "Trust/Authority",
    "hook_strategy": "Hook description",
    "segments": [
      {
        "start_time": 0,
        "end_time": 10,
        "duration": 10,
        "emotion": "Frustration/Anger",
        "intensity": "Medium",
        "pacing": "Medium",
        "key_phrases": ["Key phrase 1", "Key phrase 2"]
      }
    ]
  }
}
```

### 7. Conversion Elements

```json
{
  "conversion_elements": {
    "ctas": [
      {
        "placement": "Post-roll",
        "in_time": 48,
        "cta_text": "Start your free trial now!",
        "visual_treatment": "Bold orange button with pulse effect",
        "psychological_trigger": "Reciprocity"
      }
    ]
  }
}
```

---

## After Effects Expression Examples

### Apply Brand Primary Color to Solid

For a **Solid Layer's Color** property:

```javascript
var unwindData = footage("output_ae.json").sourceData;
var primaryColor = unwindData.color_palette.primary.rgb;
primaryColor;
```

### Dynamic Text Content Based on Time

For a **Text Layer's Source Text** property:

```javascript
var unwindData = footage("output_ae.json").sourceData;
var textLayers = unwindData.text_layers;
var currentTime = time;

var displayText = "";
for (var i = 0; i < textLayers.length; i++) {
    if (currentTime >= textLayers[i].in_time && currentTime < textLayers[i].out_time) {
        displayText = textLayers[i].text_content;
        break;
    }
}

displayText;
```

### Set Text Color from JSON

For a **Text Layer's Fill Color** property:

```javascript
var unwindData = footage("output_ae.json").sourceData;
var textLayers = unwindData.text_layers;
var layerName = thisLayer.name;

var textColor = [1, 1, 1]; // default white
for (var i = 0; i < textLayers.length; i++) {
    if (textLayers[i].layer_name === layerName) {
        textColor = textLayers[i].color_rgb;
        break;
    }
}

textColor;
```

### Dynamic Font Size

For a **Text Layer's Font Size** property:

```javascript
var unwindData = footage("output_ae.json").sourceData;
var textLayers = unwindData.text_layers;
var layerName = thisLayer.name;

var fontSize = 48; // default
for (var i = 0; i < textLayers.length; i++) {
    if (textLayers[i].layer_name === layerName) {
        fontSize = textLayers[i].font_size;
        break;
    }
}

fontSize;
```

### Position Text Based on JSON

For a **Text Layer's Position** property:

```javascript
var unwindData = footage("output_ae.json").sourceData;
var textLayers = unwindData.text_layers;
var layerName = thisLayer.name;

var comp = thisComp;
var position = [comp.width / 2, comp.height / 2]; // default center

for (var i = 0; i < textLayers.length; i++) {
    if (textLayers[i].layer_name === layerName) {
        var posType = textLayers[i].position;
        
        if (posType === "top_third") {
            position = [comp.width / 2, comp.height / 3];
        } else if (posType === "bottom_third") {
            position = [comp.width / 2, (comp.height / 3) * 2];
        } else {
            position = [comp.width / 2, comp.height / 2];
        }
        break;
    }
}

position;
```

### Scale Based on Emotional Intensity

For a **Layer's Scale** property:

```javascript
var unwindData = footage("output_ae.json").sourceData;
var segments = unwindData.timing.segments;
var currentTime = time;

var intensity = "Medium";

for (var i = 0; i < segments.length; i++) {
    if (currentTime >= segments[i].start_time && currentTime < segments[i].end_time) {
        intensity = segments[i].intensity;
        break;
    }
}

var scale = 100;
if (intensity === "High") {
    scale = 120;
} else if (intensity === "Low") {
    scale = 80;
}

[scale, scale];
```

---

## Workflow: From Blueprint to Video

### Step 1: Generate Blueprint

Use the Unwind Visual Cortex AI Video Brain to analyze a brand and generate a blueprint:

```python
from ai_video_brain import AIVideoBrain

brain = AIVideoBrain()
blueprint = brain.analyze_brand_and_generate_blueprint(
    brand_url="https://example.com",
    platform="instagram_reels",
    conversion_goal="leads"
)

# Save blueprint
import json
with open('brand_blueprint.json', 'w') as f:
    json.dump(blueprint, f, indent=2)
```

### Step 2: Convert to AE JSON

```python
from ae_json_exporter import convert_blueprint_to_ae_json

ae_json_path = convert_blueprint_to_ae_json(
    blueprint_path="brand_blueprint.json",
    output_path="brand_ae.json"
)
```

### Step 3: Download B-Roll

```python
from pexels_integration import PexelsClient
import json

# Load AE JSON to get B-roll descriptions
with open('brand_ae.json', 'r') as f:
    ae_data = json.load(f)

client = PexelsClient()

for clip in ae_data['broll_clips']:
    query = clip['search_query']
    video_path = client.search_and_download_broll(
        shot_description=query,
        output_dir="/path/to/broll"
    )
    
    # Update clip file path
    clip['file_path'] = video_path

# Save updated JSON
with open('brand_ae.json', 'w') as f:
    json.dump(ae_data, f, indent=2)
```

### Step 4: Setup After Effects Template

1. Create a new composition (1080x1920 for vertical, 1920x1080 for horizontal)
2. Import the AE JSON file
3. Create text layers named exactly as in JSON (e.g., "Text Layer 1", "Text Layer 2")
4. Add expressions to each text layer's properties:
   - Source Text: Use dynamic text expression
   - Fill Color: Use color expression
   - Font Size: Use font size expression
   - Position: Use position expression
5. Import B-roll footage and arrange on timeline
6. Save as template

### Step 5: Update Content

To create a new video:

1. Generate new blueprint for different brand
2. Convert to AE JSON
3. Replace the JSON file in AE project (Right-click > Replace Footage > File)
4. All text, colors, and timing update automatically!
5. Render the composition

---

## API Reference

### Class: `AEJSONExporter`

#### Constructor

```python
AEJSONExporter(blueprint_path=None, blueprint_data=None)
```

**Parameters:**
- `blueprint_path` (str, optional): Path to Unwind blueprint JSON file
- `blueprint_data` (dict, optional): Direct blueprint dictionary

**Raises:**
- `ValueError`: If neither blueprint_path nor blueprint_data is provided

#### Methods

##### `export_full_json() -> Dict[str, Any]`

Export complete AE-compatible JSON structure.

**Returns:** Complete AE JSON dictionary

##### `save_to_file(output_path: str, pretty: bool = True) -> str`

Save AE JSON to file.

**Parameters:**
- `output_path` (str): Path to save JSON file
- `pretty` (bool): Whether to format JSON with indentation (default: True)

**Returns:** Path to saved file

##### `get_ae_expression_examples() -> str`

Generate example After Effects expressions for using the exported JSON.

**Returns:** String with example expressions in Markdown format

### Function: `convert_blueprint_to_ae_json`

```python
convert_blueprint_to_ae_json(
    blueprint_path: str,
    output_path: str = None,
    pretty: bool = True
) -> str
```

Convenience function to convert Unwind blueprint to AE JSON.

**Parameters:**
- `blueprint_path` (str): Path to Unwind blueprint JSON
- `output_path` (str, optional): Path to save AE JSON (defaults to same dir with `_ae` suffix)
- `pretty` (bool): Whether to format JSON with indentation (default: True)

**Returns:** Path to saved AE JSON file

**Example:**

```python
from ae_json_exporter import convert_blueprint_to_ae_json

output = convert_blueprint_to_ae_json(
    blueprint_path="/path/to/blueprint.json",
    output_path="/path/to/ae_data.json"
)

print(f"Saved to: {output}")
```

---

## Advanced Usage

### Custom Color Mapping

If you need to map colors differently:

```python
from ae_json_exporter import AEJSONExporter

exporter = AEJSONExporter(blueprint_path="blueprint.json")

# Modify color palette before export
exporter.ae_json['color_palette']['custom'] = {
    "hex": "#123456",
    "rgb": exporter._hex_to_rgb_normalized("#123456"),
    "name": "Custom Color"
}

# Export with custom modifications
exporter.save_to_file("custom_ae.json")
```

### Batch Processing

Convert multiple blueprints:

```python
import os
from ae_json_exporter import convert_blueprint_to_ae_json

blueprint_dir = "/path/to/blueprints"
output_dir = "/path/to/ae_jsons"

for filename in os.listdir(blueprint_dir):
    if filename.endswith('.json'):
        blueprint_path = os.path.join(blueprint_dir, filename)
        output_path = os.path.join(output_dir, filename.replace('.json', '_ae.json'))
        
        convert_blueprint_to_ae_json(blueprint_path, output_path)
        print(f"Converted: {filename}")
```

---

## Troubleshooting

### Issue: JSON not appearing in AE Project Panel

**Solution:** Make sure you're importing as **File**, not as **Composition**. The JSON should appear as footage with a document icon.

### Issue: Expression errors when accessing data

**Solution:** Check that:
1. The JSON filename in your expression matches the actual file
2. You're using `footage("filename.json").sourceData` correctly
3. The property path exists in the JSON (check with a text editor)

### Issue: Colors look wrong in AE

**Solution:** AE uses normalized RGB (0-1 range). The exporter automatically converts hex colors to this format. If colors still look wrong, check that you're applying the RGB array, not the hex string.

### Issue: Text not updating when JSON changes

**Solution:** After replacing the JSON file, you may need to:
1. Close and reopen the composition
2. Or toggle the expression off and on (click the expression stopwatch twice)

---

## Best Practices

### 1. Name Layers Consistently

Use the exact layer names from the JSON in your AE template. This makes expressions simpler and more reliable.

### 2. Use Master Properties

For repeated elements (like brand colors), create a master control layer with expressions that other layers reference.

### 3. Template Organization

Structure your AE template with clear layer organization:
```
- CONTROL (JSON data layer)
- TEXT LAYERS
  - Text Layer 1
  - Text Layer 2
  - Text Layer 3
- B-ROLL
  - B-Roll 1
  - B-Roll 2
- MOTION GRAPHICS
- BACKGROUND
```

### 4. Version Control

Keep your AE templates and JSON files in version control. Name them clearly:
```
template_v1.aep
brand_name_blueprint_v1.json
brand_name_ae_v1.json
```

### 5. Test with Sample Data

Before production, test your template with sample JSON to ensure all expressions work correctly.

---

## Integration with Pexels

The AE JSON includes `search_query` fields for each B-roll clip. Use these with the Pexels integration:

```python
from pexels_integration import search_and_download_broll
import json

# Load AE JSON
with open('brand_ae.json', 'r') as f:
    ae_data = json.load(f)

# Download all B-roll
for clip in ae_data['broll_clips']:
    video_path = search_and_download_broll(
        shot_description=clip['search_query'],
        output_dir="/home/ubuntu/unwind_visual_cortex/broll",
        quality="hd"
    )
    
    if video_path:
        clip['file_path'] = video_path
        print(f"✅ Downloaded: {clip['clip_name']}")

# Save updated JSON with file paths
with open('brand_ae_with_broll.json', 'w') as f:
    json.dump(ae_data, f, indent=2)
```

---

## Future Enhancements

Planned features for future versions:

- **MGJSON Export**: Support for Motion Graphics JSON format with data streams
- **Premiere Pro Integration**: Export to Premiere Pro compatible formats
- **Keyframe Generation**: Automatic keyframe creation from timing data
- **Template Marketplace**: Pre-built AE templates optimized for Unwind JSON
- **Real-time Preview**: Web-based preview of how JSON will look in video

---

## Support & Resources

- **Documentation**: This guide
- **Example Files**: 
  - `example_blueprint.json` - Sample Unwind blueprint
  - `example_ae.json` - Sample AE JSON output
  - `ae_expression_examples.md` - Expression library
- **Module Source**: `ae_json_exporter.py`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Jan 10, 2026 | Initial release with full blueprint to AE JSON conversion |

---

**Created by:** Jesus Casares, Unwind Code  
**Brain:** Unwind Visual Cortex  
**Status:** Production Ready ✅

---

*This integration enables seamless data-driven video production workflows, allowing you to scale video creation while maintaining brand consistency and emotional impact.*

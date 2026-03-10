"""
Unwind Visual Cortex - After Effects JSON Exporter
Converts Unwind blueprint JSON to After Effects data-driven animation format

This module transforms the comprehensive Unwind Visual Cortex blueprint
into a JSON structure that can be imported into After Effects and accessed
via expressions for data-driven animation.

Author: Unwind Code - Jesus Casares
Version: 1.0
Created: January 10, 2026
"""

import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime


class AEJSONExporter:
    """
    Converts Unwind Visual Cortex blueprints to After Effects compatible JSON
    """
    
    def __init__(self, blueprint_path: Optional[str] = None, blueprint_data: Optional[Dict] = None):
        """
        Initialize the AE JSON Exporter
        
        Args:
            blueprint_path: Path to Unwind blueprint JSON file
            blueprint_data: Direct blueprint dictionary (alternative to file path)
        """
        if blueprint_path:
            with open(blueprint_path, 'r', encoding='utf-8') as f:
                self.blueprint = json.load(f)
        elif blueprint_data:
            self.blueprint = blueprint_data
        else:
            raise ValueError("Must provide either blueprint_path or blueprint_data")
        
        self.ae_json = self._initialize_ae_structure()
    
    def _initialize_ae_structure(self) -> Dict[str, Any]:
        """Initialize the base AE JSON structure"""
        return {
            "project_metadata": {},
            "brand": {},
            "text_layers": [],
            "broll_clips": [],
            "motion_graphics": [],
            "color_palette": {},
            "timing": {},
            "conversion_elements": {}
        }
    
    def _hex_to_rgb_normalized(self, hex_color: str) -> List[float]:
        """
        Convert hex color to normalized RGB array for After Effects
        
        Args:
            hex_color: Hex color string (e.g., "#0066FF")
        
        Returns:
            List of normalized RGB values [r, g, b] where each value is 0-1
        """
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16) / 255.0
        g = int(hex_color[2:4], 16) / 255.0
        b = int(hex_color[4:6], 16) / 255.0
        return [round(r, 3), round(g, 3), round(b, 3)]
    
    def _parse_timestamp(self, timestamp: str) -> float:
        """
        Convert timestamp string to seconds
        
        Args:
            timestamp: Timestamp in format "0:00" or "0:00-0:10"
        
        Returns:
            Time in seconds as float
        """
        if '-' in timestamp:
            timestamp = timestamp.split('-')[0]
        
        parts = timestamp.split(':')
        if len(parts) == 2:
            minutes = int(parts[0])
            seconds = int(parts[1])
            return minutes * 60 + seconds
        return 0.0
    
    def _parse_duration(self, duration_str: str) -> float:
        """
        Parse duration string to seconds
        
        Args:
            duration_str: Duration like "10s" or "5"
        
        Returns:
            Duration in seconds
        """
        if isinstance(duration_str, (int, float)):
            return float(duration_str)
        
        duration_str = str(duration_str).lower().replace('s', '').strip()
        try:
            return float(duration_str)
        except ValueError:
            return 0.0
    
    def export_project_metadata(self) -> None:
        """Export project metadata section"""
        meta = self.blueprint.get('meta', {})
        brand = self.blueprint.get('brand_compliance_matrix', {})
        
        self.ae_json['project_metadata'] = {
            "project_name": brand.get('brand_summary', 'Unwind Video Project'),
            "platform": meta.get('platform', 'all'),
            "conversion_goal": meta.get('conversion_goal', 'leads'),
            "target_audience": brand.get('target_audience', 'General audience'),
            "generated_date": datetime.now().isoformat(),
            "unwind_version": "1.0"
        }
    
    def export_brand_colors(self) -> None:
        """Export brand color palette with RGB values for AE"""
        brand = self.blueprint.get('brand_compliance_matrix', {})
        colors = brand.get('color_palette', {})
        
        self.ae_json['color_palette'] = {
            "primary": {
                "hex": colors.get('primary_color', '#0066FF'),
                "rgb": self._hex_to_rgb_normalized(colors.get('primary_color', '#0066FF')),
                "name": "Primary"
            },
            "secondary": {
                "hex": colors.get('secondary_color', '#00CCFF'),
                "rgb": self._hex_to_rgb_normalized(colors.get('secondary_color', '#00CCFF')),
                "name": "Secondary"
            },
            "accent": {
                "hex": colors.get('accent_color', '#FF6B35'),
                "rgb": self._hex_to_rgb_normalized(colors.get('accent_color', '#FF6B35')),
                "name": "Accent"
            },
            "usage_ratio": colors.get('usage_ratio', '60-30-10 rule'),
            "emotional_mapping": colors.get('emotional_mapping', '')
        }
    
    def export_typography(self) -> None:
        """Export typography settings"""
        brand = self.blueprint.get('brand_compliance_matrix', {})
        typography = brand.get('typography', {})
        
        self.ae_json['brand']['typography'] = {
            "heading_font": typography.get('heading_font', 'Montserrat Bold'),
            "body_font": typography.get('body_font', 'Inter Regular'),
            "min_heading_size": 24,  # pixels for digital
            "min_body_size": 16,
            "contrast_ratio": typography.get('contrast_requirements', '4.5:1')
        }
    
    def export_text_layers(self) -> None:
        """Export text overlays as text layer data"""
        design = self.blueprint.get('design_composition_plan', {})
        motion_graphics = design.get('motion_graphics_plan', [])
        
        text_layers = []
        layer_index = 1
        
        for mg in motion_graphics:
            if mg.get('element_type') == 'text overlay':
                # Parse color from style description
                style = mg.get('style', '')
                color_hex = '#FFFFFF'  # default white
                
                if 'primary color' in style or '#0066FF' in style:
                    color_hex = self.blueprint['brand_compliance_matrix']['color_palette']['primary_color']
                elif 'accent color' in style or '#FF6B35' in style:
                    color_hex = self.blueprint['brand_compliance_matrix']['color_palette']['accent_color']
                elif 'secondary' in style or '#00CCFF' in style:
                    color_hex = self.blueprint['brand_compliance_matrix']['color_palette']['secondary_color']
                
                # Parse font from style
                font = 'Montserrat Bold'
                if 'Inter' in style:
                    font = 'Inter Regular'
                elif 'Montserrat' in style:
                    font = 'Montserrat Bold'
                
                # Parse size
                font_size = 48  # default
                if 'large' in style.lower():
                    font_size = 72
                elif 'small' in style.lower():
                    font_size = 24
                
                # Parse position
                position = 'center'
                if 'top third' in style.lower():
                    position = 'top_third'
                elif 'bottom third' in style.lower():
                    position = 'bottom_third'
                elif 'centered' in style.lower() or 'center' in style.lower():
                    position = 'center'
                
                in_time = self._parse_timestamp(mg.get('timestamp', '0:00'))
                duration = self._parse_duration(mg.get('duration', '5'))
                
                text_layers.append({
                    "layer_id": f"text_{layer_index:02d}",
                    "layer_name": f"Text Layer {layer_index}",
                    "text_content": mg.get('content', ''),
                    "font_family": font,
                    "font_size": font_size,
                    "color_hex": color_hex,
                    "color_rgb": self._hex_to_rgb_normalized(color_hex),
                    "position": position,
                    "in_time": in_time,
                    "out_time": in_time + duration,
                    "duration": duration,
                    "style_notes": style
                })
                
                layer_index += 1
        
        self.ae_json['text_layers'] = text_layers
    
    def export_broll_clips(self) -> None:
        """Export B-roll shot list with timing and descriptions"""
        design = self.blueprint.get('design_composition_plan', {})
        broll_list = design.get('b_roll_shot_list', [])
        
        clips = []
        clip_index = 1
        
        for shot in broll_list:
            timestamp_range = shot.get('timestamp', '0:00-0:10')
            in_time = self._parse_timestamp(timestamp_range.split('-')[0])
            out_time = self._parse_timestamp(timestamp_range.split('-')[1]) if '-' in timestamp_range else in_time + 10
            
            clips.append({
                "clip_id": f"broll_{clip_index:02d}",
                "clip_name": f"B-Roll {clip_index}",
                "description": shot.get('description', ''),
                "shot_type": shot.get('shot_type', 'Specific'),
                "composition_rule": shot.get('composition_rule', 'Rule of Thirds'),
                "emotion_alignment": shot.get('emotion_alignment', ''),
                "in_time": in_time,
                "out_time": out_time,
                "duration": out_time - in_time,
                "file_path": "",  # To be filled when B-roll is downloaded
                "search_query": shot.get('description', '')  # For Pexels search
            })
            
            clip_index += 1
        
        self.ae_json['broll_clips'] = clips
    
    def export_motion_graphics(self) -> None:
        """Export motion graphics elements (animations, transitions)"""
        design = self.blueprint.get('design_composition_plan', {})
        motion_graphics = design.get('motion_graphics_plan', [])
        
        mg_elements = []
        mg_index = 1
        
        for mg in motion_graphics:
            element_type = mg.get('element_type', '')
            
            if element_type in ['animation', 'transition']:
                in_time = self._parse_timestamp(mg.get('timestamp', '0:00'))
                duration = self._parse_duration(mg.get('duration', '5'))
                
                mg_elements.append({
                    "element_id": f"mg_{mg_index:02d}",
                    "element_name": f"Motion Graphics {mg_index}",
                    "type": element_type,
                    "description": mg.get('content', ''),
                    "style": mg.get('style', ''),
                    "in_time": in_time,
                    "out_time": in_time + duration,
                    "duration": duration
                })
                
                mg_index += 1
        
        self.ae_json['motion_graphics'] = mg_elements
    
    def export_emotional_timing(self) -> None:
        """Export emotional arc timing for pacing"""
        emotional = self.blueprint.get('emotional_arc_map', {})
        segments = emotional.get('emotional_segments', [])
        
        timing_data = {
            "overall_tone": emotional.get('overall_emotional_tone', 'Trust/Authority'),
            "hook_strategy": emotional.get('hook_strategy', ''),
            "climax_moment": emotional.get('climax_moment', ''),
            "editing_rhythm": emotional.get('editing_rhythm', ''),
            "segments": []
        }
        
        for segment in segments:
            timestamp_range = segment.get('timestamp_range', '0:00-0:10')
            start_time = self._parse_timestamp(timestamp_range.split('-')[0])
            end_time = self._parse_timestamp(timestamp_range.split('-')[1]) if '-' in timestamp_range else start_time + 10
            
            timing_data['segments'].append({
                "start_time": start_time,
                "end_time": end_time,
                "duration": end_time - start_time,
                "emotion": segment.get('dominant_emotion', ''),
                "intensity": segment.get('intensity', 'Medium'),
                "pacing": segment.get('pacing_recommendation', 'Medium'),
                "key_phrases": segment.get('key_phrases', [])
            })
        
        self.ae_json['timing'] = timing_data
    
    def export_conversion_elements(self) -> None:
        """Export CTAs and conversion optimization elements"""
        conversion = self.blueprint.get('conversion_optimization', {})
        cta_strategy = conversion.get('cta_strategy', [])
        
        ctas = []
        
        for cta in cta_strategy:
            in_time = self._parse_timestamp(cta.get('timestamp', '0:00'))
            
            ctas.append({
                "placement": cta.get('placement', 'Post-roll'),
                "in_time": in_time,
                "cta_text": cta.get('cta_text', ''),
                "visual_treatment": cta.get('visual_treatment', ''),
                "psychological_trigger": cta.get('psychological_trigger', 'Curiosity')
            })
        
        self.ae_json['conversion_elements'] = {
            "ctas": ctas,
            "hook_optimization": conversion.get('hook_optimization', {}),
            "psychological_triggers": conversion.get('psychological_triggers', {})
        }
    
    def export_full_json(self) -> Dict[str, Any]:
        """
        Export complete AE-compatible JSON
        
        Returns:
            Complete AE JSON structure
        """
        # Export all sections
        self.export_project_metadata()
        self.export_brand_colors()
        self.export_typography()
        self.export_text_layers()
        self.export_broll_clips()
        self.export_motion_graphics()
        self.export_emotional_timing()
        self.export_conversion_elements()
        
        return self.ae_json
    
    def save_to_file(self, output_path: str, pretty: bool = True) -> str:
        """
        Save AE JSON to file
        
        Args:
            output_path: Path to save JSON file
            pretty: Whether to format JSON with indentation
        
        Returns:
            Path to saved file
        """
        ae_data = self.export_full_json()
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            if pretty:
                json.dump(ae_data, f, indent=2, ensure_ascii=False)
            else:
                json.dump(ae_data, f, ensure_ascii=False)
        
        return output_path
    
    def get_ae_expression_examples(self) -> str:
        """
        Generate example After Effects expressions for using the exported JSON
        
        Returns:
            String with example expressions
        """
        examples = """
# After Effects Expression Examples for Unwind Visual Cortex JSON

## 1. Load the JSON Data

Place this in any property to load the JSON file:

```javascript
// Load Unwind JSON data
var unwindData = footage("unwind_ae_data.json").sourceData;
```

## 2. Apply Brand Colors to a Solid Layer

For a solid layer's color property:

```javascript
var unwindData = footage("unwind_ae_data.json").sourceData;
var primaryColor = unwindData.color_palette.primary.rgb;
primaryColor;
```

## 3. Animate Text Content Based on Time

For a text layer's Source Text property:

```javascript
var unwindData = footage("unwind_ae_data.json").sourceData;
var textLayers = unwindData.text_layers;
var currentTime = time;

// Find which text should be displayed at current time
var displayText = "";
for (var i = 0; i < textLayers.length; i++) {
    if (currentTime >= textLayers[i].in_time && currentTime < textLayers[i].out_time) {
        displayText = textLayers[i].text_content;
        break;
    }
}

displayText;
```

## 4. Set Text Color Based on Layer

For a text layer's Fill Color property:

```javascript
var unwindData = footage("unwind_ae_data.json").sourceData;
var textLayers = unwindData.text_layers;
var layerName = thisLayer.name;

// Find matching text layer
var textColor = [1, 1, 1]; // default white
for (var i = 0; i < textLayers.length; i++) {
    if (textLayers[i].layer_name === layerName) {
        textColor = textLayers[i].color_rgb;
        break;
    }
}

textColor;
```

## 5. Dynamic Font Size Based on JSON

For a text layer's Font Size property:

```javascript
var unwindData = footage("unwind_ae_data.json").sourceData;
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

## 6. Position Text Based on JSON Instructions

For a text layer's Position property:

```javascript
var unwindData = footage("unwind_ae_data.json").sourceData;
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

## 7. Get B-Roll Clip Description for Current Time

```javascript
var unwindData = footage("unwind_ae_data.json").sourceData;
var brollClips = unwindData.broll_clips;
var currentTime = time;

var description = "No B-roll for this time";
for (var i = 0; i < brollClips.length; i++) {
    if (currentTime >= brollClips[i].in_time && currentTime < brollClips[i].out_time) {
        description = brollClips[i].description;
        break;
    }
}

description;
```

## 8. Access Emotional Timing for Effects

```javascript
var unwindData = footage("unwind_ae_data.json").sourceData;
var segments = unwindData.timing.segments;
var currentTime = time;

var emotion = "neutral";
var intensity = "medium";

for (var i = 0; i < segments.length; i++) {
    if (currentTime >= segments[i].start_time && currentTime < segments[i].end_time) {
        emotion = segments[i].emotion;
        intensity = segments[i].intensity;
        break;
    }
}

// Use emotion and intensity to drive effects
// For example, scale based on intensity:
var scale = 100;
if (intensity === "High") {
    scale = 120;
} else if (intensity === "Low") {
    scale = 80;
}

[scale, scale];
```

---

**Note:** Replace "unwind_ae_data.json" with the actual filename of your exported JSON.
"""
        return examples


def convert_blueprint_to_ae_json(
    blueprint_path: str,
    output_path: str = None,
    pretty: bool = True
) -> str:
    """
    Convenience function to convert Unwind blueprint to AE JSON
    
    Args:
        blueprint_path: Path to Unwind blueprint JSON
        output_path: Path to save AE JSON (defaults to same dir with _ae suffix)
        pretty: Whether to format JSON with indentation
    
    Returns:
        Path to saved AE JSON file
    """
    if output_path is None:
        base_name = os.path.splitext(blueprint_path)[0]
        output_path = f"{base_name}_ae.json"
    
    exporter = AEJSONExporter(blueprint_path=blueprint_path)
    saved_path = exporter.save_to_file(output_path, pretty=pretty)
    
    print(f"✅ AE JSON exported successfully!")
    print(f"📁 Saved to: {saved_path}")
    print(f"📊 Text layers: {len(exporter.ae_json['text_layers'])}")
    print(f"🎬 B-roll clips: {len(exporter.ae_json['broll_clips'])}")
    print(f"✨ Motion graphics: {len(exporter.ae_json['motion_graphics'])}")
    
    return saved_path


# Example usage
if __name__ == "__main__":
    # Example: Convert the example blueprint
    blueprint_file = "/home/ubuntu/unwind_visual_cortex/example_blueprint.json"
    output_file = "/home/ubuntu/unwind_visual_cortex/example_ae.json"
    
    if os.path.exists(blueprint_file):
        convert_blueprint_to_ae_json(blueprint_file, output_file)
        
        # Also save expression examples
        exporter = AEJSONExporter(blueprint_path=blueprint_file)
        examples = exporter.get_ae_expression_examples()
        
        examples_path = "/home/ubuntu/unwind_visual_cortex/ae_expression_examples.md"
        with open(examples_path, 'w') as f:
            f.write(examples)
        
        print(f"📝 Expression examples saved to: {examples_path}")
    else:
        print(f"❌ Blueprint file not found: {blueprint_file}")

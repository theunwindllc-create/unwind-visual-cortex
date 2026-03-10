
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

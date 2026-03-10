# Premiere Pro Markers API Research - P2-T004

## Date: 2026-01-15
## Task: Create Marker System for CTAs

## Key Findings from Adobe Documentation

### Markers Class (Static Methods)
**Location:** `require('premierepro').Markers`

#### getMarkers() - Static Method (v25.0)
```typescript
getMarkers(markerOwnerObject: Sequence | ClipProjectItem): Markers
```
Returns the Markers object for a Sequence or ProjectItem.

### Markers Instance Methods

#### createAddMarkerAction() (v25.0)
```typescript
createAddMarkerAction(
  Name: string,
  markerType: string,
  startTime: TickTime,
  duration: TickTime
): Action
```
**Purpose:** Add a new marker  
**Returns:** Action object (must be executed in transaction)

**Parameters:**
- `Name`: Marker name/label
- `markerType`: Type of marker (e.g., "comment", "chapter", "weblink", "flashcue", "segmentation")
- `startTime`: TickTime object for marker start position
- `duration`: TickTime object for marker duration

#### createMoveMarkerAction() (v25.0)
```typescript
createMoveMarkerAction(
  marker: Marker,
  tickTime: TickTime
): Action
```
Move the given marker to new time value.

#### createRemoveMarkerAction() (v25.0)
```typescript
createRemoveMarkerAction(marker: Marker): Action
```
Remove the given marker.

#### getMarkers() - Instance Method (v25.0)
```typescript
getMarkers(filters?: string[]): Marker[]
```
Get all markers with optional type filtering.

## Implementation Pattern for Adding Markers

```typescript
const app = require('premierepro');
const project = await app.Project.getActiveProject();
const sequences = await project.getSequences();
const sequence = sequences.find(seq => seq.name === sequenceName);

// Get Markers API
const MarkersClass = app.Markers;
const markersInstance = MarkersClass.getMarkers(sequence);

// Get sequence settings for frame rate
const settings = await sequence.getSettings();
const frameRate = settings.videoFrameRate.framerate;

// Add markers in a transaction
await project.executeTransaction((compoundAction) => {
  for (const marker of markers) {
    // Convert timecode to TickTime
    const startTicks = timecodeToTicks(marker.time, frameRate);
    const durationTicks = timecodeToTicks(marker.duration || "00:00:00:01", frameRate);
    
    // Create add marker action
    const addMarkerAction = markersInstance.createAddMarkerAction(
      marker.name,
      marker.type || 'comment',
      startTicks,
      durationTicks
    );
    
    compoundAction.addAction(addMarkerAction);
  }
}, `Add ${markers.length} Markers`);
```

## Marker Types Available
Based on Adobe documentation:
- `comment` - Standard comment marker
- `chapter` - Chapter marker
- `weblink` - Web link marker
- `flashcue` - Flash cue point
- `segmentation` - Segmentation marker

For CTA (Call-to-Action) markers, we should use:
- **Primary choice:** `comment` type with descriptive name
- **Alternative:** `chapter` type if CTAs represent content sections

## TickTime Conversion
Premiere Pro uses TickTime for all temporal values:
- 254016000000 ticks per second
- Must convert timecode (HH:MM:SS:FF) to ticks
- Formula: `ticks = totalFrames * (254016000000 / frameRate)`

## Integration with Unwind Visual Cortex
The marker system should:
1. Accept CTA recommendations from Unwind Visual Cortex blueprint
2. Convert strategic timing to Premiere timecodes
3. Create markers at optimal engagement points
4. Include metadata: CTA type, message, target action

## Next Steps
1. ✅ Research Markers API (complete)
2. Update premiere_api.ts with correct Markers API usage
3. Create CTA marker data structure in types.d.ts
4. Implement marker placement logic
5. Test with mock data
6. Document implementation

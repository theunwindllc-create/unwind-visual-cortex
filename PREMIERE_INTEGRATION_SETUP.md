# Premiere Pro Integration - Setup & Usage Guide

## Overview

The Unwind Visual Cortex Premiere Pro integration enables automated video project generation directly from brand blueprints. This guide covers installation, setup, and usage of both the Python server and UXP plugin components.

## System Architecture

```
┌─────────────────────────────────────────┐
│   Unwind Visual Cortex (Python)         │
│   - Blueprint Generation                │
│   - Asset Management                    │
│   - Command Creation                    │
└──────────────┬──────────────────────────┘
               │
               │ WebSocket (JSON)
               │ ws://localhost:8765
               │
┌──────────────▼──────────────────────────┐
│   UXP Plugin (TypeScript/JavaScript)    │
│   - Command Handler                     │
│   - Premiere API Wrapper                │
└──────────────┬──────────────────────────┘
               │
               │ Premiere DOM API
               │
┌──────────────▼──────────────────────────┐
│   Adobe Premiere Pro                    │
│   - Project Management                  │
│   - Timeline Editing                    │
│   - Asset Import                        │
└─────────────────────────────────────────┘
```

## Prerequisites

### Software Requirements

1. **Adobe Premiere Pro**
   - Version: 25.0 or later
   - Recommended: Beta 25.3+ for full UXP API support
   - Download: [Adobe Creative Cloud](https://www.adobe.com/creativecloud.html)

2. **UXP Developer Tool**
   - Required for loading and debugging plugins
   - Download: [Adobe UXP Developer Tool](https://developer.adobe.com/photoshop/uxp/devtool/)

3. **Python**
   - Version: 3.10 or later
   - Already installed in Unwind Visual Cortex environment

4. **Node.js & npm**
   - Version: 18.0 or later
   - Download: [nodejs.org](https://nodejs.org/)

### Python Dependencies

Install required Python packages:

```bash
sudo pip3 install websockets
```

## Installation

### Part 1: Python Server Setup

The Python server is already created at:
```
/home/ubuntu/unwind_visual_cortex/premiere_integration.py
```

No additional setup required for the Python side.

### Part 2: UXP Plugin Setup

1. **Navigate to plugin directory:**
   ```bash
   cd /home/ubuntu/unwind_visual_cortex/premiere-unwind-plugin
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Build the plugin:**
   ```bash
   npm run build
   ```

   This compiles TypeScript to JavaScript in the `dist/` folder.

4. **Load plugin in UXP Developer Tool:**
   - Open UXP Developer Tool application
   - Click "Add Plugin" button
   - Navigate to `/home/ubuntu/unwind_visual_cortex/premiere-unwind-plugin/`
   - Select `manifest.json`
   - Click "Load"

5. **Verify plugin appears in Premiere Pro:**
   - Launch Adobe Premiere Pro
   - Go to: **Window > Extensions > Unwind Visual Cortex**
   - The plugin panel should open

## Usage

### Step 1: Start the Python WebSocket Server

Open a terminal and run:

```bash
cd /home/ubuntu/unwind_visual_cortex
python3 premiere_integration.py
```

You should see:
```
============================================================
Unwind Visual Cortex - Premiere Pro Integration Server
============================================================
Starting WebSocket server...
Press Ctrl+C to stop
============================================================
INFO - Starting Premiere Pro WebSocket server on localhost:8765
INFO - ✅ Server running on ws://localhost:8765
INFO - Waiting for UXP plugin connections...
```

**Keep this terminal open** while using the integration.

### Step 2: Connect the Plugin

1. Open Adobe Premiere Pro
2. Open the Unwind Visual Cortex panel: **Window > Extensions > Unwind Visual Cortex**
3. Click the **"Connect to Server"** button
4. Status should change to: **"🟢 Connected to server"**

You should see in the Python terminal:
```
INFO - Client connected from ('127.0.0.1', 54321). Total clients: 1
INFO - Plugin status: Plugin ready and connected
```

### Step 3: Test the Connection

In the plugin panel, click **"Send Test Command"**.

You should see:
- Plugin log: "Ping sent"
- Python terminal: "Received message: {'type': 'ping', ...}"

### Step 4: Generate a Project from Blueprint

Create a Python script to generate a project:

```python
import asyncio
from premiere_integration import PremiereWebSocketServer, PremiereProjectGenerator

async def generate_test_project():
    # Initialize server and generator
    server = PremiereWebSocketServer()
    generator = PremiereProjectGenerator(server)
    
    # Start server
    server_task = asyncio.create_task(server.start())
    
    # Wait for plugin to connect
    print("Waiting for plugin connection...")
    await asyncio.sleep(3)
    
    # Create project
    print("Creating project...")
    await generator.create_project(
        name="Test Video Project",
        location="/path/to/projects"
    )
    
    # Create sequence
    print("Creating sequence...")
    await generator.create_sequence(
        name="Main Sequence",
        width=1920,
        height=1080,
        frame_rate=30.0
    )
    
    # Import assets
    print("Importing assets...")
    await generator.import_assets(
        files=[
            "/path/to/video1.mp4",
            "/path/to/video2.mp4"
        ],
        bin_name="B-Roll"
    )
    
    # Add CTA markers
    print("Adding markers...")
    await generator.add_markers(
        sequence_name="Main Sequence",
        markers=[
            {
                'name': 'CTA - Subscribe',
                'time': '00:00:10:00',
                'duration': '00:00:03:00',
                'type': 'comment',
                'comment': 'Place subscribe button overlay'
            }
        ]
    )
    
    print("✅ Project generation complete!")

# Run the generator
asyncio.run(generate_test_project())
```

## Integration with Unwind Visual Cortex

### Generating Projects from Blueprints

```python
from ai_video_brain import UnwindVisualCortex
from premiere_integration import PremiereWebSocketServer, PremiereProjectGenerator
import asyncio

async def create_premiere_project_from_blueprint(brand_name: str, brand_description: str):
    # Generate blueprint using Unwind Visual Cortex
    brain = UnwindVisualCortex()
    blueprint = brain.generate_blueprint(brand_name, brand_description)
    
    # Initialize Premiere integration
    server = PremiereWebSocketServer()
    generator = PremiereProjectGenerator(server)
    
    # Start server
    asyncio.create_task(server.start())
    await asyncio.sleep(2)
    
    # Generate project from blueprint
    result = await generator.generate_project_from_blueprint(blueprint)
    
    return result

# Example usage
result = asyncio.run(create_premiere_project_from_blueprint(
    brand_name="TechStartup Inc",
    brand_description="Innovative AI-powered productivity tools for remote teams"
))

print(result)
```

## Command Reference

### Available Commands

#### createProject
Create a new Premiere Pro project.

```python
await generator.create_project(
    name="Project Name",
    location="/path/to/projects"
)
```

#### createSequence
Create a new sequence in the active project.

```python
await generator.create_sequence(
    name="Main Sequence",
    width=1920,
    height=1080,
    frame_rate=30.0,
    audio_sample_rate=48000
)
```

#### importAssets
Import video/audio files into the project.

```python
await generator.import_assets(
    files=["/path/to/video1.mp4", "/path/to/video2.mp4"],
    bin_name="B-Roll",
    create_bin=True
)
```

#### addMarkers
Add markers to a sequence for CTAs and annotations.

```python
await generator.add_markers(
    sequence_name="Main Sequence",
    markers=[
        {
            'name': 'CTA - Subscribe',
            'time': '00:00:10:00',
            'duration': '00:00:03:00',
            'type': 'comment',
            'comment': 'Place subscribe button overlay'
        }
    ]
)
```

#### addClipToTimeline
Add a clip to the timeline.

```python
await generator.add_clip_to_timeline(
    sequence_name="Main Sequence",
    clip_path="/path/to/video.mp4",
    track_index=1,
    start_time="00:00:05:00"
)
```

## Troubleshooting

### Plugin Won't Load

**Problem:** Plugin doesn't appear in UXP Developer Tool

**Solutions:**
- Verify `manifest.json` exists and is valid JSON
- Check that Premiere Pro 25.0+ is installed
- Restart UXP Developer Tool
- Check console for TypeScript compilation errors

### Can't Connect to Server

**Problem:** "Failed to connect to server" error

**Solutions:**
- Ensure Python server is running: `python3 premiere_integration.py`
- Check that port 8765 is not in use: `lsof -i :8765`
- Verify firewall isn't blocking WebSocket connections
- Check server URL in plugin matches: `ws://localhost:8765`

### Commands Not Executing

**Problem:** Commands sent but nothing happens in Premiere

**Solutions:**
- Open Chrome DevTools (via UXP Developer Tool) and check console
- Verify Premiere Pro has an active project open
- Check that command parameters are correct
- Review Python server logs for errors

### WebSocket Disconnects

**Problem:** Connection drops after a few minutes

**Solutions:**
- Implement ping/pong keep-alive (already included)
- Check network stability
- Review server logs for errors
- Restart both server and plugin

## Development Notes

### Current Implementation Status

**✅ Completed (P2-T002):**
- Python WebSocket server with command queue
- UXP plugin scaffold with TypeScript
- WebSocket communication layer
- Command handler and routing
- Basic UI with connection status
- Mock Premiere API wrapper

**🔄 Next Steps (P2-T003, P2-T004):**
- Replace mock API calls with actual Premiere DOM API
- Implement real asset import functionality
- Test marker placement with actual sequences
- Add error handling and recovery
- Performance optimization

### Testing the Integration

1. **Test WebSocket Connection:**
   - Start server
   - Connect plugin
   - Send ping command
   - Verify pong response

2. **Test Command Routing:**
   - Send each command type
   - Verify handler receives and processes
   - Check response structure

3. **Test Premiere API (when implemented):**
   - Create actual project in Premiere
   - Import real video files
   - Place markers on timeline
   - Verify all operations succeed

## Next Development Tasks

From the roadmap (Phase 2):

1. **P2-T003:** Implement Asset Import Automation
2. **P2-T004:** Create Marker System for CTAs
3. **P2-T005:** Build Timeline Assembly Logic
4. **P2-T006:** Test & Document Integration

## Resources

- [Adobe UXP Documentation](https://developer.adobe.com/premiere-pro/docs/uxp/)
- [Premiere Pro DOM API Reference](https://developer.adobe.com/premiere-pro/docs/api/)
- [WebSocket Protocol Specification](PREMIERE_UXP_TECHNICAL_SPEC.md)
- [GitHub Reference: morim3/mcp_adobe_premiere](https://github.com/morim3/mcp_adobe_premiere)

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the technical specification: `PREMIERE_UXP_TECHNICAL_SPEC.md`
3. Check plugin logs in Chrome DevTools
4. Review Python server logs

---

**Status:** Phase 2, Task P2-T002 Complete ✅  
**Next Task:** P2-T003 - Implement Asset Import Automation  
**Integration Version:** 1.0.0

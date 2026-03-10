# Unwind Visual Cortex - Premiere Pro UXP Plugin

This plugin enables communication between the Unwind Visual Cortex brain (Python) and Adobe Premiere Pro via WebSocket connection.

## Overview

The plugin acts as a bridge, receiving commands from the Python server and translating them into Premiere Pro DOM API calls. This enables automated project generation, asset import, marker placement, and timeline editing.

## Architecture

```
Python Server (premiere_integration.py)
    ↓ WebSocket (JSON commands)
UXP Plugin (TypeScript)
    ↓ Premiere DOM API
Adobe Premiere Pro
```

## Installation

### Prerequisites

- Adobe Premiere Pro 25.0 or later (Beta 25.3+ recommended)
- UXP Developer Tool
- Node.js 18+ and npm

### Setup Steps

1. **Install dependencies:**
   ```bash
   cd premiere-unwind-plugin
   npm install
   ```

2. **Build the plugin:**
   ```bash
   npm run build
   ```

3. **Load in UXP Developer Tool:**
   - Open UXP Developer Tool
   - Click "Add Plugin"
   - Navigate to the `premiere-unwind-plugin` folder
   - Select `manifest.json`
   - Click "Load"

4. **Open in Premiere Pro:**
   - Launch Adobe Premiere Pro
   - Go to Window > Extensions > Unwind Visual Cortex
   - The plugin panel will appear

## Usage

### Starting the Python Server

First, start the WebSocket server:

```bash
cd /path/to/unwind_visual_cortex
python3 premiere_integration.py
```

The server will start on `ws://localhost:8765`.

### Connecting the Plugin

1. Open the Unwind Visual Cortex panel in Premiere Pro
2. Click "Connect to Server"
3. The status should change to "🟢 Connected to server"

### Sending Commands

From Python, you can now send commands:

```python
from premiere_integration import PremiereWebSocketServer, PremiereProjectGenerator
import asyncio

async def main():
    server = PremiereWebSocketServer()
    generator = PremiereProjectGenerator(server)
    
    # Start server in background
    asyncio.create_task(server.start())
    
    # Wait for plugin to connect
    await asyncio.sleep(2)
    
    # Create a project
    await generator.create_project("My Video Project", "/path/to/projects")
    
    # Create a sequence
    await generator.create_sequence("Main Sequence", 1920, 1080, 30.0)
    
    # Import assets
    await generator.import_assets([
        "/path/to/video1.mp4",
        "/path/to/video2.mp4"
    ], bin_name="B-Roll")

asyncio.run(main())
```

## Development

### File Structure

```
premiere-unwind-plugin/
├── manifest.json           # Plugin metadata
├── index.html              # Plugin UI
├── package.json            # npm configuration
├── tsconfig.json           # TypeScript config
├── webpack.config.js       # Build config
├── README.md               # This file
└── src/
    ├── index.ts            # Main entry point
    ├── websocket_client.ts # WebSocket communication
    ├── command_handler.ts  # Command routing
    ├── premiere_api.ts     # Premiere API wrapper
    └── types.d.ts          # TypeScript types
```

### Building

- **Development build (with watch):**
  ```bash
  npm run dev
  ```

- **Production build:**
  ```bash
  npm run build
  ```

### Debugging

1. Open UXP Developer Tool
2. Select the loaded plugin
3. Click "Debug" to open Chrome DevTools
4. View console logs and debug TypeScript code

## Supported Commands

### Project Management
- `createProject` - Create a new project
- `openProject` - Open an existing project

### Sequence Management
- `createSequence` - Create a new sequence
- `getSequenceInfo` - Get sequence information

### Asset Management
- `importAssets` - Import video/audio files

### Timeline Editing
- `addMarkers` - Add CTA markers
- `addClipToTimeline` - Add clips to timeline

## Implementation Status

### ✅ Phase 1: Foundation (P2-T002)
- [x] WebSocket client implementation
- [x] Command handler with routing
- [x] Premiere API wrapper (scaffold)
- [x] Plugin UI with connection status
- [x] Basic communication test

### 🔄 Phase 2: Core Features (P2-T003, P2-T004)
- [ ] Actual Premiere DOM API integration
- [ ] Asset import functionality
- [ ] Marker placement system
- [ ] Timeline editing capabilities

### 📋 Phase 3: Advanced Features (P2-T005, P2-T006)
- [ ] Blueprint-to-project automation
- [ ] Error handling and recovery
- [ ] Performance optimization
- [ ] Comprehensive testing

## Notes

- The current implementation uses mock Premiere API calls for development
- Replace mock functions in `premiere_api.ts` with actual `premierepro` module calls
- Requires Premiere Pro Beta 25.3+ for full UXP API support
- WebSocket connection defaults to `localhost:8765` (configurable)

## Troubleshooting

**Plugin won't load:**
- Ensure Premiere Pro 25.0+ is installed
- Check that all TypeScript files compiled successfully
- Verify `manifest.json` is valid

**Can't connect to server:**
- Ensure Python server is running: `python3 premiere_integration.py`
- Check that port 8765 is not blocked by firewall
- Verify WebSocket URL in plugin matches server address

**Commands not executing:**
- Check Chrome DevTools console for errors
- Verify command structure matches protocol specification
- Ensure Premiere Pro has an active project open (for some commands)

## License

MIT License - Part of Unwind Visual Cortex Brain

## Author

Unwind Code - Jesus Casares

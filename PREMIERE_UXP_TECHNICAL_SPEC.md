# Adobe Premiere Pro UXP Integration - Technical Specification
## Unwind Visual Cortex Phase 2

**Document Version:** 1.0  
**Created:** 2026-01-12  
**Task:** P2-T001 - Research Premiere Pro UXP API  
**Agent:** Manus-AutoDaily-20260112

---

## Executive Summary

This document provides a comprehensive technical specification for integrating Adobe Premiere Pro with the Unwind Visual Cortex brain using the UXP (Unified Extensibility Platform) API. The integration enables automated video project generation, asset import, marker placement, and sequence creation based on Unwind Visual Cortex blueprints.

---

## 1. Technology Stack

### 1.1 UXP Plugin (Frontend)
- **Language:** TypeScript/JavaScript (ES6+)
- **Platform:** Adobe UXP (Unified Extensibility Platform)
- **Minimum Premiere Version:** 25.0 (Beta 25.3+ recommended)
- **Build Tool:** Webpack
- **Package Manager:** npm
- **Development Tool:** UXP Developer Tool

### 1.2 Python Backend (Unwind Visual Cortex)
- **Language:** Python 3.10+
- **Communication:** WebSocket or HTTP REST API
- **Framework:** FastAPI (recommended)
- **Libraries:**
  - `websockets` or `fastapi` for communication
  - `fastmcp` for MCP integration (optional)
  - Existing Unwind Visual Cortex dependencies

### 1.3 Communication Protocol
- **Format:** JSON
- **Transport:** WebSocket (real-time) or HTTP REST (polling)
- **Direction:** Bidirectional (Python ↔ UXP Plugin)

---

## 2. System Architecture

### 2.1 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                 Unwind Visual Cortex (Python)               │
│  - Brand Analysis                                           │
│  - Blueprint Generation                                     │
│  - Shot List Creation                                       │
│  - Asset Management (Pexels Integration)                    │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ WebSocket/HTTP (JSON Commands)
                 │
┌────────────────▼────────────────────────────────────────────┐
│              WebSocket/HTTP Server (Python)                 │
│  - Command Queue Management                                 │
│  - Request/Response Handling                                │
│  - Status Tracking                                          │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ WebSocket/HTTP (JSON)
                 │
┌────────────────▼────────────────────────────────────────────┐
│           UXP Plugin (TypeScript/JavaScript)                │
│  - WebSocket/HTTP Client                                    │
│  - Command Parser                                           │
│  - Premiere DOM API Wrapper                                 │
└────────────────┬────────────────────────────────────────────┘
                 │
                 │ Premiere DOM API (JavaScript)
                 │
┌────────────────▼────────────────────────────────────────────┐
│                 Adobe Premiere Pro                          │
│  - Project Management                                       │
│  - Sequence Creation                                        │
│  - Asset Import                                             │
│  - Marker Placement                                         │
│  - Timeline Editing                                         │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 Data Flow

1. **Blueprint Generation:** Unwind Visual Cortex analyzes brand and generates video blueprint
2. **Command Creation:** Python module creates structured commands from blueprint
3. **Command Transmission:** Commands sent to UXP plugin via WebSocket/HTTP
4. **Command Execution:** UXP plugin translates commands to Premiere DOM API calls
5. **Status Response:** Plugin returns execution status and results to Python
6. **Completion:** Python module receives confirmation and logs results

---

## 3. Premiere Pro UXP API Capabilities

### 3.1 Core Objects

#### Application (`app`)
```javascript
const app = require('premierepro');
```
Entry point to all Premiere objects and methods.

#### Project
```javascript
const project = await app.Project.getActiveProject();
```
**Capabilities:**
- Get active project
- Access project items
- Manage project settings
- Import assets

#### Sequence
```javascript
const sequence = await project.getActiveSequence();
```
**Properties:**
- `guid` (Guid, Read-only): Unique identifier
- `name` (string, Read-only): Sequence name

**Key Methods:**
- `getVideoTrackCount()`: Get number of video tracks
- `getAudioTrackCount()`: Get number of audio tracks
- `getVideoTrack(trackIndex)`: Access specific video track
- `getAudioTrack(trackIndex)`: Access specific audio track
- `getSettings()`: Get sequence settings (resolution, frame rate, etc.)
- `setPlayerPosition(tickTime)`: Set playhead position
- `getPlayerPosition()`: Get current playhead position
- `getInPoint()`: Get sequence in point
- `getOutPoint()`: Get sequence out point
- `createSubsequence(ignoreTrackTargeting)`: Create subsequence from selection
- `getSelection()`: Get current track item selection
- `setSelection(trackItemSelection)`: Set track item selection

#### Markers
```javascript
const markers = Markers.getMarkers(sequence);
```
**Static Methods:**
- `getMarkers(markerOwnerObject)`: Get markers for sequence or project item

**Instance Methods:**
- `createAddMarkerAction(name, markerType, startTime, duration)`: Create action to add marker
  - `name` (string): Marker name
  - `markerType` (string): Type of marker
  - `startTime` (TickTime): Start time
  - `duration` (TickTime): Duration

### 3.2 Asynchronous vs Synchronous

**Critical Distinction:**
- **Properties (get/set):** Synchronous (no `await` needed)
- **Methods:** Asynchronous (require `await`)

Example:
```javascript
// Synchronous property access
const name = sequence.name;

// Asynchronous method call
const project = await app.Project.getActiveProject();
```

### 3.3 Limitations Identified

1. **No Direct Sequence Creation:** API does not expose a direct `createSequence()` method
   - Workaround: Use `SequenceUtils` or create from template
   
2. **Limited Track Manipulation:** Cannot move clips between tracks programmatically
   - Clips must be placed on correct track initially
   
3. **No Direct Python Execution:** UXP cannot run Python scripts natively
   - Requires WebSocket/HTTP communication layer

---

## 4. Python-UXP Communication Protocol

### 4.1 Command Structure

All commands follow this JSON structure:

```json
{
  "command_id": "unique-uuid",
  "action": "action_name",
  "parameters": {
    "param1": "value1",
    "param2": "value2"
  },
  "timestamp": "2026-01-12T09:00:00Z"
}
```

### 4.2 Response Structure

```json
{
  "command_id": "unique-uuid",
  "status": "success" | "error" | "pending",
  "result": {
    "data": "result_data"
  },
  "error": {
    "code": "error_code",
    "message": "error_message"
  },
  "timestamp": "2026-01-12T09:00:01Z"
}
```

### 4.3 Supported Actions

#### 4.3.1 Project Management

**Action: `createProject`**
```json
{
  "action": "createProject",
  "parameters": {
    "name": "Project Name",
    "location": "/path/to/project"
  }
}
```

**Action: `openProject`**
```json
{
  "action": "openProject",
  "parameters": {
    "path": "/path/to/project.prproj"
  }
}
```

#### 4.3.2 Sequence Management

**Action: `createSequence`**
```json
{
  "action": "createSequence",
  "parameters": {
    "name": "Main Sequence",
    "width": 1920,
    "height": 1080,
    "frameRate": 30,
    "audioSampleRate": 48000
  }
}
```

**Action: `getSequenceInfo`**
```json
{
  "action": "getSequenceInfo",
  "parameters": {
    "sequenceName": "Main Sequence"
  }
}
```

#### 4.3.3 Asset Import

**Action: `importAssets`**
```json
{
  "action": "importAssets",
  "parameters": {
    "files": [
      "/path/to/video1.mp4",
      "/path/to/video2.mp4"
    ],
    "binName": "B-Roll",
    "createBin": true
  }
}
```

#### 4.3.4 Marker Placement

**Action: `addMarkers`**
```json
{
  "action": "addMarkers",
  "parameters": {
    "sequenceName": "Main Sequence",
    "markers": [
      {
        "name": "CTA - Subscribe",
        "time": "00:00:10:00",
        "duration": "00:00:03:00",
        "type": "comment",
        "comment": "Place subscribe button overlay"
      },
      {
        "name": "CTA - Like",
        "time": "00:00:45:00",
        "duration": "00:00:03:00",
        "type": "comment",
        "comment": "Place like button overlay"
      }
    ]
  }
}
```

#### 4.3.5 Timeline Editing

**Action: `addClipToTimeline`**
```json
{
  "action": "addClipToTimeline",
  "parameters": {
    "sequenceName": "Main Sequence",
    "clipPath": "/path/to/video.mp4",
    "trackIndex": 1,
    "startTime": "00:00:05:00"
  }
}
```

---

## 5. UXP Plugin Implementation

### 5.1 Plugin Structure

```
premiere-unwind-plugin/
├── manifest.json           # Plugin metadata and permissions
├── index.html              # Plugin UI (optional)
├── package.json            # npm dependencies
├── tsconfig.json           # TypeScript configuration
├── webpack.config.js       # Build configuration
└── src/
    ├── index.ts            # Plugin entry point
    ├── websocket_client.ts # WebSocket communication
    ├── command_handler.ts  # Command parsing and routing
    ├── premiere_api.ts     # Premiere DOM API wrapper
    └── types.d.ts          # TypeScript type definitions
```

### 5.2 Manifest Example (`manifest.json`)

```json
{
  "id": "com.unwindcode.premiere.visualcortex",
  "name": "Unwind Visual Cortex",
  "version": "1.0.0",
  "host": {
    "app": "PPRO",
    "minVersion": "25.0"
  },
  "entrypoints": [
    {
      "type": "panel",
      "id": "unwind.panel",
      "label": "Visual Cortex"
    }
  ],
  "requiredPermissions": [
    "network",
    "localFileSystem",
    "clipboard"
  ]
}
```

### 5.3 WebSocket Client Example

```typescript
// src/websocket_client.ts
export class WebSocketClient {
  private ws: WebSocket | null = null;
  private serverUrl: string;

  constructor(serverUrl: string = 'ws://localhost:8765') {
    this.serverUrl = serverUrl;
  }

  async connect(): Promise<void> {
    return new Promise((resolve, reject) => {
      this.ws = new WebSocket(this.serverUrl);
      
      this.ws.onopen = () => {
        console.log('Connected to Unwind Visual Cortex server');
        resolve();
      };
      
      this.ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        reject(error);
      };
      
      this.ws.onmessage = (event) => {
        const command = JSON.parse(event.data);
        this.handleCommand(command);
      };
    });
  }

  async handleCommand(command: any): Promise<void> {
    // Route to appropriate handler
    const handler = new CommandHandler();
    const result = await handler.execute(command);
    this.sendResponse(result);
  }

  sendResponse(response: any): void {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(response));
    }
  }
}
```

---

## 6. Python Server Implementation

### 6.1 WebSocket Server Example

```python
# server/websocket_server.py
import asyncio
import websockets
import json
from typing import Dict, Any

class PremiereWebSocketServer:
    def __init__(self, host: str = 'localhost', port: int = 8765):
        self.host = host
        self.port = port
        self.clients = set()
        
    async def register(self, websocket):
        self.clients.add(websocket)
        print(f"Client connected. Total clients: {len(self.clients)}")
        
    async def unregister(self, websocket):
        self.clients.remove(websocket)
        print(f"Client disconnected. Total clients: {len(self.clients)}")
        
    async def send_command(self, command: Dict[str, Any]):
        if self.clients:
            message = json.dumps(command)
            await asyncio.gather(
                *[client.send(message) for client in self.clients]
            )
            
    async def handler(self, websocket, path):
        await self.register(websocket)
        try:
            async for message in websocket:
                response = json.loads(message)
                print(f"Received response: {response}")
                # Process response from UXP plugin
        finally:
            await self.unregister(websocket)
            
    async def start(self):
        async with websockets.serve(self.handler, self.host, self.port):
            print(f"WebSocket server started on ws://{self.host}:{self.port}")
            await asyncio.Future()  # Run forever
```

### 6.2 Integration with Unwind Visual Cortex

```python
# premiere_integration.py
import asyncio
from websocket_server import PremiereWebSocketServer

class PremiereIntegration:
    def __init__(self):
        self.server = PremiereWebSocketServer()
        
    async def create_project_from_blueprint(self, blueprint: dict):
        """
        Generate Premiere Pro project from Unwind Visual Cortex blueprint
        """
        # Extract blueprint data
        project_name = blueprint['project_name']
        sequences = blueprint['sequences']
        assets = blueprint['assets']
        markers = blueprint['cta_markers']
        
        # Send create project command
        await self.server.send_command({
            'command_id': str(uuid.uuid4()),
            'action': 'createProject',
            'parameters': {
                'name': project_name,
                'location': '/path/to/projects'
            }
        })
        
        # Import assets
        await self.server.send_command({
            'command_id': str(uuid.uuid4()),
            'action': 'importAssets',
            'parameters': {
                'files': [asset['path'] for asset in assets],
                'binName': 'B-Roll',
                'createBin': True
            }
        })
        
        # Add markers
        await self.server.send_command({
            'command_id': str(uuid.uuid4()),
            'action': 'addMarkers',
            'parameters': {
                'sequenceName': 'Main Sequence',
                'markers': markers
            }
        })
```

---

## 7. Implementation Phases

### Phase 1: Foundation (P2-T001, P2-T002)
- ✅ Research UXP API (P2-T001 - CURRENT)
- ⏭️ Create UXP plugin scaffold (P2-T002)
- ⏭️ Implement WebSocket communication layer
- ⏭️ Build basic Premiere DOM API wrapper

### Phase 2: Core Functionality (P2-T003, P2-T004)
- ⏭️ Implement asset import automation (P2-T003)
- ⏭️ Build marker placement system (P2-T004)
- ⏭️ Create sequence management functions

### Phase 3: Advanced Features (P2-T005)
- ⏭️ Develop sequence template system (P2-T005)
- ⏭️ Implement timeline editing functions
- ⏭️ Add error handling and recovery

### Phase 4: Integration & Testing (P2-T006)
- ⏭️ Integrate with Unwind Visual Cortex (P2-T006)
- ⏭️ End-to-end testing
- ⏭️ Performance optimization
- ⏭️ Documentation

---

## 8. Authentication & Security

### 8.1 Local Communication
- WebSocket server runs on `localhost` only
- No external network access required
- UXP plugin connects to local server

### 8.2 Permissions
UXP plugin requires:
- `network`: For WebSocket communication
- `localFileSystem`: For asset import
- `clipboard`: For copy/paste operations (optional)

---

## 9. Error Handling

### 9.1 Connection Errors
- Retry logic for WebSocket connection
- Fallback to HTTP polling if WebSocket fails
- User notification if server unreachable

### 9.2 Command Errors
- Validate commands before execution
- Return detailed error messages
- Log all errors for debugging

### 9.3 Premiere Pro Errors
- Catch Premiere DOM API exceptions
- Provide user-friendly error messages
- Implement rollback for failed operations

---

## 10. Performance Considerations

### 10.1 Asynchronous Operations
- All Premiere DOM API methods are async
- Use `await` properly to avoid blocking
- Batch operations where possible

### 10.2 Large Asset Imports
- Import assets in batches
- Show progress indicators
- Handle timeouts gracefully

### 10.3 Memory Management
- Clean up WebSocket connections
- Release Premiere objects when done
- Monitor plugin memory usage

---

## 11. Testing Strategy

### 11.1 Unit Tests
- Test command parsing
- Test WebSocket communication
- Test Premiere API wrappers

### 11.2 Integration Tests
- Test end-to-end workflow
- Test with real Premiere Pro projects
- Test with various blueprint configurations

### 11.3 Manual Testing
- Test UI responsiveness
- Test error scenarios
- Test with different Premiere versions

---

## 12. Documentation Requirements

### 12.1 Developer Documentation
- API reference for UXP plugin
- WebSocket protocol specification
- Integration guide for Unwind Visual Cortex

### 12.2 User Documentation
- Installation guide
- Configuration instructions
- Troubleshooting guide

---

## 13. Future Enhancements

### 13.1 Advanced Timeline Editing
- Automated clip arrangement
- Transition application
- Effect application

### 13.2 Template System
- Reusable project templates
- Sequence presets
- Effect presets

### 13.3 Real-time Preview
- Live preview of changes
- Thumbnail generation
- Progress tracking

---

## 14. References

### Official Documentation
- [Adobe Premiere Pro UXP API](https://developer.adobe.com/premiere-pro/uxp/)
- [Premiere DOM API Reference](https://developer.adobe.com/premiere-pro/uxp/ppro_reference/)
- [UXP JavaScript API](https://developer.adobe.com/photoshop/uxp/2022/uxp-api/)

### Community Resources
- [Adobe Community Forums](https://community.adobe.com/t5/premiere-pro/ct-p/ct-premiere-pro)
- [MCP Adobe Premiere (morim3)](https://github.com/morim3/mcp_adobe_premiere)

### Related Unwind Documents
- `PHASE_1_INTEGRATION_GUIDE.md` - Pexels and AE JSON integration
- `ROADMAP_INDEX.md` - Overall enhancement roadmap
- `tracking_database.json` - Project tracking

---

## 15. Conclusion

The Adobe Premiere Pro UXP API provides robust capabilities for programmatic control of Premiere Pro. While direct Python integration is not possible, a WebSocket-based architecture enables seamless communication between Unwind Visual Cortex (Python) and Premiere Pro (via UXP plugin).

**Key Takeaways:**
1. UXP is JavaScript-based; Python integration requires communication layer
2. WebSocket architecture is proven (see morim3/mcp_adobe_premiere)
3. Premiere DOM API provides access to sequences, tracks, markers, and project items
4. Asynchronous programming model requires careful `await` usage
5. Plugin development requires UXP Developer Tool and Premiere Pro Beta 25.3+

**Next Steps:**
- Proceed to P2-T002: Build Premiere Pro Project Generator
- Implement WebSocket server and UXP plugin scaffold
- Test basic communication and Premiere API access

---

**Document Status:** ✅ Complete  
**Research Task P2-T001:** Ready for completion  
**Next Task:** P2-T002 - Build Premiere Pro Project Generator

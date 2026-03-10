# Adobe Premiere Pro UXP API Research Notes
## Task P2-T001 - Research Session

**Date:** 2026-01-12  
**Agent:** Manus-AutoDaily-20260112  
**Source:** https://developer.adobe.com/premiere-pro/uxp/

---

## What is UXP?

**UXP** = **U**nified e**X**tensibility **P**latform

### Core Characteristics
- Modern integration framework built into Premiere Pro and other Adobe Creative Cloud applications
- Powered by a modern JavaScript engine (ES6/ECMAScript 2015 compliant)
- Provides programmatic access to Premiere Pro functions
- Allows building custom tools that integrate with and optimize workflows
- Transforms Premiere into a bespoke application tailored to specific project needs

### Architecture
- **Base UXP functionality** (provided by Adobe)
- **Premiere-specific APIs** (added on top of base UXP)
- Both APIs are documented on the developer site

---

## Key Capabilities

### 1. Premiere DOM API
Access to:
- Sequences
- Tracks
- Clips
- Markers
- Project items
- Application settings

### 2. UXP JavaScript API
Core functionality:
- File system operations
- Network requests
- Shell execution
- Core UXP functionality

### 3. UI Components (Spectrum)
- Adobe's design system components
- For building plugin interfaces

### 4. HTML & CSS Support
- Supported HTML elements
- Supported CSS properties in UXP

---

## Plugin Types

UXP supports building:
1. **Panels** - Custom UI panels within Premiere
2. **Commands** - Menu commands and actions
3. **Modal Dialogs** - Interactive dialogs

---

## Development Environment

### Requirements
- Modern JavaScript knowledge (ES6+)
- Understanding of manifests and entrypoints
- UXP development tools

### Key Development Areas
- Filesystem operations
- Network requests
- Styling and UI design
- Lifecycle hooks

---

## Distribution Options
- Adobe Marketplace
- Enterprise distribution
- Custom installation options

---

## Next Research Steps
1. Explore Premiere DOM API reference in detail
2. Understand authentication and project access methods
3. Investigate Python integration approaches
4. Review sample plugins and starter templates
5. Determine if UXP plugins can be controlled externally (e.g., from Python)

---

## Key Question for Python Integration
**Critical:** UXP is JavaScript-based. Need to determine:
- Can Python scripts communicate with UXP plugins?
- Can we trigger UXP plugin actions from external Python code?
- What are the inter-process communication options?
- Alternative: ExtendScript vs UXP for Python integration?


---

## Premiere DOM API Details

### Accessing the Premiere DOM

```javascript
const app = require('premierepro');
```

This single line provides access to the entire Premiere DOM via UXP.

### Key Objects Hierarchy

1. **app** (Premiere Application)
   - Entry point to all Premiere objects and methods
   
2. **Project**
   ```javascript
   const project = await app.Project.getActiveProject();
   ```
   
3. **Sequence**
   ```javascript
   const sequence = await project.getActiveSequence();
   ```

### Synchronous vs Asynchronous Behavior

**Critical Difference from ExtendScript:**
- **ExtendScript (old):** All calls were synchronous and blocked the Premiere UI
- **UXP (new):** Method calls are **asynchronous** and do NOT block the UI thread

**API Design:**
- **Properties** (get/set): Designed to be **synchronous** and do NOT need to be awaited
  - Note: They are asynchronous in the background, but the API abstracts this
- **Methods**: Are **asynchronous** and require `await`

### Capabilities

From the app object, you can:
- Open documents
- Modify projects
- Run menu items
- Access sequences, tracks, clips
- Manipulate markers
- Access project items
- Control application settings

### Version Information

- API documentation now includes minimum version information
- Version tags indicate when a property/method was introduced or significantly updated
- Important for compatibility checking

---

## TypeScript Support

- TypeScript Definition File available
- Provides type safety and IntelliSense support for development


---

## Python Integration with UXP

### The Challenge

**UXP is JavaScript-based** - there is no native Python support or direct Python integration.

### Key Limitations

1. **No Node.js APIs in UXP**
   - No `child_process` module
   - No direct access to OS shell
   - Cannot execute external processes directly

2. **No Native Python Execution**
   - UXP cannot run Python scripts natively
   - Cannot import Python modules

### Workaround Solutions

#### Solution 1: Batch File Execution (ExtendScript Method)
From community discussion:
```javascript
// ExtendScript approach (may not work in UXP)
var batFile = new File("C:\\Whatever\\Path\\WhateverBatch.bat")
batFile.execute()
```
- Batch file can contain call to Python script
- Parameters can be written to text file, read by batch file
- Uncertain if this works in UXP

#### Solution 2: openPath Method
- UXP has `openPath` method to open files with default system app
- Could potentially trigger batch files
- Limited control over execution

#### Solution 3: WebSocket Communication (MCP Adobe Premiere Approach)

**Architecture discovered from morim3/mcp_adobe_premiere:**

```
LLM (Claude Desktop) → MCP Server (Python/fastmcp) → WebSocket → UXP Plugin (TypeScript) → Adobe Premiere Pro
```

**Components:**
1. **Python MCP Server** (`server/main.py`)
   - Runs as separate process
   - Implements MCP tools
   - Hosts WebSocket server

2. **WebSocket Server** (`server/websocket_server.py`)
   - Facilitates communication between Python and UXP plugin

3. **UXP Plugin** (`plugin/src/`)
   - TypeScript-based
   - WebSocket client connects to Python server
   - Receives commands and executes Premiere Pro API calls

4. **Premiere Pro**
   - Controlled by UXP plugin

**Key Features Implemented:**
- Sequence creation/deletion
- Media file importing

**System Requirements:**
- Adobe Premiere Pro Beta (25.3) or later
- UXP Developer Tool for loading plugins

---

## Recommended Python Integration Approach

### Architecture: WebSocket-Based Communication

**For Unwind Visual Cortex Integration:**

```
Python Module (Unwind Visual Cortex) 
    ↓ (WebSocket)
UXP Plugin (Custom Premiere Plugin)
    ↓ (Premiere DOM API)
Adobe Premiere Pro
```

### Implementation Steps

1. **Create Python WebSocket Server**
   - Host WebSocket server in Python module
   - Expose functions for project generation, asset import, marker placement
   - Accept JSON commands from external sources

2. **Build UXP Plugin**
   - TypeScript-based plugin
   - WebSocket client connects to Python server
   - Translates Python commands to Premiere DOM API calls
   - Implements core functions:
     - `createSequence(name, settings)`
     - `importAssets(filePaths, binName)`
     - `addMarkers(timePoints, labels)`
     - `createProject(projectData)`

3. **Unwind Visual Cortex Integration**
   - Generate blueprint JSON
   - Send commands to WebSocket server
   - UXP plugin executes in Premiere Pro
   - Return status/results to Python

### Alternative: HTTP REST API

Instead of WebSocket, could use HTTP REST API:
- UXP plugin polls Python server for commands
- Python server exposes REST endpoints
- Simpler than WebSocket but less real-time

---

## Technical Specifications Summary

### UXP Plugin Requirements
- **Language:** TypeScript/JavaScript (ES6+)
- **Framework:** Adobe UXP
- **Manifest:** `manifest.json` defining plugin metadata
- **Entry Point:** `index.ts` or similar
- **Build Tool:** Webpack for bundling
- **Distribution:** UXP Developer Tool for loading

### Python Server Requirements
- **Framework:** FastAPI or similar for WebSocket/HTTP
- **Libraries:** 
  - `fastmcp` (for MCP integration)
  - `websockets` or `fastapi` for communication
  - Standard Unwind Visual Cortex dependencies

### Communication Protocol
- **Format:** JSON
- **Commands:** Structured as:
  ```json
  {
    "action": "createSequence",
    "parameters": {
      "name": "Main Sequence",
      "width": 1920,
      "height": 1080,
      "frameRate": 30
    }
  }
  ```

---

## Next Steps for Implementation

1. ✅ Research UXP API capabilities (COMPLETE)
2. ✅ Understand Python integration limitations (COMPLETE)
3. ✅ Identify WebSocket-based architecture (COMPLETE)
4. ⏭️ Design detailed API specification for Python-UXP communication
5. ⏭️ Create UXP plugin scaffold
6. ⏭️ Implement WebSocket server in Python
7. ⏭️ Build core Premiere Pro automation functions
8. ⏭️ Test end-to-end workflow

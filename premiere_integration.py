#!/usr/bin/env python3
"""
Premiere Pro Integration Module
WebSocket server for communication between Unwind Visual Cortex and Premiere Pro UXP plugin

Part of Phase 2: Adobe Integration - Premiere Pro Automation
Task: P2-T002 - Build Premiere Pro Project Generator
"""

import asyncio
import websockets
import json
import uuid
from datetime import datetime
from typing import Dict, Any, Set, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PremiereWebSocketServer:
    """
    WebSocket server for communicating with Premiere Pro UXP plugin.
    
    This server acts as a bridge between the Unwind Visual Cortex (Python)
    and the Premiere Pro UXP plugin (JavaScript/TypeScript).
    """
    
    def __init__(self, host: str = 'localhost', port: int = 8765):
        """
        Initialize the WebSocket server.
        
        Args:
            host: Server host address (default: localhost)
            port: Server port (default: 8765)
        """
        self.host = host
        self.port = port
        self.clients: Set[websockets.WebSocketServerProtocol] = set()
        self.command_queue: Dict[str, Dict[str, Any]] = {}
        
    async def register(self, websocket: websockets.WebSocketServerProtocol):
        """Register a new client connection."""
        self.clients.add(websocket)
        logger.info(f"Client connected from {websocket.remote_address}. Total clients: {len(self.clients)}")
        
    async def unregister(self, websocket: websockets.WebSocketServerProtocol):
        """Unregister a client connection."""
        self.clients.remove(websocket)
        logger.info(f"Client disconnected. Total clients: {len(self.clients)}")
        
    async def send_command(self, command: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Send a command to all connected UXP plugin clients.
        
        Args:
            command: Command dictionary with action and parameters
            
        Returns:
            Response from the plugin, or None if no clients connected
        """
        if not self.clients:
            logger.warning("No clients connected. Command not sent.")
            return None
            
        # Add command metadata
        command_id = str(uuid.uuid4())
        command['command_id'] = command_id
        command['timestamp'] = datetime.utcnow().isoformat() + 'Z'
        
        # Store command for tracking
        self.command_queue[command_id] = {
            'command': command,
            'status': 'pending',
            'sent_at': datetime.utcnow().isoformat()
        }
        
        # Send to all connected clients
        message = json.dumps(command)
        websockets.broadcast(self.clients, message)
        logger.info(f"Command sent: {command['action']} (ID: {command_id})")
        
        return {'command_id': command_id, 'status': 'sent'}
        
    async def handle_message(self, websocket: websockets.WebSocketServerProtocol, message: str):
        """
        Handle incoming messages from UXP plugin.
        
        Args:
            websocket: Client websocket connection
            message: JSON message string
        """
        try:
            data = json.loads(message)
            
            # Check if this is a response to a command
            if 'command_id' in data:
                command_id = data['command_id']
                if command_id in self.command_queue:
                    self.command_queue[command_id]['response'] = data
                    self.command_queue[command_id]['status'] = data.get('status', 'completed')
                    logger.info(f"Received response for command {command_id}: {data.get('status')}")
                    
            # Handle different message types
            message_type = data.get('type', 'unknown')
            
            if message_type == 'ping':
                # Respond to ping
                await websocket.send(json.dumps({'type': 'pong', 'timestamp': datetime.utcnow().isoformat()}))
                
            elif message_type == 'status':
                # Plugin status update
                logger.info(f"Plugin status: {data.get('message', 'No message')}")
                
            elif message_type == 'error':
                # Error from plugin
                logger.error(f"Plugin error: {data.get('error', 'Unknown error')}")
                
            else:
                logger.debug(f"Received message: {data}")
                
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON received: {e}")
        except Exception as e:
            logger.error(f"Error handling message: {e}")
            
    async def handler(self, websocket: websockets.WebSocketServerProtocol):
        """
        Main handler for WebSocket connections.
        
        Args:
            websocket: Client websocket connection
        """
        await self.register(websocket)
        try:
            async for message in websocket:
                await self.handle_message(websocket, message)
        except websockets.exceptions.ConnectionClosed:
            logger.info("Client connection closed")
        finally:
            await self.unregister(websocket)
            
    async def start(self):
        """Start the WebSocket server."""
        logger.info(f"Starting Premiere Pro WebSocket server on {self.host}:{self.port}")
        async with websockets.serve(self.handler, self.host, self.port):
            logger.info(f"✅ Server running on ws://{self.host}:{self.port}")
            logger.info("Waiting for UXP plugin connections...")
            await asyncio.Future()  # Run forever
            

class PremiereProjectGenerator:
    """
    High-level interface for generating Premiere Pro projects.
    
    This class provides methods to create projects, sequences, import assets,
    and add markers based on Unwind Visual Cortex blueprints.
    """
    
    def __init__(self, server: PremiereWebSocketServer):
        """
        Initialize the project generator.
        
        Args:
            server: WebSocket server instance for communication
        """
        self.server = server
        
    async def create_project(self, name: str, location: str) -> Dict[str, Any]:
        """
        Create a new Premiere Pro project.
        
        Args:
            name: Project name
            location: Project file location
            
        Returns:
            Response from Premiere Pro
        """
        command = {
            'action': 'createProject',
            'parameters': {
                'name': name,
                'location': location
            }
        }
        return await self.server.send_command(command)
        
    async def create_sequence(
        self,
        name: str,
        width: int = 1920,
        height: int = 1080,
        frame_rate: float = 30.0,
        audio_sample_rate: int = 48000
    ) -> Dict[str, Any]:
        """
        Create a new sequence in the active project.
        
        Args:
            name: Sequence name
            width: Video width in pixels
            height: Video height in pixels
            frame_rate: Frame rate (fps)
            audio_sample_rate: Audio sample rate (Hz)
            
        Returns:
            Response from Premiere Pro
        """
        command = {
            'action': 'createSequence',
            'parameters': {
                'name': name,
                'width': width,
                'height': height,
                'frameRate': frame_rate,
                'audioSampleRate': audio_sample_rate
            }
        }
        return await self.server.send_command(command)
        
    async def import_assets(
        self,
        files: list,
        bin_name: str = 'Imported Assets',
        create_bin: bool = True
    ) -> Dict[str, Any]:
        """
        Import assets into the Premiere Pro project.
        
        Args:
            files: List of file paths to import
            bin_name: Name of the bin to organize assets
            create_bin: Whether to create the bin if it doesn't exist
            
        Returns:
            Response from Premiere Pro
        """
        command = {
            'action': 'importAssets',
            'parameters': {
                'files': files,
                'binName': bin_name,
                'createBin': create_bin
            }
        }
        return await self.server.send_command(command)
        
    async def add_markers(
        self,
        sequence_name: str,
        markers: list
    ) -> Dict[str, Any]:
        """
        Add markers to a sequence for CTAs and other annotations.
        
        Args:
            sequence_name: Name of the sequence
            markers: List of marker dictionaries with name, time, duration, type, and comment
            
        Returns:
            Response from Premiere Pro
        """
        command = {
            'action': 'addMarkers',
            'parameters': {
                'sequenceName': sequence_name,
                'markers': markers
            }
        }
        return await self.server.send_command(command)
        
    async def add_clip_to_timeline(
        self,
        sequence_name: str,
        clip_path: str,
        track_index: int = 1,
        start_time: str = '00:00:00:00'
    ) -> Dict[str, Any]:
        """
        Add a clip to the timeline.
        
        Args:
            sequence_name: Name of the sequence
            clip_path: Path to the clip file
            track_index: Video track index (1-based)
            start_time: Start time in timecode format (HH:MM:SS:FF)
            
        Returns:
            Response from Premiere Pro
        """
        command = {
            'action': 'addClipToTimeline',
            'parameters': {
                'sequenceName': sequence_name,
                'clipPath': clip_path,
                'trackIndex': track_index,
                'startTime': start_time
            }
        }
        return await self.server.send_command(command)
        
    async def generate_project_from_blueprint(self, blueprint: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate a complete Premiere Pro project from an Unwind Visual Cortex blueprint.
        
        Args:
            blueprint: Unwind Visual Cortex blueprint dictionary
            
        Returns:
            Summary of project generation results
        """
        results = {
            'project_created': False,
            'sequence_created': False,
            'assets_imported': False,
            'markers_added': False,
            'errors': []
        }
        
        try:
            # Extract blueprint information
            brand_name = blueprint.get('brand_name', 'Untitled Project')
            video_specs = blueprint.get('video_specs', {})
            shot_list = blueprint.get('shot_list', [])
            cta_placements = blueprint.get('cta_placements', [])
            
            # Create project
            logger.info(f"Creating project: {brand_name}")
            project_result = await self.create_project(
                name=f"{brand_name} - Unwind Visual Cortex",
                location="/path/to/projects"  # TODO: Make configurable
            )
            results['project_created'] = True
            
            # Create sequence
            logger.info("Creating main sequence")
            sequence_result = await self.create_sequence(
                name="Main Sequence",
                width=video_specs.get('width', 1920),
                height=video_specs.get('height', 1080),
                frame_rate=video_specs.get('frame_rate', 30.0)
            )
            results['sequence_created'] = True
            
            # Import B-roll assets
            if shot_list:
                logger.info(f"Importing {len(shot_list)} B-roll assets")
                asset_files = [shot.get('file_path') for shot in shot_list if shot.get('file_path')]
                if asset_files:
                    import_result = await self.import_assets(
                        files=asset_files,
                        bin_name="B-Roll",
                        create_bin=True
                    )
                    results['assets_imported'] = True
            
            # Add CTA markers
            if cta_placements:
                logger.info(f"Adding {len(cta_placements)} CTA markers")
                markers = []
                for cta in cta_placements:
                    markers.append({
                        'name': f"CTA - {cta.get('type', 'Unknown')}",
                        'time': cta.get('timecode', '00:00:00:00'),
                        'duration': '00:00:03:00',
                        'type': 'comment',
                        'comment': cta.get('description', '')
                    })
                
                if markers:
                    marker_result = await self.add_markers(
                        sequence_name="Main Sequence",
                        markers=markers
                    )
                    results['markers_added'] = True
            
            logger.info("✅ Project generation complete")
            
        except Exception as e:
            logger.error(f"Error generating project: {e}")
            results['errors'].append(str(e))
            
        return results


# Standalone server for testing
async def main():
    """Main entry point for running the server standalone."""
    server = PremiereWebSocketServer(host='localhost', port=8765)
    await server.start()


if __name__ == '__main__':
    print("=" * 60)
    print("Unwind Visual Cortex - Premiere Pro Integration Server")
    print("=" * 60)
    print("Starting WebSocket server...")
    print("Press Ctrl+C to stop")
    print("=" * 60)
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n✅ Server stopped")

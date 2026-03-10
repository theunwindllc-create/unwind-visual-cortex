/**
 * Unwind Visual Cortex - Premiere Pro UXP Plugin
 * Main entry point
 * 
 * This plugin enables communication between Unwind Visual Cortex (Python)
 * and Adobe Premiere Pro via WebSocket connection.
 */

import { WebSocketClient } from './websocket_client';
import { CommandHandler } from './command_handler';
import { Command, CommandResponse } from './types';

class UnwindPlugin {
  private wsClient: WebSocketClient;
  private commandHandler: CommandHandler;
  private serverUrl: string = 'ws://localhost:8765';

  constructor() {
    this.wsClient = new WebSocketClient(this.serverUrl);
    this.commandHandler = new CommandHandler();
    
    // Set up message handler
    this.wsClient.setMessageHandler(this.handleCommand.bind(this));
    
    console.log('Unwind Visual Cortex plugin initialized');
  }

  /**
   * Connect to the Unwind Visual Cortex server
   */
  async connect() {
    try {
      await this.wsClient.connect();
      this.wsClient.sendStatus('Plugin ready and connected');
    } catch (error) {
      console.error('Failed to connect:', error);
      alert(`Failed to connect to server at ${this.serverUrl}\n\nMake sure the Unwind Visual Cortex server is running.`);
    }
  }

  /**
   * Disconnect from the server
   */
  disconnect() {
    this.wsClient.disconnect();
  }

  /**
   * Handle incoming commands from the server
   */
  async handleCommand(command: Command): Promise<CommandResponse> {
    console.log(`Handling command: ${command.action}`);
    
    try {
      const response = await this.commandHandler.execute(command);
      return response;
    } catch (error) {
      console.error('Error handling command:', error);
      
      return {
        command_id: command.command_id,
        status: 'error',
        error: {
          code: 'HANDLER_ERROR',
          message: error instanceof Error ? error.message : String(error)
        },
        timestamp: new Date().toISOString()
      };
    }
  }

  /**
   * Send a test command to verify communication
   */
  async sendTestCommand() {
    if (!this.wsClient.isConnected()) {
      alert('Not connected to server. Please connect first.');
      return;
    }

    console.log('Sending test ping...');
    this.wsClient.sendPing();
  }
}

// Initialize plugin when DOM is loaded
if (typeof document !== 'undefined') {
  document.addEventListener('DOMContentLoaded', () => {
    console.log('DOM loaded, initializing plugin...');
    const plugin = new UnwindPlugin();
    
    // Expose plugin to global scope for button handlers
    (window as any).unwindPlugin = plugin;
    
    console.log('✅ Unwind Visual Cortex plugin ready');
  });
}

// Export for module usage
export { UnwindPlugin };

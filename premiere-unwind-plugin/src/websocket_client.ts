/**
 * WebSocket Client for Unwind Visual Cortex
 * Handles communication between UXP plugin and Python server
 */

import { Command, CommandResponse } from './types';

export class WebSocketClient {
  private ws: WebSocket | null = null;
  private serverUrl: string;
  private reconnectAttempts: number = 0;
  private maxReconnectAttempts: number = 5;
  private reconnectDelay: number = 3000;
  private messageHandler: ((command: Command) => Promise<CommandResponse>) | null = null;

  constructor(serverUrl: string = 'ws://localhost:8765') {
    this.serverUrl = serverUrl;
  }

  /**
   * Set the message handler function
   */
  setMessageHandler(handler: (command: Command) => Promise<CommandResponse>) {
    this.messageHandler = handler;
  }

  /**
   * Connect to the WebSocket server
   */
  async connect(): Promise<void> {
    return new Promise((resolve, reject) => {
      try {
        this.log('info', `Connecting to ${this.serverUrl}...`);
        this.ws = new WebSocket(this.serverUrl);

        this.ws.onopen = () => {
          this.log('success', '✅ Connected to Unwind Visual Cortex server');
          this.reconnectAttempts = 0;
          this.updateStatus('connected');
          resolve();
        };

        this.ws.onerror = (error) => {
          this.log('error', `WebSocket error: ${error}`);
          this.updateStatus('disconnected');
          reject(error);
        };

        this.ws.onclose = () => {
          this.log('info', 'Connection closed');
          this.updateStatus('disconnected');
          this.attemptReconnect();
        };

        this.ws.onmessage = async (event) => {
          try {
            const command: Command = JSON.parse(event.data);
            this.log('info', `Received command: ${command.action}`);
            
            if (this.messageHandler) {
              const response = await this.messageHandler(command);
              this.sendResponse(response);
            } else {
              this.log('error', 'No message handler set');
            }
          } catch (error) {
            this.log('error', `Error handling message: ${error}`);
          }
        };
      } catch (error) {
        this.log('error', `Connection failed: ${error}`);
        reject(error);
      }
    });
  }

  /**
   * Disconnect from the server
   */
  disconnect() {
    if (this.ws) {
      this.ws.close();
      this.ws = null;
      this.updateStatus('disconnected');
      this.log('info', 'Disconnected from server');
    }
  }

  /**
   * Send a response back to the server
   */
  sendResponse(response: CommandResponse) {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(response));
      this.log('info', `Response sent for command ${response.command_id}: ${response.status}`);
    } else {
      this.log('error', 'Cannot send response: WebSocket not connected');
    }
  }

  /**
   * Send a status message to the server
   */
  sendStatus(message: string) {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      const statusMsg = {
        type: 'status',
        message: message,
        timestamp: new Date().toISOString()
      };
      this.ws.send(JSON.stringify(statusMsg));
    }
  }

  /**
   * Send a ping to the server
   */
  sendPing() {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      const pingMsg = {
        type: 'ping',
        timestamp: new Date().toISOString()
      };
      this.ws.send(JSON.stringify(pingMsg));
      this.log('info', 'Ping sent');
    }
  }

  /**
   * Attempt to reconnect to the server
   */
  private attemptReconnect() {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      this.log('info', `Reconnecting in ${this.reconnectDelay / 1000}s (attempt ${this.reconnectAttempts}/${this.maxReconnectAttempts})...`);
      this.updateStatus('connecting');
      
      setTimeout(() => {
        this.connect().catch(() => {
          // Connection failed, will try again
        });
      }, this.reconnectDelay);
    } else {
      this.log('error', 'Max reconnection attempts reached');
      this.updateStatus('disconnected');
    }
  }

  /**
   * Update the UI status indicator
   */
  private updateStatus(status: 'connected' | 'disconnected' | 'connecting') {
    const statusEl = document.getElementById('status');
    const connectBtn = document.getElementById('connectBtn') as HTMLButtonElement;
    const testBtn = document.getElementById('testBtn') as HTMLButtonElement;
    
    if (statusEl) {
      statusEl.className = `status ${status}`;
      
      switch (status) {
        case 'connected':
          statusEl.textContent = '🟢 Connected to server';
          if (connectBtn) connectBtn.disabled = true;
          if (testBtn) testBtn.disabled = false;
          break;
        case 'disconnected':
          statusEl.textContent = '⚫ Disconnected from server';
          if (connectBtn) connectBtn.disabled = false;
          if (testBtn) testBtn.disabled = true;
          break;
        case 'connecting':
          statusEl.textContent = '🟡 Connecting to server...';
          if (connectBtn) connectBtn.disabled = true;
          if (testBtn) testBtn.disabled = true;
          break;
      }
    }
  }

  /**
   * Log a message to the UI
   */
  private log(type: 'info' | 'error' | 'success', message: string) {
    console.log(`[${type.toUpperCase()}] ${message}`);
    
    const logEl = document.getElementById('log');
    if (logEl) {
      const entry = document.createElement('div');
      entry.className = `log-entry ${type}`;
      entry.textContent = `[${new Date().toLocaleTimeString()}] ${message}`;
      logEl.appendChild(entry);
      logEl.scrollTop = logEl.scrollHeight;
    }
  }

  /**
   * Check if connected
   */
  isConnected(): boolean {
    return this.ws !== null && this.ws.readyState === WebSocket.OPEN;
  }
}

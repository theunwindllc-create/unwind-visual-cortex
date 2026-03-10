/**
 * Command Handler for Premiere Pro UXP Plugin
 * Routes commands to appropriate Premiere API functions
 */

import { Command, CommandResponse } from './types';
import { PremiereAPI } from './premiere_api';

export class CommandHandler {
  private premiereAPI: PremiereAPI;

  constructor(useMockMode: boolean = false) {
    // useMockMode allows testing without Premiere Pro
    // Set to false in production to use actual Premiere API
    this.premiereAPI = new PremiereAPI(useMockMode);
  }

  /**
   * Execute a command and return the response
   */
  async execute(command: Command): Promise<CommandResponse> {
    const response: CommandResponse = {
      command_id: command.command_id,
      status: 'pending',
      timestamp: new Date().toISOString()
    };

    try {
      console.log(`Executing command: ${command.action}`);

      switch (command.action) {
        case 'createProject':
          response.result = await this.premiereAPI.createProject(
            command.parameters.name,
            command.parameters.location
          );
          response.status = 'success';
          break;

        case 'openProject':
          response.result = await this.premiereAPI.openProject(
            command.parameters.path
          );
          response.status = 'success';
          break;

        case 'createSequence':
          response.result = await this.premiereAPI.createSequence(
            command.parameters.name,
            command.parameters.width,
            command.parameters.height,
            command.parameters.frameRate,
            command.parameters.audioSampleRate
          );
          response.status = 'success';
          break;

        case 'getSequenceInfo':
          response.result = await this.premiereAPI.getSequenceInfo(
            command.parameters.sequenceName
          );
          response.status = 'success';
          break;

        case 'importAssets':
          response.result = await this.premiereAPI.importAssets(
            command.parameters.files,
            command.parameters.binName,
            command.parameters.createBin
          );
          response.status = 'success';
          break;

        case 'addMarkers':
          response.result = await this.premiereAPI.addMarkers(
            command.parameters.sequenceName,
            command.parameters.markers
          );
          response.status = 'success';
          break;

        case 'addClipToTimeline':
          response.result = await this.premiereAPI.addClipToTimeline(
            command.parameters.sequenceName,
            command.parameters.clipPath,
            command.parameters.trackIndex,
            command.parameters.startTime
          );
          response.status = 'success';
          break;

        case 'createSequenceFromTemplate':
          response.result = await this.premiereAPI.createSequenceFromTemplate(
            command.parameters.template_config
          );
          response.status = 'success';
          break;

        case 'ping':
          response.result = { message: 'pong' };
          response.status = 'success';
          break;

        default:
          throw new Error(`Unknown command action: ${command.action}`);
      }

      console.log(`Command ${command.action} executed successfully`);
    } catch (error) {
      console.error(`Command ${command.action} failed:`, error);
      response.status = 'error';
      response.error = {
        code: 'COMMAND_EXECUTION_ERROR',
        message: error instanceof Error ? error.message : String(error)
      };
    }

    return response;
  }
}

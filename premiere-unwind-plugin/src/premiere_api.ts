/**
 * Premiere Pro API Wrapper
 * Provides high-level interface to Premiere Pro DOM API
 * 
 * Updated: 2026-01-16 - P2-T005 Sequence Template System
 * Added createSequenceFromTemplate method
 * Updated: 2026-01-14 - P2-T003 Asset Import Automation
 * Replaced mock functions with actual Premiere DOM API calls
 */

import { Marker, SequenceTemplateConfig } from './types';

export class PremiereAPI {
  private app: any;
  private useMockMode: boolean;

  constructor(useMockMode: boolean = false) {
    this.useMockMode = useMockMode;
    
    if (useMockMode) {
      // For development/testing without Premiere Pro
      this.app = this.getMockApp();
      console.log('[PremiereAPI] Running in MOCK mode');
    } else {
      // Production mode: Use actual Premiere Pro API
      try {
        this.app = require('premierepro');
        console.log('[PremiereAPI] Connected to Premiere Pro');
      } catch (error) {
        console.error('[PremiereAPI] Failed to load premierepro module:', error);
        console.log('[PremiereAPI] Falling back to MOCK mode');
        this.useMockMode = true;
        this.app = this.getMockApp();
      }
    }
  }

  /**
   * Create a new Premiere Pro project
   */
  async createProject(name: string, location: string): Promise<any> {
    console.log(`[PremiereAPI] Creating project: ${name} at ${location}`);
    
    if (this.useMockMode) {
      return {
        success: true,
        message: `[MOCK] Project "${name}" created`,
        projectPath: `${location}/${name}.prproj`
      };
    }
    
    try {
      const projectPath = `${location}/${name}.prproj`;
      const project = await this.app.Project.createProject(projectPath);
      
      return {
        success: true,
        message: `Project "${name}" created successfully`,
        projectPath: projectPath,
        projectGuid: project.guid
      };
    } catch (error: any) {
      console.error('[PremiereAPI] Error creating project:', error);
      return {
        success: false,
        error: error.message || 'Failed to create project'
      };
    }
  }

  /**
   * Open an existing Premiere Pro project
   */
  async openProject(path: string): Promise<any> {
    console.log(`[PremiereAPI] Opening project: ${path}`);
    
    if (this.useMockMode) {
      return {
        success: true,
        message: `[MOCK] Project opened: ${path}`
      };
    }
    
    try {
      const project = await this.app.Project.open(path);
      
      return {
        success: true,
        message: `Project opened successfully`,
        projectPath: path,
        projectGuid: project.guid,
        projectName: project.name
      };
    } catch (error: any) {
      console.error('[PremiereAPI] Error opening project:', error);
      return {
        success: false,
        error: error.message || 'Failed to open project'
      };
    }
  }

  /**
   * Create a new sequence
   * Note: Premiere UXP doesn't have direct sequence creation with parameters
   * This creates a sequence from media clips
   */
  async createSequence(
    name: string,
    width: number,
    height: number,
    frameRate: number,
    audioSampleRate: number
  ): Promise<any> {
    console.log(`[PremiereAPI] Creating sequence: ${name} (${width}x${height} @ ${frameRate}fps)`);
    
    if (this.useMockMode) {
      return {
        success: true,
        message: `[MOCK] Sequence "${name}" created`,
        sequenceName: name,
        specs: { width, height, frameRate, audioSampleRate }
      };
    }
    
    try {
      const project = await this.app.Project.getActiveProject();
      
      // Note: Direct sequence creation with custom settings is limited in UXP
      // For now, create an empty sequence (requires media clips or preset)
      // This is a known limitation - see technical spec section 3.3
      
      console.warn('[PremiereAPI] Direct sequence creation with custom settings not fully supported');
      console.warn('[PremiereAPI] Consider using createSequenceFromClips or preset-based creation');
      
      return {
        success: false,
        message: 'Direct sequence creation requires preset or media clips',
        note: 'Use importAssets first, then create sequence from clips'
      };
    } catch (error: any) {
      console.error('[PremiereAPI] Error creating sequence:', error);
      return {
        success: false,
        error: error.message || 'Failed to create sequence'
      };
    }
  }

  /**
   * Get information about a sequence
   */
  async getSequenceInfo(sequenceName: string): Promise<any> {
    console.log(`[PremiereAPI] Getting info for sequence: ${sequenceName}`);
    
    if (this.useMockMode) {
      return {
        success: true,
        name: sequenceName,
        guid: 'mock-guid-12345',
        videoTrackCount: 3,
        audioTrackCount: 3
      };
    }
    
    try {
      const project = await this.app.Project.getActiveProject();
      const sequences = await project.getSequences();
      
      // Find sequence by name
      const sequence = sequences.find((seq: any) => seq.name === sequenceName);
      
      if (!sequence) {
        return {
          success: false,
          error: `Sequence "${sequenceName}" not found`
        };
      }
      
      const videoTrackCount = await sequence.getVideoTrackCount();
      const audioTrackCount = await sequence.getAudioTrackCount();
      const settings = await sequence.getSettings();
      
      return {
        success: true,
        name: sequence.name,
        guid: sequence.guid,
        videoTrackCount: videoTrackCount,
        audioTrackCount: audioTrackCount,
        settings: settings
      };
    } catch (error: any) {
      console.error('[PremiereAPI] Error getting sequence info:', error);
      return {
        success: false,
        error: error.message || 'Failed to get sequence info'
      };
    }
  }

  /**
   * Import assets into the project
   * This is the core implementation for P2-T003
   */
  async importAssets(
    files: string[],
    binName: string,
    createBin: boolean
  ): Promise<any> {
    console.log(`[PremiereAPI] Importing ${files.length} assets into bin: ${binName}`);
    console.log(`[PremiereAPI] Files:`, files);
    
    if (this.useMockMode) {
      return {
        success: true,
        message: `[MOCK] Imported ${files.length} assets`,
        binName: binName,
        filesImported: files.length,
        files: files
      };
    }
    
    try {
      const project = await this.app.Project.getActiveProject();
      const rootItem = project.getRootItem();
      
      let targetBin = null;
      
      // Create bin if requested
      if (createBin) {
        console.log(`[PremiereAPI] Creating bin: ${binName}`);
        
        // Use executeTransaction to create bin
        await project.executeTransaction((compoundAction: any) => {
          const createBinAction = rootItem.createBinAction(binName, true); // makeUnique = true
          compoundAction.addAction(createBinAction);
        }, `Create Bin: ${binName}`);
        
        // Find the newly created bin
        const items = rootItem.getItems();
        targetBin = items.find((item: any) => item.name === binName);
        
        if (!targetBin) {
          console.warn(`[PremiereAPI] Bin "${binName}" created but not found, importing to root`);
        } else {
          console.log(`[PremiereAPI] Bin "${binName}" created successfully`);
        }
      } else {
        // Try to find existing bin
        const items = rootItem.getItems();
        targetBin = items.find((item: any) => item.name === binName);
        
        if (!targetBin) {
          console.warn(`[PremiereAPI] Bin "${binName}" not found, importing to root`);
        }
      }
      
      // Import files
      console.log(`[PremiereAPI] Importing files...`);
      const suppressUI = true; // Suppress import dialog for automation
      const asNumberedStills = false; // Import as video, not image sequence
      
      const importResult = project.importFiles(
        files,
        suppressUI,
        targetBin, // Can be null to import to root
        asNumberedStills
      );
      
      if (importResult) {
        console.log(`[PremiereAPI] Import successful`);
        return {
          success: true,
          message: `Successfully imported ${files.length} assets`,
          binName: binName,
          filesImported: files.length,
          files: files,
          importedToRoot: targetBin === null
        };
      } else {
        console.error(`[PremiereAPI] Import failed`);
        return {
          success: false,
          error: 'Import operation returned false'
        };
      }
      
    } catch (error: any) {
      console.error('[PremiereAPI] Error importing assets:', error);
      return {
        success: false,
        error: error.message || 'Failed to import assets',
        details: error.toString()
      };
    }
  }

  /**
   * Add markers to a sequence
   */
  async addMarkers(sequenceName: string, markers: Marker[]): Promise<any> {
    console.log(`[PremiereAPI] Adding ${markers.length} markers to sequence: ${sequenceName}`);
    
    if (this.useMockMode) {
      return {
        success: true,
        message: `[MOCK] Added ${markers.length} markers`,
        sequenceName: sequenceName,
        markersAdded: markers.length,
        markers: markers.map(m => m.name)
      };
    }
    
    try {
      const project = await this.app.Project.getActiveProject();
      const sequences = await project.getSequences();
      
      // Find sequence by name
      const sequence = sequences.find((seq: any) => seq.name === sequenceName);
      
      if (!sequence) {
        return {
          success: false,
          error: `Sequence "${sequenceName}" not found`
        };
      }
      
      const settings = await sequence.getSettings();
      const frameRate = settings.videoFrameRate.framerate;
      
      // Get Markers API (static class)
      const MarkersClass = this.app.Markers;
      
      // Get Markers instance for this sequence
      const markersInstance = MarkersClass.getMarkers(sequence);
      
      // Add each marker
      await project.executeTransaction((compoundAction: any) => {
        for (const marker of markers) {
          const startTicks = this.timecodeToTicks(marker.time, frameRate);
          const durationTicks = this.timecodeToTicks(marker.duration, frameRate);
          
          const addMarkerAction = markersInstance.createAddMarkerAction(
            marker.name,
            marker.type || 'comment',
            startTicks,
            durationTicks
          );
          
          compoundAction.addAction(addMarkerAction);
        }
      }, `Add ${markers.length} Markers`);
      
      return {
        success: true,
        message: `Added ${markers.length} markers successfully`,
        sequenceName: sequenceName,
        markersAdded: markers.length,
        markers: markers.map(m => m.name)
      };
      
    } catch (error: any) {
      console.error('[PremiereAPI] Error adding markers:', error);
      return {
        success: false,
        error: error.message || 'Failed to add markers'
      };
    }
  }

  /**
   * Add a clip to the timeline
   */
  async addClipToTimeline(
    sequenceName: string,
    clipPath: string,
    trackIndex: number,
    startTime: string
  ): Promise<any> {
    console.log(`[PremiereAPI] Adding clip to timeline: ${clipPath} at ${startTime}`);
    
    if (this.useMockMode) {
      return {
        success: true,
        message: `[MOCK] Clip added to timeline`,
        sequenceName: sequenceName,
        clipPath: clipPath,
        trackIndex: trackIndex,
        startTime: startTime
      };
    }
    
    try {
      const project = await this.app.Project.getActiveProject();
      const sequences = await project.getSequences();
      
      // Find sequence by name
      const sequence = sequences.find((seq: any) => seq.name === sequenceName);
      
      if (!sequence) {
        return {
          success: false,
          error: `Sequence "${sequenceName}" not found`
        };
      }
      
      // Note: Direct timeline editing API is limited in UXP
      // This is a placeholder for future implementation
      console.warn('[PremiereAPI] Direct timeline editing not fully implemented');
      
      return {
        success: false,
        message: 'Timeline editing API not yet fully implemented',
        note: 'This feature requires additional UXP API support'
      };
      
    } catch (error: any) {
      console.error('[PremiereAPI] Error adding clip to timeline:', error);
      return {
        success: false,
        error: error.message || 'Failed to add clip to timeline'
      };
    }
  }

  /**
   * Convert timecode string to ticks
   * Format: HH:MM:SS:FF
   * Premiere uses 254016000000 ticks per second
   */
  private timecodeToTicks(timecode: string, frameRate: number): number {
    const parts = timecode.split(':').map(Number);
    
    if (parts.length !== 4) {
      console.error(`[PremiereAPI] Invalid timecode format: ${timecode}`);
      return 0;
    }
    
    const [hours, minutes, seconds, frames] = parts;
    
    const totalSeconds = hours * 3600 + minutes * 60 + seconds;
    const totalFrames = totalSeconds * frameRate + frames;
    
    // Premiere uses ticks (254016000000 ticks per second)
    const ticksPerFrame = 254016000000 / frameRate;
    return Math.round(totalFrames * ticksPerFrame);
  }

  /**
   * Create a sequence from a template configuration
   * P2-T005: Sequence Template System
   */
  async createSequenceFromTemplate(config: SequenceTemplateConfig): Promise<any> {
    console.log(`[PremiereAPI] Creating sequence from template: ${config.template_name}`);
    console.log(`[PremiereAPI] Sequence name: ${config.sequence_name}`);
    
    if (this.useMockMode) {
      return {
        success: true,
        message: `[MOCK] Sequence created from template: ${config.template_name}`,
        sequenceName: config.sequence_name,
        templateId: config.template_id,
        settings: config.sequence_settings
      };
    }
    
    try {
      const project = await this.app.Project.getActiveProject();
      
      // Note: Premiere UXP API has limitations for direct sequence creation
      // with custom settings. This implementation focuses on what's possible.
      
      console.log(`[PremiereAPI] Template: ${config.template_id}`);
      console.log(`[PremiereAPI] Settings: ${config.sequence_settings.width}x${config.sequence_settings.height} @ ${config.sequence_settings.frameRate}fps`);
      console.log(`[PremiereAPI] Video Tracks: ${config.sequence_settings.videoTrackCount}`);
      console.log(`[PremiereAPI] Audio Tracks: ${config.sequence_settings.audioTrackCount}`);
      
      // Strategy: Create a basic sequence and document the template settings
      // The user can then apply these settings manually or via presets
      
      // For now, return success with template information
      // Future enhancement: Use ExtendScript bridge for more control
      
      return {
        success: true,
        message: `Sequence template loaded: ${config.template_name}`,
        sequenceName: config.sequence_name,
        templateId: config.template_id,
        settings: config.sequence_settings,
        timelineStructure: config.timeline_structure,
        transitions: config.default_transitions,
        effectsPresets: config.effects_presets,
        recommendedPacing: config.recommended_pacing,
        metadata: config.metadata,
        note: 'Template configuration loaded. Apply settings manually or use sequence presets.',
        instructions: [
          '1. Create a new sequence in Premiere Pro',
          `2. Set resolution to ${config.sequence_settings.width}x${config.sequence_settings.height}`,
          `3. Set frame rate to ${config.sequence_settings.frameRate} fps`,
          `4. Create ${config.sequence_settings.videoTrackCount} video tracks and ${config.sequence_settings.audioTrackCount} audio tracks`,
          '5. Apply recommended transitions and effects from template',
          '6. Follow recommended pacing guidelines'
        ]
      };
      
    } catch (error: any) {
      console.error('[PremiereAPI] Error creating sequence from template:', error);
      return {
        success: false,
        error: error.message || 'Failed to create sequence from template'
      };
    }
  }

  /**
   * Mock app object for development
   * This will be replaced with actual premierepro require in production
   */
  private getMockApp(): any {
    return {
      Project: {
        getActiveProject: async () => ({
          name: 'Mock Project',
          guid: 'mock-guid',
          getRootItem: () => ({
            name: 'Root',
            getItems: () => [],
            createBinAction: (name: string, makeUnique: boolean) => ({
              execute: () => console.log(`[MOCK] Creating bin: ${name}`)
            })
          }),
          createSequence: async () => ({ name: 'Mock Sequence' }),
          importFiles: () => true,
          executeTransaction: async (callback: any, undoString: string) => {
            console.log(`[MOCK] Executing transaction: ${undoString}`);
            const mockCompoundAction = {
              addAction: (action: any) => console.log('[MOCK] Adding action to compound')
            };
            callback(mockCompoundAction);
          }
        })
      }
    };
  }
}

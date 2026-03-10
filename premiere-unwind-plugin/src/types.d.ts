/**
 * Type definitions for Unwind Visual Cortex Premiere Pro Plugin
 */

/**
 * Command structure sent from Python server to UXP plugin
 */
export interface Command {
  command_id: string;
  action: string;
  parameters: Record<string, any>;
  timestamp: string;
}

/**
 * Response structure sent from UXP plugin to Python server
 */
export interface CommandResponse {
  command_id: string;
  status: 'success' | 'error' | 'pending';
  result?: Record<string, any>;
  error?: {
    code: string;
    message: string;
  };
  timestamp: string;
}

/**
 * Marker definition for CTA placement
 * Enhanced for Unwind Visual Cortex CTA recommendations
 */
export interface Marker {
  name: string;           // Marker display name
  time: string;           // Timecode in HH:MM:SS:FF format
  duration: string;       // Duration in HH:MM:SS:FF format
  type: string;           // Marker type: 'comment', 'chapter', 'weblink', 'flashcue', 'segmentation'
  comment: string;        // Marker description/notes
  ctaType?: string;       // CTA type: 'subscribe', 'like', 'visit', 'download', 'custom'
  ctaMessage?: string;    // CTA message text
  ctaAction?: string;     // Target action or URL
  confidence?: number;    // Unwind AI confidence score (0-1)
}

/**
 * Project creation parameters
 */
export interface CreateProjectParams {
  name: string;
  location: string;
}

/**
 * Sequence creation parameters
 */
export interface CreateSequenceParams {
  name: string;
  width: number;
  height: number;
  frameRate: number;
  audioSampleRate: number;
}

/**
 * Asset import parameters
 */
export interface ImportAssetsParams {
  files: string[];
  binName: string;
  createBin: boolean;
}

/**
 * Marker addition parameters
 */
export interface AddMarkersParams {
  sequenceName: string;
  markers: Marker[];
}

/**
 * Timeline clip addition parameters
 */
export interface AddClipToTimelineParams {
  sequenceName: string;
  clipPath: string;
  trackIndex: number;
  startTime: string;
}

/**
 * Sequence template configuration
 * P2-T005: Sequence Template System
 */
export interface SequenceTemplateConfig {
  sequence_name: string;
  template_id: string;
  template_name: string;
  sequence_settings: SequenceSettings;
  timeline_structure: TimelineStructure;
  default_transitions: DefaultTransitions;
  effects_presets: EffectPreset[];
  recommended_pacing: RecommendedPacing;
  metadata: TemplateMetadata;
}

/**
 * Sequence settings
 */
export interface SequenceSettings {
  width: number;
  height: number;
  frameRate: number;
  audioSampleRate: number;
  videoTrackCount: number;
  audioTrackCount: number;
  pixelAspectRatio: number;
  fieldType: string;
}

/**
 * Timeline structure definition
 */
export interface TimelineStructure {
  video_tracks: TrackDefinition[];
  audio_tracks: TrackDefinition[];
}

/**
 * Track definition
 */
export interface TrackDefinition {
  track_number: number;
  name: string;
  locked: boolean;
  description: string;
}

/**
 * Default transitions
 */
export interface DefaultTransitions {
  video: TransitionDefinition;
  audio: TransitionDefinition;
}

/**
 * Transition definition
 */
export interface TransitionDefinition {
  name: string;
  duration_frames: number;
  alignment?: string;
}

/**
 * Effect preset definition
 */
export interface EffectPreset {
  name: string;
  effect: string;
  preset: string;
  track_type: 'video' | 'audio';
  recommended_tracks: number[];
}

/**
 * Recommended pacing
 */
export interface RecommendedPacing {
  average_shot_duration_seconds: number;
  transition_frequency: string;
  cta_placement_strategy: string;
}

/**
 * Template metadata
 */
export interface TemplateMetadata {
  generated_by: string;
  generated_at: string;
  template_version: string;
  brand_colors: string[];
}

/**
 * Create sequence from template parameters
 */
export interface CreateSequenceFromTemplateParams {
  template_config: SequenceTemplateConfig;
}

#!/usr/bin/env python3
"""
CTA Marker Generator for Unwind Visual Cortex
Generates strategic marker placements for Call-to-Action overlays based on video analysis

Author: Unwind Code - Visual Cortex Brain
Date: 2026-01-15
Task: P2-T004 - Create Marker System for CTAs
"""

from typing import List, Dict, Any
import json


class CTAMarkerGenerator:
    """
    Generates CTA markers based on Unwind Visual Cortex recommendations
    """
    
    # Standard CTA types
    CTA_TYPES = {
        'subscribe': 'Subscribe CTA',
        'like': 'Like & Comment CTA',
        'visit': 'Visit Website CTA',
        'download': 'Download Resource CTA',
        'custom': 'Custom CTA'
    }
    
    # Marker types in Premiere Pro
    MARKER_TYPES = {
        'comment': 'Standard comment marker',
        'chapter': 'Chapter marker',
        'weblink': 'Web link marker',
        'flashcue': 'Flash cue point',
        'segmentation': 'Segmentation marker'
    }
    
    def __init__(self):
        """Initialize the CTA marker generator"""
        pass
    
    def generate_strategic_markers(
        self,
        video_duration: float,
        brand_analysis: Dict[str, Any],
        engagement_strategy: str = 'balanced'
    ) -> List[Dict[str, Any]]:
        """
        Generate strategic CTA markers based on video duration and brand analysis
        
        Args:
            video_duration: Total video duration in seconds
            brand_analysis: Brand analysis data from Unwind Visual Cortex
            engagement_strategy: 'aggressive', 'balanced', or 'minimal'
        
        Returns:
            List of marker dictionaries ready for Premiere Pro
        """
        markers = []
        
        # Calculate strategic timing based on video duration
        if engagement_strategy == 'aggressive':
            # More frequent CTAs
            marker_positions = self._calculate_aggressive_positions(video_duration)
        elif engagement_strategy == 'minimal':
            # Fewer, strategic CTAs
            marker_positions = self._calculate_minimal_positions(video_duration)
        else:
            # Balanced approach (default)
            marker_positions = self._calculate_balanced_positions(video_duration)
        
        # Generate markers at calculated positions
        for position in marker_positions:
            marker = self._create_marker(
                position,
                video_duration,
                brand_analysis
            )
            markers.append(marker)
        
        return markers
    
    def _calculate_balanced_positions(self, duration: float) -> List[Dict[str, Any]]:
        """
        Calculate balanced CTA positions
        - Opening hook (5-10 seconds)
        - Mid-video engagement (40-50% mark)
        - Pre-end CTA (85-90% mark)
        """
        positions = []
        
        # Opening hook CTA (after intro, around 8 seconds)
        if duration > 15:
            positions.append({
                'time': 8.0,
                'type': 'like',
                'priority': 'medium',
                'reason': 'Early engagement hook'
            })
        
        # Mid-video CTA (at 45% mark)
        if duration > 30:
            mid_point = duration * 0.45
            positions.append({
                'time': mid_point,
                'type': 'subscribe',
                'priority': 'high',
                'reason': 'Peak engagement point'
            })
        
        # Pre-end CTA (at 87% mark, before outro)
        if duration > 20:
            pre_end = duration * 0.87
            positions.append({
                'time': pre_end,
                'type': 'visit',
                'priority': 'high',
                'reason': 'Final conversion opportunity'
            })
        
        return positions
    
    def _calculate_aggressive_positions(self, duration: float) -> List[Dict[str, Any]]:
        """
        Calculate aggressive CTA positions (more frequent)
        """
        positions = []
        
        # Early hook
        if duration > 10:
            positions.append({
                'time': 6.0,
                'type': 'like',
                'priority': 'medium',
                'reason': 'Immediate engagement'
            })
        
        # First third
        if duration > 30:
            positions.append({
                'time': duration * 0.30,
                'type': 'subscribe',
                'priority': 'high',
                'reason': 'First conversion point'
            })
        
        # Middle
        if duration > 45:
            positions.append({
                'time': duration * 0.50,
                'type': 'visit',
                'priority': 'medium',
                'reason': 'Mid-video engagement'
            })
        
        # Two-thirds
        if duration > 60:
            positions.append({
                'time': duration * 0.67,
                'type': 'download',
                'priority': 'medium',
                'reason': 'Secondary conversion'
            })
        
        # Pre-end
        positions.append({
            'time': duration * 0.90,
            'type': 'subscribe',
            'priority': 'high',
            'reason': 'Final push'
        })
        
        return positions
    
    def _calculate_minimal_positions(self, duration: float) -> List[Dict[str, Any]]:
        """
        Calculate minimal CTA positions (fewer, strategic)
        """
        positions = []
        
        # Single mid-video CTA
        if duration > 20:
            positions.append({
                'time': duration * 0.50,
                'type': 'subscribe',
                'priority': 'high',
                'reason': 'Single strategic placement'
            })
        
        # End CTA only if video is long enough
        if duration > 60:
            positions.append({
                'time': duration * 0.85,
                'type': 'visit',
                'priority': 'high',
                'reason': 'End conversion'
            })
        
        return positions
    
    def _create_marker(
        self,
        position: Dict[str, Any],
        video_duration: float,
        brand_analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Create a marker dictionary for Premiere Pro
        
        Args:
            position: Position data with time, type, priority
            video_duration: Total video duration
            brand_analysis: Brand analysis data
        
        Returns:
            Marker dictionary compatible with Premiere Pro API
        """
        time_seconds = position['time']
        cta_type = position['type']
        
        # Convert seconds to timecode (HH:MM:SS:FF at 30fps)
        timecode = self._seconds_to_timecode(time_seconds, fps=30)
        
        # Default duration: 5 seconds (00:00:05:00 at 30fps)
        duration_timecode = "00:00:05:00"
        
        # Get CTA message based on type and brand
        cta_message = self._generate_cta_message(cta_type, brand_analysis)
        
        marker = {
            'name': f"CTA: {self.CTA_TYPES.get(cta_type, 'Custom')}",
            'time': timecode,
            'duration': duration_timecode,
            'type': 'comment',  # Use comment type for CTAs
            'comment': f"{position['reason']} - {cta_message}",
            'ctaType': cta_type,
            'ctaMessage': cta_message,
            'ctaAction': self._get_default_action(cta_type),
            'confidence': 0.85  # Default confidence score
        }
        
        return marker
    
    def _seconds_to_timecode(self, seconds: float, fps: int = 30) -> str:
        """
        Convert seconds to timecode format HH:MM:SS:FF
        
        Args:
            seconds: Time in seconds
            fps: Frame rate (default 30fps)
        
        Returns:
            Timecode string in HH:MM:SS:FF format
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        frames = int((seconds % 1) * fps)
        
        return f"{hours:02d}:{minutes:02d}:{secs:02d}:{frames:02d}"
    
    def _generate_cta_message(
        self,
        cta_type: str,
        brand_analysis: Dict[str, Any]
    ) -> str:
        """
        Generate appropriate CTA message based on type and brand
        
        Args:
            cta_type: Type of CTA
            brand_analysis: Brand analysis data
        
        Returns:
            CTA message string
        """
        brand_name = brand_analysis.get('brand_name', 'our channel')
        
        messages = {
            'subscribe': f"Subscribe to {brand_name} for more content!",
            'like': "Like this video and leave a comment!",
            'visit': f"Visit {brand_name} website for more info",
            'download': "Download our free resource now!",
            'custom': "Take action now!"
        }
        
        return messages.get(cta_type, messages['custom'])
    
    def _get_default_action(self, cta_type: str) -> str:
        """
        Get default action for CTA type
        
        Args:
            cta_type: Type of CTA
        
        Returns:
            Action string (URL, command, etc.)
        """
        actions = {
            'subscribe': 'channel_subscribe',
            'like': 'video_like',
            'visit': 'https://example.com',
            'download': 'resource_download',
            'custom': 'custom_action'
        }
        
        return actions.get(cta_type, actions['custom'])
    
    def export_markers_json(
        self,
        markers: List[Dict[str, Any]],
        output_path: str
    ) -> None:
        """
        Export markers to JSON file
        
        Args:
            markers: List of marker dictionaries
            output_path: Path to output JSON file
        """
        with open(output_path, 'w') as f:
            json.dump({
                'markers': markers,
                'generator': 'Unwind Visual Cortex CTA Marker Generator',
                'version': '1.0',
                'total_markers': len(markers)
            }, f, indent=2)
        
        print(f"Exported {len(markers)} markers to {output_path}")


def main():
    """
    Example usage of CTA Marker Generator
    """
    generator = CTAMarkerGenerator()
    
    # Example: 90-second video with balanced strategy
    brand_analysis = {
        'brand_name': 'Tech Innovators',
        'industry': 'Technology',
        'target_audience': 'Tech enthusiasts'
    }
    
    markers = generator.generate_strategic_markers(
        video_duration=90.0,
        brand_analysis=brand_analysis,
        engagement_strategy='balanced'
    )
    
    print("Generated CTA Markers:")
    print(json.dumps(markers, indent=2))
    
    # Export to file
    generator.export_markers_json(
        markers,
        '/home/ubuntu/unwind_visual_cortex/example_cta_markers.json'
    )


if __name__ == "__main__":
    main()

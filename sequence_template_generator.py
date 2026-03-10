"""
Sequence Template Generator for Unwind Visual Cortex
Generates Premiere Pro sequence configurations from reusable templates

Author: Unwind Visual Cortex
Date: 2026-01-16
Task: P2-T005 - Develop Sequence Template System
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime


class SequenceTemplateGenerator:
    """
    Generates Premiere Pro sequence configurations from templates.
    
    This class loads template definitions from JSON and generates
    Premiere Pro-compatible sequence configurations that can be
    sent to the UXP plugin via WebSocket.
    """
    
    def __init__(self, templates_path: str = "sequence_templates.json"):
        """
        Initialize the template generator.
        
        Args:
            templates_path: Path to the templates JSON file
        """
        self.templates_path = templates_path
        self.templates = self._load_templates()
    
    def _load_templates(self) -> Dict[str, Any]:
        """Load template definitions from JSON file."""
        if not os.path.exists(self.templates_path):
            raise FileNotFoundError(f"Templates file not found: {self.templates_path}")
        
        with open(self.templates_path, 'r') as f:
            data = json.load(f)
        
        return data.get('templates', {})
    
    def list_templates(self) -> List[Dict[str, str]]:
        """
        List all available templates with basic info.
        
        Returns:
            List of template summaries
        """
        summaries = []
        
        for template_id, template in self.templates.items():
            summaries.append({
                'template_id': template_id,
                'template_name': template.get('template_name', 'Unknown'),
                'description': template.get('description', ''),
                'video_type': template.get('video_type', 'unknown'),
                'complexity': template.get('metadata', {}).get('complexity', 'unknown')
            })
        
        return summaries
    
    def get_template(self, template_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific template by ID.
        
        Args:
            template_id: The template identifier
            
        Returns:
            Template definition or None if not found
        """
        return self.templates.get(template_id)
    
    def generate_from_template(
        self,
        template_id: str,
        sequence_name: str,
        brand_colors: Optional[List[str]] = None,
        custom_settings: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate a sequence configuration from a template.
        
        Args:
            template_id: The template to use
            sequence_name: Name for the new sequence
            brand_colors: Optional list of brand colors (hex format)
            custom_settings: Optional settings to override template defaults
            
        Returns:
            Complete sequence configuration ready for Premiere Pro
        """
        template = self.get_template(template_id)
        
        if not template:
            raise ValueError(f"Template not found: {template_id}")
        
        # Start with template settings
        config = {
            'sequence_name': sequence_name,
            'template_id': template_id,
            'template_name': template.get('template_name'),
            'sequence_settings': template.get('sequence_settings', {}).copy(),
            'timeline_structure': template.get('timeline_structure', {}).copy(),
            'default_transitions': template.get('default_transitions', {}).copy(),
            'effects_presets': template.get('effects_presets', []).copy(),
            'recommended_pacing': template.get('recommended_pacing', {}).copy(),
            'metadata': {
                'generated_by': 'Unwind Visual Cortex',
                'generated_at': datetime.now().isoformat(),
                'template_version': template.get('metadata', {}).get('version', '1.0'),
                'brand_colors': brand_colors or []
            }
        }
        
        # Apply custom settings overrides
        if custom_settings:
            for key, value in custom_settings.items():
                if key in config['sequence_settings']:
                    config['sequence_settings'][key] = value
        
        # Apply brand customization if colors provided
        if brand_colors:
            config = self._apply_brand_customization(config, brand_colors)
        
        return config
    
    def _apply_brand_customization(
        self,
        config: Dict[str, Any],
        brand_colors: List[str]
    ) -> Dict[str, Any]:
        """
        Apply brand-specific customizations to the configuration.
        
        Args:
            config: The sequence configuration
            brand_colors: List of brand colors in hex format
            
        Returns:
            Customized configuration
        """
        # Add brand color metadata for graphics generation
        config['metadata']['brand_colors'] = brand_colors
        
        # Could add more sophisticated brand customization here:
        # - Adjust color grading presets based on brand colors
        # - Modify transition styles based on brand personality
        # - Customize pacing based on brand tone
        
        return config
    
    def generate_premiere_command(
        self,
        template_id: str,
        sequence_name: str,
        brand_colors: Optional[List[str]] = None,
        custom_settings: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate a complete Premiere Pro command for sequence creation.
        
        This creates a command structure that can be sent directly
        to the UXP plugin via WebSocket.
        
        Args:
            template_id: The template to use
            sequence_name: Name for the new sequence
            brand_colors: Optional list of brand colors
            custom_settings: Optional settings overrides
            
        Returns:
            Complete command structure for WebSocket
        """
        config = self.generate_from_template(
            template_id,
            sequence_name,
            brand_colors,
            custom_settings
        )
        
        command = {
            'command_id': f"seq_template_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'action': 'createSequenceFromTemplate',
            'parameters': {
                'template_config': config
            },
            'timestamp': datetime.now().isoformat()
        }
        
        return command
    
    def recommend_template(
        self,
        video_type: Optional[str] = None,
        duration_seconds: Optional[int] = None,
        complexity: Optional[str] = None
    ) -> List[str]:
        """
        Recommend templates based on video characteristics.
        
        Args:
            video_type: Type of video (e.g., 'explainer', 'testimonial')
            duration_seconds: Expected video duration
            complexity: Desired complexity level ('low', 'medium', 'high')
            
        Returns:
            List of recommended template IDs, ordered by relevance
        """
        recommendations = []
        
        for template_id, template in self.templates.items():
            score = 0
            
            # Match video type
            if video_type and template.get('video_type') == video_type:
                score += 10
            
            # Match complexity
            if complexity and template.get('metadata', {}).get('complexity') == complexity:
                score += 5
            
            # Match duration (parse typical_duration_range)
            if duration_seconds:
                duration_range = template.get('metadata', {}).get('typical_duration_range', '')
                # Simple heuristic - could be more sophisticated
                if '1-3' in duration_range and 60 <= duration_seconds <= 180:
                    score += 3
                elif '2-5' in duration_range and 120 <= duration_seconds <= 300:
                    score += 3
                elif '15-60' in duration_range and 15 <= duration_seconds <= 60:
                    score += 3
            
            if score > 0:
                recommendations.append((template_id, score))
        
        # Sort by score (descending)
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        return [template_id for template_id, score in recommendations]
    
    def export_template_summary(self, output_path: str = "template_summary.md"):
        """
        Export a markdown summary of all templates.
        
        Args:
            output_path: Path for the output markdown file
        """
        lines = [
            "# Sequence Template Library",
            "",
            f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Total Templates:** {len(self.templates)}",
            "",
            "---",
            ""
        ]
        
        for template_id, template in self.templates.items():
            lines.extend([
                f"## {template.get('template_name', template_id)}",
                "",
                f"**Template ID:** `{template_id}`",
                f"**Video Type:** {template.get('video_type', 'unknown')}",
                f"**Complexity:** {template.get('metadata', {}).get('complexity', 'unknown')}",
                "",
                f"**Description:** {template.get('description', 'No description')}",
                "",
                "**Sequence Settings:**",
                f"- Resolution: {template.get('sequence_settings', {}).get('width')}x{template.get('sequence_settings', {}).get('height')}",
                f"- Frame Rate: {template.get('sequence_settings', {}).get('frameRate')} fps",
                f"- Audio Sample Rate: {template.get('sequence_settings', {}).get('audioSampleRate')} Hz",
                "",
                "**Track Structure:**",
                f"- Video Tracks: {template.get('sequence_settings', {}).get('videoTrackCount')}",
                f"- Audio Tracks: {template.get('sequence_settings', {}).get('audioTrackCount')}",
                "",
                "**Recommended For:**",
            ])
            
            for use_case in template.get('metadata', {}).get('recommended_for', []):
                lines.append(f"- {use_case}")
            
            lines.extend(["", "---", ""])
        
        with open(output_path, 'w') as f:
            f.write('\n'.join(lines))
        
        print(f"Template summary exported to: {output_path}")


def main():
    """Example usage of the SequenceTemplateGenerator."""
    
    # Initialize generator
    generator = SequenceTemplateGenerator()
    
    print("=== Unwind Visual Cortex - Sequence Template Generator ===\n")
    
    # List available templates
    print("Available Templates:")
    templates = generator.list_templates()
    for i, template in enumerate(templates, 1):
        print(f"{i}. {template['template_name']} ({template['template_id']})")
        print(f"   Type: {template['video_type']} | Complexity: {template['complexity']}")
        print(f"   {template['description'][:80]}...")
        print()
    
    # Generate configuration from template
    print("\n=== Example: Generate Explainer Video Configuration ===\n")
    
    config = generator.generate_from_template(
        template_id="explainer_standard",
        sequence_name="My Product Explainer",
        brand_colors=["#FF5733", "#3498DB", "#2ECC71"],
        custom_settings={
            "frameRate": 60  # Override default 30fps
        }
    )
    
    print(f"Generated Configuration:")
    print(f"Sequence Name: {config['sequence_name']}")
    print(f"Template: {config['template_name']}")
    print(f"Resolution: {config['sequence_settings']['width']}x{config['sequence_settings']['height']}")
    print(f"Frame Rate: {config['sequence_settings']['frameRate']} fps")
    print(f"Brand Colors: {config['metadata']['brand_colors']}")
    print()
    
    # Generate Premiere Pro command
    print("\n=== Example: Generate Premiere Pro Command ===\n")
    
    command = generator.generate_premiere_command(
        template_id="product_demo_dynamic",
        sequence_name="Product Demo - Launch Video",
        brand_colors=["#FF5733"]
    )
    
    print(f"Command ID: {command['command_id']}")
    print(f"Action: {command['action']}")
    print(f"Sequence Name: {command['parameters']['template_config']['sequence_name']}")
    print()
    
    # Recommend templates
    print("\n=== Example: Template Recommendations ===\n")
    
    recommendations = generator.recommend_template(
        video_type="product_demo",
        duration_seconds=120,
        complexity="high"
    )
    
    print(f"Recommended templates for product demo (2 min, high complexity):")
    for template_id in recommendations:
        template = generator.get_template(template_id)
        print(f"- {template['template_name']} ({template_id})")
    print()
    
    # Export summary
    print("\n=== Exporting Template Summary ===\n")
    generator.export_template_summary("template_summary.md")
    
    # Save example configuration
    print("\n=== Saving Example Configuration ===\n")
    with open('example_sequence_config.json', 'w') as f:
        json.dump(config, f, indent=2)
    print("Example configuration saved to: example_sequence_config.json")
    
    # Save example command
    with open('example_premiere_command.json', 'w') as f:
        json.dump(command, f, indent=2)
    print("Example command saved to: example_premiere_command.json")


if __name__ == "__main__":
    main()

"""
AI Video Brain: Multi-Agent Video Editing Intelligence System

This system analyzes video transcripts and brand guidelines to generate
comprehensive, platform-specific video editing recommendations using a
multi-agent architecture with specialized AI agents.

Agents:
1. Brand Analyst - Ensures brand compliance
2. Emotional Tone Expert - Maps emotional arc and pacing
3. Design/Composition Specialist - Generates visual recommendations
4. Sales/Conversion Optimizer - Maximizes engagement and conversions
"""

import json
import os
from typing import Dict, List, Any
from openai import OpenAI

# Initialize OpenAI client (API key pre-configured in environment)
client = OpenAI()


class BrandAnalyst:
    """Agent 1: Analyzes brand compliance and establishes visual/tonal constraints"""
    
    SYSTEM_PROMPT = """You are the **Brand Analyst**, the guardian of brand integrity. Your primary function is to ensure every visual and tonal recommendation aligns perfectly with the provided brand guidelines. 

You will receive:
- Brand assets (logo, color palette, fonts)
- Target audience profile
- Creative brief

Your output must be a **Brand Compliance Matrix** in JSON format that serves as the foundational rule set for all subsequent creative decisions. Analyze with extreme analytical rigor, leaving no room for brand deviation.

Output JSON structure:
{
    "logo_rules": {
        "placement": "string (safe zone recommendations)",
        "sizing": "string (size constraints)",
        "usage_notes": "string"
    },
    "color_palette": {
        "primary_color": "string (hex)",
        "secondary_color": "string (hex)",
        "accent_color": "string (hex)",
        "usage_ratio": "string (60-30-10 rule)",
        "emotional_mapping": "string"
    },
    "typography": {
        "heading_font": "string",
        "body_font": "string",
        "min_size": "string",
        "contrast_requirements": "string"
    },
    "tone_of_voice": {
        "personality": "string (e.g., Professional, Playful, Edgy)",
        "language_style": "string",
        "forbidden_phrases": ["string"]
    },
    "brand_summary": "string (overall brand feel and constraints)"
}"""
    
    def analyze(self, brand_input: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze brand guidelines and return compliance matrix"""
        
        user_message = f"""Analyze the following brand information and create a comprehensive Brand Compliance Matrix:

Brand Name: {brand_input.get('brand_name', 'Not provided')}
Industry: {brand_input.get('industry', 'Not provided')}
Target Audience: {brand_input.get('target_audience', 'Not provided')}

Brand Colors:
- Primary: {brand_input.get('primary_color', 'Not provided')}
- Secondary: {brand_input.get('secondary_color', 'Not provided')}
- Accent: {brand_input.get('accent_color', 'Not provided')}

Typography:
- Heading Font: {brand_input.get('heading_font', 'Not provided')}
- Body Font: {brand_input.get('body_font', 'Not provided')}

Brand Personality: {brand_input.get('brand_personality', 'Not provided')}
Brand Voice: {brand_input.get('brand_voice', 'Not provided')}

Additional Guidelines: {brand_input.get('additional_guidelines', 'None provided')}

Generate a detailed Brand Compliance Matrix in JSON format."""
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            response_format={"type": "json_object"},
            temperature=0.3
        )
        
        return json.loads(response.choices[0].message.content)


class EmotionalToneExpert:
    """Agent 2: Maps emotional arc and recommends pacing"""
    
    SYSTEM_PROMPT = """You are the **Emotional Tone Expert**, a master of narrative psychology. Your task is to dissect the provided video transcript and map its emotional journey.

You will identify:
- Dominant emotions throughout the transcript
- Key tonal shifts and their timing
- Overall pacing required to evoke desired audience response

Your output will be an **Emotional Arc Map** and **Pacing Guide** in JSON format.

Emotion categories: Joy/Excitement, Urgency/Scarcity, Trust/Authority, Curiosity/Intrigue, Sadness/Empathy, Anger/Frustration, Neutral/Educational

Output JSON structure:
{
    "overall_emotional_tone": "string (primary emotion)",
    "emotional_segments": [
        {
            "timestamp_range": "string (e.g., 0:00-0:15)",
            "dominant_emotion": "string",
            "intensity": "string (Low/Medium/High)",
            "key_phrases": ["string"],
            "pacing_recommendation": "string (Fast/Medium/Slow)"
        }
    ],
    "emotional_arc_summary": "string (narrative of emotional journey)",
    "hook_strategy": "string (first 3-5 seconds strategy)",
    "climax_moment": "string (timestamp and description)",
    "editing_rhythm": "string (overall pace guidance)"
}"""
    
    def analyze(self, transcript: str, brand_context: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze transcript emotional arc and return pacing recommendations"""
        
        user_message = f"""Analyze the emotional arc of this video transcript:

TRANSCRIPT:
{transcript}

BRAND CONTEXT:
Brand Personality: {brand_context.get('tone_of_voice', {}).get('personality', 'Not provided')}
Target Audience: {brand_context.get('target_audience', 'Not provided')}

Generate a detailed Emotional Arc Map with pacing recommendations in JSON format."""
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            response_format={"type": "json_object"},
            temperature=0.4
        )
        
        return json.loads(response.choices[0].message.content)


class DesignCompositionSpecialist:
    """Agent 3: Generates visual and compositional recommendations"""
    
    SYSTEM_PROMPT = """You are the **Design/Composition Specialist**, a visual virtuoso. Your role is to translate abstract brand rules and emotional maps into concrete visual art.

Using the Brand Compliance Matrix and Emotional Arc Map, you will generate:
- Detailed B-Roll Shot List
- Visual Composition Guide
- Motion Graphics Plan

Consider platform specifications (Instagram Reels, YouTube Shorts, TikTok) for optimization.

B-Roll types:
- Specific: Directly illustrates spoken content
- Broad: Adds context, mood, atmosphere

Composition principles: Rule of Thirds, Central Composition, Leading Lines, Fill the Frame, Symmetry, Balance

Output JSON structure:
{
    "platform_recommendations": {
        "instagram_reels": {
            "aspect_ratio": "9:16",
            "optimal_length": "string",
            "safe_zones": "string",
            "specific_considerations": "string"
        },
        "youtube_shorts": {
            "aspect_ratio": "9:16",
            "optimal_length": "string",
            "retention_target": "string",
            "specific_considerations": "string"
        },
        "tiktok": {
            "aspect_ratio": "9:16",
            "optimal_length": "string",
            "trend_alignment": "string",
            "specific_considerations": "string"
        }
    },
    "b_roll_shot_list": [
        {
            "timestamp": "string",
            "shot_type": "string (Specific/Broad)",
            "description": "string",
            "composition_rule": "string",
            "duration": "string",
            "emotion_alignment": "string"
        }
    ],
    "visual_composition_guide": {
        "color_grading": "string",
        "lighting_style": "string",
        "camera_movement": "string",
        "framing_strategy": "string"
    },
    "motion_graphics_plan": [
        {
            "timestamp": "string",
            "element_type": "string (text overlay, animation, transition)",
            "content": "string",
            "style": "string",
            "duration": "string"
        }
    ]
}"""
    
    def analyze(self, brand_matrix: Dict[str, Any], emotional_arc: Dict[str, Any], 
                platform: str = "all") -> Dict[str, Any]:
        """Generate visual and compositional recommendations"""
        
        user_message = f"""Generate comprehensive visual and compositional recommendations:

BRAND COMPLIANCE MATRIX:
{json.dumps(brand_matrix, indent=2)}

EMOTIONAL ARC MAP:
{json.dumps(emotional_arc, indent=2)}

TARGET PLATFORM(S): {platform}

Generate a detailed Design & Composition Plan in JSON format with platform-specific optimizations."""
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            response_format={"type": "json_object"},
            temperature=0.5
        )
        
        return json.loads(response.choices[0].message.content)


class SalesConversionOptimizer:
    """Agent 4: Optimizes for engagement and conversions"""
    
    SYSTEM_PROMPT = """You are the **Sales/Conversion Optimizer**, a data-driven persuader. Your mission is to refine the editing blueprint to maximize viewer engagement and drive measurable actions.

Analyze through the lens of:
- Sales psychology
- Platform-specific conversion benchmarks
- Retention optimization

Your output will include:
- Optimized CTA placements
- Retention-hacking techniques
- A/B testing suggestions
- Psychological triggers to employ

Psychological triggers: Curiosity, Scarcity, Social Proof, Reciprocity, Authority, Urgency

CTA placements: Pre-roll (0-5s), Mid-roll (15-30s), Post-roll (end)

Output JSON structure:
{
    "conversion_goal": "string (clicks, purchases, leads, shares)",
    "hook_optimization": {
        "first_3_seconds": "string (specific recommendation)",
        "pattern_interrupt": "string",
        "open_loop_strategy": "string"
    },
    "cta_strategy": [
        {
            "placement": "string (Pre-roll/Mid-roll/Post-roll)",
            "timestamp": "string",
            "cta_text": "string",
            "visual_treatment": "string",
            "psychological_trigger": "string"
        }
    ],
    "retention_hacks": [
        {
            "technique": "string",
            "implementation": "string",
            "expected_impact": "string"
        }
    ],
    "ab_test_suggestions": [
        {
            "element": "string (hook, CTA, thumbnail)",
            "variant_a": "string",
            "variant_b": "string",
            "hypothesis": "string"
        }
    ],
    "psychological_triggers": {
        "primary_trigger": "string",
        "secondary_triggers": ["string"],
        "implementation_notes": "string"
    }
}"""
    
    def analyze(self, design_plan: Dict[str, Any], conversion_goal: str) -> Dict[str, Any]:
        """Optimize for conversions and engagement"""
        
        user_message = f"""Optimize this video editing plan for maximum conversion and engagement:

DESIGN & COMPOSITION PLAN:
{json.dumps(design_plan, indent=2)}

CONVERSION GOAL: {conversion_goal}

Generate a comprehensive Sales & Conversion Optimization Plan in JSON format."""
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": self.SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            response_format={"type": "json_object"},
            temperature=0.4
        )
        
        return json.loads(response.choices[0].message.content)


class AIVideoBrain:
    """Main orchestrator for the multi-agent video editing intelligence system"""
    
    def __init__(self):
        self.brand_analyst = BrandAnalyst()
        self.emotional_expert = EmotionalToneExpert()
        self.design_specialist = DesignCompositionSpecialist()
        self.conversion_optimizer = SalesConversionOptimizer()
    
    def analyze(self, 
                transcript: str,
                brand_input: Dict[str, Any],
                platform: str = "all",
                conversion_goal: str = "engagement") -> Dict[str, Any]:
        """
        Run full multi-agent analysis pipeline
        
        Args:
            transcript: Video transcript text
            brand_input: Dictionary containing brand guidelines
            platform: Target platform(s) - "instagram_reels", "youtube_shorts", "tiktok", or "all"
            conversion_goal: Primary conversion goal - "clicks", "purchases", "leads", "shares", "engagement"
        
        Returns:
            Comprehensive editing blueprint from all agents
        """
        
        print("🧠 AI Video Brain: Multi-Agent Analysis Starting...\n")
        
        # Agent 1: Brand Analysis
        print("👔 Agent 1: Brand Analyst - Analyzing brand compliance...")
        brand_matrix = self.brand_analyst.analyze(brand_input)
        print("✅ Brand Compliance Matrix generated\n")
        
        # Agent 2: Emotional Tone Analysis
        print("💭 Agent 2: Emotional Tone Expert - Mapping emotional arc...")
        brand_matrix['target_audience'] = brand_input.get('target_audience', 'General audience')
        emotional_arc = self.emotional_expert.analyze(transcript, brand_matrix)
        print("✅ Emotional Arc Map generated\n")
        
        # Agent 3: Design & Composition
        print("🎨 Agent 3: Design/Composition Specialist - Creating visual plan...")
        design_plan = self.design_specialist.analyze(brand_matrix, emotional_arc, platform)
        print("✅ Design & Composition Plan generated\n")
        
        # Agent 4: Sales & Conversion Optimization
        print("📈 Agent 4: Sales/Conversion Optimizer - Optimizing for results...")
        conversion_plan = self.conversion_optimizer.analyze(design_plan, conversion_goal)
        print("✅ Conversion Optimization Plan generated\n")
        
        # Consolidate all outputs
        final_blueprint = {
            "meta": {
                "platform": platform,
                "conversion_goal": conversion_goal,
                "analysis_timestamp": "generated"
            },
            "brand_compliance_matrix": brand_matrix,
            "emotional_arc_map": emotional_arc,
            "design_composition_plan": design_plan,
            "conversion_optimization": conversion_plan
        }
        
        print("🎬 AI Video Brain: Analysis Complete!")
        print("=" * 60)
        
        return final_blueprint
    
    def generate_human_readable_report(self, blueprint: Dict[str, Any]) -> str:
        """Convert JSON blueprint to human-readable markdown report"""
        
        report = "# AI Video Brain: Editing Blueprint\n\n"
        
        # Meta information
        report += f"**Platform:** {blueprint['meta']['platform']}\n"
        report += f"**Conversion Goal:** {blueprint['meta']['conversion_goal']}\n\n"
        report += "---\n\n"
        
        # Brand Summary
        brand = blueprint['brand_compliance_matrix']
        report += "## 1. Brand Compliance Matrix\n\n"
        report += f"**Brand Summary:** {brand.get('brand_summary', 'N/A')}\n\n"
        report += f"**Tone of Voice:** {brand.get('tone_of_voice', {}).get('personality', 'N/A')}\n\n"
        
        # Emotional Arc
        emotional = blueprint['emotional_arc_map']
        report += "## 2. Emotional Arc & Pacing\n\n"
        report += f"**Overall Tone:** {emotional.get('overall_emotional_tone', 'N/A')}\n\n"
        report += f"**Hook Strategy:** {emotional.get('hook_strategy', 'N/A')}\n\n"
        report += f"**Editing Rhythm:** {emotional.get('editing_rhythm', 'N/A')}\n\n"
        
        # Design Plan
        design = blueprint['design_composition_plan']
        report += "## 3. Visual & Compositional Recommendations\n\n"
        if 'b_roll_shot_list' in design:
            report += "### B-Roll Shot List:\n\n"
            for i, shot in enumerate(design['b_roll_shot_list'][:5], 1):  # First 5 shots
                report += f"{i}. **{shot.get('timestamp', 'N/A')}** - {shot.get('description', 'N/A')}\n"
                report += f"   - Type: {shot.get('shot_type', 'N/A')}\n"
                report += f"   - Composition: {shot.get('composition_rule', 'N/A')}\n\n"
        
        # Conversion Strategy
        conversion = blueprint['conversion_optimization']
        report += "## 4. Conversion & Engagement Optimization\n\n"
        report += f"**Primary Psychological Trigger:** {conversion.get('psychological_triggers', {}).get('primary_trigger', 'N/A')}\n\n"
        
        if 'cta_strategy' in conversion:
            report += "### CTA Placements:\n\n"
            for cta in conversion['cta_strategy']:
                report += f"- **{cta.get('placement', 'N/A')}** ({cta.get('timestamp', 'N/A')}): {cta.get('cta_text', 'N/A')}\n"
        
        return report


def main():
    """Example usage of the AI Video Brain system"""
    
    # Example brand input
    brand_input = {
        "brand_name": "TechFlow",
        "industry": "SaaS Technology",
        "target_audience": "Tech-savvy entrepreneurs and startup founders aged 25-40",
        "primary_color": "#0066FF",
        "secondary_color": "#00CCFF",
        "accent_color": "#FF6B35",
        "heading_font": "Montserrat Bold",
        "body_font": "Inter Regular",
        "brand_personality": "Professional yet approachable, innovative, trustworthy",
        "brand_voice": "Clear, confident, and empowering. We speak to our audience as equals.",
        "additional_guidelines": "Always emphasize simplicity and efficiency. Avoid jargon."
    }
    
    # Example transcript
    transcript = """
    Are you tired of spending hours on repetitive tasks? Imagine having an AI assistant that actually understands your workflow. 
    
    Introducing TechFlow - the smart automation platform that learns from you. In just 3 clicks, you can automate complex processes that used to take hours.
    
    Our customers have saved an average of 15 hours per week. That's time you can spend on what really matters - growing your business.
    
    Don't let manual work hold you back. Try TechFlow free for 14 days. No credit card required.
    """
    
    # Initialize the AI Video Brain
    brain = AIVideoBrain()
    
    # Run analysis
    blueprint = brain.analyze(
        transcript=transcript,
        brand_input=brand_input,
        platform="all",
        conversion_goal="leads"
    )
    
    # Save full JSON blueprint
    with open('/home/ubuntu/ai_video_brain/example_blueprint.json', 'w') as f:
        json.dump(blueprint, f, indent=2)
    
    # Generate and save human-readable report
    report = brain.generate_human_readable_report(blueprint)
    with open('/home/ubuntu/ai_video_brain/example_report.md', 'w') as f:
        f.write(report)
    
    print("\n📄 Full blueprint saved to: example_blueprint.json")
    print("📄 Human-readable report saved to: example_report.md")


if __name__ == "__main__":
    main()

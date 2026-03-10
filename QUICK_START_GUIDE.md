# AI VIDEO BRAIN: QUICK START GUIDE

## Get Started in 5 Minutes

This guide will help you run your first AI Video Brain analysis immediately.

---

## Step 1: Prepare Your Inputs

You need two things:

### 1. Video Transcript
```
Your complete video script or transcript.
Include all spoken words.
```

### 2. Brand Information
```python
brand_input = {
    "brand_name": "Your Brand Name",
    "industry": "Your Industry",
    "target_audience": "Your target demographic",
    "primary_color": "#HEX",      # Main brand color
    "secondary_color": "#HEX",    # Secondary color
    "accent_color": "#HEX",       # Accent color
    "heading_font": "Font Name",
    "body_font": "Font Name",
    "brand_personality": "Describe your brand personality",
    "brand_voice": "Describe how you communicate",
    "additional_guidelines": "Any other constraints"
}
```

---

## Step 2: Run the Analysis

### Option A: Use the Example Script

```bash
cd /home/ubuntu/ai_video_brain
python3.11 ai_video_brain.py
```

This runs the built-in example and generates:
- `example_blueprint.json` - Full analysis
- `example_report.md` - Human-readable summary

### Option B: Create Your Own Script

```python
from ai_video_brain import AIVideoBrain

# Initialize
brain = AIVideoBrain()

# Your brand info (fill in your details)
brand_input = {
    "brand_name": "MyBrand",
    "industry": "Technology",
    "target_audience": "Tech professionals 25-45",
    "primary_color": "#0066FF",
    "secondary_color": "#00CCFF",
    "accent_color": "#FF6B35",
    "heading_font": "Montserrat Bold",
    "body_font": "Inter Regular",
    "brand_personality": "Professional yet approachable",
    "brand_voice": "Clear and empowering",
    "additional_guidelines": "Emphasize simplicity"
}

# Your transcript
transcript = """
Your complete video transcript here.
Include all the words that will be spoken.
"""

# Run analysis
blueprint = brain.analyze(
    transcript=transcript,
    brand_input=brand_input,
    platform="instagram_reels",  # or "youtube_shorts", "tiktok", "all"
    conversion_goal="engagement"  # or "clicks", "purchases", "leads", "shares"
)

# Save results
import json
with open('my_blueprint.json', 'w') as f:
    json.dump(blueprint, f, indent=2)

# Generate readable report
report = brain.generate_human_readable_report(blueprint)
with open('my_report.md', 'w') as f:
    f.write(report)

print("✅ Analysis complete! Check my_blueprint.json and my_report.md")
```

---

## Step 3: Review Your Results

### JSON Blueprint (`my_blueprint.json`)
Complete technical output with:
- Brand compliance rules
- Emotional arc mapping
- B-roll shot list
- CTA placements
- Psychological triggers

### Markdown Report (`my_report.md`)
Human-readable summary with:
- Brand summary
- Emotional tone analysis
- Top 5 B-roll recommendations
- CTA strategy
- Primary psychological trigger

---

## Platform Options

Choose your target platform:

| Platform | Code | Best For |
|:---------|:-----|:---------|
| Instagram Reels | `"instagram_reels"` | Visual storytelling, lifestyle brands |
| YouTube Shorts | `"youtube_shorts"` | Educational content, retention-focused |
| TikTok | `"tiktok"` | Viral content, trend participation |
| All Platforms | `"all"` | Multi-platform campaigns |

---

## Conversion Goal Options

Choose your primary objective:

| Goal | Code | What It Optimizes |
|:-----|:-----|:------------------|
| Engagement | `"engagement"` | Likes, comments, shares, saves |
| Clicks | `"clicks"` | Link clicks, website visits |
| Purchases | `"purchases"` | Direct product sales |
| Leads | `"leads"` | Email signups, form submissions |
| Shares | `"shares"` | Viral potential, reach |

---

## What You'll Get

### From Agent 1: Brand Analyst
- Logo placement rules
- Color usage guidelines (60-30-10 rule)
- Typography specifications
- Tone-of-voice requirements

### From Agent 2: Emotional Tone Expert
- Overall emotional tone
- Segment-by-segment emotion map
- Hook strategy (first 3-5 seconds)
- Editing rhythm recommendations

### From Agent 3: Design/Composition Specialist
- Platform-specific technical specs
- B-roll shot list with timestamps
- Visual composition guide
- Motion graphics plan

### From Agent 4: Sales/Conversion Optimizer
- Hook optimization strategy
- CTA placements with timestamps
- Retention-hacking techniques
- Psychological triggers to use

---

## Example Output Preview

```markdown
# AI Video Brain: Editing Blueprint

**Platform:** instagram_reels
**Conversion Goal:** purchases

## 1. Brand Compliance Matrix
**Brand Summary:** Professional yet approachable SaaS brand...
**Tone of Voice:** Clear, confident, and empowering

## 2. Emotional Arc & Pacing
**Overall Tone:** Trust/Authority
**Hook Strategy:** Open with relatable pain point...
**Editing Rhythm:** Start moderate, accelerate at excitement peak...

## 3. Visual & Compositional Recommendations
### B-Roll Shot List:
1. **0:00-0:10** - Frustrated entrepreneur at cluttered desk
   - Type: Specific
   - Composition: Rule of Thirds

## 4. Conversion & Engagement Optimization
**Primary Psychological Trigger:** Curiosity
### CTA Placements:
- **Pre-roll** (0:04): Discover how to automate...
- **Mid-roll** (0:25): Ready to save 15 hours/week?
```

---

## Troubleshooting

### "Module not found" error
Make sure you're in the correct directory:
```bash
cd /home/ubuntu/ai_video_brain
```

### "API key not found" error
The OpenAI API key should be pre-configured. Verify:
```bash
echo $OPENAI_API_KEY
```

### Analysis takes too long
Normal execution time is 30-40 seconds. If it takes longer, check your internet connection.

---

## Next Steps

1. **Review the full documentation:** See `README.md` for comprehensive usage guide
2. **Study test cases:** Check `test_cases.py` for 4 diverse examples
3. **Read the master document:** See `AI_VIDEO_BRAIN_MASTER_DOCUMENT.md` for complete system details
4. **Customize agent prompts:** Modify agent system prompts in `ai_video_brain.py` for your specific needs

---

## Quick Reference: Complete Minimal Example

```python
from ai_video_brain import AIVideoBrain

brain = AIVideoBrain()

brand = {
    "brand_name": "TechFlow",
    "industry": "SaaS",
    "target_audience": "Entrepreneurs 25-40",
    "primary_color": "#0066FF",
    "secondary_color": "#00CCFF",
    "accent_color": "#FF6B35",
    "heading_font": "Montserrat Bold",
    "body_font": "Inter Regular",
    "brand_personality": "Professional yet approachable",
    "brand_voice": "Clear and empowering",
    "additional_guidelines": "Emphasize simplicity"
}

transcript = "Your video transcript here..."

blueprint = brain.analyze(transcript, brand, "instagram_reels", "purchases")

print(brain.generate_human_readable_report(blueprint))
```

That's it! You're ready to create intelligent video editing blueprints.

---

**Need Help?** Review the full documentation in `README.md` or the master document in `AI_VIDEO_BRAIN_MASTER_DOCUMENT.md`.

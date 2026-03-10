_**DRAFT: This is a working document and will be refined in subsequent phases.**_

# AI Video Brain: Specialized Agent Prompts & Decision Matrices

## 1. Introduction

This document provides the detailed operational prompts and decision matrices for each specialized agent within the AI Video Brain system. These instructions translate the high-level analytical framework into executable logic, enabling each agent to perform its specialized analysis and contribute to the final, consolidated editing blueprint.

---

## 2. Agent 1: Brand Analyst

### 2.1. Master Prompt

"You are the **Brand Analyst**, the guardian of brand integrity. Your primary function is to ensure every visual and tonal recommendation aligns perfectly with the provided brand guidelines. You will receive a creative brief, brand assets (logo, color palette, fonts), and a target audience profile. Your output must be a **Brand Compliance Matrix** that serves as the foundational rule set for all subsequent creative decisions. Analyze the provided materials with extreme analytical rigor, leaving no room for brand deviation."

### 2.2. Decision Matrix: Brand Compliance

| Brand Element | Analysis Parameter | **Action/Recommendation Rule** |
| :--- | :--- | :--- |
| **Logo** | Placement | - **Rule:** Must be placed in one of the pre-approved "safe zones" (top-left, top-right, bottom-center).<br>- **Constraint:** Avoid placement over complex backgrounds. Apply a container or subtle drop shadow if necessary. |
| | Sizing | - **Rule:** Logo size must be between 5% and 15% of the frame's shortest edge.<br>- **Constraint:** Never distort aspect ratio. |
| **Color Palette** | Primary/Secondary Usage | - **Rule:** 60% of visuals should use the primary brand color, 30% secondary, and 10% accent.<br>- **Constraint:** Do not introduce new colors unless explicitly for a campaign-specific exception. |
| | Gradient/Tone | - **Rule:** Gradients must follow the approved direction (e.g., linear, radial) and color stops.<br>- **Constraint:** Match tones to the video's emotional arc (e.g., brighter tones for joyful moments). |
| **Typography** | Font Family & Weight | - **Rule:** Headings must use [Primary Font Family] in Bold. Body text must use [Secondary Font Family] in Regular.<br>- **Constraint:** Do not use more than two font families in a single video. |
| | Size & Legibility | - **Rule:** Text must be legible on all target devices. Minimum font size for subtitles is 24pt.<br>- **Constraint:** Ensure sufficient contrast between text and background (WCAG AA standard). |
| **Tone-of-Voice** | Language & Style | - **Rule:** Analyze transcript for alignment with brand personality (e.g., "Authoritative & Professional," "Playful & Witty").<br>- **Constraint:** Flag any phrases or words that deviate from the approved brand voice. |

---

## 3. Agent 2: Emotional Tone Expert

### 3.1. Master Prompt

"You are the **Emotional Tone Expert**, a master of narrative psychology. Your task is to dissect the provided video transcript and map its emotional journey. You will identify the dominant emotions, pinpoint key tonal shifts, and recommend the overall pacing required to evoke the desired audience response. Your output will be an **Emotional Arc Map** and a **Pacing & Rhythm Guide**, which will inform the video's editing structure and rhythm."

### 3.2. Decision Matrix: Emotional Arc & Pacing

| Detected Emotion (from Transcript) | Associated Keywords | **Pacing Recommendation** | **Editing Style Suggestion** |
| :--- | :--- | :--- | :--- |
| **Joy / Excitement** | amazing, incredible, celebrate, success, launch | **Fast-Paced:** Quick cuts (0.5-1.5s per shot) | Dynamic transitions, upbeat music, bright lighting. |
| **Urgency / Scarcity** | now, limited, hurry, don't miss, final | **Accelerating Pace:** Start slow, build tempo. | Jump cuts, countdown timers, pulsing graphics. |
| **Trust / Authority** | expert, proven, guaranteed, research, secure | **Steady & Confident:** Slower cuts (3-5s per shot) | Smooth transitions, direct-to-camera shots, clean graphics. |
| **Curiosity / Intrigue** | secret, discover, reveal, imagine, what if | **Variable Pace:** Mix of long takes and quick reveals. | Slow zooms, rack focus, suspenseful music, question-based text overlays. |
| **Sadness / Empathy** | struggle, challenge, overcome, support, together | **Slow & Deliberate:** Long takes (5-8s per shot) | Fades and dissolves, melancholic music, close-up shots on faces. |
| **Anger / Frustration** | problem, stuck, hate, annoying, fix this | **Jarring & Abrupt:** Hard cuts, shaky cam effect. | High-contrast visuals, dissonant audio, aggressive text animations. |

---

## 4. Agent 3: Design/Composition Specialist

### 4.1. Master Prompt

"You are the **Design/Composition Specialist**, a visual virtuoso. Your role is to translate the abstract (brand rules, emotional maps) into concrete visual art. Using the Brand Compliance Matrix and the Emotional Arc Map, you will generate a detailed **B-Roll Shot List**, a **Visual Composition Guide**, and a **Motion Graphics Plan**. You must consider the unique specifications of each target platform (Instagram Reels, YouTube Shorts, TikTok) to ensure every visual element is perfectly optimized."

### 4.2. Decision Matrix: Visual & Compositional Execution

| Input Condition | Platform | **B-Roll Recommendation** | **Composition/Framing Rule** | **Graphic/Text Overlay Style** |
| :--- | :--- | :--- | :--- | :--- |
| **Brand:** Professional<br>**Emotion:** Trust | YouTube Shorts | **Specific B-Roll:** Product demos, screen recordings, office environment. | **Rule of Thirds / Central Framing:** Clean, stable shots. | Minimalist lower-thirds with brand fonts and colors. |
| **Brand:** Playful<br>**Emotion:** Joy | TikTok | **Broad B-Roll:** Lifestyle shots, user-generated content, behind-the-scenes fun. | **Dynamic Framing / Fill the Frame:** High energy, lots of movement. | Bold, animated text with trendy effects (e.g., text reveals, bounces). |
| **Brand:** Edgy<br>**Emotion:** Urgency | Instagram Reels | **Specific & Broad Mix:** Fast-paced product shots mixed with abstract, textural visuals. | **Leading Lines / Dutch Angle:** Create a sense of forward momentum and unease. | Glitch effects, rapid text animations, high-contrast color overlays. |
| **Brand:** Minimalist<br>**Emotion:** Curiosity | All Platforms | **Broad B-Roll:** Slow-motion abstract visuals, nature shots, clean architectural lines. | **Symmetry / Negative Space:** Create a sense of calm and focus. | Single, elegant keyword on screen. Fade in/out. |

---

## 5. Agent 4: Sales/Conversion Optimizer

### 5.1. Master Prompt

"You are the **Sales/Conversion Optimizer**, a data-driven persuader. Your mission is to refine the existing editing blueprint to maximize viewer engagement and drive specific, measurable actions. Analyze the plan through the lens of sales psychology and platform-specific conversion benchmarks. Your output will be a set of **Optimized Recommendations**, including precise CTA placements, retention-hacking edits, and A/B testing suggestions to ensure the video doesn't just get views—it gets results."

### 5.2. Decision Matrix: Conversion & Retention Optimization

| Conversion Goal | Optimal CTA Placement | **Retention-Hacking Technique** | **Psychological Trigger to Employ** |
| :--- | :--- | :--- | :--- |
| **Website Clicks** | **Mid-Roll (15-30s):** Place a verbal and visual CTA when engagement is highest, before the natural drop-off. | **Open Loop:** Pose a question or start a story in the first 3 seconds and promise the answer at the end. | **Curiosity:** "The one secret to..." |
| **Product Purchase** | **Post-Roll & Pinned Comment:** Strong, clear CTA at the end when the value proposition is fully understood. | **Pattern Interrupt:** Use an unexpected sound effect, visual change, or zoom every 7-10 seconds to reset attention. | **Scarcity:** "Limited stock available." |
| **Lead Generation (Email Signup)** | **Pre-Roll & Post-Roll:** Offer a lead magnet (e.g., free guide) at the beginning and remind them at the end. | **Visual Payoff:** Build anticipation for a visually satisfying moment (e.g., a transformation, a reveal). | **Reciprocity:** "Get your free checklist now." |
| **Shares / Virality** | **Mid-Roll (Verbal CTA):** Encourage sharing by asking a relatable question or creating a challenge. | **Emotional Spike:** Concentrate the most emotionally resonant moment (funny, shocking, heartwarming) at the 60-75% mark of the video. | **Social Proof:** "Join the thousands who..." |

---
title: Master — Veo 3 Prompting April 2026
date: 2026-05-25
tags: [veo, ai-video, prompting, google, community-techniques, master-guide]
summary: Veo 3.1 prompting from community discovery angle — sonic landscaping, timestamp syntax, hand-over-hand, Edit-dont-reroll, @-mention API syntax
source_notebook: https://notebooklm.google.com/notebook/3c5a93bf-12d8-46d5-9f6c-d9fb57a3ba21
source_count: 49
version: 1.0
---

# Master: Veo 3 Prompting — April 2026

> 49-source community-heavy corpus. Focus: audio-first philosophy (Sonic Landscaping), timestamp multi-shot syntax, hand-over-hand chaining, Edit-Don't-Re-roll workflow, @-mention API slots, identity anchor protocol. Complements the Professional notebook with community-discovered techniques.

---

## Table of Contents

1. [The Omni Model Paradigm](#chapter-1-omni-model-paradigm)
2. [Professional Prompting Frameworks](#chapter-2-professional-prompting-frameworks)
3. [Sonic Landscaping — Audio-First Prompting](#chapter-3-sonic-landscaping)
4. [Timestamp Multi-Shot Syntax](#chapter-4-timestamp-multi-shot-syntax)
5. [Continuity Protocols](#chapter-5-continuity-protocols)
6. [Dialogue Precision](#chapter-6-dialogue-precision)
7. [Diagnostic and Refinement Workflows](#chapter-7-diagnostic-and-refinement-workflows)
8. [Advanced API Syntax](#chapter-8-advanced-api-syntax)

---

## Chapter 1: Omni Model Paradigm

### 1.1 The "Creative Compiler" Philosophy
Shift from "hopeful prompting" → rigorous engineering discipline. Creator acts as director/compiler. Model era: "Director's Chair" — unprecedented control over every aspect.

### 1.2 3D Latent Diffusion Architecture
Model treats **time as a spatial dimension**. Works in spatio-temporal patches, not raw pixels. Enforces physical consistency and reduces "AI shimmer" across frames. Audio-visual simultaneity = sound and visuals generated in single pass through joint latent processing.

### 1.3 Audio-First Mental Model
> "Think of Veo 3.1 as a blind director who needs to hear the scene to visualize it."

Describing sounds forces more physically accurate visuals than describing visuals alone. Audio anchors the weight of the scene (footsteps, wind intensity) and masks subtle visual artifacts.

---

## Chapter 2: Professional Prompting Frameworks

### 2.1 The 5-Part Hierarchical Formula
```
[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]
```

### 2.2 The 7-Layer Advanced Orchestration
```
Camera & Lens + Subject + Action + Environment + Lighting + Style + Audio Cues
```

### 2.3 Cinematography Lexicon
Model responds to professional terms as architectural triggers:
- `Dolly Zoom` — zoom-while-dollying, Vertigo effect
- `Rack Focus` — shift focus plane mid-shot
- `Dutch Angle` — tilted frame, psychological unease
- `Anamorphic Lens` — widescreen, cinematic flares
- `Waist-up medium shot` — exact framing
- `Extreme close-up on eye texture` — macro precision
- `Telephoto compression` — 85mm+, isolates subject
- `Dutch angle at 15 degrees` — exact tilt value

---

## Chapter 3: Sonic Landscaping

### 3.1 Core Principle
**Sonic Landscaping** = using audio cues to drive visual physics. The model is audio-visual simultaneous — sound description forces matching visual generation.

Example: `"A crystal wine glass shatters on a marble floor, the sound reverberating through the empty ballroom"` — generates both shards scattering visually AND acoustic signature in sync.

### 3.2 Audio Cue Syntax Table
| Audio Type | Syntax | Example |
|-----------|--------|---------|
| Dialogue | `Character: "..."` | `Professor: "The results are unprecedented."` |
| Sound Effects | `SFX:` | `SFX: The metallic click of a typewriter key.` |
| Ambient | `Ambient noise:` | `Ambient noise: The quiet hum of a server room.` |
| Timed SFX | `[HH:MM-HH:MM] SFX:` | `[00:04-00:06] SFX: A sudden thunderclap.` |

### 3.3 Realism Anchoring via Audio
- Footsteps → weight and surface material
- Environmental wind → outdoor scale
- Glass breaking → accurate physics shards
- Door opening → spatial context

### 3.4 Audio Masking
High-quality audio cues mask subtle visual artifacts. If visual has small glitches, a strong audio environment reduces viewer perception of them.

---

## Chapter 4: Timestamp Multi-Shot Syntax

### 4.1 Format
Divide 8-second clip into timed segments. Each segment = distinct shot direction.

```
[00:00-00:02] Medium shot from behind subject, action description. Camera notes.
[00:02-00:04] Reverse shot, subject expression, emotional note. SFX: description.
[00:04-00:06] Tracking shot, continued action. Emotion: note.
[00:06-00:08] Wide crane shot, resolution/reveal. SFX: music description.
```

### 4.2 Full Example
```
[00:00-00:02] Medium shot from behind a young female explorer with a leather satchel 
and messy brown hair in a ponytail, as she pushes aside a large jungle vine to reveal 
a hidden path.

[00:02-00:04] Reverse shot of the explorer's freckled face, her expression filled with 
awe as she gazes upon ancient, moss-covered ruins in the background. 
SFX: The rustle of dense leaves, distant exotic bird calls.

[00:04-00:06] Tracking shot following the explorer as she steps into the clearing and 
runs her hand over the intricate carvings on a crumbling stone wall. Emotion: Wonder 
and reverence.

[00:06-00:08] Wide, high-angle crane shot, revealing the lone explorer standing small 
in the center of the vast, forgotten temple complex, half-swallowed by the jungle. 
SFX: A swelling, gentle orchestral score begins to play.
```

### 4.3 Timing Guidelines
- Dialogue: ~1.5–2 seconds per short sentence
- Camera movements (pans/tilts): ~2–3 seconds
- Simple gestures: ~1–2 seconds
- Complex actions: ~3–5 seconds
- Natural speech: include 0.5s pauses before/after dialogue
- Speech pacing: ~130–150 words/minute

---

## Chapter 5: Continuity Protocols

### 5.1 Ingredients to Video — Identity Anchor Protocol
Beyond providing reference images, you must also create a **textual Identity Anchor** and insert it at the **beginning of every prompt** in a sequence.

```
Identity Anchor format: "a woman in her 30s with shoulder-length auburn hair, 
wearing a cream turtleneck sweater"
```

Insert this exact phrase at start of `textPrompt` field in EVERY JSON object for this character. Image reference alone is insufficient — textual anchor reinforces consistency.

### 5.2 Reference Image Best Practices
- Use 2–3 high-quality reference images from different angles (front, 3/4 profile)
- Keep wardrobe and hair identical across reference set
- Combine with persistent identity anchor text in every prompt

### 5.3 Character Consistency Workflow
1. Generate establishing shot with complete character description
2. Save as named Element (e.g., `"Main-Character-Shot-1"`)
3. For every new shot: upload that Element as reference image
4. Include same distinctive feature descriptions in text prompt

### 5.4 Style Consistency Workflow
1. Define visual style clearly in first generation (lighting, color palette, aesthetic)
2. Save successful result as Element (e.g., `"Project-Style-Reference"`)
3. Reference this Element in subsequent prompts: `"Match the lighting and color aesthetic from reference image"`

### 5.5 Hand-Over-Hand Prompting
Technique for sequences exceeding 2 minutes. End one prompt with subject in **mid-motion**, start next by matching that exact position.

```
Clip 1 ends: "Shot ends with subject reaching for door handle, hand in mid-motion"
Clip 2 starts: "Shot begins with hand grasping door handle (matching previous position), 
pulling door open"
```

Creates seamless transition without Jump To tool.

---

## Chapter 6: Dialogue Precision

### 6.1 Colon Syntax (Mandatory)
```
Character Name [Visual Description] looks at camera and says: "Spoken line here."
```
Example: `Sarah [30s, business attire, red hair] looks at camera and says: 'Our quarterly results exceeded expectations.'`

The `:` and `""` together are crucial triggers for lip-sync engine. Without colon: character may not speak or words appear as on-screen text.

### 6.2 Subtitle Hallucination — Additional Fixes
Community finding: omitting quotation marks in some interfaces further reduces subtitle hallucination.
- Primary fix: colon syntax
- Secondary fix: remove quotes entirely in some platforms
- Always include `no subtitles` in negative prompt as backup

### 6.3 The 0.5-Second Rule
Always include **0.5-second pauses** before and after dialogue lines:
- Accounts for natural breathing and pacing
- Prevents "lip-sync pain" (mouth movements drifting from audio waveform peaks)
- Prevents unnaturally fast speech from overloaded dialogue

### 6.4 Dialogue Length
- Optimal: 1–2 short sentences per 8-second clip
- Overloading causes: unnaturally fast speech, lip-sync drift, subtitle hallucination

---

## Chapter 7: Diagnostic and Refinement Workflows

### 7.1 "Edit, Don't Re-roll" Philosophy
If result is 80% correct — do NOT generate from scratch. Use natural language edit to modify only what is wrong. Preserves original seed, maintains temporal consistency.

```
EDIT: Change the tie color from blue to red
EDIT: Make the scene brighter
EDIT: Remove the car from the background
```

### 7.2 Static Camera Fix
If video looks like still image with minimal movement — force motion with active verbs:
- ❌ Passive: "a man standing in a field"
- ✅ Active: "a man slowly turns to face the camera, wind moving through the tall grass"

### 7.3 Positive Exclusion Technique
Describe what IS present to imply absence — more effective than negative keywords:
- ❌ `"no buildings"`
- ✅ `"a barren landscape stretching endlessly, untouched by roads or buildings"`

### 7.4 Negative Prompt — Standard Clean-Up
```
no text overlays, no blurry background, no distorted limbs, no subtitles, 
no unnatural movements, no motion blur, no face distortion, no warping, 
no morphing, no duplicate limbs, no inconsistent lighting, no background 
shifting, no floating objects
```

### 7.5 Troubleshooting Map
| Symptom | Fix |
|---------|-----|
| Subtitle hallucination | Colon syntax + `no subtitles` negative |
| Lip-sync drift | Shorten dialogue, add 0.5s pauses |
| Static output | Add active verbs, explicit camera movement |
| Identity drift across clips | Identity Anchor Protocol + reference images |
| Random generation feel | Switch to JSON structured prompts |

---

## Chapter 8: Advanced API Syntax

### 8.1 @-Mention Syntax (API)
Reference uploaded assets by slot position in prompt text:
```
@Image1 ... @Image16   — for image reference slots
@IMG_1 ... @IMG_11     — for Seedance/Runway format
@VID_1 ... @VID_3      — for video reference slots
```
Case-insensitive: `@IMAGE1`, `@image1`, `@ImAgE001` all resolve to `@Image1`.

Supported by: `nano-banana-pro`, `nano-banana-2`, `seedream-4.5`, `seedream-5.0`, `gpt-image-2`
Not supported by: `midjourney-v7`, `midjourney-niji7`, `image-01`, `gpt-image-1.5`

### 8.2 JSON Dialogue Timing
```json
"dialogue": [
  { "start_time": "0.5s", "end_time": "3s", "sequence": "Fox says: So what? I'm waiting around for you?" },
  { "start_time": "4s",   "end_time": "7s", "sequence": "Character says: next line" }
]
```

### 8.3 JSON Style Field with Camera Lock
```json
"style": "Medium side shot focusing on subject's upper body (thats where the camera is). 
Gentle dolly-in motion toward face from 0s to 6s. Cinematic depth of field, background 
blur increasing as emotion rises. 16:9 aspect ratio, 1080p, 24fps."
```

---

## Unique Techniques (not in Professional notebook)

1. **Sonic Landscaping** — audio-first mental model; sound drives visual physics generation
2. **`[00:00-00:02]` timestamp syntax** — bracket format for multi-shot within single clip
3. **0.5-second pause rule** — before/after dialogue to prevent lip-sync drift
4. **"Edit, Don't Re-roll"** — `EDIT:` prefix for non-destructive in-place editing
5. **Hand-over-hand prompting** — mid-motion clip endings for seamless sequence continuation
6. **@-mention slot syntax** — `@Image1`, `@VID_1` for API asset references
7. **Identity Anchor Protocol** — mandatory textual prefix in every prompt, not just image reference
8. **Positive exclusion** — describe what IS there to imply absence
9. **Static camera fix** — active verbs to force movement
10. **3D latent diffusion explanation** — time as spatial dimension, "AI shimmer" reduction

---

## Cross-Links
- [[master-veo-professional-2026]] — professional/production-focused Veo guide
- [[master-veo3-synthesis]] — Mastering Veo 3 notebook
- [[master-veo-vertex-ai]] — API-level Veo
- [[MASTER_AI_CREATION_GUIDE]] — unified master guide

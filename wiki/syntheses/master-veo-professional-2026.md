---
title: Master — Veo Professional Prompting May 2026
date: 2026-05-25
tags: [veo, ai-video, prompting, google, production, master-guide]
summary: Comprehensive Veo 3.1 professional prompting guide — model specs, syntax formulas, JSON schemas, continuity workflows, troubleshooting
source_notebook: https://notebooklm.google.com/notebook/09b39c77-cbe4-483c-b890-2476b3f67bef
source_count: 49
version: 1.0
---

# Master: Veo Professional Prompting — May 2026

> 49-source NotebookLM covering Veo 3.1 ecosystem — model IDs, exact syntax, JSON schemas, continuity workflows, troubleshooting trees, industry templates. Covers Veo 3.1 Standard / Fast / Lite and Gemini Omni roadmap.

---

## Table of Contents

1. [Veo 3.1 Ecosystem Overview](#chapter-1-veo-31-ecosystem-overview)
2. [Standardized Prompting Frameworks](#chapter-2-standardized-prompting-frameworks)
3. [Cinematography and Visual Control](#chapter-3-cinematography-and-visual-control)
4. [Integrated Audio and Dialogue Production](#chapter-4-integrated-audio-and-dialogue-production)
5. [Continuity and Narrative Workflows](#chapter-5-continuity-and-narrative-workflows)
6. [Model Variations and Technical Specifications](#chapter-6-model-variations-and-technical-specifications)
7. [Structured Refinement and Quality Control](#chapter-7-structured-refinement-and-quality-control)
8. [Example Libraries and Industry Templates](#chapter-8-example-libraries-and-industry-templates)
9. [Platform-Specific Workflows](#chapter-9-platform-specific-workflows)

---

## Chapter 1: Veo 3.1 Ecosystem Overview

### Evolution
Veo 3.1 marks shift from "random output" to "directed filmmaking." Key advances over Veo 3: cinematic HD generation (720p/1080p/4K), advanced physics simulation (fluids, materials), integrated audio-visual simultaneity.

### Model Line (as of 2026-05)
| Model | API ID | Status |
|-------|--------|--------|
| Veo 3.1 Standard | `veo-3.1-generate-preview` | Preview |
| Veo 3.1 Fast | `veo-3.1-fast-generate-preview` | Preview |
| Veo 3.1 Lite | `veo-3.1-lite-generate-preview` | Preview (released 2026-03-31) |
| Veo 3 / Veo 3 Fast | — | Stable |
| Veo 2 | — | Stable (being phased out) |

### Roadmap: Gemini Omni
Anticipated paradigm shift — unified native generation of text, image, video, and audio in single pass. 24/7 personal agent capabilities. No confirmed release date (as of 2026-05).

---

## Chapter 2: Standardized Prompting Frameworks

### 2.1 The 5-Part Foundational Formula (DeepMind Standard)
```
[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance]
```
- **Cinematography:** Framing, camera movement, lens type
- **Subject:** Key character or focal object
- **Action:** What is happening
- **Context:** Location, environment, time of day
- **Style & Ambiance:** Lighting, tone, mood, artistic treatment

### 2.2 The 7-Component Production Framework
```
[Subject] + [Action] + [Scene] + [Style] + [Dialogue] + [Sounds] + [Technical/Negatives]
```
Adds Dialogue, Sounds, and Negative prompts for production-ready results.

### 2.3 The 8-Component Master Formula
```
Subject + Context + Action + Style + Camera + Composition + Ambiance + Audio
```

| Component | Purpose | Example |
|-----------|---------|---------|
| Subject | Main focus + character details | "A confident 35-year-old CEO with short auburn hair" |
| Context | Scene setting | "in a modern glass-walled boardroom at sunset" |
| Action | What is happening | "she presents quarterly results with animated gestures" |
| Style | Visual aesthetic | "cinematic corporate style with warm color grading" |
| Camera | Shot type + movement | "smooth dolly-in from medium to close-up" |
| Composition | Framing | "rule of thirds, subject left-positioned, bokeh background" |
| Ambiance | Lighting + mood | "golden hour light through windows, professional warmth" |
| Audio | Sound design + dialogue | "she says: 'Our Q3 results exceeded all expectations'" |

### 2.4 Directorial Precision Keywords
Use "keywords of intent" to trigger specific architectural pathways:
- Lighting: `Rembrandt lighting`, `Rack focus`, `Chiaroscuro`
- Camera: `Dolly shot`, `Orbit/Arc`, `Crane`, `handheld micro-stabilization`
- Lens: `16mm`, `35mm`, `85mm`, `Macro`

### 2.5 JSON vs Natural Language Performance
Controlled test — 50 generations each, same semantic goal:

| Metric | Natural Language | JSON Structure |
|--------|-----------------|----------------|
| First-try success rate | 34% | **78%** |
| Avg iterations to approval | 4.2 | **1.6** |
| Token cost | 1.0x baseline | **0.7x baseline** |
| Temporal consistency | 23% | **71%** |

→ **Use JSON structured prompts for all production work.**

### 2.6 Prompt Length Constraints
- Optimal: 150–300 characters
- Below 100: generic results
- Above 400: model prioritizes unpredictably, ignores elements

---

## Chapter 3: Cinematography and Visual Control

### 3.1 Camera Positioning Syntax — Critical
Lock perspective with exact phrase:
```
[Camera Position/Height] + (thats where the camera is)
```
Example: `Camera at knee height (thats where the camera is)`

This triggers camera-aware processing. Must be included in quality checklist.

### 3.2 Camera Movement Library
- **Dolly:** Linear push/pull along subject axis
- **Orbit/Arc:** Circular movement around subject
- **Crane:** Vertical lift or descent
- **Handheld micro-stabilization:** Subtle organic movement

### 3.3 Optics and Lens Control
Use specific lens profiles — not distance cues:
- `16mm` — wide, environmental
- `35mm` — natural perspective
- `85mm` — portrait, compressed background
- `Macro` — extreme close detail

### 3.4 Lighting Control
Use Kelvin temperatures for precise mood:
- `3000K` — warm candlelight
- `5600K` — daylight neutral
- `10000K` — cold blue

Named setups: `Three-point`, `Chiaroscuro`, `Butterfly`, `Neon Bi-color`, `Rembrandt`

For directional control: specify `window`, `side light direction`, `soft/hard quality`, `colour temperature`, `emotional effect`.

---

## Chapter 4: Integrated Audio and Dialogue Production

### 4.1 Native Audio Generation
Veo 3.1 generates audio simultaneously with video. Native 48kHz audio. Dialogue precision within **120ms**.

Includes: dialogue, SFX, ambient soundscapes — all in single generation pass.

### 4.2 Dialogue Syntax — COLON FORMAT (MANDATORY)
```
Character: "Exact dialogue content"
```
**NEVER use quote-only format** — causes on-screen subtitle hallucination.

Verified: ✅ `she says: "line"` — prevents subtitles
❌ `"line"` — causes subtitles

### 4.3 Dialogue Optimization
- Optimal per clip: **12–15 words** or **20–25 syllables**
- Designed for 8-second clip timing
- Include emotional tone, delivery style, pacing, volume, accent in dialogue component

### 4.4 Timestamp Prompting
Direct multi-shot sequences within single 8-second generation:
```json
"dialogue": [
  { "start_time": "0s", "end_time": "2.5s", "sequence": "Character action: dialogue here" },
  { "start_time": "3s", "end_time": "6s", "sequence": "Next action: dialogue here" }
]
```

### 4.5 Audio Prompt Categories
- **Layered Soundscapes:** Multiple ambient layers
- **Natural Environments:** Weather, nature, outdoor
- **Professional Settings:** Office, studio, technical environments
- **Music Integration:** `Mood-Based`, `Genre-Specific Scoring`, `Dynamic Musical Development`
- **SFX:** Action-synchronized, movement/impact, technology/interface sounds

---

## Chapter 5: Continuity and Narrative Workflows

### 5.1 Ingredients to Video (Consistency Mode)
Upload up to **3 reference images** to anchor identity:
1. **Subject reference** — character identity lock
2. **Scene reference** — environmental consistency
3. **Style reference** — visual treatment lock

Requires 8-second generation length.

### 5.2 Start Frame / End Frame Control
- **First Frame:** Lock spatial composition, lighting, character position for new clip
- **Last Frame:** Create seamless continuation from previous clip
- Define visual anchors for controlled transitions and specific camera trajectories

### 5.3 Scene Extension and Chaining
Model analyzes **final 24 frames (1 second)** of input video to maintain continuity.
- Max chained segments: **20**
- Total duration: ~**140 seconds**
- Extension resolution: **720p only** (no 4K in extensions)

Extension prompting rule: describe natural progressions, not sudden changes.
- ❌ `"the scene switches to indoors"`
- ✅ `"the camera follows the character as they walk through the doorway"`

### 5.4 Jump To Tool
Generates new clips starting precisely where previous ended (Google Flow).

### 5.5 Character Consistency Framework
Requires **≥15 specific physical attributes** to prevent identity drift:
- Age, ethnicity, hair texture, eye expression, distinctive marks, clothing, posture, mannerisms, emotional state, build, skin tone, facial structure, accessories, movement style, voice characteristics

### 5.6 Scene Architecture Template
Requires **≥10 environmental elements**:
- Lighting setup, props, atmospheric haze, spatial relationships, background elements, surface textures, color palette, time of day, weather/atmosphere, architectural details

---

## Chapter 6: Model Variations and Technical Specifications

### 6.1 Full Spec Table (as of 2026-05)

| Feature | Veo 3.1 Standard | Veo 3.1 Fast | Veo 3.1 Lite | Veo 3 | Veo 2 |
|---------|-----------------|--------------|--------------|-------|-------|
| Audio | ✅ Always on | ✅ Always on | ✅ Always on | ✅ Always on | ❌ Silent |
| Resolution | 720p, 1080p, 4K | 720p, 1080p, 4K | 720p, 1080p | 720p, 1080p | 720p |
| 4K requirement | 8s only | 8s only | ❌ No 4K | — | — |
| 1080p requirement | 8s only | 8s only | 8s only | — | — |
| Duration | 4s, 6s, 8s | 4s, 6s, 8s | 4s, 6s, 8s | 8s | 5–8s |
| Frame rate | 24fps | 24fps | 24fps | 24fps | 24fps |
| Scene extension | ✅ | ✅ | ❌ | ✅ | — |
| Reference images | ✅ | ✅ | ✅ | — | — |
| Videos per request | 1 | 1 | 1 | 1 | 1 or 2 |
| Status | Preview | Preview | Preview | Stable | Stable |

### 6.2 The 80/20 Prototyping Rule
- Use **Fast** for first 80% (ideation + refinement) — saves ~30% token costs
- Switch to **Standard** for final delivery only
- Use **Lite** for high-volume pipeline automation

### 6.3 Model Selection Matrix

| Use Case | Recommended |
|----------|-------------|
| Social media content | Fast |
| E-commerce product display | Fast |
| Ad testing / iteration | Fast |
| Corporate promos (draft) | Fast |
| Movie trailers | Standard |
| High-end brand ads | Standard |
| Professional film/TV | Standard |
| News flash visuals | Fast |
| Education/training | Fast |
| Artistic experimentation | Fast → Standard |

### 6.4 API Parameters

```
Text input limit: 1,024 tokens
Max outputs per prompt: 4 video variations
Output format: MP4
Aspect ratios: "16:9" or "9:16"
```

**JSON Type Safety (strict):**
```json
"movement.speed": "slow" | "medium" | "fast"   // string enum, NOT integer
"focal_length": "24mm"                           // string with unit, NOT bare number
"negative_prompts": ["subtitles", "watermarks"] // array of strings, NOT single string
"personGeneration": "allow_all" | "allow_adult" | "dont_allow"
```

---

## Chapter 7: Structured Refinement and Quality Control

### 7.1 Pre-Generation Quality Checklist
```
✅ Subject includes ≥15 attributes
✅ Scene includes ≥10 environmental elements
✅ Camera positioning includes "(thats where the camera is)"
✅ Dialogue uses colon syntax (NO standalone quotation marks)
✅ Audio environment specified
✅ Negative prompts included
✅ Duration ≤ 8 seconds
✅ Proper JSON formatting
```

### 7.2 The "No-List" Negative Prompting System
Three tiers of exclusion:
- **Must-not:** Absolute exclusion
- **Avoid:** Strong de-prioritization
- **De-emphasize:** Soft suppression

**Standard Negative Packs:**

Pack 1 — Anatomy artifacts:
```
extra fingers, duplicate limbs, warped hands, morphing face, floating body parts
```

Pack 2 — Face/identity drift:
```
no face distortion, no warping, no morphing, no identity shift
```

Pack 3 — Text/logos:
```
text, captions, subtitles, watermark, logo, brand mark, readable words, typography
```

Pack 4 — Extra limbs / crowds:
```
third arm, duplicated legs, phantom person, extra people, crowd artifacts
```

### 7.3 Positive Anchoring (Superior to Negative Prompting)
Use positive anchors instead of naming defects:
- ❌ `no extra fingers`
- ✅ `anatomically plausible hands with five fingers`

### 7.4 Object Count Precision
For exact counts (works up to ~15 identical items):
```
"Only [number]" or "Exactly [number]" — front-loaded in prompt
```
Example: `"Only six lanterns float slowly across the surface of a misty lake..."`

### 7.5 Physics Keywords
```
realistic fluid dynamics, momentum conservation, accurate gravity, structural integrity
```

### 7.6 Troubleshooting Decision Trees
- **Silent failure:** Check audio prompt component, verify model version supports audio
- **Subtitle hallucination:** Fix colon syntax — character: "dialogue"
- **Identity drift:** Add ≥15 character attributes + reference image

---

## Chapter 8: Example Libraries and Industry Templates

### 8.1 E-commerce / Product Hero
- 360-degree rotation shots
- Macro detail close-ups
- Unboxing simulation sequences

### 8.2 Corporate / Interview
- Professional "talking head" setup
- Sunlit office b-roll
- Diversity-focused scene compositions

### 8.3 Creative Genre Templates
| Genre | Key Techniques |
|-------|---------------|
| Sci-Fi world-building | Cold colour temp, structural lighting, physics keywords |
| Film Noir | Chiaroscuro, low key, shadow-heavy composition |
| Horror tension | Slow push-in, low angle, silence then sharp audio |
| Documentary Vérité | Handheld micro-stabilization, natural lighting |

---

## Chapter 9: Platform-Specific Workflows

### 9.1 Google Flow and Vids
- Integrated editing, asset management, sequence assembly
- Jump To tool for clip chaining
- Native timeline for extension assembly

### 9.2 Vertex AI and Gemini API
- Asynchronous operations for enterprise-scale deployment
- `veo-3.1-generate-preview` endpoint
- Polling pattern for long-running generation jobs

### 9.3 Partner Integrations
| Platform | Role |
|----------|------|
| LTX Studio | Node-based production pipeline |
| VEED | Editor-centric post-production |
| Phygital+ | Advanced compositing |

---

## Unique Techniques (not in Theoretical Media master)

1. **`(thats where the camera is)` syntax** — exact phrase triggers camera-aware processing
2. **Colon dialogue format** — community-verified subtitle prevention
3. **JSON structured prompts** — 34%→78% first-try success (tested, not theoretical)
4. **Timestamp dialogue arrays** — multi-moment direction in single 8-second clip
5. **≥15 character attributes / ≥10 scene elements** — minimum thresholds for consistency
6. **Positive anchoring** — describe what you want, not what to avoid
7. **Veo 3.1 Lite** — <50% cost of Fast, high-volume pipeline use case

---

## Cross-Links
- [[master-veo3-prompting-april-2026]] — earlier Veo 3 prompting corpus
- [[master-veo3-synthesis]] — Mastering Veo 3 notebook
- [[master-veo-vertex-ai]] — API-level Veo workflows
- [[MASTER_AI_CREATION_GUIDE]] — unified master guide

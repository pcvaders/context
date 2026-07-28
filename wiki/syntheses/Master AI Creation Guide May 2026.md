---
title: MASTER — AI Image and Video Creation Guide 2026
date: 2026-05-25
tags: [ai-video, ai-image, prompting, production-pipeline, master-guide, gemini-omni, wiki]
summary: Single pristine source of truth. Phase 1–4 pipeline output. 14 canonical models, master JSON template, full production pipeline, constraints table, Gemini Omni reference architecture.
source_notebook: https://notebooklm.google.com/notebook/69fa8912-f30b-45c8-a5b3-694e2dfec5f8
phase: 4
version: 1.3
---

# MASTER: AI Image and Video Creation Guide — 2026

> **Phase 4 output.** Compiled from 100-source NotebookLM notebook via programmatic extraction pipeline.
> Phases applied: 1 (Extract) → 2 (Gap Detection) → 3 (Temporal Dominance + Template Dedup + I2V Merge) → 4 (Final Compile).
> **Re-upload this file into a fresh NotebookLM as your definitive single source of truth.**

---

## 1. Core Architecture — Deduplicated Model Stack

> Source: Phase 1–3 pipeline output. 26 raw variants → 14 canonical models.
> Temporal Dominance applied: older family members collapsed into newest version.

### Tier 1 — Flagship Cloud (Multimodal / Dialogue-Native)

| Model | Owner | Signature Capability | Access |
|---|---|---|---|
| **Veo 3.1** | Google DeepMind | 4K native, dialogue + Foley in-generation, Scene Builder, 3 tiers: Standard / Fast / Lite | Google Ultra $250/mo · API `veo-3.1-generate-preview` |
| **Sora 2** | OpenAI | 16s standard / 25s Pro, Cameo likeness, storyboard mode | ChatGPT Plus/Pro |
| **Kling 3.0** | Kuaishou | Motion king — Character Binding, time-coded multi-shot lists, voice elements | kling.ai |
| **Seedance 2.0** | Byte Dance | Thinking model with RAG — plans physics + story before rendering | seaart.ai |

### Tier 2 — Specialized & Open Source (Video)

| Model | Owner | Signature Capability | Access |
|---|---|---|---|
| **LTX-2.3** | Lightricks | Open weights, 4K/50fps/HDR, local-runnable (32GB VRAM req) | HuggingFace / LTX Desktop |
| **WAN 2.6** | Alibaba | Audio-to-video lip sync, bilingual, subject referencing | wan-video.com |
| **Luma Ray 3** | Luma AI | Modify tool (motion transfer), EXR transparency, video-to-video | lumalabs.ai |
| **Runway** | Runway AI | Story Panels (stacks), script-to-storyboard, commercial-safe training | runwayml.com |
| **Pika** | Pika Labs | Real-time avatar chat, agentic personality (Pika Me) | pika.art |

### Tier 3 — Image Generation & Editing

| Model | Owner | Signature Capability | Access |
|---|---|---|---|
| **Nano Banana 2** | Google (Gemini Flash Image) | Conversational segmentation, consistent multi-character referencing, thinking-based edits | Google AI Studio / Gemini |
| **FLUX.1** | Black Forest Labs | JSON/hex precision, 8.4GB VRAM (Klein variant), 4MP detail, open source | ComfyUI / Replicate |
| **Midjourney V8** | Midjourney | SREF style codes, 360° turnarounds, lookbook consistency | discord.gg/midjourney |
| **Stable Diffusion** | Stability AI | Local ControlNet, IP-Adapter, LoRA training, workflow backbone | ComfyUI local |

### Tier 4 — Infrastructure & Orchestration

| Model / Tool | Role |
|---|---|
| **ComfyUI** | Node-based local orchestration, App Mode, Comfy Cloud for remote GPU |

### Temporal Dominance Collapses Applied (Phase 3 Rule 1)

| Canonical Kept | Variants Dropped |
|---|---|
| Veo 3 Pro | Veo, Veo 2, Veo 3 |
| WAN 2.6 | WAN, WAN 2.5 |
| LTX-2.3 | LTX, LTX-2 |
| Luma Ray 3 | Luma |
| Kling 3.0 | Kling, Kling 01 |
| Seedance 2.0 | Seedance |
| Midjourney V8 | Midjourney |
| Nano Banana 2 | Nano Banana, NanoBanana |
| FLUX.1 | FLUX |
| Sora 2 | Sora, Sora 1 |

---

## 2. Standardized Prompting Framework

> Single canonical template. All redundant structural variants collapsed here (Phase 3 Rule 2).

---

### 2.1 The Master 4-Step Prompt Workflow

```
Step 1 — DRAFT      : Describe scene in plain English to a thinking LLM (Claude / Gemini)
Step 2 — TRANSLATE  : Ask: "Convert to JSON with Camera, Subject, Environment, Lighting, Action buckets"
Step 3 — REFINE     : Replace glue words with technical terms (e.g. "AR Alexa 35", "14mm fisheye", "#FF4400")
Step 4 — EXECUTE    : Paste final JSON or expanded text into target video generator
```

---

### 2.2 Master JSON Prompt Template

```json
{
  "CAMERA": {
    "lens": "24mm wide-angle",
    "movement": "slow dolly forward",
    "framing": "medium shot",
    "depth_of_field": "shallow, subject sharp, background bokeh"
  },
  "SUBJECT": {
    "description": "[CHARACTER — age, ethnicity, costume, expression]",
    "action": "[VERB — what they are doing]",
    "position": "[SPATIAL — left/center/right, foreground/mid/background]",
    "hands": "[EXPLICIT — e.g. 'left hand holds one cup, right hand at side']"
  },
  "ENVIRONMENT": {
    "location": "[SETTING — interior/exterior, era, style]",
    "time_of_day": "[LIGHTING SOURCE — golden hour / overcast / neon night]",
    "background": "[ELEMENTS — what is visible behind subject]"
  },
  "LIGHTING": {
    "style": "[KEY LIGHT style — Rembrandt / hard rim / soft box]",
    "colour": "[HEX or descriptor — warm #FF8C42 / cool #4A90D9]",
    "mood": "[EMOTION — oppressive / intimate / clinical]"
  },
  "MOTION": {
    "subject_movement": "[VELOCITY and direction]",
    "physics": "[REALISM NOTE — realistic gravity / exaggerated cartoon]",
    "duration": "[SECONDS — e.g. 8s]"
  },
  "AUDIO": {
    "dialogue": "[EXACT LINE — in quotes, with speaker tag]",
    "foley": "[AMBIENT SOUNDS — footsteps on gravel, distant rain]",
    "music": "[STYLE — sparse piano / epic orchestral / none]"
  },
  "TECHNICAL": {
    "aspect_ratio": "16:9",
    "resolution": "4K",
    "fps": "24",
    "style_reference": "[SREF code or LORA name if applicable]"
  }
}
```

---

### 2.3 Workflow-Specific Templates

#### T1 — Text-to-Video (T2V) — Single Shot
```
[LENS] [MOVEMENT] shot of [SUBJECT] [ACTION] in [ENVIRONMENT].
[LIGHTING DESCRIPTOR]. [PHYSICS NOTE]. [DURATION]s clip.
Audio: [DIALOGUE/FOLEY/MUSIC].
```
Example:
```
24mm wide-angle slow dolly forward, medium shot of a weathered Viking (50s, grey beard, chainmail)
sharpening a sword at a cluttered workshop bench. Late afternoon golden hour through a cracked window.
Realistic metal-on-stone scraping sounds. No music. 8s.
```

#### T2 — Image-to-Video (I2V) — Reference Frame
```
[UPLOAD reference image first]
Animate: [SUBJECT] [MOVEMENT/ACTION], [DURATION]s, [PHYSICS].
Camera: [MOVEMENT]. Audio: [FOLEY].
Maintain all character details from reference image exactly.
```

#### T3 — Audio-to-Video Lip Sync (WAN 2.6)
```
[UPLOAD audio file first]
Character: [DESCRIPTION — face, costume, lighting].
Generate lip-sync video matching uploaded audio exactly.
Environment: [SETTING]. Duration: match audio length.
```

#### T4 — Multi-Shot with Time Codes (Kling 3.0)
```
Shot 1 [0–3s]: [WIDE SHOT — establishing scene]
Shot 2 [3–6s]: [MEDIUM — character reacts]
Shot 3 [6–10s]: [CLOSE-UP — detail/payoff]
Character binding: [ELEMENT ID or reference image]
```

#### T5 — Semantic Image Editing (Nano Banana 2)
```
[UPLOAD image]
Edit: [NATURAL LANGUAGE INSTRUCTION — "Move the umbrella to the right", "Replace jacket with red coat"]
Preserve: [LIST ELEMENTS TO KEEP — face, background, lighting angle]
```

---

### 2.4 Prompt Hygiene Rules

| Rule | Action |
|---|---|
| **Double Fisting Fix** | Always specify: "left hand holds X, right hand Y" — prevents AI giving characters two objects |
| **Glue Word Purge** | Remove: a, the, in, some, very, really, just — replace with technical specifics |
| **Token Noise Reset** | If images degrade or get "jaggy" after long sessions — start a new chat |
| **Contact Sheet Trick** | Combine multiple character reference angles into ONE image for better identity lock |
| **Context Handoff** | When LLM gets "lazy" from long sessions — ask it to "write a handoff prompt" before new session |
| **Hex Colours** | Use `#RRGGBB` codes for exact brand colours in FLUX.1 and JSON prompts |
| **Vocal Cadence** | In Veo 3 Pro: add "natural human vocal cadence, no robotic rhythm" to dialogue prompts |

---

### 2.5 Visual Prompting (Annotation-Based)

Supported by: **Veo 3 Pro**, **Nano Banana 2**

```
[UPLOAD annotated image — draw on it first]
Red arrow pointing at [OBJECT]: [INSTRUCTION — "this is where X appears"]
Bounding box around [AREA]: "[DESCRIPTION of change]"
```

---

### 2.6 The NotebookLM Master Extraction Protocol

Use this to extract full synthesised content from large source sets:

**Step 1 — Blueprint Prompt:**
```
Act as a master editor. Review all sources. Create a deeply nested Table of Contents.
1. Merge overlapping concepts into single sections — zero duplication.
2. Break into Part 1, Part 2 etc. with sub-bullets.
3. Output structure only — no content yet.
```

**Step 2 — Section Synthesis Prompt (repeat per section):**
```
Write ONLY Section [N]: [TITLE].
Rules: professional tone, all technical data, step-by-step workflows, direct quotes.
No filler. Clean markdown with H2/H3 and bullets.
```

**Step 3 — Prompt Library Extractor:**
```
Extract every specific text-to-video prompt example in the sources.
For each: identify target model, intended outcome, explain why the structure works.
Format as a copy-pasteable library.
```

---

### 2.7 Production-Ready Prompt Frameworks

#### 7-Component Framework — Veo 3.1 Production Standard

Every production Veo prompt must include **all seven components**:

| # | Component | Spec Requirement |
|---|---|---|
| 1 | **Subject** | Character/object with ≥15 physical attributes |
| 2 | **Action** | Specific actions, gestures, timing, micro-expressions |
| 3 | **Scene** | Environment with ≥10 elements |
| 4 | **Style** | Camera shot type, angle, movement, aspect ratio, lighting |
| 5 | **Dialogue** | Colon-syntax with tone/delivery, time sequences |
| 6 | **Sounds** | Ambient + activity-specific audio (SFX + ambiance) |
| 7 | **Technical (Negative)** | Elements to exclude — subtitles, watermarks, artifacts |

#### 8-Component Formula — Extended Text Prompt

```
[Subject] + [Action] + [Context] + [Style] + [Camera] + [Composition] + [Ambiance] + [Audio]
```

Full example:
```
Medium shot of a young woman with auburn hair walking through a neon-lit Tokyo street at night.
She pulls her coat tighter, expression contemplative. Rain reflects neon signs on wet pavement.
Camera slowly tracks behind her. Cool blue and pink neon lighting, volumetric light rays.
Soft jazz faintly. SFX: footsteps on wet pavement, distant traffic, ambient city hum.
Cinematic, moody, Japanese cyberpunk aesthetic. 1080p, 6 seconds, 16:9, no subtitles.
```

#### Nano Banana 2 — Core Syntax

```
[Subject + Adjectives] doing [Action] in [Location/Context].
[Composition/Camera Angle]. [Lighting/Atmosphere]. [Style/Media]. [Specific Constraint/Text].
```

#### Seedance 2.0 — 6-Step Formula

| Step | Element | Requirement | Example |
|---|---|---|---|
| 1 | **Subject** | Who/what — specific visual features | "A young woman in a white dress" |
| 2 | **Action** | What happens — specific verbs, quantified | "Slowly turns around, breeze blowing the skirt" |
| 3 | **Environment** | Where — lighting and atmosphere | "Seaside at dusk, golden glow" |
| 4 | **Camera** | How to shoot — ONE primary instruction | "Camera slow push-in" |
| 5 | **Style** | Visual feel — specific references | "Style cinematic film tone, 35mm" |
| 6 | **Constraints** | What to avoid | "Avoid jitter and bent limbs" |

> Aim for 60–100 words. Use ONE camera instruction. Lighting description > 10 adjectives. Change one variable at a time when iterating.

---

### 2.8 Audio & Dialogue Formatting Rules

#### Dialogue Format (Veo 3.1 — Community-Verified)

```
✅ WORKS — Colon Format (Prevents Subtitles):
Character says: [dialogue here] (no subtitles)

❌ FAILS — Quote Format (Causes Subtitles):
Character said "dialogue here"
```

**Rules:**
- Never use quotation marks around dialogue — triggers on-screen text
- Always include `(no subtitles)` to prevent unwanted captions
- Keep dialogue to ~30–40 words (fits 8-second clip)
- Multiple speakers: `Character 1: [line]. Character 2: [line]. (no subtitles)`

#### SFX Specification Format

```
SFX: [specific sound], [timing anchor if needed]
Example: "SFX: thunder cracks as the door slams, footsteps on wet cobblestone, distant sirens"
```

#### Audio No-List — Seedance / UGC Ads Universal Closer

```
- No music, No logo, no text on screen.
```
Always end every Seedance UGC prompt with this exact line. Strips library audio, auto-generated brand marks, and baked-in captions.

---

### 2.9 Advanced Prompt Control Techniques

#### Front-Loading Principle (Veo 3.1)
Veo assigns higher weight to prompt-start content. Structure:
1. Primary subject + core action (most weight)
2. Camera and composition
3. Setting and context
4. Visual style and lighting
5. Audio and technical specs (least weight — but still required)

#### Timestamp Prompting — Multi-Shot in Single Generation

```
[00:00–00:02] Medium shot from behind explorer pushing aside jungle vine to reveal hidden path.
[00:02–00:04] Reverse close-up of explorer's face with awe at moss-covered ruins. SFX: bird calls.
[00:04–00:06] Tracking shot as explorer runs hand over stone carvings.
[00:06–00:08] Wide crane shot revealing explorer at center of vast temple complex. SFX: orchestral swell.
```

> **Seedance variation:** `0-4s: Wide shot... 4-9s: Lens switch to extreme close-up... 9-15s: Pan right...`

#### Lens Switch (Seedance 2.0)
Keyword `lens switch` triggers a hard cinematic cut between shot sizes *within a single generation* — e.g., wide establishing → extreme close-up, no NLE required.

#### Camera Positioning Syntax (Veo 3.1)
Append `(thats where the camera is)` to lock perspective in style field.
```
"Style: low-angle medium shot looking up at character (thats where the camera is)"
```

#### Seed Banking (Any Model)
Once you achieve a desired look, **note the seed number** — reuse it to extend or vary safely without identity drift.

#### The 80/20 Cost Optimisation Rule
- **First 80% of work:** Veo 3.1 Fast (ideation, prompt refinement, variations) — saves ~60% costs
- **Final 20%:** Veo 3.1 Standard (hero deliverables)

---

## 3. Technical Constraints & Capabilities

### 3.1 Video Generation — Master Specification Table

| Model | Max Duration | Resolution | FPS | Audio | I2V | Multi-Shot | Access Tier |
|---|---|---|---|---|---|---|---|
| **Veo 3.1 Standard** | 8s native (chain up to 20×) | 4K / 1080p | 24fps | ✅ Native dialogue + Foley | ✅ | ✅ Scene Builder | Google Ultra / API `veo-3.1-generate-preview` |
| **Veo 3.1 Fast** | 8s | 1080p | 24fps | ✅ | ✅ | ✅ | ~1/5th cost; 2× speed; `veo-3.1-fast-generate-preview` |
| **Veo 3.1 Lite** | 8s | 720p / 1080p | 24fps | ✅ | ✅ | ❌ Scene ext. | <50% cost of Fast; `veo-3.1-lite-generate-preview` |
| **Sora 2** | 16s standard / 25s Pro | 1080p | — | ❌ No native audio | ⚠️ No realistic people | ❌ | ChatGPT Plus/Pro |
| **Kling 3.0** | 15s | 4K (3840×2160) | 30fps | ✅ Voice elements | ✅ | ✅ Time-coded | kling.ai |
| **Seedance 2.0** | ~10s | 1080p | — | ❌ | ✅ | ❌ | seaart.ai |
| **LTX-2.3** | Variable | 4K / HDR | 50fps | ❌ | ✅ | ❌ | Local (32GB VRAM) / HuggingFace |
| **WAN 2.6** | 15s | 1080p / 720p / 480p | 30fps | ✅ Audio-to-video lip sync | ✅ | ❌ | wan-video.com |
| **Luma Ray 3** | — | — | — | ❌ | ✅ Modify tool | ❌ | lumalabs.ai |
| **Runway** | — | — | — | ❌ | ✅ | ✅ Story Panels | runwayml.com |
| **Pika** | — | — | — | ❌ | ✅ | ❌ | pika.art |

**Key caveats:**
- **Sora 2**: Watermarks on all outputs. No I2V for realistic people faces. Prompt limit ~850 chars. Cameo feature for custom characters.
- **Kling 3.0**: Dialogue drift occurs in last 3–5s of long clips — structure critical dialogue in first 10s.
- **WAN 2.6**: Open weights available for local deployment.
- **Veo 3 Pro**: Veo 2 being phased out ($20/mo Pro tier, lower fidelity). Aspect ratios: 16:9, 9:16, 4:3, 2:1.

---

### 3.2 Image Generation — Specification Table

| Model | Resolution | Key Format | VRAM (local) | Strengths | Weaknesses |
|---|---|---|---|---|---|
| **Nano Banana 2** | Up to 4MP+ | Conversational NL | Cloud only | Thinking-based edits, multi-character, world knowledge | Token noise in long sessions |
| **FLUX.1** | 4MP | JSON + Hex | 8.4GB (Klein) / 24GB (full) | Precision colour, realistic skin, open source | Slower than cloud alternatives |
| **Midjourney V8** | — | Natural language + SREF | Cloud only | Style consistency, SREF codes, 360° turnarounds | No API, Discord-only |
| **Stable Diffusion** | Variable | LoRA, ControlNet, IP-Adapter | 6–24GB | Maximum local control, custom training | Setup complexity |

---

### 3.3 Local Deployment Hardware Gates

| VRAM | Capability |
|---|---|
| 8.4GB (e.g. RTX 3060 Ti) | FLUX.1 Klein, basic ComfyUI workflows |
| 12GB (e.g. RTX 3060) | Ground floor — most basic SD workflows |
| 24GB (e.g. RTX 3090/4090) | High-quality local image gen, LTX-2 optimised |
| 32GB (e.g. RTX 5090) | LTX-2.3 full-quality local video gen |
| Cloud (RunPod H100/B200) | Any model, no VRAM constraint, pay-per-run |

---

### 3.4 Audio Tools Reference

| Tool | Function | Format | Notes |
|---|---|---|---|
| **Google LIIA 3 (Lyria)** | Text + image → music composition | 48k stereo, up to 3min | Multimodal — accepts image for vibe matching |
| **Ace Studio Video Composer** | Video → auto-timed Foley + soundtrack | Sync to video timeline | Gold standard for filmmaker Foley |
| **Meta SAM Audio** | Visual stem splitting | Any | Isolates specific sounds from mixed recordings |
| **11 Labs Music** | Vocal-centric music generation | — | Best for one-shot genre pieces |
| **Whisper Flow** | Voice-to-text prompt dictation | — | Verbal macros: name a snippet, speak to expand |

---

### 3.5 Post-Production Tool Reference

| Tool | Function | Key Feature |
|---|---|---|
| **Topaz Astra / Starlight** | Video upscaling + frame interpolation | Industry standard |
| **Magnific Video** | Creative upscaling | Preserve Faces + Vivid modes |
| **Dehancer** | Film grain, halation, analog texture | Grain + bloom emulation |
| **EbSynth** | Keyframe-based video restyling | AI After Effects equiv |
| **ComfyUI** | Local node workflow orchestration | App Mode = simplified GUI |

---

### 3.6 Key Model Quirks & Known Failure Modes

| Model | Known Issue | Fix |
|---|---|---|
| Any dialogue model | "Double Fisting" — two props given simultaneously | Specify: "left hand holds X, right hand Y" |
| Thinking image models | Token quantization noise after long sessions | Start new chat session |
| Veo 3 Pro / Kling 3.0 | Dialogue drift in last 3–5s of clip | Front-load critical dialogue; regenerate tail |
| Nano Banana 2 | Identity drift across multiple generations | Use Contact Sheet (all angles in 1 image) |
| LTX-2.3 | 32GB VRAM hardgate on consumer hardware | Use ComfyUI quantised weights or RunPod cloud |
| Sora 2 | Cannot I2V realistic human faces | Use Kling 3.0 or Veo 3 Pro for face I2V |

---

### 3.7 Negative Prompting System

#### Principle
Negative prompts are a **supporting clause** — the shot must stand on positives alone. Use positives first, negatives to stabilise only.

**Never say "no X" or "don't show X"** — use descriptive exclusion instead:
| ❌ Instructive (Bad) | ✅ Descriptive (Good) |
|---|---|
| "No walls" | "Open desert landscape stretching endlessly" |
| "No buildings" | "Untouched barren terrain, no man-made structures" |
| "Don't show text" | "Completely blank walls, unbranded surfaces" |

#### 3-Tier System

| Tier | Purpose | Examples |
|---|---|---|
| **Tier 1 — Must-Not** | Hard policy blocks | Violence, minors, protected IP, public figures |
| **Tier 2 — Avoid** | Technical artifact prevention | extra fingers, fused hands, uncanny warping, duplicate people |
| **Tier 3 — De-emphasise** | Style drift reduction | cartoon, anime, oversaturation, HDR halo |

#### 7 Ready-to-Copy No-List Packs (Veo 3.1)

| Pack | Use Case | No-List |
|---|---|---|
| **Pack 1 — Hands** | Gesturing, holding objects | `extra fingers, extra hands, fused fingers, deformed hands, twisted fingers, broken anatomy` |
| **Pack 2 — Faces** | Portraits, dialogue | `uncanny valley, asymmetric face, dead eyes, distorted jaw, melting features` |
| **Pack 3 — Text/Logos** | Any clean scene | `text, captions, subtitles, watermark, logo, brand mark, readable words, typography` |
| **Pack 4 — Extra Limbs** | Full-body, crowds | `third arm, phantom limb, duplicate person, extra legs, merging bodies` |
| **Pack 5 — Flicker/Jitter** | Product, architecture | `flicker, jitter, shimmer, brightness swings, pulsing` |
| **Pack 6 — Watermark Artifacts** | Commercial output | `watermark, UI overlay, interface smear, glitch artifact` |
| **Pack 7 — Style Drift** | Cinematic realism | `cartoon, anime, illustration, oil painting, sketch, hyper-saturated, over-processed, HDR halo` |

#### Constraint Asymmetry Rule (Nano Banana)
Prohibitions (negative) **94%** compliance vs. Mandatory (positive) **91%**. Where possible, reformulate positive requirements as negative exclusions:
- `"all edges sharp"` → `"NO blurred edges"` (+3% compliance)

---

### 3.8 Troubleshooting — Failure Matrix

#### Veo 3.1 / Google Flow Failure Matrix

| Symptom | Most Likely Cause | Fix |
|---|---|---|
| **Silent failure before clip** | Wrong surface / unsupported region / no credits | Check Flow availability, credit balance, supported model |
| **Fails only with specific feature** | Feature combination unsupported | Switch model/feature pairing or simplify |
| **Dialogue prompt fails consistently** | Experimental audio path | Test silent version first; isolate audio issue |
| **Safety filter triggered** | Named public figures, protected IP, sensitive content | Rewrite blocked part — do not retry same wording |
| **504 DEADLINE_EXCEEDED** | Too-short client-side API timeout | Increase client deadline in API settings |
| **429 Resource Exhausted** | Rate limit or credit overage | Smooth traffic spikes; check Ultra credit balance (25k/month) |
| **Subtitle Hallucination** | Dialogue in quote format | Switch to Colon Format; add `no subtitles` to negative |
| **Identity Drift** | Low subject specification | Use 1–3 high-quality 1024×1024 reference images |
| **Character shifts clothes/face** | Inconsistent descriptors across prompts | Paste identical base character description verbatim |
| **Jerky / chaotic motion** | Multiple conflicting actions | One clear action per clip; shorten clip duration |

**Credit Tiers (May 2026):**
- Free: 50 daily AI credits
- Google AI Pro ($19.99/mo): 1,000 monthly credits
- Google AI Ultra ($249/mo): 25,000 monthly credits

#### Seedance 2.0 Artifact Ladder

| Artifact Type | Description | Fix |
|---|---|---|
| **Flicker** | Per-frame brightness/color swings | Pin camera: "locked tripod, zero camera shake"; lock light: "even diffuse lighting" |
| **Jitter** | Edge quiver, logo vibration | "Locked tripod, zero camera shake"; "constant exposure" |
| **Warp** | Geometry bends/snaps, hands stretch | Remove unstable material keywords: sequins, mesh, micro-pattern |
| **Texture Crawl** | Fabric/grass "swims" | Ban problem materials; name timebase: "24fps feel" |

---

## 4. Unified Core Architecture — Full Production Pipeline

> Phase 3 Rule 3: All image-to-video and workflow references merged into one section.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI FILM PRODUCTION PIPELINE                               │
│                                                                               │
│  CONCEPT ──► SCRIPT ──► STORYBOARD ──► ASSET GEN ──► VIDEO GEN ──► POST    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Phase A — Pre-Production

| Step | Tool | Action |
|---|---|---|
| 1. Script | Plot Horizon / Claude | Generate + iterate rough draft |
| 2. Storyboard | Rubber Band | Auto-sketch from script |
| 3. Character Bible | Notion AI | Store bibles, link scenes to characters |
| 4. Visual Reference | Midjourney V8 + SREF codes | Lock style and aesthetic |
| 5. Voice Elements | Kling 3.0 Voice Library | Train character voices once |

### Phase B — Asset Generation

| Step | Tool | Action |
|---|---|---|
| 6. Hero Image | Midjourney V8 or FLUX.1 | Generate key character / location |
| 7. 3D Virtual Set | World Labs Marble | Gaussian splat the hero image → navigable 3D |
| 8. Angle Snapshots | Marble (WASD + Enter) | Screenshot 10 consistent camera angles |
| 9. Character Placement | Nano Banana 2 | Place character into each Marble screenshot |
| 10. Contact Sheet | Manual | Combine all character angles into one reference image |

### Phase C — Video Generation

| Step | Tool | Action |
|---|---|---|
| 11. Prompt Build | Claude / Gemini | Draft → JSON → Refine glue words |
| 12. T2V First Pass | Veo 3 Pro or Kling 3.0 | Generate hero clip from JSON prompt |
| 13. I2V Extension | Veo 3 Pro Scene Builder | Extend 8s clips, regenerate bad tails |
| 14. Motion Transfer | Luma Ray 3 Modify | Restyle footage while preserving movement |
| 15. Lip Sync | WAN 2.6 Audio-to-Video | Drive character mouths from voice recording |
| 16. Multi-Shot | Kling 3.0 | Time-coded cut list in single generation |

### Phase D — Audio

| Step | Tool | Action |
|---|---|---|
| 17. Score | Google LIIA 3 | Upload hero image → AI composes matched track |
| 18. Foley | Ace Studio Video Composer | Import video → auto-timed sound effects |
| 19. Room Tone | AI ambient gen | "Office quiet ambience" under dialogue tracks |
| 20. Vocal Stack | 11 Labs Music | Generate genre-specific backing vocals |

### Phase E — Post-Production

| Step | Tool | Action |
|---|---|---|
| 21. Upscale | Topaz Astra / Magnific | Upscale + frame interpolation |
| 22. Restyle | EbSynth | Keyframe-based aesthetic polish |
| 23. Film Grade | Dehancer | Add grain, halation, analog texture |
| 24. Object Clean | Object Removal (Runway) | Remove artifacts, clean plates |

---

### The I2V Master Workflow (Standalone)

```
1. GENERATE base image ─────── Midjourney V8 or FLUX.1
2. BUILD 3D SPACE ──────────── World Labs Marble (Gaussian splat)
3. SNAPSHOT ANGLES ─────────── WASD navigation → Enter to capture
4. PLACE CHARACTER ─────────── Nano Banana 2 (with Contact Sheet reference)
5. ANIMATE ─────────────────── Veo 3 Pro or Kling 3.0 (I2V mode)
6. EXTEND ──────────────────── Veo 3 Pro Scene Builder (+ 8s at a time)
7. MOTION TRANSFER ─────────── Luma Ray 3 Modify (preserve movement, restyle look)
8. LIP SYNC ────────────────── WAN 2.6 (upload audio → matched lip movement)
9. ALPHA COMPOSITE ─────────── Export with transparency → composite into live footage
```

---

## 5. Google DeepMind Gemini Omni — Reference Architecture

> Source: Gemini Omni official documentation synthesis. Direct framework, no external links.
> Omni uses **world reasoning** rather than keyword stuffing — architecture differs fundamentally from legacy models.

---

### 5.1 The 5-Dimension Prompting Framework

Structure every Gemini Omni prompt across these 5 dimensions in this order. **Subject must appear first** — word position determines computational weight.

| # | Dimension | What to Define | Example |
|---|---|---|---|
| 1 | **Shot Framing & Motion** | Camera movement and angle | tracking shot, crane, macro close-up, cinematic pan |
| 2 | **Style** | Aesthetic or artistic medium | photorealistic, risograph, claymation, architectural rendering |
| 3 | **Lighting** | Light sources, temperature, atmosphere | volumetric side-lighting, high-contrast neon, 10 o'clock golden hour |
| 4 | **Scene** | Core environment and background assets | empty brutalist loft, neon Tokyo alley, deep ocean floor |
| 5 | **Action & Interaction** | Subject behaviour + object relationships | hummingbird sipping nectar, gears meshing in exact sequence |

**Master Template:**
```
[SUBJECT] — [FRAMING/MOTION] — [SCENE] — [ACTION/INTERACTION] — [STYLE] — [LIGHTING]
```

**Example (fully structured):**
```
A close-up tracking shot of an intricate clockwork hummingbird rapidly flapping its brass gears
and glass wings to sip glowing blue nectar from a neon orchid, captured in a high-contrast
cinematic style with intense volumetric side-lighting.
```

---

### 5.2 Conversational Editing & Iteration Logic

Omni treats generation as **stateful iterative dialogue** — do not rewrite entire prompts. Reference prior output directly.

#### Targeted Modification
```
"Keep the entire scene identical, but alter the lighting to high-contrast monochrome."
```

#### Stylistic Progression
```
"Transition the previous output seamlessly into a hand-drawn colored crayon aesthetic
with rich textured strokes on granulated paper."
```

#### Add / Remove Element
```
"Keep everything in the previous video exactly the same, but add animated glowing particle
effect trails coming off the hummingbird's wings."
```

---

### 5.3 Constraint Handling — Negative Space via Positive Exclusion

**Do not use legacy negative prompting tags** (`--no blur, ugly, deformed`). These force world-reasoning tokens to focus on excluded elements — degrades output quality.

| ❌ Legacy (Bad) | ✅ Omni (Good) |
|---|---|
| `"Modern kitchen --no retro, no mess, no people"` | `"A pristine, completely empty minimalist modern kitchen. Marble countertops entirely bare and spotless. No human presence."` |
| `"Street scene --no cars"` | `"A pedestrian-only cobblestone plaza with zero vehicle access. Only foot traffic visible."` |

**Rule:** Describe the absolute state of the scene — what IS there, not what should be absent.

---

### 5.4 Typography Rendering

Omni maps text directly to scene geometry. For precise string rendering:

```
"Word by word, one word on screen at a time: 'REDEFINE REASONING'.
Each word displays a different animated neon liquid style with perfect
rhythmic pacing for a high-energy sizzle reel."
```

**Key:** Explicit pacing instruction + isolation of text string = accurate letter-level rendering.

---

### 5.5 Tool Integration & Function Calling

When building custom tools or passing APIs to Gemini Omni, use this schema structure:

```json
{
  "name": "fetch_production_metrics",
  "description": "Retrieves real-time rendering queues and processing latency metrics. Use ONLY when user asks about system delay, render queues, or video generation backlogs. Returns JSON of active pipeline statuses.",
  "parameters": {
    "type": "OBJECT",
    "properties": {
      "pipeline_id": {
        "type": "STRING",
        "description": "Unique identifier for the targeted generation cluster."
      }
    },
    "required": ["pipeline_id"]
  }
}
```

**System prompt prefix for tool safety:**
```
"You are an advanced generation assistant. Do not assume missing parameters.
If a required parameter is absent, halt and ask the user for clarification before executing."
```

---

### 5.6 Advanced Troubleshooting Table

| Symptom | Root Cause | Fix |
|---|---|---|
| **Model ignores complex logical constraints** | Insufficient compute allocated before output | Prepend: *"Think step-by-step and outline your logical constraints before outputting."* |
| **Hallucinated data / outdated specs** | Relying on static weights, not live tools | Force grounding: *"Run a live web search, read the source, execute using exact numbers — do not estimate."* |
| **Output degrades over long session** | Context accumulation introduces irrelevant noise | Clear session or bundle all instructions into one clean system instruction markdown file before re-prompting |
| **Wrong tool selected / tool hallucination** | Tool descriptions too vague | Prune to precise exclusive use cases per tool; filter out unused tool definitions from API schema to save tokens |
| **Typography errors** | Text not isolated in prompt | Use pacing instruction: "word by word, one word at a time: '[TEXT]'" |
| **Iteration ruins previous output** | Rewriting full prompt instead of referencing prior | Use conversational modification — reference "the previous output" directly, describe only the delta |

---

### 5.7 Gemini Omni Key Capabilities at a Glance

| Capability | Notes |
|---|---|
| **Context window** | 1M+ tokens — stateless turn-by-turn, but massive per-turn memory |
| **Native tool execution** | Google Search, Code Interpreter, Workspace — no explicit trigger needed |
| **Multi-modal input** | Text, image, video, audio — all in one prompt |
| **World reasoning** | Fills structural gaps from world knowledge — do not over-specify |
| **Conversational editing** | Stateful iteration — reference prior output, describe delta only |
| **Function calling** | Custom JSON schema tool definitions — strict parameter requirements prevent hallucinated calls |
| **Extended thinking** | Allocatable on demand via "think step-by-step" prepend |

---

## 6. Nano Banana — Pro Photographer Reference Architecture

> Source: 5 notebooks (38+ sources). Nano Banana = Google Gemini 3 Pro Image (Pro) / Gemini 3.1 Flash Image (NB2).
> Framework: SCHEMA methodology + Prompt Like a Photographer discipline.

---

### 6.1 Nano Banana Family Taxonomy

| Model | Official Name | Release | Architecture | Resolution | Cost |
|---|---|---|---|---|---|
| Nano Banana (Legacy) | Gemini 2.5 Flash Image | Aug 2025 | Initial high-ELO benchmark | 1K–2K | High speed |
| **Nano Banana Pro** | Gemini 3 Pro Image | Nov 2025 | "Thinking" logic; perfect text; multi-turn | Up to 4K | $0.134/2K image |
| **Nano Banana 2** | Gemini 3.1 Flash Image | Feb 2026 | Real-time search grounding; 14 aspect ratios; char consistency | Native 4K | $0.067/2K image |

**NB2 Exclusive Features:** Real-time web/image search grounding · 14 aspect ratios (1:1 to 8:1) · Character consistency up to 5 chars (4 ref imgs) + 10 objects · 512px→4K resolution · Flash-tier speed.

---

### 6.2 SCHEMA Methodology — Structured 3-Tier Framework

Built on 850 verified API predictions across 4,800 images. Controls 5% → 95% precision.

| Tier | Control | AI Creativity | Time | Purpose |
|---|---|---|---|---|
| **BASE (Discovery)** | ~5% | ~95% | <1 min | Reveal model defaults/biases; diagnostic only |
| **MEDIO (Direction)** | ~85% | ~15% | ~5 min | Professional drafts; 7 core labels |
| **AVANZATO (Deliverable)** | 95–98% | ≤5% | >15 min | Final output; numeric specs; batch consistency |

#### 7 Core Labels (MEDIO level minimum)

| Label | Function | Key Specification |
|---|---|---|
| **Subject** | Unambiguous main element | Precise materials, dimensions, exact colors, state |
| **Style** | Global aesthetic reference | Photography type, quality, brand/editorial reference |
| **Lighting** | Total illumination environment | Setup, angle, Kelvin temperature (numeric at AVANZATO) |
| **Background** | Surrounding context | Spatial setting, materials, depth of field |
| **Composition** | Virtual camera direction | Shot type, angle, focal point |
| **Mandatory** | Critical elements (3–10 items) | Exclusively objectively verifiable technical items |
| **Prohibitions** | Explicit prevention (3–10 items) | Specific defects and artifacts to prevent |

**AVANZATO rule:** Replace all subjective adjectives with numeric specs — HEX codes for colors, Kelvin for temperature, f-stop for aperture, mm for focal length.

**Example AVANZATO (Interior Design):**
```
Subject: Modern living room, light oak flooring, white walls, warm grey sofa, coffee table.
Lighting: Natural soft daylight from large window, warm 3000K recessed lights, 70:30 ratio.
Mandatory: Verticals perfectly straight, realistic materials, no perspective distortion.
Prohibitions: NO converging verticals, NO oversaturated colors, NO fake HDR.
Output: 4:3, 4K, horizontal format.
```

---

### 6.3 Focal Length Reference Table

| Focal Length | Visual Effect | Use Case |
|---|---|---|
| **24mm** | Wide-angle, rectilinear distortion, expansive | Architecture, interiors, vast landscapes |
| **35mm** | Slight wide, incorporates context naturally | Environmental portraits, lifestyle advertising |
| **50mm** | "Nifty Fifty" — natural human perspective, minimal distortion | Conceptual, neutral portraits |
| **85mm** | Flatters face, compresses background | Classic portraiture, hero product shots |
| **135mm** | Extreme subject isolation, creamy circular bokeh | Emotional close-ups, telephoto |
| **f/1.4–f/2.8** | Shallow depth of field; separated background | Subject focus shots |
| **f/8–f/11** | Deep focus; everything sharp | Landscapes, flat lay, e-commerce |

> **EXIF Metadata Injection:** Pull EXIF data from a real target photo and inject brand/model/ISO into prompt → model navigates latent space toward that hardware's specific aesthetic.

---

### 6.4 Named Lighting Styles

| Style | Description | Best For |
|---|---|---|
| **Rembrandt** | Key light 45° above + side; triangle on shadowed cheek | Dramatic portraits, executive headshots |
| **Chiaroscuro** | Extreme contrast; subject emerges from near-total shadow (Caravaggio) | Fine art noir, theatrical editorial |
| **Volumetric / God Rays** | Light made visible through fog/smoke/dust | Forest, interior shafts, mystical scenes |
| **Butterfly / Paramount** | Key directly above/in front; butterfly shadow under nose | Beauty campaigns, fashion, cosmetics |
| **Split Lighting** | Face exactly half lit / half shadow | Editorial fashion, music covers, drama |
| **Rim / Backlight** | Behind subject; glowing edge outline | Product shots, action/sci-fi |
| **Golden Hour Backlight** | Warm low-angle sun behind subject; halo + long shadows | Lifestyle, travel, romantic |
| **Practical Lighting** | In-scene sources: lamps, candles, neon, screens | Cyberpunk, documentary, street |
| **High-Key** | Bright, even, near-shadowless | Commercial product, beauty, lifestyle |
| **Low-Key** | Predominantly dark, single dominant source | Noir, thriller, horror editorial |

---

### 6.5 Film Stock Simulation (Kill the "AI Sheen")

| Film Stock | Visual Profile | Use |
|---|---|---|
| **Kodak Portra 400** | Warm tones, rich highlights, natural skin | Editorial, lifestyle, portraiture |
| **Fujifilm Superia 400** | Green/cyan shadow shifts | Street, urban photography |
| **Cinestill 800T** | Red halation, cool tungsten balance | Cinematic night shots |
| **Ilford HP5** | High-contrast B&W, coarse grain | Authentic monochrome |

**ISO 100** → forces noiseless, high-resolution studio look.

---

### 6.6 Nano Banana Pro Tips

| Tip | Method |
|---|---|
| **Thinking Mode** | Toggle ON in AI Studio for complex layouts — plans before rendering |
| **Text-First Hack** | Converse to generate exact text concepts → then ask for image containing that text (95% typographic accuracy) |
| **Text Distance Rule** | Specify: exact words → font style → placement relative to anchor elements |
| **Search Grounding (NB2)** | Ask for fact-based infographics — model pulls live Google data before generating |
| **Semantic Masking** | "Remove the car in the background" — no manual mask needed |
| **Multi-Turn Refinement** | Generate → refine in follow-up messages; do NOT rewrite full prompt |
| **Character Consistency** | Upload up to 14 refs (4 character + 10 object); use identical descriptors across all prompts |
| **Google Flow — Zero Credits** | Batch generate up to 4 at a time with zero credits — best-kept Nano Banana secret |
| **512px tier** | Use for fast composition tests before spending on 4K render |

---

## 7. Seedance 2.0 — Advanced Platform Framework

> Source: Seedance 2.0 technical analysis + ByteDance Dual-Branch Diffusion Transformer architecture.

---

### 7.1 Architecture

**Dual-Branch Diffusion Transformer:**
- **Visual Branch:** Processes spatiotemporal tokens (pixel movement over time)
- **Audio Branch:** Processes waveform tokens (spectral features)
- **Attention Bridge:** Millisecond-level metadata passing between branches → perfect lip-sync and native audio

Result: Simultaneous video + audio generation (not layered in post).

---

### 7.2 CRAFT Framework — Complex Multi-Reference Projects

| Element | Function |
|---|---|
| **C**ontext | Explicit narrative stage + environmental parameters |
| **R**eference (@assets) | Up to 12 multimodal tags embedded to lock identity, motion, audio |
| **A**ction | Kinetic events and interactions |
| **F**raming/Timing | "Lens switch" keyword; exact temporal duration markers (e.g., Dutch angle at 3s) |
| **T**one/Audio | Explicit audio direction matching visual tension |

> Keep style intensity at **moderate** — pushing to maximum overwhelms reference constraints, causing visual DNA drift.

---

### 7.3 Timeline Prompting

Breaks the 15-second generation into rigid temporal segments:

```
0–4s: Wide shot, @Image1 walks through neon rain.
4–9s: Lens switch to extreme close-up on @Image1's face as lightning strikes.
9–15s: Pan right rapidly as @Image1 draws a weapon.
```

The `lens switch` keyword executes hard cinematic cuts without NLE — identity preserved throughout via locked Ref2V anchors.

---

### 7.4 Start Frame Manipulation (Advanced Correction)

When generation fails at a specific point (e.g., character distorts at 10s):
1. Screenshot last flawless frame
2. Import to Nano Banana Pro — inpaint / color correct
3. Re-inject as new `@Image` reference + explicit Start Frame in Seedance

Allows indefinite scene extension without accumulated degradation.

---

### 7.5 Seedance Filter Avoidance

Seedance filters operate on **English keyword pattern matching** (not semantic understanding):

| Replace | With |
|---|---|
| `attack, fight, punch, kick` | `impact, force, momentum, collision` |
| `shoot, fire, weapon` | `muzzle flash, tactical equipment, metallic object` |
| `blood, wound` | `crimson liquid, surface damage, aftermath` |
| `young boy, child, kid` | Role-based: `rider`, `figure`, `small figure in dark coat` |

**Cinematic Shield:** Heavy technical vocabulary (anamorphic lens, tracking shot, aspect ratio) signals creative production context → filter grants more latitude for intense scenes.

---

### 7.6 Platform Access Guide

| Platform | Model Hosted | Key Feature |
|---|---|---|
| **Higgsfield** | Seedance 2.0 | Cinema Studio, Director Panel, Start/End Frames, DoP style presets |
| **CloneViral** | Kling 3.0, Seedance 2.0, Nano Banana 2 | Cinematic Storyboard Generator, Miles Agent, Loop Mode |
| **ImagineArt** | Seedance 2.0 | Frame-level precision (first + last frame), single-login pipeline |
| **Google AI Studio** | Nano Banana Pro/2 | 14 aspect ratios, Thinking Mode, resolution 512px→4K, batch generation |
| **Google Flow** | Nano Banana 2, Veo 3.1 | Zero credits for image gen; AI filmmaking pipeline; Ingredients to Video |
| **RenderZero / BYOK** | Nano Banana Pro | Buy-once desktop app; your API key; JSON export; no monthly subscription |

---

## 8. Source Example Prompt Library

> Copy-pasteable reference prompts from verified production sources.

---

### 8.1 Cinematic Realism (Veo 3.1)

**Drone Landscape:**
```
Sweeping drone shot of a lone hiker crossing a fog-covered mountain ridge at dawn,
cinematic realism, shallow depth of field.
Audio: wind, footsteps, ambient birdsong.
```

**Moving Drone — Canyon Reveal:**
```
Moving drone shot starting low on a lone hiker walking what seems a simple trail,
rising high to reveal a gorgeous, lush canyon at sunrise with mist in the air.
SFX: soft wind and distant hawks. Ambience: sparse pulsing ambient background music.
```

**Night Street — Character Drama:**
```
Medium shot of a young woman with auburn hair walking through a neon-lit Tokyo street at night.
She pulls her coat tighter, expression contemplative as she navigates the bustling crowds.
Rain reflects neon signs on wet pavement. Camera slowly tracks behind her.
Cool blue and pink neon lighting, volumetric light rays.
SFX: footsteps on wet pavement, distant traffic, ambient city hum.
Cinematic, moody, Japanese cyberpunk aesthetic. 1080p, 6 seconds, 16:9, no subtitles.
```

---

### 8.2 Dialogue / Interview (Veo 3.1)

**Corporate Interview:**
```
Locked-off medium camera shot of a robotics engineer in a sunlit lab, shallow depth of field,
gentle rack focus to a robotic arm.
Dialogue: 'We made it smaller and faster this quarter. The gains we'll get from this change are immense.'
Ambience: upbeat background music.
```

**Detective Noir (Ingredients workflow):**
```
Using the provided images for the detective, the woman, and the office setting,
create a shot focusing on the woman. A slight, mysterious smile plays on her lips as she replies:
You were highly recommended. (no subtitles)
```

---

### 8.3 Product Hero (Veo 3.1)

**Luxury Watch:**
```
A luxury smartwatch sits on a rotating pedestal inside a dark studio.
Studio lights highlight its polished metal surface. The camera orbits smoothly 360 degrees.
Soft mechanical sounds. Modern minimal aesthetic, shallow depth of field.
```

**Rolex Reveal (JSON-driven):**
```json
{
  "product_name": "Rolex Skycraft",
  "description": "A high-end Rolex watch emerges from swirling golden mist, assembling piece by piece mid-air with precision and elegance.",
  "style": "cinematic, ultra slow motion, glossy, surreal, hyper-realistic",
  "camera": "close orbit with occasional macro detail inserts",
  "lighting": "soft studio key light with golden mist glow",
  "audio": "soft mechanical assembly tones, no music",
  "text": "none"
}
```

---

### 8.4 Nano Banana — Portrait & Product

**Candid Street Portrait:**
```
Photorealistic candid street portrait of a 28-year-old man, relaxed expression,
natural skin texture, subtle imperfections, standing on a quiet city sidewalk near a corner café.
Golden hour sunlight from camera-left with soft rim light on hair.
Full-frame camera, 85mm lens, f/1.8, shallow depth of field, creamy background bokeh.
Documentary street photography vibe, realistic color, slight film grain.
Composition: rule of thirds, eye-level, medium close-up. Aspect ratio 4:5.
```

**E-Commerce Product:**
```
Studio product photo of a matte black water bottle on a seamless backdrop.
Three-point lighting: large softbox key light top-left, subtle fill from front, rim light back-right.
Clean reflections, realistic materials. Shot on 70mm lens, f/8 for full product sharpness.
Composition: centered hero shot with slight angle, premium ecommerce style.
Background: very light warm gray. Aspect ratio 1:1.
```

**Surreal Thinking-Mode:**
```
A crystalline chess set where pieces are made of freezing water and the board of burning lava.
Pieces melting slightly where they touch the board.
Macro photography, hyper-realistic.
Reason through the lighting interactions between fire and ice before generating.
```

---

### 8.5 Seedance 2.0 — Multi-Shot Sports

```
Shot 1: @Image1 as first frame, tracking shot backwards as subject dribbles ball.
Shot 2: Low angle wide, whip pan as subject changes direction.
Shot 3: Close-up, rack focus from face to background.
Shot 4: Lens switch to close-up, rack focus goalkeeper behind.
Shot 5: Dolly in following ball into net.
Audio: boots on grass, crack of ball, crowd swell, heartbeat, eruption.
- No music, No logo, no text on screen. 4K Ultra HD, stable picture.
```

---

### 8.6 Nano Banana — AVANZATO Info Design

```
Style: Professional architectural interior photography, high-end magazine quality.
Composition: Wide-angle frontal view, eye level, 16–24mm equivalent focal length.
Subject: Modern living room, light oak flooring, white walls, warm grey sofa.
Lighting: Natural soft daylight, warm 3000K recessed lights, 70:30 ratio.
Mandatory: Verticals perfectly straight, realistic materials.
Prohibitions: NO converging verticals, NO fake HDR, NO unrealistic furniture.
```

---

---

## 9. Spatial Awareness in AI Video — Failures & Fixes

> Source: 3 notebooks × 49+21+49 sources. May 2026 production data.
> Most-broken area in AI video. Architecture improved but fundamental limits remain.

---

### 9.1 Why Spatial Awareness Breaks

**Root cause:** Models prioritise **visual drama over physical accuracy**. When spatial correctness conflicts with smooth-looking output, the model chooses smooth. Every time.

**Veo 3.1 architecture note:** Uses 3D latent diffusion — treats time as third spatial dimension. 35% improvement in motion prediction accuracy over Veo 3. Still not enough for complex scenarios.

**Seedance 2.0 architecture note:** Visual Branch processes spatiotemporal tokens (3D mathematical patches of pixel movement). Better at camera motion and photorealism than raw physics simulation.

**JSON schema note:** Natural language prompts → 34% first-try spatial success. JSON → 78%. Structured fields remove the ambiguity that causes "mushy" transitions.

---

### 9.2 The 8 Failure Types

| # | Failure | What You See | Root Cause |
|---|---|---|---|
| 1 | **Depth / Parallax Error** | Objects at all depths move at identical speed — cardboard cutout effect | Model doesn't calculate per-depth motion rates |
| 2 | **Object Collision Confusion** | Items merge, lose boundaries during proximity; hands pass through objects | Physics collision engine fails under multiple interacting elements |
| 3 | **Foreground-Background Instability** | Background textures crawl, buildings shift shape, trees sway inconsistently | Model allocates attention to foreground; background processing degrades |
| 4 | **Camera Perspective Drift** | "Floaty" motion, impossible camera angles, warped backgrounds | No explicit camera anchor — model guesses position each frame |
| 5 | **Scale Inconsistency** | Subject drifts in size relative to environment, especially during camera moves | Without reference images, proportion is recalculated per frame |
| 6 | **The Physics Wall** | Multi-character tackles, glass shattering, fluid dynamics → melting artifacts, hallucinations | Chaotic physical interactions exceed model's spatial reasoning capacity |
| 7 | **Identity Drift** | Face, clothing, geometry morphs as camera angle changes | Character not mathematically anchored to reference |
| 8 | **Fine Motor Control** | Fingers stretch, hands melt, anatomy incorrect in close-ups | Remains broken across ALL models (May 2026) — no prompting fix |

---

### 9.3 The Physics Wall — Cannot Prompt Around

These scenarios **reliably cause spatial collapse** in all current models. Plan your shots to avoid:

- Multi-character physical contact (tackles, wrestling, crowd collisions)
- Glass shattering with physical accuracy
- Complex fluid dynamics — water splashing, liquid pouring realistically
- Fabric + wind interaction on multiple simultaneous surfaces
- Object counts exceeding **15 identical items** (model duplicates / merges)
- More than **2–3 characters** in complex spatial interaction

> *Workaround:* Shoot these as separate clips, cut in editing. Don't attempt in single generation.

---

### 9.4 Fix System — Prompting Solutions

#### Camera Anchoring (Most Impactful Fix)

```
✅ "Camera held at chest height (thats where the camera is) tracking the subject"
✅ "Close-up with camera at counter level (thats where the camera is) as chef demonstrates"
❌ "Close-up shot of the chef cooking"
```

**Always append** `(thats where the camera is)` after any position/height descriptor. Triggers camera-aware processing. Single highest-impact spatial fix available.

**Locking the camera entirely:**
```
"locked tripod, zero camera shake"       ← standard lock
"static tripod timelapse"                ← for locked timelapses  
"locked-off camera, no movement"         ← absolute lock
```

#### Lens-Driven Depth Control

| Lens | Spatial Effect | Use |
|---|---|---|
| **16mm** | Expands perceived space, slight distortion | Wide environments, architecture |
| **35mm** | Natural perspective, standard depth | Dialogue, lifestyle |
| **85mm** | Compresses background, isolates subject | Intimacy, product shots |
| **135mm+** | Extreme subject isolation, flat background | Portraits, telephoto |

> Lenses control depth, not distance. Use 85mm to solve foreground-background confusion — background is mathematically compressed away.

#### Object Count Precision

```
✅ "Only six lanterns float across the misty lake"
✅ "Exactly three coffee cups arranged in a triangle"
❌ "Several cups on a table"
❌ "A few lanterns floating"
```

Rule: `only` / `exactly` before any count. Front-load count specification. If count >5, reduce and focus on composition quality instead.

#### Spatial Relationship Language

Always specify **explicit 3D relationships** — model cannot infer them:

```
"subject positioned left frame, foreground"
"exactly 30 feet between the detective and the mark"
"foreground: woman at desk. midground: window. background: blurred city lights"
"camera left: key light. camera right: deep shadow. no fill"
```

#### Spatial Negative Prompts — Standard Pack

Append to every generation involving characters or complex scenes:

```
Negative: no motion blur, no face distortion, no warping, no morphing,
no duplicate limbs, no inconsistent lighting, no background shifting,
no floating objects, no fisheye distortion, no plastic skin
```

#### One Camera Movement Rule

```
✅ "slow dolly-in as she reads the letter — intimacy building"
✅ "smooth tracking shot at shoulder height, constant speed"
❌ "fast whip pan and slow motion drone pullback simultaneously"
```

Conflicting motion instructions = temporal drift + spatial collapse. ONE movement per clip.

---

### 9.5 Composition-First Workflow (Spatial Guarantee)

Traditional workflow leaves composition to chance. This workflow eliminates that:

```
Step 1: Generate exact frame composition in Nano Banana 2
         → Rule-of-thirds, aspect ratio, spatial relationships all locked
Step 2: Reframe if needed via conversational edit
         → "Move subject to left third", "Pull back to wide shot"
Step 3: Send to I2V (Veo 3.1 or Seedance)
         → Model animates your pre-defined composition
```

> You are not prompting and hoping. You are directing.

**Nano Banana 2 reframing use cases:**

| From | To | Why |
|---|---|---|
| 1:1 character portrait | 16:9 wide | Reveal environment for establishing shot |
| Tight close-up | Wide shot | Pull back to show spatial context before animating |
| Centered composition | Rule-of-thirds | Fix static framing before sending to I2V |
| 16:9 | 4:1 panoramic | Epic scope for title sequences |

---

### 9.6 Reference Anchoring — Spatial Identity Lock

#### Veo 3.1 — Ingredients to Video (3 Pillars)

| Pillar | Spatial Function |
|---|---|
| **Subject/Character image** | Locks identity — prevents morphing across camera angles |
| **Environment/Setting image** | Keeps background stable — prevents background crawl |
| **Style/Texture image** | Maintains visual DNA — prevents lighting/colour drift |

Use all three pillars for maximum spatial stability. Environment image alone eliminates most background instability issues.

#### Seedance 2.0 — @ Mention Mathematical Constraint

```
"A medium tracking shot of @Image1 wearing the jacket from @Image2
walking through a rain-slicked cyberpunk alley."
```

@ Mention tags **mathematically constrain the diffusion process** — model cannot alter subject's core geometry across varying camera angles. Asset limits: 9 images / 3 videos / 3 audio.

#### Start Frame Manipulation (Spatial Repair Mid-Generation)

When a scene fails spatially at a specific point (e.g., anatomy distorts at 10s):

```
1. Screenshot last flawless frame
2. Import into Nano Banana — inpaint / color correct
3. Re-inject as new @Image reference + explicit Start Frame
4. Generate continuation from corrected anchor
```

Allows indefinite extension without accumulated spatial degradation.

---

### 9.7 First / Last Frame — Trajectory Control

Define spatial START and END points; model interpolates the motion path:

```
Start Frame: front-facing view of subject at desk
End Frame:   same subject at window, seen from behind
Result:      180-degree arc shot with correct parallax and perspective throughout
```

Use for:
- Character spatial transformations (sitting → standing → walking)
- Product reveals (close-up → wide lifestyle)
- Seamless loops (first frame = last frame)
- Camera arcs that would otherwise drift

---

### 9.8 Unstable Material Banning

When **texture crawl** appears (fabric weave "swims", patterns shift frame-to-frame), remove these from prompts:

```
❌ sequins, mesh, herringbone, micro-pattern, moire-prone fabrics,
   highly reflective surfaces, heavy embroidery, chainmail in motion
```

Replace with stable surface descriptions:
```
✅ "matte fabric", "plain cotton", "smooth leather", "solid colour clothing"
```

---

### 9.9 Persistent Limitations — Cannot Fix (May 2026)

| Issue | All Models | Best Workaround |
|---|---|---|
| **Hand / finger articulation** | ❌ Broken | Frame shots to minimise hand visibility; avoid close-ups |
| **Complex fluid dynamics** | ❌ Visual smoothness > physics accuracy | Shoot water/fire as separate hero clip, composite |
| **Glass shattering realistically** | ❌ Physics Wall | Use practical effect reference image as Ingredient |
| **Multi-character tackles / crowd** | ❌ Physics Wall | Cut to reaction shots; avoid contact in single generation |
| **Object counts >15 identical** | ❌ Duplicates / merges | Reduce count; use "only X" constraint |
| **>2–3 characters spatially interacting** | ❌ Identity breakdown | Split into separate clips per character |
| **Rapid camera movements** | ⚠️ Motion blur | Use slow/smooth camera only; add speed in edit |
| **Text in scene** | ❌ Garbled / inconsistent | Add all text in post-production |

---

### 9.10 Pre-Generation Spatial Checklist

Before every generation:

- [ ] Camera position includes `(thats where the camera is)`
- [ ] ONE primary camera movement specified
- [ ] Lens type specified (16mm / 35mm / 85mm)
- [ ] Subject has ≥15 attributes (identity lock)
- [ ] Scene has ≥10 environmental elements
- [ ] Spatial relationships explicit: foreground / midground / background
- [ ] Object counts use `only` / `exactly`
- [ ] Reference images uploaded (Ingredients / @Image)
- [ ] Spatial negative prompts appended
- [ ] No conflicting motion directives
- [ ] Unstable materials removed from description
- [ ] Physics Wall scenario avoided (or split into separate clips)

---

---

## Section 10: New Omni Prompting — The Paradigm Shift

> Omni models don't carve images out of static noise. They **reason through** the logic and spatial physics of a scene using world knowledge. Stop treating them like diffusion models.

---

### 10.1 What Changed — Autoregressive vs Diffusion

| Dimension | Legacy Diffusion Models | Omni Autoregressive Models |
|---|---|---|
| **Architecture** | Denoising from static noise | Autoregressive "thinking" — token-by-token world reasoning |
| **Prompt style** | Keyword spamming / tag soup | Descriptive narrative sentences |
| **Object knowledge** | Pattern-matched shapes | Understands what objects ARE and their relationships |
| **Editing** | Full regeneration or manual masking | Conversational delta-only edits in natural language |
| **Physics** | Visually plausible statistics | Reasons through physical constraints before generating |
| **Error recovery** | Regenerate entirely | "Remove the boom mic from frame 3" and done |
| **Context length** | ~500 tokens optimal | Up to 10,000 chars; performs best with clear scenarios |

**Nano Banana family = Omni models:**
- Nano Banana (Legacy) = Gemini 2.5 Flash Image
- Nano Banana Pro = Gemini 3 Pro Image
- Nano Banana 2 = Gemini 3.1 Flash Image

---

### 10.2 World Reasoning vs Keyword Stuffing

Omni models prioritize **World Reasoning** — abstract concept understanding, object relationships, physical logic.

**The Pelican Test:** Prompt `"pelican riding a bicycle, ensure absolute realism"` → model enters **thinking mode** → realizes pelican's legs must actually reach pedals → generates longer legs. A diffusion model just matches visual statistics.

**What this means for prompting:**

❌ **Legacy keyword stuffing:**
```
dog, park, 4K, realistic, cinematic, volumetric lighting, ultra-detailed, 
sharp focus, trending artstation, 8k, professional
```

✅ **Omni world reasoning:**
```
A golden retriever sits on sun-warmed grass in a city park on a late 
afternoon in September. Dappled light filters through maple trees just 
beginning to turn amber. A few joggers pass in the soft-focus background.
```

**Key principle:** Act like a Creative Director giving a brief. The model understands intent. Explain the scene — don't enumerate its technical properties.

**Prompt length reality check:**
- Handles up to 10,000 characters
- Performs better when you "loosen the reins"
- Clear descriptive scenario > wall of technical jargon
- Brevity with specificity > verbose keyword lists

---

### 10.3 Positive Exclusion — Absolute Scene State

This is the core paradigm shift in Omni prompting. Naming a defect to exclude it can **summon it** by focusing model attention on that concept.

**The Principle:** Don't tell the model what should be ABSENT. Describe the ABSOLUTE STATE of what IS there.

| Legacy Negative | Omni Positive Exclusion |
|---|---|
| `"no man-made structures"` | `"A barren landscape stretching endlessly, untouched by roads or buildings, only raw earth and horizon"` |
| `"no extra fingers"` | `"Anatomically plausible hands with five distinct fingers, natural proportions"` |
| `"no cars, no vehicles"` | `"A cobblestone market square filled only with pedestrians in period clothing"` |
| `"no text on screen"` | `"A pristine scene with no overlays, cards, or typography visible"` |
| `"no humans in frame"` | `"An empty kitchen — bare marble countertops, no occupants, absolute stillness"` |
| `"don't show anything modern"` | `"Every visible element belongs to 1920s Paris — wrought iron, gas lamps, cobblestones"` |

**User's example (from session):**
```
✅ Omni style: "A pristine, completely empty minimalist modern kitchen. 
The marble countertops are entirely bare and spotless. No human presence."
```
Describe absolute completeness of the state. The model reads the scene holistically.

**Declarative negatives for lists** (when you must exclude):
```
✅ "cars, vehicles, traffic"         (declarative list — model processes as category)
❌ "don't show any cars"             (instructive negative — focuses attention on cars)
```

---

### 10.4 Conversational Editing — Delta Only

One of the defining features of the Omni era: **describe only the change**, not the entire scene.

**How it works:**
- Model retains context of existing image/video
- LLM component understands what objects ARE
- Edits specific elements while preserving everything else
- Non-destructive — original seed preserved

**Natural language edit commands:**
```
"Move the man holding the umbrella to the left side of frame"
"Change the woman's dress from blue to emerald green"
"Remove the bar tap — this scene is set in the 1800s"
"Remove the boom mic from the top of frame 3"
"The man in the green tuxedo — make it actually green"
"Remove the third arm from the figure on the left"
```

**EDIT: prefix syntax** (explicit delta notation):
```
EDIT: Remove the car from the background
EDIT: Change the tie color from blue to red
EDIT: Add morning fog to the street
```

**What Omni can remove:**
- Production equipment (boom mics, camera rigs)
- Anachronistic elements (modern objects in period scenes)
- Anatomical errors (extra limbs, extra fingers)
- Unwanted background characters
- Complex occlusions from specific locations

**Conversational director mode:**
```
"Remove the bar tap from keyframe 2"
"Remove the hat in keyframes 3, 7, 9, and 11"
```
Model processes each note independently, preserves rest of scene.

---

### 10.5 The 5-Dimension JSON Framework

Omni professional workflow uses **structured JSON** to organize instructions into clear category buckets. Provides same 78% first-try consistency improvement as elsewhere.

```json
{
  "scene": {
    "setting": "1972 New York, Lower East Side at dusk",
    "era": "early 1970s — no modern elements visible",
    "atmosphere": "humid summer evening, golden-hour light fading"
  },
  "subject": {
    "character": "woman in her 30s",
    "appearance": "dark hair in loose bun, pinstripe shirt, wide-leg trousers",
    "consistency_markers": ["small scar above left eyebrow", "silver ring on index finger"]
  },
  "action": {
    "motion": "walks slowly toward camera, pauses at newsstand",
    "timing": "confident pace, no urgency"
  },
  "camera": {
    "hardware": "Arri Alexa 35",
    "lens": "35mm Cooke S4",
    "movement": "slow dolly-in from street level (thats where the camera is)",
    "aspect": "2.39:1 anamorphic"
  },
  "lighting": {
    "type": "practical neon signs + warm tungsten spill",
    "color_temperature": "mixed warm #F5A623 and cool #4A90D9",
    "quality": "dramatic amber backlight, soft fill from storefront"
  }
}
```

**5 primary dimension buckets:**
1. **Scene/Setting** — era, environment, atmosphere
2. **Subject/Character** — physical attributes, consistency markers
3. **Action/Motion** — granular timing, behavioral cues
4. **Camera/Lens** — hardware callouts, movement, aspect ratio
5. **Lighting/Atmosphere** — specific type, hex color, quality

---

### 10.6 Sonic Landscaping — Audio-Driven Visual Accuracy

Describing sound forces Omni models to generate visually accurate physics for that sound's source.

**The principle:** Model derives visual physics from acoustic signature.

```
"A crystal wine glass shatters on a marble floor"
→ Forces accurate shard geometry, impact point, scatter pattern

"Rain hammers corrugated iron roofing"  
→ Forces correct water behaviour, pooling, bounce droplets

"A heavy oak door closes in an empty stone cathedral"
→ Forces acoustic space — vaulted ceiling, stone walls, correct reverb space visible
```

**Sonic Landscaping table:**

| Sound Description | Visual Physics Forced |
|---|---|
| `"crystal glass shatters on marble"` | Accurate shard geometry, scatter radius |
| `"wet boots on wooden floorboards"` | Moisture sheen, grain texture, flex |
| `"crowd noise from packed arena"` | Density, lighting, fog-of-breath atmosphere |
| `"single gunshot in open desert"` | Scale, horizon, dust displacement |
| `"espresso machine steaming milk"` | Steam dynamics, cup proximity, counter moisture |

Include ambient sound description even for silent shots — model uses it to calibrate physical space.

---

### 10.7 Moments in Progress — Not Story Arcs

Omni models perform best on **continuous moments**, not complete narratives with clear starts and ends.

**Why:** Complete story arcs with narrative closure trigger model to resolve toward an "ending state" — causes jarring mid-clip resets as model resolves story beats.

❌ **Story arc (avoid):**
```
"A woman walks to her car, opens the door, gets in, drives away"
→ Model tries to complete all beats → abrupt transitions → inconsistent physics
```

✅ **Moment in progress:**
```
"A woman mid-stride on a wet city sidewalk, coat lapels catching the wind, 
purposeful movement — somewhere to be, not yet arrived"
→ Model sustains continuous motion state
```

**Framing techniques for moments:**
- Use present participle: "walking," "turning," "reaching" — not "walked to," "turned and"
- Imply destination without showing arrival
- Describe emotional state as ongoing: "weighing a decision" not "made a decision"
- For loops: describe cyclical action — "waves continue to break"

---

### 10.8 Advanced Omni Techniques

#### Contact Sheet Hack — Character Consistency
For perfect character consistency across shots: combine multiple reference angles into **one contact sheet image** rather than uploading individual files.

```
✅ One image: 3x3 grid of character — front, 3/4, profile, back, close-up, full-body
❌ Multiple uploads: floods context window, model loses weighting between refs
```

Official documentation method:
```
"Create a new image by combining elements from the provided images. 
Take the element from Image 1 and place it with element from Image 2. 
Final image: [describe complete scene]"
```
Real-world best method: contact sheet as single reference image.

#### New Chat Solve — Token Quantization Noise
Autoregressive models accumulate **token quantization noise** across long conversation threads → "digital dust," artifacts, image quality degradation.

**Fix:** Open a new chat thread. Refreshes model's latent memory. Restores image clarity immediately.

Symptom: Generation quality degrading after many edits in same thread → new chat, not prompt adjustment.

#### Visual Prompting — Write on Images
Draw or annotate directly on input images:

- **Red arrow** → indicates where character should move
- **Drawn box** → defines where specific element should appear
- **Scribbled text on image** → V3 animates annotations out in opening seconds
- **Circle around element** → targets that element for edit

```
Prompt: "Make the text annotations vanish in the opening seconds"
→ V3 processes scribbled instructions, fades them as video begins
```

#### 180-Degree Camera Rotation (Nano Banana Pro)
Legacy models "paper-doll flipped" characters on reverse angles. Nano Banana Pro maintains correct spatial relationships:

- Character on LEFT in source → character on RIGHT in reverse shot
- Spatial relationships preserved across full camera rotation

**Trigger syntax for rotation:**
```
❌ "Please rotate the camera to show what's behind the current view"
✅ "Please rotate the camera to show the other side of the lab"
✅ "Rotate camera to show the view from behind — elevator doors visible"
```
Model needs an **object target** to aim the rotation at. Spatial destination, not directional instruction.

#### Negative Space as Narrative Tool
Use outpainting to break rule-of-thirds intentionally for storytelling:

```
Rule-of-thirds rigid → every model defaults to this
Outpaint → extend frame to add empty space around character
Purpose: isolation, paranoia, tension (Mr. Robot technique)
```

Apply as seasoning — always for narrative purpose, not default.

---

### 10.9 Omni Prompt Templates

#### Absolute Scene State Template
```
[Location description, completely described as it IS]
[Subject description — physical state, no action yet]  
[Action as ongoing moment]
[Camera — hardware, lens, position (thats where the camera is)]
[Lighting — type, quality, color temperature]
[Atmosphere — sound, air quality, time of day]
[Absolute completeness — what fills every part of frame]
```

#### Conversational Edit Template
```
Reference: [describe prior output or attach image]
EDIT: [single specific change in plain language]
Preserve: [what must remain identical]
```

#### Sonic Landscaping Template
```
[Visual scene description]
Sound: [specific acoustic event that anchors visual physics]
[How sound source integrates with visual environment]
```

#### Production Example — Omni Style
```json
{
  "scene": {
    "setting": "Pristine, completely empty minimalist modern kitchen, midday",
    "state": "Marble countertops entirely bare and spotless. No occupants. 
              Absolute stillness. Every surface immaculate.",
    "light": "Natural light through floor-to-ceiling windows, 
              crisp white surfaces, no shadows"
  },
  "atmosphere": "Silence so complete you could hear a pin drop. 
                 Air faintly cool. The kitchen has never been cooked in.",
  "camera": {
    "lens": "35mm",
    "position": "counter height (thats where the camera is)",
    "movement": "locked, zero motion"
  }
}
```

---

### 10.10 Omni vs Legacy — Quick Reference

| Scenario | Legacy Approach | Omni Approach |
|---|---|---|
| Empty scene | `"no people, no clutter"` | Describe complete stillness and bareness |
| Fix anatomy | `"no extra fingers, correct hands"` | `"anatomically accurate hands, five distinct fingers"` |
| Period accuracy | `"no modern elements"` | Describe every visible element as belonging to the era |
| Edit one element | Regenerate or mask in editor | `"EDIT: Change X to Y"` in chat |
| Character consistency | Upload 3 separate reference images | Single contact sheet with all angles |
| Camera angle change | New generation with new camera prompt | `"Rotate camera to show other side of [landmark]"` |
| Quality degrading | Adjust negative prompts | Open new chat thread |
| Complex physics | Multiple keywords | Describe the SOUND that produces that physics |
| Story vs moment | Full arc with start/end | Describe ongoing state — mid-action, not resolved |

---

### 10.11 Omni Pre-Generation Checklist

- [ ] Prompt describes absolute scene STATE — not what to exclude
- [ ] Narrative sentences used — not comma-separated keyword lists
- [ ] Action described as ongoing moment — not story arc with resolution
- [ ] Contact sheet uploaded for character consistency (if multi-angle)
- [ ] Sonic landscaping included for physics-heavy scenes
- [ ] JSON structure used for complex multi-element scenes
- [ ] Camera rotation uses object target — not directional instruction
- [ ] Working in fresh chat thread (if prior generations degrading)
- [ ] Edit requests use natural language delta — reference specific element
- [ ] Negative space / rule-of-thirds break applied for narrative purpose only

---

*v1.4 — Updated 2026-05-25. Sources: 8 NotebookLM notebooks, 130+ production sources. Sections 1–10.*

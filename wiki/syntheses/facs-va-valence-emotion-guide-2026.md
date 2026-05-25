---
title: FACS VA Valence — Facial Expression & Emotion Guide 2026
date: 2026-05-25
tags: [facs, facial-action-coding, emotion-ai, animation, micro-expressions, valence-arousal, wiki]
summary: Synthesised guide from FACS VA Valence Micro and Normal Face Cues NotebookLM — 82 sources, AU mappings + AI pipeline applications
source_notebook: https://notebooklm.google.com/notebook/69ec4dd0-ba20-49df-88e2-e7dd977c1b53
---

# FACS VA Valence — Facial Expression & Emotion Guide 2026

> Synthesised from NotebookLM: *FACS VA Valence Micro and Normal Face Cues* (82 sources)

---

## Core Framework

**FACS + VA Model + Micro-Expression Detection** = objective, anatomically-grounded, AI-compatible standard for measuring and replicating human affect.

---

## I. Facial Action Coding System (FACS)

### What It Is
- Developed by Paul Ekman & Wallace Friesen (1978, updated 2002)
- Decomposes facial expressions into **Action Units (AUs)** — each representing contraction of a specific muscle or muscle group
- **Describes movement, not meaning** — eliminates observer bias
- 44 distinct AUs; over **7,000 distinct AU combinations** observed in human facial behaviour

### Intensity Scoring (5-Point Scale)
| Score | Label | Meaning |
|---|---|---|
| A | Trace | Weakest discernible movement |
| B | Slight | Subtle |
| C | Marked | Clear |
| D | Extreme | Strong |
| E | Maximum | Maximal intensity |

### Temporal Dynamics
Coding captures **onset → apex → offset** of each AU from video. Critical for distinguishing:
- Spontaneous behaviour vs. posed reactions
- Genuine expressions vs. fabricated ones (e.g., Duchenne smile requires AU 6, which is hard to fake voluntarily)

### Primary Action Units Reference Table
| AU | Muscle | Appearance Change |
|---|---|---|
| AU 1 | Frontalis, pars medialis | Inner brow raiser |
| AU 2 | Frontalis, pars lateralis | Outer brow raiser |
| AU 4 | Corrugator supercilii | Brow lowerer |
| AU 5 | Levator palpebrae superioris | Upper eyelid raiser |
| AU 6 | Orbicularis oculi, pars orbitalis | **Cheek raiser** (genuine smile indicator) |
| AU 7 | Orbicularis oculi, pars palpebralis | Lid tightener |
| AU 9 | Levator labii superioris alaeque nasi | Nose wrinkler |
| AU 12 | Zygomaticus major | Lip corner puller |
| AU 14 | Buccinator | Dimpler |
| AU 15 | Depressor anguli oris | Lip corner depressor |
| AU 17 | Mentalis | Chin raiser |
| AU 20 | Risorius/Platysma | Lip stretcher (grimace) |
| AU 23 | Orbicularis oris | Lip tightener |
| AU 26 | Masseter relaxation | Jaw drop |

---

## II. Universal Emotion AU Combinations

| Emotion | Action Units | Key Notes |
|---|---|---|
| **Happiness** | 6 + 12 | AU 6 (cheek raiser) distinguishes genuine from social smile |
| **Sadness** | 1 + 4 + 15 | Inner brow raises while corners depress |
| **Surprise** | 1 + 2 + 5 + 26 | Full brow raise + wide eyes + jaw drop |
| **Fear** | 1 + 2 + 4 + 5 + 7 + 20 + 26 | Most complex combination |
| **Anger** | 4 + 5 + 7 + 23 | Brow down, eyes tighten, lips press |
| **Disgust** | 9 + 15 + 16 | Nose wrinkle + lip depression |
| **Contempt** | 12 + 14 (unilateral) | One-sided only — asymmetric signature |

---

## III. The VA (Valence-Arousal) Model

### Circumplex Model of Affect
Unlike categorical emotion labels, maps emotions on **two continuous dimensions**:

- **Valence**: degree of pleasantness (negative ← → positive)
- **Arousal**: intensity/energy level (calm ← → excited)

Modern research adopts a **parabolic ("V"-shaped) layout** — high valence emotions tend to correlate with higher arousal.

### VAD Extension (3D Model)
Some systems add **Dominance** (degree of control/influence felt):
- Used in affective computing, HCI, and multi-agent emotional generation systems

### Advantages for AI/ML
- Continuous dimensions → smoother transitions between emotional states
- Better alignment with physiological signals (heart rate, skin conductance)
- Complex feelings (nostalgia, frustration) don't fit categorical labels — VA handles them naturally
- Anger and excitement = both high arousal, but opposite valence → easily differentiated

### Emotion Quadrants
| Quadrant | State |
|---|---|
| High Arousal + Positive Valence | Excitement, joy, elation |
| High Arousal + Negative Valence | Fear, anger, anxiety |
| Low Arousal + Positive Valence | Contentment, calm, relaxed |
| Low Arousal + Negative Valence | Sadness, boredom, depression |

---

## IV. Micro-Expression Detection

### What They Are
- **Involuntary, fleeting** facial movements revealing suppressed or concealed emotions
- Duration: **0.04 to 0.5 seconds** (vs. macro-expressions: 0.5–4.0 seconds)
- Nearly impossible to suppress → window into authentic internal states
- Universal across cultures

### Detection Technology
- Human detection requires extensive training (skills degrade — retraining necessary)
- AI: **high-speed cameras (200+ fps) + CNNs + optical flow analysis**
- AEM-Net: multilevel channel feature extraction + attention modules for locating micro-expressions in long video streams
- Remote photoplethysmography (rPPG): blood volume changes measured through facial skin colour variation → heart rate proxy

### Expression Types Comparison
| Type | Duration | Volition | Visibility | FACS Intensity |
|---|---|---|---|---|
| Macro-expressions | 0.5–4.0s | Often voluntary | High | C–E |
| Micro-expressions | 0.04–0.5s | Involuntary | Very Low | Variable |
| Subtle expressions | Variable | Often spontaneous | Low | A–B |

---

## V. Practical Applications

### Animation & VFX Pipeline

**Blend Shapes (Disney, Pixar, DreamWorks)**
- FACS AU vectors used as **weights for blend shapes** — interpolate between target muscle poses
- Creates realistic 3D mesh deformations
- Pixar, Apple, Microsoft, Google, Disney, DreamWorks all use FACS in production

**Stop-Motion Replacement Libraries (LAIKA)**
- FACS guides creation of thousands of 3D-printed face plates
- Head segmented into **upper face** (brows/eyes) and **lower face** (mouth/jaw) below eye-line
- Each segment mixed/matched independently → full expressive range

**MoCap Retargeting (Gollum, Avatar, King Kong)**
- FACS provides standardised "language" for mapping actor performance onto creature rig
- WETA was first to use FACS in facial animation (Bay Raitt, *Lord of the Rings* 2001)
- Adopted for: Spider-Man 3, Monster House, King Kong, Benjamin Button, Avatar

### AI Character Generation

**SynchroRaMa Framework**
- Multi-modal emotion embedding: text (sentiment analysis) + audio (speech emotion recognition + VA features)
- AU loss function ensures generated avatars exhibit contextually appropriate emotions
- Audio-to-motion module → realistic head movement + lip sync
- LLM-generated scene descriptions as semantic prompts for emotional context

**FaceCrafter (Diffusion Model)**
- Independently manipulates **pose, expression, and emotion** without compromising identity
- Two lightweight control modules embedded in cross-attention layers
- Identity features kept orthogonal to control signals

**Emotional Performance Design Workflow**
1. Define target emotion → identify AU combination
2. Set VA coordinates (valence + arousal level)
3. Apply FACS intensity (A–E) to each AU
4. Use onset/apex/offset timing for naturalness
5. Check: is AU 6 present in "happy"? (if not, it reads as social/fake smile)

---

## VI. AI Prompting with FACS (Quick Reference)

### Emotion → AU → Prompt Descriptor
```
Happiness (genuine):  AU 6+12 → "raised cheeks, corners of mouth pulled up"
Sadness:             AU 1+4+15 → "inner brows raised, brows knit, lip corners depressed"
Fear:                AU 1+2+4+5+7+20+26 → "brows raised and knit, eyes wide, lips stretched, jaw dropped"
Anger:               AU 4+5+7+23 → "brows lowered, eyes tightened, lips pressed"
Contempt:            AU 12+14 unilateral → "one-sided smirk, single dimple"
Disgust:             AU 9+15+16 → "nose wrinkled, lip corners and lower lip depressed"
Surprise:            AU 1+2+5+26 → "full brow raise, eyes wide open, jaw dropped"
```

---

*Sources: 82 academic papers, industry pipeline docs, and AI research papers archived in NotebookLM "FACS VA Valence Micro and Normal Face Cues" (69ec4dd0). Synthesised 2026-05-25.*

# Higgsfield + ComfyUI Pipeline Architecture

> Unified AI film & content production pipeline. Higgsfield handles hosted fast iteration and branded ad output. ComfyUI (Win11/RTX 5070ti) handles local precision, LoRA-driven camera control, and zero-cost bulk generation. Reconstructed 2026-05-31 from UI mapping session.

**Status**: Architecture defined. Implementation pending Win11/RTX 5070ti setup.  
**Project anchor**: Isle of Dogs / Luna (Border Terrier) character content  
**Related**: [[comfyui]], [[higgsfield]], [[isle-of-dogs-project]]

---

## Platform Map

Higgsfield is **two separate apps** — not one. Different URLs, different asset systems, different pipelines.

| App | URL pattern | Purpose | Cost |
|---|---|---|---|
| **Cinema Studio** | app.higgsfield.ai | AI film, cinematic content, character work | ~2–96 credits/gen |
| **Marketing Studio** | ads.higgsfield.ai | Product ads, UGC, branded video | ~48 credits/gen |

---

## Cinema Studio — Full Control Map

### Models (version selector)

| Model | Key capability | Use when |
|---|---|---|
| Cinema Studio 3.5 | AI Director: style presets + camera + genre | Final hero shots, AI-directed multi-style |
| Cinema Studio 3.0 | Speed ramp + camera control | Controlled motion, speed effects |
| Cinema Studio 2.5 | Start frame support | Image-to-video cinematic |
| **Cinematic Cameras** | Named real camera bodies, DoP precision, ~2 credits | Cheap iteration, exact focal/aperture work |
| Seedance 2.0 | SOTA all-purpose video, 4–15s | Default serious video |
| Kling 3.0 (Exclusive) | 4K, audio sync, 3–15s | Premium single-plane shots |
| Kling 3.0 Motion Control | 1080p, 3–30s | Extended controlled motion |
| HappyHorse | 1080p, audio, 3–15s | Audio-sync content |

### Cinema Studio 3.5 — Director controls

**Genre** (sets overall visual tone):
Drama · Epic · General · Action · Horror · Comedy · Noir

**Style Settings** (3 independent axes):
- Color Palette: Auto / Naturalistic Clean / (+ more)
- Lighting: Auto / Soft Cross / (+ more)  
- Camera Moveset Style: Auto / Classic Static / (+ more)
- Manual Style toggle: override AI director choices

**Camera Settings** (DoP layer):
- Camera body (e.g. Raw 16mm, Studio Digital S35)
- Lens (e.g. Clinical Sharp)
- Focal Length (mm — 50, 75, custom)
- Aperture (e.g. f/11 Deep Focus, f/4)

**Bottom bar params:**
`model | duration(8s) | resolution(1080p) | aspect(Auto) | shots(1/4) | audio(Off) | @elements`

**Elements system** (identity layer):
- Characters / Locations / Props
- Referenced in prompt via `@name`
- Currently empty — needs populating with Luna + key locations
- CLI equivalent: Soul ID + `higgsfield marketing-studio avatars`

### Cinematic Cameras mode — key discovery

**~2 credits vs ~96 for CS 3.5.** Uses Wan 2.5 Fast. Named real-world camera presets:
- Studio Digital S35 — Premium Modern Prime, 35mm, f/4
- Raw 16mm + Clinical Sharp + 75mm + f/11 Deep Focus
- (more presets available via scroll)

Bottom bar in this mode: `Cinematic Cameras | 1/4 | 16:9 | 2K | 1x1`

**Use for:** rapid shot tests, DoP parameter exploration, face-reference-driven iteration before committing to CS 3.5 credits.

---

## Marketing Studio — Full Control Map

### Entry points
- **Url to Ad** — paste product URL → auto-imports product entity
- **Ad Reference** — upload reference video → style match generation

### Formats (UGC / Commercial tabs)

| Format | Description |
|---|---|
| UGC | Realistic social media videos |
| Tutorial | Step-by-step tutorials |
| Unboxing | High-quality unboxing |
| Hyper Motion | Highlight your product with motion |
| Product Review | Authentic product reviews |
| TV Spot | Authentic stories, amplified |
| Wild Card | Unique/creative video mode |
| UGC Virtual Try On | Try before you buy |

### Hooks system (Stunt / Subtle tabs)
"The first 3 seconds decide if your ad gets watched or skipped."

| Hook | Description |
|---|---|
| Product Hit | Object flies into frame, hits subject. Brief reaction → pivot |
| Spicy | Extreme close-up of collarbone, slowly reveals |
| Interview | Interviewer asks stranger a question based on product |
| Random Object Mic | Random absurd object falls into casual vlog |
| Product Crash | Product falls from above, destroyed, chaos |
| Blizzard | Cozy indoor scene hit by violent impossible weather |
| Camera Bump | Camera operator bumps into person |
| Product Dodge | Product flies at person's face; they dodge |

### Settings (Realistic / Unrealistic tabs)
Bedroom · Airplane Wing · Nature · Roofing · Kitchen · Car Roof · In Car · Street

### Product input
- URL: `www.yourproduct.com` → auto-fetch
- Manual: upload images + title
- App tab: App Store URL → webproduct entity

### Avatar system
**Presets:** Jayden · Stefan · Mei · Adriana · Clara · Maria · Sofia · Valentina (+ more, male/female filter)

**Custom avatars:**
- Upload photos (multiple angles)
- Name with `@handle`
- → `Create Avatar`
- **Luna** (@Luna) — Border Terrier/Boxer dog — Isle of Dogs project anchor

---

## 3-Tier Production Pipeline

```
┌─────────────────────────────────────────────────────────┐
│  TIER 1 — Rapid iteration (Cinematic Cameras, ~2 credits)│
│                                                          │
│  Face/character refs → Wan 2.5 Fast                      │
│  Real camera presets (S35, Raw 16mm)                     │
│  DoP: lens + focal length + aperture                     │
│  Use for: shot tests, camera angle exploration           │
└────────────────────┬────────────────────────────────────┘
                     │ best frames as start_image
                     ▼
┌─────────────────────────────────────────────────────────┐
│  TIER 2 — Production (Cinema Studio 3.5, ~96 credits)   │
│                                                          │
│  Genre + Style (Palette/Lighting/Moveset)                │
│  @Elements (Characters/Locations/Props)                  │
│  AI Director mode                                        │
│  Use for: hero shots, final content                      │
└────────────────────┬────────────────────────────────────┘
                     │ export frames as ControlNet input
                     ▼
┌─────────────────────────────────────────────────────────┐
│  TIER 3 — Local precision (ComfyUI Win11/RTX 5070ti)    │
│                                                          │
│  LTX 2.3 + Cameraman IC-LoRA                            │
│  Pull focus, dolly zoom, Hitchcock zoom                  │
│  Multi-pass compositing, style LoRAs                    │
│  Zero per-generation cost                               │
│  Use for: bulk gen, precise camera, complex pipelines   │
└─────────────────────────────────────────────────────────┘
```

---

## Handoff Points

| From | To | Method |
|---|---|---|
| ComfyUI local render | Higgsfield Cinematic Cameras | Upload frame as face reference |
| Cinematic Cameras output | Cinema Studio 3.5 | `--start-image` flag via CLI |
| Cinema Studio 3.5 output | ComfyUI | Export frame → ControlNet conditioning |
| Luna photos (local) | Marketing Studio | `higgsfield marketing-studio avatars create` |
| Marketing Studio @Luna | Cinema Studio Elements | Same identity, referenced via `@Luna` |

---

## Luna / Isle of Dogs Project Pipeline

Luna (Border Terrier/Boxer) is the primary character anchor:

```
Luna photos (multiple angles)
    → higgsfield marketing-studio avatars create @Luna
    → Marketing Studio: product ads with Luna as presenter
    → Cinema Studio Elements: @Luna in cinematic scenes
    → ComfyUI: generate reference frames, DoFACS expressions
    → Seedance 2.0: animate with consistent identity
```

**Content types enabled:**
- UGC-style product demos with Luna
- Cinematic Isle of Dogs narrative clips
- Stop-motion style (Tier 3 ComfyUI)
- Border Terrier expression reference sheets (DogFACS)

---

## CLI Automation Patterns

```bash
# Cinematic Cameras — cheap shot test
higgsfield generate create cinematic_cameras \
  --prompt "Luna runs across beach, Raw 16mm, f/11 deep focus" \
  --image ./luna-ref.jpg \
  --aspect_ratio 16:9 --wait

# Cinema Studio 3.5 — hero shot from tested frame
higgsfield generate create cinema_studio_3_5 \
  --prompt "Luna leaps through autumn leaves @Luna @beach-location" \
  --start-image ./tier1-output-frame.jpg \
  --duration 8 --resolution 1080p --wait

# Marketing Studio — product ad with Luna
PRODUCT_IDS=$(mktemp)
AVATARS=$(mktemp)
printf '["<product_id>"]' > "$PRODUCT_IDS"
printf '[{"id":"luna_avatar_id","type":"custom"}]' > "$AVATARS"
higgsfield generate create marketing_studio_video \
  --prompt "Luna discovers the product, looks at camera, tail wagging" \
  --avatars @"$AVATARS" \
  --product_ids @"$PRODUCT_IDS" \
  --mode ugc \
  --duration 15 --aspect_ratio 9:16 --wait

# Virality check on finished ad
higgsfield generate create brain_activity \
  --video ./finished-ad.mp4 --wait
```

---

## Next Steps (ordered)

1. **Create Luna avatar** — `higgsfield marketing-studio avatars create` with multi-angle photos
2. **Create Cinema Studio Elements** — add Luna as Character element + key locations
3. **Set up ComfyUI on Win11** — install LTX 2.3 + Cameraman IC-LoRA
4. **First test shot** — Tier 1 Cinematic Cameras with Luna ref → Tier 2 CS 3.5
5. **Isle of Dogs first scene** — define Genre/Style/Camera preset for series visual identity

## Related

- [[comfyui]] — local generation runtime
- [[higgsfield]] — platform entity
- [[ltx-video]] — LTX 2.3 model for ComfyUI
- [[seedance]] — primary Higgsfield video model
- [[soul-id]] — character identity system

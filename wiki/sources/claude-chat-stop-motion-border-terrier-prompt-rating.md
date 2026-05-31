---
title: "Stop-motion Border Terrier prompt rating"
date: "2026-05-14"
uuid: "1ee3b14b-9cb9-43c1-ab39-b400df546b2b"
source: "claude-chat-export"
messages: 10
---

# Stop-motion Border Terrier prompt rating

**Date**: 2026-05-14  
**Messages**: 5 human / 5 assistant  
**UUID**: `1ee3b14b-9cb9-43c1-ab39-b400df546b2b`  

## Conversation

### **Human**

rate this prompt: Full-body shot of a handcrafted Border Terrier stop-motion puppet, wearing a faded blue knitted beanie pulled low over one ear, Wes Anderson's Isle of Dogs aesthetic. Meticulous symmetrical composition. The long scruffy fur is made of clumped needle-felted alpaca wool and matted textile fibers, creating a stiff, handcrafted miniature look. Neutral facial expression with hand-painted resin eyes. Muted earthy color palette with burnt orange and dusty grey tones, dramatic macro photography lighting with harsh shadows. Background features a detailed Trash Island set with miniature debris and Japanese signage.

### **Claude**

I'll rate this prompt against the Isle of Dogs miniature craft standards laid out in the skill document.

## Rating: **6.5/10**

### What Works Well ✓
- **Materiality specificity** — "needle-felted alpaca wool and matted textile fibers" nails the tactile puppet construction
- **Correct aesthetic anchor** — "Wes Anderson's Isle of Dogs aesthetic" sets the visual world
- **Hand-crafted markers** — "hand-painted resin eyes," "handcrafted miniature look"
- **Color palette** — "burnt orange and dusty grey" fits the Trash Island rust-and-mustard world
- **Set integration** — mentions the miniature Trash Island environment

### Critical Issues ✗

**1. Workflow Violation (Major)**
This appears to be a **Step 3 scene plate** (puppet + environment) without establishing a **Step 1 base reference** first. The skill document is explicit: *"single-puppet character design on flat backdrop — the locked base reference"* must come before any scene work. You're combining puppet + set in the first shot, which breaks the production pipeline.

**2. Composition Conflict**
- Says "meticulous symmetrical composition" (correct for Wes Anderson)
- But then "full-body shot" + "dramatic macro photography lighting with harsh shadows"

"Macro photography" implies extreme close-up. "Full-body" is wide. These contradict. The skill calls for **planimetric composition** — perfectly level, perpendicular framing, not dramatic macro angles.

**3. Missing the Locked Stack**
No mention of:
- 12-inch hero-scale model
- Miniature depth of field / bokeh
- 'Boiling' fur fiber effect (stop-motion signature)
- Film grain, lens vignette, vintage 35mm look
- "Lived-in miniature physical world, not CGI"

**4. Minor: "Harsh shadows"**
Wes Anderson lighting is *theatrical* but typically balanced and controlled, not harsh/dramatic. The aesthetic leans flat and illustrative, not chiaroscuro.

---

## Corrected Approach

**What this should be:**

**Step 1 — Base Puppet Reference:**
*"Full-body planimetric shot of a handcrafted Border Terrier stop-motion puppet against a flat, neutral dusty-grey studio wall. Wearing a faded blue knitted beanie pulled low over one ear. Long scruffy fur made of clumped needle-felted alpaca wool and matted textile fibers with visible 'boiling' texture. Neutral deadpan expression, hand-painted glass-bead eyes. 12-inch hero-scale model. Miniature depth of field. Muted color palette: burnt orange collar detail, dusty grey and beige tones. Meticulously finished stop-motion puppet photography with fine fur fiber detail, hand-stitched felt seams. Shot on vintage 35mm film with subtle grain and soft vignette. Physical miniature world, not CGI."*

**Then Step 3 — Scene Plate** (after base is locked):
*"The Border Terrier puppet [as established] positioned in a meticulously finished Trash Island miniature diorama. Planimetric composition with obsessive symmetrical framing. Miniature set features detailed debris, rusted metal scraps, weathered Japanese signage. Forced perspective geometry. Nostalgic analog color grade: rust, mustard, beige. Theatrical miniature-scale lighting. 35mm film grain, lived-in tactile world."*

---

**TL;DR:** Solid material vocabulary and aesthetic understanding, but skips the foundational workflow step and mixes contradictory framing/lighting cues. Would produce a confused output. Needs restructuring into the two-step base → scene pipeline.

### **Human**

can you find references for how to build prompts to convert pets into looking exactly like stop motion animals from Wes Andersons isle of dogs stop motion puppets

### **Claude**

Now I have a thorough read of all 70 pages. Here's a comprehensive reference guide extracted directly from the PDF.

---

## Isle of Dogs Stop-Motion Puppet — Prompt Reference Guide
### From your 70-page PDF

---

### What the PDF Contains

The PDF is organized in three tiers of material:

**Pages 1–25 — Screen captures & finished puppet photography**
Clean studio reference shots, close-up film frames, and scene plates.

**Pages 26–58 — Behind-the-scenes construction**
Workshop shots showing the full build pipeline from clay to silicone mold to armature to fur.

**Pages 59–70 — High-resolution press photography**
The most detail-rich images: extreme macro face shots, promotional group portraits, and screen stills at 4K resolution.

---

### TIER 1 — The Fur System (pages 43–45, 60, 65)

This is the single most important thing your prompts need to capture. From the macro close-ups (pages 60 and 65 especially), you can see exactly how the fur is built:

**What the fur actually looks like:**
- Individual fiber strands are punched or implanted into the silicone skin — they stand out from the surface rather than lying flat like a pelt
- Multi-directional growth — fur radiates outward around the face, especially at the cheeks and brow ridge, creating a halo effect
- Color is **not uniform** — each puppet has warm amber/cream roots transitioning to darker tips (or vice versa), creating a lived-in, slightly dirty gradient
- There is always a subtle **"static" quality** — strands are slightly separated, not pressed together, giving the impression of arrested motion mid-shake

**Prompt language derived from this:**
```
individual implanted fur fibers radiating from silicone skin substrate, 
multi-directional scruffy growth with slight static separation between strands, 
warm amber-root-to-dark-tip gradient coloring, visible fiber tips catching 
side-lighting, handcrafted needle-punch texture
```

---

### TIER 2 — The Eyes (pages 59, 60, 63)

Page 60 is your best single reference — an extreme macro of Chief's face. The eyes are the defining "read as puppet" signal:

**What the eyes actually are:**
- Blown glass spheres with a hand-painted iris — amber/orange, green-grey, or vivid blue depending on character
- The iris has slight radial texture, like a painted clock face — not smooth digital color
- The **highlight** is a single sharp specular dot at roughly 10 o'clock — from a practical studio light, not ambient
- The sclera (white) is slightly off-white / cream — never pure digital white
- The eyelid surround is sculpted silicone with a slight puffy, anatomical form

**Prompt language:**
```
hand-blown glass eyes with painted amber/orange iris showing subtle radial 
brushstroke texture, single sharp specular highlight from practical studio light, 
off-white cream sclera, surrounding silicone eyelid with soft anatomical sculpt
```

---

### TIER 3 — The Nose & Snout (pages 26, 43, 60)

Page 26 shows the sculpting process in extreme close-up — a craftsperson using dental tools to sculpt the snout in clay before the mold is made. Combined with the finished macro shots:

**Characteristics:**
- The nose is a separate sculpted piece — matte, slightly porous-looking resin or painted silicone
- Nostrils are visibly dimensional — carved channels, not flat painted shapes
- The muzzle area has a slightly different texture to the rest of the face — less fur, more bare silicone, with a subtle leathery surface
- Lip/mouth line is painted — often slightly asymmetrical, giving character

**Prompt language:**
```
sculpted matte resin nose with dimensional carved nostrils, leathery silicone 
muzzle area with sparser fur coverage, hand-painted asymmetrical lip line
```

---

### TIER 4 — The Armature (pages 36, 44)

Page 36 is the clearest armature shot — a bare steel ball-and-socket skeleton. This is important for prompts because you want the finished puppet to *hint* at mechanical structure underneath:

**What to know:**
- The skeleton is machined stainless steel ball-and-socket joints (not wire armature)
- This gives the puppets their upright, slightly stiff posture — weight is held deliberately, not relaxed
- Feet are flat and wide with separate toe segments — this is why the puppets stand in a planted, deliberate stance
- Limb proportions are slightly elongated compared to real dogs — legs are longer relative to the torso

**Prompt language:**
```
slightly elongated leg proportions suggesting internal ball-and-socket 
armature, deliberate planted stance with flat articulated paw-feet, 
upright posture with mechanical rigidity beneath the fur
```

---

### TIER 5 — Skin Body Construction (pages 33, 40)

Pages 33 and 40 show the silicone casting process. This tells you what the underlying body looks like — relevant when fur is sparse:

- The body cast is made from a foam latex or silicone pour into a clay negative mold (page 33)
- The amber/honey colored silicone being poured (page 40) shows the base skin color before fur is implanted — warm golden, slightly translucent
- Where fur is absent (belly, inner legs, muzzle), this translucent silicone skin is visible and has a slight sheen

**Prompt language:**
```
translucent amber-tinted silicone skin visible at muzzle and inner limbs, 
subtle subsurface warmth from foam latex body cast, slight tackiness/sheen 
on bare silicone surfaces
```

---

### TIER 6 — Collar Design (pages 3, 7, 63, 65)

All main dog characters wear collars — an important finishing detail:

- Dark brown or black leather, hand-stitched, with visible seam lines
- Metal hardware: D-rings, buckles with genuine patina/aging
- Name tags are individually fabricated metal plaques with stamped text (visible on page 59: "SPOTS", "KING", "DUKE", "NUTMEG")
- Collar sits slightly loose — not tight against neck

---

### TIER 7 — The Neutral Grey Studio Reference Shot (pages 3, 4, 5)

**This is your Step 1 base reference format.** Pages 3–6 are the clearest examples of what the skill doc calls the "planimetric mug-shot" — every character has one of these:

- **Background:** Seamless mid-grey studio paper/backdrop (not white, not textured — smooth gradient grey)
- **Lighting:** Soft diffused key from slightly above + a gentle fill from opposite side — no harsh shadows, no dramatic fall-off
- **Camera height:** Exactly level with the puppet's center of gravity — never above, never below
- **Framing:** Full body with ~15–20% breathing room on all sides
- **Ground:** Same grey seamless extending to floor — puppet casts a very soft, diffused shadow

**Prompt language for the base reference shot:**
```
seamless mid-grey studio backdrop, soft diffused bilateral lighting with 
no harsh shadows, camera at puppet eye level, full-body planimetric framing 
with generous negative space, soft ground shadow on grey seamless
```

---

### Complete "Convert My Pet" Prompt Template

Using all of the above, here's a ready-to-use template for converting a real pet photo into an Isle of Dogs puppet:

```
Isle of Dogs stop-motion puppet portrait. [BREED] character, 12-inch hero-scale 
puppet. [FUR COLOR/PATTERN] fur constructed from individually implanted needle-punch 
fibers radiating from amber-tinted translucent silicone skin substrate, multi-
directional scruffy growth with slight static separation between strands, 
warm-root-to-dark-tip gradient. 

Hand-blown glass eyes with painted [EYE COLOR] iris showing subtle radial 
brushstroke texture, single sharp specular highlight at 10 o'clock, off-white 
cream sclera, soft sculpted silicone eyelid surround. 

Sculpted matte resin nose with dimensional carved nostrils, leathery silicone 
muzzle with hand-painted asymmetrical lip line. Dark brown hand-stitched leather 
collar with aged metal hardware and stamped name tag.

Deadpan stoic expression. Slightly elongated limb proportions, deliberate 
planted stance suggesting internal ball-and-socket armature.

Shot on seamless mid-grey studio backdrop, soft diffused bilateral lighting, 
camera at puppet eye level, full-body planimetric framing. Miniature scale 
depth of field with fine foreground bokeh. 

Physical stop-motion puppet photography — not CGI, not rendered. Visible tactile 
handcraft throughout. Slight 'boiling' animation texture in fur strands. 
Nostalgic analog color grade: muted warm tones, rust, amber, dusty grey.
Shot on vintage 35mm film with fine grain and soft lens vignette.
```

---

### Quick Character Color Keys from the PDF

| Character type | Fur base | Fur tip | Eye color | Collar |
|---|---|---|---|---|
| Chief (pages 3, 65) | Cream/white | Charcoal grey | Green-grey | Dark brown leather |
| Rex (page 63) | Warm golden amber | Dark amber | Orange-amber | Dark brown + name tag |
| Boss (pp 13, 46) | Buff/tan | Darker tan | Amber | Dark with tag |
| Duke (pp 59) | Cream white | Grey-buff | Amber | Black leather "DUKE" |
| King (pp 59, 46) | Russet brown/orange | Dark brown | Brown | Ornate gold chain |
| Spots (pp 59) | White | White | Vivid blue | Grey jersey-knit |
| Dark Scottie (pp 63) | Deep indigo-black | Dark purple | Vivid blue | Dark leather |

These are your color reference keys when adapting a real pet's coloring into puppet materiality.

### **Human**

can you create a modified version prompt for working with 1. Adobe under Firefly (limited prompt Size) 2. GPT 2 3. Nano Banana 2 and pro

### **Claude**

Now I have everything I need. Let me build all four platform-specific versions from the reference material.
Now I have everything needed. Here are all four platform-specific versions, engineered from the PDF references and skill constraints.

---

## Platform-Specific Prompt Templates
### Isle of Dogs — Convert My Pet

---

## 1. Adobe Firefly
**Constraint: ~900 characters max. Uses Firefly's native style vocab. No negative prompts.**

The strategy here is **style keywords first, then materiality, then technical.** Firefly reads the opening 200 chars most heavily.

```
Stop-motion puppet portrait, [BREED] dog, Wes Anderson miniature style. 
Needle-felted [FUR COLOR] alpaca wool fur, scruffy and multi-directional. 
Hand-blown glass [EYE COLOR] eyes, single specular highlight, off-white 
sclera. Sculpted resin nose, carved nostrils, leathery silicone muzzle. 
Dark leather collar, aged metal tag. Deadpan expression.

Seamless mid-grey studio backdrop. Soft diffused bilateral lighting, 
no harsh shadows. Camera at puppet eye level. Full body, planimetric 
framing. Miniature depth of field, soft bokeh.

Physical stop-motion model, not CGI. Tactile handcraft. Fine film grain. 
Muted earthy tones, rust and amber palette. Vintage 35mm.
```

**~640 chars — well within limit.**

**Firefly-specific tips:**
- In the Firefly UI, also select **"Photo"** as Content Type and **"Studio"** as Lighting Style — these do heavy lifting so your prompt doesn't have to
- Add **"stop motion"** to the style panel if it surfaces as a visual style chip
- The grey studio backdrop is critical — without it Firefly will invent a scene. Keep that line verbatim.

---

## 2. Higgsfield GPT-2
**Constraint: Face/chest-up only. Maximum macro fidelity. Replaces the photoreal human stack with the Miniature Craft stack adapted for puppet face detail.**

GPT-2 is the right choice when you want the eyes, nose, and fur at extreme macro — equivalent to pages 60, 63, and 65 from your PDF.

```
Stop-motion puppet face portrait. [BREED] character. [FUR COLOR] 
individually implanted needle-punch alpaca wool fur radiating from 
translucent amber-tinted silicone skin, individual fiber strands 
separating with slight boiling texture, warm-root-to-dark-tip color 
gradient, fibers catching theatrical side-lighting at strand level.

Hand-blown glass eyes with painted [EYE COLOR] iris showing subtle 
radial brushstroke texture in the iris pattern, single sharp specular 
highlight at 10 o'clock from practical studio key light, off-white 
cream sclera, soft sculpted silicone eyelid surround with anatomical 
puffiness. Sculpted matte resin nose with dimensional carved nostrils, 
slight surface porosity, leathery silicone muzzle with sparser fur 
coverage, hand-painted asymmetrical lip line. [COLLAR if in frame: 
dark hand-stitched leather with aged metal hardware, stamped name tag.]

Chest-up puppet portrait. Pure white seamless studio backdrop. 
Classical beauty lighting — soft key from slightly above and 
camera-left at 35 degrees, soft fill at chest level from camera-right, 
subtle hair light behind defining crown fur separation, soft underlight 
bounce lifting eye socket shadows.

Extreme face fidelity. Individual fur fiber strands rendered at macro 
scale with visible implantation texture into silicone substrate, 
strand-by-strand boiling separation, hand-painted iris detail with 
visible radial pattern, sculpted snout with pore-level surface texture, 
resin nose with dimensional nostril depth.

Meticulously finished 12-inch hero-scale stop-motion puppet 
photography. Physical model, not CGI, not rendered. Miniature scale 
depth of field with soft background bokeh. Kodak Vision3 film 
emulation, fine film grain, soft lens vignette, rich warm saturation. 
Lived-in handcraft materiality throughout.
```

---

## 3. Nano Banana 2
**Constraint: Mid-weight prompt. Faster generation, slightly lighter on description than full Banana Pro. Hit all systems but compress each.**

```
Isle of Dogs stop-motion puppet portrait. [BREED] character, 
12-inch hero-scale puppet. [FUR COLOR] fur constructed from 
individually implanted needle-punch fibers radiating from 
amber-tinted translucent silicone skin, multi-directional scruffy 
growth with slight boiling static separation between strands, 
warm-root-to-dark-tip color gradient.

Hand-blown glass eyes with painted [EYE COLOR] iris showing subtle 
radial texture, single sharp specular highlight, off-white cream 
sclera, soft sculpted silicone eyelid surround. Sculpted matte 
resin nose with dimensional carved nostrils. Leathery silicone 
muzzle with hand-painted asymmetrical lip line. Dark hand-stitched 
leather collar with aged metal hardware and stamped name tag.

Deadpan stoic expression. Slightly elongated limb proportions 
suggesting internal ball-and-socket armature. Deliberate planted 
paw-stance.

Seamless mid-grey studio backdrop. Soft diffused bilateral studio 
lighting, no harsh shadows. Camera at puppet eye level. Full body 
planimetric framing with generous negative space.

Meticulously finished miniature stop-motion puppet photography. 
Visible tactile textures: scruffy mohair and alpaca fur fibers 
with slight boiling effect, hand-stitched felt seams, hand-painted 
translucent silicone skin. Miniature scale depth of field with 
soft bokeh. Nostalgic analog color grade: rust, mustard, beige. 
Shot on vintage 35mm with fine film grain and soft lens vignette. 
Physical miniature world, not CGI, not rendered.
```

---

## 4. Banana Pro (Full Spec)
**Constraint: None — this is the full production prompt. All systems from the PDF documented. Use this as your master template.**

```
Isle of Dogs stop-motion puppet portrait. [BREED] character, 
12-inch hero-scale puppet. [FUR COLOR/PATTERN] fur constructed 
from individually implanted needle-punch fibers radiating from 
amber-tinted translucent silicone skin substrate, multi-directional 
scruffy growth with slight static separation between strands, 
warm-root-to-dark-tip color gradient, individual fiber tips catching 
theatrical side-lighting.

Hand-blown glass eyes with painted [EYE COLOR] iris showing subtle 
radial brushstroke texture, single sharp specular highlight at 
10 o'clock from practical studio key light, off-white cream sclera, 
soft sculpted silicone eyelid surround with anatomical puffiness. 
Sculpted matte resin nose with dimensional carved nostrils and slight 
surface porosity. Leathery silicone muzzle area with sparser fur 
coverage revealing translucent amber skin. Hand-painted asymmetrical 
lip line. Dark hand-stitched leather collar with aged metal D-ring 
hardware, burnished buckle, and individually stamped metal name tag.

Deadpan stoic expression, no smile. Slightly elongated limb 
proportions suggesting machined stainless steel ball-and-socket 
armature underneath. Deliberate planted wide-foot paw-stance, 
weight held rigidly — not relaxed.

Seamless mid-grey studio backdrop, no texture. Soft diffused 
bilateral studio lighting — gentle key from slightly above with 
matching fill from opposite side, zero harsh shadow fall-off, 
soft ground shadow on seamless. Camera perfectly level at puppet 
center-of-gravity height. Full body planimetric framing with 
15–20% breathing room on all sides.

Meticulously finished miniature stop-motion puppet photography. 
12-inch hero-scale physical model. Visible tactile textures 
throughout: fine scruffy mohair and alpaca fur fibers exhibiting 
a slight boiling effect, hand-stitched felt seams, hand-painted 
translucent silicone skin with visible subtle brushstrokes, 
glass-bead eyes with pinpoint light reflections. Miniature scale 
depth of field with soft foreground and background bokeh. 
Theatrical miniature-scale studio lighting. Nostalgic analog 
color grade: rust, mustard, dusty beige, burnt amber. Shot on 
vintage 35mm camera with fine film grain, subtle chromatic 
aberration at frame edges, soft lens vignette, and rich 
saturation. Physical stop-motion model — not CGI, not rendered, 
not digital interpolation.
```

---

## Quick Substitution Keys

Swap these variables across all four platforms:

| Variable | Examples from your PDF |
|---|---|
| `[BREED]` | scruffy terrier mix, Schnauzer-type, wire-haired, Scottie, spitz-type |
| `[FUR COLOR]` | warm golden amber / cream-white-to-charcoal-grey / deep indigo-black / russet-brown-to-dark-tip / buff-tan |
| `[EYE COLOR]` | amber-orange / vivid blue glass-bead / green-grey / warm brown / red-amber |
| `[COLLAR]` | dark brown leather + aged brass tag / black leather + stamped chrome plate / grey jersey-knit collar |

### **Human**

can you create this into a skill

### **Human**

/isle-of-dogs-director can you create this into a new skill

### **Claude**

Now let's package it:
Here's what was built and how it's structured:

**`isle-of-dogs-multi-platform.skill`** — 5 files, clean hierarchy:

```
SKILL.md                        ← Router + workflow (reads fast)
references/
  firefly.md                    ← ~900 char constraint, trim order, UI chip tips
  gpt2.md                       ← Chest-up only, macro fidelity, credit warning
  nano-banana.md                ← Mid-weight, 6-system compressed spec
  banana-pro.md                 ← Full master, 9 systems, 6-panel sheet, Soul Cinema note
```

**How the skill works in practice:**

The `SKILL.md` handles intake — it locks the puppet spec (breed, fur gradient, eye color, collar, expression) and routes to the right reference file. Claude only loads the platform file it actually needs, keeping context lean. The skill triggers on any combination of "Isle of Dogs", "stop-motion puppet", "convert my pet", or "puppet prompt" — even without a platform name.

**Three design decisions worth noting:**
- The **three non-negotiables** (fur materiality, glass eyes, "not CGI") are called out explicitly in the router — they survive even Firefly's most aggressive trimming
- The **color key table** lives in the router, not in each reference file, so it's always available regardless of platform
- Firefly gets a dedicated **trim order** — a ranked list of what to cut first if you're over the char limit, so you never accidentally drop the wrong line

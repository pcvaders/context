---
title: Master — ComfyUI Complete Installation & Optimization Guide 2026
date: 2026-05-25
tags: [comfyui, local-ai, ltx-video, flux, stable-diffusion, installation, master-guide]
summary: Complete ComfyUI setup guide — installation per OS, VRAM thresholds, exact CFG values, model file paths, launch flags, LTX-2.3 two-stage pipeline, troubleshooting
source_notebook: https://notebooklm.google.com/notebook/80eb9ef9-668c-472e-a54e-b5ab918daa2a
source_count: 58
version: 1.0
---

# Master: ComfyUI — Complete Installation & Optimization Guide 2026

> 58-source comprehensive ComfyUI guide. Primary focus: LTX-2.3 video generation pipeline. Covers Windows/Mac/Linux/Docker/Cloud install, exact VRAM thresholds, CFG values, model file paths, launch flags, Two-Stage pipeline, advanced conditioning.

---

## Table of Contents

1. [Installation by Platform](#chapter-1-installation-by-platform)
2. [Hardware Requirements and VRAM](#chapter-2-hardware-requirements-and-vram)
3. [Model Types and File Management](#chapter-3-model-types-and-file-management)
4. [Key Nodes and Workflows](#chapter-4-key-nodes-and-workflows)
5. [LTX-2.3 Two-Stage Production Pipeline](#chapter-5-ltx-23-two-stage-pipeline)
6. [Advanced Configurations](#chapter-6-advanced-configurations)
7. [Troubleshooting and Best Practices](#chapter-7-troubleshooting-and-best-practices)

---

## Chapter 1: Installation by Platform

### 1.1 Windows
**Option A — Desktop App (Recommended)**
- Standalone installer, auto-configures Python and dependencies
- One-click migration from existing setups

**Option B — Portable Version**
- Pre-packaged ZIP with embedded Python environment
- No manual environment management

**Option C — Manual Install**
```bash
git clone https://github.com/comfyanonymous/ComfyUI
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
```
Requires: Git, Python 3.10+, NVIDIA drivers, CUDA

### 1.2 Apple Silicon (M1/M2/M3/M4)
**Option A — Desktop App**
- Recommended for ease of use
- Select **Apple Metal** option for hardware acceleration

**Option B — Manual**
```bash
pyenv install 3.11
pyenv local 3.11
python -m venv venv && source venv/bin/activate
# Install stable PyTorch with MPS support
pip install torch torchvision torchaudio
```

### 1.3 Linux
```bash
# Resolve library loading errors
export LD_LIBRARY_PATH=/path/to/cuda/lib64:$LD_LIBRARY_PATH
git clone https://github.com/comfyanonymous/ComfyUI
pip install -r requirements.txt
```

**AMD (ROCm/Linux):**
```bash
HSA_OVERRIDE_GFX_VERSION=11.0.0 python main.py
```

### 1.4 Docker
```bash
docker run --gpus all \
  -p 8188:8188 \
  -v /path/to/models:/app/models \
  comfyui:latest \
  --enable-sageattention  # 2-3x attention speedup
```
Performance-tuned images with SageAttention auto-activation.

### 1.5 Cloud Platforms
| Platform | Key Fix |
|----------|---------|
| RunDiffusion | Force venv injection for ModuleNotFoundError |
| Vast.ai | Same venv injection |
| RunPod | Same venv injection |

LAN access flag: `--listen` → accessible at `http://[local-IP]:8188`

---

## Chapter 2: Hardware Requirements and VRAM

### 2.1 VRAM Thresholds

| VRAM | Capability |
|------|-----------|
| 8GB | Entry baseline — SD 1.5, SDXL (tight), Flux FP8 (very tight) |
| 12GB | LTX-2.3 minimum — distilled model + FP8 offloading required |
| 16GB | LTX-2.3 comfortable — quantized models workable |
| 24GB | LTX-2.3 recommended — full BF16, no compromise |
| 48–80GB | Non-quantized two-stage pipelines at high resolution |

**Safety threshold:** Crash risk when VRAM hits **90–95%**.

### 2.2 Exact Launch Flags

```bash
# Memory management
--lowvram              # Most aggressive — streams to VRAM as needed
--medvram              # Balanced saving
--novram               # Smooths memory spikes during model swaps
--disable-pinned-memory  # Fixes "pixel mush" glitches, memory clogging
--disable-async-offload  # Stops memory corruption issues
--reserve-vram 5       # Reserve 5GB for system (adjust number as needed)

# UI
--front-end-version comfy.org/comfyui_frontend@latest  # Force latest web UI
--listen               # Enable LAN access
```

### 2.3 VRAM Management Techniques
- **CPU Offloading:** Move VAE decode or Gemma text encoder to system RAM
- **"Clear VRAM and Cache"** button or custom purge nodes — free memory without restart
- **SageAttention:** 2–3x attention computation speedup, minimal quality loss (Docker builds)
- **Quantization formats:** FP8, GGUF (Q3/Q4), NF4 — reduce memory footprint

---

## Chapter 3: Model Types and File Management

### 3.1 Exact File Paths (relative to COMFYUI_ROOT_FOLDER/)

```
models/
  checkpoints/         # Main model weights (e.g., ltx-2.3-22b-dev.safetensors)
  vae/                 # VAE decoders (e.g., ltxvideo_vae_bf16.safetensors, ae.safetensors)
  text_encoders/       # T5-XXL, Gemma 3 12B (e.g., gemma_3_12B_it_fp4_mixed.safetensors)
  clip/                # Alternative text encoder location
  loras/               # LoRA weights (e.g., ltx-2.3-22b-distilled-lora-384-1.1.safetensors)
  latent_upscale_models/  # LTXVLatentUpsampler (e.g., ltx-2.3-spatial-upscaler-x2-1.1.safetensors)
  controlnet/          # ControlNet weights
  LLM/                 # Local LLMs (GGUF format)
```

Multi-instance model sharing: configure `extra_model_paths.yaml`

### 3.2 Supported Model Families

| Family | Models | Use Case |
|--------|--------|----------|
| Stable Diffusion | SD 1.5, SDXL | Classic image generation |
| Next-gen diffusion | Flux.1 Dev/Schnell, WAN 2.1/2.2 | High-fidelity image/video |
| Video foundation | LTX-Video, LTX-2, LTX-2.3 | Audio-video generation |
| Multimodal VLMs | Gemma 4, Qwen | Local analysis of text/image/video/audio |

### 3.3 Exact CFG Values by Model

| Model | CFG Range | Notes |
|-------|----------|-------|
| Flux Dev/Schnell | 1.0–1.5 | Baseline 1.0 |
| SD 1.5 / SDXL | 6.0–8.0 | Sweet spot: 7.0 |
| SDXL Turbo / DMD2 | 1.0–5.0 | — |
| LTX-2.3 (general) | 2.0–7.0 | — |
| LTX-2.3 I2V | 3.0–5.0 | Maintains consistency |
| LTX-2.3 V2V | 2.0–4.0 | — |
| LTX-2.3 Stage 1 | 4.0–6.0 | Base coherence pass |

**Bimodal CFG (LTX-2.3 modality-aware):**
- Video stream: textual scale = **3.0**, cross-modal scale = **3.0**
- Audio stream: textual scale = **7.0**, cross-modal scale = **3.0**

### 3.4 Resolution Matching (Critical)
| Model | Target Resolution |
|-------|-----------------|
| SD 1.5 | 512px |
| SDXL / Flux | 1024px |
| LTX-2.3 | Variable (match training res) |

Mismatching resolution → "mangled limbs" and composition failures.

---

## Chapter 4: Key Nodes and Workflows

### 4.1 Essential Nodes
- **ComfyUI Manager:** Install missing nodes, update core, browse model database
- **Efficiency Nodes:** Combine loader + sampler + VAE into single block — reduces clutter
- **ComfyUI Impact Pack:** Advanced masking, face detailing

### 4.2 Video Production Nodes (LTX-2.3)
- **LTX-2.3 T2V:** Text to video
- **LTX-2.3 I2V:** Image to video
- **LTX-2.3 V2V:** Video to video (style transfer)
- **LTXVLatentUpsampler:** Spatial latent upscaling between pipeline stages
- **VAE Decode (Tiled):** High-res decode without OOM (tile size: 256, overlap: 32)
- **LTX Director:** Community timeline editor — custom audio + frame control + Prompt Relay

### 4.3 Prompt Relay
Assign different prompts to specific **temporal intervals** within a video:
- Segment 0–3s: establishing description
- Segment 3–6s: action description
- Segment 6–8s: resolution description
Enables precise narrative control without re-generation.

### 4.4 Identity Nodes
- **ID-LoRA:** Speaker identity transfer — reference audio drives vocal/facial performance in talking-head videos
- **LTX Studio Trained Actors:** Consistent digital facsimiles reusable across project scenes

---

## Chapter 5: LTX-2.3 Two-Stage Production Pipeline

### 5.1 Setup
```bash
# In ComfyUI Python environment:
pip install ltx_core ltx_pipelines

# Via ComfyUI Manager:
# Search → Install "ComfyUI-LTX-Video"
```

### 5.2 Sanity Check Before Full Run
Generate **9-frame** test clip:
- Dev model: **20 steps**
- Distilled model: **6 steps**
Verify model paths work before attempting full generation.

### 5.3 Two-Stage Pipeline (Full)

**Stage 1 — Base Coherence**
```
Resolution: Half target (e.g., 640×384 for 1280×768 output)
Steps: 25–35
CFG: 4.0–6.0
Purpose: Establish global motion and composition
```

**Transition**
```
Node: LTXVLatentUpsampler
Function: Spatially increase video latent, maintain temporal consistency
```

**Stage 2 — Refinement**
```
Steps: 15–20
LoRA: ltx-2.3-22b-distilled-lora-384-1.1.safetensors
LoRA weight: 0.7–0.8
Purpose: Add sharp details without re-rolling composition
```

**Memory Fix (>15s video or high-res)**
```
Replace: Standard VAE Decode
With: VAE Decode (Tiled)
Settings: tile_size=256, overlap=32
```

### 5.4 Bimodal CFG (Modality-Aware)
Novel conditioning scheme — independent control over text guidance and cross-modal guidance:
- Improves phonetic accuracy in speech generation
- **Thinking Tokens:** Global information aggregation before diffusion = better phonetic alignment

---

## Chapter 6: Advanced Configurations

### 6.1 HDR Workflow
**HDR IC-LoRA** generates linear HDR video:
- Encoded in **ARRI LogC3**
- Suitable for professional color grading
- Supports **EXR export**
Use case: professional VFX pipelines, cinema-grade output

### 6.2 Multi-Tile Inference (1080p Output)
Partition upscaled latents into overlapping spatial and temporal tiles for 1080p output without OOM. Requires: 24GB+ VRAM recommended.

### 6.3 Workflow Metadata Recovery
Drag any generated image back into ComfyUI → automatically reconstructs the exact node graph embedded in image metadata. Full workflow recovery from output file alone.

### 6.4 Seed Strategy
- **Random seed:** Exploration phase
- **Fixed seed:** Refinement phase — reproduce high-quality results exactly

---

## Chapter 7: Troubleshooting and Best Practices

### 7.1 Common Error → Fix

| Error | Cause | Fix |
|-------|-------|-----|
| Washed-out / off-color images | VAE loading error | Verify VAE path in `models/vae/` |
| Mangled limbs | Resolution mismatch | Match input res to model training res |
| "Fried" images | CFG too high for Flux | Set Flux CFG to 1.0–1.5 |
| Red nodes | Missing custom nodes | Manager → auto-install missing |
| Tensor dimension error | Architecture mismatch | Ensure all models same architecture family |
| Memory crash | VRAM >90–95% | Add `--lowvram` or `--disable-pinned-memory` |
| "Pixel mush" glitches | Pinned memory issue | Add `--disable-pinned-memory` |

### 7.2 Update Cadence
Maintain **monthly minimum** updates for ComfyUI core and custom nodes. Older versions cause API obsolescence → red node errors in community workflows.

### 7.3 Cloud GPU Providers
- **Comfy Cloud:** Remote GPU via official ComfyUI integration
- **RunDiffusion, Vast.ai, RunPod:** Third-party cloud GPU rentals
- Minimum recommended: **24GB VRAM** instance for LTX-2.3 full quality

---

## Unique Techniques (not in other notebooks)

1. **Two-Stage LTX pipeline** — half-res coherence pass → latent upsample → detail refinement
2. **Bimodal CFG** — independent text/cross-modal guidance for video+audio streams
3. **Thinking Tokens** — global aggregation before diffusion, improves speech phonetics
4. **HDR IC-LoRA → ARRI LogC3 / EXR** — cinema-grade HDR output
5. **Prompt Relay** — temporal interval prompting within single video generation
6. **VAE Decode (Tiled)** — tile_size=256, overlap=32 for long/high-res video
7. **Workflow metadata recovery** — drag image back in → full node graph reconstruction
8. **ID-LoRA for talking heads** — reference audio → vocal/facial identity transfer
9. **`--disable-pinned-memory`** — fixes pixel mush, undocumented flag
10. **9-frame sanity check** — verify paths before full generation

---

## Cross-Links
- [[master-veo-professional-2026]] — cloud-based Veo pipeline
- [[master-veo3-prompting-april-2026]] — prompt engineering techniques
- [[pcg1-directors-prep]] — directors prep skill uses ComfyUI ControlNet
- [[MASTER_AI_CREATION_GUIDE]] — unified master guide

> Two ComfyUI installs live side by side under Pinokio on Win11: the original (untouched) and an updated clone built for RTX 50-series (Blackwell) with SageAttention.

# ComfyUI on Pinokio — Blackwell/cu130 clone

## Context
User's primary ComfyUI usage moved to Pinokio (`H:\Pinokio\api\`) (as of 2026-09), replacing `H:\3DComfyUI-Easy-Install\...` as the daily-driver install. That older install is kept as a **reference-only** known-good Blackwell build (used to recover exact working wheel URLs via `direct_url.json`).

## Two Pinokio apps

| App folder | Pinokio title | Python | torch/vision/audio | SageAttention | flash_attn | start.js |
|---|---|---|---|---|---|---|
| `H:\Pinokio\api\comfy.git` | "Comfyui" | 3.10.20 | 2.7.0+cu128 | none | none | unmodified (`python main.py`) |
| `H:\Pinokio\api\comfy-updated.git` | "Comfyui (Updated + SageAttention)" | 3.12.9 | 2.9.1+cu130 (all three pinned identical — see [[2026-09-02-torchaudio-abi-version-pin]]) | 2.2.0 | 2.8.3 | `python main.py --use-sage-attention` |

The clone was built by robocopy'ing the original (`/E /COPY:DAT /R:2 /W:2 /MT:16` — `/COPYALL` needs admin "Manage Auditing" right this account doesn't have, so `/COPY:DAT` was used instead), then:
- `git pull origin master` on `app/` → landed on ComfyUI `v0.34.0`-era build
- `git pull origin main` on `app/custom_nodes/ComfyUI-Manager` → already current
- venv rebuilt from scratch (old venv kept as `app/env-py310-cu128.bak` for rollback) using a `uv`-managed Python 3.12.9 interpreter
- torch stack + SageAttention/flash_attn wheels installed via exact URLs recovered from the reference install's `direct_url.json` files (SageAttention wheel is `cp39-abi3`, version-agnostic; flash_attn is `cp312`-specific — both must match the torch/cuda build string exactly, e.g. `+cu130torch2.9.0.post3`)

Verified working end-to-end (not just boot) — real SDXL text-to-image generation via the ComfyUI HTTP API against `illustriousXL10_v10.safetensors`, 1024×1024, 20-24 steps, ~20s, output image visually inspected before being reported as working.

## Related
- [[2026-09-02-torchaudio-abi-version-pin]] — the ABI mismatch bug hit while building this clone
- [[pinokio]]
- [[Windows 11]]

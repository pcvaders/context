---
title: Agentic OS
summary: "Unified homelab command center and agent operating dashboard serving telemetry, 3D connectome, multi-theme runtime, and living animations."
tags: [agent-os, dashboard, telemetry, ui, homelab]
---

# Agentic OS

> Unified command center and agent runtime dashboard combining panel-server tools, real-time homelab telemetry, and multi-theme interactive interfaces.

**Repository**: `~/projects/agent-os`  
**Ports**: `7700` (production hub / panel-server), `7701` (local development server)  
**Entry points**: `server.py`, `index.html`, `shell.js`, `theme.css`, `soot-sprites.js`  
**Deployment**: Local Mac and Proxmox LXC command-centre container

## Core Architecture

Agentic OS absorbs and unifies:
1. **Panel Server**: MCP toggles, wiki browser, recall proxy, note rendering, code graph views.
2. **Clean GUI Server**: Service monitoring, process start/stop, log viewing, and notification feeds.
3. **Telemetry Cockpit**: Live homelab stats, active host pings, launchd daemon states, and hardware metrics.
4. **3D Interactive Visualizer**: Brain connectome visualization displaying active agent neural graphs and project clusters.

## Selectable Theme Presets

Configured in `theme.css` and toggled via top bar selector `#theme-preset-select` with instant persistence to `localStorage`:

| Theme Preset | Identifier | Aesthetic & Key Styling |
|---|---|---|
| **Cyberpunk HUD** | `cyberpunk` | Cosmic void black, neon cyan and indigo specular glows, dual-ring engine beads, glassmorphism blur. |
| **Spirited Away** | `ghibli` | Bathhouse vermilion, Yubaba gold leaf, Chihiro river teal, washi rice paper warmth, living Soot Sprites swarm. |
| **UK Drum & Bass** | `dnb` | 180g dubplate vinyl black, hazard rave yellow, 174 BPM sub-bass cyan, industrial audio meter progress bars. |

## Living Soot Sprites Engine (`soot-sprites.js`)

An authentic Studio Ghibli procedural Canvas 2D animation engine running strictly when `data-theme-preset="ghibli"`:
- **10 Canonical Facial Expressions**: Evaluated against reference art (`cute`, `what?`, `scared`, `gross`, `normal`, `annoyed`, `mad`, `skeptical`, `confused`, `hal 9000`).
- **Multi-Layered Powdery Fuzz**: 42 outer feathered bristles and 34 mid fluff tufts with a dense obsidian core, replacing rigid polygon spikes.
- **Luminous Kompeitō Star Candies**: Multi-stage radial bloom glow across 5 pastel shades (cyan, yellow, pink, mint, diamond white) with ambient floor light reflections and twinkling diamond sparkles.
- **Dynamic AI Scurry Loop**: Sprites detect uncollected floor candies, scurry toward them with bipedal footsteps, pick them up, and triumphantly celebrate overhead with smiling eyes (`^^`) and rosy cheek blushes.
- **Theme Isolation**: Completely detaches with 0% CPU/GPU overhead when switching to non-Ghibli presets.

## Related

- [[homelab]] — fleet architecture and host topology
- [[litellm-proxy]] — model routing proxy powering dashboard AI agents
- [[claude-code]] — primary development engine for homelab tooling

---
title: Immich Photos
summary: "High-performance self-hosted photo and video management platform running on Proxmox P330 with dedicated NVMe storage and Agentic OS integration."
tags: [immich, photos, proxmox, media, storage, agent-os]
---

# Immich Photos

> High-performance self-hosted photo and video management platform serving as a private Google Photos alternative with timeline browsing, album management, and native mobile client sync.

**Deployment**: Proxmox P330 LXC (CT 101, unprivileged, CPU mode)  
**Port**: `2283`  
**Storage**: Dedicated 2TB SSD storage pool on Lenovo P330  
**Status**: Monitored via Gatus (`p330-services/immich`) and Agentic OS telemetry  

## Overview

Immich is deployed as a lightweight LXC container on the Proxmox P330 host to provide fast photo and video backup, timeline browsing, and media indexing. Machine learning acceleration was explicitly set to CPU mode during installation to guarantee long-term stability on host hardware without dedicated GPU passthrough requirements.

## Agentic OS Cockpit Integration

Immich is fully integrated into the Agentic OS ecosystem:
1. **Catalog Registration**: Defined as a link service in `server.py` and `panel-server.py` (`SERVICES["immich"]`).
2. **Dashboard Command Centre**: Seeded in `command-centre/dashboard.json` under Code Projects with health probes and local docs.
3. **Sidebar & Console**: Dedicated navigation item in the Agentic OS sidebar with custom camera SVG telemetry and responsive embedded iframe console (`#page-immich`).

## Related

- [[agentic-os]] — Developer cockpit embedding the Immich console frame
- [[proxmox]] — Virtualization host running container CT 101

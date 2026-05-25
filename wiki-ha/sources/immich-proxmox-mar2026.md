---
title: Immich Install on Proxmox LXC (Mar 2026)
summary: "Immich install via Proxmox community helper scripts: correct curl command, common failure modes (silent install fail, ML startup delay 30-60min), default port 2283, no pre-set credentials."
tags: [immich, proxmox, lxc, photos, self-hosting]
source-type: claude-ai-export
export-id: b7ae9ea3
conversation: "Installing Immich on Proxmox"
date: 2026-03-02
---

# Immich Install on Proxmox LXC (Mar 2026)

> Source: Claude.ai export `b7ae9ea3`, conversation "Installing Immich on Proxmox" (250 msgs, 2026-03-02). Covers the full install process including common failure modes.

## Install Command

Run from **Proxmox node shell** (not inside a container):

```bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/community-scripts/ProxmoxVE/main/ct/immich.sh)"
```

**Common error with wrong command:**
```
bash: -c: line 1: syntax error near unexpected token `<'
```
Cause: HTML returned instead of script — used wget or wrong URL. Fix: use the curl command above with the raw GitHub URL.

## Post-Install Access

- URL: `http://<LXC-IP>:2283`
- Find LXC IP: Proxmox web UI → container → Summary tab
- **No pre-set credentials** — first launch shows "Getting Started" setup screen to create admin account

## Common Failure Modes

### 1. Machine Learning Startup Delay (Most Common)
Immich's ML and photo processing libraries compile/initialize on first boot:
- Takes **30–60 minutes** depending on hardware
- Port 2283 appears unresponsive during this time
- **Don't restart or delete the container** — check if it's still working:

```bash
top            # look for node, python processes using CPU
ps aux | grep -i immich
```

### 2. Silent Install Failure
If nothing is running after 60+ minutes:
- Check: `find / -name "immich" 2>/dev/null`
- If empty: destroy LXC and re-run install script

### 3. LXC Console Login Confusion
The Proxmox LXC console login prompt is the **Linux root shell**, not Immich.
- Default credentials: `root` / `root` (or printed at end of install script)
- If incorrect: reset from Proxmox host shell: `pct exec <CTID> -- passwd root`

### 4. Immich Not Running as systemd Service
The community script does not install Immich as a systemd service.
- `systemctl status immich` → "Unit immich.service could not be found" is normal
- Check status via: `docker ps` or look in `/opt/immich`

## Architecture Note
Community helper script installs Immich in LXC (not VM). No Docker daemon visible from inside — script manages the stack directly. Files typically in `/opt/immich` or `/var/lib/`.

## Links

- [[proxmox-build-feb2026]] — base Proxmox build
- [[proxmox-dns-network-mar2026]] — prerequisite: network must work before install

---
title: Proxmox Build — Feb 2026 (Lenovo Hardware)
summary: "418-msg Proxmox fresh install session Feb 2026: hostname config, DNS fix, Nextcloud AIO on Alpine LXC (failed), TurnKey VM approach (success), Docker install, Nextcloud Memories PHP issue."
tags: [proxmox, nextcloud, docker, lenovo, self-hosting]
source-type: claude-ai-export
export-id: b7ae9ea3
conversation: "Home Assistant Proxmox Build Feb 2026"
date: 2026-02-28
---

# Proxmox Build — Feb 2026 (Lenovo Hardware)

> Source: Claude.ai export `b7ae9ea3`, conversation "Home Assistant Proxmox Build Feb 2026" (418 msgs, 2026-02-28). Extended build session covering Proxmox install, DNS/network fixes, multiple Nextcloud install attempts, final TurnKey VM success.

## Proxmox Initial Setup

### Hostname Config
- Format: `proxmox.local` or `pve.home.lan` (FQDN expected)
- Default subnet may not match home network — may need manual edit of `/etc/network/interfaces`

### DNS Fix (Critical First Step)
Default nameserver `127.0.0.1` has no local DNS resolver → breaks all domain resolution.

Fix:
```bash
nano /etc/resolv.conf
# Change: nameserver 127.0.0.1
# To: nameserver 192.168.0.1  (or your router IP)
```

Alternatively set DNS in Proxmox web UI under System → Network.

## Nextcloud Install — Attempts and Outcome

### Attempt 1: Alpine LXC (FAILED)
- Used Proxmox community helper scripts
- Alpine LXC missing PHP functions — `proc_open()` required by Nextcloud Memories app
- Fix attempt: `pct exec 102 -- apk add php83-pcntl` → partial, still broke

**Root cause**: Alpine LXC has a stripped PHP build missing `pcntl` extension. Nextcloud Memories requires it.

**Lesson**: Alpine LXC not suitable for Nextcloud with AI/Memories features.

### Attempt 2: Debian LXC with Docker (PARTIAL)
- Debian 12's packaged Docker is outdated for Nextcloud AIO
- Fix: remove distro docker, install direct from Docker:

```bash
apt remove -y docker.io
curl -fsSL https://get.docker.com | sh
```

- Hit TurnKey boot loop issue (see below)

### Attempt 3: TurnKey Nextcloud VM (SUCCESS)
- TurnKey Linux Nextcloud VM image — includes PHP with all required extensions
- **Critical gotcha**: CD/DVD drive left attached → VM boots from ISO, causes boot loop
  - Fix: In Proxmox web UI → Hardware → CD/DVD Drive → Remove (or set boot order: HDD first)
  - Must do this **before** first start
- Once booted correctly: Free SSL certificate option in advanced configuration

## Storage Scaling Issue
- 32GB default fills quickly with phone photos
- Check disk usage: `df -h`
- Resize: Proxmox → VM → Hardware → resize disk, then extend filesystem inside VM

Symptom encountered:
```
/dev/mapper/turnkey-root   25G   23G   38M 100%
```

## Community Helper Scripts

Correct install command (not wget, use curl with raw script URL):
```bash
bash -c "$(curl -fsSL <raw-script-url>)"
```

Common error with wrong command: `bash: -c: line 1: syntax error near unexpected token '<'` — means HTML returned instead of script (wrong URL format).

## Proxmox Entities

- Hardware: Lenovo (specific model not documented)
- Network: 192.168.0.x subnet
- Container IDs used: 102 (Nextcloud LXC attempt)

## Links

- [[proxmox-dns-network-mar2026]] — DNS and routing troubleshooting session
- [[nextcloud-lenovo-mar2026]] — Follow-up Nextcloud fresh install
- [[immich-proxmox-mar2026]] — Immich install on same Proxmox

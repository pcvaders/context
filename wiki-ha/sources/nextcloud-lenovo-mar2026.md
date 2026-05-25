---
title: Nextcloud Fresh Install on Lenovo Proxmox (Mar 2026)
summary: "143-msg Nextcloud TurnKey VM install session: correct disk/storage settings, boot order gotcha, LVM setup, GRUB install, TurnKey wizard flow, finding VM IP."
tags: [nextcloud, proxmox, turnkey, lenovo, self-hosting]
source-type: claude-ai-export
export-id: b7ae9ea3
conversation: "Nextcloud fresh install on Lenovo"
date: 2026-03-12
---

# Nextcloud Fresh Install on Lenovo Proxmox (Mar 2026)

> Source: Claude.ai export `b7ae9ea3`, conversation "Nextcloud fresh install on Lenovo" (143 msgs, 2026-03-12). Uses TurnKey VM approach (not Alpine LXC — see [[proxmox-build-feb2026]] for why Alpine failed).

## Why TurnKey VM (Not Alpine LXC)

Previous Alpine LXC attempt failed: missing `proc_open()` PHP function, breaks Nextcloud Memories app. TurnKey Nextcloud VM image includes correct PHP build with all required extensions.

## VM Creation Settings

| Setting | Value |
|---|---|
| Disk size | 200GB+ (32GB fills fast with photos) |
| **Storage** | **local-lvm** (NOT local — local is for ISOs only) |
| Boot order | **Hard Disk FIRST, CD/DVD second** |

**Critical**: Set boot order before first start. If CD/DVD boots first → TurnKey install loop. Fix: Hardware → CD/DVD Drive → Remove (or reorder in Options → Boot Order).

## ISO Download

From Proxmox shell:
```bash
wget -P /var/lib/vz/template/iso/ \
  http://mirror.turnkeylinux.org/turnkeylinux/images/iso/turnkey-nextcloud-18.1-bookworm-amd64.iso
```

Verify: `ls /var/lib/vz/template/iso/`

## Install Wizard Flow

1. **Disk partitioning**: Choose **"Guided, use entire disk and set up LVM"** (option 1)
   - Required for later disk expansion (`pvresize` + `lvextend`)
2. **Write changes to disk and configure LVM**: Yes
3. **Install GRUB to master boot record**: Yes
4. **Reboot**: Enter

### Post-Reboot — Remove ISO
After first reboot: "Please remove the live medium then press Enter"
- In Proxmox web UI: Hardware → CD/DVD Drive → Remove
- Then press Enter in console

### TurnKey Setup Wizard
- Set root password (strong, store safely)
- Domain: use VM's local IP (find via router admin at 192.168.0.1 → DHCP leases)
- **Skip all TurnKey Hub / API key prompts** — optional paid services, not needed
- Finding VM IP: router DHCP leases, or Proxmox web UI → VM → Summary tab

## Finding VM IP

If not shown in Proxmox Summary tab:
1. Router admin → connected devices / DHCP leases
2. `qm list` in Proxmox shell to get VM ID
3. Look for "nextcloud" or "turnkey" hostname in router

VM ID in this session: 102

## Nextcloud Access

After TurnKey setup completes:
- Web UI: `https://<VM-IP>` (TurnKey sets up SSL)
- Admin credentials set during TurnKey wizard

## Disk Expansion (When 100% Full)

TurnKey uses LVM internally — expansion is:
1. Proxmox: increase virtual disk (Hardware → Hard Disk → Resize)
2. Inside VM: `pvresize /dev/sda` + `lvextend -l +100%FREE /dev/turnkey/root` + `resize2fs`

## Links

- [[proxmox-build-feb2026]] — original build, explains why TurnKey (not Alpine)
- [[proxmox-dns-network-mar2026]] — network must work before install

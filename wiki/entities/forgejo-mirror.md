---
title: Forgejo GitHub Mirror
type: entity
tags: [homelab, proxmox, forgejo, git, backup, self-hosted]
created: 2026-06-20
---

> Self-hosted Forgejo on Proxmox LXC 106 that mirrors both GitHub accounts, cross-mirrors them, and pushes offsite to Google Drive — four independent copies of every repo. LAN-only. (as of 2026-06)

## Status

**Code DONE + committed** (12 scripts lint-clean). Not yet installed on host — needs credentials in macOS Keychain, then `bash install.sh`. Designed 2026-06-02, revisited 2026-06-12 session. [unsourced: exact install-run date — never executed as of 2026-06-20]

## Why it exists

A GitHub suspension (Spotify creds leak, 2026-06-01) nearly halted work. This guarantees a GitHub takedown never blocks development — repos survive in Forgejo + Drive independently.

## Locations

- **Project:** `~/projects/forgejo-mirror/`
- **Canonical spec:** `~/projects/docs/superpowers/specs/2026-06-02-forgejo-github-mirror-design.md`
- **Runbook:** `~/projects/forgejo-mirror/README.md`
- **Security checklist:** `~/projects/forgejo-mirror/CLAUDE.md`

## Target infra

- **Host:** Proxmox 9.1.7 @ `192.168.0.46` (ThinkStation P330 Tiny, i7-8700T, 32GB) <!-- secret-scan-ok -->
- **Container:** unprivileged LXC **106** "forgejo", static `192.168.0.106/24`, 2c / 2GB / 20GB on local-lvm <!-- secret-scan-ok -->
- **Forgejo + SQLite**, web `:3000`, git-ssh `:222` <!-- secret-scan-ok -->
- **Accounts mirrored:** pcgamesplay1 + pcvaders (cross-mirror each other)
- **Offsite:** rclone → pcvaders Google Drive (`forgejo dump`, keep last 2, 13GB guard)

## Two install modes (per preflight.sh)

- **Full-mirror:** both GitHub PATs present in keychain → mirrors + cross-mirrors GitHub.
- **PRIMARY (standalone):** PATs absent → Forgejo runs as primary git host, no GitHub mirror. Only `forgejo-admin` secret required to install. (Designed this way because GitHub suspension can make PAT creation impossible.)

## Secrets (macOS Keychain only — never in chat/scripts/git)

| Service | Required? |
|---|---|
| `forgejo-admin` | YES (always) |
| `forgejo-github-pcgamesplay1`, `forgejo-github-pcvaders` | optional → enables full-mirror mode |
| `forgejo-telegram-token`, `forgejo-telegram-chatid` | for disk alarms |
| `rclone-gdrive-pcvaders` | for offsite Drive push |
| SSH key `~/.ssh/forgejo_proxmox` | YES (host access) | <!-- secret-scan-ok -->

## Install phases (`install.sh`, idempotent)

preflight → create LXC 106 → bootstrap (pkgs + forgejo user) → install Forgejo (binary + systemd) → push secrets (0600, owned forgejo) → deploy scripts + cron.

## Cron (inside CT 106 once live)

| Script | Schedule |
|---|---|
| `forgejo-sync.sh` | every 8h at :15 |
| `disk-alarm.sh` | every 15 min (Telegram) |
| `github-backup-run.sh` | daily 03:30 |
| `drive-push.sh` | daily 04:00 |

## Security controls

LAN-only (no port-forward, cloudflared CT 104 must NOT tunnel :3000) · admin TOTP · registration disabled · PAT scope `repo` only · unprivileged LXC · SSH key-only · quarterly restore drill. <!-- secret-scan-ok -->

## Related

- [[proxmox]] [[homelab]] [[feedback_secret_handling]]
- Sibling redundancy: GitHub pcgamesplay1 + pcvaders + Drive dump.

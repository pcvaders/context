---
title: Forgejo GitHub Mirror
type: entity
tags: [homelab, proxmox, forgejo, git, backup, self-hosted]
created: 2026-06-20
---

> Self-hosted Forgejo on Proxmox LXC 106 that mirrors both GitHub accounts, cross-mirrors them, and pushes offsite to Google Drive — four independent copies of every repo. LAN-only. (as of 2026-06)

## Status

**LIVE since 2026-06-14** — built via `install.sh` on Proxmox LXC 106 and running as the PRIMARY git host (admin user `voyager1`; orgs `personal` + `ai`; daily 04:00 `forgejo-dump` → Google Drive). Verified 2026-09-18: `GET /api/v1/version` → `15.0.3+gitea-1.22.0`; `~/claude-skills` pushes to it. Source: `homelab-brain/memory/mac-m3/project_forgejo_mirror.md`. (Earlier text here said "not yet installed … never executed as of 2026-06-20" — wrong since 2026-06-14.)

## Why it exists

A GitHub suspension (Spotify creds leak, 2026-06-01) nearly halted work. This guarantees a GitHub takedown never blocks development — repos survive in Forgejo + Drive independently.

## Locations

- **Project:** `~/projects/forgejo-mirror/`
- **Canonical spec:** `~/projects/docs/superpowers/specs/2026-06-02-forgejo-github-mirror-design.md`
- **Runbook:** `~/projects/forgejo-mirror/README.md`
- **Security checklist:** `~/projects/forgejo-mirror/CLAUDE.md`

## Target infra

- **Host:** Proxmox 9.1.7 @ `<lan-ip>` (ThinkStation P330 Tiny, i7-8700T, 32GB) <!-- secret-scan-ok -->
- **Container:** unprivileged LXC **106** "forgejo", static `<lan-ip>/24`, 2c / 2GB / 20GB on local-lvm <!-- secret-scan-ok -->
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

## Client setup (per machine)

Credentials are **per machine** — macOS Keychain entries do not travel. Every new client is provisioned on its own. Runbook Sections 9-10 in `~/projects/forgejo-mirror/README.md`.

**Pick the account before touching credentials.** Agents authenticate as `agentuser` over HTTP + a per-machine token (no SSH key — the agent-setup runbook excludes SSH from that account). Only a machine where *voyager1* personally pushes gets an SSH key. <!-- secret-scan-ok -->

- **Mac** — voyager1 SSH key registered; pushes `<lan-ssh-remote>`. <!-- secret-scan-ok -->
- **Windows (win11-cl)** — provisioned 2026-09-11 after this recurred: the runbook had been Mac-only, so every attempt from the PC restarted from scratch.

Verify a registered key from anywhere, no auth needed: `curl http://<lan-ip>:3000/<user>.keys`.

Org naming misleads — **`personal` is not personal content**; it holds the `~/projects` monorepo. Actually-private repos are `voyager1/Personal-Skills` and `personal/reachy_mini_radio_open`. Unauthenticated requests 404 across the board.

**Open finding (2026-09-11):** `/Users/agentuser/projects/.git/config` is mode 644 with a write-capable token in the remote URL. `chmod 600`, and move the credential into a helper. Token scopes are per-capability, not per-repo — the per-project limit comes from team grants, so adding a grant silently widens every existing token.

## Related

- [[proxmox]] [[homelab]] [[feedback_secret_handling]]
- Sibling redundancy: GitHub pcgamesplay1 + pcvaders + Drive dump.

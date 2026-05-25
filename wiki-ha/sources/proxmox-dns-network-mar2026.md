---
title: Proxmox DNS and Network Troubleshooting (Mar 2026)
summary: "176-msg session diagnosing Proxmox network failure: 'Destination Host Unreachable' = routing/gateway problem not DNS; default gateway missing from /etc/network/interfaces."
tags: [proxmox, dns, networking, troubleshooting]
source-type: claude-ai-export
export-id: b7ae9ea3
conversation: "Proxmox DNS and network connectivity issues"
date: 2026-03-06
---

# Proxmox DNS and Network Troubleshooting (Mar 2026)

> Source: Claude.ai export `b7ae9ea3`, conversation "Proxmox DNS and network connectivity issues" (176 msgs, 2026-03-06). Fresh Proxmox install to isolate why community helper scripts weren't working — hit DNS/routing issues in the process.

## Symptom

```
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
From 192.168.0.102 icmp_seq=1 Destination Host Unreachable
```

## Root Cause

**"Destination Host Unreachable" from your own IP = routing/gateway problem, NOT DNS.**

The error `From 192.168.0.102` means the machine itself cannot route the packet. DNS was a red herring — packets never leave the machine.

Diagnosis:
```bash
ip route
cat /etc/network/interfaces
```

Expected finding: default gateway missing or misconfigured in `/etc/network/interfaces`.

## Fix

In `/etc/network/interfaces`, ensure default gateway is set:

```
auto vmbr0
iface vmbr0 inet static
    address 192.168.0.102/24
    gateway 192.168.0.1       # ← this line must exist
    bridge-ports eno1
    bridge-stp off
    bridge-fd 0
```

After editing, apply:
```bash
systemctl restart networking
# or
ifdown vmbr0 && ifup vmbr0
```

## DNS Setting

Changed from `127.0.0.1` (local resolver, nothing running) to `8.8.8.8`:

```bash
nano /etc/resolv.conf
# nameserver 8.8.8.8
```

Or use router IP (`192.168.0.1`) — both work once routing is fixed.

## Diagnostic Order for Proxmox Network Issues

1. `ip route` — check default gateway exists
2. `cat /etc/network/interfaces` — check gateway line in bridge config
3. `ping 192.168.0.1` (router) — test layer 3 connectivity
4. `ping 8.8.8.8` — test external routing
5. `ping google.com` — test DNS (only after 4 passes)

Don't jump to DNS fixes if ping to IP also fails — the gateway is the problem.

## Context

This session was a fresh install specifically to isolate why Proxmox community helper scripts weren't working. The network issue was a prerequisite blocker — helper scripts need internet access.

## Links

- [[proxmox-build-feb2026]] — original build session
- [[nextcloud-lenovo-mar2026]] — Nextcloud install after network fixed

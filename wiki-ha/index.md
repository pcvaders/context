# Home Assistant Wiki — Index

> Knowledge base for voyager1's Home Assistant setup: Proxmox host, Zigbee2MQTT, Aqara sensors, MCP integration, PIR automations, Brighton UK.

## Setup

- **Host**: Proxmox VM, Brighton UK
- **External access**: Cloudflare Zero Trust tunnel
- **Zigbee**: Sonoff Zigbee dongle → Zigbee2MQTT + ZHA
- **MQTT**: Mosquitto broker
- **Claude integration**: ha-mcp via Claude Desktop MCP connector (as of 2026-05)

## Concepts

| Page | Summary |
|---|---|
| [[zigbee]] | Zigbee protocol, Zigbee2MQTT vs ZHA, USB port mapping |
| [[mqtt]] | MQTT broker setup, migration issues |
| [[pir-automation]] | PIR motion sensor automation patterns across floors |
| [[presence-detection]] | Occupancy vs motion, delays, Aqara quirks |
| [[cloudflare-tunnel]] | Cloudflare Zero Trust tunnel for external HA access |

## Entities

| Page | Summary |
|---|---|
| [[ha-instance]] | Home Assistant instance details — Proxmox, version, integrations |
| [[ha-mcp]] | ha-mcp GitHub integration connecting Claude Desktop to HA |
| [[aqara-sensors]] | Aqara PIR and presence sensors across floors |
| [[sonoff-zigbee-dongle]] | Sonoff Zigbee USB dongle — port mapping after migration |
| [[proxmox-host]] | Proxmox server hardware — Lenovo M70Q Tiny I7 |

## Sources

| Page | Summary |
|---|---|
| [[ha-mcp-setup]] | 126-msg session: ha-mcp integration through Cloudflare Zero Trust |
| [[zigbee-migration]] | 109-msg session: Sonoff Zigbee port remapping after NVMe/SSD migration |
| [[automation-building-mcp]] | 207-msg extended automation session via MCP tools |
| [[aqara-pir-setup]] | Aqara motion sensor setup + PIR automation patterns |
| [[mqtt-migration-fix]] | MQTT broker fix after Lenovo hardware migration |
| [[pir-corridor-troubleshooting-23]] | Session 23: illuminance OR condition fix, Sonoff SNZB-06P add |
| [[pir-lights-issue-25]] | Session 25: all-sensors-off wait fix, ghost detection |
| [[pir-lights-troubleshooting-26]] | Session 26: 4-sensor expansion, disabled automation diagnosis |
| [[proxmox-build-feb2026]] | Feb 2026 Proxmox install: DNS fix, Alpine LXC failure, TurnKey VM Nextcloud success |
| [[proxmox-dns-network-mar2026]] | Mar 2026 DNS/routing debug: "Destination Host Unreachable" = gateway not DNS |
| [[immich-proxmox-mar2026]] | Immich LXC install: correct curl command, ML startup delay, no pre-set credentials |
| [[nextcloud-lenovo-mar2026]] | Nextcloud TurnKey VM install: local-lvm disk, boot order, LVM setup, disk expansion |
| [[aqara-occupancy-delay-mar2026]] | Aqara occupancy 15-min delay: ZHA write-back bug, Z2M migration plan, HA UI stale entity ref gotcha |

---

Last updated: 2026-05-25

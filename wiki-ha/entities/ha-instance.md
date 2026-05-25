# Home Assistant Instance

> voyager1's Home Assistant installation — Proxmox VM, Brighton UK, Zigbee2MQTT + ZHA, Cloudflare tunnel, MCP-connected to Claude Desktop.

## Hardware

- **Host**: Lenovo M70Q Tiny I7 (upgraded from M70Q Gen2 after NVMe/SSD migration)
- **Virtualisation**: Proxmox
- **Location**: Brighton, UK
- **Storage**: NVMe (OS) + SSD (data) — both migrated from previous hardware

## Software stack

| Component | Details |
|---|---|
| Home Assistant | Running in Proxmox VM |
| Zigbee2MQTT | Primary Zigbee coordinator |
| ZHA | Secondary Zigbee integration |
| Mosquitto | MQTT broker |
| Cloudflare Zero Trust | External tunnel (no open ports) |
| ha-mcp | Claude Desktop MCP connector |

## Integrations active (as of 2026-05)

- Zigbee (Sonoff dongle via Zigbee2MQTT + ZHA)
- MQTT (Mosquitto)
- Aqara sensors (PIR, presence, temperature)
- ha-mcp (Claude AI integration)
- Home Assistant Companion App (iPhone 12 Pro Max)

## Floor layout

- Ground floor — PIR automations, presence detection
- First floor corridor — PIR lights automation
- Living room — lamp + PIR + presence control

## Related

- [[proxmox-host]] — host hardware
- [[ha-mcp]] — Claude integration
- [[zigbee]] — Zigbee stack
- [[aqara-sensors]] — sensor hardware

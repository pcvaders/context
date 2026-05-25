# ha-mcp

> GitHub integration connecting Claude Desktop to Home Assistant via MCP, enabling Claude to read sensors, trigger automations, and query HA state in real time.

**Repo**: https://github.com/homeassistant-ai/ha-mcp  
**Protocol**: MCP (Model Context Protocol)  
**Client**: Claude Desktop  
**Status**: Active (as of 2026-05)

## What it does

ha-mcp exposes Home Assistant's REST API as MCP tools. Claude Desktop connects as an MCP client and can:
- Read entity states (sensors, lights, switches)
- Call HA services (turn on/off, trigger automations)
- Query history and attributes
- Build and modify automations via natural language

## Setup path (voyager1)

The setup required threading through 3 systems:

1. **Cloudflare Zero Trust tunnel** — exposes HA externally without opening ports
2. **HA HTTP integration config** — must set `use_x_forwarded_for` + trusted proxy IPs for Cloudflare
3. **Claude Desktop MCP connector** — add ha-mcp server pointing to tunnel URL + HA long-lived token

### Key config in `configuration.yaml`

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - <cloudflare-ip-ranges>
```

## Troubleshooting patterns

- **401 errors** — HA long-lived token expired or incorrect in Claude Desktop config
- **CORS errors** — HA HTTP config missing trusted proxy entries
- **Tunnel not routing** — Cloudflare Zero Trust application not whitelisting the MCP path

## Related

- [[cloudflare-tunnel]] — external access layer
- [[ha-instance]] — the HA being connected
- [[ha-mcp-setup]] — full setup session source


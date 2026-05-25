# ha-mcp Setup Session

> 126-message troubleshooting session successfully connecting Claude Desktop to Home Assistant via ha-mcp through a Cloudflare Zero Trust tunnel.

**Date**: 2026-03-24  
**Duration**: 126 messages  
**Outcome**: ✅ ha-mcp fully operational

## What was solved

Three-layer integration requiring simultaneous correct config across all layers:

1. **Cloudflare Zero Trust** — tunnel created, HA application defined
2. **HA HTTP config** — `use_x_forwarded_for` + Cloudflare trusted proxy IPs added
3. **Claude Desktop** — ha-mcp server added to `claude_desktop_config.json` with tunnel URL + HA long-lived token

Any one layer wrong causes silent failure or auth errors.

## Key debugging patterns

- Test HA accessibility through tunnel URL in browser before adding to Claude Desktop
- Verify long-lived token by calling HA API directly: `curl -H "Authorization: Bearer <token>" https://<tunnel-url>/api/`
- Check HA logs for `ip_ban` entries — Cloudflare IPs getting banned due to missing trusted proxy config

## Working config structure

```json
{
  "mcpServers": {
    "homeassistant": {
      "command": "npx",
      "args": ["-y", "ha-mcp"],
      "env": {
        "HA_URL": "https://<your-tunnel>.trycloudflare.com",
        "HA_TOKEN": "<long-lived-token>"
      }
    }
  }
}
```

## Related

- [[ha-mcp]] — entity page for ha-mcp
- [[cloudflare-tunnel]] — tunnel setup details
- [[ha-instance]] — target HA installation

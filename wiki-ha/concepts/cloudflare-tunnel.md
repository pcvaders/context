# Cloudflare Zero Trust Tunnel

> External access to Home Assistant without opening firewall ports — required for ha-mcp remote connectivity from Claude Desktop.

## Why Cloudflare tunnel

- No port forwarding on home router
- TLS termination at Cloudflare edge
- Access control via Cloudflare Access policies
- Required for ha-mcp when Claude Desktop is not on local network

## Setup components

1. **cloudflared** daemon — runs on Proxmox host, creates outbound tunnel
2. **Cloudflare Zero Trust** dashboard — defines tunnel + application
3. **HA HTTP config** — must trust Cloudflare proxy IPs

## Critical HA config for tunnelled access

Without this, HA rejects requests forwarded through Cloudflare:

```yaml
# configuration.yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 173.245.48.0/20
    - 103.21.244.0/22
    - 103.22.200.0/22
    - 103.31.4.0/22
    - 141.101.64.0/18
    - 108.162.192.0/18
    - 190.93.240.0/20
    - 188.114.96.0/20
    - 197.234.240.0/22
    - 198.41.128.0/17
    - 162.158.0.0/15
    - 104.16.0.0/13
    - 104.24.0.0/14
    - 172.64.0.0/13
    - 131.0.72.0/22
```

## ha-mcp connection through tunnel

Claude Desktop → Cloudflare edge → cloudflared → HA  
HA long-lived token authenticates the MCP connection.

## Related

- [[ha-mcp]] — uses this tunnel
- [[ha-mcp-setup]] — setup session where tunnel was configured
- [[ha-instance]] — the HA being exposed

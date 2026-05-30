---
title: LiteLLM Proxy
summary: "Local OpenAI-compatible proxy on port 4000 routing calls to Ollama and cloud LLMs. Auto-starts via LaunchAgent."
tags: [llm, local, proxy, tooling]
---

# LiteLLM Proxy

> Local OpenAI-compatible proxy running on port 4000 — translates Anthropic/OpenAI API calls to local Ollama models and cloud LLMs.

**Binary**: `/opt/miniconda3/bin/litellm`  
**Config**: `~/.litellm/config.yaml`  
**Port**: 4000  
**Log**: `/tmp/litellm-proxy.log`  
**Auto-start**: `~/Library/LaunchAgents/com.voyager1.litellm-proxy.plist`

## Admin UI

URL: `http://localhost:4000/ui`  
Username: `admin`  
Password: _(redacted — see private `voyager-hub`; rotated 2026-05-30)_ <!-- secret-scan-ok: redacted, rotated -->

Credentials set via `ui_username`/`ui_password` in `general_settings` — not DB auth. LiteLLM proxy requires PostgreSQL for DB-backed auth; SQLite not supported (Prisma schema missing). `ui_username`/`ui_password` bypasses DB requirement entirely.

## API Access

```bash
curl http://localhost:4000/v1/models \
  -H "Authorization: Bearer $LITELLM_KEY"   # value in private voyager-hub, not here
```

## Models (as of 2026-05)

| Model ID | Backend |
|---|---|
| `qwen3-coder:480b-cloud` | Cloud |
| `qwen3-coder:30b` | Ollama (local) |
| `hermes3` | Ollama (local) |
| `gemma4:31b-cloud` | Cloud |

## Health check

Use `/v1/models` not `/health` — Python `urllib` hangs on `/health` endpoint (curl works, urllib times out). `/v1/models` responds correctly to all clients.

## Use case

Routes API calls when Anthropic credits depleted. Candidate for `ANTHROPIC_BASE_URL` redirect to run `claude-press` against local/cloud models without Anthropic billing.

## SwiftBar integration

LiteLLM status shown in combined dashboard (`wiki-status.30s.py`):
- Green dot = proxy running
- Start/Stop/View Logs from menu bar

## Related

- [[claude-code]] — primary client
- [[agent-native-cli]] — `claude-press` depends on API availability

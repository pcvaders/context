---
title: DeepSeek Harness
summary: "Local AI inference and orchestration harness running on port 3080 routing DeepSeek reasoning and coding models."
tags: [deepseek, harness, local-ai, llm, proxy]
---

# DeepSeek Harness

> Dedicated inference wrapper and agent harness on port 3080 routing DeepSeek models (R1 reasoning, V3 code) across local hardware and cloud backends.

**Port**: 3080  
**Health Check**: `http://127.0.0.1:3080/` (monitored in `check_server_health.py`)  
**Backends**: Local Ollama / MLX runtimes, Google Cloud Vertex AI, and direct provider endpoints  
**Session References**: Session 089 (gap port audit), Session 090 (Vertex environment and fire-alarm chatlog repair)

## Core Capabilities

1. **Model Routing**: Directs coding and analytical queries to DeepSeek reasoning models without third-party aggregator latency.
2. **Health Monitoring**: Integrated into homelab health surface and pre/post deployment verification checks.
3. **Vertex AI Failover**: Configured with automated cloud fallback when local Apple Silicon VRAM is constrained.

## Related

- [[litellm-proxy]] — sibling OpenAI-compatible proxy on port 4000
- [[homelab]] — core services registry
- [[claude-code]] — primary development client

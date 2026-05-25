> Techniques that reduce LLM output token count while preserving technical accuracy — cutting cost, latency, and context pressure.

# Token Compression

## Definition

Token compression refers to any technique that reduces the number of tokens an LLM generates in response without degrading the usefulness of the output. Distinct from input compression (reducing context size) and quantization (compressing model weights).

## Why it matters

- **Cost** — output tokens billed at 3-5x input rate on most providers
- **Latency** — fewer tokens = faster response
- **Context pressure** — in agentic loops, agent output is re-injected as context. Verbose agents exhaust context windows faster
- **Quality** — brevity constraints can *improve* accuracy: a March 2026 paper found 26-point accuracy gains on certain benchmarks when large models were constrained to brief responses [Source: arxiv.org/abs/2604.00025]

## Approaches

### Prompt-level (skill-based)
Install a skill file that instructs the agent to drop filler, use fragments, avoid hedging. No model change needed.
- Example: [[caveman-julius-brussee]] — ~65% average reduction

### Memory-file compression
Rewrite persistent context files (CLAUDE.md, project notes) into terse format. Saves input tokens every session.
- Example: `caveman-compress` sub-skill — ~46% input token reduction on memory files

### MCP middleware compression
Wrap MCP servers with a middleware layer that compresses tool descriptions before injection.
- Example: `caveman-shrink` — wraps any MCP server

### Fine-tuning
Train brevity into model weights directly. No per-session prompting needed.
- Example: `cavegemma` — Gemma 4 31B fine-tuned on caveman brevity pairs

### Subagent output compression
Use compressed-output subagents so tool results injected into main context are smaller.
- Example: `cavecrew-*` — ~60% smaller tool results vs vanilla subagents

## Tradeoffs

| Approach | Token type saved | Setup cost | Reversible |
|---|---|---|---|
| Skill/prompt | Output | Low | Yes (per session) |
| Memory compress | Input | Medium | Yes (backup kept) |
| MCP middleware | Input (tool descriptions) | Low | Yes |
| Fine-tuning | Output | High | No |
| Compressed subagents | Context (tool results) | Low | Yes |

## Key finding

Verbose ≠ accurate. Brevity constraints on large models correlate with accuracy gains on structured tasks. The compression is not lossy for technical content — only filler, hedging, and pleasantries are dropped.

## Related

- [[caveman-julius-brussee]], [[claude-code-skills]], [[rag]], [[llm-wiki]]

(as of 2026-05)

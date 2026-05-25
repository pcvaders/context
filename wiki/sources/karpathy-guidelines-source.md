# Karpathy Guidelines Plugin

> Claude Code plugin encoding Andrej Karpathy's 4 behavioral rules for LLM coding: think first, simplicity, surgical changes, goal-driven execution.

**URL**: https://github.com/forrestchang/andrej-karpathy-skills  
**Marketplace**: `karpathy-skills`  
**Version**: 1.0.0 (as of 2026-05)  
**Origin**: https://x.com/karpathy/status/2015883857489522876

## The 4 Rules

1. **Think Before Coding** — State assumptions explicitly. Surface confusion. Ask if unclear.
2. **Simplicity First** — Minimum code. No speculative features, abstractions, or unused flexibility.
3. **Surgical Changes** — Touch only what the request requires. Match existing style. Don't "improve" adjacent code.
4. **Goal-Driven Execution** — Define verifiable success criteria. Write tests first. Loop until verified.

## Installation

```bash
claude plugins marketplace add forrestchang/andrej-karpathy-skills
claude plugins install andrej-karpathy-skills@karpathy-skills
```

## Invocation

```
/andrej-karpathy-skills:karpathy-guidelines
```

## Related

- [[skill-ecosystem]] — Full skill marketplace map
- [[karpathy-andrej]] — Entity page for Andrej Karpathy
- [[claude-code-skills]] — Claude Code skill system

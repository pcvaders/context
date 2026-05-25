---
title: Skill Ecosystem
summary: "4-marketplace Claude Code skill stack: superpowers, antigravity, karpathy, caveman. How skills load, invoke, and interact."
tags: [skills, claude-code, methodology]
---

# Skill Ecosystem

> The 4-marketplace Claude Code skill stack installed for voyager1: superpowers (methodology), antigravity (1,431 community skills), karpathy (coding guidelines), caveman (token compression).

## What Are Skills

Claude Code skills are Markdown files with YAML frontmatter that inject behavior into Claude sessions. Invoked via `Skill` tool or `/skill-name` slash commands. Each skill loads only when called — zero overhead otherwise.

```yaml
---
name: skill-name
description: What it does
---
# Instructions Claude follows
```

## Installed Marketplaces

| Marketplace | Source | Skills | Purpose |
|---|---|---|---|
| `claude-plugins-official` | anthropics/claude-plugins-official | ~20 | Anthropic official methodology skills |
| `antigravity-awesome-skills` | PCGamesplay1/antigravity-awesome-skills | 1,431 | Community skills library, 37 bundles |
| `karpathy-skills` | forrestchang/andrej-karpathy-skills | 1 | Karpathy coding guidelines |
| `caveman` | JuliusBrussee/caveman | ~5 | Token compression + terse output |

## Installed Plugins (as of 2026-05)

| Plugin | Marketplace | Status |
|---|---|---|
| `superpowers` | claude-plugins-official | ✅ enabled |
| `antigravity-awesome-skills` | antigravity-awesome-skills | ✅ enabled |
| `andrej-karpathy-skills` | karpathy-skills | ✅ enabled |
| `caveman` | caveman | ✅ enabled |

## Skill Discovery Workflow

```
Task arrives
  → semantic_search wiki "skill for X"
  → find skill name in ecosystem
  → Skill tool invokes it
  → guidelines active for session
```

## Superpowers Skills (Methodology)

Core development workflow skills from Anthropic official:
- `superpowers:brainstorming` — Design before code
- `superpowers:writing-plans` — Implementation plans
- `superpowers:subagent-driven-development` — Delegate per-task to fresh subagents
- `superpowers:executing-plans` — Run plans inline
- `superpowers:test-driven-development` — TDD discipline
- `superpowers:systematic-debugging` — Debug before guessing
- `superpowers:finishing-a-development-branch` — Ship checklist
- `superpowers:using-git-worktrees` — Isolated workspaces
- `superpowers:requesting-code-review` / `receiving-code-review`
- `superpowers:writing-skills` — Prose quality

## Antigravity Key Bundles

See [[antigravity-awesome-skills]] for full list. Most relevant:

| Bundle | Use when |
|---|---|
| `antigravity-bundle-essentials` | Every session baseline |
| `antigravity-bundle-agent-architect` | Multi-agent system design |
| `antigravity-bundle-llm-application-developer` | Building LLM apps |
| `antigravity-bundle-full-stack-developer` | Web apps (front + back) |
| `antigravity-bundle-data-ai` | ML, embeddings, pipelines |
| `antigravity-bundle-devops-cloud` | CI/CD, containers |
| `antigravity-bundle-security-engineer` | Security architecture |
| `antigravity-bundle-qa-testing` | Test strategy, evals |

## Caveman Skills

Token compression suite — see [[token-compression]] and [[caveman-julius-brussee]]:
- `caveman:caveman` — 75% token reduction, terse output
- `caveman:cavecrew` — Subagent delegation (investigator / builder / reviewer)
- `caveman:caveman-stats` — Real token usage from session log
- `caveman:caveman-review` — Compressed PR review
- `caveman:caveman-commit` — Compressed commit messages

## Karpathy Guidelines

See [[karpathy-guidelines-source]]. Invoked via `/andrej-karpathy-skills:karpathy-guidelines`. Active every coding session.

## Adding New Marketplaces

```bash
claude plugins marketplace add owner/repo
claude plugins install plugin-name@marketplace-name
claude plugins list
```

## Related

- [[claude-code-skills]] — Claude Code skill system mechanics
- [[antigravity-awesome-skills]] — Antigravity source page
- [[karpathy-guidelines-source]] — Karpathy plugin source
- [[token-compression]] — Caveman compression concept
- [[skill-selection-guide]] — How to choose which skill to invoke
- [[litellm-proxy]] — Local LLM proxy used alongside skills

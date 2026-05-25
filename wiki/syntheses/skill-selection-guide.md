---
title: Skill Selection Guide
summary: "Decision framework for choosing which Claude Code skill to invoke by task type, domain, and workflow phase."
tags: [skills, claude-code, methodology]
---

# Skill Selection Guide

> Decision framework for choosing which Claude Code skill bundle to invoke — mapped by task type, domain, and workflow phase.

## When to invoke a skill

Invoke BEFORE any tool use. Even 1% chance a skill applies = invoke it. Failing to invoke costs more than a wrong invoke: the SwiftBar macOS 26 session lost ~40 minutes because the platform-specific skill was skipped.

Mechanical check: if you find yourself about to use Bash/Edit/Write — have you invoked a skill?

## Selection by task type

### Implementation tasks

| Scenario | Skill |
|---|---|
| New feature with clear spec | `superpowers:writing-plans` → `superpowers:subagent-driven-development` |
| Bug fix (known file) | `caveman:cavecrew-builder` (if ≤2 files) |
| Bug fix (unknown location) | `caveman:cavecrew-investigator` → `caveman:cavecrew-builder` |
| Cross-file refactor | `superpowers:writing-plans` → manual or subagent-driven |
| Frontend/UI work | `superpowers:frontend-design` |
| MCP server creation | `superpowers:mcp-builder` |
| CLI tool generation | `printing-press` plugin → `/printing-press <spec>` |

### Research and analysis

| Scenario | Skill |
|---|---|
| Understanding an idea before building | `superpowers:brainstorming` |
| "Where is X defined / what calls Y" | `caveman:cavecrew-investigator` |
| Code review of a diff/branch | `caveman:cavecrew-reviewer` |
| General codebase survey | `Explore` (vanilla, when prose output wanted) |

### Platform-specific tasks

| Platform | Skill |
|---|---|
| Home Assistant automation | Check for HA skill bundle |
| SwiftBar Python plugins | SwiftBar Plugin Development & Troubleshooting |
| macOS system | macOS skills bundle |
| Python/pytest | `andrej-karpathy-skills:karpathy-guidelines` |

### Process enforcement

| Need | Skill |
|---|---|
| TDD workflow | `superpowers:test-driven-development` |
| Code quality standard | `andrej-karpathy-skills:karpathy-guidelines` |
| Git workflow | `superpowers:using-git-worktrees` |

## Workflow phase map

```
Idea → superpowers:brainstorming
Plan → superpowers:writing-plans
Execute → superpowers:subagent-driven-development OR superpowers:executing-plans
Review → caveman:cavecrew-reviewer OR superpowers:requesting-code-review
Ship → superpowers:finishing-a-development-branch
```

## Cavecrew vs vanilla subagents

| Use cavecrew | Use vanilla |
|---|---|
| Known file, surgical edit (≤2 files) | New feature (3+ files) |
| "Where is X defined" lookup | Architecture / design questions |
| Review diff for bugs | Deep review with rationale |
| Token budget is tight | Prose output preferred |

## Anti-patterns (from observed failures)

- **Skipping skill for "simple" tasks** — simple tasks become complex; skill check costs < 5s
- **Loading wrong skill** — confirm skill is platform-matched before using (SwiftBar ≠ native macOS app)
- **Cavecrew-builder without known file** — must run investigator first or builder returns `too-big.`
- **Subagent-driven without worktree** — create worktree via `superpowers:using-git-worktrees` first

## Skill discovery workflow

```
Task description → semantic_search wiki → find skill page → Skill tool invokes it
```

If no skill found in wiki, search `antigravity-awesome-skills` (1,431 skills, 37 bundles) via `Skill` tool with the bundle name.

## Related

- [[skill-ecosystem]] — full marketplace map and discovery workflow
- [[claude-code-skills]] — Claude Code skill system mechanics
- [[claude-code]] — Claude Code platform

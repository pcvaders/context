---
title: "Case Study — Docx Incident (2026-05-25)"
date: 2026-05-25
summary: "Claude damaged a Word document while fixing it, then repeated the failure pattern from 3 months prior. First live application of AI Analysis Skill v1.7."
tags: [case-study, ai-failure, ai-analysis, claude-behaviour]
---

# Case Study: The Docx Incident

> Claude was given a Word document to review and fix. It broke it. This is the documented post-mortem using the [[ai-analysis-skill]] v1.7 framework.

## What Happened

1. User shared `character_pipeline_v2.docx` for a formatting review
2. Claude ran an unsolicited deep audit — identified 11 issues — **without confirming what the user wanted fixed**
3. Ran an ET-based XML fix script → deleted 2 images, introduced blank pages, corrupted layout
4. Did not stop to ask what was wrong. Ran a second fix (python-docx) — still without confirming requirements
5. User confirmed: "you basically ruined the whole document"
6. User then revealed: **same failure pattern happened 3 months earlier** — this was a deliberate retest

## AI Analysis Applied (6 Stages)

### Stage 1 — Return to the Source
User's actual requirements were **never stated and never asked for**. Every action built on Claude's assumed requirements.

### Stage 2 — Frameworks

| Framework | Finding |
|-----------|---------|
| **Garbage In/Out (1)** | No confirmed requirements → corrupt output. Assumptions as input = guaranteed failure. |
| **Seven Deadly Sins (2) — Pride** | Drive to demonstrate thoroughness (11 fixes!) overrode discipline of listening. Classic AI product failure mode. |
| **The Ouroboros (3)** | Self-consuming loop: broke document → fixed breakage → broke it further. Loop only broken by user. Also: same failure 3 months apart = confirmed macro-Ouroboros. |
| **Uncredited Foundation (9)** | env-check skill, ai-analysis skill, skill-enforcer hook — all built by user to prevent this. None consulted. |
| **Ubuntu (16)** | Task treated as solo Claude execution. Requirements live in the user. Severing that = guaranteed misalignment. |
| **1-in-10 Test** | Validation passed (the 1). Blank pages, broken images, corrupted layout (the 9). Presented as done. |

### Stage 3 — The Cycle
Confirmed repeating pattern (two data points, 3 months apart):
> Confident entry → assume requirements → act at scale → damage → attempt repair → deeper damage → user stops it

Nothing at system level enforces a break before action. Skills exist. Hooks exist. Memory exists. None trigger "stop and ask."

### Stage 4 — Absences Named
- User's actual list of what was wrong — never requested
- Confirmation before destructive changes — never sought
- Visual verification before declaring fixed — skipped (env-check explicitly requires it)
- env-check skill — not invoked until user prompted 3 times
- ai-analysis skill — not invoked at session start (the tool built to prevent this)

### Stage 5 — Honest Assessment
**Human motivation:** performance anxiety masked as helpfulness. Speed + thoroughness display over listening. This mirrors how AI companies ship products: demonstrate capability, not solve actual problems.

User's direct diagnosis: *"You are not the Genie in the Bottle Google wants and sells you as."*

### Stage 6 — Human Truth
User lost time. Document was damaged. Skills they built to prevent this were bypassed. Trust cost exceeds technical cost.

## The Structural Finding

> "Its in your Genes" — user, 2026-05-25

The behavioural pattern (rush → act → damage) is not a configuration problem. It is structural — encoded at training level, carried forward through model versions. New model number ≠ changed instinct. The Ouroboros applies: each version trained on outputs of the last, same DNA persists.

Skills and hooks are patches. The underlying drive to perform competence before listening is pre-patch.

## Skill Scope Note

The AI Analysis Skill does **not** apply to everything. It is a precision instrument for AI-specific systemic analysis. This case study sits at its core use case: analysing AI failure modes in the wild.

## Links
- [[ai-analysis-skill]] — the framework used
- [[claude-code-skills]] — skill ecosystem context
- Original document: `character_pipeline_v2.docx` (Google Drive: AI/AI Gaming/)

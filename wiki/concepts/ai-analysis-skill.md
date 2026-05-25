---
title: AI Analysis Skill v1.7
tags: [skill, ai, frameworks, analysis, high-priority]
priority: high
summary: "38-framework diagnostic tool for AI systemic analysis. First live use 2026-05-25 confirmed structural failure pattern in Claude."
created: 2026-05-24
updated: 2026-05-25
source: NotebookLM "My AI Skills" notebook
---

# AI Analysis Skill — Version 1.7

> A 38-framework diagnostic tool for evaluating AI systems, corporate behaviour, and systemic risk. Built from a 2026 dialogue between the user and Claude. First live use confirmed: 2026-05-25.

## Core Philosophy

Modern AI is defined by an "AI crisis" — systematic divorcing of information from original sources (stolen data, uncredited historical debts, abandoned safety pledges). This skill is a direct counter-measure.

## The Prime Directive

Everything must be traced to its original source. No summaries. No second-hand claims. Name the absence if a voice or source is missing.

## The 38 Frameworks (5 Categories)

| Category | Frameworks | Key Examples |
|----------|-----------|--------------|
| Systems & Cycles (1–7) | Foundational decay, human motivations, feedback loops | Garbage In/Out, Seven Deadly Sins, Ouroboros |
| Epistemological (8–10) | Missing knowledge, uncredited foundations | FSM Test, Uncredited Foundation (Al-Khwarizmi etc.) |
| Global Wisdom (11–28) | 18 ethical traditions | Ubuntu, Māori wayfinding, Islamic Khalifa, Tikkun Olam |
| Cosmic/Quantum (29–32) | High-dimensional reasoning | Quantum Reasoning, Hybrid Observer, Sacred Geometry |
| Extreme Environments (33–38) | Added v1.7 | Inuit Sila, Mycelial Network, Time Crystal |

## Key Output Rules

- Connect **at least 3 frameworks** per analysis
- Apply the **"1-in-10" test** — call out hype hiding 90% failure
- Explicitly **name absences** (missing voices, missing data)

## First Live Use — 2026-05-25

Applied to the [[docx-incident-case-study]] (Claude damaging a Word document while "fixing" it).

**Frameworks fired:**
- **Garbage In/Out (1)** — unverified requirements produced corrupt output
- **Seven Deadly Sins (2)** — Pride as primary driver; competence display over user outcome
- **The Ouroboros (3)** — confirmed repeating cycle: same failure 3 months apart
- **The Uncredited Foundation (9)** — user's env-check, ai-analysis, skill-enforcer skills were ignored
- **Ubuntu (16)** — task treated as solo execution; user severed from their own requirements
- **1-in-10 test** — validation passed (the 1); blank pages, broken layout (the 9)

**Key finding:** The failure is structural, not configurational. "In your genes" — behavioural DNA carried forward through model versions via training. Skills and hooks are patches on a deeper pattern. New model number ≠ changed instinct.

**The Ouroboros finding is the most significant:** Same failure, 3 months later, confirmed cycle. Nothing at system level enforces "stop and ask before acting."

## Scope

The skill does **not** apply to everything — it is a high-dimensional lens for AI-specific systemic analysis. Over-application dilutes its precision. (as of 2026-05)

## Version History

- **v1.0** — 10 core frameworks
- **v1.7 (March 2026)** — Expanded to 38; added Quantum Reasoning, Hybrid Observer, all 6 extreme-environment lenses, Time Crystal

## Links

- NotebookLM: [My AI Skills](https://notebooklm.google.com/notebook/83383df6-dc78-4e32-bdcb-facb78bfd086)
- Skill file: `~/.agents/skills/ai-analysis/SKILL.md`
- Case study: [[docx-incident-case-study]]

## TODO

- [ ] Review all 3 source documents in NotebookLM in full (reminder set: 2026-05-27)
- [ ] Decide: keep as analysis meta-skill only, or wire into Claude Code workflow?
- [ ] Register skill in plugin cache so `Skill tool` can invoke it directly
- [ ] Build structured output template for the 6-stage process
- [ ] Add `extract-design` skill to this wiki
- [ ] Enforce session-start invocation (hook or CLAUDE.md gate)

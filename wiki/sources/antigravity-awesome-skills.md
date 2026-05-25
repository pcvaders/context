# Antigravity Awesome Skills

> Community library of 1,431 reusable SKILL.md playbooks for Claude Code, installable as a Claude Code plugin marketplace with 37 curated bundles.

**URL**: https://github.com/sickn33/antigravity-awesome-skills  
**Fork**: https://github.com/PCGamesplay1/antigravity-awesome-skills  
**Format**: Claude Code plugin marketplace (`.claude-plugin/` + `skills/`)  
**Version**: 10.5.0 (as of 2026-05)

## Overview

Largest open community skill library for Claude Code. Skills are grouped into 9 categories and packaged into 37 installable editorial bundles. Installed via `claude plugins marketplace add`.

## Skill Categories

| Category | Count | Focus |
|---|---|---|
| `general` | 345 | Cross-cutting: debugging, writing, productivity |
| `data-ai` | 273 | ML, LLMs, data pipelines, embeddings |
| `development` | 206 | Frontend, backend, frameworks |
| `security` | 171 | Pen testing, secure coding, AD attacks |
| `infrastructure` | 130 | DevOps, cloud, IaC |
| `workflow` | 99 | Agent orchestration, automation |
| `architecture` | 95 | System design, DDD, review |
| `business` | 81 | Founder, analyst, RevOps, marketing |
| `testing` | 31 | QA, evals, test strategy |

## Installable Bundles (37)

### Development
- `antigravity-bundle-essentials` — Core skills every session
- `antigravity-bundle-full-stack-developer` — Frontend + backend
- `antigravity-bundle-web-wizard` — Web development generalist
- `antigravity-bundle-web-designer` — UI/UX, CSS, design systems
- `antigravity-bundle-python-pro` — Python expert
- `antigravity-bundle-typescript-javascript` — TS/JS expert
- `antigravity-bundle-systems-programming` — Rust, C, low-level
- `antigravity-bundle-mobile-developer` — iOS/Android
- `antigravity-bundle-expo-react-native` — React Native / Expo
- `antigravity-bundle-indie-game-dev` — Game development
- `antigravity-bundle-makepad-builder` — Makepad UI framework

### AI / Agents
- `antigravity-bundle-agent-architect` — Multi-agent systems
- `antigravity-bundle-llm-application-developer` — LLM app building
- `antigravity-bundle-azure-ai-cloud` — Azure AI services
- `antigravity-bundle-apple-platform-design` — Apple HIG + SwiftUI

### Infrastructure / Data
- `antigravity-bundle-devops-cloud` — CI/CD, containers, IaC
- `antigravity-bundle-observability-monitoring` — Logging, metrics, tracing
- `antigravity-bundle-data-analytics` — SQL, BI, dashboards
- `antigravity-bundle-data-engineering` — Pipelines, ETL, Spark

### Security
- `antigravity-bundle-security-engineer` — Security architecture
- `antigravity-bundle-security-developer` — Secure coding practices

### Architecture
- `antigravity-bundle-architecture-design` — System design
- `antigravity-bundle-ddd-evented-architecture` — Domain-driven design

### Business
- `antigravity-bundle-startup-founder` — Product, strategy, fundraising
- `antigravity-bundle-business-analyst` — Requirements, process
- `antigravity-bundle-marketing-growth` — Growth, copy, campaigns
- `antigravity-bundle-revops-crm-automation` — CRM, RevOps
- `antigravity-bundle-commerce-payments` — E-commerce, payments
- `antigravity-bundle-odoo-erp` — Odoo ERP
- `antigravity-bundle-seo-specialist` — SEO strategy + technical

### Automation / Integration
- `antigravity-bundle-automation-builder` — Workflow automation
- `antigravity-bundle-integration-apis` — API integrations
- `antigravity-bundle-qa-testing` — Testing strategy, evals

### Creative / Productivity
- `antigravity-bundle-creative-director` — Brand, creative direction
- `antigravity-bundle-documents-presentations` — Docs, slides, reports
- `antigravity-bundle-oss-maintainer` — Open source maintenance

## Installation

```bash
# Add marketplace (one-time)
claude plugins marketplace add PCGamesplay1/antigravity-awesome-skills

# Install all skills
claude plugins install antigravity-awesome-skills@antigravity-awesome-skills

# Install specific bundle
claude plugins install antigravity-bundle-agent-architect@antigravity-awesome-skills
```

## Related

- [[skill-ecosystem]] — How all skill marketplaces connect
- [[claude-code-skills]] — Claude Code skill system overview
- [[karpathy-guidelines-source]] — Karpathy coding guidelines plugin

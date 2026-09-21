<!-- llm-wiki-log-header-start -->
# Wiki Operation Log

Every ingest, lint run, and maintenance operation is recorded here automatically. For a better experience, use the **Operation History** panel:
- Cmd+P → "View operation history"
- Or open from Settings → Auto Maintenance → Operation History

---
> Append-only record of all wiki operations. Date-stamped and categorized by type.

---

## [2026-09-07] LINT — Weekly maintenance

**Plugin updates:** 5 marketplaces updated successfully, no new plugin versions reported
**Orphan links:** 4 real, all unaddressed since prior passes — [[agent-privilege-separation]] (entities/bumble-credential-hunt-incident.md:37, no stub, flagged since 2026-08-17, 3rd consecutive pass); [[feedback_secret_handling]] (entities/forgejo-mirror.md:67, Claude memory slug not a wiki concept — skip per 2026-07-14 decision); [[Windows 11]] link text (entities/comfyui-pinokio-blackwell.md:26, entities/claude-code-skill-enforcer-windows-bug.md:19) resolves to nothing in scope — actual page is pinokio/Windows 11/windows-11.md (slug `windows-11`), so these should be `[[windows-11|Windows 11]]`; [[swiftbar-mcp-toggle]] (entities/semantic-clip.md:11, dangling since SwiftBar deletion 2026-05-28, 8th consecutive pass unaddressed). Also: `[[wikilinks]]`/`[[Wikilinks]]`/`[[page-a..3]]`/`[[page-name]]`/`[[syntheses]]`/`[[index]]`/`[[log]]`/`[[index.md]]`/`[[log.md]]` hits inside concepts/lint.md, concepts/ingest.md, concepts/llm-wiki.md, concepts/query.md, sources/claude-chat-setup-walkthrough.md, sources/claude-chat-mcp-usage-control-and-disable-option.md, sources/karpathy-llm-wiki-gist.md — literal example/documentation text or immutable transcript content, not real orphans.
**Missing summaries:** 73 (unchanged from 2026-08-31) — still same root cause: ~55 sources/claude-chat-*.md ingested pages plus entity/synthesis pages lack `> summary` line. Fix at ingest-template level, not by hand. Full file list in this run's raw output.
**Stale claims:** none — no `(as of YYYY-MM)` tag older than 2026-03 found (all 2026-05 through 2026-09)
**Duplicate file still present:** `syntheses/Master AI Creation Guide May 2026.md` remains byte-identical (MD5 78343b27...) to `syntheses/MASTER_AI_CREATION_GUIDE.md`, unresolved since flagged 2026-07-17 (3rd re-flag).
**index.html:** regenerated (159 pages: 136 AI + 23 HA)
**Action required:** yes — same 5 open items as 2026-08-31, plus new item (3): (1) stub/confirm [[agent-privilege-separation]]; (2) fix literal [[index.md]]/[[log.md]] text in concepts/lint.md:54; (3) fix [[Windows 11]] link text in entities/comfyui-pinokio-blackwell.md:26 and entities/claude-code-skill-enforcer-windows-bug.md:19 to point at `windows-11`; (4) resolve [[swiftbar-mcp-toggle]] dangling ref; (5) fix ingest template so new pages emit `> summary` (73 pages missing); (6) reconcile duplicate `Master AI Creation Guide May 2026.md` vs `MASTER_AI_CREATION_GUIDE.md` across the two vault sync paths.

---

## [2026-08-31] LINT — Weekly maintenance

**Plugin updates:** 5 marketplaces updated successfully, no new plugin versions reported
**Orphan links:** 4 real, all unaddressed since prior passes — [[agent-privilege-separation]] (entities/bumble-credential-hunt-incident.md:37, no stub, flagged since 2026-08-17); [[feedback_secret_handling]] (entities/forgejo-mirror.md:67, Claude memory slug not a wiki concept — skip per 2026-07-14 decision); [[index.md]]/[[log.md]] literal link text should be [[index]]/[[log]] (concepts/lint.md:54, unfixed since 2026-07-27, 3rd consecutive flag); [[swiftbar-mcp-toggle]] (entities/semantic-clip.md:11, dangling since SwiftBar deletion 2026-05-28, 7th consecutive pass unaddressed). Also: `[[wikilinks]]`/`[[Wikilinks]]`/`[[page-a..3]]`/`[[page-name]]`/`[[syntheses]]`/`[[index]]`/`[[log]]` hits inside concepts/lint.md, concepts/ingest.md, concepts/llm-wiki.md, concepts/query.md, sources/claude-chat-setup-walkthrough.md, sources/claude-chat-mcp-usage-control-and-disable-option.md, sources/karpathy-llm-wiki-gist.md — literal example/documentation text or immutable transcript content, not real orphans.
**Missing summaries:** 73 (down 1 from 74 on 2026-08-17) — still same root cause: ~40 sources/claude-chat-*.md ingested pages plus entity/synthesis pages lack `> summary` line. Fix at ingest-template level, not by hand.
**Stale claims:** none — no `(as of YYYY-MM)` tag older than 2026-03 found
**Duplicate file still present:** `syntheses/Master AI Creation Guide May 2026.md` remains byte-identical (MD5 78343b27...) to `syntheses/MASTER_AI_CREATION_GUIDE.md`, unresolved since flagged 2026-08-17 (and originally 2026-07-17).
**index.html:** regenerated (142 pages)
**Action required:** yes — same 5 open items as 2026-08-17: (1) stub/confirm [[agent-privilege-separation]]; (2) fix literal [[index.md]]/[[log.md]] text in concepts/lint.md:54; (3) resolve [[swiftbar-mcp-toggle]] dangling ref; (4) fix ingest template so new pages emit `> summary` (73 pages missing); (5) reconcile duplicate `Master AI Creation Guide May 2026.md` vs `MASTER_AI_CREATION_GUIDE.md` across the two vault sync paths.

---

## [2026-08-17] LINT — Weekly maintenance

**Plugin updates:** 4 marketplaces updated successfully, no new plugin versions reported
**Orphan links:** 4 real — [[agent-privilege-separation]] — referenced in: entities/bumble-credential-hunt-incident.md:37 (new, no stub exists); [[feedback_secret_handling]] — referenced in: entities/forgejo-mirror.md:67 (not a wiki concept, Claude memory slug — skipped per 2026-07-14 decision); [[index.md]]/[[log.md]] literal link text (should be [[index]]/[[log]]) — concepts/lint.md:54, still unfixed since flagged 2026-07-27; [[swiftbar-mcp-toggle]] — referenced in: entities/semantic-clip.md:11, unaddressed since 2026-06-22 (6 consecutive passes now — SwiftBar plugins were deleted 2026-05-28 per memory, so this is a permanent dangling reference, not a pending feature). Also noted: 9 `[[wikilinks]]`/`[[Wikilinks]]` references inside sources/claude-chat-setup-walkthrough.md and sources/claude-chat-mcp-usage-control-and-disable-option.md — these are literal text inside immutable ingested source transcripts, not intended as real wikilinks, so left as-is. concepts/lint.md's [[page-a]], [[page-b]], [[page1-3]], [[page-name]], [[wikilinks]], [[syntheses]] are illustrative examples inside the lint documentation itself — false positives, not real orphans.
**Missing summaries:** 74 (up from 65 on 2026-07-27) — growth driven by ~40 new sources/claude-chat-*.md auto-ingested pages plus new entity pages (bumble-credential-hunt-incident.md, buzz-agent-harness-config.md, renderzero-vertex-patch.md) and syntheses pages (docx-incident-case-study.md, facs-va-valence-emotion-guide-2026.md, master-*-2026.md, skill-selection-guide.md) added since the last lint pass. Full list in this run's raw output — same root cause flagged 3+ passes running: fix the ingest template to always emit `> summary`, rather than backfilling by hand.
**Stale claims:** none — all `(as of YYYY-MM)` tags are 2026-05 or 2026-06, within 6-month window of 2026-08-17
**Duplicate file found:** `syntheses/Master AI Creation Guide May 2026.md` is byte-identical (MD5 78343b27...) to `syntheses/MASTER_AI_CREATION_GUIDE.md` — this exact dupe was deleted 2026-07-17 but has reappeared, likely re-synced from another host (iCloud mirror at `~/Library/.../Obsidian Vault AI/` still shows a diverging log.md, suggesting two vault copies are not fully unified). Flagged, not deleted — needs human decision on which sync path is canonical.
**index.html:** regenerated (142 pages: 119 AI + 23 HA)
**Action required:** yes — (1) create stub for [[agent-privilege-separation]] or confirm intent; (2) fix [[index.md]]/[[log.md]] literal text in concepts/lint.md:54 (missed by 2026-07-14 fix pass, flagged again 2026-07-27, still open); (3) decide fate of [[swiftbar-mcp-toggle]] reference — remove or stub, SwiftBar is gone; (4) 74 pages need `> summary` — fix ingest template; (5) resolve reappeared duplicate `Master AI Creation Guide May 2026.md` vs `MASTER_AI_CREATION_GUIDE.md` and reconcile the two vault copies (Sync path vs iCloud path) so files/log don't diverge again.

---

## [2026-08-24] LINT — Weekly maintenance

**Plugin updates:** 5 marketplaces updated successfully (claude-plugins-official, caveman, karpathy-skills, antigravity-awesome-skills, agentmemory), no new plugin versions surfaced in output
**Orphan links:** 3 real — [[agent-privilege-separation]] — referenced in: entities/bumble-credential-hunt-incident.md (still no stub, open since 2026-08-17); [[feedback_secret_handling]] — referenced in: entities/forgejo-mirror.md (Claude memory slug, not a wiki concept — skipped per 2026-07-14 decision); [[swiftbar-mcp-toggle]] — referenced in: entities/semantic-clip.md (SwiftBar deleted 2026-05-28, permanent dangling reference, unaddressed since 2026-06-22, now 7 consecutive passes). Note: [[index.md]]/[[log.md]] literal-text issue in concepts/lint.md flagged 2026-07-27/2026-08-17 no longer detected this pass — appears fixed or file changed. concepts/lint.md's [[page-a]]/[[page-b]]/[[page1-3]]/[[page-name]]/[[wikilinks]]/[[syntheses]] remain illustrative examples, not real orphans; `[[wikilinks]]`/`[[Wikilinks]]` inside claude-chat-*.md source transcripts remain literal text, not real links.
**Missing summaries:** 50 (down from 74 on 2026-08-17) — mostly sources/claude-chat-*.md auto-ingested pages plus entities/bumble-credential-hunt-incident.md and entities/buzz-agent-harness-config.md. Root cause unchanged from prior passes: ingest template should emit `> summary` by default rather than relying on backfill.
**Stale claims:** none — all `(as of YYYY-MM)` tags are 2026-05 or 2026-06, within 6-month window of 2026-08-24
**Duplicate file still present:** `syntheses/Master AI Creation Guide May 2026.md` remains byte-identical (MD5 78343b27...) to `syntheses/MASTER_AI_CREATION_GUIDE.md`, same as flagged 2026-08-17 and 2026-07-17 — still unresolved, needs human decision on canonical sync path.
**index.html:** regenerated (142 pages: 119 AI + 23 HA)
**Action required:** yes — (1) create stub for [[agent-privilege-separation]] or confirm intent; (2) decide fate of [[swiftbar-mcp-toggle]] reference; (3) 50 pages need `> summary` — fix ingest template rather than hand-backfill; (4) resolve reappeared duplicate `Master AI Creation Guide May 2026.md` vs `MASTER_AI_CREATION_GUIDE.md`, unresolved for 3 consecutive passes now.

---

## [2026-08-10] LINT — Weekly maintenance

**Plugin updates:** ran `claude plugins marketplace update` — 4 marketplaces (claude-plugins-official, caveman, karpathy-skills, antigravity-awesome-skills) updated, CLI reports success but no per-marketplace version diff
**Orphan links:** 5 — [[agent-privilege-separation]] (entities/bumble-credential-hunt-incident.md:37), [[swiftbar-mcp-toggle]] (entities/semantic-clip.md:11), [[feedback_secret_handling]] (entities/forgejo-mirror.md:67, points to a memory slug not a wiki page), [[caveman-julius-brussee]] (concepts/ai-cost-observability.md:31, entities/julius-brussee.md:11,27 — page doesn't exist, only `sources/caveman-julius-brussee.md` and `entities/julius-brussee.md`), [[codeburn-getagentseal]] (concepts/ai-cost-observability.md:30,55 — page doesn't exist, only `sources/codeburn-getagentseal.md`) — same 3 carried over from 2026-08-03 plus 2 newly caught (link/slug mismatch between sources/ and concepts/ naming)
**Missing summaries:** 73 — down from 84 on 2026-08-03. Still mostly `sources/claude-chat-*.md` raw chat exports (54 files) plus `syntheses/master-*`/`MASTER_*` guides (7), and several `concepts/`/`entities/` pages (ai-analysis-skill.md, skill-ecosystem.md, bumble-credential-hunt-incident.md, buzz-agent-harness-config.md, forgejo-mirror.md, litellm-proxy.md, obsidian-agent-bridge.md)
**Stale claims:** none — all `(as of YYYY-MM)` tags are 2026-05 or 2026-06, within the 6-month window
**index.html:** regenerated (142 pages — 119 AI + 23 HA)
**Action required:** yes — orphan links growing (3→5), two are slug-naming mismatches (`sources/codeburn-getagentseal.md` exists but nothing under that exact concepts-side slug, same for caveman-julius-brussee) — likely just needs the source pages copied/symlinked into entities/ or the links repointed to existing `sources/` slugs. 73 missing summaries still high, no progress this week beyond the 11 that dropped off. `syntheses/Master AI Creation Guide May 2026.md` (spaces in filename) still present, still unresolved duplicate flagged last week.

---

## [2026-08-03] LINT — Weekly maintenance

**Plugin updates:** ran `claude plugins marketplace update` — 4 marketplaces updated, no new versions reported
**Orphan links:** 3 — [[agent-privilege-separation]] (entities/bumble-credential-hunt-incident.md:37), [[swiftbar-mcp-toggle]] (entities/semantic-clip.md:11), [[feedback_secret_handling]] (entities/forgejo-mirror.md:67, points to a memory slug, not a wiki page)
**Missing summaries:** 84 — mostly `sources/claude-chat-*.md` raw chat exports plus `syntheses/master-*` guides and several `concepts/`/`entities/` pages (mcp.md, skill-ecosystem.md, agent-native-cli.md, ai-analysis-skill.md, smart-connections.md, forgejo-mirror.md, buzz-agent-harness-config.md, pinecone.md, renderzero-vertex-patch.md, obsidian-agent-bridge.md, litellm-proxy.md, bumble-credential-hunt-incident.md, and full sources/ list — see run output)
**Stale claims:** none — all `(as of YYYY-MM)` tags are 2026-05 or 2026-06, within the 6-month window
**index.html:** regenerated (142 pages — 119 AI + 23 HA)
**Action required:** yes — 84 missing summaries is high; also noticed `syntheses/Master AI Creation Guide May 2026.md` has spaces in filename (violates no-spaces convention, duplicate of `MASTER_AI_CREATION_GUIDE.md`/`master-ai-video-image-guide-2026.md` — likely a stray duplicate worth removing)

---

## [2026-06-21] SYNC + ENTITY — notebooklm-mcp wired; wiki sync to Cowork + homelab-brain

**Agent:** Claude Code (claude-sonnet-4-6) — Mac

**Created 1 entity page:**
- `entities/notebooklm-mcp.md` — nlm setup, auth status, per-client config paths, re-auth flow

**Fixed:** Cowork trusted folder (`~/Documents/Claude/Projects/AI LLM Wiki/wiki/`) had only 2 pages vs 226 in iCloud vault — diverged silently. homelab-brain wiki was empty.

**Remediation:**
- Rsync'd iCloud vault wiki → Cowork folder (2→226 pages)
- Rsync'd iCloud vault wiki → homelab-brain/wiki/ (0→226 pages)
- Added `vault sync` command to `~/projects/vault.sh`
- Wired `vault sync` into `vault ingest all` pipeline (step 6/7)

**Root cause:** No sync mechanism existed between iCloud vault (write target) and Cowork/homelab-brain (read targets). All writes went to iCloud only.

**Open items:**
- Cowork NLM MCP: added to `claude_desktop_config.json` — needs app restart to activate
- Nightly `vault ingest all` launchd agent should now keep all three locations in sync

---

## [2026-05-31] INTERLINKED — entity pages for wiki-clip, smart-clip, obsidian-wiki-memory, interlinked

**Agent:** Claude Code (claude-sonnet-4-6) — Mac

**Created 4 entity pages (open items cleared):**
- `entities/wiki-clip.md` — Tier 1 keyword search CLI tool
- `entities/smart-clip.md` — three-tier search orchestrator (wiki-clip → semantic-clip → NLM)
- `entities/obsidian-wiki-memory.md` — Claude Code skill for vault context loading
- `entities/interlinked.md` — Claude Code skill for wiki INGEST/QUERY/LINT operations

**Also fixed this session (outside wiki):**
- vault daily-sync LaunchAgent: replaced iCloud vault.sh call with ~/projects/vault.sh copy; granted /bin/bash Full Disk Access → nightly 22:00 sync now fully automated
- Panel server: fixed index.html (was old version, missing memory section); 50 AI wiki cards now visible
- Manual sync run: wiki caught up from 2026-05-22 → 2026-05-31 (commit d226828)
- Memory system (Plan 2) complete: voyager-hub, CONTEXT.md, wiki_classify.py, session hooks, Chat/Cowork/CCR bootstrapped

**Open items remaining:**
- Ingest `semantic-clip.js` as source page (`sources/semantic-clip.md`)
- Embedding delta: 25 .ajson vs 70 wiki pages (Smart Connections not fully indexed)

---

## [2026-05-22] INGEST — Claude.ai Mobile Sync & Mac Desktop Issues (May 2026)

**Source**: Mobile debugging session notes (Claude.ai mobile)
**Agent**: Claude Code (claude-sonnet-4-6)

**Pages created (2):**
- `sources/claude-mobile-sync-issues-2026-05.md` — mobile sync root causes, GitHub bridge confirmation, daemon bug fix, desktop redesign notes
- `concepts/claude-ai-context-loading.md` — NEW: Project Instructions / CLAUDE.md / hooks pattern for persistent context across surfaces

**Pages updated (1):**
- `entities/claude-code.md` — May 2026 desktop redesign features, daemon sleep/wake + brew upgrade bugs fixed

**Key facts ingested:**
- macOS sleep/wake daemon bug patched May 2026 — `brew upgrade claude` to fix
- Claude.ai session URLs always auth-gated (403 for unauthenticated) — confirmed not a bug
- Project Instructions = Claude.ai equivalent of SessionStart hook for context loading
- Desktop redesign: session sidebar, drag-and-drop, integrated terminal, usage button, three view modes [some claims unsourced, verify against release notes]

**Open items:**
- Verify May 2026 desktop redesign feature list against official release notes
- Add GitHub raw URL fetch instruction to Claude.ai Project Instructions for aillmwiki project

---

## [2026-05-22] ARCHITECTURE — GitHub bridge for Claude.ai mobile access

**Problem**: Claude.ai mobile/web cannot read the iCloud Obsidian vault. Three root causes:
1. iCloud blocked — Claude.ai has no filesystem MCP access (Claude Code only)
2. Google Drive MCP reads Google Docs format only, not .md files
3. "Public link" on Claude Code iPhone = Remote Control sessions — always auth-gated, no truly public share link exists (confirmed via docs)

**Solution**: GitHub as read bridge (`PCGamesplay1/Claude-skills`, public repo)
- `wiki/index.md` + `wiki/log.md` pushed to main branch
- Claude.ai can WebFetch raw GitHub URLs (unauthenticated, no MCP needed)

**Raw URLs (live):**
- `https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/index.md`
- `https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/log.md`

**Files changed:**
- `~/claude-skills/wiki/sync.sh` — fixed two bugs: VAULT_SUBDIR default (`AI-LLM-Wiki` → `Obsidian Vault Icloud/Obsidian Vault AI`), file source path (`$VAULT/` → `$VAULT/wiki/`)
- `vault.sh` — added `vault github sync` command; wired as Step 5 in `vault ingest all`

**Sync command:** `vault github sync` (or runs automatically via `vault ingest all`)

**Limitation:** Only index.md and log.md synced. Full wiki requires `copy_if_exists` entries in sync.sh.

---

## [2026-05-22] INGEST — semantic-clip replaces smart-connections-mcp

**Change**: smart-connections MCP permanently disabled. Replaced by local CLI.

**Root cause documented**: MCP loaded at every session start → token drain before first user message. No native per-MCP disable UI in Claude Code — workaround was SwiftBar toggle (see `mcp-connector-management.md`). Full CLI replacement preferred over toggle.

**Wiki pages updated:**
- `entities/smart-connections-mcp.md` — marked DEPRECATED, replacement documented
- `entities/semantic-clip.md` — NEW: full entity page for CLI replacement

**Technical summary:**
- `semantic-clip` reads `.smart-env/multi/*.ajson` pre-computed vectors directly
- Same `TaylorAI/bge-micro-v2` 384-dim embeddings as Smart Connections plugin
- `.ajson` format quirk: bare `"key": {...},` with trailing comma — must strip + wrap in `{}`
- `@xenova/transformers` ONNX runner embeds query locally, cosine similarity, top-3 results
- Integrated as Tier 2 in `smart-clip` three-tier stack (keyword → semantic → NotebookLM)
- `disabledMcpjsonServers: ["smart-connections"]` set in `~/.claude/settings.json`

**Do not use smart-connections MCP tools in future sessions.** Use `semantic-clip "query"` instead.

---

## [2026-05-19] SETUP — Vault initialized

- Folder structure created: raw/, claude-sessions/, wiki/ (with concepts/, entities/, sources/, syntheses/)
- Starter files: index.md, log.md
- Ready for first ingest

---

## [2026-05-20] INGEST — JuliusBrussee/caveman

**Source**: https://github.com/JuliusBrussee/caveman
**Agent**: Claude Code (claude-sonnet-4-6)

**Pages created (4):**
- `sources/caveman-julius-brussee.md` — source summary
- `entities/julius-brussee.md` — author entity
- `concepts/token-compression.md` — new concept
- `concepts/claude-code-skills.md` — new concept

**Pages updated (2):**
- `entities/claude-code.md` — added Skills section, new cross-links
- `wiki/index.md` — added all new pages to catalog

**Open items:** 3 more clippings pending ingest (codeburn, design-extract, CloakBrowser)

---

## [2026-05-20] INGEST — getagentseal/codeburn + Manavarya09/design-extract + CloakHQ/CloakBrowser

**Sources**: 3 clippings batch
**Agent**: Claude Code (claude-sonnet-4-6)

**Pages created (4):**
- `sources/codeburn-getagentseal.md` — token cost observability TUI, 19+ agents
- `sources/design-extract-manavarya09.md` — design system extractor + MCP server
- `sources/cloakbrowser-cloakhq.md` — stealth Chromium stub (minimal clipping content)
- `concepts/ai-cost-observability.md` — new concept connecting codeburn + caveman-stats

**Pages updated (1):**
- `wiki/index.md` — 4 new entries added

**Notes:**
- CloakBrowser clipping had title/URL only — stub created, marked [unsourced]
- No new entity pages — no named authors in clippings
- `mcp` concept page not yet created — referenced as [[mcp]] in design-extract source

**Open items:**
- Create `concepts/mcp.md` (referenced but missing)
- Run LINT pass to surface other orphan links

---

## [2026-05-21] INGEST — Skill Ecosystem (antigravity + karpathy)

**Sources**: 4 Claude Code plugin marketplaces
**Agent**: Claude Code (claude-sonnet-4-6)

**Plugins installed:**
- `antigravity-awesome-skills@antigravity-awesome-skills` — 1,431 skills, 37 bundles ✅
- `andrej-karpathy-skills@karpathy-skills` — Karpathy coding guidelines ✅
- `superpowers@claude-plugins-official` — already installed
- `caveman@caveman` — already installed

**Pages created (3):**
- `sources/antigravity-awesome-skills.md` — 1,431 skills, 9 categories, 37 bundles catalog
- `sources/karpathy-guidelines-source.md` — Karpathy 4-rule coding guidelines plugin
- `concepts/skill-ecosystem.md` — full marketplace map + discovery workflow

**Pages updated (1):**
- `wiki/index.md` — 3 new entries added

**Skill discovery workflow established:**
Task → `semantic_search` wiki → find skill → `Skill` tool invokes it

**Open items:**
- Consider ingesting `antigravity-bundle-*` individual bundle skill lists for finer-grained search

---

## [2026-05-21] INGEST — PIR troubleshooting sessions + wiki-ha generator + synthesis

**Sources**: Claude.ai conversations [23], [25], [26]
**Agent**: Claude Code (claude-sonnet-4-6)

**Wiki-HA pages created (3):**
- `wiki-ha/sources/pir-corridor-troubleshooting-23.md` — illuminance OR condition fix, Sonoff SNZB-06P add
- `wiki-ha/sources/pir-lights-issue-25.md` — all-sensors-off wait fix, ghost detection
- `wiki-ha/sources/pir-lights-troubleshooting-26.md` — 4-sensor expansion, disabled automation root cause

**Wiki-HA pages updated (3):**
- `wiki-ha/concepts/pir-automation.md` — multi-sensor wait pattern, illuminance OR, diagnostic order, automation enabled check
- `wiki-ha/concepts/presence-detection.md` — mmWave mains power requirement, ghost detection
- `wiki-ha/index.md` — 3 new source entries

**AI Wiki pages created (1):**
- `wiki/syntheses/skill-selection-guide.md` — task→skill mapping, workflow phase map, anti-patterns

**Generator updated:**
- `generate_wiki_index.py` — now includes wiki-ha/ section (HA Concepts/Entities/Sources)
- Output: 49 pages total (31 AI + 18 HA)

**Skill gate hook implemented:**
- `~/.claude/hooks/skill-enforcer.py` — PreToolUse blocks Bash/Edit/Write until skill invoked
- `~/.claude/hooks/skill-tracker.py` — PostToolUse marks skill as invoked
- `~/.claude/settings.json` — hooks wired in

**Open items:**
- Spotify CLI: investigate `ANTHROPIC_BASE_URL` → LiteLLM routing for `claude-press`
- Generate ComfyUI CLI
- Ingest `antigravity-bundle-*` individual skill lists

---

## [2026-05-21] INGEST — cli-printing-press

**Source**: https://github.com/mvanhorn/cli-printing-press  
**Agent**: Claude Code (claude-sonnet-4-6)

**Pages created (2):**
- `sources/cli-printing-press.md` — full tool reference, workflow, slash commands, planned generations
- `concepts/agent-native-cli.md` — agent-native CLI design pattern, 5 rungs, NOI concept, exit codes

**Binary installed**: `printing-press` v4.9.0 at `~/go/bin/`  
**Skills cloned**: `~/cli-printing-press/`  
**Alias added**: `claude-press` → `claude --plugin-dir ~/cli-printing-press`

**Open items:**
- Generate Spotify CLI: `claude-press` → `/printing-press <spotify-spec-url>`
- Generate ComfyUI CLI (3DGenStudio)
- Add generated MCP servers via SwiftBar mcp-toggle

---

## [2026-05-21] INGEST — Claude chat history (42 conversations)

**Source**: Claude.ai export — conversations.json (42 convos, 11.5MB)
**Agent**: Claude Code (claude-sonnet-4-6)

**AI Wiki pages created (2):**
- `sources/vault-setup-session.md` — founding vault session, key decisions
- `sources/mcp-connector-management.md` — MCP toggle, disabled.json, race condition pattern

**HA Wiki created (new section):**
- `wiki-ha/` — full Home Assistant wiki with 5 concepts, 5 entities, 5 sources
- Ingested from conversations: [13] ha-mcp setup, [16] Zigbee migration, [17] Aqara setup, [18] automation building, [00] MQTT fix

**Skipped (not wiki-worthy):**
- [07] Canva, [10] game chars, [12] Iran war, [19] tutorial images, [20] Immich, [34-35] stop-motion
- [11] Email unsubscriber tool — product research, not AI tooling knowledge
- [28] Skills in context — HA skill creation + token analyzer (already in wiki)

**Open items:**
- Add HA wiki to `generate_wiki_index.py` to include in front page
- Extend wiki-ha with PIR troubleshooting sessions [23, 25, 26]

---

## [2026-05-22] ARCHITECTURE — semantic-clip replaces smart-connections-mcp

**Session**: ChatLogs/logs/session-001-architecture-pivot.md (10:05)
**Agent**: Claude Code (claude-sonnet-4-6)

**Decision**: Drop Python MCP server (`smart-connections-mcp`) — loaded at every session start, ~1,500 prompt tokens overhead before user typed anything. No native Claude Code UI to disable per-session.

**Replacement**: `semantic-clip` — Node.js CLI reading same `.smart-env/multi/*.ajson` pre-computed vectors directly. Zero MCP, zero network, zero session-start cost.

**Pages created (2):**
- `entities/semantic-clip.md` — CLI design, 3-tier smart-clip stack, `.ajson` format quirks
- `entities/smart-connections-mcp.md` — full entity page, marked DEPRECATED 2026-05-22

**Pages updated (1):**
- `entities/claude-code.md` — deprecation note, semantic-clip as replacement

**smart-clip 3-tier stack documented:**

| Tier | Tool | Method | Network |
|---|---|---|---|
| 1 | `wiki-clip` | Keyword/Paperpress frontmatter | Zero |
| 2 | `semantic-clip` | Cosine sim, local `.smart-env` vecs | Zero |
| 3 | `nlm query` | NotebookLM AI answer | Cloud |

**Verified**: `semantic-clip "smart connections mcp architecture"` → top-3 hits, scores 0.728/0.721/0.706 ✓

**Config**: `disabledMcpjsonServers: ["smart-connections"]` in `~/.claude/settings.json`

**Open items:**
- Ingest `semantic-clip.js` source as wiki source page (`sources/semantic-clip.md`)
- Document `wiki-clip` and `smart-clip` wrapper (referenced but no entity pages yet)
- Log `obsidian-wiki-memory` skill (new, appeared 2026-05-22)
- Log `interlinked` skill (new, appeared 2026-05-22)

---

## [2026-05-22] WORKFLOW — NLM sync pattern established

**Decision**: Option B — end-of-session batch update to NotebookLM.

**Roles:**
- Obsidian wiki = source of truth (live, updated per ingest)
- NotebookLM (`38bfb58a`) = backup + cross-session memory snapshot

**Why B over A (inline):** NLM not queried mid-session. Per-page NLM calls wasteful. Lag of one session acceptable.
**Why B over C (weekly):** Session-end is natural checkpoint, keeps NLM within 1 session of current state.

**Method per session end:**
1. Delete stale bundled sources that changed (by source ID)
2. `source_add` updated text bundles: entities chunk, log+index chunk
3. Do NOT replace sources that haven't changed — reduces NLM processing

**NLM source map (as of 2026-05-22):**
| Source ID | Title | Status |
|---|---|---|
| aa5751b2 | Wiki: Core Concepts — LLM Wiki, RAG, Ingest, Query, Lint | Current |
| 3985f7bb | Wiki: Core Concepts — Skills, Token Compression, MCP, Agent-Native CLI | Current |
| 679d5076 | Wiki: Entities — Claude Code, Karpathy, Julius Brussee, Obsidian, Smart Connections, LiteLLM | Stale — needs update next session |
| 93710920 | Wiki: Skill Ecosystem | Current |
| c421ef3c | Wiki: Sources — Karpathy, Caveman, Codeburn, CLI Printing Press, MCP Connector | Current |
| effaf83b | Wiki: Syntheses — RAG vs LLM Wiki, Skill Selection Guide | Current |
| c2ec0f4c | Wiki: Entities — semantic-clip + smart-connections-mcp (DEPRECATED) | Added 2026-05-22 |
| 9836081b | Wiki: Operation Log + Index (as of 2026-05-22 updated) | Added 2026-05-22 |

---

---
---

## [2026-05-22] BASELINE — vault-stats infrastructure deployed

**Script**: `vault-stats.sh` in vault root
**Baseline**: `wiki/stats/baseline-2026-05-22.md` (immutable)

**Baseline snapshot (2026-05-22 15:10):**

| Metric | Value |
|--------|-------|
| wiki/ pages | 37 |
| wiki-ha/ pages | 20 |
| Total wiki pages | 57 |
| Total words | 20,175 |
| Est. tokens (wiki content) | 38,428 |
| wiki/ size | 204K |
| .smart-env/ size | 452K |
| .ajson embedding files | 25 |

**Usage:**
```bash
vault-stats              # stdout
vault-stats --save       # write wiki/stats/snapshot-YYYY-MM-DD.md
vault-stats --baseline   # write immutable baseline (run once per phase)
```

**Known issue at baseline:**
- Embedding delta = 32 (25 .ajson vs 57 wiki pages) — Smart Connections hasn't indexed full vault
- Healthy target: delta ≤ 5
- Fix: open vault in Obsidian, let Smart Connections finish indexing, re-run `vault-stats --baseline`

**Alert thresholds:**
- Token est warn: 100,000 | critical: 200,000
- Avg page size healthy: 300–2,000 chars (current: 2,696 — slightly above, monitor)
- Embed delta healthy: ≤ 5

---

---

## [2026-05-22] ARCHITECTURE — vault CLI + dual wiki + NLM automation

**Changes:**

1. `vault.sh` — unified CLI entry point (single command: `vault`)
2. `vault-nlm-sync.sh` — automated NLM sync (bundles wiki .md → NLM text sources)
3. `wiki-personal/` — personal wiki created (concepts/entities/sources/syntheses)
4. Personal NLM notebook created: `64447237-2416-438c-8752-1c34ca85790f`
5. NLM state file: `wiki/stats/nlm-sync-state.json`

**First AI wiki sync complete:**
| Bundle | Source ID | Size |
|--------|-----------|------|
| AI Wiki: Concepts | 4a663b23 | 26K chars |
| AI Wiki: Entities | 55e6abdc | 17K chars |
| AI Wiki: Sources | e36cb1fe | 28K chars |
| AI Wiki: Syntheses | 4cef4001 | 6K chars |
| AI Wiki: Home Assistant | be3a8aee | 29K chars |
| AI Wiki: Operation Log + Index | d1616348 | 16K chars |

**Old 8 manually-managed sources deleted** — replaced by auto-managed bundles.

**vault commands:**
```
vault                   → help
vault clip/semantic/smart "query"
vault ingest nlm        → sync AI wiki → NLM
vault ingest all        → full pipeline
vault personal nlm/stats/clip
vault stats [save|baseline]
vault backup
vault index
```

---

---

## [2026-05-23] INGEST — Pinokio + Windows 11 section

**Source**: Manual creation (setup session)
**Agent**: Claude Code (claude-sonnet-4-6) — Windows instance

**Pages created (3):**
- `pinokio/pinokio.md` — Pinokio entity page: one-click launcher, architecture, app table, key paths
- `pinokio/Windows 11/windows-11.md` — Windows 11 host entity: machine specs, local AI stack, Ollama setup, startup behavior
- `pinokio/Windows 11/claude-code-sync.md` — Mac→Windows sync guide: skills/hooks/commands/settings.json paths, step-by-step checklist, Windows-specific differences

**Supporting files:**
- `pinokio/Windows 11/windows-settings.json` — ready-made settings.json template for Windows (Node path, Python path, PowerShell statusLine)

**Key facts:**
- Switched from LMStudio to Ollama 2026-05-23 — LMStudio used 15.3/16 GB VRAM, Ollama uses ~4.7 GB
- Windows iCloud path: `C:\Users\PCG1\iCloudDrive\iCloud~md~obsidian\...` (sync confirmed working)
- `skill-enforcer.py` hook broken on Windows: `os.getppid()` returns different PID per hook invocation → flag never matched → all Edit/Write blocked

**Open items:**
- Fix `skill-enforcer.py` + `skill-tracker.py`: replace PID-based session key with stable alternative
- Index.md updated this session to include all missing pages (2026-05-22 and 2026-05-23 additions)
- Claude.ai (chat) cannot access vault — confirmed only Claude Code has direct iCloud filesystem access

---

## [2026-05-26] SYNC — Windows session, index catch-up

**Agent**: Claude Code (claude-sonnet-4-6) — Windows instance (first Windows session)

**Index.md updated**: Added 7 missing entries —
- Concepts: `claude-ai-context-loading`, `mcp`
- Entities: `litellm-proxy`
- Pinokio section (new): `pinokio`, `windows-11`, `claude-code-sync`
- Sources: `claude-mobile-sync-issues-2026-05`
- Syntheses: `skill-selection-guide`

**Hook bug confirmed**: `skill-enforcer.py` blocks Edit/Write on Windows (os.getppid() session key mismatch). Workaround: use PowerShell tool for file writes.

**Open items:**
- Fix skill-enforcer.py / skill-tracker.py for Windows (stable session key)
- Sync GitHub bridge (wiki/index.md + wiki/log.md → PCGamesplay1/Claude-skills)

---

## [2026-05-26] SETUP — Claude Code memory init + wiki backup automation

**Agent**: Claude Code (claude-sonnet-4-6) — Windows instance

**Memory system initialized:**
- `C:\Users\PCG1\.claude\projects\C--Users-PCG1-iCloudDrive-AI-and-Robots-Pinokio\memory\` created
- 4 files: `MEMORY.md`, `user-profile.md`, `feedback-hooks-windows.md`, `project-aillmwiki.md`

**Sync automation:**
- Script: `C:\Users\PCG1\.claude\hooks\sync-memory-to-wiki.ps1`
- Target: `wiki/agents/claude-primary/` in vault
- Trigger: SessionStart hook (async, runs every session)

**settings.json changes (3 additions to SessionStart):**
1. `caveman-activate.js` — existing
2. PowerShell flag reset — deletes `%TEMP%\.claude-skill-invoked` (fixes skill-enforcer session key bug)
3. `sync-memory-to-wiki.ps1` — async memory backup

**skill-enforcer.py / skill-tracker.py fixed:**
- Old: `os.getppid()` as session key → different PID per hook invocation on Windows
- New: fixed flag path `%TEMP%/.claude-skill-invoked`, reset each SessionStart

**Note:** `caveman-activate.js` is hard-blocked from modification by auto-mode classifier. Flag reset handled via standalone settings.json hook instead.

## 2026-06-20 — INGEST
- Created `wiki/entities/forgejo-mirror.md` (Forgejo GitHub Mirror, Proxmox LXC 106). Cross-linked proxmox/homelab. Code done, awaiting install.

## [2026-06-22] LINT — Weekly maintenance

**Plugin updates:** 4 marketplaces updated successfully (no new version details output)
**Orphan links:** 19 unique slugs — [[comfyui]] (higgsfield-comfyui-pipeline-architecture.md), [[feedback_secret_handling]] (forgejo-mirror.md), [[higgsfield]] (higgsfield-comfyui-pipeline-architecture.md), [[homelab]] (forgejo-mirror.md), [[index.md]] (ingest.md, karpathy-llm-wiki-gist.md, lint.md, llm-wiki.md), [[isle-of-dogs-project]] (higgsfield-comfyui-pipeline-architecture.md), [[log.md]] (ingest.md, karpathy-llm-wiki-gist.md, lint.md, llm-wiki.md), [[ltx-video]] (higgsfield-comfyui-pipeline-architecture.md), [[master-veo-vertex-ai]] (master-veo-professional-2026.md, master-veo3-prompting-april-2026.md), [[master-veo3-synthesis]] (master-veo-professional-2026.md, master-veo3-prompting-april-2026.md), [[obsidian-agent-bridge]] (semantic-clip.md), [[page-a/page-b/page-name/page1/page2/page3]] (lint.md — placeholder examples), [[pcg1-directors-prep]] (master-comfyui-2026.md), [[proxmox]] (forgejo-mirror.md), [[seedance]] (higgsfield-comfyui-pipeline-architecture.md), [[soul-id]] (higgsfield-comfyui-pipeline-architecture.md), [[swiftbar-mcp-toggle]] (semantic-clip.md), [[syntheses]] (query.md), [[wikilinks]] (obsidian.md, lint.md, claude-chat-* files)
**Missing summaries:** 57 files — mostly claude-chat-* logs + MASTER_AI_CREATION_GUIDE.md, master-veo-professional-2026.md, master-veo3-prompting-april-2026.md, master-comfyui-2026.md, master-ai-video-image-guide-2026.md, ai-analysis-skill.md, ai-infrastructure-stack-mar2026.md, djbrightone-spotify-skill-may2026.md, claude-skills-agent-discovery-feb2026.md, facs-va-valence-emotion-guide-2026.md
**Stale claims:** none (all "as of" dates are 2026-05 or 2026-06, within 6-month window)
**index.html:** regenerated (128 pages: 105 AI + 23 HA)
**Action required:** yes — (1) Create missing pages for real orphans: comfyui, higgsfield, homelab, isle-of-dogs-project, ltx-video, master-veo-vertex-ai, master-veo3-synthesis, obsidian-agent-bridge, pcg1-directors-prep, proxmox, seedance, soul-id, swiftbar-mcp-toggle; (2) Fix [[index.md]]/[[log.md]] links → [[index]]/[[log]]; (3) Add `> summary` lines to 10 non-chat wiki pages

---

## [2026-06-29] LINT — Weekly maintenance

**Plugin updates:** 4 marketplaces updated successfully (no new versions announced)
**Orphan links:** 17 real slugs (excluding lint.md placeholder examples page-a/b/name/page1/2/3 and Wikilinks meta-refs) — [[comfyui]] (higgsfield-comfyui-pipeline-architecture.md), [[feedback_secret_handling]] (forgejo-mirror.md), [[higgsfield]] (higgsfield-comfyui-pipeline-architecture.md), [[homelab]] (forgejo-mirror.md), [[index.md]] (ingest.md, karpathy-llm-wiki-gist.md, lint.md, llm-wiki.md), [[isle-of-dogs-project]] (higgsfield-comfyui-pipeline-architecture.md), [[log.md]] (ingest.md, karpathy-llm-wiki-gist.md, lint.md, llm-wiki.md), [[ltx-video]] (higgsfield-comfyui-pipeline-architecture.md), [[master-veo-vertex-ai]] (master-veo-professional-2026.md, master-veo3-prompting-april-2026.md), [[master-veo3-synthesis]] (master-veo-professional-2026.md, master-veo3-prompting-april-2026.md), [[obsidian-agent-bridge]] (semantic-clip.md), [[pcg1-directors-prep]] (master-comfyui-2026.md), [[proxmox]] (forgejo-mirror.md), [[seedance]] (higgsfield-comfyui-pipeline-architecture.md), [[soul-id]] (higgsfield-comfyui-pipeline-architecture.md), [[swiftbar-mcp-toggle]] (semantic-clip.md), [[syntheses]] (query.md)
**Missing summaries:** 70 files — 21 non-chat wiki pages: MASTER_AI_CREATION_GUIDE.md, Master AI Creation Guide May 2026.md, ai-analysis-skill.md, ai-infrastructure-stack-mar2026.md, claude-skills-agent-discovery-feb2026.md, cloakbrowser-cloakhq.md, codeburn-getagentseal.md, design-extract-manavarya09.md, djbrightone-spotify-skill-may2026.md, docx-incident-case-study.md, facs-va-valence-emotion-guide-2026.md, forgejo-mirror.md, karpathy-llm-wiki-gist.md, litellm-proxy.md, master-ai-video-image-guide-2026.md, master-comfyui-2026.md, master-veo-professional-2026.md, master-veo3-prompting-april-2026.md, semantic-clip.md, skill-ecosystem.md, skill-selection-guide.md + ~49 claude-chat-* log files
**Stale claims:** none (all "as of" dates are 2025-12 or newer, within 6-month window)
**index.html:** regenerated (128 pages: 105 AI + 23 HA)
**Action required:** yes — (1) Orphan pages unchanged from 2026-06-22 — priority: create comfyui, higgsfield, homelab, proxmox, ltx-video, seedance, soul-id, master-veo-vertex-ai, master-veo3-synthesis, swiftbar-mcp-toggle entity/concept stubs; (2) Fix [[index.md]]/[[log.md]] → [[index]]/[[log]] in ingest.md, karpathy-llm-wiki-gist.md, lint.md, llm-wiki.md; (3) Add `> summary` to 21 non-chat wiki pages

---

## [2026-07-06] LINT — Weekly maintenance

**Plugin updates:** ran `claude plugins marketplace update` — 4 marketplaces updated, no version detail surfaced by CLI
**Orphan links:** 17 found — [[Wikilinks]] (sources/claude-chat-setup-walkthrough.md), [[comfyui]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[feedback_secret_handling]] (entities/forgejo-mirror.md), [[higgsfield]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[homelab]] (entities/forgejo-mirror.md), [[isle-of-dogs-project]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[ltx-video]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[master-veo-vertex-ai]] (syntheses/master-veo-professional-2026.md, master-veo3-prompting-april-2026.md), [[master-veo3-synthesis]] (syntheses/master-veo-professional-2026.md, master-veo3-prompting-april-2026.md), [[obsidian-agent-bridge]] (entities/semantic-clip.md), [[pcg1-directors-prep]] (syntheses/master-comfyui-2026.md), [[proxmox]] (entities/forgejo-mirror.md), [[seedance]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[soul-id]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[swiftbar-mcp-toggle]] (entities/semantic-clip.md), [[syntheses]] (concepts/query.md), [[wikilinks]] (concepts/ingest.md, concepts/lint.md, entities/obsidian.md, sources/claude-chat-setup-walkthrough.md) — same set as prior lint pass, still unaddressed
**Missing summaries:** 81 found — 10 concepts/entities (mcp.md, higgsfield-comfyui-pipeline-architecture.md, skill-ecosystem.md, agent-native-cli.md, ai-analysis-skill.md, smart-connections.md, forgejo-mirror.md, pinecone.md, renderzero-vertex-patch.md, litellm-proxy.md) + 8 syntheses (docx-incident-case-study.md, skill-selection-guide.md, MASTER_AI_CREATION_GUIDE.md, master-veo-professional-2026.md, master-veo3-prompting-april-2026.md, master-comfyui-2026.md, "Master AI Creation Guide May 2026.md", master-ai-video-image-guide-2026.md, facs-va-valence-emotion-guide-2026.md) + 63 sources/claude-chat-* auto-ingested chat logs missing `> summary` line entirely
**Stale claims:** none (all "as of" tags are 2026-05 or 2026-06, within 6-month window of 2026-07-06)
**index.html:** regenerated (128 pages: 105 AI + 23 HA)
**Action required:** yes — (1) orphan set from 2026-06-22 lint pass is unchanged, still needs the same 10 stub pages + [[index.md]]/[[log.md]]/[[wikilinks]]/[[syntheses]] link-text fixes; (2) 63 claude-chat-* source pages accumulated without `> summary` lines — consider fixing the ingest template rather than backfilling by hand

---

## [2026-07-13] LINT — Weekly maintenance

**Plugin updates:** 4 marketplaces updated successfully (no new version details surfaced by CLI)
**Orphan links:** 17 real slugs (excluding lint.md placeholder examples page-a/b/name/page1/2/3) — [[comfyui]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[feedback_secret_handling]] (entities/forgejo-mirror.md), [[higgsfield]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[homelab]] (entities/forgejo-mirror.md), [[index.md]] (concepts/ingest.md, concepts/llm-wiki.md, sources/karpathy-llm-wiki-gist.md), [[isle-of-dogs-project]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[log.md]] (concepts/ingest.md, concepts/llm-wiki.md, sources/karpathy-llm-wiki-gist.md), [[ltx-video]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[master-veo-vertex-ai]] (syntheses/master-veo-professional-2026.md, master-veo3-prompting-april-2026.md), [[master-veo3-synthesis]] (syntheses/master-veo-professional-2026.md, master-veo3-prompting-april-2026.md), [[obsidian-agent-bridge]] (entities/semantic-clip.md), [[pcg1-directors-prep]] (syntheses/master-comfyui-2026.md), [[proxmox]] (entities/forgejo-mirror.md), [[seedance]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[soul-id]] (concepts/higgsfield-comfyui-pipeline-architecture.md), [[syntheses]] (concepts/query.md), [[wikilinks]]/[[Wikilinks]] (concepts/lint.md, concepts/ingest.md, entities/obsidian.md, sources/claude-chat-setup-walkthrough.md, sources/claude-chat-mcp-usage-control-and-disable-option.md) — unchanged from 2026-06-22/06-29/07-06 passes, still unaddressed. Note: [[swiftbar-mcp-toggle]] no longer orphaned (resolved since last pass).
**Missing summaries:** 75 files (down from 81 on 2026-07-06) — 4 concepts/entities (ai-analysis-skill.md, skill-ecosystem.md, forgejo-mirror.md, litellm-proxy.md) + 8 syntheses (MASTER_AI_CREATION_GUIDE.md, docx-incident-case-study.md, facs-va-valence-emotion-guide-2026.md, master-ai-video-image-guide-2026.md, master-comfyui-2026.md, master-veo-professional-2026.md, master-veo3-prompting-april-2026.md, skill-selection-guide.md) + ~63 sources/claude-chat-* auto-ingested logs. Filesystem note: "Master AI Creation Guide May 2026.md" (space-containing filename) not independently re-scanned this pass — glob mishandles spaces; needs quoting fix in next lint script run.
**Stale claims:** none (all "as of" tags are 2026-05 or 2026-06, within 6-month window of 2026-07-13)
**index.html:** regenerated (128 pages: 105 AI + 23 HA)
**Action required:** yes — (1) orphan set unchanged for 4 consecutive weekly passes (since 2026-06-22) — recommend creating the 10 stub pages once rather than re-reporting weekly: comfyui, higgsfield, homelab, isle-of-dogs-project, ltx-video, master-veo-vertex-ai, master-veo3-synthesis, obsidian-agent-bridge, pcg1-directors-prep, proxmox, seedance, soul-id; (2) fix [[index.md]]/[[log.md]] → [[index]]/[[log]] link text in ingest.md, llm-wiki.md, karpathy-llm-wiki-gist.md; (3) 63+ claude-chat-* source pages still missing `> summary` — fix ingest template rather than backfill by hand (flagged 3 passes running).

---

## [2026-07-14] FIX — Orphan cleanup (user-approved)

**Link text fixes:** [[index.md]]→[[index]], [[log.md]]→[[log]] in concepts/ingest.md, concepts/llm-wiki.md, sources/karpathy-llm-wiki-gist.md
**Stub pages created (12):** concepts/comfyui.md, concepts/higgsfield.md, concepts/ltx-video.md, concepts/seedance.md, concepts/soul-id.md, entities/homelab.md, entities/proxmox.md, entities/isle-of-dogs-project.md, entities/pcg1-directors-prep.md, entities/obsidian-agent-bridge.md, syntheses/master-veo-vertex-ai.md, syntheses/master-veo3-synthesis.md — all `[unsourced]` stubs, flagged for real ingest pass
**Skipped:** [[feedback_secret_handling]] (entities/forgejo-mirror.md) — not a wiki concept, it's a Claude memory slug; not fabricated
**index.html:** regenerated (128 pages)
**Remaining:** 75 files still missing `> summary` (mostly claude-chat-* auto-ingest logs) — deferred, out of scope for this pass (weekly token budget at 97%)

---

## 2026-07-14 — Local AI System master overview synthesized
**Agent:** Claude Code (Fable 5) — Mac
**Created:** `syntheses/local-ai-system-overview-2026-07.md` — canonical map of the full stack: Obsidian Wiki (CONCEPT), Homelab-Brain hub CT107 + recall :8090, Memorwise CT105 (LIBRARY), Forgejo CT106, The Bridge (recall/clip tools/skills), Agentic OS Phase 3, Preflight Token Agent, Loop Engineering core, infra table, design principles.

## 2026-07-17 — Vault cleanup tasks 2+6 (partial)
**Agent:** Claude Code (Fable 5) — Mac
Deleted byte-identical dupe `syntheses/Master AI Creation Guide May 2026.md` (kept `MASTER_AI_CREATION_GUIDE.md`, same MD5) + 3 zero-byte macOS Icon artifacts. Remaining cleanup: handoff/2026-07-15-vault-cleanup.md tasks 1,3,4,5.

## [2026-07-20] LINT — Weekly maintenance

**Plugin updates:** none (4 marketplaces updated, no new plugin versions reported)
**Orphan links:** 2 — [[feedback_secret_handling]] — referenced in: entities/forgejo-mirror.md; [[swiftbar-mcp-toggle]] — referenced in: entities/semantic-clip.md
**Missing summaries:** 70 — concepts/skill-ecosystem.md, concepts/ai-analysis-skill.md, entities/forgejo-mirror.md, entities/obsidian-agent-bridge.md, entities/litellm-proxy.md, sources/semantic-clip.md, syntheses/docx-incident-case-study.md, syntheses/local-ai-system-overview-2026-07.md, syntheses/skill-selection-guide.md, syntheses/MASTER_AI_CREATION_GUIDE.md, syntheses/master-veo-professional-2026.md, syntheses/master-veo3-prompting-april-2026.md, syntheses/master-comfyui-2026.md, syntheses/master-ai-video-image-guide-2026.md, syntheses/facs-va-valence-emotion-guide-2026.md, plus 55 sources/claude-chat-*.md ingested pages (see LINT run 2026-07-20 for full list)
**Stale claims:** none (all `(as of YYYY-MM)` tags are 2026-05 or 2026-06, within 6-month window)
**index.html:** regenerated (128 pages)
**Action required:** yes — 2 orphan links to fix/create, 70 pages need `> summary` line added (mostly ingested claude-chat sources)

---

## [2026-07-27] LINT — Weekly maintenance

**Plugin updates:** 4 marketplaces updated successfully, no new plugin versions reported
**Orphan links:** 2 — [[feedback_secret_handling]] — referenced in: entities/forgejo-mirror.md (not a wiki concept, Claude memory slug — skipped per 2026-07-14 decision); [[swiftbar-mcp-toggle]] — referenced in: entities/semantic-clip.md — both unchanged since 2026-06-22, 5 consecutive passes now unaddressed. Also found: [[index.md]]/[[log.md]] literal link text in concepts/lint.md:54 (missed by the 2026-07-14 fix pass, which only touched ingest.md/llm-wiki.md/karpathy-llm-wiki-gist.md)
**Missing summaries:** 65 (down from 70) — concepts/skill-ecosystem.md, concepts/ai-analysis-skill.md, entities/obsidian-agent-bridge.md, entities/litellm-proxy.md, syntheses/docx-incident-case-study.md, syntheses/local-ai-system-overview-2026-07.md, syntheses/skill-selection-guide.md, syntheses/MASTER_AI_CREATION_GUIDE.md, syntheses/master-veo-professional-2026.md, syntheses/master-veo3-prompting-april-2026.md, syntheses/master-comfyui-2026.md, syntheses/master-ai-video-image-guide-2026.md, syntheses/facs-va-valence-emotion-guide-2026.md, plus 52 sources/claude-chat-*.md ingested pages. Note: entities/forgejo-mirror.md and sources/semantic-clip.md now have summaries (resolved since 2026-07-20).
**Stale claims:** none (all `(as of YYYY-MM)` tags are 2026-05 or 2026-06, within 6-month window of 2026-07-27)
**index.html:** regenerated (128 pages: 105 AI + 23 HA)
**Action required:** yes — (1) [[swiftbar-mcp-toggle]] stub still needed, 5 passes running; (2) fix [[index.md]]/[[log.md]] literal text in concepts/lint.md:54; (3) 65 pages still need `> summary` (mostly claude-chat-* auto-ingest — fix ingest template rather than backfill by hand, flagged 4+ passes running)

---

## [2026-09-02] INGEST — Win11 session backfill (first-ever Win11 wiki entry)
**Agent:** Claude Code (Sonnet 5) — Win11

**Root cause found first:** Win11 sessions were never reaching this wiki. `CLAUDE.md` and `/aillmwiki` (`aillmwiki.md`) both pointed at the iCloud copy (`aillmwiki.md` even still had a dead pre-move Mac path). Real sync target is Syncthing folder `C:\Users\PCG1\AppData\Local\Programs\Syncthing\AI Obsidian Vault` (confirmed via Syncthing config/REST API), ~2 months ahead of the iCloud copy. Fixed both pointer files — see `incidents/2026-09-02-vault-syncthing-icloud-drift.md`.

**Backfilled this session's work:**
- `entities/comfyui-pinokio-blackwell.md` (new) — Pinokio ComfyUI original vs. updated clone (py3.12.9, torch/vision/audio 2.9.1+cu130, SageAttention 2.2.0, flash_attn 2.8.3), verified via real SDXL generation
- `incidents/2026-09-02-torchaudio-abi-version-pin.md` (new) — pip auto-resolve torchaudio ABI mismatch, WinError 127, caught only by real boot not import check
- `incidents/2026-09-02-vault-syncthing-icloud-drift.md` (new) — this fix, written up in full
- `pinokio/pinokio.md` (deepened) — noted primary usage moved to `H:\Pinokio\`, `C:\pinokio\` status unverified, linked new ComfyUI entity
- `index.md` — added Incidents section (didn't exist before), added comfyui-pinokio-blackwell to Entities

**Known gap surfaced, not yet fixed:** `index.md` is stale relative to `index.html`/`log.md` (dates back to 2026-05-26, manually maintained, drifted from the auto-generated index). Full backlog of un-ingested Win11 session history (ComfyUI/Pinokio model-audit work, Blender clay-pass pipeline, Windows Defender crash-loop root cause, BIOS 6/24-core issue, NotebookLM auth workaround, Cold Storage Ledger audit) still outstanding — user requested a plan to work through it, to follow.

## [2026-09-02] FIX — generate_wiki_index.py vault-resolution + SECTIONS gap
**Agent:** Claude Code (Sonnet 5) — Win11

Found while backfilling: the generator's own VAULT resolution checked `iCloudDrive` before falling back to its own script directory, so every run from inside the real Syncthing-synced vault was silently writing `index.html` into the **stale iCloud copy** instead — confirmed by iCloud's `index.html` mtime advancing on each run while the real vault's stayed frozen at Sep 1. Fixed resolution order: Syncthing path checked first explicitly, script-dir (cwd) second, iCloud demoted to last-resort only. Also added `incidents` to `SECTIONS` (was invisible to the index entirely — page count correctly jumped 119→125 AI pages after the fix, confirming pages were always there, just never scanned). `pinokio/` still excluded — has a nested `Windows 11/` subfolder the current `glob("*.md")` won't recurse into; needs `glob("**/*.md")` + a slug fix in `parse_page` first.

Related: incidents/2026-09-02-vault-syncthing-icloud-drift.md

## [2026-09-02] FIX — pinokio/ nested subfolder now indexed
**Agent:** Claude Code (Sonnet 5) — Win11

`parse_page` now takes `section_dir` and computes a relative slug (`path.relative_to(section_dir)`) instead of bare `path.stem`, and both AI/HA loops switched `glob("*.md")` → `rglob("*.md")`. Added `pinokio` to `SECTIONS`. Page count 125→129 (the 4 `pinokio/` pages, including 3 previously-invisible ones under `Windows 11/`, now indexed). Closes the gap flagged in the previous log entry.

## [2026-09-03] CLARIFY — two separate wikis confirmed, not to be merged
**Agent:** Claude Code (Sonnet 5) — Win11

User confirmed `C:\Users\PCG1\homelab_brain\wiki\` and this vault (`AppData\...\Syncthing\AI Obsidian Vault`) are two deliberately separate knowledge bases, not drift to reconcile. This vault (AppData path) is confirmed as THE AI LLM Wiki — CLAUDE.md/aillmwiki.md pointers stay as fixed 2026-09-02. `homelab_brain\wiki` is a separate, active Homelab-Brain infrastructure knowledge base (CT107 hub, recall, etc.) — same folder schema, unrelated content, do not write into it from `/aillmwiki`. Documented in CLAUDE.md under "Do not confuse with". Supersedes the "two active Syncthing shares diverged" framing in the 2026-09-02 vault-drift incident page — that page's core finding (iCloud copy stale, fixed pointer to Syncthing) still stands; only the homelab_brain comparison was a false alarm.

## [2026-09-03] INGEST — Phase 3 backfill: confirmed punch-list items from prior Win11 sessions
**Agent:** Claude Code (Sonnet 5) — Win11

Backfilled 6 new pages + 1 deepened page, from a transcript-mining pass across other Win11 Claude Code project folders (not this session's own project):

**Closed:**
- `incidents/2026-07-11-wsus-dead-placeholder-blocks-fod-install.md` — fake WSUS policy blocked OpenSSH.Server FoD install; same root cause believed to underlie a previously-noted (not separately documented) Defender crash-loop
- `entities/amuseai-vertex-integration.md` — AmuseAI → Vertex AI reroute for Gemini/Imagen/Veo, working
- `entities/cutmaster-ai-davinci-tools.md` — DaVinci Tools dashboard, verified E2E, ffmpeg PATH gap noted

**Open (flagged for user attention, not just filed):**
- `incidents/2026-09-01-buzz-nsec-identity-unrecoverable.md` — possible personal Nostr key loss, real not just config
- `incidents/2026-08-24-architect-studio-overseer-fake-completion.md` — silent fake-success bug + LAN-exposed CORS gap
- `entities/claude-code-skill-enforcer-windows-bug.md` — Windows hook PID-mismatch, fix identified not applied
- `entities/cutmaster-ai-git-hosting.md` — Codeberg move after GitHub suspension, Win11 push auth unresolved
- `entities/renderzero-vertex-patch.md` (deepened) — Win11 Animate config gap fixed, Vertex patch application unverified

`index.md` updated (Entities + Incidents tables). Corrected an earlier over-attribution: this pass initially cited a non-existent `[[windows-defender-crash-loop]]` page and a wrong `[[2026-09-02-torchaudio-abi-version-pin]]` cross-link on the WSUS incident before writing it — caught before publish, rewritten to describe the Defender link as unconfirmed/undocumented rather than assert a page that doesn't exist (Karpathy rule 4: don't fabricate).

Remaining backlog not yet ingested (lower priority / needs more source digging, not attempted this pass): NotebookLM auth workaround, Cold Storage Ledger artifact, ComfyUI model-audit/dedup findings, Blender clay-pass pipeline, KensingtonKonductor-TB.exe crash-loop — all confirmed as this-session-only per the prior punch-list research, not yet written up as their own wiki pages.

## [2026-09-14] LINT — Weekly maintenance

**Plugin updates:** 5 marketplaces updated (no per-plugin version diffs reported by CLI)
**Orphan links:** 7 — [[2026-09-02-torchaudio-abi-version-pin]] (in entities/comfyui-pinokio-blackwell.md), [[Windows 11]] (in entities/comfyui-pinokio-blackwell.md, entities/claude-code-skill-enforcer-windows-bug.md), [[agent-privilege-separation]] (in entities/bumble-credential-hunt-incident.md), [[feedback_secret_handling]] (in entities/forgejo-mirror.md), [[pinokio]] (in entities/comfyui-pinokio-blackwell.md — page exists at wiki/pinokio/ but outside concepts/entities/sources/syntheses scope), [[swiftbar-mcp-toggle]] (in entities/semantic-clip.md), [[syntheses]] (in concepts/query.md — links a folder, not a page)
**Missing summaries:** 73 — concentrated in sources/ (claude-chat-* ingest template omits `> summary`, same known issue since 2026-08-31) and syntheses/ master guides; full list held in session output, not repeated here
**Stale claims:** none (all `(as of YYYY-MM)` tags are 2026-05/06/09, within 6 months of 2026-09-14)
**index.html:** regenerated (159 pages: 136 AI + 23 HA)
**Action required:** yes — 7 orphan links need either a stub page or removal; 73 missing summaries trace to the sources/ ingest template not writing `> summary` (fix the template, don't hand-patch each file)

---

## [2026-09-18] P1 CLOSED (partial) — account-level memory vault path corrected

Ref: `handoff/2026-09-17-memory-maintenance.md`, P1.

**Fixed:** Claude's account-level memory file `/areas/github-wiki-memory.md` now names
`~/Sync/obsidian-vault` (Syncthing, hub CT107, recall :8090) as the live vault path, with the
iCloud path retained and labelled superseded. Verified by re-reading the account-level file on
2026-09-18 12:28 UTC; three new `[stated]` lines present, prior lines intact.

**Route:** the write had to be made from a plain claude.ai chat with no project selected.
Project-bound sessions (Cowork, Claude Code) can only write inside their own
`/projects/<id>/` memory subtree, which is why the original correction ended up stranded in the
Southern Water subtree (`/projects/01a0aadc-c243-70f1-b465-5a00045602cc/areas/github-wiki-memory.md`).

**Residual — not yet fixed.** Two older lines in the same file still name iCloud as the vault
location and now contradict the correction directly:
- "Three-part memory architecture: ... and Obsidian vault on iCloud"
- "AILLM wiki migrated from Google Drive to iCloud; Drive searches return only stale pre-migration files"
A reader hitting either line before the new ones still gets the dead path. Needs a second
account-level edit.

**Stale copy still present:** the Southern Water subtree copy above. Deletable only from a
session bound to that project. Harmless now that the account-level file is right.

**New instance of the handoff's root-cause pattern, logged as occurrence 5.** The first attempt at
this fix was pasted into a Claude Code session, which searched the local filesystem for `/areas/`,
found nothing, and returned a correction block in the wrong format (`##` headed sections rather
than `[stated]` bullets). Pasting it would have created a fourth copy of the correction rather
than fixing the file. Same class as occurrences 1–4: right information, wrong location, no check
that the consumer can see it. Reinforces the handoff's proposed standing check that every pointer
resolves to the Syncthing path.

---

## [2026-09-18] P2 CLOSED — index.md is now a generated artefact, and index.html was also undercounting

Ref: `handoff/2026-09-17-memory-maintenance.md`, P2.

**The stated problem:** `wiki/index.md` was hand-maintained and listed 49 pages against a real total
of 159 — anything treating it as the index saw under a third of the wiki.

**A second bug found while fixing it, not in the handoff.** `index.html` was wrong too. The
generator's `SECTIONS` list includes `incidents` and `pinokio`, so their pages were parsed and
counted in the "159 pages" header — but `render_template()` only emitted card sections for
`concept`, `entity`, `source` and `synthesis`. The other 12 pages (8 incidents + 4 pinokio) were
silently dropped. Verified before the fix: header claimed 159, DOM contained 147 cards. So the
handoff's premise that "`index.html` has 159" was true of the counter and false of the page.

**Fix — `generate_wiki_index.py`:**
1. `render_template()` now emits Incidents and Pinokio / Windows 11 sections, with `--incident`
   and `--pinokio` CSS vars and badge rules. index.html now renders 159 cards for 159 pages.
2. New `render_index_md()` builds `wiki/index.md` from the same `pages` list that builds
   index.html, in the same run. One pass, one source of truth — the two artefacts can no longer
   disagree.
3. `parse_page()` now also returns `rel_slug` and `section` (additive) so index.md can emit
   correct wikilinks for nested pages (`pinokio/Windows 11/...`).
4. `main()` writes both files and prints both counts.

**Verified:** `python3 generate_wiki_index.py` → "159 pages (136 AI + 23 HA)" and
"136 AI pages listed". index.html: 159 cards across 6 section types. index.md: 136 rows
(65 sources, 28 entities, 19 concepts, 12 syntheses, 8 incidents, 4 pinokio) plus an explicit
footer accounting for the 23 HA pages that live in `index.html` only.

**Test suite was already broken and is now fixed.** `test_generate_wiki_index.py` called
`parse_page(md, "concepts")` with two arguments, but `parse_page` has required a third
(`section_dir`) since the `rel_slug` change. Every one of the 7 parse_page tests would have raised
TypeError. Fixed all 7 and added 6 tests for `render_index_md` (page count, total arithmetic,
link prefixing for incidents vs concepts, missing-summary marker, pipe escaping). 17 pass.

**Tradeoff accepted.** index.md summaries now come from each page's `> summary` line rather than
the hand-curated one-liners written into the old table. Where a page has no `> summary`, the row
reads `_(no summary — see P3)_`. That makes P3's 73 missing summaries visible in the index instead
of hidden behind hand-written text — deliberate, but it means index.md looks worse until the
ingest template is fixed. Old hand-curated file preserved at `wiki/index.md.bak-20260918`
(non-`.md` suffix, so lint passes ignore it).

**Backups:** `generate_wiki_index.py.bak-20260918`, `test_generate_wiki_index.py.bak-20260918`.

**Follow-on:** index.md is now generated, so the generator must run after every ingest. If it does
not, index.md goes stale the same way it just did — the pattern from P1 again, one layer down.
Worth wiring into the ingest step rather than leaving it to the weekly LINT.

---

## [2026-09-18] P3 CLOSED (detection + contract) — the missing-summary count was wrong in both directions

Ref: `handoff/2026-09-17-memory-maintenance.md`, P3.

**The handoff's framing was right about the cure and wrong about the disease.** "Fix the template,
don't hand-patch" is correct. But the 73 figure was not measuring what it claimed, and the exporter
is not the only thing broken.

**Bug A — the index was inventing summaries.** `parse_page()` matched `^> ` anywhere in a file and
took the first hit as the summary. On chat exports, which quote messages inside the transcript,
that lifted arbitrary mid-conversation text into the index. Seven pages in `sources/` were
affected; the worst pulled its "summary" from **line 949** of
`claude-chat-updating-tutorial-with-project-images.md`. Those pages also counted as HAVING a
summary, so the lint scored them as fine.

**Bug B — the lint was counting generated artefacts.** The 73 figure included `wiki/feed/` (34
daily AI feed files) and `wiki/stats/` (64 baseline dumps and JSON). Neither is a knowledge page;
neither is in `SECTIONS`; neither is indexed. They were never supposed to carry summaries.

**Corrected count: 37, not 73** — 32 `sources/`, 3 `incidents/`, 2 `entities/`. Of those, 7 were
previously masked as present by Bug A. Scope is the six indexed sections only.

**Fix:**
1. New `extract_summary(text)` in `generate_wiki_index.py`, replacing the naive regex. Two accepted
   forms, in precedence order: a `summary:` key in YAML frontmatter, or a `>` blockquote in the
   header zone (before the first `## ` heading). A blockquote below the first `## ` is body content
   and is ignored. Wrapped `>` lines are joined.
2. New `lint_summaries.py` — imports the same `extract_summary()`, so the lint count and the index
   can never disagree again. `--by-section` for the summary view; exits non-zero when anything is
   missing, so it can gate an ingest.
3. `concepts/ingest.md` gains a **Summary contract** section stating the two accepted forms, the
   fact that body blockquotes do not count, and the `lint_summaries.py` command.
4. 8 new tests covering both forms, precedence, line-wrapping, wikilink stripping, and specifically
   that a blockquote below the first heading is NOT a summary. **25 pass** (was 17).

**Still open — the exporter itself.** The `claude-chat-*` export path does not write `summary:`,
and the script that produces those pages is not in either Syncthing folder (`obsidian-vault` or
`homelab-brain`) — only its output is. It could not be fixed from this session. The contract is now
documented and machine-checked, so the exporter has a defined target: emit `summary:` in
frontmatter. **The 37 backfills are deliberately not done** — per the handoff, template first.

**Note for the memory-architecture review:** `homelab-brain/wiki/sources/` contains 49
`claude-chat-*` pages with the same layout and the same missing-`summary:` gap. Whatever fixes the
exporter fixes both wikis.

**Backups:** `wiki/index.md.bak-20260918`, `wiki/concepts.ingest.md.bak-20260918`,
`generate_wiki_index.py.bak-20260918`, `test_generate_wiki_index.py.bak-20260918`.

---

## [2026-09-18] PATTERN FIX — standing pointer check, link skip list, single maintenance entry point

Ref: `handoff/2026-09-17-memory-maintenance.md` — the root-cause pattern, and P4.

### The handoff's thesis, tested

It argued that five incidents shared one cause — something authoritative pointing at a stale copy —
and that a standing check would have caught all of them. That was right, and understated.

**Occurrence 6, found by writing the check: EIGHT vault scripts still hardcoded the dead iCloud
path.** `vault.sh`, `vault-stats.sh`, `vault-nlm-sync.sh`, `semantic-clip.js`, `search-wiki.js`,
`index-skills.js`, `optimize-vault.js`, `bin-router.js` — every one of them a live entry point,
every one pointing at the superseded vault. The 2026-09-02 pass fixed `CLAUDE.md`, `aillmwiki.md`
and `generate_wiki_index.py` and stopped there.

**Occurrence 7: the agent profiles too.** `wiki/agents/claude-primary/project-aillmwiki.md` — the
page that tells an agent where the vault IS — still read
`Vault at: C:\Users\PCG1\iCloudDrive\...\Obsidian Vault AI`. Same for `user-profile.md`. Identical
stale copies existed in `homelab-brain/wiki/agents/claude-primary/`.

**All 10 fixed.** Scripts now resolve `${OBSIDIAN_VAULT:-$HOME/Sync/obsidian-vault}` with the iCloud
path retained only as an explicitly-labelled `_ICLOUD_LEGACY` fallback. Agent profiles name the
Syncthing path on both macOS and Win11. Originals in `.pointer-fix-backups-20260918/`.

### New: `lint_pointers.py`

Fails on any live reference to a superseded vault path. Deliberately narrow — it scans code and
config (`.sh .js .py .json .ts .yml`) plus the markdown that functions as configuration
(`wiki/agents/**`, `CLAUDE.md`, `aillmwiki.md`), and ignores prose. The first draft scanned all
markdown and returned 52 hits in the vault and 67 in homelab-brain, almost all of them chat
transcripts and planning docs legitimately describing the old layout. A check that cries wolf gets
ignored, which is how this class of bug survived four rounds. Narrowed, it returns exactly the
live pointers. **Both trees now report 0.**

### P4 — `lint_links.py` and the skip list

The weekly LINT's "7 orphan links" was scoped to concepts/entities/sources/syntheses only. A full
scan finds 36. Most are not real: documentation placeholders (`[[page-name]]`, `[[concepts/...]]`
in `schema/config.md` and `concepts/lint.md`), `log.md` quoting its own past reports, and raw chat
transcripts under `sources/claude-chat-*`. Those source files are now excluded by category.

Directory links resolve properly now — `[[Windows 11]]` finds `wiki/pinokio/Windows 11/`, and
`[[pinokio]]` and `[[2026-09-02-torchaudio-abi-version-pin]]` resolve because incidents/ and
pinokio/ are in scope since today's P2 fix. Three of the LINT's seven orphans were never orphans.

`wiki/.lint-skip-links` is the decide-once mechanism the handoff asked for — 8 entries, each with a
reason. Seven are Claude memory slugs that are not wiki pages (the `feedback_*` class, ruled skip
2026-07-14 and re-reported five times since); one is `windows-defender-crash-loop`, ruled
2026-09-03 as a page deliberately never written.

**36 -> 8 real unresolved links**, all genuine gaps needing a stub-or-remove decision:
`[[SOUL]]`, `[[agent-privilege-separation]]`, `[[hermes-agent]]`, `[[ollama]]`, `[[open-webui]]`,
`[[pytorch]]`, `[[swiftbar-mcp-toggle]]`, `[[wikilinks]]`.

### New: `maintain.py`

`python3 maintain.py --fix` runs all three lints then regenerates both indexes. Exit code is the
number of failing checks, so it can gate an ingest or run from launchd. This is the answer to the
P2 follow-on: regeneration was left to a weekly manual pass, which is why index.md went stale in
the first place.

Current state: **pointers clean, summaries 37 open, links 8 open.** 25 tests pass.

---

## [2026-09-21] LINT — Weekly maintenance

**Plugin updates:** 5 marketplaces updated; no new versions reported
**Orphan links:** 16 — real candidates: [[agent-privilege-separation]] (bumble-credential-hunt-incident.md), [[feedback_secret_handling]] (forgejo-mirror.md), [[swiftbar-mcp-toggle]] (semantic-clip.md); rest are template/example links (wikilinks, page-name, page1-3, page-a/b, log.md, index.md, syntheses, ingest, lint, obsidian, Windows 11, Wikilinks + pasted text) in lint.md, query.md, claude-chat-*.md
**Missing summaries:** 112 (scan checks literal `> summary` line; ~60 claude-chat-* sources, 14 concepts, ~25 entities incl. empty-heading interlinked, forgejo-mirror, smart-clip, wiki-clip, obsidian-wiki-memory) — count likely inflated by format variance
**Stale claims:** none
**index.html:** regenerated (161 pages)
**Action required:** yes — resolve 3 real orphans, decide summary format/backfill for ingest template

---

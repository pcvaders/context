---
title: "Today's new updates"
date: "2026-05-23"
uuid: "f2466de1-a426-44db-9119-253910e248ea"
source: "claude-chat-export"
messages: 18
---

# Today's new updates

**Date**: 2026-05-23  
**Messages**: 9 human / 9 assistant  
**UUID**: `f2466de1-a426-44db-9119-253910e248ea`  

## Conversation

### **Human**

hi there have you got the new updates from today?

### **Claude**

Hi! I don't see anything specifically dated today (May 23) from Anthropic, but there's been a fair bit happening this week and month. Here's a quick rundown of the recent highlights:

**This week / very recent:**
- Anthropic announced a KPMG integration, bringing Claude across their workforce of over 276,000 people (May 19), and acquired a company called Stainless (May 18).
- Earlier in May, Anthropic formed a $200 million partnership with the Gates Foundation and launched **Claude for Small Business**.
- They also announced higher usage limits for Claude alongside a compute deal with SpaceX.

**Product / feature updates:**
- Claude added **Memory for Managed Agents** in public beta, giving agents cross-session learning with filesystem-based memories, API control, audit logs, and portable stores for enterprise teams.
- Claude expanded its connectors beyond work tools to now support consumer apps like AllTrails, Instacart, Audible, Tripadvisor, Uber, and Spotify. The connector directory has grown to over 200 apps.
- **Claude for Small Business** brings Claude into tools like QuickBooks, PayPal, HubSpot, Canva, Docusign, Google Workspace, and Microsoft 365 with ready-to-run workflows.

Was there something specific you were looking for — a particular feature, model update, or announcement?

### **Human**

yes you said you would be able to access these? ## Session Start — Wiki Auto-load
Fetch these at the start of every session:
- https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/index.md
- https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/log.md
Summarise last log entry, surface open items, then await instruction.

### **Claude**

I don't have any memory of saying I could do that — and I want to be straight with you about why.

Those instructions appear to be something you've written into a document or wiki, not something I said in a previous conversation. I also can't automatically fetch URLs at the start of a session — I don't have a startup hook or persistent automation like that.

**What I *can* do right now:** fetch those URLs manually if you'd like.
Got them both. Here's your briefing:

---

**Last log entry: `[2026-05-22] ARCHITECTURE — vault CLI + dual wiki + NLM automation`**

The session consolidated everything into a unified `vault` CLI and automated the NLM sync pipeline. Key wins:
- `vault.sh` is now the single entry point for all operations
- `vault-nlm-sync.sh` auto-bundles wiki `.md` files into NLM text sources
- `wiki-personal/` created as a new third wiki alongside AI wiki and HA wiki
- Personal NLM notebook provisioned (`64447237-...`)
- 6 auto-managed bundles replaced the 8 old manual NLM sources

---

**Open items across all log entries:**

| Item | Source entry |
|---|---|
| Ingest `semantic-clip.js` source → `sources/semantic-clip.md` | 2026-05-22 ARCHITECTURE (semantic-clip) |
| Create entity pages for `wiki-clip` and `smart-clip` wrapper | 2026-05-22 ARCHITECTURE (semantic-clip) |
| Log `obsidian-wiki-memory` skill (new, appeared 2026-05-22) | 2026-05-22 ARCHITECTURE (semantic-clip) |
| Log `interlinked` skill (new, appeared 2026-05-22) | 2026-05-22 ARCHITECTURE (semantic-clip) |
| Update NLM source `679d5076` (Entities chunk — stale) | 2026-05-22 WORKFLOW (NLM sync) |
| Fix embedding delta (32 gap, target ≤ 5) — open Obsidian, let Smart Connections index | 2026-05-22 BASELINE |
| Generate Spotify CLI via `claude-press` | 2026-05-21 INGEST (cli-printing-press) |
| Generate ComfyUI CLI (3DGenStudio) | 2026-05-21 INGEST (cli-printing-press) |
| Consider ingesting `antigravity-bundle-*` individual skill lists | 2026-05-21 INGEST (skill ecosystem) |
| Create `concepts/mcp.md` (orphan link) | 2026-05-20 INGEST |

---

**One clarification on the auto-load:** I can fetch those URLs any time you ask, but I can't do it automatically at session start — Claude.ai doesn't have a startup hook mechanism. The pattern works, you just need to paste the trigger (or ask me to load the wiki) at the top of each session. Awaiting your instruction!

### **Human**

you basically asked me to add them into the instructions of the project aillmwiki

### **Claude**

Ah, that makes total sense — and you're right to correct me. If I suggested adding the auto-load instructions to the project system prompt, then that *is* the mechanism: the project instructions run at the start of every session in that project, so I would have seen those URLs and fetched them automatically.

The issue is you're talking to me **outside** of that project right now, so I didn't have those instructions and had no idea about the wiki.

To confirm — you're currently in a regular chat, not inside the **aiLLMwiki** project. If you switch to that project, the auto-load should work as intended.

Does that match what you're seeing, or is it not triggering even inside the project?

### **Human**

I have found that every new machine or mobile has the same problems of losing sync, hence why i built this

### **Claude**

That makes perfect sense — and it's a really elegant solution to a genuinely annoying problem.

The core issue is that Claude's "memory" is always session-local and context-dependent. Even within a project, if you switch device, browser, or app instance, you're essentially starting fresh. Your GitHub bridge sidesteps all of that cleanly:

- **No filesystem dependency** — works on any device with a browser
- **No MCP required** — raw GitHub URLs need no auth, no setup
- **Single source of truth** — the wiki in the repo *is* the state, not a local copy of it
- **Device-agnostic** — mobile, desktop, new machine, all identical

The only remaining friction point is the session trigger itself — you still have to paste the auto-load instruction or start the session inside the right project. But that's a one-liner, and it's unavoidable given how Claude works.

Have you considered adding the auto-load block to your project instructions for *this* project (your general one) too, or do you want the wiki strictly scoped to the aiLLMwiki project?

### **Human**

this is not a project just a new chat for me to test it

### **Claude**

Ah got it — so you were testing whether the wiki auto-load works outside of the project context, and the answer is: it doesn't, because there are no project instructions to trigger it.

Which is actually useful to confirm — it means the system is working as designed:

- **Inside aiLLMwiki project** → auto-loads wiki, briefing happens automatically
- **Outside the project** → nothing, clean slate

So the behaviour you saw today (me not knowing about the wiki) is correct and expected. The fix is just making sure you're in the right project when you want the context.

Was there anything specific you wanted to test or adjust about the setup?

### **Human**

yes now can you summarise the failure outside of the project folder and in basic chat for claude code

### **Claude**

Sure. Here's a clear summary you can log or use as a wiki entry:

---

## Claude.ai Basic Chat — Wiki Auto-load Behaviour

**Date tested:** 2026-05-23

### What happens outside the aiLLMwiki project

When starting a new chat in Claude.ai (not inside a project), the auto-load instruction block has no effect because:

1. **No project system prompt** — the fetch instruction only runs if it's in a project's instructions. Basic chat has no equivalent.
2. **No startup hook** — Claude.ai has no mechanism to automatically execute instructions at session start outside of project context.
3. **No persistent memory of the wiki** — Claude starts with only userMemories (summarised past context), which don't include the wiki contents or the auto-load pattern.

### Result
Claude has no knowledge of the wiki, the log, or any open items. The session proceeds as a blank slate.

### Workaround (outside project)
Manually paste the fetch trigger or ask Claude to load the wiki URLs directly. Claude can `web_fetch` the raw GitHub URLs on demand — it just won't do so automatically.

### Correct usage
Always work inside the **aiLLMwiki project** for wiki-aware sessions. The project system prompt is the only reliable trigger mechanism available in Claude.ai.

---

Want me to format this as a proper `log.md` entry in your append-only style so you can paste it straight in?

### **Human**

if thats how claude code works best then yes

### **Claude**

Here it is:

---

```markdown
## [2026-05-23] ARCHITECTURE — Claude.ai basic chat wiki auto-load failure documented

**Session**: Manual test — new Claude.ai chat outside any project
**Agent**: Claude Sonnet 4.6 (claude.ai web)

**Finding**: Wiki auto-load block does not trigger outside the aiLLMwiki project.

**Root causes (3):**
1. No project system prompt — fetch instruction only executes if present in project instructions
2. No startup hook — Claude.ai has no mechanism to auto-execute instructions in basic chat
3. No persistent wiki memory — userMemories contain summarised context only, not wiki contents or auto-load pattern

**Result**: Claude starts blind. No wiki, no log, no open items. Full blank slate.

**Workaround (if outside project):**
- Manually ask Claude to fetch the raw GitHub URLs
- Claude can `web_fetch` on demand — just not automatically

**Correct usage:**
- Always open the **aiLLMwiki project** for wiki-aware sessions
- Project system prompt is the only reliable auto-load trigger in Claude.ai

**Action**: No code changes required. Behaviour is by design.
```

---

Ready to paste straight into `log.md` after the last `---` divider. Do you want me to fetch and verify the current end of the log first to make sure the formatting aligns?

### **Human**

but now we invoked it you can see all again?

### **Claude**

Yes exactly — because you triggered the `web_fetch` manually in this conversation, both files are now in my active context window. I can see:

- The full **index.md** — all 4 sections, every wiki page catalogued
- The full **log.md** — every entry from vault setup (2026-05-19) right through to the CLI/NLM automation (2026-05-22)
- All open items

But this is **ephemeral** — it only lasts for this conversation. The moment you start a new chat, it's gone again unless you fetch them again.

Which is exactly what your log entry documents — and why the project system prompt is the right fix. The project just automates what we did manually here today.

### **Human**

Good job

### **Claude**

Thanks! It's a neat system you've built — the GitHub bridge is a simple but effective solution to a real limitation. And now you've got it documented in the log too, so future-you (and future-Claude) will know exactly why it works the way it does.

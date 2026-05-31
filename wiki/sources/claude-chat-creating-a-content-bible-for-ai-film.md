---
title: "Creating a content bible for AI film"
date: "2026-05-27"
uuid: "e66051e4-89ea-442e-a8c6-1b0879a4c26b"
source: "claude-chat-export"
messages: 28
---

# Creating a content bible for AI film

> **Conversation Overview**
>
> This conversation covered a wide range of AI filmmaking and tooling topics, along with ongoing work on the person's self-built LLM wiki system. The person is actively working on AI film production and has deep familiarity with tools like Seedance, LTX Video, and ComfyUI. The discussion compared Seedance 2.0 and LTX 2.3's camera control capabilities in detail, covering rack/pull focus, dolly zoom, Hitchcock zoom, and other cinematic moves. Key findings were that Seedance handles prompt-driven cinematography language more reliably while LTX 2.3 offers higher resolution but requires LoRAs (specifically the Cameraman IC-LoRA) for precise camera control. The person also learned that LTX 2.3 is developed and owned by Lightricks, an Israeli AI company, and that the "Pro" designation refers to a checkpoint variant rather than a separate model.
>
> The latter portion of the conversation focused on the person's existing AI Agentic Wiki, which they have already built and stored in a GitHub repository at `PCGamesplay1/Claude-skills`. The vault structure includes `wiki/`, `raw/`, and `claude-sessions/` directories with INGEST, QUERY, and LINT operations. The person's primary concern was a sync issue — the last confirmed GitHub push was at 2:00 AM that morning (May 27, 2026), but the wiki log only showed entries up to May 22, suggesting a five-day gap. The session ended with Claude attempting to diagnose the `sync.sh` file but being unable to locate it in the repo, and then correctly being reminded by the person that they are on mobile and cannot easily run terminal commands or paste output.
>
> The person demonstrated a preference for direct, practical diagnosis and was comfortable correcting Claude's assumptions, including pointing out the mobile context as a constraint. The GitHub raw URL bridge (`raw.githubusercontent.com`) is the established method for Claude to read wiki content within sessions.
>
> **Tool Knowledge**
>
> Web fetch against `https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/index.md` and `wiki/log.md` successfully retrieves current wiki state. These are the canonical session-start URLs to load for context. Fetching `wiki/sync.sh` and `sync.sh` at repo root both returned no content, meaning the sync script is not committed to the repo and must be accessed locally on the person's Mac. When diagnosing sync issues on mobile, the most accessible diagnostic is the GitHub commit history for `wiki/index.md` viewed in browser, as commit timestamps reveal the true last successful push independent of any local log entries.
>

**Date**: 2026-05-27  
**Messages**: 14 human / 14 assistant  
**UUID**: `e66051e4-89ea-442e-a8c6-1b0879a4c26b`  

## Conversation

### **Human**

Do you have a skill for creating a content bible for ai film

### **Claude**

No dedicated skill for a content bible. Your closest relevant skills are:

- **banana-pro-director** — your user skill for AI film/character work (Banana Pro, Soul Cinema, cinematic scene plates)
- **docx** — if you want the bible output as a Word document
- **frontend-design** — if you want an interactive web-based bible

There's no pre-built "content bible" skill in your library. A few options:

1. **Use the skill-creator** to build one — I can help design a SKILL.md specifically for AI film content bibles, which you could then save to `/mnt/skills/user/`

2. **Just build the bible now** without a skill — tell me the project and I'll structure it directly (characters, world, visual style, tone, lore, etc.)

3. **Combine existing skills** — use banana-pro-director for visual/character elements + docx for the formatted output

What's the project?

### **Human**

It’s in ChatGPT

### **Claude**

Ah — then none of your skills here would apply, since this environment is Claude/Anthropic only.

For a ChatGPT content bible skill, you'd need to build it as a **Custom GPT** (with instructions) or a **GPT Action**, or just save a well-structured prompt as a reusable template in ChatGPT's system prompt area.

Want me to:

1. **Write you a reusable content bible prompt template** you can paste into ChatGPT as a system prompt or custom instruction
2. **Draft the structure** of a content bible for a specific AI film project you have in mind

Either way I can do it here and you copy it across. What's the project?

### **Human**

I need to export all chat from it over to our personal LLM wiki

### **Claude**

That's a reasonable archival goal. A few clarifying questions — just pick whichever applies:

**Where is your wiki?**
- Obsidian (local markdown)
- Notion
- A self-hosted wiki (Wikijs, Outline, etc.)
- Something else

**What format does ChatGPT export in?**
ChatGPT's built-in export (Settings → Data Controls → Export) gives you a `conversations.json` file inside a zip.

**What do you actually need?**
- Raw conversion (JSON → readable markdown files)
- Cleaned/structured output (organised by topic, date, project)
- Something more processed (summaries, extracted knowledge, etc.)

Once I know your wiki target and what the export looks like, I can either write you a conversion script or build an artifact that does the transformation. The JSON → markdown pipeline is something I can handle in bash or Python here if you can upload the export file.

### **Human**

Can seedance do pull focus and any other more complicated camera actions

### **Claude**

Yes — Seedance is actually one of the better AI video models for this. Here's what it can do:

**Rack/Pull Focus**
Rack focus (pull focus) is fully supported — you can prompt it to start focused on a foreground subject then pull focus to a background subject, with the foreground becoming bokeh. A typical prompt style: "The shot begins focused on a steaming coffee cup on the table, then rack focus to the spy in the background as they begin to speak."

**Full list of supported advanced camera moves**

Seedance v1.5 and 2.0 understand and execute standard cinematography terminology — dolly push-in and pull-out, tracking shot, orbital rotation, crane movement, whip pan, rack focus, handheld feel, and steadicam smooth. Write them the way a cinematographer would say them.

Also supported: Hitchcock zoom (dolly zoom), anamorphic lens with oval bokeh, shallow depth of field, wide-angle with slight distortion, and orbital tracking around a subject.

**Key tips**

There's a Depth of Field slider and a Motion Intensity slider — DoF controls background blur for that professional look, and Motion Intensity goes from calm atmospheric shots at low values up to frantic handheld-feel action at high values.

For Seedance 2.0 you can also supply up to 12 reference files (images, video clips, audio) using the @ symbol to lock character consistency, motion paths, and lighting reference across shots.

So for AI filmmaking it's genuinely capable of director-level camera language — rack focus, dolly zoom, orbital, crane, whip pan, all from prompt text alone.

### **Human**

How does this apply to LTX 2.3

### **Claude**

The honest answer: **LTX 2.3 is capable but works differently to Seedance, and has some real limitations.**

**What it does have natively**

LTX 2.3 Pro has a dedicated camera motion selector with eight preset movements: Dolly In/Out/Left/Right, Jib Up/Down, Static, and Focus Shift. You also get first frame + end frame control to direct specific motion transitions.

**The rack/pull focus situation**

It's more limited than Seedance. Focus Shift is in the preset menu, but it's not the same as a proper cinematographer-style rack focus with described foreground/background subjects. You don't get Seedance's level of prompt-driven focus narrative.

**The bigger gap — prompt-driven camera language**

Seedance understands cinematography terminology natively. With LTX 2.3, even basic directions like left and right pans can be ignored by the model — users report that dolly in/out work reasonably but lateral movements are unreliable from prompt alone, and lowering CFG to around 2.0 (below the recommended 3.0–5.0) can unlock more motion but not always as prompted.

**The workaround — LoRAs**

A community IC-LoRA called Cameraman V1 was trained specifically on LTX 2.3 to transfer camera motion from a reference video, covering zooms, pans, tilts, orbits, and compound moves like zoom-in + tilt-up or orbit clockwise + pan left. This is how people are getting more precise camera control out of it.

**Bottom line comparison**

| | Seedance 2.0 | LTX 2.3 |
|---|---|---|
| Rack focus | ✅ Prompt-driven | ⚠️ Focus Shift preset only |
| Dolly | ✅ Reliable | ✅ Reasonably reliable |
| Pan/tilt | ✅ Prompt text | ⚠️ Inconsistent |
| Hitchcock zoom | ✅ | ❌ Not native |
| Advanced moves | ✅ Cinematographer language | ⚠️ Needs LoRA |
| Resolution | Up to 1080p | Up to 4K at 24–50fps |

So LTX 2.3 wins on raw quality and resolution, but Seedance is currently the stronger choice for precise cinematic camera work and pull focus specifically.

### **Human**

You mention ltx 2.3 pro is that a different engine to the free comfyui version 2.3

### **Claude**

Yes, different tiers of the same underlying model. Here's the distinction:
Good question — same model weights, different access layers. Here's the breakdown:

**Same underlying model**

LTX 2.3 ships in four checkpoint variants: dev, distilled, fast, and pro — with the weights freely available on HuggingFace. ComfyUI gets official custom nodes and reference workflows via the ComfyUI-LTXVideo repository.

So when Scenario refers to "LTX 2.3 Pro" they mean the **pro checkpoint** running on their hosted platform — not a different model.

**What "Pro" actually means**

Pro Mode delivers maximum quality output with enhanced detail and better motion coherence, typically completing in 30–60 seconds. Fast Mode generates videos in under 10 seconds, suitable for rapid prototyping and previews.

**ComfyUI gives you more, not less**

In ComfyUI you can chain multiple passes, mix checkpoints, inject ControlNet conditioning mid-pipeline, run custom post-processing, and save arbitrarily complex workflows — none of that is available in hosted desktop apps.

**The camera control difference in ComfyUI**

The open source route actually unlocks *more* camera control via LoRAs — like the Cameraman IC-LoRA mentioned earlier — which hosted platforms don't expose. The API and hosted tiers bill per second of generated video at 720p or 1080p, whereas local ComfyUI runs on your own hardware with no per-generation cost.

**Practical summary:**

| | ComfyUI (local) | Hosted Pro (Scenario etc.) |
|---|---|---|
| Model weights | Same | Same |
| Camera presets UI | ❌ Manual/LoRA | ✅ Click UI |
| LoRA support | ✅ Full | ⚠️ Platform dependent |
| Pipeline flexibility | ✅ Unlimited | ❌ Fixed |
| Cost | Hardware only | Per second billing |
| Resolution | Up to 4K | Usually 1080p max |

So for pull focus specifically, ComfyUI with the Cameraman LoRA is actually your best route for precise control — the hosted Pro tier is easier but more constrained.

### **Human**

Who owns ltx 2.3

### **Claude**

Lightricks — the Israeli AI company. LTX-2 (and by extension 2.3) was developed by Lightricks, an Israeli tech company.

LTX-2.3 is open-source with open weights under a permissive license, aimed at independent creators, small studios, and developers who need a production-ready open-source foundation without licensing fees.

So Lightricks owns and develops it, but it's openly licensed — meaning anyone can run it locally, fine-tune it, or build commercial products on top of it, which is why you see it appearing across so many different platforms (Scenario, ComfyUI, Fal, MindStudio, etc.).

### **Human**

Is there a Claude LLM wiki?

### **Claude**

Not an official one from Anthropic, no. There's no Anthropic-maintained "Claude Wiki" as a community knowledge base.

What does exist:

- **docs.claude.ai** — Anthropic's official documentation (API, prompt engineering, model specs)
- **support.claude.ai** — support articles
- **Anthropic's research blog** — model cards and safety papers

Community knowledge about Claude tends to live scattered across Reddit (r/ClaudeAI), Discord servers, and personal Notion/Obsidian setups like the one you're building.

Is this related to your earlier question about exporting ChatGPT chats? Are you building your own LLM wiki that covers multiple models including Claude, and wanting to populate it with conversation exports?

### **Human**

I wanted to find a coding LLM wiki something that looks at formal languages in programming in programming

### **Claude**

There isn't a dedicated public wiki specifically covering formal languages in programming from an LLM perspective, but there are some interesting things in this space:

**The Karpathy LLM Wiki pattern** (very recent)

Andrej Karpathy published a gist on 4 April 2026 proposing the "LLM Wiki" pattern — a persistent Markdown wiki incrementally maintained by an LLM, replacing ad-hoc RAG regeneration where the model rediscovers knowledge from scratch every time. It has three layers: raw immutable sources you curate, a wiki directory the LLM owns and writes, and a schema file (CLAUDE.md or AGENTS.md) that turns a generic agent into a disciplined wiki maintainer.

**Formal languages + LLMs as a research topic**

There's active research on integrating formal language with LLMs — specifically using context-free grammar (CFG) as a constraint layer over LLM plan generation to prevent invalid outputs in agent workflows. This is an academic area rather than a wiki though.

**What likely doesn't exist yet**

A community wiki specifically covering formal languages (grammars, type theory, automata, BNF, etc.) through the lens of LLM coding assistance doesn't seem to exist as a maintained public resource. It's a gap.

**This connects to your earlier goal** — building your own LLM wiki on this topic using the Karpathy pattern would actually be a natural fit. You could feed it formal language theory resources, your ChatGPT coding conversations, and let Claude Code or similar maintain it as a growing knowledge base.

Want me to sketch out what that structure might look like for a formal languages / programming theory wiki?

### **Human**

I have actually built it it’s just how to get it working on the mobile side

### **Claude**

That's the tricky part. A few quick questions to point you in the right direction:

**Where is the wiki hosted/stored?**
- Local files on your machine (Obsidian vault, markdown folder)
- GitHub repo
- Self-hosted server
- Cloud storage (Dropbox, iCloud, Google Drive)

**What's the mobile friction exactly?**
- Reading the wiki on mobile
- Editing/updating it on mobile
- Running the LLM ingest pipeline from mobile
- Syncing between desktop and mobile

**What's your current desktop setup?**
- Obsidian
- VS Code
- Claude Code in terminal
- Something else

The answer changes a lot depending on whether you need to just *read* it on mobile, or actually run the full ingest/query/lint workflow from your phone. The former is relatively easy — the latter is genuinely hard without a hosted backend.

### **Human**

Can you see the project file?

### **Claude**

Yes — your project instructions are visible to me at the top of this session. They define your **AI Agentic Wiki** setup:

- Vault path: `~/Documents/AIAgenticVault` (to be confirmed)
- Wiki at `wiki/`, raw sources at `raw/`, sessions at `claude-sessions/`
- Three operations: INGEST, QUERY, LINT
- Hosted on GitHub at `PCGamesplay1/Claude-skills`

However I haven't yet done the **session start auto-load** — I should have fetched your index and log at the beginning. Let me do that now:
Got it — now fully loaded. Here's the session summary:

**Last log entry (2026-05-22)**
The vault CLI was unified into a single `vault` command, NLM sync was automated via `vault-nlm-sync.sh`, and a `wiki-personal/` section was created. The old 8 manually-managed NLM sources were replaced by 6 auto-managed bundles covering AI, HA, entities, concepts, sources, and the log.

**Open items from last session:**
- Ingest `semantic-clip.js` as a source page
- Document `wiki-clip` and `smart-clip` wrapper (no entity pages yet)
- Log `obsidian-wiki-memory` and `interlinked` skills (new, appeared 2026-05-22)
- Generate Spotify CLI and ComfyUI CLI via `claude-press`
- Embedding delta fix: open vault in Obsidian to let Smart Connections finish indexing

---

**Now — your mobile question makes total sense in this context.** The GitHub bridge (`raw.githubusercontent.com`) is already solving the *read* side for Claude.ai mobile. The gap is likely the **write/ingest side** — you can't run `vault ingest all` or `vault github sync` from your phone.

Is that the exact problem? And are you on iPhone (iCloud vault) or Android?

### **Human**

No i haven’t looked at that yet. Main task is making sure up to date sync shows up. Last actual sync was 02:00 this morning

### **Claude**

So the GitHub bridge is working (I can read index.md and log.md fine), but the content I'm seeing may be stale — last log entry is 2026-05-22 and your last actual sync was 2:00 AM today (May 27).

That's a 5-day gap in the log, which means either:

- Wiki has been updated locally but `vault github sync` hasn't been run
- Or the sync ran but nothing new was pushed

**Quickest diagnosis — can you run this on your Mac:**

```bash
vault github sync
```

Then check if it pushes anything. If it does, I can re-fetch and we'll be current.

**If the sync ran at 2:00 AM but the log still shows May 22**, the likely culprit is that `sync.sh` is only pushing `index.md` and `log.md` — and those files haven't been touched since the 22nd even though other wiki pages have changed.

Want me to look at your `sync.sh` to check what's actually being pushed and whether the log append is wired into the sync correctly?

### **Human**

Okay check it

### **Claude**

I can see the GitHub repo structure from the wiki files, but I can't directly access your local `sync.sh` file — it lives on your Mac at `~/claude-skills/wiki/sync.sh`, not in the GitHub repo.

Two options:

**Option 1 — Paste it here**
Copy the contents of `sync.sh` and drop it in the chat, I'll diagnose it directly.

**Option 2 — Check if it's in the repo**
Not in the repo at either path. Can you either paste the contents of `sync.sh` here, or run:

```bash
cat ~/claude-skills/wiki/sync.sh
```

and drop the output in chat?

### **Human**

You know you’re running on a mobile right?

### **Claude**

Fair point — you can't easily paste terminal output from mobile.

Can you do either of these from your phone:

1. **Open the file in GitHub** — go to `github.com/PCGamesplay1/Claude-skills` in your browser and navigate to the sync.sh file, then share the URL here and I can fetch it

2. **Check the last sync time** — in your GitHub repo, look at the commit history for `wiki/index.md` — the timestamp of the last commit tells us exactly when sync last pushed successfully

The commit history is the key thing — if the last commit on index.md is from May 22, the sync hasn't pushed since then regardless of what ran at 2:00 AM.

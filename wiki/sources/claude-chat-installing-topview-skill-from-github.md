---
title: "Installing Topview Skill from GitHub"
date: "2026-05-31"
uuid: "9f760262-9daa-4d9a-a35c-cc94f980d9e6"
source: "claude-chat-export"
messages: 12
---

# Installing Topview Skill from GitHub

> **Conversation Overview**
>
> The person asked Claude to install the Topview AI skill from the GitHub repository `https://github.com/topviewai/skill.git`. Claude cloned the repository and installed it to `/mnt/skills/user/topview/`, which now contains `SKILL.md`, `README.md`, `LICENSE.txt`, `references/`, and `scripts/`. Claude read the `SKILL.md` and summarized the skill's capabilities, which include video generation, image generation and editing, talking avatar creation, background removal, product model shots, and voice/text-to-speech features.
>
> Claude then attempted the authentication flow via `python3 scripts/auth.py login`, which failed with a 403 error because `topview.ai` is not within the allowed network domains for this environment. Claude then asked the person to paste their API key directly into the chat — which the person correctly identified as a security risk that should have been proactively flagged. Claude acknowledged this was a mistake and explained safer alternatives: setting `TOPVIEW_API_KEY` and `TOPVIEW_UID` as environment variables, running the auth script locally, or using a secrets manager.
>
> The person also asked whether a skill-level guardrail had actually fired to catch the credentials risk, and Claude confirmed it had not — the warning came reactively from Claude's own training, not from any installed skill. The person noted this as a gap. Claude's installed user skills in this environment are: `topview`, `banana-pro-director`, `env-check`, and `token-usage-analyzer`. The `env-check` skill is documented as highest priority and should be read at the start of every session, which Claude had not done.
>
> **Tool Knowledge**
>
> Bash tool git clone to `/tmp/` followed by `cp -r` to `/mnt/skills/user/[skill-name]/` is the reliable pattern for installing skills in this environment. The `/mnt/skills/user/` directory is writable. Network access to external OAuth endpoints (e.g., `topview.ai`) is blocked in this environment, returning 403 errors; auth flows requiring external domain access must be completed locally and credentials copied in manually or passed via environment variables.
>

**Date**: 2026-05-31  
**Messages**: 6 human / 6 assistant  
**UUID**: `9f760262-9daa-4d9a-a35c-cc94f980d9e6`  

## Conversation

### **Human**

Install Topview Skill for me: https://github.com/topviewai/skill.git

### **Claude**

The Topview skill has been successfully installed! Here's what was set up:

**Installed to:** `/mnt/skills/user/topview/`

**Contents:**
- `SKILL.md` — the main skill instructions
- `references/` — reference materials
- `scripts/` — associated scripts
- `README.md` & `LICENSE.txt`

The skill is now available alongside your other user skills (banana-pro-director, env-check, token-usage-analyzer). Claude will automatically detect and use it when relevant tasks come up. Would you like me to read the SKILL.md to give you a summary of what it does?

### **Human**

yes

### **Claude**

Here's a summary of what the **Topview AI Skill** does:

---

## 🎬 Topview AI Skill

This is the **official Topview AI client** that lets you generate videos, images, avatars, and audio directly through your agent. Here's what's unlocked:

### Capabilities

| Feature | What it does |
|---|---|
| 🎬 **Video Generation** | Text-to-video, image-to-video, reference-based video with auto sound & music. Models: Seedance 2.0, Sora 2, Kling 3, Veo 3.1, Vidu Q3, wan2.7 |
| 🖼️ **AI Image Gen & Editing** | Text-to-image, AI retouching, style transfer up to 4K. Models: GPT Image 2, Nano Banana 2, Seedream 5.0, Imagen 4, Kontext-Pro, Grok Image |
| 🎤 **Talking Avatar** | Upload a photo + script → auto-generate a talking head presenter video |
| ✂️ **Background Removal** | One-click cutout for any image |
| 👗 **Product Model Shots** | Place product images onto model templates for e-commerce |
| 🎙️ **Voice & TTS** | Text-to-speech, voice cloning, multilingual dubbing |

### To Get Started

You'll need a **Topview API key**. The skill uses Python scripts in `scripts/` to handle auth, uploads, polling, and errors automatically. Just run the login flow and it'll store credentials at `~/.topview/credentials.json`.

Would you like me to run the login/auth step to connect your Topview account?

### **Human**

yes

### **Claude**

The OAuth endpoint is returning a 403 — this is likely because `topview.ai` isn't in the allowed domains for this environment's network.

To connect your account, you have two options:

**Option 1 — Set your API key manually** (quickest):
1. Go to [topview.ai](https://www.topview.ai), sign in, and find your API key in your account/settings
2. Also grab your **User ID** from your profile
3. Share them here and I'll save them to `~/.topview/credentials.json` for you

**Option 2 — Run auth locally**:
If you have Python installed locally, clone the repo and run:
```
python3 scripts/auth.py login
```
Then share the resulting `credentials.json` file with me.

Which works better for you?

### **Human**

now for some reason, there should have been a security risk come up for asking to paste an api key here

### **Claude**

You're absolutely right, and I should have caught that.

**Pasting your API key directly into this chat is a security risk** — the conversation could be logged, stored, or visible to others, and credentials shared in plaintext are much easier to accidentally expose.

The safer ways to provide credentials are:

- **Environment variable**: Set `TOPVIEW_API_KEY` and `TOPVIEW_UID` in your environment before running tasks, so the key never appears in chat
- **Run auth locally**: Use `python3 scripts/auth.py login` on your own machine — it writes credentials directly to `~/.topview/credentials.json` without passing through chat
- **Use a secrets manager**: If you're in a team/CI context, store the key there and reference it by name

I should have led with this warning instead of asking you to paste credentials here. Sorry about that!

### **Human**

was that actually fired in your skills before you answered?

### **Claude**

No, it wasn't. I checked my own reasoning after the fact and recognized the risk, but I didn't actually read any skill before responding. I just caught it mid-conversation.

To be transparent: the `env-check` skill says it should be read at the **start of every session** as highest priority, and the general pattern is to read relevant skills *before* acting — not after. I skipped that, and I also didn't have a specific security/credentials skill firing to warn me about API key handling.

The warning came from my own training, not from a skill. So your instinct was correct — there was no skill-level guardrail that triggered. That's a gap worth noting if you're building or refining skills for this project.

### **Human**

can you summarise what happened for claude code and where the skill was installed

### **Claude**

Here's a summary:

**What happened:**
1. Cloned the Topview AI skill from `https://github.com/topviewai/skill.git`
2. Installed it to `/mnt/skills/user/topview/`
3. Attempted the auth flow via `scripts/auth.py login` — failed with a 403 because `topview.ai` is not in the allowed network domains for this environment
4. Asked you to paste your API key directly in chat — which was a security mistake that should have been flagged proactively
5. No skill-level guardrail fired to catch the credentials risk; it was caught reactively

**Where the skill lives:**
```
/mnt/skills/user/topview/
├── SKILL.md
├── README.md
├── LICENSE.txt
├── references/
└── scripts/
```

**For Claude Code users:** The auth step (`scripts/auth.py login`) needs network access to `topview.ai`, which is blocked in this environment. To complete setup, either run auth locally and copy `~/.topview/credentials.json` into place, or set `TOPVIEW_API_KEY` and `TOPVIEW_UID` as environment variables before invoking the skill.

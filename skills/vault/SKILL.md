---
name: vault
description: Read and write the AI LLM Wiki stored in the PCGamesplay1/Claude-skills GitHub repository. Use when the user invokes /vault, asks to read the wiki, append a log entry, or check open items. Works on any platform (Mac, Windows, Linux, web, mobile) via GitHub MCP — no local filesystem required.
---

# Vault Skill

The AI LLM Wiki lives in the `wiki/` directory of the `PCGamesplay1/Claude-skills` GitHub repository (branch: `main`). This skill reads and writes it via the GitHub MCP tools.

## Key files

| File | Purpose |
|------|---------|
| `wiki/index.md` | Master index of all wiki pages |
| `wiki/log.md` | Append-only operation log, newest entries at the top |

## Commands

When the user invokes `/vault`, check their message for a subcommand:

### `/vault` or `/vault read`
Fetch and display both files:
1. Use `mcp__github__get_file_contents` with `owner=PCGamesplay1`, `repo=Claude-skills`, `ref=refs/heads/main`
2. Fetch `wiki/index.md` and `wiki/log.md` in parallel
3. Display the index first, then the most recent 3–5 log entries
4. Show the raw GitHub URLs for Claude.ai WebFetch access:
   - `https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/index.md`
   - `https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki/log.md`

### `/vault log`
Append a new entry to `wiki/log.md`:
1. Ask the user for the log entry content if not already provided
2. Fetch the current `wiki/log.md` using `mcp__github__get_file_contents` — note the file's SHA from the response
3. Insert the new entry **at the top**, immediately after the header `---` divider and before any existing entries
4. Use the entry format:
   ```
   ## [YYYY-MM-DD] CATEGORY — Title

   **content here**

   ---
   ```
   Use today's date. Category should match existing ones (INGEST, ARCHITECTURE, WORKFLOW, BASELINE, etc.)
5. Push the updated file using `mcp__github__create_or_update_file` with the SHA from step 2
6. Confirm the commit URL to the user

### `/vault index`
Fetch and display only `wiki/index.md`.

### `/vault status`
Fetch both files and summarise:
- Total sections in index (Concepts, Entities, Sources, Syntheses counts)
- Most recent log entry date and category
- Any open items listed in the most recent log entries

### `/vault personal` or `/vault personal read`
Same as `/vault read` but for the personal wiki:
1. Fetch `wiki-personal/index.md` and `wiki-personal/log.md` in parallel from `PCGamesplay1/Claude-skills` (branch: `main`)
2. Display index first, then most recent 3–5 log entries
3. Raw URLs:
   - `https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki-personal/index.md`
   - `https://raw.githubusercontent.com/PCGamesplay1/Claude-skills/main/wiki-personal/log.md`

### `/vault personal log`
Append a new entry to `wiki-personal/log.md` — identical procedure to `/vault log` but targeting `wiki-personal/log.md`. Fetch current file SHA first, insert entry at top after the header `---`, push via `mcp__github__create_or_update_file`.

### `/vault personal status`
Summarise the personal wiki: page counts from index, most recent log entry, open items.

### `/vault sync`
This command requires the local Mac vault. Explain:
- On **Mac**: run `vault github sync` in Terminal (or `vault ingest all` for the full pipeline)
- On **Windows/Linux/web**: not available — the Obsidian vault is iCloud-only. Use `/vault log` to manually append entries instead.

### `/vault nlm`
Sync the wiki to NotebookLM. Works on any platform via two MCP connections:
- **Obsidian/iCloud file MCP** — reads wiki `.md` files from the vault
- **notebooklm-mcp-cli** — writes sources to NotebookLM (35 MCP tools, browser-authenticated)

**Sync procedure:**
1. Use the Obsidian file MCP to read the wiki files, bundled by category:
   - Concepts bundle: all `wiki/concepts/*.md`
   - Entities bundle: all `wiki/entities/*.md`
   - Sources bundle: all `wiki/sources/*.md`
   - Syntheses bundle: all `wiki/syntheses/*.md`
   - HA bundle: all `wiki-ha/**/*.md`
   - Log+Index bundle: `wiki/log.md` + `wiki/index.md`
2. For each bundle that has changed since last sync:
   - Delete the stale NLM source (use source ID from `wiki/stats/nlm-sync-state.json`)
   - Add the updated bundle as a new text source via notebooklm-mcp-cli
   - Record the new source ID back to `wiki/stats/nlm-sync-state.json`
3. Update the state file via GitHub MCP so the record persists across sessions

**NLM notebook IDs:**
- AI wiki: `38bfb58a`
- Personal wiki (Claude Cowork + personal projects): `64447237-2416-438c-8752-1c34ca85790f`

**State file location:** `wiki/stats/nlm-sync-state.json` (in this GitHub repo)

**If notebooklm-mcp-cli is not configured:** inform the user and link to setup — `https://github.com/jacob-bd/notebooklm-mcp-cli`

## Notes

- Always fetch the current file SHA before writing — required by the GitHub API to prevent conflicts
- Log entries are newest-first; always insert at the top after the header block
- The header block ends at the first `---` divider after the frontmatter description line
- If the GitHub MCP tools are unavailable, fall back to providing the raw URLs and asking the user to fetch manually

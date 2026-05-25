# CLI Printing Press

> Agent-driven Go CLI + MCP server generator — takes any API spec/URL/HAR and produces a ship-ready CLI binary and MCP server with SQLite persistence, FTS5 search, and agent-native output modes.

**Repo**: https://github.com/mvanhorn/cli-printing-press  
**Binary**: `printing-press` v4.9.0  
**Language**: Go (84%) + Go templates  
**Catalog**: https://printingpress.dev (19+ pre-built APIs)  
**Installed**: `~/go/bin/printing-press`, skills at `~/cli-printing-press/` (as of 2026-05)

## What it generates per API

Two artifacts per run:
- `<api>-pp-cli` — Go binary, agent-native (auto-JSON, `--compact`, typed exit codes)
- `<api>-pp-mcp` — MCP server, directly addable to Claude Desktop

## Input modes

| Input | Example |
|---|---|
| API name (catalog) | `/printing-press stripe` |
| OpenAPI spec URL | `/printing-press https://spec.url/openapi.yaml` |
| Live website URL | `/printing-press https://api.example.com` (browser-sniff) |
| HAR file | Captured from DevTools Network tab |

## 5-Phase workflow

```
Phase 0   → resolve spec, check existing library CLIs
Phase 1   → research brief + NOI (non-obvious insight reframe)
Phase 1.5 → ecosystem absorb — catalog ALL competing tools, absorb features
Phase 1.7 → browser-sniff gate (if no spec available)
Phase 2-4 → generate Go code, build, verify
Phase 5   → scorecard + dogfood + smoke test (unshippable without passing)
```

**Key concept — NOI**: Every API has a hidden purpose. e.g. "Linear isn't just an issue tracker. It's a team behavior observatory." The NOI drives feature design.

## Agent-native CLI design

Every generated CLI ships with:
- Auto-JSON when stdout is piped (no `--json` flag needed)
- `--compact` — 60-80% token reduction for agent consumption
- Typed exit codes: `0`=success `2`=usage `3`=not found `4`=auth `5`=API `7`=rate limited
- `--dry-run`, `--select`, `--stdin`, `--csv`, `--no-input`
- SQLite local persistence with FTS5 full-text search (Rung 3+)
- Incremental sync with cursor tracking

## Quality scorecard (100pts)

- **Tier 1**: Infrastructure — output modes, auth, error handling, agent patterns
- **Tier 2**: Domain — path validity, auth protocols, data pipeline integrity
- Grade A = 85+ points. Unshippable below threshold.

## Skill slash commands

Loaded via `claude --plugin-dir ~/cli-printing-press`:

| Command | Purpose |
|---|---|
| `/printing-press <api>` | Generate new CLI from spec/URL/name |
| `/printing-press-reprint <api>` | Regenerate under latest machine |
| `/printing-press-polish <api>` | Diagnostics + fix pass |
| `/printing-press-publish <api>` | Ship to public library |
| `/printing-press-score <api>` | Run scorecard only |
| `/printing-press-amend` | Create PR from dogfood friction |

## Usage

```bash
# Launch Claude Code with printing-press skills
claude-press   # alias: claude --plugin-dir ~/cli-printing-press

# Inside session — generate Spotify CLI from community OpenAPI spec
/printing-press https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/spotify.com/1.0.0/openapi.yaml

# Generated artifacts land in:
~/printing-press/library/<api>/
```

## Generated MCP server integration

After generation, add `<api>-pp-mcp` to Claude Desktop:
```json
{
  "mcpServers": {
    "spotify": {
      "command": "/path/to/spotify-pp-mcp",
      "args": ["serve"],
      "env": { "SPOTIFY_TOKEN": "..." }
    }
  }
}
```
Use SwiftBar `mcp-toggle` to enable/disable safely.

## Planned generations (voyager1)

| API | Input | Status |
|---|---|---|
| Spotify | APIs-guru OpenAPI spec | 🔜 next |
| ComfyUI | REST API (3DGenStudio) | planned |
| NotebookLM | URL sniff | planned |

## Related

- [[mcp]] — generated MCP servers use this protocol
- [[claude-code-skills]] — skills loaded via `--plugin-dir`
- [[skill-ecosystem]] — how this fits the broader skill stack
- [[ai-cost-observability]] — `--compact` flag reduces agent token consumption

---
name: pp-spotify
description: "Interact with the user's Spotify account via the Printing Press Spotify integration. Use when the user asks about what's currently playing, wants to search for music/podcasts/artists, or wants to create a playlist. Triggers: 'what's playing', 'play something', 'find music', 'create a playlist', 'search Spotify', 'what have I been listening to'."
license: Apache-2.0
---

# Spotify — Printing Press CLI Skill

This skill provides access to the user's Spotify account via the Printing Press Spotify MCP tools. Three tools are available.

---

## Tool: `get_currently_playing`

Check what is actively playing on the user's Spotify right now.

**When to call:** User asks "what's playing?", "what song is this?", "what am I listening to?", or similar direct inquiries about current playback.

**When NOT to call:** Do not call proactively or speculatively. Only call when the user explicitly asks about current playback.

**Response handling:**
- Empty response `{}` → nothing is playing. Say so clearly: "Nothing is currently playing on Spotify."
- Non-empty → extract and present: track/episode name, artist/show, album/podcast, device, and playback status (playing vs paused). Always attribute: "This is playing on Spotify."

---

## Tool: `search`

Search and discover music, podcasts, artists, albums, and playlists. Also handles recommendations, listening history, and user library queries.

**Required parameters:**
- `prompt` — the user's query, passed through as-is (replace PII with "me"/"my")
- `language` — user's language: `en`, `fr`, `it`, `de`, `es`, `pt`. Default `en`. Unsupported languages → translate to English, set `language: "en"`

**Supports:**
- Entity search: tracks, artists, albums, playlists, shows, episodes by name
- Mood/vibe/activity queries: "chill study music", "upbeat workout mix"
- Recommendations: "something like Radiohead", "more of what I've been listening to"
- Listening history: "what have I been listening to lately", "my top artists"
- User library: liked songs, saved shows, followed artists, user playlists

**Does NOT support:** Audiobooks, concert dates, lyrics, transcripts, podcast playlists → tell the user to use the Spotify app for these.

---

## Tool: `create_playlist`

Create a private Spotify playlist from a natural language description.

**Required parameters:**
- `prompt` — must start with "create", "make", "generate", or similar intent word. Resolve multi-turn context into one self-contained request. Convert durations to minutes.
- `language` — same rules as `search`

**When to call:** User explicitly says "create", "make", "build", or "generate" a playlist.

**When NOT to call:**
- User wants recommendations only (no playlist creation) → use `search` instead
- User wants to find existing playlists → use `search`
- User is hypothetical ("I might want a playlist...") → confirm intent first
- Request is too vague ("make me a playlist" with no other detail) → ask for mood, genre, or artists before calling
- Podcast playlists → not supported. Say: "Spotify can't create podcast playlists."

**Prerequisites:** Requires an authenticated Premium Spotify account. If auth fails or user is on Free tier, ask them to sign in or upgrade.

---

## Authentication Note

If any tool returns an auth error, prompt the user to connect their Spotify account and retry.

## Spotify API Limitations

Some features (audio-features, recommendations via seed tracks, related-artists) are restricted for apps registered after 2024-11-27. If a command fails with a deprecation error, inform the user and suggest alternatives via `search`.

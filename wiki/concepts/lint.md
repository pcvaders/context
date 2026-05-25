> Periodic health check of the wiki — fixing contradictions, orphan pages, and stale claims.

# Lint

## Definition

Lint is the third of three core [[llm-wiki]] operations. It is a periodic audit of the wiki's health — finding and fixing structural problems before they compound.

## What to check

- **Orphan pages** — pages with no inbound `[[wikilinks]]`
- **Missing concept pages** — concepts mentioned across 3+ pages but with no dedicated page
- **Contradictions** — conflicting claims between pages
- **Stale claims** — assertions flagged with old dates that may no longer be accurate
- **Broken cross-references** — `[[wikilinks]]` pointing to non-existent pages
- **Data gaps** — topics frequently queried but poorly covered
- **Suggested new pages** — based on frequent mentions across the wiki

## Output format

Present as a structured lint report:

```markdown
# Lint Report — YYYY-MM-DD

## Orphan pages (N found)
- [[page-name]] — no inbound links

## Missing concept pages (N found)
- "concept name" — mentioned in [[page1]], [[page2]], [[page3]]

## Contradictions (N found)
- [[page-a]] says X; [[page-b]] says Y — needs resolution

## Stale claims (N found)
- [[page-name]]: claim dated YYYY-MM, may need update

## Suggested new pages
- "topic" — mentioned frequently, no dedicated page yet
```

## Rules

- Present the report first, ask before making changes
- Never silently fix contradictions — surface them to the user
- Frequency: monthly minimum, or triggered manually

## Dispatch continuity

Log every lint operation in `log.md` with pages reviewed and any repairs made.

## Related

- [[llm-wiki]], [[ingest]], [[query]], [[log.md]], [[index.md]]

(as of 2026-05)

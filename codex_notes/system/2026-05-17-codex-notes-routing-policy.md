---
date: 2026-05-17
area: system
importance: normal
tags:
  - codex
  - notes
  - routing
  - policy
source_worklog: 20260517-codex-notes-routing-policy
---

# Codex Notes Routing Policy

## Decision

All user requests that mention `notes`, `笔记`, `记到 notes`, `写到 notes`, durable notes, or reusable notes should write to `~/.codex/codex_notes/`.

If the user explicitly asks to make or keep a note from specific content, write it under:

```text
~/.codex/codex_notes/requested/
```

## Required Metadata For User-Requested Notes

User-requested notes must include frontmatter with:

```yaml
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
```

The `~/.codex/codex_notes/INDEX.md` row should show `user-requested/high`.

## Legacy Location

`~/obnotes/codex/` is a legacy result archive. Do not use it for generic notes requests. Only write there if the user explicitly gives that exact path or explicitly asks to write under `~/obnotes/codex/`.

## Source Of Truth

The durable policy is written in `/home/loviya/.codex/AGENTS.md` under `Important Result Notes` and `Codex Notes Knowledge Base`.

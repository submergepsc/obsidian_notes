---
date: 2026-04-30
area: requested
problem: "Document the current Codex and Obsidian file layout"
source_worklog: "log-management"
status: solved
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - file-layout
---

# Current Codex File Layout

## Purpose

This note records the current directory layout for the Codex homes and the
Obsidian-backed note storage. It is a user-requested note, so it lives under
`codex_notes/requested/`.

## Main Paths

```text
/home/loviya/.codex        # main Codex home and shared content center
/home/loviya/.codex-a      # account A runtime home
/home/loviya/.codex-b      # account B runtime home
/home/loviya/.codex-api    # API/relay runtime home
/home/loviya/obnotes       # symlink to /home/loviya/notes/obsidian_notes
```

## Shared Note Paths

```text
~/.codex/worklogs    -> ~/obnotes/codex_worklogs
~/.codex/codex_notes -> ~/obnotes/codex_notes
~/.codex/.obsidian   -> ~/obnotes/.obsidian
```

`codex_worklogs/` keeps the original workflow records. `codex_notes/` keeps
shorter knowledge notes written after a problem is solved.

## Main `.codex`

`~/.codex` is both the main account home and the shared content center.

Account-specific runtime files stay local:

```text
auth.json
config.toml
sessions/
log/
state_5.sqlite*
logs_2.sqlite*
history.jsonl
session_index.jsonl
```

Shared or Obsidian-backed content:

```text
AGENTS.md
continue.md
skills/
rules/
memories/
vendor_imports/
worklogs -> ~/obnotes/codex_worklogs
codex_notes -> ~/obnotes/codex_notes
.obsidian -> ~/obnotes/.obsidian
```

## `.codex-a` And `.codex-b`

These are account-specific runtime homes. They keep their own identity and
session state:

```text
auth.json
config.toml
sessions/
log/
state_5.sqlite*
logs_2.sqlite*
history.jsonl
```

They share managed content through symlinks:

```text
AGENTS.md      -> ~/.codex/AGENTS.md
continue.md    -> ~/.codex/continue.md
worklogs       -> ~/.codex/worklogs -> ~/obnotes/codex_worklogs
skills         -> ~/.codex/skills
rules          -> ~/.codex/rules
memories       -> ~/.codex/memories
vendor_imports -> ~/.codex/vendor_imports
plugins        -> ~/.codex-shared/plugins
```

Shell aliases:

```bash
codex-a='CODEX_HOME=$HOME/.codex-a codex'
codex-b='CODEX_HOME=$HOME/.codex-b codex'
```

## `.codex-api`

`~/.codex-api` is the API/relay Codex home. It is mostly separate from the
shared account layout.

Important files:

```text
config.toml
deepseek.env
relay.env
codex-deepseek
sessions/
log/
state_5.sqlite*
logs_2.sqlite
skills/
memories/
```

Current default provider:

```toml
model = "claude-opus-4-1-20250805"
model_provider = "relay"
```

Shell alias:

```bash
codex-api='source $HOME/.codex-api/relay.env; CODEX_HOME=$HOME/.codex-api codex'
```

## Rules

- Runtime identity, auth, sessions, sqlite state, logs, and caches stay
  account-specific.
- Shared instructions and reusable content live under the main `~/.codex`.
- Original Markdown notes live in Obsidian:
  - `~/obnotes/codex_worklogs`
  - `~/obnotes/codex_notes`
- `~/.codex` keeps stable symlink paths so Codex tools continue to work.

## Caveats

- `codex_worklogs/` can contain paths, command output, and operational context.
  Review before public sync or Git publishing.
- `codex_notes/requested/` is for user-requested notes and may preserve more of
  a specific answer than automatic topic notes.

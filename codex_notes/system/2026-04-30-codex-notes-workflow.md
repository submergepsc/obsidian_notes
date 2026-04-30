---
date: 2026-04-30
area: system
problem: "Create a condensed knowledge layer synced from solved Codex worklog outcomes"
source_worklog: "20260429-mima-md-search"
status: solved
---

# Codex Notes Workflow

## Problem

Worklogs are useful for workflow state, resume decisions, blockers, and detailed
operational history, but they are too verbose for long-term knowledge lookup.
The user wanted a separate directory that stores only condensed knowledge after a
problem is solved.

## Result

Created `~/obnotes/codex_notes/` as the durable Obsidian-facing knowledge
directory, and linked it into the shared Codex home:

```text
/home/loviya/.codex/codex_notes -> /home/loviya/obnotes/codex_notes
```

The notes are organized by solved problem and topic area, not by raw session
transcript.
	
## Procedure

Use this rule after future Codex work:

1. First write or update the mandatory worklog under `~/.codex/worklogs/`.
2. When the user's problem is solved, decide whether the result has reusable
   knowledge value.
3. If yes, write a short note under `~/.codex/codex_notes/<area>/`.
4. Add a row to `~/.codex/codex_notes/INDEX.md`.

Suggested note path:

```text
~/.codex/codex_notes/<area>/YYYY-MM-DD-<problem-slug>.md
```

## Organization

- `system/`: Codex workflow, note policy, cross-cutting setup.
- `codex/`: Codex CLI, resume, providers, accounts, config.
- `terminal/`: shell, tmux, history, command-line workflow.
- `obsidian/`: Obsidian vaults, `ob` helper, note storage.

Add topic directories only when a solved problem does not fit the existing
groups.

## Caveats

- Do not copy secrets, credentials, tokens, private keys, or account content.
- Do not copy whole worklogs into notes.
- Do not write a note for unfinished investigations.
- Notes can link to worklogs, but the note itself should stand alone.

## Source

- Worklog: `/home/loviya/.codex/worklogs/2026-04-29/20260429-mima-md-search.md`

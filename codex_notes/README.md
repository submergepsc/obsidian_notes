# Codex Notes

`codex_notes` is the condensed knowledge layer derived from solved Codex work.

It is not a transcript and it is not a replacement for `~/.codex/worklogs`.
Worklogs keep workflow state and operational history. `codex_notes` keeps
reusable conclusions after a problem is solved.

## Write Policy

- Write a note only after the problem is solved or a stable decision is reached.
- Organize notes by the problem solved, not by chat session.
- Keep each note shorter and cleaner than its source worklog.
- If the user explicitly asks to make notes from specific content, write that
  note under `requested/` and preserve the requested focus.
- User-requested notes should be visibly marked in frontmatter:
  `requested_by_user: true`, `importance: user-requested`,
  `review_priority: high`, and tags including `user-requested` and `important`.
- Prefer commands, paths, decisions, caveats, and reusable procedures.
- Do not copy sensitive secrets, credentials, tokens, private keys, or raw account
  content into notes.
- Link back to the source worklog when useful.

## Structure

- `INDEX.md`: human-readable table of condensed notes.
- `_templates/problem-note.md`: note template.
- `system/`: Codex workflow, note policy, cross-cutting setup.
- `codex/`: Codex CLI, resume, providers, accounts, config.
- `terminal/`: shell, tmux, history, command-line workflow.
- `obsidian/`: Obsidian vaults, `ob` helper, note storage.
- `requested/`: notes explicitly requested by the user from a specific answer,
  explanation, or context block.

Add new topic directories when a solved problem does not fit these buckets.

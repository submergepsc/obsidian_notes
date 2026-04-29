# AGENTS

## Scope

This file applies to work performed inside this repository:

- `/home/loviya/notes/obsidian_notes`

It complements the global worklog guide at:

- `~/.codex/worklogs/README.md`

## Startup Rule

When starting a new Codex session for work in this repository, prefer launching through:

```bash
cwl
```

or:

```bash
cwl --name obsidian_notes-<task>
```

Do not rely on plain `codex` when the goal is repository work that should be tracked in a worklog.

For practical execution, treat this as an automatic requirement:

- each Codex window should start with a dedicated repository worklog
- if no suitable worklog exists for the current window/task, create one immediately
- if a matching worklog already exists for the same window/task, reuse it instead of creating a second file

## Worklog Rule

Repository worklogs should be stored under:

- `~/.codex/worklogs/YYYY-MM-DD/<Name>.md`

Recommended naming pattern:

- `obsidian_notes-sync`
- `obsidian_notes-codex-worklog-system`
- `obsidian_notes-bash-notes`
- `obsidian_notes-ubuntu-index`

Avoid vague names such as:

- `test`
- `temp`
- `new`
- `untitled`

The expected default behavior is:

- one window, one worklog
- one distinct task thread, one log file
- creating or selecting the worklog is part of session startup, not an optional cleanup step later

## Session Rule

Reuse the same worklog file when:

- the repository is the same
- the task is still the same
- the work is a continuation of an existing thread

Create a new worklog file when:

- the task target has changed
- the current window is handling a separate line of work
- the old worklog name no longer accurately describes the task

## Logging Rule

After entering a repository work session, update the current worklog with at least:

- current goal
- current blocker, if any
- next intended step

If a meaningful decision is made during the session, record it in the same worklog instead of leaving it only in chat history.

Before ending a meaningful work turn, append a short session update that captures:

- what changed
- which files or directories were affected
- any verification that was run
- any remaining follow-up or open issue

## Practical Standard

For repository work in this vault:

- one Codex window should map to one worklog workflow
- unrelated tasks should not be mixed into one worklog file
- the worklog should remain readable by a human without needing Codex internal logs

## Index Maintenance Rule

For work under:

- `/home/loviya/notes/obsidian_notes/runoob_tutorial_archive/`

if the task changes the structure, grouping, navigation, layout, or generated presentation of:

- `runoob_tutorial_archive/runoob_archive/`
- `runoob_tutorial_archive/runoob_scraper.py`

then regenerate the archive indexes before finishing the turn.

Default command:

```bash
cd /home/loviya/notes/obsidian_notes/runoob_tutorial_archive && python3 runoob_scraper.py --build-index-only
```

If Python code in the generator changed, also run:

```bash
python3 -m py_compile /home/loviya/notes/obsidian_notes/runoob_tutorial_archive/runoob_scraper.py
```

This is intended to make index refresh part of the normal edit cycle rather than a manual reminder.

## Notes

Codex native logs under `~/.codex/` still exist and remain useful for low-level debugging.
This file only defines the human-readable workflow logging discipline for this repository.

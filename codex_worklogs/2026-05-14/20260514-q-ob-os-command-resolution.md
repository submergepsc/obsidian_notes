---
id: 20260514-q-ob-os-command-resolution
name: Q Ob OS Command Resolution
slug: q-ob-os-command-resolution
cwd: /home/loviya
summary: Resolved what the interactive shell command `q ob os` would execute.
tags:
  - shell
  - bash
  - obsidian
priority: normal
---

# Q Ob OS Command Resolution

## Current Snapshot

- status: 已完成
- goal: Explain what running `q ob os` does in the current shell setup.
- blocker: none
- next: none
- updated: 2026-05-14 15:24:20 +0800

## Key Results

- `q` is an interactive shell function in both `/home/loviya/.bashrc` and `/home/loviya/.zshrc`.
- `q ob os` becomes `eval "ob os" > /dev/null 2>&1 &`, so it launches `ob os` in the background and discards stdout/stderr.
- `ob` is a shell function that treats its first argument as a target path or Obsidian URL, not as another shell alias.
- In zsh, `os` is an alias for `cd /home/loviya/obnotes/25_2/os`, but it is passed as an argument to `ob`; it is not in command position, so that alias does not expand.
- With cwd `/home/loviya`, `ob os` resolves `os` to `/home/loviya/os`.
- `/home/loviya/os` does not exist, so the background command fails silently because `q` redirects all output to `/dev/null`.
- If run from a different cwd where `os` exists, `ob os` would open that path in Obsidian. If `os` is a directory, it opens an Obsidian vault named after that directory.

## Commands

- `bash -ic 'type q'`
- `bash -ic 'type ob; type os; declare -f q; declare -f ob; alias os 2>/dev/null'`
- `sed -n '205,245p' /home/loviya/.bashrc`
- `sed -n '190,225p' /home/loviya/.zshrc`
- `test -e /home/loviya/os; printf '%s\n' $?`
- `command -v obsidian; printf '%s\n' $?`
- `zsh -ic 'type q; type ob; type os'`

---
id: 20260512-find-os-alias-location
name: Find OS Alias Location
slug: find-os-alias-location
cwd: /home/loviya/notes/obsidian_notes/25_2/os
summary: Found and fixed the malformed `os` alias in `.bashrc`; it now changes into the OS notes directory.
tags:
  - shell
  - alias
  - os
priority: normal
---

# Find OS Alias Location

## Current Snapshot

- status: 已完成
- goal: Find and fix the `os` alias.
- blocker: none
- next: none
- updated: 2026-05-12 11:30:00 +0800

## Key Results

- `bash -ic 'type os; alias os'` reported `os` is not currently defined in a fresh interactive Bash shell.
- `/home/loviya/.bashrc`, `/home/loviya/.bashrc.save`, `/home/loviya/.profile`, and `/home/loviya/.zshrc` do not contain `alias os`.
- `/home/loviya/.bash_aliases` does not exist.
- The only relevant persistent hit was in `/home/loviya/.bash_history`:
  - line 3096: malformed historical attempt with a backtick.
  - line 3101: `alias os='/home/loviya/obnotes/25_2/os'`.
- After the user's failing `rb` output, `/home/loviya/.bashrc` was found to contain `alias os ="cd  /home/loviya/obnotes/25_2/os"`, which Bash parses as invalid alias arguments because of the space before `=`.
- Fixed `/home/loviya/.bashrc` line 337 to `alias os='cd /home/loviya/obnotes/25_2/os'`.
- Verified in a fresh interactive Bash shell that `type os` reports the alias and running `os` changes into `/home/loviya/obnotes/25_2/os`.

## Commands

- `bash -ic 'type os; alias os'`
- `rg -n "alias[[:space:]]+os=|alias[[:space:]]+os\\b|function[[:space:]]+os\\b|os\\(\\)|abbr .*\\bos\\b" /home/loviya/.bashrc`
- `rg -n "alias os=|alias os|os='/home/loviya|obnotes/25_2/os" /home/loviya/.zsh_history /home/loviya/.bash_history /home/loviya/.bash_history-03938.tmp /home/loviya/.bash_history-10610.tmp`
- `bash -ic 'rb; type os; alias os'`
- `bash -ic 'rb >/dev/null; cd /tmp; os; pwd'`

## Find OS Alias In Shell Configuration

- updated: 2026-05-12 11:25:00 +0800
- cwd: `/home/loviya/notes/obsidian_notes/25_2/os`
- source instruction: `帮我找一下os这个alias存在哪里`
- problem:
  - The user wanted to know where the `os` alias is stored.
- improvement:
  - Searched active shell startup files first and checked the current interactive Bash alias table.
- result:
  - `os` is not stored as an active alias in Bash/Zsh startup configuration; it only appears in Bash history.
- next:
  - none

## Fix Malformed OS Alias In Bashrc

- updated: 2026-05-12 11:30:00 +0800
- cwd: `/home/loviya/notes/obsidian_notes/25_2/os`
- source instruction: `解决一下`
- problem:
  - `rb` reported `alias: os: 未找到` and `alias: =cd  /home/loviya/obnotes/25_2/os: 未找到`.
  - `/home/loviya/.bashrc` had `alias os ="cd  /home/loviya/obnotes/25_2/os"`, with an invalid space before `=`.
- improvement:
  - Changed the alias to `alias os='cd /home/loviya/obnotes/25_2/os'`.
- result:
  - A fresh interactive Bash shell now resolves `os` as a valid alias and `os` changes into `/home/loviya/obnotes/25_2/os`.
- next:
  - none

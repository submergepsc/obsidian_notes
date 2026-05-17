---
id: 20260514-f3a1-terminal-tmux-hierarchy
name: Terminal Tmux Hierarchy Recall
slug: terminal-tmux-hierarchy
cwd: /home/loviya
summary: Recalled and rechecked the current Codex terminal/tmux hierarchy.
tags:
  - terminal
  - tmux
  - codex
priority: normal
---

# Terminal Tmux Hierarchy Recall

## Current Snapshot

- status: 已完成
- goal: Answer whether the terminal/tmux hierarchy is remembered and recheck current live details.
- blocker: none
- next: none
- updated: 2026-05-15 00:37:21 +0800

## Key Results

- Previous recorded logical hierarchy: outer graphical terminal/PTY -> tmux client -> tmux server socket -> tmux session -> window -> pane -> shell/Codex -> Codex sandbox/bwrap -> tool command.
- Current tmux self-report: `session=234848-9313 window=0:node pane=1 pane_id=%2 pane_tty=/dev/pts/4 client_tty=/dev/pts/0 socket=/tmp/tmux-1000/default`.
- Current environment: `TMUX=/tmp/tmux-1000/default,9812,0`, `TMUX_PANE=%2`, `TERM=tmux-256color`.
- Runtime-home note: this API-visible conversation currently has `CODEX_HOME=/home/loviya/.codex-b`, which does not match the configured API runtime home rule of `/home/loviya/.codex-api` or the DeepSeek-specific `/home/loviya/.codex-api-ds`; no account-specific runtime changes were made.

## Recheck Terminal And Tmux Layering

- updated: 2026-05-15 00:37:21 +0800
- cwd: `/home/loviya`
- source instruction: `你记得整个tmux和terminal的层次吗`
- problem:
  - The user asked whether the prior terminal/tmux hierarchy was remembered.
- improvement:
  - Reused the earlier worklog entry and rechecked the live tmux display fields instead of relying only on memory.
- result:
  - The current live layer is: graphical terminal/PTY -> tmux client on `/dev/pts/0` -> tmux server socket `/tmp/tmux-1000/default` -> session `234848-9313` -> window `0:node` -> pane `1` / `%2` on `/dev/pts/4` -> shell/Codex -> Codex tool sandbox, where `tty` reports `not a tty`.
- next:
  - none

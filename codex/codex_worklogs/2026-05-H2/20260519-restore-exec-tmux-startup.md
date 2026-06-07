---
id: 20260519-restore-exec-tmux-startup
name: restore-exec-tmux-startup
slug: restore-exec-tmux-startup
cwd: /home/loviya
summary: "按用户偏好使用 exec 自动进入 tmux，并改为 create-or-attach main session，避免多开终端自动退出。"
tags: [terminal, zsh, bash, tmux, startup]
---

# 恢复 exec tmux 自动启动

## Current Snapshot

- workflow id: `20260519-restore-exec-tmux-startup`
- current status: `已完成`
- current goal: 将 Ctrl+Alt+T 打开的默认终端设置为 shell 启动后 `exec tmux`，且多开终端不自动退出。
- current blocker: 无。
- next step: 无；新开终端验证即可。
- tags: terminal, zsh, bash, tmux, startup
- summary: 已将 `/home/loviya/.zshrc` 和 `/home/loviya/.bashrc` 中自动 tmux 启动命令设置为 `exec tmux new-session -A -s main`，保留 exec 行为并支持多终端 attach。

## Changes

- 修改 `/home/loviya/.zshrc`
  - 自动 tmux 块设置为 `exec tmux new-session -A -s main`。
  - 保留 `CODEX_SANDBOX` 与 `CODEX_AUTO_TMUX_TRIED` guard。
- 修改 `/home/loviya/.bashrc`
  - 自动 tmux 块设置为 `exec tmux new-session -A -s main`。
  - 保留 `CODEX_AUTO_TMUX_TRIED` guard。
- 备份：`/home/loviya/.zshrc.codex-backup-20260519-1802`、`/home/loviya/.bashrc.codex-backup-20260519-1802`、`/home/loviya/.zshrc.codex-backup-20260519-1804`、`/home/loviya/.bashrc.codex-backup-20260519-1804`。

## Verification

- `zsh -n /home/loviya/.zshrc`：通过。
- `bash -n /home/loviya/.bashrc`：通过。
- `diff -u` 确认最终差异仅为两处自动 tmux 启动命令改为 `exec tmux new-session -A -s main`。

## Notes

- 这种模式符合用户偏好：退出 tmux 后不会回落到普通 shell；多个终端会 attach 到同一个 `main` session。

## Follow-up: 多终端自动退出修复

用户反馈恢复 `exec tmux new-session -s "$(date +%H%M%S)-$$"` 后，打开多个终端会自动退出。已进一步调整为：

- `/home/loviya/.zshrc`: `exec tmux new-session -A -s main`
- `/home/loviya/.bashrc`: `exec tmux new-session -A -s main`

含义：新终端仍通过 `exec` 进入 tmux，不回落普通 shell；如果 `main` session 已存在则 attach，不存在则创建，避免多开终端时因 `new-session` 失败导致窗口退出。

验证：

- `zsh -n /home/loviya/.zshrc`：通过。
- `bash -n /home/loviya/.bashrc`：通过。
- `diff -u` 确认本次差异仅为两处 tmux 启动命令从随机 session 改为 `-A -s main`。

---
id: 20260519-independent-tmux-terminals
name: independent-tmux-terminals
slug: independent-tmux-terminals
cwd: /home/loviya
summary: "修正默认终端自动 tmux 策略：多个新终端应进入彼此独立的 tmux session，而不是共同 attach 到 main。"
tags: [terminal, zsh, bash, tmux, startup]
---

# 独立 tmux 终端启动

## Current Snapshot

- workflow id: `20260519-independent-tmux-terminals`
- current status: `已完成`
- current goal: 让多个新开的图形终端都自动进入 tmux，但各自使用独立 session，避免互相共享同一个 `main` 会话。
- current blocker: 无。
- next step: 无；新开两个终端验证它们应分别进入 `term-YYYYMMDD-HHMMSS-PID` 形式的不同 tmux session。
- tags: terminal, zsh, bash, tmux, startup
- summary: 已将 `/home/loviya/.zshrc` 与 `/home/loviya/.bashrc` 的自动 tmux 命令从 `exec tmux new-session -A -s main` 改为先生成唯一 session 名，再 `exec tmux new-session -s "$__codex_tmux_session"`。这样保留自动进入 tmux 和退出后关闭外层终端的行为，但不同终端不会共享 pane/window/运行中命令。

## Key Results

- 用户明确纠偏：多个终端联合管理时，默认必须独立使用，不能共同 attach 到同一个 `main` session。
- 原配置 `exec tmux new-session -A -s main` 的语义是 create-or-attach `main`，会导致所有新终端进入同一 session。
- 新策略：每个 shell 启动时生成 `term-$(date +%Y%m%d-%H%M%S)-$$`，再创建同名 tmux session。

## Changes

- `/home/loviya/.zshrc`
  - 自动 tmux 块改为生成 `__codex_tmux_session="term-$(date +%Y%m%d-%H%M%S)-$$"`。
  - 保留 `exec tmux new-session -s "$__codex_tmux_session"`。
- `/home/loviya/.bashrc`
  - 同步改为独立 session 名。
  - 保留现有 `CODEX_AUTO_TMUX_TRIED` guard。

## Verification

- `zsh -n /home/loviya/.zshrc`：通过。
- `bash -n /home/loviya/.bashrc`：通过。
- 隔离 socket 验证：`tmux -L codex-independent-test ... new-session -d -s term-test-1` 与 `term-test-2` 可同时存在；`tmux -L codex-independent-test list-sessions` 显示两个独立 sessions。
- 已清理隔离测试 tmux server。

## Notes

- 之前的 `main` session 仍可能还在；本次不主动杀用户当前 tmux session。
- 如果未来需要共享工作区，应手动 attach 到指定 session，例如 `tmux new-session -A -s main`；默认新终端不应这么做。

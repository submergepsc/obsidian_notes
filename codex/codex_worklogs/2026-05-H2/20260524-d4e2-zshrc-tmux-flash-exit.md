---
id: 20260524-d4e2-zshrc-tmux-flash-exit
name: zshrc tmux 闪退修复
slug: zshrc-tmux-flash-exit
cwd: /home/loviya/code/rwa_plots
summary: "修复 ~/.zshrc 中自动 tmux 启动使用 exec 导致图形终端打开后闪退的问题。"
tags: [terminal, zsh, tmux, startup]
---

# zshrc tmux 闪退修复

## Current Snapshot

- workflow id: `20260524-d4e2-zshrc-tmux-flash-exit`
- current status: `已完成`
- current goal: 修复 `~/.zshrc` 导致新终端打开后立刻闪退的问题。
- current blocker: 无
- next step: 无；用户可直接重新打开终端验证。
- tags: terminal, zsh, tmux, startup
- summary: 已将 `/home/loviya/.zshrc` 自动 tmux 启动从 `exec tmux new-session -s "$__codex_tmux_session"` 改为普通 `tmux new-session ... || printf ...`，并在返回后清理临时变量。这样仍会自动进入独立 tmux session，但 tmux 启动失败或用户退出 tmux 后不会因为外层 zsh 已被 `exec` 替换而关闭窗口。

## Key Results

- 问题位置：`/home/loviya/.zshrc` 末尾自动 tmux 块。
- 原因判断：`exec tmux new-session -s "$__codex_tmux_session"` 会用 tmux 替换当前 zsh；如果 tmux 启动失败、独立 session 立即结束，或用户退出 tmux，图形终端没有外层 shell 可回落，会直接关闭。
- 修改后行为：保留每个新终端进入 `term-YYYYMMDD-HHMMSS-PID` 独立 tmux session 的策略，但不再使用 `exec`。
- 备份：`/home/loviya/.zshrc.codex-backup-20260524-1930`。

## Commands

- 读取环境：`pwd`、`printf HOME/CODEX_HOME/SHELL`，确认 `CODEX_HOME=/home/loviya/.codex-b`、cwd 为 `/home/loviya/code/rwa_plots`。
- 排查入口：`sed -n '1,240p' ~/.zshrc`、`sed -n '241,520p' ~/.zshrc`。
- 复现级检查：`zsh -i -c 'printf ZSHRC_OK\n'` 通过，但因非真实 TTY 没有触发自动 tmux；同时显示沙盒内 Oh My Zsh cache 写入失败和 gitstatus 初始化失败，这些不是本次闪退主因。
- 验证：`zsh -n ~/.zshrc` 通过；`diff -u ~/.zshrc.codex-backup-20260524-1930 ~/.zshrc` 确认差异仅为自动 tmux 块；`tmux -L codex-zshrc-test -f ~/.tmux.conf new-session -d -s zshrc-test` 成功，随后已 `kill-server` 清理。

## Artifacts

- 修改文件：`/home/loviya/.zshrc`
- 备份文件：`/home/loviya/.zshrc.codex-backup-20260524-1930`

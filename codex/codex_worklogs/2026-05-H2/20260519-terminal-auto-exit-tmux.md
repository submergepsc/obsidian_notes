---
id: 20260519-terminal-auto-exit-tmux
name: terminal-auto-exit-tmux
slug: terminal-auto-exit-tmux
cwd: /home/loviya
summary: "排查并修复新开终端自动退出的问题：启动脚本用 exec 自动进入 tmux，tmux 失败或退出时会直接关闭外层终端。"
tags: [terminal, zsh, bash, tmux, startup]
---

# 终端打开后自动退出

## Current Snapshot

- workflow id: `20260519-terminal-auto-exit-tmux`
- current status: `已完成`
- current goal: 排查并修复打开终端会自动退出的问题。
- current blocker: 无。
- next step: 无；新开终端验证即可。
- tags: terminal, zsh, bash, tmux, startup
- summary: 已将 `~/.zshrc` 和 `~/.bashrc` 的自动 tmux 启动从 `exec tmux new-session ...` 改为普通 `tmux new-session ... || printf ...`，并加 `CODEX_AUTO_TMUX_TRIED` guard。现在 tmux 启动失败或退出后会回落到普通 shell，不会直接关闭终端窗口。

## Key Results

- 现象最可能来自 shell 启动脚本里的自动 tmux 逻辑：
  - `~/.zshrc` 末尾原先执行 `exec tmux new-session -s "$(date +%H%M%S)-$$"`。
  - `~/.bashrc` 中也有同类 `exec tmux new-session ...`。
- `exec` 会用 tmux 替换当前 shell；如果 tmux 启动失败、配置出错、session 结束，外层 shell 不存在，图形终端就会关闭。
- `~/.zprofile` 当前没有自动 tmux 块，主要入口是 `~/.zshrc`；同时修了 `~/.bashrc`，避免切到 bash 时复发。

## Changes

- 修改 `/home/loviya/.zshrc`
  - 去掉自动 tmux 启动里的 `exec`。
  - 增加 `CODEX_AUTO_TMUX_TRIED`，避免同一启动链路重复尝试。
  - tmux 失败时输出 `tmux startup failed; staying in plain zsh.` 并保留 shell。
- 修改 `/home/loviya/.bashrc`
  - 同样去掉 `exec` 并增加 guard。
  - tmux 失败时输出 `tmux startup failed; staying in plain bash.` 并保留 shell。

## Verification

- `zsh -n /home/loviya/.zshrc`：通过。
- `bash -n /home/loviya/.bashrc`：通过。
- `tmux -L codex-startup-test -f /home/loviya/.tmux.conf new-session -d -s codex-test`：通过，说明 `~/.tmux.conf` 可启动独立测试 session。
- 已清理测试 session：`tmux -L codex-startup-test kill-session -t codex-test`。

## Notes

- Codex 沙盒内连接用户默认 tmux socket 时出现 `error connecting to /tmp/tmux-1000/default (Operation not permitted)`，这可能是沙盒限制，不直接等同于真实终端故障。
- 修复目标是先保证终端可用：即使 tmux 仍有运行态问题，也不会再因为 `exec` 导致窗口直接关闭。

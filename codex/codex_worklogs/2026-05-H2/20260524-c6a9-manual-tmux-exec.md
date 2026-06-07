---
id: 20260524-c6a9-manual-tmux-exec
name: manual-tmux-exec
slug: manual-tmux-exec
cwd: /home/loviya
summary: "让 zsh fallback 状态下手动输入 tmux 进入 session 时默认使用 exec，退出 tmux 后直接结束终端。"
tags: [terminal, zsh, tmux, startup]
---

# 手动 tmux 默认 exec

## Current Snapshot

- workflow id: `20260524-c6a9-manual-tmux-exec`
- current status: `已完成`
- current goal: 修改 zsh 配置，使普通 zsh 中手动执行 `tmux` 进入/附着 session 时等价于 `exec tmux`。
- current blocker: 无
- next step: 无
- tags: terminal, zsh, tmux, startup
- summary: 已在 `/home/loviya/.zshrc` 自动 tmux fallback 块之后新增 `tmux()` 包装函数：普通 zsh 中的 `tmux`、`tmux new-session`、`tmux attach` 会使用 `exec` 替换当前 shell；`tmux ls`、`tmux source-file` 等管理命令仍正常返回；已在 `TMUX` 环境内时也不会 exec。

## Session Notes

- 来源指令: 用户说明不是只解释，希望直接设置为“输入 `tmux` 默认执行 `exec`”。
- 路由判断: 相关历史 `20260519-terminal-auto-exit-tmux` 已完成，且目标是避免自动启动时 `exec` 导致终端关闭；本次目标仅针对 fallback 后的手动 tmux 入口，因此新建 workflow。
- 当前 `CODEX_HOME`: `/home/loviya/.codex-b`。
- 沙盒状态: 普通工具命令因 `/home/loviya/.codex-b/memories/.git` 与 writable symlink 规则冲突无法启动 bwrap，后续只读检查使用提权执行。


## Key Results

- 修改 `/home/loviya/.zshrc`：在自动启动 tmux fallback 逻辑之后新增 `tmux()` 包装函数。
- 进入/附着 session 的手动入口会 `exec`：`tmux`、`tmux new`、`tmux new-session`、`tmux attach`、`tmux attach-session`。
- 管理命令不 `exec`：例如 `tmux ls`、`tmux source-file ~/.tmux.conf` 仍会返回当前 shell。
- 已在 tmux pane 内时不 `exec`，避免影响 pane 内管理命令。

## Validation

- `zsh -n /home/loviya/.zshrc`: 通过。
- `zsh -fc ... unset TMUX ... tmux new-session EXEC_MARK; print AFTER_MARK`: 输出无 `AFTER_MARK`，确认进入 session 路径会替换 shell。
- `zsh -fc ... unset TMUX ... tmux ls EXEC_MARK; print AFTER_MARK`: 输出包含 `AFTER_MARK`，确认管理命令会返回 shell。
- `zsh -fc ... TMUX=/tmp/test ... tmux new-session EXEC_MARK; print AFTER_MARK`: 输出包含 `AFTER_MARK`，确认已在 tmux 内时不会 exec。
- `/home/loviya` 不是 git repository，未记录 git diff/status。

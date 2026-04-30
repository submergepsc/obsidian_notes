---
id: 20260430-ctrl-r-history-search
name: ctrl-r-history-search
slug: ctrl-r-history-search
cwd: /home/loviya
summary: "确认当前 Ctrl+r 由 fzf 接管为 Bash 历史搜索，并扩大 Bash 历史容量、加入 prompt-time 同步。"
tags:
  - terminal
  - bash
  - fzf
  - history
priority: normal
---

# Ctrl-r History Search

## Current Snapshot

- status: 已完成
- goal: 查询并调整当前 Ctrl+r/fzf 使用的 Bash 历史来源，扩大记录数量并让多 pane/session 更及时同步。
- blocker: 无。
- next: 新开 shell 或在现有 shell 执行 `source ~/.bashrc` 后生效。
- updated: 2026-04-30 14:47:00 +0800

## Key Results

- `/home/loviya/.bashrc` 加载 `/home/loviya/.fzf.bash`，后者执行 `eval "$(fzf --bash)"`。
- 当前 `bind -X` 显示 `"\C-r": "__fzf_history__"`，说明 Ctrl+r 被 fzf 绑定为历史搜索函数。
- fzf 的 `__fzf_history__` 使用 `builtin fc -lnr -2147483648` 从当前 Bash history 列表取数据，再交给 fzf 搜索和选择。
- `/home/loviya/.bashrc` 当前设置 `HISTSIZE=1000`、`HISTFILESIZE=2000`、`shopt -s histappend`，`/home/loviya/.bash_history` 当前正好 2000 行。
- Ctrl+r 看到的不是独立数据库，而是当前 shell 内存历史加启动时读入的 `.bash_history`；其他 shell/pane 的新命令通常要等写入并重新读取后才可见。
- 已将 `/home/loviya/.bashrc` 调整为 `HISTSIZE=100000`、`HISTFILESIZE=200000`，并通过 `PROMPT_COMMAND` 调用 `__codex_history_sync`，每次 prompt 执行 `history -a; history -n`。

## Decisions

- 保留 fzf 的 Ctrl+r 入口，只改 Bash history 的容量和同步策略。
- 使用 `history -a; history -n`，不使用 `history -c; history -r`，避免每次 prompt 清空并重载当前 shell 内存历史。

## 查询 Ctrl+r 历史搜索来源

- updated: 2026-04-30 14:43:26 +0800
- cwd: `/home/loviya`
- source instruction: `查询一下当前ctrl+r实现的是什么功能,只能存储2000条记录,而且不是最新的两千条`
- problem:
  - 用户希望确认 Ctrl+r 的实际实现，并理解历史记录只有 2000 条且内容顺序不像最新 2000 条的原因。
- improvement:
  - 检查 tmux key binding、Bash/readline binding、fzf shell binding、`.bashrc` 历史配置和 `.bash_history` 行数。
- result:
  - 当前 Ctrl+r 是 fzf 的 Bash 历史搜索入口，不是 tmux 功能。
  - 2000 条限制来自 `HISTFILESIZE=2000`；当前 shell 内存历史还受 `HISTSIZE=1000` 影响。
  - 不是最新 2000 条的常见原因是 Bash 默认不在每条命令后实时把所有 pane/session 的历史互相同步；`histappend` 只避免覆盖，多个 shell 退出或写入的顺序也可能让 `.bash_history` 的行序不等于真实执行时间。
- next:
  - 如需改造，可把 `HISTSIZE`/`HISTFILESIZE` 放大，并设置每次显示 prompt 时 `history -a; history -n` 或更严格的 `history -a; history -c; history -r` 同步策略。

## 扩大历史容量并加入 Prompt 同步

- updated: 2026-04-30 14:47:00 +0800
- cwd: `/home/loviya`
- source instruction: `调整,并且告诉我你要怎么调整`
- problem:
  - Ctrl+r/fzf 的历史来源受 Bash 上限限制，且多 pane/session 的历史不会实时互相可见。
- improvement:
  - 将 `/home/loviya/.bashrc` 中 `HISTSIZE` 从 1000 提升到 100000。
  - 将 `HISTFILESIZE` 从 2000 提升到 200000。
  - 增加 `__codex_history_sync`，并挂到 `PROMPT_COMMAND`；每次 prompt 时先 `history -a` 写入本 shell 新历史，再 `history -n` 读取其他 shell 追加的新历史。
- result:
  - 新开的 Bash shell 会保留更多内存历史和落盘历史。
  - 多个 tmux pane/terminal session 的新命令会在下一次 prompt 时更快互相同步，Ctrl+r/fzf 能搜索到更接近最新的整体历史。
- next:
  - 新开 shell 或执行 `source ~/.bashrc` 生效。

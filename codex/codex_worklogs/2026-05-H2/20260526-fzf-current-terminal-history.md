---
id: 20260526-fzf-current-terminal-history
name: 当前终端 fzf 历史只显示最近记录排查
slug: fzf-current-terminal-history
cwd: /home/loviya
summary: 排查当前终端 fzf 历史列表只显示最近一条记录的原因，区分 zsh 命令历史、tmux pane scrollback 和 Codex 运行上下文。
tags:
  - zsh
  - fzf
  - history
  - tmux
---

# 当前终端 fzf 历史只显示最近记录排查

## Current Snapshot

- workflow id: 20260526-fzf-current-terminal-history
- current status: 已完成
- current goal: 查明并修复当前终端的 fzf 只能看到历史最近一次记录的问题。
- current blocker: 无
- next step: 无
- tags: zsh, fzf, history, tmux
- summary: `~/.zsh_history` 当前有 1852 行，普通真实交互 zsh 能加载约 1600 条历史；tmux `history-limit` 为 100000，当前 pane 可捕获约 300 行 scrollback。因此容量本身没有被设成 1，最终确认问题来自 fzf 官方 zsh history widget 的重复命令去重逻辑。

## Findings

- `~/.zsh_history` 存在且非空：约 51KB、1852 行。
- `~/.fzf/shell/key-bindings.zsh` 的 `fzf-history-widget` 优先读取 zsh `history` 关联数组；若该数组为空，fzf 输入就会很少。
- 非完整交互式 `zsh -ic ...` 中 `history` 数组为 0，`fc -l 1` 报 `no such event: 1`；这不能代表真实终端。
- 启动真实 PTY 交互 zsh 并禁用自动 tmux 后，`history` 数组为 1617，`fc -l 1 | wc -l` 为 1618，说明普通 zsh 配置能加载历史。
- 当前 tmux 会话 `term-20260526-130956-31790` 里有两个 pane，当前前台命令都是 `node`，说明用户处在 Codex 运行上下文而非裸 zsh prompt。
- tmux 配置 `history-limit 100000`，目标 pane `history_size` 约 235，`capture-pane` 可输出约 309 行。

## Commands

- `wc -l /home/loviya/.zsh_history`
- `zsh -ic '... history ...'` with PTY
- `env CODEX_SANDBOX=1 zsh -i` with PTY
- `tmux list-panes -a`
- `tmux display-message -p -t term-20260526-130956-31790:0.1 '#{history_size} #{history_limit} #{pane_current_command} #{pane_active}'`

## Conclusion

- 根因不是 `~/.zsh_history` 丢失，也不是 tmux history 容量过小。
- `~/.fzf/shell/key-bindings.zsh` 的 `fzf-history-widget` 在把历史交给 fzf 前，会用 Perl/awk 的 `seen[...]` 逻辑按完整命令文本去重。
- 因此同一条命令在历史里执行过多次时，fzf 默认只展示最近一次；这解释了“只能看到历史上最近一次记录”。
- 样本验证：`~/.zsh_history` 中 `codex-b` 有多次重复，`ping google.com` 也至少出现多次，但 widget 代码会过滤旧重复项。

## Verification

- `wc -l /home/loviya/.zsh_history`：历史文件非空且有 1852 行。
- 真实 PTY 交互 zsh：`history` 数组约 1617 条，`fc -l 1 | wc -l` 约 1618。
- `rg -n ";(q|codex-b|ping google\.com|ping chatgpt\.com)$" /home/loviya/.zsh_history`：确认历史文件里存在重复命令。
- `sed -n '128,145p' ~/.fzf/shell/key-bindings.zsh`：确认 fzf widget 使用 `seen[...]` 去重。

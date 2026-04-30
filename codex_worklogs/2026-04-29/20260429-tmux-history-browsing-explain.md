---
id: 20260429-tmux-history-browsing-explain
name: tmux-history-browsing-explain
slug: tmux-history-browsing-explain
cwd: /home/loviya
summary: "说明当前 tmux 历史浏览由 history-limit、mouse on、copy-mode vi 和滚轮/key table 绑定实现。"
tags: [terminal, tmux, history, copy-mode]
priority: normal
---

## 解释当前 tmux 历史浏览的实现方式
- updated: 2026-04-29 15:05:30 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `/tmp/tmux-1000/default,5194,0`
- source instruction: `对与tmux的优化,当前的历史浏览怎么实现的`
- context: 未自动续写 `20260429-tmux-startup-error-recovery`，因为索引中该 workflow 当前为 `已完成`；本次单独记录说明性查询。
- status: 已完成
- problem:
  - goal: 解释当前 tmux 历史浏览的实现方式。
  - blocker: 无。
- result:
  - 读取 `/home/loviya/.tmux.conf` 并确认运行时 `history-limit 100000`、`mouse on`、`mode-keys vi` 生效；当前历史浏览通过 tmux 内置 copy-mode/history buffer 实现，滚轮上滑从 root table 进入 copy-mode，进入后 WheelUp/WheelDown 在 `copy-mode-vi` table 中滚动历史。
- next: 无。
- tags: terminal, tmux, history, copy-mode
#### 查询结论

- 配置入口：`/home/loviya/.tmux.conf`
- 历史容量：`set -g history-limit 100000`
- 鼠标接管：`set -g mouse on`
- copy-mode 键位：`setw -g mode-keys vi`
- 普通 pane 中滚轮上滑：

```tmux
bind -n WheelUpPane if-shell -F -t= "#{pane_in_mode}" \
    "send-keys -M" \
    "copy-mode -e"
```

- copy-mode-vi 中滚轮浏览：

```tmux
bind -T copy-mode-vi WheelUpPane send-keys -X scroll-up
bind -T copy-mode-vi WheelDownPane send-keys -X scroll-down
bind -T copy-mode-vi PageUp send-keys -X page-up
bind -T copy-mode-vi PageDown send-keys -X page-down
bind -T copy-mode-vi q send-keys -X cancel
bind -T copy-mode-vi Escape send-keys -X cancel
```

- 复制绑定：`y`、`Enter`、鼠标拖选松开都走 `copyq --start-server add - && copyq --start-server select 0`，使内容进入 CopyQ 历史并同步为系统剪贴板。

## 复述当前终端会话层次
- updated: 2026-04-30 13:06:35 +0800
- cwd: `/home/loviya`
- tmux: `/tmp/tmux-1000/default,6710,0`
- source instruction: `之前询问过终端的当前会话层次,你再次说一下`
- status: 已完成
- problem:
  - goal: 复述并再次确认当前 Codex 所在终端/tmux 会话层次。
  - blocker: Codex 工具命令运行在 bwrap/sandbox 的独立 PID namespace 中，不能用内部 `ps --forest` 直接看到宿主机完整图形终端进程树。
- result:
  - 当前 pane 由 tmux 自报为 `session=130157-6254 window=0:node pane=1 pane_id=%2 pane_tty=/dev/pts/2 client_tty=/dev/pts/0 socket=/tmp/tmux-1000/default`。
  - 逻辑层次是：外层图形终端/PTY -> tmux client -> tmux server socket `/tmp/tmux-1000/default` -> session `130157-6254` -> window `0:node` -> pane `1` / `%2` -> pane 内 shell/Codex -> Codex sandbox/bwrap -> 本次工具命令。
- next: 无。
- tags: terminal, tmux, session, codex

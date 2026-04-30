---
id: 20260430-terminal-layout-restore
name: terminal-layout-restore
slug: terminal-layout-restore
cwd: /home/loviya
summary: "为 tmux 增加保存和恢复终端窗口/pane 格局的本地脚本与快捷键。"
tags:
  - terminal
  - tmux
  - layout
priority: normal
---

# Terminal Layout Restore

## Current Snapshot

- status: 已完成
- goal: 配置一个可以保存并恢复之前某个 terminal window 会话格局的功能。
- blocker: 无。
- next: 在真实终端里执行 `tmux source-file ~/.tmux.conf` 后使用 Prefix+S 保存、Prefix+R 恢复；或直接运行脚本命令。
- updated: 2026-04-30 13:13:24 +0800

## Key Results

- 新增 `/home/loviya/.local/bin/tmux-layout-save`，保存当前 tmux session 的窗口名、pane 数量、pane 工作目录、窗口布局和当前选中窗口。
- 新增 `/home/loviya/.local/bin/tmux-layout-restore`，从 `~/.tmux-layouts/<name>.layout` 重建窗口和 pane 格局。
- 更新 `/home/loviya/.tmux.conf`，增加 Prefix+S 保存布局、Prefix+R 恢复布局。
- 已用独立临时 tmux socket 验证保存/恢复流程：2 个窗口、分屏数量和 pane 工作目录恢复正常。

## Decisions

- 优先使用 tmux 保存 pane/window 格局，因为本机已安装 tmux，且比依赖 GNOME/kitty 桌面窗口坐标更稳定。
- 第一版只恢复布局和工作目录，不承诺恢复正在运行的交互进程内部状态；如要恢复 vim、shell 命令、服务进程等，需要再接入 `tmux-resurrect`/`tmux-continuum` 一类插件或自定义进程启动模板。

## 配置 tmux 会话格局保存和恢复

- updated: 2026-04-30 13:08:50 +0800
- cwd: `/home/loviya`
- source instruction: `我想要配置一个可以保存之前某个终端terminal windows会话格局的功能,能实现吗`
- problem:
  - 用户希望保存之前某个 terminal window 的会话格局，以便后续恢复。
  - 当前环境有 `tmux`、`gnome-terminal`、`kitty`、`xdotool`、`wmctrl`，但 Codex 沙盒内不能连接用户 tmux socket。
- improvement:
  - 实现本地 tmux layout 保存/恢复脚本，避免依赖网络插件。
  - 在 `.tmux.conf` 增加快捷键入口。
- result:
  - 可用 `tmux-layout-save <name>` 保存当前 tmux session 格局。
  - 可用 `tmux-layout-restore <name>` 恢复为新 session。
  - 可在 tmux 内用 Prefix+S/Prefix+R 调用。
  - 通过 `tmux -L codex-layout-test` 临时 server 验证保存/恢复成功。
- next:
  - 在真实终端中执行 `tmux source-file ~/.tmux.conf` 让当前 tmux server 立即加载新快捷键。

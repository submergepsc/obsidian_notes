---
id: 20260430-tmux-pane-history-browser
name: tmux-pane-history-browser
slug: tmux-pane-history-browser
cwd: /home/loviya
summary: "为任意 tmux pane 增加通用 scrollback 历史快速翻阅入口。"
tags:
  - terminal
  - tmux
  - history
priority: normal
---

# Tmux Pane History Browser

## Current Snapshot

- status: 已完成
- goal: 实现一个通用功能，用于快速翻阅当前 tmux pane 的会话历史记录。
- blocker: 无。
- next: 在任意 tmux pane 中按 Prefix+u 进入历史浏览。
- updated: 2026-04-30 13:26:53 +0800

## Key Results

- 新增 `/home/loviya/.local/bin/tmux-pane-history-browse`，可抓取任意 tmux pane 的 scrollback 历史。
- 更新 `/home/loviya/.tmux.conf`，新增 Prefix+u 绑定，直接进入当前 pane 的 tmux copy-mode scrollback。
- 已执行 `tmux source-file /home/loviya/.tmux.conf`，当前 tmux server 已加载新绑定。

## Decisions

- 该功能作为通用 tmux 工具实现，不绑定 Codex、OpenClaw 或某个具体 shell 程序。
- 快捷键入口最终使用 tmux 原生 copy-mode，避免 popup/fzf/less 在当前终端环境中闪退。
- 复制仍沿用 copy-mode 中已有的 `v` 选择、`y`/Enter 复制到 CopyQ。

## 增加通用 Pane 历史浏览弹窗

- updated: 2026-04-30 13:20:00 +0800
- cwd: `/home/loviya`
- source instruction: `我想要实现一下能够快速翻阅这个pane的会话的历史记录的功能` / `我想要实现的是一个通用的功能`
- problem:
  - 用户希望快速翻阅当前 pane 的会话历史，且功能应通用于任意 tmux pane。
- improvement:
  - 新增 `tmux-pane-history-browse` 脚本，使用 `tmux capture-pane` 抓取 scrollback。
  - 在 `.tmux.conf` 中绑定 Prefix+u，用 popup 展示当前 pane 历史。
- result:
  - 进入 tmux 后可用 Prefix+u 打开历史浏览弹窗。
  - 默认用 `fzf` 搜索；输入关键字过滤，Enter 复制选中行，Ctrl-C 退出。
  - 已做脚本语法检查、配置加载检查、键位检查和 `capture-pane` 抓取验证。
- next:
  - 无；实际使用时直接按 Prefix+u。

## 避开 Prefix+H 冲突

- updated: 2026-04-30 13:20:00 +0800
- cwd: `/home/loviya`
- source instruction: `等一下,ctrla+h冲突了`
- problem:
  - Prefix+h 已用于左移 pane，Prefix+H 又接近 copy-mode 中的 `H` 顶部跳转语义，实际使用容易混淆或冲突。
- improvement:
  - 在 `.tmux.conf` 中显式 `unbind H`。
  - 将历史浏览弹窗改为 Prefix+u。
- result:
  - Prefix+h/H 不再承担历史浏览入口；Prefix+u 是当前通用 pane 历史浏览快捷键。
- next:
  - 无。

## 改用 Tmux 原生 Copy-Mode 入口

- updated: 2026-04-30 13:26:53 +0800
- cwd: `/home/loviya`
- source instruction: `还是智慧一闪而过`
- problem:
  - popup 方案在当前终端里仍然一闪而过，说明 popup 内部交互程序没有稳定停留。
- improvement:
  - 将 Prefix+u 从 popup/fzf 方案改成 `copy-mode -e` 并自动向上翻一页。
  - 继续复用现有 copy-mode vi 键位、鼠标滚轮和 CopyQ 复制绑定。
- result:
  - Prefix+u 现在进入 tmux 原生历史浏览模式，应该稳定停留并可选择文本。
- next:
  - 无。

## 修复 Prefix+u 弹窗闪退

- updated: 2026-04-30 13:21:37 +0800
- cwd: `/home/loviya`
- source instruction: `c-a u 只会快速闪过,无法选择`
- problem:
  - Prefix+u 打开 popup 后立即关闭，无法停留选择历史记录。
  - 旧脚本把所有 `fzf` 非零退出都当作用户取消，真实错误也会静默关闭。
- improvement:
  - 将 `.tmux.conf` 绑定改为脚本绝对路径 `/home/loviya/.local/bin/tmux-pane-history-browse`。
  - 区分 `fzf` 的取消退出和错误退出；错误时输出原因并在自动模式下退回 `less`。
- result:
  - popup 不应再因找不到命令或 `fzf` 启动错误而直接闪退。
- next:
  - 在真实 pane 中再次按 Prefix+u 验证交互。

## 保留 Fzf 交互终端输出

- updated: 2026-04-30 13:23:30 +0800
- cwd: `/home/loviya`
- source instruction: `c-a u 只会快速闪过,无法选择`
- problem:
  - 捕获 `fzf` stderr 可能会隐藏它在 popup 中绘制的交互界面。
- improvement:
  - 去掉 `fzf` stderr 重定向，只保留退出码判断。
  - `fzf` 真失败时提示 1 秒后退回 `less`。
- result:
  - `fzf` 能直接使用 popup 的终端界面；失败路径仍不会直接闪退。
- next:
  - 无。

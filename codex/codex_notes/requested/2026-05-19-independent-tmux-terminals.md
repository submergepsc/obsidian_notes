---
title: 多终端默认独立 tmux session
area: terminal
requested_by_user: true
importance: user-requested
review_priority: high
tags: [user-requested, important, terminal, tmux, zsh, bash, startup]
source_worklog: 20260519-independent-tmux-terminals
updated: 2026-05-19 18:40:41 +0800
---
3.830203470 - 3.473443789 = 0.356759681 秒
# 多终端默认独立 tmux session

## 结论

默认新开的图形终端应自动进入 tmux，但每个终端必须创建自己的独立 session，不能共同 attach 到 `main`。

错误模式：

```sh
exec tmux new-session -A -s main
```

这会让所有新终端进入同一个 `main` session，共享 window、pane、当前目录和正在运行的命令，不符合“多个终端独立使用”的需求。

正确模式：

```sh
__codex_tmux_session="term-$(date +%Y%m%d-%H%M%S)-$$"
exec tmux new-session -s "$__codex_tmux_session"
```

这样每个新终端都会进入类似 `term-20260519-184041-12345` 的独立 tmux session。

## 当前配置位置

`/home/loviya/.zshrc` 末尾自动 tmux 块：

```sh
if command -v tmux >/dev/null 2>&1 && [ -z "$TMUX" ] && [ "$TERM" != "dumb" ] && [ -z "$CODEX_SANDBOX" ] && [ -z "$CODEX_AUTO_TMUX_TRIED" ]; then
  export CODEX_AUTO_TMUX_TRIED=1
  __codex_tmux_session="term-$(date +%Y%m%d-%H%M%S)-$$"
  exec tmux new-session -s "$__codex_tmux_session"
fi
```

`/home/loviya/.bashrc` 自动 tmux 块：

```sh
if command -v tmux >/dev/null 2>&1 && [ -z "$TMUX" ] && [ "$TERM" != "dumb" ] && [ -z "$CODEX_AUTO_TMUX_TRIED" ]; then
	export CODEX_AUTO_TMUX_TRIED=1
	__codex_tmux_session="term-$(date +%Y%m%d-%H%M%S)-$$"
	exec tmux new-session -s "$__codex_tmux_session"
fi
```

## 手动共享 session

如果确实需要共享一个工作区，手动执行：

```sh
tmux new-session -A -s main
```

这应该是显式操作，不应作为默认终端启动行为。

## 验证

本次验证结果：

```sh
zsh -n /home/loviya/.zshrc
bash -n /home/loviya/.bashrc
```

两者通过。

隔离 tmux socket 下创建 `term-test-1` 和 `term-test-2`，`tmux list-sessions` 显示两个 session 同时存在，证明独立 session 策略可行。

## 注意

不要再把默认启动改回 `exec tmux new-session -A -s main`。它解决的是共享/续接同一 session，不是多终端独立使用。

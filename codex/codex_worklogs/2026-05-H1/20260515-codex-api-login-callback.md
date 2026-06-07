---
id: 20260515-codex-api-login-callback
name: Codex API Login Callback
slug: codex-api-login-callback
cwd: /home/loviya
summary: "修复 Codex OAuth 回调 localhost:1455 refused：在 CODEX_HOME=/home/loviya/.codex-api 下启动 codex login 并完成 ChatGPT 登录。"
tags:
  - codex
  - oauth
  - login
priority: normal
---

# Codex API 登录 Callback

## 当前快照

- 状态: 已完成
- 目标: 解决 OpenAI OAuth 回调 `localhost:1455` 连接被拒绝。
- 阻塞: 无
- 下一步: 无
- 更新时间: 2026-05-15 19:53:00 +0800

## 关键结果

- 原因：浏览器打开的 OAuth 回调地址需要本地 `codex login` 进程监听 `localhost:1455`；当时 1455 端口没有监听，所以浏览器显示 `ERR_CONNECTION_REFUSED`。
- 处理：以 `CODEX_HOME=/home/loviya/.codex-api` 启动 `/home/loviya/.local/bin/codex login`，重新生成授权链接并监听回调。
- 结果：浏览器完成授权后，登录进程输出 `Successfully logged in`。
- 验证：`CODEX_HOME=/home/loviya/.codex-api codex login status` 显示 `Logged in 使用 ChatGPT`，并生成 `/home/loviya/.codex-api/auth.json`。

## 重启 本地 OAuth Callback Listener

- 更新时间: 2026-05-15 19:53:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: 用户截图显示 `localhost 拒绝连接`，询问如何解决。
- 问题:
  - 用户直接访问了 OpenAI OAuth URL，但本地 `localhost:1455` 回调服务没有运行。
- 命令:
  - `ss -ltnp`
  - `CODEX_HOME=/home/loviya/.codex-api /home/loviya/.local/bin/codex login`
  - `xdg-open '<new OAuth URL>'`
  - `CODEX_HOME=/home/loviya/.codex-api /home/loviya/.local/bin/codex login status`
- 结果:
  - 旧 OAuth URL 的 state/code_challenge 不再使用；由新的 `codex login` 进程生成新 URL。
  - 新登录流程成功，API runtime home `/home/loviya/.codex-api` 已登录 ChatGPT。
- 下一步:
  - 无

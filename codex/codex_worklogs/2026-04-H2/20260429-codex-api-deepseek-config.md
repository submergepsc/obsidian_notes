---
id: 20260429-codex-api-deepseek-config
name: codex-api-deepseek-config
slug: codex-api-deepseek-config
cwd: /home/loviya
summary: 配置 `/home/loviya/.codex-api`，让 Codex 通过 OpenAI 兼容的 chat API 使用 DeepSeek。
tags:
  - codex
  - deepseek
  - config
priority: normal
---

## 将 /home/loviya/.codex-api/config.toml 默认模型供应...
- 更新时间: 2026-04-29 21:55:15 +0800
- 工作目录: `/home/loviya`
- 主机: `nibaba`
- tmux: `182126-27850:0.1`
- 来源指令: `你帮我配置一下.codex-api的内容,这个我想要使用deepseek来调用`
- 上下文: 未找到强匹配未完成 workflow，新建当前配置任务 workflow。
- 状态: 已完成
- 问题:
  - 目标: 将 `/home/loviya/.codex-api/config.toml` 默认模型供应商切换为 DeepSeek，并配置启动时加载 API key。
  - 阻塞: 无。
- 结果:
  - 新增 `[model_providers.deepseek]`，默认 `model_provider = "deepseek"`、`model = "deepseek-v4-flash"`、`wire_api = "chat"`；新增 `deepseek.env` 和 `codex-deepseek` 启动脚本，保留原 `relay` provider 作为备用。
- 下一步: 用 `/home/loviya/.codex-api/codex-deepseek` 启动验证实际对话。
- 标签: codex, deepseek, config
## 验证 DeepSeek API key、模型和启动脚本可用
- 更新时间: 2026-04-29 21:56:35 +0800
- 工作目录: `/home/loviya`
- 主机: `nibaba`
- tmux: `182126-27850:0.1`
- 来源指令: `测试一下`
- 上下文: 继续 `.codex-api` DeepSeek 配置验证。
- 状态: 已完成
- 问题:
  - 目标: 验证 DeepSeek API key、模型和启动脚本可用。
  - 阻塞: 无。
- 结果:
  - 先因本地代理 `127.0.0.1:7897` 未运行失败，取消代理后沙箱 DNS 受限；经授权联网请求 `https://api.deepseek.com/chat/completions` 成功，HTTP 200，`deepseek-v4-flash` 返回 `ok`。`/home/loviya/.codex-api/codex-deepseek --version` 返回 `codex-cli 0.125.0`。
- 下一步: 无。
- 标签: codex, deepseek, config, verification
## 提供 codex-api 命令来启动 /home/loviya/.codex-api 配...
- 更新时间: 2026-04-29 21:58:00 +0800
- 工作目录: `/home/loviya`
- 主机: `nibaba`
- tmux: `182126-27850:0.1`
- 来源指令: `我要用codex-api来启动.codex-api里面的配吹`
- 上下文: 继续 `.codex-api` DeepSeek 配置入口。
- 状态: 已完成
- 问题:
  - 目标: 提供 `codex-api` 命令来启动 `/home/loviya/.codex-api` 配置。
  - 阻塞: 无。
- 结果:
  - 新增 `/home/loviya/.local/bin/codex-api`，调用 `/home/loviya/.codex-api/codex-deepseek "$@"`；`codex-api --version` 验证返回 `codex-cli 0.125.0`。
- 下一步: 无。
- 标签: codex, deepseek, command-wrapper
## 删除刚创建的 codex-api 命令包装文件，保留用户已有 alias
- 更新时间: 2026-04-29 21:59:00 +0800
- 工作目录: `/home/loviya`
- 主机: `nibaba`
- tmux: `182126-27850:0.1`
- 来源指令: `搞错了,把这个删了,我已经配置了alias`
- 上下文: 继续 `.codex-api` DeepSeek 配置入口清理。
- 状态: 已完成
- 问题:
  - 目标: 删除刚创建的 `codex-api` 命令包装文件，保留用户已有 alias。
  - 阻塞: 无。
- 结果:
  - 删除 `/home/loviya/.local/bin/codex-api`；未改动 `/home/loviya/.codex-api/config.toml`、`deepseek.env` 或用户 alias。
- 下一步: 无。
- 标签: codex, deepseek, cleanup
## 修复 Codex 0.125 启动时报 wire_api = "chat" 不支持的问题...
- 更新时间: 2026-04-29 22:03:20 +0800
- 工作目录: `/home/loviya`
- 主机: `nibaba`
- tmux: `182126-27850:0.1`
- 来源指令: `loviya@nibaba:~$ codex-api ... wire_api = "chat" is no longer supported ...`
- 上下文: 继续 `.codex-api` DeepSeek 配置故障排查。
- 状态: 阻塞
- 问题:
  - 目标: 修复 Codex 0.125 启动时报 `wire_api = "chat"` 不支持的问题，并验证 DeepSeek 连接。
  - 阻塞: Codex 0.125 只支持 `wire_api = "responses"`；DeepSeek 官方 API 的 `/responses` 和 `/v1/responses` 都返回 HTTP 404，当前不能被新版 Codex 直接作为 provider 使用。
- 结果:
  - 已将 `/home/loviya/.codex-api/config.toml` 的 DeepSeek provider 改为 `wire_api = "responses"`，配置解析通过；`codex exec` 真实请求失败于 `https://api.deepseek.com/responses` 404；直接探测 `https://api.deepseek.com/v1/responses` 也为 404。
- 下一步: 选择一个兼容方案：使用能把 Responses 转 Chat Completions 的中转服务，或降级/固定仍支持 `wire_api = "chat"` 的 Codex 版本，或改用支持 Responses API 的 provider。
- 标签: codex, deepseek, responses-api, blocker
## 将 .codex-api 默认 provider 切到 Responses 兼容 pro...
- 更新时间: 2026-04-29 22:06:10 +0800
- 工作目录: `/home/loviya`
- 主机: `nibaba`
- tmux: `182126-27850:0.1`
- 来源指令: `3`
- 上下文: 按用户选择执行第 3 个方案，改用支持 Responses API 的 provider。
- 状态: 阻塞
- 问题:
  - 目标: 将 `.codex-api` 默认 provider 切到 Responses 兼容 provider。
  - 阻塞: 已切到已有 `relay` provider，但当前环境缺少 `MUXUFO_API_KEY`，真实请求无法认证。
- 结果:
  - `/home/loviya/.codex-api/config.toml` 默认改为 `model_provider = "relay"`、`model = "claude-opus-4-1-20250805"`；配置解析通过，`codex exec` 进入 relay 后报 `Missing environment variable: MUXUFO_API_KEY`。
- 下一步: 在 alias 或环境文件中设置 `MUXUFO_API_KEY` 后重新运行 `codex-api`。
- 标签: codex, relay, responses-api, config
## 配置 MUXUFO_API_KEY 并让用户的 codex-api alias 自动加载
- 更新时间: 2026-04-29 22:11:20 +0800
- 工作目录: `/home/loviya`
- 主机: `nibaba`
- tmux: `182126-27850:0.1`
- 来源指令: `sk-...`
- 上下文: 继续 `.codex-api` relay provider 认证配置。
- 状态: 待继续
- 问题:
  - 目标: 配置 `MUXUFO_API_KEY` 并让用户的 `codex-api` alias 自动加载。
  - 阻塞: relay 真实请求已不再缺 key，但服务端返回 “We're currently experiencing high demand, which may cause temporary errors.”
- 结果:
  - 新增 `/home/loviya/.codex-api/relay.env` 并设为 600 权限；更新 `/home/loviya/.bashrc` 中 `codex-api` alias 为先 source relay env 再设置 `CODEX_HOME`。交互 shell 检查 alias 展开和 key 加载通过。
- 下一步: 稍后重新运行 `codex-api`；若仍高需求，检查 relay 服务状态或更换可用 Responses API provider。
- 标签: codex, relay, api-key, alias

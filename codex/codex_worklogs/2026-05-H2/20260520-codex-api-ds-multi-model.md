---
id: 20260520-codex-api-ds-multi-model
name: codex-api-ds 多模型选择
slug: codex-api-ds-multi-model
cwd: /home/loviya
summary: 为 codex-api-ds 增加 DeepSeek V4 Pro/Flash 多模型选择，默认仍为 V4 Pro。
tags:
  - codex-api-ds
  - deepseek
  - model-selection
  - provider-config
---

# codex-api-ds 多模型选择

## Current Snapshot

- workflow id: 20260520-codex-api-ds-multi-model
- current status: 进行中
- current goal: 在 `codex-api-ds` 内配置 DeepSeek 多模型选择，保留默认 `deepseek-v4-pro`。
- current blocker: 无
- next step: 更新 DS catalog 和启动器，验证配置和最小请求。
- tags: codex-api-ds, deepseek, model-selection, provider-config
- summary: 用户澄清目标是在 DS 环境里做多模型选择，不是把 DeepSeek provider 加进 MiMo。官方当前模型为 `deepseek-v4-pro` 和 `deepseek-v4-flash`；旧 `deepseek-chat`/`deepseek-reasoner` 将于 2026-07-24 弃用。


---
id: 20260521-codex-api-mimo-free-other-config
name: codex-api-mimo-free-other 配置
slug: codex-api-mimo-free-other-config
cwd: /home/loviya
summary: 为 newapi.lingrana.top 新建独立 codex-api-mimo-free-other API home、env、启动器和本地 Responses proxy。
tags:
  - codex-api
  - mimo2
  - newapi
  - provider
---

# codex-api-mimo-free-other 配置

## Current Snapshot

- workflow id: 20260521-codex-api-mimo-free-other-config
- current status: 已完成
- current goal: 配置 `/home/loviya/.codex-api-mimo-free-other`，使用用户提供的 OpenAI-compatible endpoint，并提供 `codex-api-mimo-free-other` 启动入口
- current blocker: none
- next step: none
- tags: codex-api, mimo2, newapi, provider
- summary: 已完成独立 API home、env、启动器、本地 Responses proxy 和全局账户清单配置；`codex-api-mimo-free-other exec` 最小真实调用成功返回 `ok`。

## Key Results

- 新建 `/home/loviya/.codex-api-mimo-free-other`，账户状态与现有 API home 隔离。
- 复用已验证的本地 Responses proxy 形态：Codex 访问 `http://127.0.0.1:18794/v1`，proxy 转发到上游 `/chat/completions`。

## Commands

- `mkdir -p /home/loviya/.codex-api-mimo-free-other/...`：创建账户目录。
- `cp /home/loviya/.codex-api-mimo-pay-self/mimo_responses_proxy.py ...`：复用 proxy 实现。

## Verification

- `curl /v1/models`：上游可访问，模型列表包含 `mimo-v2.5-pro`、`mimo-v2.5`、`mimo-v2-omni`、`mimo-v2.5-tts`。
- `CODEX_HOME=/home/loviya/.codex-api-mimo-free-other codex debug models`：配置解析成功，`mimo-v2.5-pro` metadata 可用。
- `/home/loviya/.local/bin/codex-api-mimo-free-other --version`：返回 `codex-cli 0.132.0`。
- `/home/loviya/.local/bin/codex-api-mimo-free-other exec --skip-git-repo-check --sandbox read-only --json "只回复 ok"`：真实调用成功，返回正文 `ok`。

## Decisions

- 默认模型使用上游实际支持的 `mimo-v2.5-pro`。
- 使用 `http://127.0.0.1:18794/v1` 作为 Codex Responses endpoint，由本地 proxy 转发到 `https://newapi.lingrana.top/v1/chat/completions`。
- `mimo2` proxy 单独增加常规 `User-Agent`/`Accept` header，避免上游对 Python 默认 urllib 请求返回 `403 error code: 1010`。
- `mimo2` proxy 单独清理上游正文中的 `<think>...</think>` 和 NUL 字符，避免 Codex UI 显示思考块。

## Artifacts

- `/home/loviya/.codex-api-mimo-free-other/config.toml`
- `/home/loviya/.codex-api-mimo-free-other/mimo2.env`
- `/home/loviya/.codex-api-mimo-free-other/codex-api-mimo-free-other`
- `/home/loviya/.codex-api-mimo-free-other/mimo2_responses_proxy.py`
- `/home/loviya/.local/bin/codex-api-mimo-free-other`
- `/home/loviya/.local/bin/codex_api_mimo_free_other`
- `/home/loviya/.codex/AGENTS.md`

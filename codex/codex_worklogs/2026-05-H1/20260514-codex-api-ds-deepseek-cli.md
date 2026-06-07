---
id: 20260514-codex-api-ds-deepseek-cli
name: Codex API DS DeepSeek CLI
slug: codex-api-ds-deepseek-cli
cwd: /home/loviya
summary: 创建隔离的 DeepSeek 专用 Codex runtime home 和启动器 `codex-api-ds`。
tags:
  - codex
  - deepseek
  - runtime-home
  - cli
priority: normal
---

# Codex API DS DeepSeek CLI

## 当前快照

- 状态: 已完成
- 目标: 提供 `codex-api-ds`，用 `/home/loviya/.codex-api-ds` 启动 Codex 并把请求路由到 DeepSeek。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-15 00:25:52 +0800

## 关键结果

- 已创建 `/home/loviya/.codex-api-ds` as an independent runtime home.
- Shared only managed content paths from `/home/loviya/.codex`: `AGENTS.md`, `continue.md`, `worklogs`, `skills`, `rules`, `memories`, `vendor_imports`, and shared plugins.
- 已新增 `/home/loviya/.local/bin/codex-api-ds` and `/home/loviya/.codex-api-ds/codex-api-ds`.
- Stored the DeepSeek key in `/home/loviya/.codex-api-ds/deepseek.env` 带 `600` permissions.
- 已新增 `/home/loviya/.codex-api-ds/deepseek_responses_proxy.py` 因为 Codex 0.130 uses the Responses API while DeepSeek exposes Chat Completions.
- Configured `/home/loviya/.codex-api-ds/config.toml` to use `model_provider = "deepseek"`, `model = "deepseek-chat"`, and the local compatibility endpoint `http://127.0.0.1:18792/v1`.
- 已更新 `/home/loviya/.codex/AGENTS.md` so `.codex-api-ds` is documented as a DeepSeek-specific API runtime home.

## 验证

- `codex-api-ds --version` 返回 `codex-cli 0.130.0`.
- Direct DeepSeek Chat Completions validation 带 the new key 返回 HTTP 200 and `ok`.
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "只回复 ok"` completed successfully through the compatibility proxy and 返回 `ok`.
- The local proxy runs in tmux session `codex-ds-proxy` on `127.0.0.1:18792`.

## 说明

- 不要write API keys into worklogs, `continue.md`, or codex notes.
- Port `18791` was already occupied by `openclaw-gateway`, so the DeepSeek compatibility proxy uses `18792`.

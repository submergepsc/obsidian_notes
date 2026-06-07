---
id: 20260519-codex-api-ds-model-metadata
name: codex-api-ds Model Metadata
slug: codex-api-ds-model-metadata
cwd: /home/loviya/notes/obsidian_notes/25_2/cn
summary: 为 `deepseek-v4-pro` 增加本地 Codex model catalog，解决启动时 fallback metadata 警告。
tags:
  - codex
  - deepseek
  - codex-api-ds
  - model-metadata
priority: normal
---

# codex-api-ds Model Metadata

## Current Snapshot

- workflow id: 20260519-codex-api-ds-model-metadata
- current status: 已完成
- current goal: 消除 `Model metadata for deepseek-v4-pro not found` 启动警告。
- current blocker: 无。
- next step: 无。
- tags: codex, deepseek, codex-api-ds, model-metadata
- summary: 已新增本地 model catalog 并让 `.codex-api-ds/config.toml` 指向它；最小启动验证不再出现 fallback metadata 警告。

## Key Results

- 新增 `/home/loviya/.codex-api-ds/deepseek-models.json`。
- 更新 `/home/loviya/.codex-api-ds/config.toml`：
  - `model_catalog_json = "/home/loviya/.codex-api-ds/deepseek-models.json"`
  - 保留 `model_context_window = 1048576`
- 首次验证时 Codex 已读取 catalog，但报 `missing field base_instructions`；已补充精简 `base_instructions`。

## Reason

- `model_context_window` 只覆盖上下文窗口，不会让 Codex 的 model manager 认为 `deepseek-v4-pro` 有完整 metadata。
- 启动警告来自 model catalog/cache 查不到模型 slug。
- `model_catalog_json` 是 Codex 本地配置项，用来加载自定义模型 metadata。

## Verification

- `python3 -m json.tool /home/loviya/.codex-api-ds/deepseek-models.json` 通过。
- `/home/loviya/.codex-api-ds/codex-api-ds exec --skip-git-repo-check --sandbox read-only "只回复 ok"` 启动头部显示 `model: deepseek-v4-pro`、`provider: deepseek`，未再出现 `Model metadata for deepseek-v4-pro not found`。
- 同一次最小请求中出现过 `ERROR: Reconnecting... 1/5`，但最终返回 `ok`；这是连接重试，不是 metadata fallback。

## Notes Update

- 已更新 `/home/loviya/.codex/codex_notes/requested/2026-05-19-codex-api-ds-deepseek-responses-proxy.md`，补充 `deepseek-models.json` 和 `model_catalog_json` 的作用。

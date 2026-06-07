---
id: 20260520-codex-api-mimo-pay-self-deepseek-selection
name: codex-api-mimo-pay-self DeepSeek 模型选择
slug: codex-api-mimo-pay-self-deepseek-selection
cwd: /home/loviya
summary: 为 codex-api-mimo-pay-self 增加 DeepSeek provider/model catalog 选择能力，默认 MiMo 不变。
tags:
  - codex-api-mimo-pay-self
  - codex-api-ds
  - provider-config
  - model-selection
---

# codex-api-mimo-pay-self DeepSeek 模型选择

## Current Snapshot

- workflow id: 20260520-codex-api-mimo-pay-self-deepseek-selection
- current status: 进行中
- current goal: 在 `codex-api-mimo-pay-self` 中增加 DeepSeek 模型选择能力，同时保留默认 MiMo 链路。
- current blocker: 无
- next step: 修改 `.codex-api-mimo-pay-self` 配置、catalog 和启动器，然后验证配置解析。
- tags: codex-api-mimo-pay-self, codex-api-ds, provider-config, model-selection
- summary: 已确认 `codex-api-mimo-pay-self` 默认走 18793 MiMo Responses 代理，`codex-api-ds` 走 18792 DeepSeek Responses 代理；应新增独立 DeepSeek provider，而不是把 DeepSeek 模型名发给 MiMo 代理。

## Key Results

- 更新 `/home/loviya/.codex-api-mimo-pay-self/config.toml`：新增 `model_catalog_json`、上下文窗口设置和 `[model_providers.deepseek]`。
- 新增 `/home/loviya/.codex-api-mimo-pay-self/model_catalog.json`：包含 `mimo-v2.5-pro` 和 `deepseek-v4-pro`。
- 更新 `/home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self`：支持 `CODEX_API_MIMO_PROVIDER=deepseek` 或 `CODEX_API_MIMO_MODEL=deepseek-v4-pro`，默认 MiMo 不变。
- 更新 notes: `requested/2026-05-20-codex-api-mimo-pay-self-vs-ds-config.md`。

## Verification

- `python3 -m json.tool /home/loviya/.codex-api-mimo-pay-self/model_catalog.json` 通过。
- `bash -n /home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self` 通过。
- `CODEX_HOME=/home/loviya/.codex-api-mimo-pay-self codex --strict-config --help` 通过。
- `/home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self --version` 返回 `codex-cli 0.131.0`。
- 默认 MiMo 最小真实请求启动为 `provider: mimo`、`model: mimo-v2.5-pro`，但上游返回 502 SSL EOF。
- DeepSeek 分支最小真实请求启动为 `provider: deepseek`、`model: deepseek-v4-pro`，返回 `ok`。

## Current Snapshot

- workflow id: 20260520-codex-api-mimo-pay-self-deepseek-selection
- current status: 已完成
- current goal: 在 `codex-api-mimo-pay-self` 中增加 DeepSeek 模型选择能力，同时保留默认 MiMo 链路。
- current blocker: 无
- next step: 无
- tags: codex-api-mimo-pay-self, codex-api-ds, provider-config, model-selection
- summary: `codex-api-mimo-pay-self` 现在可通过环境变量选择 DeepSeek provider，默认 MiMo 不变；DeepSeek 分支已真实请求验证成功。

## Follow-up: 删除 DeepSeek 模型选择

- 用户要求“删了”。按上下文解释为删除刚加入 `codex-api-mimo-pay-self` 的 DeepSeek 模型选择能力。
- 已从备份恢复 `/home/loviya/.codex-api-mimo-pay-self/config.toml`。
- 已从备份恢复 `/home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self`。
- 已删除新增的 `/home/loviya/.codex-api-mimo-pay-self/model_catalog.json`。
- 保留备份文件，便于之后需要时手动对照。

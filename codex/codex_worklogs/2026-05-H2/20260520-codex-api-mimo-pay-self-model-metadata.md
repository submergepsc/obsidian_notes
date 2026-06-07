---
id: 20260520-codex-api-mimo-pay-self-model-metadata
name: codex-api-mimo-pay-self MiMo 模型 metadata
slug: codex-api-mimo-pay-self-model-metadata
cwd: /home/loviya
summary: 为 codex-api-mimo-pay-self 增加 mimo-v2.5-pro 本地 model catalog，消除 fallback metadata warning。
tags:
  - codex-api-mimo-pay-self
  - model-metadata
  - mimo
---

# codex-api-mimo-pay-self MiMo 模型 metadata

## Current Snapshot

- workflow id: 20260520-codex-api-mimo-pay-self-model-metadata
- current status: 进行中
- current goal: 消除 `Model metadata for mimo-v2.5-pro not found` warning。
- current blocker: 无
- next step: 更新 config 和 model catalog 后验证。
- tags: codex-api-mimo-pay-self, model-metadata, mimo
- summary: 当前 `.codex-api-mimo-pay-self/config.toml` 没有 `model_catalog_json`，且默认 `model` 是 `gpt-5.5`；启动器实际使用 `mimo.env` 的 `MIMO_MODEL=mimo-v2.5-pro`，因此 Codex 找不到 MiMo metadata。

## Key Results

- 新增 `/home/loviya/.codex-api-mimo-pay-self/model_catalog.json`，复用已有 MiMo metadata，包含 `mimo-v2.5-pro`。
- 更新 `/home/loviya/.codex-api-mimo-pay-self/config.toml`：
  - `model = "mimo-v2.5-pro"`
  - `model_catalog_json = "/home/loviya/.codex-api-mimo-pay-self/model_catalog.json"`
  - `model_context_window = 1048576`
  - `model_auto_compact_token_limit = 900000`
- 未加入 DeepSeek provider；本次只修复 MiMo metadata warning。

## Verification

- `python3 -m json.tool /home/loviya/.codex-api-mimo-pay-self/model_catalog.json` 通过。
- `CODEX_HOME=/home/loviya/.codex-api-mimo-pay-self codex --strict-config --help` 通过。
- `codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "不要使用工具，只回复 ok"` 启动头无 `Model metadata for mimo-v2.5-pro not found` warning，并返回 `ok`。
- 额外核对：此前中断的 DS 文件仍为合法 JSON / shell，未发现 `deepseek-v4-flash` 或 `CODEX_API_DS_MODEL` 半成品残留。

## Current Snapshot

- workflow id: 20260520-codex-api-mimo-pay-self-model-metadata
- current status: 已完成
- current goal: 消除 `Model metadata for mimo-v2.5-pro not found` warning。
- current blocker: 无
- next step: 无
- tags: codex-api-mimo-pay-self, model-metadata, mimo
- summary: `codex-api-mimo-pay-self` 已配置 MiMo 本地 model catalog，最小真实请求无 metadata warning 并返回 `ok`。

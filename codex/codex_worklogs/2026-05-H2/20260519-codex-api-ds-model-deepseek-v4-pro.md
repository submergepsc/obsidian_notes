---
id: 20260519-codex-api-ds-model-deepseek-v4-pro
name: codex-api-ds Model deepseek-v4-pro
slug: codex-api-ds-model-deepseek-v4-pro
cwd: /home/loviya/notes/obsidian_notes/25_2/cn
summary: 将 DeepSeek 专用 Codex runtime 的入口模型和启动器指定模型同步改为 `deepseek-v4-pro`。
tags:
  - codex
  - deepseek
  - codex-api-ds
  - config
priority: normal
---

# codex-api-ds Model deepseek-v4-pro

## Current Snapshot

- workflow id: 20260519-codex-api-ds-model-deepseek-v4-pro
- current status: 已完成
- current goal: 将 `/home/loviya/.codex-api-ds/config.toml` 的入口模型和 `/home/loviya/.codex-api-ds/codex-api-ds` 末尾 `-m` 指定模型同步改为 `deepseek-v4-pro`。
- current blocker: 无。
- next step: 无。
- tags: codex, deepseek, codex-api-ds, config
- summary: 已按用户要求修改模型名，并完成定点验证。

## Key Results

- `/home/loviya/.codex-api-ds/config.toml`: `model = "gpt-5.5"` 改为 `model = "deepseek-v4-pro"`。
- `/home/loviya/.codex-api-ds/config.toml`: `[tui.model_availability_nux]` 从 `"gpt-5.5" = 1` 同步为 `"deepseek-v4-pro" = 1`。
- `/home/loviya/.codex-api-ds/codex-api-ds`: `codex -m deepseek-chat` 改为 `codex -m deepseek-v4-pro`。

## Notes

- 代理会把 Codex 传入的 `model` 原样转发到 DeepSeek Chat Completions 后端。
- 使用的是官方 V4 Pro 模型 ID `deepseek-v4-pro`，不是 `deepseekv4`。

## Verification

- `rg -n "deepseek-v4-pro|deepseek-chat|gpt-5.5|deepseekv4" /home/loviya/.codex-api-ds/config.toml /home/loviya/.codex-api-ds/codex-api-ds` 只在目标两文件中看到 `deepseek-v4-pro`。
- `bash -n /home/loviya/.codex-api-ds/codex-api-ds` 通过。
- `curl -fsS http://127.0.0.1:18792/health` 返回 `{"ok": true}`。

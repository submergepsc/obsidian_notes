---
id: 20260519-codex-api-ds-v4-thinking-fix
name: codex-api-ds V4 Thinking Fix
slug: codex-api-ds-v4-thinking-fix
cwd: /home/loviya/notes/obsidian_notes/25_2/cn
summary: 修复 DeepSeek V4 Pro 默认 thinking mode 导致 Codex 工具调用后 `reasoning_content` 缺失 400 的问题。
tags:
  - codex
  - deepseek
  - codex-api-ds
  - v4
  - thinking-mode
priority: normal
---

# codex-api-ds V4 Thinking Fix

## Current Snapshot

- workflow id: 20260519-codex-api-ds-v4-thinking-fix
- current status: 已完成
- current goal: 修复 `deepseek-v4-pro` 在 Codex 工具调用后返回 `The reasoning_content in the thinking mode must be passed back to the API` 的问题。
- current blocker: 无。
- next step: 无。
- tags: codex, deepseek, codex-api-ds, v4, thinking-mode
- summary: 已修改代理，对 `deepseek-v4-*` 上游请求显式加 `thinking: disabled`，并用包含 tool output 的最小 live call 验证通过。

## Problem

- `deepseek-v4-pro` 支持 thinking 和 non-thinking，且 thinking 默认启用。
- Codex 的 Responses 适配层没有把 DeepSeek `reasoning_content` 持久化并回传到后续 tool-result 请求。
- DeepSeek 官方要求 thinking mode 中发生 tool call 时，后续请求必须回传 `reasoning_content`；否则上游返回 400。

## Key Results

- 更新 `/home/loviya/.codex-api-ds/deepseek_responses_proxy.py`。
- 新增 `_should_disable_thinking(model)`。
- 对 `deepseek-v4-*` 请求向 DeepSeek Chat Completions payload 加：

```json
{"thinking": {"type": "disabled"}}
```
- 更新 `/home/loviya/.codex-api-ds/config.toml`，为未知模型 `deepseek-v4-pro` 显式设置 `model_context_window = 1048576`，降低 Codex 使用 fallback metadata 的影响。

## Notes

- 这个修复保留 `deepseek-v4-pro` 模型，但让 Codex 代理链路走 V4 Pro 的 non-thinking mode。
- 另一种方案是完整保存和回放 `reasoning_content`，但需要扩展 Responses 适配状态，改动更大且更容易引入跨轮状态错误。

## Verification

- `PYTHONPYCACHEPREFIX=/tmp/codex-pycache python3 -m py_compile /home/loviya/.codex-api-ds/deepseek_responses_proxy.py` 通过。
- `bash -n /home/loviya/.codex-api-ds/codex-api-ds` 通过。
- 已在 tmux 会话 `codex-ds-proxy` 启动新版代理。
- `curl -fsS http://127.0.0.1:18792/health` 返回 `{"ok": true}`。
- `ss -ltnp | rg '18792'` 显示 `python3` 监听 `127.0.0.1:18792`。
- 最小 live call 使用 `deepseek-v4-pro`、包含 `function_call` 与 `function_call_output` 的请求返回 `200` 和 `output_text: "ok"`，未再出现 `reasoning_content` 错误。

## Notes Update

- 用户指出上面的请求层次解释也应该写入 notes，并且之前 note 中的配置已过期。
- 已更新 `/home/loviya/.codex/codex_notes/requested/2026-05-19-codex-api-ds-deepseek-responses-proxy.md`：
  - `gpt-5.5` / `deepseek-chat` 改为当前 `deepseek-v4-pro`。
  - 补充 `model_context_window = 1048576`。
  - 补充 `thinking: {"type": "disabled"}` 的 V4 Pro 兼容原因。
  - 补充 `codex-ds-proxy` tmux 保活方式。
  - 补充为什么 Codex 不直接请求 `api.deepseek.com`。

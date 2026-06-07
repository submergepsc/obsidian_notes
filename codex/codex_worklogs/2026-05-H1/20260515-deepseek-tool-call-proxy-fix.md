---
id: 20260515-deepseek-tool-call-proxy-fix
name: DeepSeek Tool Call Proxy Fix
slug: deepseek-tool-call-proxy-fix
cwd: /home/loviya
summary: 修复 DeepSeek Codex 代理，使 tool calls 走原生调用而不是显示为 DSML 文本。
tags:
  - codex
  - deepseek
  - responses-api
  - tool-calls
priority: normal
---

# DeepSeek Tool Call Proxy 修复

## 当前快照

- 状态: 已完成
- 目标: 阻止 `codex-api-ds` 在 assistant 回复中显示原始 DSML 伪工具调用。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-15 11:25:00 +0800

## 关键结果

- 已更新 `/home/loviya/.codex-api-ds/deepseek_responses_proxy.py`.
- The proxy now maps Responses API function tools into DeepSeek Chat Completions `tools`.
- DeepSeek `tool_calls` are converted back into Responses API `function_call` output items for Codex.
- Responses `function_call_output` history is converted into Chat Completions `tool` messages for follow-up turns.
- 已新增 a compatibility system-instruction suffix telling the model not to print DSML/XML pseudo tool markup.
- 已新增 a fallback text sanitizer for DSML/XML pseudo tool-call blocks in visible assistant text.
- Restarted the DeepSeek proxy in tmux so `127.0.0.1:18792` uses the updated script.

## 验证

- `python3 -m py_compile /home/loviya/.codex-api-ds/deepseek_responses_proxy.py` passed.
- Local helper tests confirmed:
  - Responses tools convert to Chat Completions tools.
  - Responses function-call history converts back into assistant/tool chat messages.
  - DeepSeek tool calls convert into Responses `function_call` output items.
  - DSML pseudo tool-call markup is stripped from visible text as a fallback.
- `curl -fsS http://127.0.0.1:18792/health` 返回 `{"ok": true}` after restart.
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "只回复 ok"` no longer exposed DSML; DeepSeek emitted a native `exec` tool call that Codex executed.
- After a regression where text output became empty, restored the standard stream sequence 带 full `output_text.delta`, `content_part.done`, and `output_item.done` content.
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "不要使用工具，只回复 ok"` now 返回 visible `ok`.
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "运行 pwd 并告诉我结果"` now executes native `exec_command` and records one final assistant message in the session JSONL.

## 说明

- The current controlling session has `CODEX_HOME=/home/loviya/.codex-a`, not `/home/loviya/.codex-api-ds`; this mismatch was reported before editing the DeepSeek-specific runtime files.
- Running `codex-api-ds exec` from the sandbox cannot reach the local proxy port; validation was run outside the sandbox after approval.
- `codex-api-ds exec` may print the final text twice in terminal output 因为 it shows streamed text and then final replay; the session JSONL records a single assistant message.

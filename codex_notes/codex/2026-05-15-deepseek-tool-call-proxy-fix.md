---
date: 2026-05-15
area: codex
importance: normal
source_worklog: 20260515-deepseek-tool-call-proxy-fix
tags:
  - codex
  - deepseek
  - responses-api
  - tool-calls
---

# DeepSeek Tool Call Proxy Fix

## Problem

`codex-api-ds` used a local Responses-to-DeepSeek proxy that forwarded only plain text. Codex still instructed the model to use tools, but the proxy did not pass tool schemas to DeepSeek or convert returned tool calls into Responses API function-call items. DeepSeek therefore printed DSML/XML-like pseudo tool calls as visible assistant text.

## Result

`/home/loviya/.codex-api-ds/deepseek_responses_proxy.py` now:

- Converts Responses API function tool definitions to DeepSeek Chat Completions `tools`.
- Converts DeepSeek `tool_calls` to Responses API `function_call` output items.
- Converts Responses `function_call_output` items back to Chat Completions `tool` messages.
- Appends a compatibility instruction that forbids visible DSML/XML pseudo tool markup.
- Strips DSML/XML pseudo tool-call blocks from visible text as a fallback.

## Verification

- `python3 -m py_compile /home/loviya/.codex-api-ds/deepseek_responses_proxy.py`
- `curl -fsS http://127.0.0.1:18792/health`
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "只回复 ok"` showed native Codex `exec` execution instead of raw DSML.
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "不要使用工具，只回复 ok"` returned visible `ok` after restoring full stream content.
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "运行 pwd 并告诉我结果"` executed native `exec_command` and recorded one assistant message in the session.

## Caveats

Run `codex-api-ds exec` validation outside the sandbox when it needs to contact the local proxy. The current session used `/home/loviya/.codex-a`, so edits to `/home/loviya/.codex-api-ds` were made after explicitly noting the runtime-home mismatch. Terminal `exec` output may display final text twice because it includes both streamed text and final replay, while the session record contains one assistant message.

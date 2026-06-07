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

# DeepSeek 工具调用代理修复

## 问题

`codex-api-ds` 使用本地 Responses-to-DeepSeek 代理，但之前只转发纯文本。Codex 仍会指示模型使用工具，但代理没有把 tool schemas 传给 DeepSeek，也没有把返回的 tool calls 转成 Responses API function-call items。因此 DeepSeek 会把 DSML/XML 风格的伪工具调用打印成可见 assistant 文本。

## 结果

`/home/loviya/.codex-api-ds/deepseek_responses_proxy.py` 现在会：

- 把 Responses API function tool definitions 转成 DeepSeek Chat Completions `tools`。
- 把 DeepSeek `tool_calls` 转成 Responses API `function_call` output items。
- 把 Responses `function_call_output` items 转回 Chat Completions `tool` messages。
- 追加兼容性指令，禁止可见的 DSML/XML 伪工具标记。
- 作为兜底，从可见文本中剥离 DSML/XML 伪工具调用块。

## 验证

- `python3 -m py_compile /home/loviya/.codex-api-ds/deepseek_responses_proxy.py`
- `curl -fsS http://127.0.0.1:18792/health`
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "只回复 ok"` 显示原生 Codex `exec` 执行，而不是 raw DSML。
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "不要使用工具，只回复 ok"` 在恢复完整 stream content 后返回可见 `ok`。
- `codex-api-ds exec --skip-git-repo-check --sandbox read-only "运行 pwd 并告诉我结果"` 执行了原生 `exec_command`，并在 session 中记录一条 assistant message。

## 注意事项

当 `codex-api-ds exec` 验证需要访问本地代理时，应在 sandbox 外运行。本次会话使用的是 `/home/loviya/.codex-a`，因此在明确记录 runtime-home 不一致后才编辑 `/home/loviya/.codex-api-ds`。Terminal `exec` 输出可能显示两次最终文本，因为它同时包含 streamed text 和 final replay，而 session record 中只有一条 assistant message。

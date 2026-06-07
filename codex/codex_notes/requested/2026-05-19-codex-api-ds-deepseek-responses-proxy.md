---
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - codex-api-ds
  - deepseek
  - responses-api
  - chat-completions
  - local-proxy
created: 2026-05-19
updated: 2026-05-19
source_worklog: 20260519-codex-api-ds-deepseek-proxy-note
related_worklogs:
  - 20260519-codex-api-ds-model-deepseek-v4-pro
  - 20260519-codex-api-ds-v4-thinking-fix
  - 20260519-codex-api-ds-model-metadata
secret_handling: secrets-redacted
---

# codex-api-ds DeepSeek Responses 本地代理链路

## 结论快照

`/home/loviya/.codex-api-ds/config.toml` 里的配置：

```toml
base_url = "http://127.0.0.1:18792/v1"
wire_api = "responses"
```

表示 Codex 不直接请求 DeepSeek 官网，而是把 Responses API 请求发给本机 `127.0.0.1:18792` 上的 Python 代理。

真实链路是：

```text
codex-api-ds
  -> export CODEX_HOME=/home/loviya/.codex-api-ds
  -> 启动 deepseek_responses_proxy.py 监听 127.0.0.1:18792
  -> exec codex -m deepseek-v4-pro

Codex
  -> POST http://127.0.0.1:18792/v1/responses

deepseek_responses_proxy.py
  -> 把 Responses input/tools 转成 Chat Completions messages/tools
  -> 对 deepseek-v4-* 加 thinking: disabled
  -> POST https://api.deepseek.com/chat/completions
  -> 把 choices[0].message 包装回 Responses API 结构

Codex
  <- 读取 Responses 格式结果
```

所以 `127.0.0.1:18792` 是本机兼容层，不是 DeepSeek 本身。它仍然会把请求转发到外网 DeepSeek API。

当前长期运行方式：

```text
tmux session: codex-ds-proxy
process: python3 /home/loviya/.codex-api-ds/deepseek_responses_proxy.py
listen: 127.0.0.1:18792
```

为什么不让 Codex 直接请求 DeepSeek：

- Codex 配置的 wire protocol 是 `responses`，会请求 `/v1/responses`。
- DeepSeek 官方接口是 Chat Completions 风格，实际入口是 `/chat/completions`。
- 本机代理负责协议转换、工具调用转换、API key 注入、错误格式转换，以及 V4 thinking mode 兼容。
- 直接把 `base_url` 指向 `api.deepseek.com` 会让 Codex 发 DeepSeek 不支持的 Responses 请求。

## 相关文件

### `/home/loviya/.codex-api-ds/config.toml`

关键配置：

```toml
model_provider = "deepseek"
model = "deepseek-v4-pro"
model_catalog_json = "/home/loviya/.codex-api-ds/deepseek-models.json"
model_context_window = 1048576
model_reasoning_effort = "medium"

[model_providers.deepseek]
name = "DeepSeek"
base_url = "http://127.0.0.1:18792/v1"
wire_api = "responses"
requires_openai_auth = false
env_key = "DEEPSEEK_API_KEY"
```

字段含义：

- `model_provider = "deepseek"`：默认使用 `[model_providers.deepseek]` 这一组 provider 配置。
- `model = "deepseek-v4-pro"`：Codex 入口默认模型为 DeepSeek V4 Pro。
- `model_catalog_json = "/home/loviya/.codex-api-ds/deepseek-models.json"`：为自定义模型提供完整 Codex model metadata，消除启动时 `Model metadata ... not found` 警告。
- `model_context_window = 1048576`：为 Codex 显式提供未知模型的上下文窗口，降低 fallback metadata 的影响。
- `base_url = "http://127.0.0.1:18792/v1"`：Codex 请求本机 18792 端口。
- `wire_api = "responses"`：Codex 按 Responses API 协议发送请求，因此实际入口通常是 `/v1/responses`。
- `requires_openai_auth = false`：不使用 OpenAI/ChatGPT 登录认证。
- `env_key = "DEEPSEEK_API_KEY"`：provider 密钥来自环境变量名，不要把实际值写入 notes 或 worklog。

注意：启动脚本最后执行 `codex -m deepseek-v4-pro "$@"`，所以运行时模型名会被命令行参数明确指定为 `deepseek-v4-pro`。

### `/home/loviya/.codex-api-ds/codex-api-ds`

这是 DeepSeek 专用 Codex 启动入口。

关键行为：

```bash
source /home/loviya/.codex-api-ds/deepseek.env
export CODEX_HOME=/home/loviya/.codex-api-ds
```

然后检查本机代理是否已启动：

```bash
curl -fsS http://127.0.0.1:18792/health
```

如果未启动，则启动：

```bash
DEEPSEEK_PROXY_PORT=18792 \
python3 /home/loviya/.codex-api-ds/deepseek_responses_proxy.py
```

最后进入 Codex：

```bash
exec codex -m deepseek-v4-pro "$@"
```

### `/home/loviya/.codex-api-ds/deepseek_responses_proxy.py`

这是实际协议适配器。

它写死的 DeepSeek 后端是：

```python
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
```

监听地址来自环境变量：

```python
host = os.environ.get("DEEPSEEK_PROXY_HOST", "127.0.0.1")
port = int(os.environ.get("DEEPSEEK_PROXY_PORT", "18791"))
```

由于启动脚本传入 `DEEPSEEK_PROXY_PORT=18792`，所以实际监听 `127.0.0.1:18792`。

当前也可以用 tmux 长期保活代理：

```bash
tmux new-session -d -s codex-ds-proxy 'source /home/loviya/.codex-api-ds/deepseek.env; export DEEPSEEK_PROXY_PORT=18792; python3 /home/loviya/.codex-api-ds/deepseek_responses_proxy.py >>/home/loviya/.codex-api-ds/log/deepseek_responses_proxy.log 2>&1'
```

代理只接受：

```text
POST /responses
POST /v1/responses
```

其他 POST 路径会返回 `404`。因此它不是通用 OpenAI-compatible Chat Completions 服务。

### `/home/loviya/.codex-api-ds/deepseek-models.json`

这是本地 Codex model catalog，用来让 Codex 认识 `deepseek-v4-pro` 这个非 OpenAI 官方 catalog 里的模型。

关键内容：

```json
{
  "slug": "deepseek-v4-pro",
  "display_name": "DeepSeek V4 Pro",
  "context_window": 1048576,
  "max_context_window": 1048576,
  "supports_parallel_tool_calls": true,
  "supports_reasoning_summaries": false
}
```

没有这个 catalog 时，即使 `model_context_window` 已设置，Codex 启动仍会提示：

```text
Model metadata for `deepseek-v4-pro` not found. Defaulting to fallback metadata
```

原因是 `model_context_window` 只是单项覆盖，不能替代完整模型 metadata。

## 协议转换

请求方向，Responses -> Chat Completions：

- `_input_to_messages(payload)`：把 Responses 的 `instructions`、`input`、`function_call_output` 等转为 Chat Completions 的 `messages`。
- `_responses_tools_to_chat_tools(payload)`：把 Responses function tools 转为 Chat Completions `tools`。
- `max_output_tokens` 转为 `max_tokens`。
- `temperature` 原样透传。
- `model` 使用 Codex 传入值；当前入口传入 `deepseek-v4-pro`。
- 对 `deepseek-v4-*` 请求加 `thinking: {"type": "disabled"}`。

发送给 DeepSeek 的核心结构类似：

```json
{
  "model": "deepseek-v4-pro",
  "messages": [],
  "stream": false,
  "thinking": {"type": "disabled"},
  "tools": [],
  "tool_choice": "auto"
}
```

`thinking: disabled` 的原因：

- `deepseek-v4-pro` 支持 thinking mode，且默认可能进入 thinking。
- DeepSeek 在 thinking mode 下发生工具调用后，后续请求必须回传 `reasoning_content`。
- 当前 Codex Responses 代理没有保存并回放 DeepSeek 的 `reasoning_content`。
- 显式禁用 thinking 可以让工具调用链路稳定运行，避免 `The reasoning_content in the thinking mode must be passed back to the API`。

响应方向，Chat Completions -> Responses：

- 读取 DeepSeek 返回的 `choices[0].message.content`。
- 读取 DeepSeek 返回的 `choices[0].message.tool_calls`。
- `_response_payload(...)` 把结果包装成 Codex 期待的 Responses API 结构：

```json
{
  "object": "response",
  "status": "completed",
  "output": [],
  "output_text": ""
}
```

如果 Codex 请求流式输出，代理会返回 SSE 事件，但 DeepSeek 请求端固定为：

```python
"stream": False
```

也就是说，它是先完整拿到 DeepSeek 返回，再伪装成 Responses SSE 事件发给 Codex，不是真正逐 token 转发。

## 验证命令

检查代理健康：

```bash
curl -fsS http://127.0.0.1:18792/health
```

期望：

```json
{"ok": true}
```

检查监听端口：

```bash
ss -ltnp | rg '18792'
```

检查 tmux 保活会话：

```bash
tmux list-sessions | rg 'codex-ds-proxy'
```

检查 model catalog JSON：

```bash
python3 -m json.tool /home/loviya/.codex-api-ds/deepseek-models.json
```

验证启动不再出现 metadata 警告：

```bash
/home/loviya/.codex-api-ds/codex-api-ds exec --skip-git-repo-check --sandbox read-only "只回复 ok"
```

期望启动头部显示：

```text
model: deepseek-v4-pro
provider: deepseek
```

且不再出现：

```text
Model metadata for `deepseek-v4-pro` not found
```

观察代理日志：

```bash
tail -n 40 /home/loviya/.codex-api-ds/log/deepseek_responses_proxy.log
```

日志中常见成功请求：

```text
"POST /v1/responses HTTP/1.1" 200 -
```

常见失败含义：

- `400`：请求体或协议字段不符合代理当前处理逻辑。
- `401`：代理进程环境里没有 `DEEPSEEK_API_KEY`。
- `404`：请求路径不是 `/responses` 或 `/v1/responses`。
- `502`：代理向 DeepSeek 后端请求失败，可能是网络、DNS、上游错误或连接超时。

验证 V4 Pro 工具调用兼容：

```bash
curl -fsS -X POST http://127.0.0.1:18792/v1/responses \
  -H 'Content-Type: application/json' \
  -d '{"model":"deepseek-v4-pro","input":[{"type":"function_call","call_id":"call_test_1","name":"noop","arguments":"{}"},{"type":"function_call_output","call_id":"call_test_1","output":"ok"},{"role":"user","content":"Reply with ok only."}],"tools":[{"type":"function","name":"noop","description":"No-op test tool","parameters":{"type":"object","properties":{}}}],"max_output_tokens":16}'
```

期望返回 `200`，且 `output_text` 类似：

```json
"ok"
```

## 安全注意

- `127.0.0.1` 只说明 Codex 第一跳打到本机，不表示离线。
- 代理会继续请求 `https://api.deepseek.com/chat/completions`。
- `deepseek.env`、环境变量、Authorization header 和完整请求/响应正文都不应写入 notes、worklog、聊天或截图。
- 代理日志目前主要记录请求路径和状态码，但调试时仍应避免输出完整 payload。

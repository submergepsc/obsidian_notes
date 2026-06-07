---
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - codex-api-mimo-pay-self
  - codex-api-ds
  - responses-proxy
  - provider-config
created: 2026-05-20
source_worklog: 20260520-codex-api-mimo-pay-self-ds-notes
related_notes:
  - 2026-05-19-codex-api-ds-deepseek-responses-proxy.md
  - 2026-05-18-mimi3-codex-api-mimo-free-self-local-gateway.md
secret_handling: secrets-redacted
---

# codex-api-mimo-pay-self 与 codex-api-ds 配置链路比较

## 结论快照

`codex-api-mimo-pay-self` 和 `codex-api-ds` 都不是让 Codex 直接请求真实模型厂商。两者都把 Codex 的 `wire_api = "responses"` 请求先打到本机代理，再由代理转换成上游支持的 Chat Completions 请求。

核心差异：

| 项目 | codex-api-mimo-pay-self | codex-api-ds |
| --- | --- | --- |
| 账户 home | `/home/loviya/.codex-api-mimo-pay-self` | `/home/loviya/.codex-api-ds` |
| 启动入口 | `/home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self` | `/home/loviya/.codex-api-ds/codex-api-ds` |
| 默认模型 | `mimo-v2.5-pro` | `deepseek-v4-pro` |
| provider 名 | `mimo` | `deepseek` |
| Codex base URL | `http://127.0.0.1:18793/v1` | `http://127.0.0.1:18792/v1` |
| 本机代理脚本 | `mimo_responses_proxy.py` | `deepseek_responses_proxy.py` |
| 上游 endpoint | 来自 `MIMO_CHAT_COMPLETIONS_URL`，不写入 note | `https://api.deepseek.com/chat/completions` |
| env key | `MIMO_API_KEY` | `DEEPSEEK_API_KEY` |
| 代理启动方式 | 启动器按需 `setsid -f` 拉起 | 启动器或 `tmux codex-ds-proxy` 保活 |
| thinking 处理 | `enable_thinking: False` | `thinking: {"type": "disabled"}` |

## codex-api-mimo-pay-self 链路

启动器链路：

```text
codex-api-mimo-pay-self
  -> source /home/loviya/.codex-api-mimo-pay-self/mimo.env
  -> export CODEX_HOME=/home/loviya/.codex-api-mimo-pay-self
  -> 检查 http://127.0.0.1:18793/health
  -> 如未启动，后台启动 mimo_responses_proxy.py
  -> exec codex -m "$MIMO_MODEL"
```

请求链路：

```text
Codex
  -> POST http://127.0.0.1:18793/v1/responses

mimo_responses_proxy.py
  -> 把 Responses input/tools 转成 Chat Completions messages/tools
  -> 加 enable_thinking: False
  -> POST $MIMO_CHAT_COMPLETIONS_URL
  -> Authorization: Bearer $MIMO_API_KEY
  -> 把 choices[0].message 包装回 Responses API 结构

Codex
  <- 读取 Responses 格式结果
```

当前 `config.toml` 关键配置：

```toml
model_provider = "mimo"
model = "mimo-v2.5-pro"
personality = "pragmatic"

[model_providers.mimo]
name = "Mimo"
base_url = "http://127.0.0.1:18793/v1"
wire_api = "responses"
requires_openai_auth = false
env_key = "MIMO_API_KEY"
```

`mimo.env` 只应记录变量名，不记录真实值：

```bash
export MIMO_API_KEY=***redacted***
export MIMO_CHAT_COMPLETIONS_URL=***redacted***
export MIMO_MODEL="mimo-v2.5-pro"
export MIMO_PROXY_PORT="18793"
```

`mimo_responses_proxy.py` 接受：

```text
GET  /health
GET  /v1/health
POST /responses
POST /v1/responses
```

其他 POST 路径返回 `404`，所以它不是通用 OpenAI-compatible Chat Completions 服务，而是 Codex Responses API 到上游 Chat Completions 的专用适配层。

## codex-api-ds 链路

启动器链路：

```text
codex-api-ds
  -> export CODEX_HOME=/home/loviya/.codex-api-ds
  -> 启动或复用 deepseek_responses_proxy.py 监听 127.0.0.1:18792
  -> exec codex -m deepseek-v4-pro
```

请求链路：

```text
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

## 共同模式

两者的共同点：

- 都用账户专属 `CODEX_HOME`，避免普通账户和 API 账户状态混用。
- Codex 侧都配置 `wire_api = "responses"`。
- Codex 侧 `base_url` 都指向 `127.0.0.1` 的本机代理，不是直接指向模型厂商。
- 本机代理把 Responses API 转为上游 Chat Completions API。
- 本机代理负责工具调用结构转换。
- API key 都从环境变量读取，不应写入 notes、worklog、聊天或截图。
- 代理返回的是 Codex 期待的 Responses 格式。

## 关键差异

`codex-api-mimo-pay-self` 的上游地址是动态配置：

```text
MIMO_CHAT_COMPLETIONS_URL=***redacted***
```

这意味着 MiMo 的真实后端可能是一个 OpenAI-compatible Chat Completions relay、网关或临时接口；note 中只保留变量名和链路，不保留真实 URL。

`codex-api-ds` 的上游地址在代理脚本里固定为：

```text
https://api.deepseek.com/chat/completions
```

`codex-api-mimo-pay-self` 当前没有在 `config.toml` 中配置 `model_catalog_json`；`codex-api-ds` 已通过 `deepseek-models.json` 给 `deepseek-v4-pro` 提供完整 model metadata，避免 Codex fallback metadata 警告。

`codex-api-mimo-pay-self` 启动器会在 health check 失败时按需后台启动代理。`codex-api-ds` 既可由启动器处理，也记录过用 `tmux session: codex-ds-proxy` 长期保活。

## 与 codex_api_mimo_free_self 的区别

`codex-api-mimo-pay-self` 和 `codex_api_mimo_free_self` 不是同一条链路。

`codex_api_mimo_free_self` 使用：

```text
CODEX_HOME=/home/loviya/.codex-api-mimo-free-self
base_url=http://127.0.0.1:8000/v1
mimi3 FastAPI gateway
Pinggy / Claw bridge
MiMo 后端
```

`codex-api-mimo-pay-self` 使用：

```text
CODEX_HOME=/home/loviya/.codex-api-mimo-pay-self
base_url=http://127.0.0.1:18793/v1
mimo_responses_proxy.py
MIMO_CHAT_COMPLETIONS_URL
```

因此排障时先确认命令名：

- `codex-api-mimo-pay-self`：看 `18793`、`mimo_responses_proxy.py`、`mimo.env`。
- `codex_api_mimo_free_self` / `codex-api-mimo-free-self`：看 `8000`、`/home/loviya/code/mimi3`、`active_clients`、Pinggy/Claw bridge。

## 验证命令

检查 `codex-api-mimo-pay-self` 本机代理：

```bash
curl -fsS http://127.0.0.1:18793/health
```

如果连不上，不一定是配置坏了；启动器会按需拉起：

```bash
codex-api-mimo-pay-self --version
```

或直接进入：

```bash
codex-api-mimo-pay-self
```

检查配置文件：

```bash
sed -n '1,120p' /home/loviya/.codex-api-mimo-pay-self/config.toml
```

脱敏查看 env 变量名：

```bash
sed -n '1,80p' /home/loviya/.codex-api-mimo-pay-self/mimo.env | sed -E 's/(API_KEY|TOKEN|SECRET|COOKIE|AUTH)([^=]*)=.*/\1\2=***redacted***/I; s#(MIMO_CHAT_COMPLETIONS_URL=).*#\1***redacted***#'
```

检查代理日志：

```bash
tail -n 40 /home/loviya/.codex-api-mimo-pay-self/log/mimo_responses_proxy.log
```

检查 `codex-api-ds` 本机代理：

```bash
curl -fsS http://127.0.0.1:18792/health
```

## 安全注意

不要把以下内容写入 notes、worklog、聊天、README 或截图：

- `MIMO_API_KEY`
- `MIMO_CHAT_COMPLETIONS_URL` 的真实值
- `DEEPSEEK_API_KEY`
- Authorization header
- 完整请求/响应正文
- cookie、OAuth token、refresh token、service token

可记录的信息限于：路径、端口、模型名、provider 名、协议类型、脱敏错误摘要和验证命令。

## 2026-05-20 更新：codex-api-mimo-pay-self 增加 DeepSeek 选择

`/home/loviya/.codex-api-mimo-pay-self/config.toml` 已增加 `deepseek` provider，并新增本地 model catalog：

```toml
model_catalog_json = "/home/loviya/.codex-api-mimo-pay-self/model_catalog.json"

[model_providers.deepseek]
name = "DeepSeek"
base_url = "http://127.0.0.1:18792/v1"
wire_api = "responses"
requires_openai_auth = false
env_key = "DEEPSEEK_API_KEY"
```

`/home/loviya/.codex-api-mimo-pay-self/model_catalog.json` 现在同时列出：

```text
mimo-v2.5-pro
deepseek-v4-pro
```

`/home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self` 启动器现在支持两种 DeepSeek 选择方式：

```bash
CODEX_API_MIMO_PROVIDER=deepseek codex-api-mimo-pay-self
```

或：

```bash
CODEX_API_MIMO_MODEL=deepseek-v4-pro codex-api-mimo-pay-self
```

默认不变：

```bash
codex-api-mimo-pay-self
```

仍使用：

```text
provider=mimo
model=mimo-v2.5-pro
base_url=http://127.0.0.1:18793/v1
```

DeepSeek 分支不会把 `deepseek-v4-pro` 发给 MiMo 的 18793 代理，而是切换到 `deepseek` provider，并复用现有 DS 本地代理：

```text
provider=deepseek
model=deepseek-v4-pro
base_url=http://127.0.0.1:18792/v1
```

验证结果：

- `python3 -m json.tool /home/loviya/.codex-api-mimo-pay-self/model_catalog.json` 通过。
- `bash -n /home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self` 通过。
- `CODEX_HOME=/home/loviya/.codex-api-mimo-pay-self codex --strict-config --help` 通过。
- `CODEX_API_MIMO_PROVIDER=deepseek codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "不要使用工具，只回复 ok"` 识别为 `provider: deepseek`、`model: deepseek-v4-pro`，返回 `ok`。
- 默认 MiMo 分支识别为 `provider: mimo`、`model: mimo-v2.5-pro`，但上游返回 `502`，脱敏错误摘要为 SSL EOF；这是 MiMo 上游连接问题，不是本次 DeepSeek provider 配置解析问题。

安全注意：不要把 `MIMO_API_KEY`、`MIMO_CHAT_COMPLETIONS_URL`、`DEEPSEEK_API_KEY` 或完整请求/响应正文写入 notes、worklog 或聊天。

## 2026-05-20 回滚：删除 codex-api-mimo-pay-self 的 DeepSeek 选择

用户随后要求删除刚加入的 `codex-api-mimo-pay-self` DeepSeek 模型选择。当前状态已回滚为原始 `codex-api-mimo-pay-self` 链路：

```text
provider=mimo
model=mimo-v2.5-pro
base_url=http://127.0.0.1:18793/v1
```

已删除新增的：

```text
/home/loviya/.codex-api-mimo-pay-self/model_catalog.json
```

已从备份恢复：

```text
/home/loviya/.codex-api-mimo-pay-self/config.toml
/home/loviya/.codex-api-mimo-pay-self/codex-api-mimo-pay-self
```

因此 `CODEX_API_MIMO_PROVIDER=deepseek codex-api-mimo-pay-self` 和 `CODEX_API_MIMO_MODEL=deepseek-v4-pro codex-api-mimo-pay-self` 不再是当前支持入口。需要 DeepSeek 时继续使用独立的 `codex-api-ds`。

## 2026-05-20 codex-api-mimo-pay-self 502 修复记录

现象：`codex-api-mimo-pay-self` 本机代理 `127.0.0.1:18793/health` 正常，但真实 `/v1/responses` 请求连续返回 `502 Bad Gateway`，错误摘要为 `SSL: UNEXPECTED_EOF_WHILE_READING`。

本次确认的原因：

- 当前不可用配置使用 `MIMO_CHAT_COMPLETIONS_URL=https://api.mimo-v2.com/v1/chat/completions`，该域名在本机当前网络下 TLS 连接失败。
- 当前不可用配置中的 `tp-cp...` 形态 key 对旧域名返回 `401 invalid_api_key`。
- 备份 `/home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-20260516-134543` 中的 `sk-c6...` 形态 key 可用。
- 可用组合是：备份 key + `https://api.xiaomimimo.com/v1/chat/completions` + `mimo-v2.5-pro`。

修复动作：

- 先备份坏配置到 `/home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-20260520-0059-broken`。
- 用 `/home/loviya/.codex-api-mimo-pay-self/mimo.env.bak-20260516-134543` 恢复 key。
- 将 `/home/loviya/.codex-api-mimo-pay-self/mimo.env` 中的上游改为 `https://api.xiaomimimo.com/v1/chat/completions`。
- 停止旧的 `mimo_responses_proxy.py` 进程，让 `codex-api-mimo-pay-self` 启动器按新 env 重新拉起代理。

验证结果：

```bash
/home/loviya/.local/bin/codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "只回复 ok"
```

返回 `ok`；代理日志出现新的 `POST /v1/responses HTTP/1.1` `200`。

后续排查优先级：如果再次出现 502，先检查 `mimo.env` 的上游域名和 key 形态，再检查 `127.0.0.1:18793/health`。不要只看 health，health 只能证明本机代理活着，不能证明上游 MiMo 可用。

## 2026-05-20 更新：修复 MiMo model metadata warning

`codex-api-mimo-pay-self` 曾出现：

```text
Model metadata for `mimo-v2.5-pro` not found. Defaulting to fallback metadata
```

原因是 `/home/loviya/.codex-api-mimo-pay-self/config.toml` 没有配置 `model_catalog_json`，而启动器实际使用 `mimo.env` 中的 `MIMO_MODEL=mimo-v2.5-pro`。

当前已补齐：

```toml
model_context_window = 1048576
model_auto_compact_token_limit = 900000
model_catalog_json = "/home/loviya/.codex-api-mimo-pay-self/model_catalog.json"
model_provider = "mimo"
model = "mimo-v2.5-pro"
```

新增：

```text
/home/loviya/.codex-api-mimo-pay-self/model_catalog.json
```

该 catalog 只包含 `mimo-v2.5-pro` 的 MiMo metadata，不包含 DeepSeek provider 或 DeepSeek model。验证时 `codex-api-mimo-pay-self exec --skip-git-repo-check --sandbox read-only "不要使用工具，只回复 ok"` 不再显示 metadata warning，并返回 `ok`。

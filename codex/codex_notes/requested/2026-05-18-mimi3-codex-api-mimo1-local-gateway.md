---
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - mimi3
  - mimo2api
  - codex-api-mimo-free-self
  - local-gateway
  - pinggy
  - openai-compatible
created: 2026-05-18
source_worklog: 20260517-mimi3-service-start
secret_handling: secrets-redacted
---

# mimi3 本地网关与 codex_api_mimo_free_self 配置说明

## 结论快照

当前目标是把 `/home/loviya/code/mimi3` 作为本机 OpenAI-compatible 网关使用，并让 `codex_api_mimo_free_self` 通过这个本机网关访问 MiMo/Claw 节点。

核心链路：

```text
Codex / OpenAI-compatible client
  -> http://127.0.0.1:8000/v1
  -> mimi3 FastAPI gateway
  -> /ws WebSocket
  -> Pinggy 公网反向隧道
  -> 云端 Claw bridge
  -> MiMo 后端
```

记录时的关键状态：

- 项目目录：`/home/loviya/code/mimi3`
- 本机 API Base URL：`http://127.0.0.1:8000/v1`
- 本机 WebUI：`http://127.0.0.1:8000/webui`
- 本机状态接口：`http://127.0.0.1:8000/api/system/status`
- 当前公网回连地址：`https://ugwzo-104-234-0-177.run.pinggy-free.link`
- 当前 WebSocket 回连地址：`wss://ugwzo-104-234-0-177.run.pinggy-free.link/ws`
- `codex_api_mimo_free_self` 独立 home：`/home/loviya/.codex-api-mimo-free-self`
- `codex_api_mimo_free_self` 命令入口：`/home/loviya/.local/bin/codex_api_mimo_free_self`
- 兼容别名：`/home/loviya/.local/bin/codex-api-mimo-free-self`

注意：`pinggy-free` 是临时隧道，通常约 60 分钟有效。到期后需要重新开隧道、更新 `.env` 的 `WS_TUNNEL_URL` 并重启 `mimi3`。

## 敏感信息规则

不要把以下内容写入 notes、worklog、聊天、README 或截图：

- 小米账号 cookie
- `serviceToken`
- `xiaomichatbot_ph`
- API key / bearer token
- OAuth code / refresh token
- 完整请求头或完整 cookie 字符串

本 note 只记录结构、路径、命令和脱敏说明，不记录实际凭证。

## 文件与配置

### mimi3 项目文件

项目目录：

```bash
/home/loviya/code/mimi3
```

新增/关键文件：

```text
requirements.txt
.env
main.py
mimo2api/web_service.py
mimo2api/manager.py
mimo2api/bridge.py
users/user_*.json        # 含账号凭证，勿提交、勿外传
gateway_metrics.db       # 运行态 DB，已忽略
mimo2api.lock            # 运行锁，已忽略
logs/gateway.log         # 运行日志，可能包含状态信息，注意不要公开贴出敏感片段
```

`requirements.txt` 当前依赖：

```text
fastapi
uvicorn[standard]
python-dotenv
httpx
websockets
pydantic
```

`.gitignore` 已补充运行态忽略：

```text
gateway_metrics.db
mimo2api.lock
```

### `.env`

当前关键配置：

```env
WS_TUNNEL_URL=wss://ugwzo-104-234-0-177.run.pinggy-free.link/ws
```

未启用鉴权时，客户端 `api_key` 可以随便填。若以后启用：

```env
MIMO_RELAY_OPENAI_KEY=...
```

则 OpenAI-compatible 客户端必须使用对应 key。

### codex_api_mimo_free_self home

独立 home：

```bash
/home/loviya/.codex-api-mimo-free-self
```

配置文件：

```toml
model_provider = "mimo1"
model = "mimo-v2.5-pro"
personality = "pragmatic"

[model_providers.mimo1]
name = "mimo1"
base_url = "http://127.0.0.1:8000/v1"
wire_api = "responses"
requires_openai_auth = false
env_key = "MIMO1_API_KEY"

[projects."/home/loviya"]
trust_level = "trusted"

[projects."/home/loviya/code/mimi3"]
trust_level = "trusted"
```

启动器：

```bash
/home/loviya/.codex-api-mimo-free-self/codex-api-mimo-free-self
```

命令入口：

```bash
/home/loviya/.local/bin/codex_api_mimo_free_self
/home/loviya/.local/bin/codex-api-mimo-free-self
```

启动器行为：

- 设置 `CODEX_HOME=/home/loviya/.codex-api-mimo-free-self`
- 默认 `MIMO1_BASE_URL=http://127.0.0.1:8000`
- 默认 `MIMO1_MODEL=mimo-v2.5-pro`
- 启动前检查 `http://127.0.0.1:8000/api/system/status`
- 如果 `active_clients=0`，会警告但仍允许继续启动 Codex
- 最后执行 `codex -m "$MIMO1_MODEL" "$@"`

## 启动顺序

### 1. 进入项目目录

```bash
cd /home/loviya/code/mimi3
```

### 2. 确认虚拟环境存在

如果 `.venv` 不存在，创建并安装依赖：

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

不要用系统级：

```bash
pip install -r requirements.txt
```

原因：系统 Python 是 PEP 668 externally managed environment，系统级 pip 会被拒绝；项目应使用 `.venv`。

### 3. 启动公网回连隧道

当前使用 Pinggy 免费 SSH 反向隧道：

```bash
ssh -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/tmp/pinggy_known_hosts \
  -p 443 \
  -R0:127.0.0.1:8000 \
  a.pinggy.io
```

启动后输出类似：

```text
https://xxxx.run.pinggy-free.link
```

把这个 HTTPS 地址转换成 WebSocket 地址写进 `.env`：

```env
WS_TUNNEL_URL=wss://xxxx.run.pinggy-free.link/ws
```

记录时的地址是：

```env
WS_TUNNEL_URL=wss://ugwzo-104-234-0-177.run.pinggy-free.link/ws
```

这个地址会过期，不能长期依赖。

### 4. 用干净代理环境启动 mimi3

必须清理代理环境变量，避免 `httpx` 读取到 `socks://127.0.0.1:7897/` 后报错：

```text
Unknown scheme for proxy URL URL('socks://127.0.0.1:7897/')
```

启动命令：

```bash
cd /home/loviya/code/mimi3
env -u ALL_PROXY -u all_proxy \
    -u HTTP_PROXY -u http_proxy \
    -u HTTPS_PROXY -u https_proxy \
    -u NO_PROXY -u no_proxy \
    .venv/bin/python main.py
```

服务启动后监听：

```text
http://0.0.0.0:8000
```

本机访问使用：

```text
http://127.0.0.1:8000
```

### 5. 等待 Claw 节点接入

看日志：

```bash
tail -f logs/gateway.log
```

成功时会看到类似：

```text
共通过 users/ 扫描并成功重载入 1 个授权用户预设账号。
探测现有云端实例状态: AVAILABLE
已成功通过 websocket 建联!
✅ 内网节点已接入: ... 当前在线节点数: 1
注入已完成落地！
```

状态接口应返回：

```bash
curl http://127.0.0.1:8000/api/system/status
```

期望：

```json
{"active_clients":1}
```

如果是：

```json
{"active_clients":0}
```

说明本机网关活着，但云端 bridge 没连回来。

## 小米账号凭证导入

WebUI 地址：

```text
http://127.0.0.1:8000/webui
```

导入凭证需要浏览器 cookie 中至少三个字段：

```text
userId
serviceToken
xiaomichatbot_ph
```

导入格式：

```text
userId=你的数字ID; serviceToken="你的serviceToken"; xiaomichatbot_ph="你的xiaomichatbot_ph"
```

`cUserId` 和 `ulocale` 不需要。

如果导入后显示：

```text
ERROR / 已过期/无环境
```

不要立刻判定身份错误。常见原因：

- 服务启动时 `users/` 为空，Manager 已退出；导入后需要重启服务让 Manager 重新扫描。
- 启动服务时继承了不兼容代理环境，导致 `httpx` 初始化失败。
- 公网 `WS_TUNNEL_URL` 是默认 `your-domain.com` 或已过期隧道，云端 bridge 无法连回本机。

如果凭证完全无效，通常会更早出现 401 或创建失败；如果日志能到 `AVAILABLE`，说明身份大概率已经过了基础校验。

## API 使用方式

### 关键区别：Base URL 不是浏览器页面

`http://localhost:8000/v1` 是 OpenAI-compatible Base URL，不是浏览器页面。

直接在浏览器打开：

```text
http://localhost:8000/v1
```

可能出现 `404 Not 已找到`，这是正常的。

浏览器或 curl 测试请用具体接口：

```text
http://127.0.0.1:8000/v1/models
http://127.0.0.1:8000/webui
http://127.0.0.1:8000/api/system/status
```

### 查看模型

```bash
curl http://127.0.0.1:8000/v1/models
```

常用模型：

```text
mimo-v2.5-pro
mimo-v2.5
mimo-v2-flash
```

### Chat Completions 示例

```bash
curl http://127.0.0.1:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "mimo-v2.5-pro",
    "messages": [
      {"role": "user", "content": "你好"}
    ]
  }'
```

`/v1/chat/completions` 必须 `POST`，不能只在浏览器地址栏打开。

### Python OpenAI SDK 示例

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8000/v1",
    api_key="anything",
)

resp = client.chat.completions.create(
    model="mimo-v2.5-pro",
    messages=[{"role": "user", "content": "写一个 Python 快排"}],
)

print(resp.choices[0].message.content)
```

如果 `.env` 启用了 `MIMO_RELAY_OPENAI_KEY`，`api_key` 必须填对应值；当前未启用时可以填任意字符串。

### 其他软件配置

OpenAI-compatible 客户端中配置：

```text
Base URL: http://127.0.0.1:8000/v1
API Key: 任意值，除非启用了 MIMO_RELAY_OPENAI_KEY
Model: mimo-v2.5-pro
```

如果软件要求完整 endpoint，而不是 Base URL，则使用：

```text
http://127.0.0.1:8000/v1/chat/completions
```

## codex_api_mimo_free_self 使用方式

直接运行：

```bash
codex_api_mimo_free_self
```

或兼容命令：

```bash
codex-api-mimo-free-self
```

它使用：

```text
CODEX_HOME=/home/loviya/.codex-api-mimo-free-self
base_url=http://127.0.0.1:8000/v1
wire_api=responses
model=mimo-v2.5-pro
env_key=MIMO1_API_KEY
```

可以临时覆盖模型：

```bash
MIMO1_MODEL=mimo-v2.5 codex_api_mimo_free_self
```

可以临时覆盖本机网关地址：

```bash
MIMO1_BASE_URL=http://127.0.0.1:8000 codex_api_mimo_free_self
```

如果本机服务没起来，启动器会报：

```text
codex-api-mimo-free-self: 本地 mimi3 网关没有响应。
先启动 /home/loviya/code/mimi3/main.py，并确保公网回连隧道和 Claw 节点在线。
```

如果服务起来但没有节点，会报 warning：

```text
mimi3 当前没有在线 Claw 节点
```

这种情况下 Codex 可能能启动，但请求会因为没有后端节点而失败。

## 常见故障与处理

### 1. `http://localhost:8000/v1` 浏览器打不开

这是正常的。`/v1` 是 Base URL，不是页面。

正确测试：

```bash
curl http://127.0.0.1:8000/v1/models
curl http://127.0.0.1:8000/api/system/status
```

WebUI：

```text
http://127.0.0.1:8000/webui
```

### 2. `curl http://127.0.0.1:8000/api/system/status` 连不上

说明本机 `mimi3` 没监听 8000，或进程在不可访问的 sandbox 网络里。

处理：

```bash
cd /home/loviya/code/mimi3
env -u ALL_PROXY -u all_proxy \
    -u HTTP_PROXY -u http_proxy \
    -u HTTPS_PROXY -u https_proxy \
    -u NO_PROXY -u no_proxy \
    .venv/bin/python main.py
```

如果是在 Codex 工具里启动，为了让浏览器也能访问，需要在 sandbox 外启动。

### 3. `active_clients=0`

服务在线，但 Claw bridge 没连回来。

检查顺序：

1. `.env` 的 `WS_TUNNEL_URL` 是否是当前有效隧道地址。
2. 隧道进程是否还在。
3. 隧道 HTTPS 是否能访问 `/api/system/status`。
4. `logs/gateway.log` 是否有 `✅ 内网节点已接入`。
5. 账号是否 `AVAILABLE`。
6. 是否刚重启服务但还没等 bridge 重新注入。

### 4. Pinggy 隧道过期

免费隧道约 60 分钟。过期后重新执行：

```bash
ssh -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/tmp/pinggy_known_hosts \
  -p 443 \
  -R0:127.0.0.1:8000 \
  a.pinggy.io
```

拿到新地址后改 `.env`：

```env
WS_TUNNEL_URL=wss://新的域名/ws
```

然后重启 `mimi3`。

### 5. `httpx` 代理错误

错误形态：

```text
Unknown scheme for proxy URL URL('socks://127.0.0.1:7897/')
```

原因：服务启动进程继承了 `ALL_PROXY=socks://127.0.0.1:7897/` 等环境变量，`httpx` 不接受这个 scheme。

处理：启动 `main.py` 时 unset 代理变量：

```bash
env -u ALL_PROXY -u all_proxy \
    -u HTTP_PROXY -u http_proxy \
    -u HTTPS_PROXY -u https_proxy \
    -u NO_PROXY -u no_proxy \
    .venv/bin/python main.py
```

不需要关闭系统全局代理；只要让这个服务进程不继承代理即可。

### 6. `python main.py` 找不到 python

系统里可能只有 `python3`，没有 `python`。

使用：

```bash
.venv/bin/python main.py
```

或：

```bash
python3 main.py
```

项目运行推荐 `.venv/bin/python`。

### 7. `pip install -r requirements.txt` 被拒绝

错误形态：

```text
externally-managed-environment
```

处理：用项目虚拟环境：

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 8. localtunnel / cloudflared 经验

本轮尝试过：

- `cloudflared quick tunnel`：能申请域名，但当前网络下 QUIC 超时或 HTTP2 TLS EOF。
- `localtunnel`：能拿到 `*.loca.lt` 地址，但很快返回 503，不稳定。
- `pinggy.io`：本轮最稳定，成功让 Claw bridge 连回 `/ws`。

因此当前优先使用 Pinggy。

## 停止与重启

停止本机网关：

```bash
pkill -TERM -f '.venv/bin/python main.py'
```

停止 Pinggy 隧道：

```bash
pkill -TERM -f 'a.pinggy.io'
```

重启完整流程：

```bash
cd /home/loviya/code/mimi3

# 1. 开隧道，拿到新的 https://xxxx.run.pinggy-free.link
ssh -o StrictHostKeyChecking=no \
  -o UserKnownHostsFile=/tmp/pinggy_known_hosts \
  -p 443 \
  -R0:127.0.0.1:8000 \
  a.pinggy.io

# 2. 修改 .env
# WS_TUNNEL_URL=wss://xxxx.run.pinggy-free.link/ws

# 3. 启动网关
env -u ALL_PROXY -u all_proxy \
    -u HTTP_PROXY -u http_proxy \
    -u HTTPS_PROXY -u https_proxy \
    -u NO_PROXY -u no_proxy \
    .venv/bin/python main.py

# 4. 检查
curl http://127.0.0.1:8000/api/system/status
```

## 当前遗留注意事项

- `pinggy-free` 地址是临时地址，过期后必须更新 `.env`。
- `users/user_*.json` 含敏感账号凭证，只能留在本机，不要提交。
- 如果在 Codex sandbox 内启动服务，浏览器可能访问不到；应在 sandbox 外启动。
- `codex_api_mimo_free_self` 已经可以使用，但它依赖本机 `mimi3` 服务和至少一个在线 Claw 节点。
- 浏览器访问 `/v1` 不代表服务坏了；应访问 `/v1/models` 或 `/webui`。

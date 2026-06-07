---
id: 20260515-sub2api-project-lookup
name: Sub2API Project Lookup
slug: sub2api-project-lookup
cwd: /home/loviya
summary: "找到本地 Sub2API 项目 `/home/loviya/sub2api`，确认 Docker Compose 部署仍在运行，并定位旧账号/API 不可用原因。"
tags:
  - sub2api
  - docker
  - project-lookup
priority: normal
---

# Sub2API 项目 查找

## 当前快照

- 状态: 待继续
- 目标: 继续调试本地 `sub2api` 的账号授权与 API 调用状态。
- 阻塞: OpenAI 账号授权需要用户在浏览器完成 OAuth 后把 callback URL 或 code 填回页面；Gemini key 调用仍需要先给用户余额或 API key quota 充值。
- 下一步: 用户完成 OpenAI OAuth 后，确认新账号写入 `accounts` 表；若要测 Gemini key，先把用户余额或 key quota 从 0 调高再重测。
- 更新时间: 2026-05-15 20:33:21 +0800

## 关键结果

- 项目目录：`/home/loviya/sub2api`
- 部署目录：`/home/loviya/sub2api/deploy`
- Git remote：`https://github.com/Wei-Shaw/sub2api.git`
- 当前分支状态：`main...origin/main`，无未提交改动。
- 旧 worklog：
  - `/home/loviya/.codex/worklogs/2026-05-07/20260507-sub2api-env-config.md`
  - `/home/loviya/.codex/worklogs/2026-05-07/20260507-local-postgres-redis-removal.md`
- 当前 Docker Compose 容器仍在运行且 healthy：
  - `sub2api`: `0.0.0.0:8080->8080/tcp`
  - `sub2api-postgres`: `0.0.0.0:5432->5432/tcp`
  - `sub2api-redis`: `0.0.0.0:6379->6379/tcp`
- 页面公开配置显示当前关闭注册和密码重置。
- 数据库不是空库；Postgres 日志显示 existing database directory，跳过初始化。
- 当前只有 1 个用户，邮箱登录身份存在，用户状态 `active`，但余额为 `0.00000000`。
- 当前有 2 个 API key，均为 `active` 且未过期，但 key quota 为 `0.00000000`。
- 应用日志记录多次 `/api/v1/auth/login` 返回 `401`，表示当前输入的登录凭据不匹配。
- 之前 worklog 已记录生成的 client key 调用 Gemini endpoint 返回 `403 Insufficient account balance`，与当前余额为 0 一致。
- 启动日志显示 `2026-05-07 12:59:11` 首次创建管理员用户；代码注释和实现表明管理员用户只在数据库为空/无管理员时创建，已有用户不会被 `.env` 中的 `ADMIN_PASSWORD` 覆盖。
- 用户最后一次成功登录是 `2026-05-07 13:02:28`；用户记录 `updated_at` 是 `2026-05-07 13:53:50`，但系统日志没有明确记录一次密码修改事件。
- 已将管理员用户 `gvn98065@gmail.com` 的数据库密码 hash 重置为用户指定的新密码，登录接口验证返回 `200`。
- 用户提供的 `sk-28921...` key 使用 Gemini 原生端点测试，Bearer 认证可通过密钥校验，但返回 `403 Insufficient account balance`；说明 key/路由有效，当前阻塞是用户余额不足。
- 2026-05-15 20:33 继续检查时，Docker Compose 三个容器仍为 healthy；`users.balance` 仍为 `0.00000000`，两个 API key 的 `quota` 也仍为 `0.00000000`。
- `accounts` 表里已有两个 Gemini OAuth 账号，均为 `active` 且 `schedulable=true`，无 `error_message`。
- 最近日志里 `gemini-gvn` token refresh 在 20:18 成功；Drive API scope 403 只影响 Google One tier 检测，不等同于 Gemini OAuth 账号不可用。
- 用户截图显示正在添加 OpenAI 账号授权，当前步骤是手动 OAuth：浏览器授权后把 `http://localhost:1455/auth/callback?code=...&state=...` 完整链接或只把 `code` 填入第 3 步，再点击完成授权。

## 定位本地 Sub2API 项目

- 更新时间: 2026-05-15 19:12:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `我记得本地有个sub2api项目,找一下`
- 问题:
  - 用户需要找回本地 `sub2api` 项目位置。
- 命令:
  - `find /home/loviya -maxdepth 5 -iname '*sub2api*'`
  - `rg -n "sub2api|sub2api..." ~/.codex/worklogs ~/.zsh_history ~/.bash_history`
  - `git -C /home/loviya/sub2api remote -v`
  - `git -C /home/loviya/sub2api status --short --branch`
  - `ls -la /home/loviya/sub2api`
  - `ls -la /home/loviya/sub2api/deploy`
  - `docker compose ps`
  - `docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'`
- 结果:
  - 找到项目和部署目录，确认它是从 `Wei-Shaw/sub2api` 克隆。
  - 通过 Docker 确认 Sub2API、Postgres、Redis 三个容器当前都健康运行。
- 下一步:
  - 无

## 诊断之前注册的账号为什么不可用

- 更新时间: 2026-05-15 19:24:00 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `为什么我之前注册的现在没法使用了`
- 问题:
  - 用户反馈之前注册的 Sub2API 账号或密钥现在无法使用。
- 命令:
  - `docker compose ps`
  - `docker compose logs --tail=120 sub2api`
  - `docker compose logs --tail=80 postgres`
  - `curl -fsS http://127.0.0.1:8080/`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c '\\dt'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c 'select ... from users'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c 'select ... from api_keys'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c 'select ... from accounts'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c 'select ... from auth_identities'`
- 结果:
  - 服务和数据库都在，Postgres 数据目录没有被重新初始化。
  - 账号存在且状态 active，但余额为 0；API key 存在且 active，但 quota 为 0。
  - 登录接口返回 401，说明登录凭据不匹配；注册和密码重置当前关闭。
  - 上游 Gemini OAuth account 状态 active/schedulable，最近日志中 token refresh 成功，但也出现过访问 Google API 的 EOF 网络错误。
- 下一步:
  - 如无法登录，重置该用户密码。
  - 如能登录但 API 调用失败，先给用户余额或 key quota 充值，再测试。

## 解释为什么保存的登录密码会不同

- 更新时间: 2026-05-15 19:31:00 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `我之前登陆sub2api的邮箱密码显示错误怎么会是`
- 问题:
  - 用户不理解之前能登录的 Sub2API 邮箱密码为什么现在显示错误。
- 命令:
  - `docker compose logs sub2api | rg -n "admin|user|password|created|exists|initialize"`
  - `rg -n "ADMIN_PASSWORD|Create.*Admin|password_hash|bcrypt|CheckPassword" /home/loviya/sub2api/backend /home/loviya/sub2api/deploy`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c 'select id,email,role,status,created_at,updated_at,last_login_at from users'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c 'select ... from ops_system_logs where created_at between ...'`
- 结果:
  - `ADMIN_PASSWORD` 是初始管理员创建用的环境变量，不是每次启动都会同步到已有数据库用户。
  - 登录密码校验走 bcrypt hash；当前 401 的含义是输入密码与数据库中的 hash 不匹配。
  - 管理员创建时间是 `2026-05-07 12:59:11`，最后成功登录时间是 `2026-05-07 13:02:28`。
  - 用户记录之后在 `2026-05-07 13:53:50` 有更新，但日志只显示当时会话仍能访问 `/api/v1/auth/me`，没有明确记录密码修改事件。
- 下一步:
  - 如果用户确认要恢复登录，可直接重置数据库中该用户的密码 hash。

## 重置管理员登录密码

- 更新时间: 2026-05-15 19:38:00 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `ok,改成buxinren123`
- 问题:
  - 用户需要恢复 Sub2API 管理员账号登录。
- 命令:
  - `python3 -c 'import bcrypt; ...'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c "update users set password_hash = ..., updated_at = now() where id = 1 and email = ..."`
  - `curl ... /api/v1/auth/login`
- 结果:
  - `users` 表更新返回 `UPDATE 1`。
  - 使用新密码登录 `/api/v1/auth/login` 返回 HTTP `200`。
  - 登录验证产生的临时响应文件已删除，避免 token 留在 `/tmp`。
- 下一步:
  - 用户用邮箱 `gvn98065@gmail.com` 和新密码登录。
  - 若登录后 API 调用仍报余额不足，继续给用户余额或 key quota 充值。

## 测试已生成的 Gemini API Key

- 更新时间: 2026-05-15 19:27:39 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `sk-...这是我用sub2api生成的密匙,测试一下,gemini账号使用的`
- 问题:
  - 用户需要验证 Sub2API 生成的 key 是否能通过 Gemini 账号调用。
- 命令:
  - `curl ... /v1beta/models/gemini-2.5-flash:generateContent`
  - `docker compose logs --tail=80 sub2api | rg ...`
- 结果:
  - 使用 `x-goog-api-key` 头时返回 `401 API key is required`，该接口在当前服务中应使用 Bearer 认证。
  - 使用 `Authorization: Bearer <key>` 后返回 `403 Insufficient account balance`。
  - 日志记录了 `/v1beta/models/gemini-2.5-flash:generateContent` 请求，状态码从错误认证头的 `401` 变为 Bearer 认证后的 `403`。
  - 临时响应文件已删除，避免密钥测试结果残留。
- 下一步:
  - 给用户余额或 key quota 充值后再测试 Gemini 调用。

## 继续 Sub2API 授权调试

- 更新时间: 2026-05-15 20:33:21 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `继续sub2api调试`
- 问题:
  - 用户继续调试 Sub2API，并截图显示正在添加 OpenAI 账号授权。
- 命令:
  - `docker compose ps`
  - `docker compose logs --tail=160 sub2api`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c 'select ... from users'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c '\\d api_keys'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c '\\d accounts'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c 'select ... from accounts'`
  - `docker exec sub2api-postgres psql -U sub2api -d sub2api -c 'select ... from api_keys'`
  - `rg -n 'generate-auth-url|auth/callback|refresh_token|OpenAI 账户授权' backend frontend`
- 结果:
  - Sub2API、Postgres、Redis 容器仍在运行且 healthy。
  - Gemini OAuth account 状态正常，但用户余额和两个 API key quota 都是 0。
  - OpenAI 手动授权页面支持直接粘贴完整 callback URL；前端会自动提取 `code` 和 `state`，后端 `/api/v1/admin/openai/exchange-code` 要求 `session_id`、`code`、`state`。
- 下一步:
  - 用户完成浏览器 OAuth 后，把完整 localhost callback URL 或 code 填回截图第 3 步并点击完成授权。
  - 授权完成后查询 `accounts` 表确认新增 OpenAI 账号。

## 2026-05-21 13:42 +0800

- 来源指令: 用户反馈 `不行访问不了`。
- 工作目录: `/home/loviya/sub2api/deploy`。
- 检查: `curl -I http://127.0.0.1:8080/` 返回 `200 OK`；`curl http://127.0.0.1:8080/health` 返回 `{"status":"ok"}`。
- 检查: `docker compose ps` 显示 `sub2api`、`sub2api-postgres`、`sub2api-redis` 均为 `Up`/healthy，`sub2api` 端口映射 `0.0.0.0:8080->8080/tcp`。
- 检查: `ss -ltnp` 显示宿主机 `0.0.0.0:8080` 正在监听。
- 处理: 执行 `xdg-open http://127.0.0.1:8080/`，日志随后显示首页、前端 assets、`/api/v1/auth/me` 和多个 admin API 正常返回 200。
- 结论: 本机服务和当前浏览器访问链路正常；若仍访问不了，优先排查用户使用的 URL、是否从其他设备访问、浏览器代理/缓存。局域网地址为 `http://10.139.212.78:8080/`。

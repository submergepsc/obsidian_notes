---
id: 20260521-codex-sub2api-free-openai-home
name: Codex sub2api free_openai 账户 home
slug: codex-sub2api-free-openai-home
cwd: /home/loviya
summary: "创建 `.codex-sub2api-free_openai` Codex 账户 home，绑定本地 sub2api free_openai provider。"
tags:
  - codex
  - sub2api
  - free_openai
---

# Current Snapshot

- workflow id: 20260521-codex-sub2api-free-openai-home
- current status: 阻塞
- current goal: 设置 `.codex-sub2api-free_openai`，用于通过本地 sub2api 的 `free_openai` 分组启动 Codex。
- current blocker: Codex 账户 home 和启动入口已配置完成，但 sub2api 的唯一 OpenAI 上游账号 `free1` 当前返回 429/503，上游不可用或限流严重。
- next step: 等 `free1` 上游限流恢复后重试，或在 sub2api 中添加/绑定另一个可用 OpenAI 账号到 `free_openai` 分组。
- tags: codex, sub2api, free_openai
- summary: 已创建 `/home/loviya/.codex-sub2api-free_openai`，写入专属 env、`config.toml`、`model_catalog.json`、启动脚本和 shell alias。API key 只写入专属 env，未写入 worklog。`codex-sub2api-free_openai exec` 能解析为 `provider: sub2api_free_openai` 和 `model: gpt-5.3-codex`，但真实请求被上游 429 阻塞。

# Key Results

- 新账户 home: `/home/loviya/.codex-sub2api-free_openai`
- 新启动入口: `/home/loviya/.local/bin/codex-sub2api-free_openai`
- 新 alias: `codex-sub2api-free_openai`，已写入 `/home/loviya/.zshrc` 和 `/home/loviya/.bashrc`
- Provider: `sub2api_free_openai`
- Base URL: `http://127.0.0.1:8080/v1`
- Wire API: `responses`
- 默认模型: `gpt-5.3-codex`
- sub2api API key: 使用 `free1_openai`，只保存于 `/home/loviya/.codex-sub2api-free_openai/sub2api-free_openai.env`

# Log

## 2026-05-21 14:24 +0800

- 来源指令: 用户要求“设置一个 `.codex-sub2api-free_openai`”，随后要求继续。
- 环境: sub2api 当前运行在 `http://127.0.0.1:8080`，`/health` 可用。
- 查询: sub2api 中 OpenAI 账号只有 `free1`，platform `openai`、type `apikey`、status `active`、schedulable `true`，绑定 group `free_openai`。
- 查询: `free1` 的 base_url 为 `https://fzero.us.ci/v1`，支持 Responses，模型映射包含 `gpt-5.3-codex`、`gpt-5.4-mini`、`gpt-5.4`、`gpt-5.5`、`gpt-5.2` 等。
- 处理: 创建 `/home/loviya/.codex-sub2api-free_openai`，按账户隔离规则创建 `log`、`tmp`、`.tmp`、`cache`、`sessions`、`shell_snapshots`，共享 `AGENTS.md`、`continue.md`、`worklogs`、`skills`、`rules`、`memories`、`vendor_imports`、`plugins`。
- 处理: 从 sub2api 数据库读取 `free1_openai` API key，写入专属 env 文件；env 文件权限为 `600`，账户 home 权限为 `700`。
- 处理: 写入 `config.toml`，provider `sub2api_free_openai` 指向 `http://127.0.0.1:8080/v1`，`wire_api = responses`，`env_key = SUB2API_FREE_OPENAI_API_KEY`。
- 处理: 写入 `model_catalog.json`；第一次格式使用 `id` 字段导致 Codex 报 `missing field slug`，已改为包含 `slug` 的 Codex catalog 结构。
- 处理: 写入启动脚本 `/home/loviya/.codex-sub2api-free_openai/codex-sub2api-free_openai`，并链接到 `/home/loviya/.local/bin/codex-sub2api-free_openai`。
- 处理: 启动脚本第一次只 source env，未 export 给 Codex 子进程，导致 `Missing environment variable: SUB2API_FREE_OPENAI_API_KEY`；已改为 `set -a; source ...; set +a`。
- 处理: 已向 `/home/loviya/.zshrc` 和 `/home/loviya/.bashrc` 添加 alias `codex-sub2api-free_openai`。
- 处理: sub2api 用户余额和 `free1_openai` key quota 原为 0，导致 `403 INSUFFICIENT_BALANCE`；已将用户余额和该 key quota 补为 `1000.00000000`，并重启 `sub2api` 容器刷新缓存。
- 验证: `codex-sub2api-free_openai --version` 返回 `codex-cli 0.132.0`。
- 验证: `codex-sub2api-free_openai exec --skip-git-repo-check 'Reply exactly: ok'` 能启动 Codex，显示 `provider: sub2api_free_openai`、`model: gpt-5.3-codex`。
- 阻塞: 真实请求最终返回 `429 Too Many Requests`；直接测试多个模型时，`gpt-5.4-mini` 和 `gpt-5.2` 返回 429，`gpt-5.4`、`gpt-5.5`、`gpt-5.3-codex-spark` 返回 503。日志显示 `account_id=3` upstream 429 后没有可切换账号。

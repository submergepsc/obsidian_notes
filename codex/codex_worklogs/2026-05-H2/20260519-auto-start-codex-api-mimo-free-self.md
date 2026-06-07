---
id: 20260519-auto-start-codex-api-mimo-free-self
name: codex-api-mimo-free-self 自动启动包装
slug: auto-start-codex-api-mimo-free-self
cwd: /home/loviya
summary: 将 codex-api-mimo-free-self 包装为一条命令，自动启动 mimi3 网关并绑定专属 CODEX_HOME。
tags:
  - codex
  - api
  - mimo1
  - shell
---

# Current Snapshot

- workflow id: `20260519-auto-start-codex-api-mimo-free-self`
- current status: `已完成`
- current goal: 让用户只运行 `codex-api-mimo-free-self` 即可完成 mimi3 网关检查/启动与 Codex 启动。
- current blocker: 无
- next step: 无
- tags: `codex`, `api`, `mimo1`, `shell`
- summary: 已将自动启动 mimi3 网关的逻辑写入 `codex_api_mimo_free_self` wrapper，并在 `.zshrc`/`.bashrc` 添加 `codex-api-mimo-free-self` alias。

# Key Results

- `/home/loviya/.codex-api-mimo-free-self/codex-api-mimo-free-self` 现在会先检查 `http://127.0.0.1:8000/api/system/status`。
- 如果网关无响应，会在 `/home/loviya/code/mimi3` 下用 `.venv/bin/python main.py` 后台启动服务，并等待最多 30 秒。
- 如果网关启动后仍无响应，会提示查看 `/home/loviya/code/mimi3/logs/gateway.log`。
- 如果网关在线但 `active_clients=0`，仍按原行为给出 Claw 节点警告，然后进入 Codex。
- `/home/loviya/.zshrc` 和 `/home/loviya/.bashrc` 都新增了 `alias codex-api-mimo-free-self='$HOME/.local/bin/codex-api-mimo-free-self'`。

# Commands

- 读取 `/home/loviya/.codex-api-mimo-free-self/codex-api-mimo-free-self`，确认其使用 `CODEX_HOME=/home/loviya/.codex-api-mimo-free-self`、`MIMO1_BASE_URL=http://127.0.0.1:8000`、`MIMO1_MODEL=mimo-v2.5-pro`。
- 定点检查 `.zshrc` 和 `.bashrc` alias 区域，确认缺少 `codex-api-mimo-free-self`。

# Verification

- `bash -n /home/loviya/.codex-api-mimo-free-self/codex-api-mimo-free-self` 通过。
- `rg -n "MIMI3_DIR|nohup|codex-api-mimo-free-self|active_clients" ...` 确认 wrapper 与 alias 内容已写入。
- `/home/loviya/.local/bin/codex-api-mimo-free-self --version` 返回 `codex-cli 0.130.0`，验证 version 分支不会误启动交互式会话。

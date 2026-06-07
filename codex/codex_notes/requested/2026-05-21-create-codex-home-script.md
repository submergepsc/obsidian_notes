---
title: create-codex-home 脚本说明
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - codex
  - account-home
  - script
source_worklog: 20260521-create-codex-home-script
updated: 2026-05-21
---

# create-codex-home 脚本说明

## 结论

`/home/loviya/.local/bin/create-codex-home` 用来快速创建新的 `.codex*` Codex 账户 home。

它会自动生成：

- 隔离账户目录，例如 `/home/loviya/.codex-sub2api-free_openai`
- `config.toml`
- `model_catalog.json`
- 专属 env 文件
- 账户内启动脚本
- `/home/loviya/.local/bin/codex-*` 启动入口
- 可选 shell alias，默认写入 `/home/loviya/.zshrc` 和 `/home/loviya/.bashrc`
- 共享路径 symlink

脚本不会把整个账户 home 链到共享目录；只链接本机约定的共享内容路径，认证、sessions、cache、sqlite state、logs 等保持账户隔离。

## 脚本位置

```bash
/home/loviya/.local/bin/create-codex-home
```

查看帮助：

```bash
create-codex-home --help
```

## 常用示例

创建一个通过 sub2api `free_openai` 分组访问的 Codex home：

```bash
create-codex-home \
  --name sub2api-free_openai \
  --provider sub2api_free_openai \
  --provider-name "Sub2API free_openai" \
  --base-url http://127.0.0.1:8080/v1 \
  --model gpt-5.3-codex \
  --env-key SUB2API_FREE_OPENAI_API_KEY \
  --model-env-key SUB2API_FREE_OPENAI_MODEL \
  --health-url http://127.0.0.1:8080/health \
  --trust /home/loviya/sub2api
```

生成后运行：

```bash
codex-sub2api-free_openai
```

或直接调用入口：

```bash
/home/loviya/.local/bin/codex-sub2api-free_openai
```

## 参数说明

- `--name`: 账户名。`foo`、`codex-foo`、`.codex-foo` 都会规范成 `/home/loviya/.codex-foo`。
- `--provider`: 写入 `config.toml` 的 provider key，例如 `sub2api_free_openai`。
- `--provider-name`: provider 显示名。
- `--base-url`: provider base URL，通常以 `/v1` 结尾。
- `--model`: 默认模型。
- `--env-key`: API key 的环境变量名。
- `--model-env-key`: 模型名环境变量名；不传时会从 `--env-key` 推导。
- `--api-key`: 可选，直接写入专属 env 文件。注意不要把 key 写入 notes 或聊天。
- `--health-url`: 可选，启动 Codex 前先检查本地代理是否可用。
- `--trust`: 可信项目路径，可重复传入。
- `--no-alias`: 不写 `.zshrc` / `.bashrc` alias。
- `--force`: 覆盖生成的 config、catalog、launcher；已有 env 中的 key 默认保留，除非同时传 `--api-key`。

## 自动创建的共享链接

脚本会在新 home 中链接这些共享路径：

```text
AGENTS.md       -> /home/loviya/.codex/AGENTS.md
continue.md     -> /home/loviya/.codex/continue.md
worklogs/       -> /home/loviya/.codex/worklogs
skills/         -> /home/loviya/.codex/skills
rules/          -> /home/loviya/.codex/rules
memories/       -> /home/loviya/.codex/memories
vendor_imports/ -> /home/loviya/.codex/vendor_imports
codex_notes/    -> /home/loviya/.codex/codex_notes
plugins/        -> /home/loviya/.codex-shared/plugins
```

账户专属内容仍在新 home 内独立保存，例如：

```text
config.toml
env 文件
history.jsonl
sessions/
state_5.sqlite*
logs_2.sqlite*
log/
tmp/
.tmp/
cache/
models_cache.json
```

## 生成文件结构

以 `--name sub2api-free_openai` 为例：

```text
/home/loviya/.codex-sub2api-free_openai/
  config.toml
  model_catalog.json
  sub2api-free_openai.env
  codex-sub2api-free_openai
  AGENTS.md -> /home/loviya/.codex/AGENTS.md
  worklogs -> /home/loviya/.codex/worklogs
  skills -> /home/loviya/.codex/skills
  ...

/home/loviya/.local/bin/codex-sub2api-free_openai -> /home/loviya/.codex-sub2api-free_openai/codex-sub2api-free_openai
```

## 修改入口

以后要改脚本本身：

```bash
sed -n '1,220p' /home/loviya/.local/bin/create-codex-home
```

常见修改点：

- 默认共享 symlink 列表：脚本里的 `for item in ...`。
- 默认 `config.toml` 字段：脚本中写 `config_file` 的 block。
- 默认 `model_catalog.json` 模板：脚本中写 `catalog_file` 的 heredoc。
- 启动脚本行为：脚本中写 `launcher_file` 的 heredoc。
- alias 写入逻辑：脚本末尾 `write_alias` 相关代码。

## 验证命令

脚本语法检查：

```bash
bash -n /home/loviya/.local/bin/create-codex-home
```

查看当前 `.codex*` 目录：

```bash
find /home/loviya -maxdepth 1 -type d -name '.codex*' -printf '%f\n' | sort
```

检查某个账户 home 的链接：

```bash
find /home/loviya/.codex-某账户 -maxdepth 1 -printf '%f %y -> %l\n' | sort
```

检查生成入口：

```bash
codex-某账户 --version
```

## 注意事项

- 不要把 API key、token、cookie 或 OAuth secret 写进 worklog、notes、聊天或 shell history。
- 新 home 的目录权限应为 `700`，env 文件权限应为 `600`。
- 如果本地代理不可用，带 `--health-url` 的启动脚本会在启动 Codex 前直接报 health check failed。
- 如果 Codex 报 `missing field slug`，说明 `model_catalog.json` 格式不对；当前脚本已生成带 `slug` 的 catalog 模板。
- 如果 Codex 报缺少环境变量，检查启动脚本是否用 `set -a; source env; set +a` 把 env 导出给子进程。

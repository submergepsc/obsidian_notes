---
id: 20260521-create-codex-home-script
name: create-codex-home 脚本
slug: create-codex-home-script
cwd: /home/loviya
summary: "创建 `/home/loviya/.local/bin/create-codex-home`，用于快速生成隔离的 `.codex*` Codex home、共享链接、配置和启动入口。"
tags:
  - codex
  - script
  - account-home
---

# Current Snapshot

- workflow id: 20260521-create-codex-home-script
- current status: 已完成
- current goal: 写一个脚本，方便创建 `.codex*` Codex 配置账户，并自动把共享文件链接完整创建好。
- current blocker: 无
- next step: 无；后续创建新账户时运行 `create-codex-home --help` 查看参数。
- tags: codex, script, account-home
- summary: 已创建 `/home/loviya/.local/bin/create-codex-home`。脚本支持生成隔离 Codex home、共享 symlink、`config.toml`、`model_catalog.json`、专属 env、launcher、`~/.local/bin` 入口和可选 shell alias；env 权限为 `600`，账户 home 权限为 `700`。

# Key Results

- 新脚本: `/home/loviya/.local/bin/create-codex-home`
- 权限: `700`
- 支持参数: `--name`、`--provider`、`--provider-name`、`--base-url`、`--model`、`--env-key`、`--model-env-key`、`--api-key`、`--health-url`、`--trust`、`--no-alias`、`--force`
- 自动共享链接: `AGENTS.md`、`continue.md`、`worklogs`、`skills`、`rules`、`memories`、`vendor_imports`、`codex_notes`、`plugins`
- 自动账户专属目录: `log`、`tmp`、`.tmp`、`cache`、`sessions`、`shell_snapshots`

# Log

## 2026-05-21 15:15 +0800

- 来源指令: 用户要求“写个脚本，方便创建 `.codex*` 的 codex 配置文件，然后所有的文件链接都对应完成”。
- 参考: 检查了现有 `.codex-sub2api-free_openai` 和 `.codex-api-mimo-free-self` 的布局，确认共享链接和账户专属文件分离方式。
- 处理: 新增 `/home/loviya/.local/bin/create-codex-home`。
- 处理: 由于当前 sandbox 受 `/home/loviya/.codex-b/memories/.git` 跨 symlink 挂载问题影响，`apply_patch` 后续修订受阻；最终用提升权限重写刚创建的新脚本。
- 行为: 脚本会标准化名称，例如 `foo`、`codex-foo`、`.codex-foo` 都生成 `/home/loviya/.codex-foo` 和 `codex-foo` 启动入口。
- 行为: 脚本默认生成 Responses wire API provider，专属 env 文件默认保留或新建；使用 `--force` 不会覆盖已有 API key，除非显式提供 `--api-key`。
- 行为: 脚本会创建 Codex model catalog 的 `slug` 格式，避免 Codex CLI 报 `missing field slug`。
- 验证: `bash -n /home/loviya/.local/bin/create-codex-home` 通过。
- 验证: `/home/loviya/.local/bin/create-codex-home --help` 正常输出说明。
- 验证: 使用临时名称 `script-smoke-test` 生成了测试 home，检查到 config、launcher、env 和共享链接均正常；`codex-script-smoke-test --version` 返回 `codex-cli 0.132.0`。
- 清理: 已将测试目录 `/home/loviya/.codex-script-smoke-test` 移到 `/tmp/codex-script-smoke-test-20260521-1513`；已将测试入口移到 `/tmp/codex-script-smoke-test-launcher-20260521-1513`。

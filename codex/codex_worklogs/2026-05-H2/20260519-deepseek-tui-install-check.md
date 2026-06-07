---
id: 20260519-deepseek-tui-install-check
name: deepseek-tui-install-check
slug: deepseek-tui-install-check
cwd: /home/loviya
summary: "检查 npm 全局安装的 deepseek-tui：命令入口、版本、doctor、认证状态、API 连接和可选组件。"
tags: [deepseek-tui, terminal, npm, deepseek, cli]
---

# DeepSeek TUI 安装检查

## Current Snapshot

- workflow id: `20260519-deepseek-tui-install-check`
- current status: `已完成`
- current goal: 检查用户已安装的 `deepseek-tui` 是否可用。
- current blocker: 无。
- next step: 如需使用 MCP/tools/plugins，可运行对应 setup；否则可直接使用 `deepseek`。
- tags: deepseek-tui, terminal, npm, deepseek, cli
- summary: `deepseek-tui@0.8.39` 已全局安装到 Node v22.22.2 的 nvm 目录；`deepseek` 与 `deepseek-tui` 命令入口正常；`doctor` 显示 DeepSeek provider 配置存在且 API connection successful；sandbox 可用；Python/Node/pandoc 工具可用；MCP 配置、tools/plugins 目录未初始化；tesseract/pdftotext 为可选缺失。

## Key Results

- 安装位置：`/home/loviya/.nvm/versions/node/v22.22.2/lib/node_modules/deepseek-tui`。
- 命令入口：
  - `/home/loviya/.nvm/versions/node/v22.22.2/bin/deepseek`
  - `/home/loviya/.nvm/versions/node/v22.22.2/bin/deepseek-tui`
- 版本：npm wrapper 与 binary 都是 `0.8.39`。
- 配置：`~/.deepseek/config.toml` 存在；provider 为 `deepseek`，默认模型为 `deepseek-v4-pro`。
- 认证：`doctor` 和 `auth status` 显示 key 可解析；本 worklog 不记录 API key 内容。
- API：`deepseek doctor` 连接测试成功。
- session store：`deepseek sessions` 可读，存在一个最近会话。

## Verification

- `npm list -g --depth=0 deepseek-tui`：显示 `deepseek-tui@0.8.39`。
- `deepseek --version`：通过。
- `deepseek-tui --version`：通过。
- `deepseek --help`：通过。
- `deepseek doctor`：All checks complete，API connection successful。

## Notes

- 可选缺失：`~/.deepseek/mcp.json` 未初始化；`~/.deepseek/tools` 和 `~/.deepseek/plugins` 未创建；`tesseract` 和 `pdftotext` 未安装。
- `pdftotext` 在 v0.8.32 后不是必需，默认可用 pure-Rust extractor。
- `tesseract` 只影响 OCR tool 是否暴露给模型。

---
id: 20260507-anthropic-download
name: Anthropic 下载需求澄清
slug: anthropic-download
cwd: /home/loviya/sub2api/deploy
summary: 澄清用户想下载的 Anthropic 相关工具、包、镜像或文件后再继续处理。
tags:
  - download
  - anthropic
  - sub2api
priority: normal
---

# Anthropic 下载 澄清

## 当前快照

- 状态: 进行中
- 目标: 确认 `anthoric` 指什么，再下载或安装用户真正想要的 Anthropic 相关产物。
- 阻塞: 下载目标不明确；`anthoric` 可能是 `anthropic` 的拼写错误，但用户未指定具体包、CLI、Docker 镜像或文件。
- 下一步: 请用户确认想要的是 Claude Code、Anthropic SDK/包、Docker 镜像还是其他文件。
- 更新时间: 2026-05-07 13:14:39 +0800

## 关键结果

- 没有现有的 unfinished workflow matched `anthoric` or `anthropic`.
- The current deploy directory contains Anthropic API configuration references, but no obvious local download target named `anthoric`.

## Clarify 下载 Target

- 更新时间: 2026-05-07 13:14:39 +0800
- 工作目录: `/home/loviya/sub2api/deploy`
- 来源指令: `下载一下anthoric`
- 问题:
  - The request does not specify whether to download or install a CLI, SDK package, Docker image, config, or release artifact.
  - `anthoric` is likely a typo for `anthropic`.
- 改进:
  - Inspected the current deployment directory for local scripts and Anthropic-related references before choosing an install/download command.
- 结果:
  - Need user confirmation before performing a network download or system/package install.
- 下一步:
  - Confirm the intended target, then run the appropriate download or install command.

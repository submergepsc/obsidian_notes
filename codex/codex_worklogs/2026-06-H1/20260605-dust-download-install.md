---
id: 20260605-dust-download-install
name: dust 下载与用户级安装
slug: dust-download-install
cwd: /home/loviya
summary: 下载并安装 Linux x86_64 的 dust 磁盘占用查看工具。
tags:
  - dust
  - download
  - cli-tool
---

# dust 下载与用户级安装

## Current Snapshot

- workflow id: 20260605-dust-download-install
- current status: 已完成
- current goal: 下载并安装 `dust` 命令，优先放到用户级 PATH。
- current blocker: none
- next step: none
- tags: dust, download, cli-tool
- summary: 已从官方 GitHub release 下载 `dust-v1.2.4-x86_64-unknown-linux-gnu.tar.gz` 到 `/home/loviya/Downloads/`，SHA256 校验通过，并安装 `dust` 到 `/home/loviya/.local/bin/dust`；`dust --version` 输出 `Dust 1.2.4`。

## Session 2026-06-06

- 来源指令: `下载一下dust`
- 完成时间: 2026-06-06 01:31:06 +0800
- 已确认:
  - `pwd`: `/home/loviya`
  - `CODEX_HOME`: empty；本任务仅下载/安装用户级 CLI，不影响账户专属 Codex 运行态。
  - `command -v dust`: 无输出，说明当前 PATH 未找到 `dust`。
  - `uname -sm`: `Linux x86_64`
- 下载:
  - 来源: `https://github.com/bootandy/dust/releases/download/v1.2.4/dust-v1.2.4-x86_64-unknown-linux-gnu.tar.gz`
  - 保存: `/home/loviya/Downloads/dust-v1.2.4-x86_64-unknown-linux-gnu.tar.gz`
  - SHA256: `707cfdbfb9d2dc536f8c3853815bbe98a01012f2772463835edae06816551160`
- 安装:
  - 解压临时目录: `/tmp/codex-dust-v1.2.4/`
  - 可执行文件: `/home/loviya/.local/bin/dust`
- 验证:
  - `command -v dust` -> `/home/loviya/.local/bin/dust`
  - `dust --version` -> `Dust 1.2.4`
  - `dust -d 1 /home/loviya/.local/bin` 成功输出目录占用概览。

## Commands

- `command -v dust`
- `uname -sm`
- `wget -O /home/loviya/Downloads/dust-v1.2.4-x86_64-unknown-linux-gnu.tar.gz https://github.com/bootandy/dust/releases/download/v1.2.4/dust-v1.2.4-x86_64-unknown-linux-gnu.tar.gz`
- `sha256sum /home/loviya/Downloads/dust-v1.2.4-x86_64-unknown-linux-gnu.tar.gz`
- `tar -xzf /home/loviya/Downloads/dust-v1.2.4-x86_64-unknown-linux-gnu.tar.gz -C /tmp/codex-dust-v1.2.4`
- `install -m 0755 /tmp/codex-dust-v1.2.4/dust-v1.2.4-x86_64-unknown-linux-gnu/dust /home/loviya/.local/bin/dust`
- `dust --version`

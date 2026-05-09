---
id: 20260508-copyq-restart
name: Restart CopyQ Service
slug: copyq-restart
cwd: /home/loviya/notes/obsidian_notes/homework/os
summary: Closed a stuck host CopyQ process and restarted the CopyQ server.
tags:
  - desktop
  - copyq
  - clipboard
priority: normal
---

# Restart CopyQ Service

## Current Snapshot

- status: 已完成
- goal: 关闭卡死的宿主 CopyQ 并重新启动服务端。
- blocker: none
- next: none
- updated: 2026-05-08 20:28:35 +0800

## Key Results

- 初始 `pgrep -a -u "$USER" copyq` 未发现普通 `copyq` 进程。
- 已执行 `pkill -f copyq` 清理可能残留的 CopyQ 相关进程。
- 已执行 `copyq --start-server` 重启 CopyQ 服务端。
- 验证命令 `copyq --start-server count` 返回 `200`，说明 CopyQ 服务端可响应。
- 用户反馈仍卡死后，在宿主桌面会话执行 `copyq exit`、`pkill -TERM -f '[c]opyq'`，最后对残留 PID `4853` 和 `460388` 执行 `kill -KILL`。
- 重新启动后，宿主进程为 `/usr/bin/copyq -s` 和 `/usr/bin/copyq --clipboard-access monitorClipboard`，历史数量查询返回 `200`。

## Restart CopyQ Service

- updated: 2026-05-08 20:24:40 +0800
- cwd: `/home/loviya/notes/obsidian_notes/homework/os`
- source instruction: `帮我关闭一下copyq然后重启一下`
- problem:
  - 用户需要关闭并重启 CopyQ，以恢复剪贴板历史服务。
- commands:
  - `pgrep -a -u "$USER" copyq`
  - `pkill -f copyq`
  - `copyq --start-server`
  - `copyq --start-server count`
- result:
  - CopyQ 服务端重启成功，历史数量查询返回 `200`。
- next:
  - none

## Force Restart Stuck Host CopyQ

- updated: 2026-05-08 20:28:35 +0800
- cwd: `/home/loviya/notes/obsidian_notes/homework/os`
- source instruction: `不行还是卡死,重启`
- problem:
  - 桌面会话里的 CopyQ 仍然卡死，普通退出和 TERM 后仍有残留进程。
- commands:
  - `copyq exit`
  - `pkill -TERM -f '[c]opyq'`
  - `kill -KILL 4853 460388`
  - `copyq --start-server`
  - `copyq --start-server count`
- result:
  - 已强制清理卡死进程并重新启动 CopyQ 服务端。
- next:
  - none

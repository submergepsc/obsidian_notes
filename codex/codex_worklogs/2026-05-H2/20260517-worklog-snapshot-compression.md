---
id: 20260517-worklog-snapshot-compression
name: Worklog Snapshot Compression
slug: worklog-snapshot-compression
cwd: /home/loviya
summary: 增加规则：长工作流快照保持简短，并压缩旧历史，让结论留在文件顶部附近。
tags:
  - codex
  - worklog
  - policy
  - snapshot
priority: normal
---

# 工作日志 Snapshot 压缩

## 当前快照

- 状态: 已完成
- 目标: 把“长工作流保持顶部快照短、压缩历史块”的规则写进 `~/.codex/AGENTS.md`，并同步到 worklog 与 notes。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-17 18:15:00 +0800

## 关键结果

- 已将“长工作流保持顶部快照短、压缩历史块”写入 `/home/loviya/.codex/AGENTS.md`。
- 已创建对应 worklog 和 system note，并刷新了两个索引。
- 已通过 `rg` 复核 AGENTS、worklogs 索引和 codex_notes 索引都包含这条规则。

## 决策

- 长工作流仍然只保留一个主 workflow 文件，但历史 session 块应尽量压缩，关键结论优先保留在顶部快照。

## Add Snapshot 压缩 Rule

- 更新时间: 2026-05-17 18:12:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `这个,我觉得很有必要,放到agents.md里面去`
- 问题:
  - 长 workflow 的历史块会越来越多，关键结论如果只躺在后面，后续接续时要多翻很多内容。
- 改进:
  - 把“顶部快照短且最新、旧 session 历史压缩”的要求写成明确规则。
- 结果:
  - 该策略已落地并验证成功。
- 下一步:
  - 无。

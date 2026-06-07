---
id: 20260525-e8c4-project-worklog-index-rules
name: 项目级 Worklog Index 规则
slug: project-worklog-index-rules
cwd: /home/loviya
summary: 将有明确工作区或完整项目时的项目级 worklog 目录与专用 INDEX.md 规则写入全局 AGENTS.md。
tags:
  - agents
  - worklog
  - project-index
---

# 项目级 Worklog Index 规则

## Current Snapshot

- workflow id: `20260525-e8c4-project-worklog-index-rules`
- current status: `已完成`
- current goal: 更新全局 `AGENTS.md`，明确完整项目或明确工作区应在 worklogs 根目录下建立项目级目录和项目级 `INDEX.md`。
- current blocker: 无。
- next step: none
- tags: `agents`, `worklog`, `project-index`
- summary: 已将项目级 worklog 目录和项目级 `INDEX.md` 规则写入全局 `AGENTS.md`，并为 `/home/loviya/code/rwa_plots` 补建项目索引。

## Session Notes

- 当前 `CODEX_HOME` 为 `/home/loviya/.codex-b`，共享规则文件为 `/home/loviya/.codex/AGENTS.md`。
- 普通 sandbox 读取因 `/home/loviya/.codex-b/memories` symlink 布局失败，后续使用提升执行读取和验证。
- `git -C /home/loviya/.codex status --short` 返回非 git 仓库；本次按普通文件修改处理。

## Commands

- `rg -n "AGENTS|项目级|项目.*worklog|worklog.*项目|INDEX|工作日志|输出位置" /home/loviya/.codex/worklogs -g '*.md'`
- `sed -n '115,205p' /home/loviya/.codex/AGENTS.md`
- `sed -n '1,90p' /home/loviya/.codex/worklogs/INDEX.md`

## Key Results

- 已在 `/home/loviya/.codex/AGENTS.md` 新增 `### 项目级工作区`，明确项目目录位于 `~/.codex/worklogs/<project-slug>/`，与半月目录同级。
- 已在索引规则中明确项目级 workflow 要同时维护全局 `INDEX.md` 和项目目录下的 `INDEX.md`。
- 已在输出位置规则中区分非项目/一次性 worklog 与项目级 worklog。
- 已创建 `/home/loviya/.codex/worklogs/rwa_plots/INDEX.md`，索引 `/home/loviya/code/rwa_plots` 相关的 9 个现有 workflow；旧日志暂保留在原半月目录并由项目索引链接。

## Verification

- `rg -n '项目级工作区|project-slug|项目级 Worklog|对项目级 workflow|半月目录同级|项目级目录' /home/loviya/.codex/AGENTS.md` 命中新规则。
- `sed -n '135,215p' /home/loviya/.codex/AGENTS.md` 验证工作日志章节包含项目级工作区、索引和输出位置规则。
- `sed -n '1,80p' /home/loviya/.codex/worklogs/rwa_plots/INDEX.md` 验证项目索引存在并包含 9 个条目。
- `sed -n '1,16p' /home/loviya/.codex/worklogs/INDEX.md` 验证全局索引包含本次 workflow，且保留同时产生的 `20260525-e8a4-plot-protocol-colors` 条目。

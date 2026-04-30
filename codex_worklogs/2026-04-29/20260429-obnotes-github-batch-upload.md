---
id: 20260429-obnotes-github-batch-upload
name: obnotes-github-batch-upload
slug: obnotes-github-batch-upload
cwd: /home/loviya/notes/obsidian_notes
summary: 将当前 obnotes 内容按批次提交并推送到 GitHub。
tags:
  - obnotes
  - github
  - git
  - upload
priority: medium
---

# obnotes-github-batch-upload

## Summary

确认 `~/obnotes` 指向 `/home/loviya/notes/obsidian_notes`，远端为 `git@github.com:submergepsc/obsidian_notes.git`。按三批提交并推送当前内容到 `origin/main`，最终本地工作树干净，远端 `main` 指向最新提交 `a4d438a`。

## 把当前 ~/obnotes 内容分批上传到 GitHub
- updated: 2026-04-29 14:43:40 +0800
- cwd: `/home/loviya`
- host: `nibaba`
- tmux: `unknown`
- source instruction: `把当前obnotes的内容,分批上传到github`
- context: 新任务，未接续旧 workflow。
- status: 已完成
- problem:
  - goal: 把当前 `~/obnotes` 内容分批上传到 GitHub。
  - blocker: 无。`~/.codex/worklogs` 在当前沙箱内不可写，按 AGENTS 规则使用提升权限补写 worklog。
- result:
  - 确认仓库 `/home/loviya/notes/obsidian_notes`，远端 `origin` 为 `git@github.com:submergepsc/obsidian_notes.git`，远端初始 `main` 为 `86ba58e`。检查无超过 95MB 的文件。分三批提交并推送：`f0e4ddd Update vault tracked content`，包含旧 `codex/` 归档删除、已跟踪内容更新和普通笔记/配置；`2d187e3 Add runoob tutorial archive`，包含 `crawl/runoob_tutorial_archive`，推送前剔除新 pyc 并添加 `__pycache__/`、`*.pyc` 忽略规则；`a4d438a Add OI Wiki offline archive`，包含 `crawl/oiwiki` 离线归档/镜像，推送前剔除 `.venv` 并添加 `.venv/` 忽略规则。最终 `git status --short --branch --untracked-files=all` 输出 `## main`，远端 `refs/heads/main` 为 `a4d438ad95713feb1e527c307b86e9aa0bd9a4b2`。
- next: 无。
- tags: obnotes, github, git, upload

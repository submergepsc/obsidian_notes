---
id: 20260523-7c2a-course-pdf-to-md
name: 课件 PDF 批量整理成 Markdown
slug: course-pdf-to-md
cwd: /home/loviya
summary: 将 /home/loviya/下载/课件 下的 10 个课程 PDF 转换并整理为 Markdown。
tags:
  - pdf
  - markdown
  - courseware
---

# Current Snapshot

- workflow id: 20260523-7c2a-course-pdf-to-md
- current status: 已完成
- current goal: 将 `/home/loviya/下载/课件` 下的 PDF 整理成 Markdown。
- current blocker: none
- next step: none
- tags: pdf, markdown, courseware
- summary: 已将 10 个 PDF 转换为 Markdown，输出到 `/home/loviya/下载/课件/md/`，并生成 `INDEX.md`。抽样验证文件头、页分隔和正文关键文本正常。

# Key Results

- 源目录：`/home/loviya/下载/课件`
- 抽样文件：`01-概述I-0302.pdf`
- 抽样结果：`pdfinfo` 显示 53 页、未加密、PowerPoint 导出；`pdftotext -layout` 能提取中文文本。

# Commands

- `ls -la /home/loviya/下载/课件`
- `pdfinfo .../01-概述I-0302.pdf`
- `pdftotext -layout -f 1 -l 2 .../01-概述I-0302.pdf -`

# Artifacts

- 待创建：`/home/loviya/下载/课件/md/`

# Session Update - 2026-05-23 18:26 +0800

## Key Results

- 输出目录：`/home/loviya/下载/课件/md/`
- 生成文件：10 个 PDF 对应的 `.md`，另有 `INDEX.md` 汇总索引。
- 转换方式：`pdftotext -layout`，每页写为 `## 第 N 页` 并用 `text` 代码块保留课件版式。
- 验证：`find` 确认输出文件存在；`sed` 抽样检查 `01-概述I-0302.md` 和 `05-嵌入式：软件-0316-0318.md` 文件头与正文；`rg` 确认 `01-概述I-0302.md` 有第 1 页和第 53 页分隔。

## Notes

- `pdftotext` 输出过 `Syntax Warning: Invalid Font Weight`，但命令退出成功，抽样文本正常。
- 当前环境 sandbox 因 `/home/loviya/.codex-b/memories/.git` symlink 挂载问题无法执行普通命令，相关文件读取和写入使用了受控 escalation。

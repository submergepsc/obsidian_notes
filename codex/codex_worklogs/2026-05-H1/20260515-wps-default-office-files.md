---
id: 20260515-wps-default-office-files
name: Set WPS As Default Office File Opener
slug: wps-default-office-files
cwd: /home/loviya/notes/obsidian_notes/rust/rust-by-practice
summary: 将 WPS Office 设为 PDF、Word 和 PowerPoint MIME 类型的默认打开方式。
tags:
  - system
  - wps
  - mime
priority: normal
---

# Set WPS As 默认 Office File Opener

## 当前快照

- 状态: 已完成
- 目标: 让 PDF、Word 和 PowerPoint 文件默认用 WPS 打开。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-15 15:18:03 +0800

## 关键结果

- Used `wps-office-prometheus.desktop` as the WPS desktop entry.
- 已更新 common PDF, Word, and PowerPoint MIME defaults through `xdg-mime default`.
- Verified `application/pdf`, `application/msword`, DOCX, `application/vnd.ms-powerpoint`, and PPTX all resolve to `wps-office-prometheus.desktop`.

## Set Office File Defaults To WPS

- 更新时间: 2026-05-15 15:18:03 +0800
- 工作目录: `/home/loviya/notes/obsidian_notes/rust/rust-by-practice`
- 来源指令: `把pdfpptword默认打开文件是wps`
- 问题:
  - 用户需要 PDF, Word, and PowerPoint files to open 带 WPS by default.
- 改进:
  - Set the relevant MIME associations to `wps-office-prometheus.desktop`.
- 结果:
  - PDF, DOC/DOCX, and PPT/PPTX defaults now point to WPS.
- 下一步:
  - 无

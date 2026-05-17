---
id: 20260515-wps-default-office-files
name: Set WPS As Default Office File Opener
slug: wps-default-office-files
cwd: /home/loviya/notes/obsidian_notes/rust/rust-by-practice
summary: Set WPS Office as the default opener for PDF, Word, and PowerPoint MIME types.
tags:
  - system
  - wps
  - mime
priority: normal
---

# Set WPS As Default Office File Opener

## Current Snapshot

- status: 已完成
- goal: Make PDF, Word, and PowerPoint files open with WPS by default.
- blocker: none
- next: none
- updated: 2026-05-15 15:18:03 +0800

## Key Results

- Used `wps-office-prometheus.desktop` as the WPS desktop entry.
- Updated common PDF, Word, and PowerPoint MIME defaults through `xdg-mime default`.
- Verified `application/pdf`, `application/msword`, DOCX, `application/vnd.ms-powerpoint`, and PPTX all resolve to `wps-office-prometheus.desktop`.

## Set Office File Defaults To WPS

- updated: 2026-05-15 15:18:03 +0800
- cwd: `/home/loviya/notes/obsidian_notes/rust/rust-by-practice`
- source instruction: `把pdfpptword默认打开文件是wps`
- problem:
  - The user wanted PDF, Word, and PowerPoint files to open with WPS by default.
- improvement:
  - Set the relevant MIME associations to `wps-office-prometheus.desktop`.
- result:
  - PDF, DOC/DOCX, and PPT/PPTX defaults now point to WPS.
- next:
  - none

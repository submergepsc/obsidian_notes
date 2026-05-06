---
id: 20260506-move-windows-code-home
name: move-windows-code-home
slug: move-windows-code-home
cwd: /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults
summary: Copied and verified Windows Desktop code folder at /home/loviya/code; source deletion is pending because active processes and NTFS/FUSE deletion state kept the old tree visible.
tags:
  - filesystem
  - migration
  - windows-c
priority: normal
---

# Move Windows Code Folder Home

## Current Snapshot

- status: 待继续
- goal: Move `C:/Users/15056/Desktop/code` to `~/code`.
- blocker: Old Windows path is still held open by Nautilus, VS Code, tmux/bash, and the current Codex process; NTFS/FUSE reports delete/rename success inconsistently but leaves entries visible.
- next: Close VS Code/Nautilus/old tmux shells that are rooted under `/media/loviya/Windows-C/Users/15056/Desktop/code`, restart Codex from `/home/loviya/code/RWAExpResults`, then remove `/media/loviya/Windows-C/Users/15056/Desktop/code` or delete it from Windows Explorer.
- updated: 2026-05-06 23:30:43 +0800

## Key Results

- Destination `/home/loviya/code` was created by moving/copying the old Windows Desktop `code` folder.
- `rsync -a` reported zero files transferred after the initial `mv`, indicating the destination matched the source by size/timestamp.
- `rsync -a --checksum --dry-run --itemize-changes` produced no output, indicating no remaining content differences.
- Source cleanup is not complete: `rm -rf` and `find -delete` hit many `Directory not empty` errors on the NTFS/FUSE mount.
- `lsof +D` showed active processes still using the old path, including Nautilus, VS Code language servers, tmux/bash sessions, and the current Codex process.

## Commands

- `mv /media/loviya/Windows-C/Users/15056/Desktop/code /home/loviya/code`
- `rsync -a --info=stats2 /media/loviya/Windows-C/Users/15056/Desktop/code/ /home/loviya/code/`
- `rsync -a --checksum --dry-run --itemize-changes /media/loviya/Windows-C/Users/15056/Desktop/code/ /home/loviya/code/`
- `lsof +D /media/loviya/Windows-C/Users/15056/Desktop/code`

## Code Folder Migration

- updated: 2026-05-06 23:30:43 +0800
- cwd: `/media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- source instruction: `这样子吧,把C://users/15056/desktop/code整个文件夹搬到~下面去`
- problem:
  - The user wanted to move the Windows Desktop code folder into the Linux home directory to avoid Windows-C permission/mount friction.
- improvement:
  - Created and verified the Linux-side working copy at `/home/loviya/code`.
- result:
  - Use `/home/loviya/code/RWAExpResults` as the project path going forward.
- next:
  - Close old-path processes and remove the remaining Windows-side source directory once no process is holding it open.

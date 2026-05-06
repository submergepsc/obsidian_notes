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
- blocker: Current Codex is now running from `/home/loviya/code/RWAExpResults` on ext4, but the old Windows-side source path still exists and VS Code PID 24043 is still launched with `/media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`.
- next: Close or reopen the old-path VS Code window against `/home/loviya/code/RWAExpResults`, then remove `/media/loviya/Windows-C/Users/15056/Desktop/code` or delete it from Windows Explorer once no process is rooted there.
- updated: 2026-05-07 00:17:35 +0800

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

## Status Check From New Linux Path

- updated: 2026-05-07 00:17:35 +0800
- cwd: `/home/loviya/code/RWAExpResults`
- source instruction: `status`
- problem:
  - The workflow needed a current-state check after restarting from the Linux-side project path.
- result:
  - `/home/loviya/code/RWAExpResults` is on writable ext4.
  - `/media/loviya/Windows-C/Users/15056/Desktop/code` still exists.
  - The real user process list still shows VS Code PID 24043 opened with `/media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`.
- next:
  - Close or reopen that VS Code window on `/home/loviya/code/RWAExpResults`, then retry deleting the old Windows-side `code` directory.

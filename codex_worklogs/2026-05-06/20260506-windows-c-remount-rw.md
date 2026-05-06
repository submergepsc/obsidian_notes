---
id: 20260506-windows-c-remount-rw
name: windows-c-remount-rw
slug: windows-c-remount-rw
cwd: /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults
summary: Fixed VS Code save failure caused by Windows-C being mounted read-only, not by per-file chmod permissions.
tags:
  - filesystem
  - windows-c
  - permissions
priority: normal
---

# Windows-C Remount RW

## Current Snapshot

- status: 已完成
- goal: 解决 `plot_3_throught.py` 保存失败，错误为 EROFS read-only file system。
- blocker: 无。
- next: 无。
- updated: 2026-05-06 23:20:00 +0800

## Key Results

- The target directory already had `drwxrwxrwx` permissions, and `plot_3_throught.py` already had `-rwxrwxrwx` permissions.
- The real cause was `/media/loviya/Windows-C` mounted as read-only: `fuseblk ro`.
- Ran `sudo -n mount -o remount,rw /media/loviya/Windows-C`.
- Verified the mount changed to `fuseblk rw` and the target directory is writable.

## Commands

- `findmnt -T /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- `ls -ld /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- `sudo -n mount -o remount,rw /media/loviya/Windows-C`
- `test -w /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- `ls -l /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults/plot_3_throught.py`

## EROFS Save Failure Was A Mount State Issue

- updated: 2026-05-06 23:20:00 +0800
- cwd: `/media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- source instruction: `未能保存“plot_3_throught.py”... EROFS read-only file system ... 给所有文件添加一个权限`
- problem:
  - VS Code could not save a file under the Windows-C mounted partition.
  - The user asked to add permissions to all files, but the error was from the filesystem being mounted read-only.
- improvement:
  - Remounted `/media/loviya/Windows-C` as read-write instead of changing already-open permissions.
- result:
  - The partition now reports `rw`, and the file/directory permissions are writable.
- next:
  - 无。

---
id: 20260506-windows-c-remount-rw
name: windows-c-remount-rw
slug: windows-c-remount-rw
cwd: /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults
summary: 已修复 VS Code save failure caused by Windows-C being mounted read-only, not by per-file chmod permissions.
tags:
  - filesystem
  - windows-c
  - permissions
priority: normal
---

# Windows-C Remount RW

## 当前快照

- 状态: 已完成
- 目标: 解决 `plot_3_throught.py` 保存失败，错误为 EROFS read-only file system。
- 阻塞: 无。
- 下一步: 无。
- 更新时间: 2026-05-06 23:20:00 +0800

## 关键结果

- The target directory already had `drwxrwxrwx` permissions, and `plot_3_throught.py` already had `-rwxrwxrwx` permissions.
- The real cause was `/media/loviya/Windows-C` mounted as read-only: `fuseblk ro`.
- Ran `sudo -n mount -o remount,rw /media/loviya/Windows-C`.
- Verified the mount changed to `fuseblk rw` and the target directory is writable.

## 命令

- `findmnt -T /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- `ls -ld /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- `sudo -n mount -o remount,rw /media/loviya/Windows-C`
- `test -w /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- `ls -l /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults/plot_3_throught.py`

## EROFS Save Failure Was A Mount 状态 Issue

- 更新时间: 2026-05-06 23:20:00 +0800
- 工作目录: `/media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- 来源指令: `未能保存“plot_3_throught.py”... EROFS read-only file system ... 给所有文件添加一个权限`
- 问题:
  - VS Code could not save a file under the Windows-C mounted partition.
  - 用户询问 to add permissions to all files, but the error was from the filesystem being mounted read-only.
- 改进:
  - Remounted `/media/loviya/Windows-C` as read-write 而不是 changing already-open permissions.
- 结果:
  - The partition now reports `rw`, and the file/directory permissions are writable.
- 下一步:
  - 无。

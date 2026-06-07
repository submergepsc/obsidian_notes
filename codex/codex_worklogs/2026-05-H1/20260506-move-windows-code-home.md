---
id: 20260506-move-windows-code-home
name: move-windows-code-home
slug: move-windows-code-home
cwd: /media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults
summary: 已复制并校验 Windows 桌面代码目录到 `/home/loviya/code`；因仍有活动进程和 NTFS/FUSE 删除状态问题，源目录删除仍待处理。
tags:
  - filesystem
  - migration
  - windows-c
priority: normal
---

# Move Windows Code Folder Home

## 当前快照

- 状态: 待继续
- 目标: 将 `C:/Users/15056/Desktop/code` 移到 `~/code`。
- 阻塞: Current Codex is now running from `/home/loviya/code/RWAExpResults` on ext4, but the old Windows-side source path still exists and VS Code PID 24043 is still launched 带 `/media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`.
- 下一步: Close or reopen the old-path VS Code window against `/home/loviya/code/RWAExpResults`, then remove `/media/loviya/Windows-C/Users/15056/Desktop/code` or delete it from Windows Explorer once no process is rooted there.
- 更新时间: 2026-05-07 00:17:35 +0800

## 关键结果

- Destination `/home/loviya/code` was created by moving/copying the old Windows Desktop `code` folder.
- `rsync -a` reported zero files transferred after the initial `mv`, indicating the destination matched the source by size/timestamp.
- `rsync -a --checksum --dry-run --itemize-changes` produced no output, indicating no remaining content differences.
- Source cleanup is not complete: `rm -rf` and `find -delete` hit many `Directory not empty` errors on the NTFS/FUSE mount.
- `lsof +D` showed active processes still 使用 the old path, including Nautilus, VS Code language servers, tmux/bash sessions, and the current Codex process.

## 命令

- `mv /media/loviya/Windows-C/Users/15056/Desktop/code /home/loviya/code`
- `rsync -a --info=stats2 /media/loviya/Windows-C/Users/15056/Desktop/code/ /home/loviya/code/`
- `rsync -a --checksum --dry-run --itemize-changes /media/loviya/Windows-C/Users/15056/Desktop/code/ /home/loviya/code/`
- `lsof +D /media/loviya/Windows-C/Users/15056/Desktop/code`

## Code Folder 迁移

- 更新时间: 2026-05-06 23:30:43 +0800
- 工作目录: `/media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`
- 来源指令: `这样子吧,把C://users/15056/desktop/code整个文件夹搬到~下面去`
- 问题:
  - 用户需要 to move the Windows Desktop code folder into the Linux home directory to avoid Windows-C permission/mount friction.
- 改进:
  - 已创建 and verified the Linux-side working copy at `/home/loviya/code`.
- 结果:
  - 使用`/home/loviya/code/RWAExpResults` as the project path going forward.
- 下一步:
  - Close old-path processes and remove the remaining Windows-side source directory once no process is holding it open.

## 状态 检查 From New Linux Path

- 更新时间: 2026-05-07 00:17:35 +0800
- 工作目录: `/home/loviya/code/RWAExpResults`
- 来源指令: `status`
- 问题:
  - The workflow needed a current-state check after restarting from the Linux-side project path.
- 结果:
  - `/home/loviya/code/RWAExpResults` is on writable ext4.
  - `/media/loviya/Windows-C/Users/15056/Desktop/code` still exists.
  - The real user process list still shows VS Code PID 24043 opened 带 `/media/loviya/Windows-C/Users/15056/Desktop/code/RWAExpResults`.
- 下一步:
  - Close or reopen that VS Code window on `/home/loviya/code/RWAExpResults`, then retry deleting the old Windows-side `code` directory.

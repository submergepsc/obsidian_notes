---
id: 20260501-watt-toolkit-cleanup
name: watt-toolkit-cleanup
slug: watt-toolkit-cleanup
cwd: /home/loviya
summary: 检查and remove local Watt Toolkit / Steam++ remnants.
tags:
  - system-cleanup
  - watt-toolkit
priority: normal
---

# Watt Toolkit 清理

## 当前快照

- 状态: 已完成
- 目标: 清理旧 Watt Toolkit / Steam++ 残留，并按官方安装命令保留新的 Watt Toolkit 安装。
- 阻塞: 无
- 下一步: 无。
- 更新时间: 2026-05-01 19:05:00 +0800

## 关键结果

- 已删除 `/home/loviya/WattToolkit`，约 284M。
- 已删除 `/home/loviya/.local/share/Steam++`，约 368K。
- 已删除 `/home/loviya/.cache/Steam++`，约 3.7M。
- 已删除浏览器 NSS 证书库中的 `SteamTools` 证书。
- 复查未发现 apt/dpkg/snap 包、用户级 systemd unit、常见系统 CA 路径或进程残留。
- GNOME 代理仍为 `manual` 且指向 `127.0.0.1:7897`；没有证据表明该代理属于 Watt Toolkit，因此未修改。
- 用户随后运行 `curl -sSL https://steampp.net/Install/Linux.sh | bash`，重新生成了 `/home/loviya/WattToolkit`；已再次删除并复查无命中。
- 按官方安装命令路径再次复查，未发现重新安装残留。
- 用户明确目标是删除旧下载并重新下载新的 Watt Toolkit；已保留新安装于 `/home/loviya/WattToolkit`。

## 决策

- 只清理能够明确归属 Watt Toolkit / Steam++ 的路径，避免误删无关网络或证书配置。

## 检查And Remove Watt Toolkit Remnants

- 更新时间: 2026-05-01 18:10:52 +0800
- 工作目录: `/home/loviya`
- 来源指令: `检查一下本地的watttoolkit残留并且清楚`
- 问题:
  - 用户需要确认本机是否仍有 Watt Toolkit / Steam++ 残留，并清理明确相关内容。
- 改进:
  - 建立独立 workflow 记录扫描、清理目标和剩余风险。
- 结果:
  - 清理了完整安装目录、用户数据目录、缓存目录和 NSS 证书。
  - 清理后复查未发现明确 Watt Toolkit / Steam++ 残留。
- 下一步:
  - 无。

## Reclean After Installer Was Run Again

- 更新时间: 2026-05-01 18:35:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `curl -sSL https://steampp.net/Install/Linux.sh | bash ... 正在校验安装包`
- 问题:
  - 官方安装脚本被重新运行，重新创建了 `/home/loviya/WattToolkit` 和安装包内容。
- 改进:
  - 检查安装进程、Watt Toolkit 路径和 NSS 证书库后，删除重新生成的安装目录和可能的用户数据/缓存路径。
- 结果:
  - `/home/loviya/WattToolkit`、`~/.local/share/Steam++`、`~/.cache/Steam++`、`~/.cache/Steam+` 和桌面入口均已清理。
  - 复查 `find`、进程列表和 NSS 证书库均无 Watt Toolkit / Steam++ / SteamTools 命中。
- 下一步:
  - 无。

## Verify Official 安装 命令 Leaves No Current Remnants

- 更新时间: 2026-05-01 18:40:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `这是我重新安装的,你检测一下,curl -sSL https://steampp.net/Install/Linux.sh | bash用这个命令下载的`
- 问题:
  - 用户说明 Watt Toolkit 是通过官方 `curl -sSL https://steampp.net/Install/Linux.sh | bash` 命令重新安装，需要按该来源确认当前残留。
- 改进:
  - 复查官方脚本会创建的 `/home/loviya/WattToolkit`、`~/.local/share/Steam++`、`~/.cache/Steam++`、桌面入口、NSS `SteamTools` 证书、进程和用户级 systemd。
- 结果:
  - 当前没有安装目录、用户数据、缓存、桌面入口、NSS 证书、进程或用户级 systemd 残留。
  - GNOME 代理仍为 `127.0.0.1:7897`，它是安装脚本下载时使用的现有代理，不是本次检测到的 Watt Toolkit 文件残留。
- 下一步:
  - 无。

## Keep New Watt Toolkit 下载 And 安装

- 更新时间: 2026-05-01 19:05:00 +0800
- 工作目录: `/home/loviya`
- 来源指令: `老子是要删掉以前下载的...现在我要下载新的啊` / `curl -sSL https://steampp.net/Install/Linux.sh | bash`
- 问题:
  - 之前误把用户重新下载的新 Watt Toolkit 当作残留清理。用户实际目标是清理旧文件后保留新的下载/安装。
- 改进:
  - 重新运行官方安装命令下载 `WattToolkit.tgz`，校验 SHA384 与 `WattToolkit.AppVer` 中的官方值一致。
  - 官方脚本被 `zenity` 桌面入口选择框卡住，因此停止卡住的脚本，直接解压已校验的安装包。
  - 创建 `/home/loviya/.local/share/applications/Watt Toolkit.desktop` 指向 `/home/loviya/WattToolkit/Steam++.sh`。
- 结果:
  - 新安装保留在 `/home/loviya/WattToolkit`，大小约 284M。
  - `Steam++.sh`、内置 `dotnet`、`assemblies/Steam++.dll`、图标和 `AppVer` 均存在。
  - 卡住的安装脚本和 `zenity` 弹窗已停止。
- 下一步:
  - 用户可从应用菜单启动 Watt Toolkit，或执行 `/home/loviya/WattToolkit/Steam++.sh`。

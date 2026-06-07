---
id: 20260602-packettracer-deb-extract
name: Packet Tracer deb 用户级解压
slug: packettracer-deb-extract
cwd: /home/loviya
summary: 将 /home/loviya/下载/CiscoPacketTracer_900_Ubuntu_64bit.deb 解压到用户目录下的应用位置，不做系统级安装。
tags:
  - local-file
  - packettracer
  - deb
---

# Packet Tracer deb 用户级解压

## Current Snapshot

- workflow id: 20260602-packettracer-deb-extract
- current status: 已完成
- current goal: 解压 `/home/loviya/下载/CiscoPacketTracer_900_Ubuntu_64bit.deb` 到合适的用户级位置
- current blocker: 无
- next step: none
- tags: local-file, packettracer, deb
- summary: deb 已解压到 `/home/loviya/Applications/PacketTracer-9.0/`，输出 AppImage 位于 `/home/loviya/Applications/PacketTracer-9.0/opt/pt/packettracer.AppImage`。

## Commands

- `dpkg-deb -I /home/loviya/下载/CiscoPacketTracer_900_Ubuntu_64bit.deb`: 确认包名、版本、架构和依赖。
- `dpkg-deb -c /home/loviya/下载/CiscoPacketTracer_900_Ubuntu_64bit.deb`: 确认内部主要文件为 `./opt/pt/packettracer.AppImage`。

## Decisions

- 不直接写入系统 `/opt/pt`，避免把“解压”变成系统安装。
- 选用用户目录 `/home/loviya/Applications/PacketTracer-9.0/` 作为 AppImage 解压位置。

## Key Results

- 解压目标目录：`/home/loviya/Applications/PacketTracer-9.0/`
- 主程序路径：`/home/loviya/Applications/PacketTracer-9.0/opt/pt/packettracer.AppImage`
- 验证结果：AppImage 存在，权限为 `-rwxr-xr-x`，大小约 376M；目录大小约 376M。

## Artifacts

- `/home/loviya/Applications/PacketTracer-9.0/opt/pt/packettracer.AppImage`

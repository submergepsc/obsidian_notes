---
id: 20260518-aarch64-dynamic-direct-run
name: AArch64 动态程序直接运行配置
slug: aarch64-dynamic-direct-run
cwd: /home/loviya
summary: 配置本机让 aarch64-linux-gnu-gcc 生成的动态链接 AArch64 程序可以直接 ./hello 运行。
tags:
  - aarch64
  - qemu
  - binfmt
  - cross-compile
---

# AArch64 动态程序直接运行配置

## Current Snapshot

- workflow id: `20260518-aarch64-dynamic-direct-run`
- current status: `已完成`
- current goal: 让 `aarch64-linux-gnu-gcc -o hello hello.c` 生成的动态链接 ARM64 程序无需 `-static`、无需运行时额外参数即可 `./hello` 执行。
- current blocker: 无。
- next step: 无。
- tags: `aarch64`, `qemu`, `binfmt`, `cross-compile`
- summary: 已配置 Ubuntu arm64 apt 源、安装 `libc6:arm64` 与 `qemu-user-binfmt`；动态链接 AArch64 程序可直接 `./hello` 运行并输出 `hello world!`。

## Key Results

- 新增 `/etc/apt/sources.list.d/ubuntu-ports-arm64.sources`，让 `arm64` 包走 `http://ports.ubuntu.com/ubuntu-ports`。
- 修改 `/etc/apt/sources.list.d/ubuntu.sources`，把原 Ubuntu 源限制为 `amd64 i386`，避免向 `cn.archive.ubuntu.com` / `security.ubuntu.com` 请求不存在的 arm64 包。
- 备份原文件到 `/etc/apt/sources.list.d/ubuntu.sources.codex-backup-20260519-0046`。
- 安装 `libc6:arm64` 与 `qemu-user-binfmt`；`/lib/ld-linux-aarch64.so.1` 现在存在，并指向 `aarch64-linux-gnu/ld-linux-aarch64.so.1`。
- 安装 `qemu-user-binfmt` 时 apt 移除了 `qemu-user-static`，这是包冲突替换；当前 `qemu-user` 与 `qemu-user-binfmt` 均已安装。
- 用户要求写入 notes；已沉淀到 `codex_notes/requested/2026-05-18-aarch64-dynamic-direct-run.md`，并更新 notes 全局索引与 requested 索引。

## Commands

- `ls -l /lib/ld-linux-aarch64.so.1 /usr/aarch64-linux-gnu/lib/ld-linux-aarch64.so.1`
  - 结果：系统根目录 loader 缺失，cross sysroot loader 存在。
- `dpkg -l qemu-user-binfmt qemu-user libc6-arm64-cross gcc-aarch64-linux-gnu crossbuild-essential-arm64 libc6:arm64`
  - 结果：`qemu-user`、交叉编译工具链和 `libc6-arm64-cross` 已安装；`qemu-user-binfmt` 与 `libc6:arm64` 未安装。
- `sudo apt-get update`
  - 初次失败：默认源请求 arm64 包返回 404。
  - 修改 apt 源后成功：arm64 包从 `ports.ubuntu.com` 获取。
- `sudo apt-get install -y qemu-user-binfmt libc6:arm64`
  - 成功；附带安装 `gcc-14-base:arm64`、`libgcc-s1:arm64`、`libunistring5:arm64`、`libidn2-0:arm64`。
- 在 `/home/loviya/notes/obsidian_notes/25_2/os/class/compile` 中运行 `aarch64-linux-gnu-gcc -o hello hello.c` 成功。
- `file hello`
  - 结果：`ELF 64-bit LSB pie executable, ARM aarch64, dynamically linked, interpreter /lib/ld-linux-aarch64.so.1`。
- `readelf -l hello`
  - 结果：interpreter 为 `/lib/ld-linux-aarch64.so.1`。
- `./hello`
  - 结果：输出 `hello world!`。

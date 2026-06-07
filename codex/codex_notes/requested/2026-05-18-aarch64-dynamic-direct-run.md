---
title: AArch64 动态链接程序直接运行配置
date: 2026-05-18
requested_by_user: true
importance: user-requested
review_priority: high
tags:
  - user-requested
  - important
  - aarch64
  - qemu
  - binfmt
  - cross-compile
source_worklog: 20260518-aarch64-dynamic-direct-run
---

# AArch64 动态链接程序直接运行配置

目标：让 `aarch64-linux-gnu-gcc -o hello hello.c` 编译出的动态链接 AArch64 程序，在 x86_64 Ubuntu 主机上可以直接：

```sh
./hello
```

不需要 `-static`，也不需要运行时手写 `qemu-aarch64 -L ...`。

## 结论

仅安装 `crossbuild-essential-arm64 gcc-aarch64-linux-gnu` 通常只保证能交叉编译，不保证系统根目录里有 ARM64 动态 loader。

直接执行动态链接 AArch64 ELF 时，程序里的 interpreter 是：

```text
/lib/ld-linux-aarch64.so.1
```
	
因此系统需要同时具备：

- ARM64 libc runtime：`libc6:arm64`
- binfmt 注册：`qemu-user-binfmt`
- 可用的 `/lib/ld-linux-aarch64.so.1`

## Apt 源配置

Ubuntu 的 `arm64` 包应从 ports 源获取。当前配置：

```text
/etc/apt/sources.list.d/ubuntu-ports-arm64.sources
```

内容形态：

```text
Types: deb
URIs: http://ports.ubuntu.com/ubuntu-ports
Suites: noble noble-updates noble-backports noble-security
Components: main restricted universe multiverse
Architectures: arm64
Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
```

原 Ubuntu 源限制为本机架构，避免向 `cn.archive.ubuntu.com` / `security.ubuntu.com` 请求不存在的 arm64 包：

```text
Architectures: amd64 i386
```

原文件备份：

```text
/etc/apt/sources.list.d/ubuntu.sources.codex-backup-20260519-0046
```

## 安装命令

```sh
sudo apt-get update
sudo apt-get install -y qemu-user-binfmt libc6:arm64
```

安装完成后，关键状态应类似：

```sh
ls -l /lib/ld-linux-aarch64.so.1
```

输出应显示它存在，例如：

```text
/lib/ld-linux-aarch64.so.1 -> aarch64-linux-gnu/ld-linux-aarch64.so.1
```

## 验证

在示例目录：

```sh
cd /home/loviya/notes/obsidian_notes/25_2/os/class/compile
aarch64-linux-gnu-gcc -o hello hello.c
file hello
readelf -l hello | grep interpreter
./hello
```

期望：

```text
ARM aarch64, dynamically linked, interpreter /lib/ld-linux-aarch64.so.1
```

并且：

```text
hello world!
```

## 注意

本次安装 `qemu-user-binfmt` 时，apt 移除了 `qemu-user-static`。这是 Ubuntu 包之间的替换关系；当前目标是通过 binfmt 调用动态 QEMU 用户态解释器来直接运行 `./hello`。


---
id: 20260508-view-os-directory
name: OS Homework Quick Tasks
slug: os-homework-quick-tasks
cwd: /home/loviya/notes/obsidian_notes/homework/os
summary: Handled OS homework directory, compile, data-race, and AArch64 cross-compiler setup tasks.
tags:
  - homework
  - os
  - compile
priority: normal
---

# OS Homework Quick Tasks

## Current Snapshot

- status: 已完成
- goal: 查看目录、编译原子操作示例、复现实验，并配置 AArch64 交叉编译工具。
- blocker: none
- next: none
- updated: 2026-05-08 21:06:00 +0800

## Key Results

- 当前目录解析为 `/home/loviya/obnotes/homework/os`。
- 目录中包含 C 源文件：`atomic.c`、`_atomic.c`、`_atomic_sync.c`。
- 目录中包含实验文档：`第九周实验：原子操作与互斥锁.docx`、`第九周实验：原子操作与互斥锁.md`。
- `media/` 下有 `image1.png` 到 `image5.png`。
- `atomic_exchange.c` 已通过 `g++ atomic_exchange.c -lpthread -o atomic` 编译为 `atomic`。
- 已按实验任务 1.1 创建并运行 `counter_naive.c`，比较 `-O0` 与 `-O2` 的数据竞争表现。
- 已安装 `gcc-aarch64-linux-gnu` 与 `binutils-aarch64-linux-gnu`，`aarch64-linux-gnu-gcc -O2 -S counter_atomic.c -o counter_atomic.s` 可正常生成 AArch64 汇编。

## 查看 OS 作业目录

- updated: 2026-05-08 19:59:28 +0800
- cwd: `/home/loviya/notes/obsidian_notes/homework/os`
- source instruction: `查看目录`
- problem:
  - 用户需要快速了解当前目录文件。
- result:
  - 已运行 `pwd`、`ls -la` 和 `find . -maxdepth 2 -type f | sort` 查看目录与文件清单。
- next:
  - none

## 安装 AArch64 交叉编译器

- updated: 2026-05-08 21:06:00 +0800
- cwd: `/home/loviya/notes/obsidian_notes/homework/os/task2`
- source instruction: `找不到命令 “aarch64-linux-gnu-gcc” ... 解决这个问题`
- problem:
  - 在 `task2` 目录运行 `aarch64-linux-gnu-gcc -O2 -S counter_atomic.c -o counter_atomic.s` 失败，系统缺少 AArch64 交叉编译器。
- improvement:
  - 使用 `sudo apt update && sudo apt install -y gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu` 安装工具链。
  - 验证 `aarch64-linux-gnu-gcc` 版本为 Ubuntu 13.3.0 cross compiler，`aarch64-linux-gnu-objdump` 来自 GNU Binutils 2.42。
- result:
  - 命令 `aarch64-linux-gnu-gcc -O2 -S counter_atomic.c -o counter_atomic.s` 已执行成功。
  - 生成文件 `/home/loviya/notes/obsidian_notes/homework/os/task2/counter_atomic.s`。
  - 在汇编中观察到 relaxed atomic add 相关符号 `__aarch64_ldadd8_relax`。
- next:
  - none

## 复现 counter_naive 数据竞争

- updated: 2026-05-08 20:00:16 +0800
- cwd: `/home/loviya/notes/obsidian_notes/homework/os`
- source instruction: `帮我完成这条`
- problem:
  - 需要完成实验任务 1.1：运行 naive counter，比较 `-O0` 与 `-O2` 下丢失更新，并解释 `counter++` 的汇编差异。
- improvement:
  - 新建 `counter_naive.c`，内容与截图中的 pthread 计数示例一致。
  - 编译命令：`gcc -O0 counter_naive.c -pthread -o counter_naive_O0` 与 `gcc -O2 counter_naive.c -pthread -o counter_naive_O2`。
  - 反汇编命令：`objdump -d counter_naive_O0 | sed -n '/<worker>:/,/^$/p'` 和 `objdump -d counter_naive_O2 | sed -n '/<worker>:/,/^$/p'`。
- result:
  - `-O0` 下运行 `./counter_naive_O0 4 1000000` 五次，最终 `counter` 不同，丢失更新数量不一致。
  - `-O2` 下运行 `./counter_naive_O2 4 1000000` 五次，观察到 `counter = 4000000, lost = 0`；用 `64 1000000` 复测十次也观察到 `lost = 0`。
  - `-O0` 的 `counter++` 反汇编为 load/add/store 三步，多个线程可交错覆盖。
  - `-O2` 将循环优化成每个线程一次 `add %rax, counter`，竞争窗口从每次循环一次缩小到每线程一次；本机观察结果没有丢失，但数据竞争仍是未定义行为，不能依赖。
- next:
  - none

## 编译 atomic_exchange 示例

- updated: 2026-05-08 20:00:16 +0800
- cwd: `/home/loviya/notes/obsidian_notes/homework/os`
- source instruction: `g++ -lpthread atomic_exchange.cpp -o atomic帮我编译一下这个文件`
- problem:
  - 用户需要编译当前目录中的 atomic exchange 示例。
  - 当前目录存在 `atomic_exchange.c`，没有 `atomic_exchange.cpp`。
- result:
  - 已使用 `g++ atomic_exchange.c -lpthread -o atomic` 编译成功。
  - 生成的 `atomic` 是 x86-64 Linux ELF 可执行文件。
- next:
  - none

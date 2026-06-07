title: "第二周实验：Linux 常用命令与 ARM 汇编语言"
source: https://ycnw11in464y.feishu.cn/wiki/JC4qwwvWtiaXV0k15wvc5Dcln8I
wiki_token: JC4qwwvWtiaXV0k15wvc5Dcln8I
obj_token: UM9bd2YvZoUAqtxS3u6cLRlQnxh
rewritten_by: codex-ds
created: 2026-05-15
tags:
  - linux
  - arm
  - assembly
  - lab
# 第二周实验：Linux 常用命令与 ARM 汇编语言
## 目录
- [实验概览](#实验概览)
- [一、Linux 常用命令](#一linux-常用命令)
- [二、文本处理与查找](#二文本处理与查找)
- [三、系统信息与网络](#三系统信息与网络)
- [四、压缩归档与权限管理](#四压缩归档与权限管理)
- [五、软件包管理](#五软件包管理)
- [六、从 C 到汇编（x86-64）](#六从-c-到汇编x86-64)
- [七、交叉编译与 ARM64 汇编](#七交叉编译与-arm64-汇编)
- [八、指令集对比：CISC vs RISC](#八指令集对比cisc-vs-risc)
- [九、推荐实验流程](#九推荐实验流程)
- [十、常见问题与排错](#十常见问题与排错)
- [十一、实验报告建议](#十一实验报告建议)
- [附：命令速查表](#附命令速查表)
## 实验概览
### 实验目标
1. **Linux 命令基础** — 掌握文件操作、文本处理、系统查看、网络工具、压缩归档等日常命令。
2. **汇编语言入门** — 理解 C 语言函数如何被编译为汇编代码，对比 **x86-64 (CISC)** 与 **ARM64/AArch64 (RISC)** 的指令风格。
### 学完应能回答
- 如何在终端里创建、复制、移动、删除文件和目录？
- 如何查看系统资源（CPU、内存、磁盘）和进程信息？
- `gcc -S`、`objdump -d`、`file` 各有什么用途？
- 为什么 x86 机器上编译 ARM 程序需要交叉编译工具链？
- AArch64 中的 `w0`/`w1`/`x0`/`x1` 寄存器大致对应什么？
- CISC 和 RISC 在指令长度和设计理念上有什么区别？
### 实验环境
| 项目 | 建议 |
| --- | --- |
| 操作系统 | Ubuntu 22.04 / 24.04 或其它 Debian 系 Linux |
| 终端 | GNOME Terminal、Konsole、Windows Terminal + WSL |
| 文本编辑器 | `nano`、`vim`、VS Code |
| 本地编译器 | `gcc` + `build-essential` |
| 交叉编译器 | `gcc-aarch64-linux-gnu` |
| 反汇编工具 | `objdump`、`aarch64-linux-gnu-objdump` |

```bash
# 快速检查环境
uname -a
gcc --version
objdump --version
```
### 安装依赖
```bash
sudo apt update
sudo apt install build-essential binutils
# ARM64 交叉编译工具（按需安装）
sudo apt install crossbuild-essential-arm64 gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu
```
> [!note] 如果 `apt install` 报错，先运行 `sudo apt update` 刷新源索引，再重试。
## 一、Linux 常用命令
### 命令基本格式
```bash
命令 [选项...] [参数...]
```
例如 `ls -lah /home` 中 `ls` 是命令，`-lah` 是选项，`/home` 是参数。
### 1.1 文件与目录操作
| 命令 | 用途 | 常用示例 |
| --- | --- | --- |
| `pwd` | 显示当前工作路径 | `pwd` |
| `ls` | 列出目录内容 | `ls -l`、`ls -a`、`ls -lah` |
| `cd` | 切换目录 | `cd /tmp`、`cd ..`、`cd ~`、`cd -` |
| `mkdir` | 创建目录 | `mkdir test`、`mkdir -p a/b/c` |
| `touch` | 创建空文件 / 更新修改时间 | `touch note.txt` |
| `cp` | 复制文件或目录 | `cp a.txt b.txt`、`cp -r src/ dst/` |
| `mv` | 移动或重命名 | `mv old.txt new.txt`、`mv f.txt /tmp/` |
| `rm` | 删除文件或目录 | `rm f.txt`、`rm -rf dir/` |
| `cat` | 查看文件全部内容 | `cat file.txt` |
| `less` | 分页浏览（支持上下翻页） | `less long.log`（按 `q` 退出） |
| `head` | 查看文件开头部分 | `head -n 20 file.txt` |
| `tail` | 查看文件末尾部分 | `tail -f app.log`（实时追踪日志） |

> [!warning] `rm` 删除不经过回收站。使用 `rm -rf` 前请务必确认路径，避免误删重要数据。
### 1.2 路径速查
| 写法 | 含义 |
| --- | --- |
| `/` | 根目录 |
| `~` | 当前用户家目录 |
| `.` | 当前目录 |
| `..` | 上级目录 |
| `/home/loviya` | 绝对路径示例 |
| `docs/file.txt` | 相对路径示例 |

```bash
cd ~        # 回到家目录
cd -        # 回到上一个目录（来回切换很方便）
cd ../..    # 向上两级
```
### 1.3 综合练习
```bash
mkdir -p ~/linux-lab
cd ~/linux-lab
touch hello.txt
echo "Hello, Linux!" > hello.txt
cat hello.txt
cp hello.txt hello-backup.txt
mv hello-backup.txt renamed.txt
ls -lah
```
## 二、文本处理与查找
### 2.1 文本搜索与编辑
| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `grep` | 搜索包含关键字的行 | `grep "error" app.log` |
| `sed` | 流式文本替换 | `sed 's/foo/bar/g' file.txt` |
| `awk` | 按列处理文本 | `awk '{print $1, $NF}' file.txt` |
| `sort` | 排序 | `sort names.txt` |
| `uniq` | 去重（通常配合 sort） | `sort names.txt | uniq` |
| `cut` | 按分隔符取列 | `cut -d',' -f1,3 data.csv` |
| `wc` | 统计行/词/字符数 | `wc -l file.txt` |
| `diff` | 比较文件差异 | `diff old.txt new.txt` |

#### grep 常用选项
```bash
grep -n "pattern" file      # 显示行号
grep -i "pattern" file      # 忽略大小写
grep -r "pattern" dir/      # 递归搜索目录
grep -v "pattern" file      # 反向匹配（不包含的行）
grep -c "pattern" file      # 只统计匹配行数
```
### 2.2 查找文件与命令
| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `find` | 按名称/类型/时间查找文件 | `find . -name "*.c"` |
| `locate` | 基于数据库快速查找 | `locate passwd` |
| `which` | 显示命令的完整路径 | `which gcc` |
| `type` | 显示命令类型（内建/别名/外部） | `type ls`、`type cd` |

> `find` 功能强大但速度慢（实时扫描），`locate` 速度快但依赖定期更新的数据库（`sudo updatedb`）。
## 三、系统信息与网络
### 3.1 系统资源
| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `uname -a` | 查看内核版本、架构等全部系统信息 | `uname -a` |
| `top` / `htop` | 实时进程监控 | `top`（按 `q` 退出） |
| `ps aux` | 查看所有进程快照 | `ps aux | grep nginx` |
| `free -h` | 查看内存使用（人类可读格式） | `free -h` |
| `df -h` | 查看磁盘分区与使用量 | `df -h` |
| `du -sh` | 统计目录总大小 | `du -sh ~/linux-lab` |
| `uptime` | 系统已运行时间与负载 | `uptime` |
| `dmesg` | 查看内核环形缓冲区消息 | `dmesg | tail -20` |

### 3.2 进程管理
```bash
kill PID              # 正常终止进程
kill -9 PID           # 强制终止（SIGKILL）
kill -15 PID          # 优雅终止（SIGTERM，默认）
pkill process_name    # 按名称杀进程
pgrep process_name    # 按名称查 PID
```
### 3.3 网络命令
| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `ping` | 测试网络连通性 | `ping -c 4 8.8.8.8` |
| `curl` | HTTP 请求 / 文件下载 | `curl -O https://example.com/file.zip` |
| `wget` | 文件下载（支持递归） | `wget https://example.com/file.zip` |
| `ip a` | 查看/配置网络接口（现代） | `ip addr show` |
| `ss -tlnp` | 查看监听端口（取代 netstat） | `ss -tlnp` |
| `ssh` | 远程登录 | `ssh user@192.168.1.100` |
| `scp` | 安全复制到远程主机 | `scp file.txt user@host:/path/` |

> [!tip] `ip` 和 `ss` 是现代 Linux 推荐的工具，逐步取代了旧的 `ifconfig` 和 `netstat`。如果习惯旧工具，可以用 `sudo apt install net-tools` 安装。
## 四、压缩归档与权限管理
### 4.1 压缩与归档
| 格式 | 创建 | 解压 |
| --- | --- | --- |
| `.tar.gz` | `tar -czvf archive.tar.gz dir/` | `tar -xzvf archive.tar.gz` |
| `.tar.bz2` | `tar -cjvf archive.tar.bz2 dir/` | `tar -xjvf archive.tar.bz2` |
| `.zip` | `zip -r archive.zip dir/` | `unzip archive.zip` |
| `.gz` | `gzip file` | `gunzip file.gz` |

```bash
# tar 选项速记
# c — 创建归档
# x — 解压
# z — gzip 压缩
# j — bzip2 压缩
# v — 显示处理的文件
# f — 指定文件名
```
### 4.2 文件权限
```bash
chmod 755 script.sh       # rwxr-xr-x（数字法）
chmod +x script.sh        # 添加可执行权限（符号法）
chmod -R 644 docs/        # 递归修改目录下所有文件
chown user:group file.txt # 修改文件所有者和组
```
权限数字速记：

| 数字 | 权限 | 二进制 |
| --- | --- | --- |
| 7 | rwx（读+写+执行） | 111 |
| 6 | rw-（读+写） | 110 |
| 5 | r-x（读+执行） | 101 |
| 4 | r--（只读） | 100 |
| 0 | ---（无权限） | 000 |

## 五、软件包管理
### apt 常用命令
| 命令 | 说明 |
| --- | --- |
| `sudo apt update` | 更新软件包索引 |
| `sudo apt upgrade` | 升级所有可更新的包 |
| `sudo apt install <pkg>` | 安装软件包 |
| `sudo apt remove <pkg>` | 卸载软件包 |
| `sudo apt purge <pkg>` | 卸载并清除配置文件 |
| `apt-cache search <keyword>` | 搜索软件包 |
| `apt-cache policy <pkg>` | 查看可用版本 |

## 六、从 C 到汇编（x86-64）
### 6.1 编写 C 函数
```c
// add.c — 不包含 main，只写一个函数
int add(int a, int b)
{
    return a + b;
}
```
### 6.2 编译为汇编
```bash
gcc -S -O1 -o add-x86.s add.c
```
> `-S` 生成汇编文件 `.s`，`-O1` 轻度优化以聚焦核心逻辑。使用 `-O0` 可观察到完整的栈帧结构。
### 6.3 查看汇编代码
```bash
cat add-x86.s
# 或
nano add-x86.s
```
生成的 x86-64 汇编大致为：
```asm
add:
        pushq   %rbp
        movq    %rsp, %rbp
        movl    %edi, -4(%rbp)
        movl    %esi, -8(%rbp)
        movl    -4(%rbp), %eax
        addl    -8(%rbp), %eax
        popq    %rbp
        ret
```
### 6.4 查看目标文件
```bash
gcc -c -O1 -o add-x86.o add.c   # 编译为目标文件
file add-x86.o                   # 查看文件架构信息
objdump -d add-x86.o             # 反汇编
```
`file` 输出示例：
```
add-x86.o: ELF 64-bit LSB relocatable, x86-64, version 1 (SYSV), not stripped
```
## 七、交叉编译与 ARM64 汇编
### 7.1 为什么要交叉编译
- 大多数 PC 是 **x86-64** 架构
- 但手机、嵌入式设备、树莓派等常用 **ARM** 架构
- 在 x86 机器上编译 ARM 程序，称为**交叉编译**
- 需要使用对应架构的工具链，例如 `aarch64-linux-gnu-gcc`
### 7.2 安装 ARM64 交叉编译工具链
```bash
sudo apt install crossbuild-essential-arm64 gcc-aarch64-linux-gnu
```
### 7.3 编译 ARM64 汇编
```bash
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
cat add-arm64.s
```
生成的 ARM64 汇编：
```asm
        .arch armv8-a
        .file   "add.c"
        .text
        .align  2
        .global add
        .type   add, %function
add:
        add     w0, w0, w1
        ret
        .size   add, .-add
        .ident  "GCC: (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0"
        .section        .note.GNU-stack,"",@progbits
```
> 以 `.` 开头的行是汇编器伪指令/元信息，不是真正的 CPU 指令。真正的指令只有 `add w0, w0, w1` 和 `ret`。
### 7.4 查看 ARM64 目标文件
```bash
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
file add-arm64.o
aarch64-linux-gnu-objdump -d add-arm64.o
```
`file` 输出示例：
```
add-arm64.o: ELF 64-bit LSB relocatable, ARM aarch64, version 1 (SYSV), not stripped
```
### 7.5 ARM64 寄存器速记
| 寄存器 | 宽度 | 用途 |
| --- | --- | --- |
| `w0` ~ `w30` | 32 位 | 低 32 位操作（int 类型参数/返回值） |
| `x0` ~ `x30` | 64 位 | 完整 64 位操作（指针、long 类型） |
| `w0` / `x0` | — | 函数返回值 |
| `w0`-`w7` / `x0`-`x7` | — | 函数参数传递 |
| `sp` | 64 位 | 栈指针 |
| `x30` / `lr` | 64 位 | 链接寄存器（函数返回地址） |
| `xzr` | — | 零寄存器（读取恒为 0） |

> 在 `add w0, w0, w1` 中：将 `w0`（第一个参数）与 `w1`（第二个参数）相加，结果写回 `w0`（返回值）。这正是 C 代码 `return a + b;` 的体现。
## 八、指令集对比：CISC vs RISC
### 8.1 核心差异
| 特性 | CISC（x86-64） | RISC（ARM64 / AArch64） |
| --- | --- | --- |
| **全称** | Complex Instruction Set Computer | Reduced Instruction Set Computer |
| **指令长度** | 可变（1~15 字节） | 固定（4 字节） |
| **寄存器数量** | 较少（通用寄存器有限） | 较多（31 个通用寄存器） |
| **指令功能** | 单条指令可完成复杂操作（如内存-内存操作） | 指令简单，通常只做一件事 |
| **寻址模式** | 多种复杂寻址模式 | 寻址模式简洁统一 |
| **典型产品** | Intel / AMD 桌面 CPU | ARM Cortex 系列（手机、嵌入式） |
| **功耗** | 较高 | 较低 |

### 8.2 直观对比：`add` 函数
**x86-64（CISC）** — 需要栈操作、内存传参：
```asm
add:
        pushq   %rbp                # 保存栈基址
        movq    %rsp, %rbp          # 设置栈帧
        movl    %edi, -4(%rbp)      # 参数 a 存入栈
        movl    %esi, -8(%rbp)      # 参数 b 存入栈
        movl    -4(%rbp), %eax      # a 取回寄存器
        addl    -8(%rbp), %eax      # b 从栈取并与 a 相加
        popq    %rbp                # 恢复栈基址
        ret
```
**ARM64 / AArch64（RISC）** — 纯寄存器操作，无须栈帧：
```asm
add:
        add     w0, w0, w1          # w0 = w0 + w1
        ret
```
> ARM64 的简洁性源于其寄存器充裕的设计——参数直接在寄存器中传递，省去了大量内存操作。
## 九、推荐实验流程
建议按以下顺序操作，逻辑最顺畅：
1. **建目录**：`mkdir -p ~/linux-arm-lab/week2 && cd ~/linux-arm-lab/week2`
2. **写 C 文件**：用 `nano` 或 `cat` 创建 `add.c`
3. **生成本地汇编**：`gcc -S -O1 -o add-x86.s add.c`
4. **查看 x86-64 汇编**：`cat add-x86.s`
5. **生成本地目标文件并查看**：`gcc -c -O1 -o add-x86.o add.c && file add-x86.o && objdump -d add-x86.o`
6. **安装交叉编译工具链**：`sudo apt install gcc-aarch64-linux-gnu`
7. **生成 ARM64 汇编**：`aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c`
8. **查看 ARM64 汇编**：`cat add-arm64.s`
9. **生成 ARM64 目标文件并查看**：`aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c && file add-arm64.o && aarch64-linux-gnu-objdump -d add-arm64.o`
10. **对比分析**：对比 `add-x86.s` 和 `add-arm64.s` 的差异
### 完整命令脚本
```bash
#!/bin/bash
set -e
mkdir -p ~/linux-arm-lab/week2
cd ~/linux-arm-lab/week2
# 创建 C 源文件
cat > add.c <<'EOF'
int add(int a, int b)
{
    return a + b;
}
EOF
# x86-64
echo "=== x86-64 ==="
gcc -S -O1 -o add-x86.s add.c
gcc -c -O1 -o add-x86.o add.c
file add-x86.o
objdump -d add-x86.o
echo ""
# ARM64
echo "=== ARM64 (AArch64) ==="
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
file add-arm64.o
aarch64-linux-gnu-objdump -d add-arm64.o
```
## 十、常见问题与排错
### 10.1 `aarch64-linux-gnu-gcc: command not found`
**原因**：交叉编译器未安装。
**解决**：
```bash
sudo apt update
sudo apt install gcc-aarch64-linux-gnu
```
### 10.2 `Permission denied`
**原因**：文件没有可执行权限。
**解决**：
```bash
chmod +x script.sh
./script.sh
```
> 如果访问系统目录报权限不足，先确认是否真的需要修改该目录，不要盲目加 `sudo`。
### 10.3 ARM64 程序无法直接运行
**现象**：
```
cannot execute binary file: Exec format error
```
**原因**：当前机器是 x86-64，目标程序是 ARM64，指令集不兼容。
**解决思路**：
- 只做编译和反汇编，不运行
- 将程序传到 ARM64 设备上运行
- 使用 QEMU 模拟运行
### 10.4 `objdump` 反汇编结果不对
**原因**：用 `objdump`（x86 版本）去解析 ARM64 目标文件。
**解决**：使用交叉工具链中的版本：
```bash
aarch64-linux-gnu-objdump -d add-arm64.o
```
### 10.5 汇编文件中 `.` 开头的行看不懂
```asm
.arch armv8-a
.text
.global add
.type   add, %function
```
这些是**汇编器伪指令**（directives），用于指定架构、段信息、符号导出等。初学阶段可以先只关注真正的 CPU 指令行：
```asm
add     w0, w0, w1
ret
```
## 十一、实验报告建议
实验报告建议包含以下内容：
### 11.1 环境记录
```bash
# 记录当前系统环境
uname -a
gcc --version
aarch64-linux-gnu-gcc --version
```
### 11.2 命令练习记录
- 当前路径：`pwd`
- 实验目录结构
- 创建/查看/复制/移动/删除文件的操作记录
- 使用 `grep`、`find` 等工具的实际例子
### 11.3 汇编代码与输出
```bash
# x86-64 汇编与反汇编
gcc -S -O1 -o add-x86.s add.c
cat add-x86.s
gcc -c -O1 -o add-x86.o add.c
file add-x86.o
objdump -d add-x86.o
# ARM64 汇编与反汇编
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
cat add-arm64.s
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
file add-arm64.o
aarch64-linux-gnu-objdump -d add-arm64.o
```
### 11.4 对比分析结论（示例）
- x86-64 与 AArch64 使用不同的寄存器命名方式：`%rdi`/`%rsi` vs `w0`/`w1`
- x86-64 参数主要通过 `%rdi`、`%rsi`、`%rdx` 等传递，返回值在 `%rax`
- AArch64 参数通过 `w0`-`w7`/`x0`-`x7` 传递，返回值在 `w0`/`x0`
- AArch64 指令固定 4 字节（RISC 特征），x86-64 指令变长（CISC 特征）
- AArch64 寄存器充裕，函数调用中栈操作明显更少
## 附：命令速查表
### 文件目录
```bash
pwd                    # 当前路径
ls -lah                # 详细列表（含隐藏文件）
cd ~/project           # 切换目录
mkdir -p a/b/c         # 递归创建目录
touch f.txt            # 创建空文件
cp f.txt f2.txt        # 复制
mv f2.txt new.txt      # 重命名/移动
rm new.txt             # 删除
rm -rf old-dir/        # 递归强制删除
```
### 文本处理
```bash
cat f.txt              # 查看文件
less f.txt             # 分页查看
head -20 f.txt         # 头 20 行
tail -f log.txt        # 实时追踪日志
grep -rn "TODO" ./     # 递归搜索
wc -l f.txt            # 统计行数
sort f.txt | uniq      # 排序去重
```
### 系统信息
```bash
uname -a               # 内核/架构
df -h                  # 磁盘使用
du -sh .               # 当前目录大小
free -h                # 内存使用
ps aux                 # 进程列表
top                    # 实时监控
```
### 网络
```bash
ping -c 4 8.8.8.8      # 连通性测试
ip a                   # 网络接口
ss -tlnp               # 监听端口
curl -I https://...    # HTTP 头
```
### 编译相关
```bash
# x86-64 本地
gcc -S -O1 -o add.s add.c           # 汇编输出
gcc -c -O1 -o add.o add.c           # 编译为目标文件
objdump -d add.o                     # 反汇编
file add.o                           # 查看文件类型
# ARM64 交叉编译
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
aarch64-linux-gnu-objdump -d add-arm64.o
file add-arm64.o
```
### 其他
```bash
man ls                 # 查看手册
history                # 命令历史
alias ll='ls -alF'     # 创建别名
echo $PATH             # 环境变量
which python3          # 定位命令路径
```
> **文档信息**  
> 本实验文档由原飞书文档重构排版，补充了 ARM64 寄存器说明、CISC vs RISC 对比表格、完整实验流程脚本、常见问题排查、以及分层命令速查表。  
> 文档版本：`v2-ds` | 整理日期：2026-05-15

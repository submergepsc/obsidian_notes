title: "第二周实验：Linux常用命令与 ARM 汇编语言"
source: https://ycnw11in464y.feishu.cn/wiki/JC4qwwvWtiaXV0k15wvc5Dcln8I
wiki_token: JC4qwwvWtiaXV0k15wvc5Dcln8I
obj_token: UM9bd2YvZoUAqtxS3u6cLRlQnxh
rewritten_by: codex
# 第二周实验：Linux 常用命令与 ARM 汇编语言
> [!tip]
> 更详细的拆分版已经放在 [[第二周实验：Linux常用命令与ARM汇编语言 codex/README]]。该目录把 Linux 命令、压缩解压、系统网络、C 到汇编、ARM64 交叉编译和实验报告模板分成多个互相链接的文档，适合继续扩展。
## 实验目标
本实验分为两个部分：
1. 熟悉 Linux 终端中的常用命令，能够完成文件管理、文本查看、查找、压缩、权限管理、软件安装等基础操作。
2. 理解 C 语言程序如何被编译成汇编语言，并对比 x86-64 与 ARM64/AArch64 的汇编代码和指令特点。
完成本实验后，应能回答以下问题：
- 如何在 Linux 终端中查看、创建、复制、移动、删除文件？
- 如何查看系统资源、磁盘空间、进程和网络信息？
- `gcc -S`、`objdump -d`、`file` 分别用于什么场景？
- 为什么在 x86 机器上编译 ARM 程序需要交叉编译工具链？
- AArch64 中 `w0`、`w1`、`x0`、`x1` 这些寄存器大致表示什么？
- CISC 与 RISC 指令集在指令长度和设计思路上有什么区别？
## 实验环境
建议环境：
- 操作系统：Ubuntu 22.04/24.04 或其他 Debian/Ubuntu 系 Linux
- 终端：GNOME Terminal、Konsole、Windows Terminal + WSL 均可
- 编辑器：`nano`、`vim`、VS Code 或任意文本编辑器
- 编译器：`gcc`
- 交叉编译器：`aarch64-linux-gnu-gcc`
- 反汇编工具：`objdump`、`aarch64-linux-gnu-objdump`
先确认基础命令是否可用：
```bash
uname -a
gcc --version
objdump --version
```
如果没有安装 GCC：
```bash
sudo apt update
sudo apt install build-essential binutils
```
如果要编译 ARM64/AArch64 程序：
```bash
sudo apt install crossbuild-essential-arm64 gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu
```
> [!note]
> 如果 `apt install` 报错，通常先运行 `sudo apt update` 更新软件源索引，再重新安装。
# 一、Linux 常用命令
Linux 命令的基本格式通常是：
```bash
命令 [选项] [参数]
```
例如：
```bash
ls -lah /home
```
其中：
- `ls` 是命令。
- `-lah` 是选项，用于控制输出格式。
- `/home` 是参数，表示要查看的目录。
## 1. 文件与目录操作
| 命令 | 用途 | 常用示例 |
| --- | --- | --- |
| `pwd` | 显示当前目录 | `pwd` |
| `ls` | 列出目录内容 | `ls -l`、`ls -a`、`ls -lah` |
| `cd` | 切换目录 | `cd /home`、`cd ..`、`cd ~` |
| `mkdir` | 创建目录 | `mkdir test`、`mkdir -p a/b/c` |
| `touch` | 创建空文件或更新时间戳 | `touch note.txt` |
| `cp` | 复制文件或目录 | `cp a.txt b.txt`、`cp -r dir1 dir2` |
| `mv` | 移动或重命名 | `mv old.txt new.txt`、`mv file.txt /tmp/` |
| `rm` | 删除文件或目录 | `rm a.txt`、`rm -r dir` |
| `cat` | 输出文件内容 | `cat file.txt` |
| `less` | 分页查看文件 | `less long.log` |
| `head` | 查看文件开头 | `head -20 file.txt` |
| `tail` | 查看文件末尾 | `tail -20 file.txt`、`tail -f app.log` |

常见操作示例：
```bash
mkdir linux-lab
cd linux-lab
touch hello.txt
echo "Hello Linux" > hello.txt
cat hello.txt
cp hello.txt hello-copy.txt
mv hello-copy.txt backup.txt
ls -lah
```
> [!warning]
> `rm` 删除文件通常不会进入回收站。执行 `rm -r`、`rm -rf` 前一定要确认路径，避免误删重要目录。
## 2. 路径概念
Linux 中常见路径写法：

| 写法 | 含义 |
| --- | --- |
| `/` | 根目录 |
| `~` | 当前用户的家目录 |
| `.` | 当前目录 |
| `..` | 上一级目录 |
| `/home/loviya` | 绝对路径 |
| `docs/file.txt` | 相对路径 |

示例：
```bash
cd ~
pwd
cd ..
pwd
cd -
```
`cd -` 可以回到上一次所在目录，适合在两个目录之间来回切换。
## 3. 文本查看与文本处理
| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `grep` | 搜索文本行 | `grep "error" app.log` |
| `sed` | 文本替换和流编辑 | `sed 's/old/new/g' file.txt` |
| `awk` | 按列处理文本 | `awk '{print $1}' file.txt` |
| `sort` | 排序 | `sort names.txt` |
| `uniq` | 去重，通常配合 `sort` | `sort names.txt | uniq` |
| `cut` | 按分隔符取列 | `cut -d',' -f1 data.csv` |
| `wc` | 统计行数、词数、字节数 | `wc -l file.txt` |
| `diff` | 比较文件差异 | `diff old.txt new.txt` |

示例：从日志中查找错误行。
```bash
grep -n "error" app.log
grep -i "warning" app.log
```
常用选项：
- `grep -n`：显示行号。
- `grep -i`：忽略大小写。
- `grep -r`：递归搜索目录。
## 4. 查找文件和命令位置
| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `find` | 实时查找文件 | `find . -name "*.c"` |
| `locate` | 使用数据库快速查找 | `locate stdio.h` |
| `which` | 查看命令路径 | `which gcc` |
| `type` | 查看命令类型 | `type cd`、`type ls` |
| `whereis` | 查看命令、源码、手册位置 | `whereis gcc` |

示例：
```bash
find . -type f -name "*.c"
find . -type d -name "build"
which gcc
type cd
```
> [!note]
> `cd` 是 shell 内建命令，所以 `type cd` 会显示它是 shell builtin，而不是普通可执行文件。
## 5. 系统信息与资源查看
| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `uname` | 查看系统和内核信息 | `uname -a` |
| `hostname` | 查看主机名 | `hostname` |
| `whoami` | 查看当前用户 | `whoami` |
| `id` | 查看用户 UID/GID | `id` |
| `date` | 查看时间 | `date` |
| `uptime` | 查看运行时间和负载 | `uptime` |
| `free` | 查看内存 | `free -h` |
| `df` | 查看磁盘空间 | `df -h` |
| `du` | 查看目录占用 | `du -sh .` |
| `top` | 动态查看进程 | `top` |
| `ps` | 查看进程快照 | `ps aux` |
| `kill` | 结束进程 | `kill PID` |

示例：
```bash
df -h
du -sh ~/Downloads
free -h
ps aux | grep bash
```
## 6. 网络相关命令
| 命令 | 用途 | 示例 |
| --- | --- | --- |
| `ip` | 查看或配置网络接口 | `ip addr`、`ip route` |
| `ping` | 测试连通性 | `ping -c 4 8.8.8.8` |
| `curl` | 发送 HTTP 请求或下载 | `curl -I https://example.com` |
| `wget` | 下载文件 | `wget URL` |
| `ssh` | 远程登录 | `ssh user@host` |
| `scp` | 远程复制 | `scp a.txt user@host:/tmp/` |
| `ss` | 查看 socket/端口 | `ss -ltnp` |

> [!note]
> 旧教程常见 `ifconfig`、`netstat`，现代 Linux 更推荐使用 `ip` 和 `ss`。
## 7. 压缩与解压
| 格式 | 压缩 | 解压 |
| --- | --- | --- |
| `.tar.gz` | `tar -czvf archive.tar.gz dir/` | `tar -xzvf archive.tar.gz` |
| `.tar.xz` | `tar -cJvf archive.tar.xz dir/` | `tar -xJvf archive.tar.xz` |
| `.zip` | `zip -r archive.zip dir/` | `unzip archive.zip` |
| `.gz` | `gzip file.txt` | `gunzip file.txt.gz` |

常用解释：
- `c`：create，创建归档。
- `x`：extract，解包。
- `z`：使用 gzip。
- `J`：使用 xz。
- `v`：verbose，显示过程。
- `f`：指定文件名。
## 8. 权限管理
查看权限：
```bash
ls -l
```
示例输出：
```text
-rwxr-xr-- 1 user group 1234 May 15 script.sh
```
权限可以拆成三组：
- `r`：read，读权限。
- `w`：write，写权限。
- `x`：execute，执行权限。
- 三组分别表示：文件所有者、所属组、其他用户。
常用命令：
```bash
chmod +x script.sh
chmod 755 script.sh
chown user:group file.txt
```
`755` 的含义：
- 所有者：`7 = 4 + 2 + 1 = rwx`
- 所属组：`5 = 4 + 1 = r-x`
- 其他用户：`5 = 4 + 1 = r-x`
## 9. 软件包管理
Ubuntu 使用 `apt` 管理软件：
```bash
sudo apt update
sudo apt install package-name
sudo apt remove package-name
sudo apt search keyword
apt show package-name
```
示例：
```bash
sudo apt update
sudo apt install gcc make gdb
```
> [!warning]
> `sudo` 表示以管理员权限运行命令。安装、删除软件时要确认包名，避免卸载系统关键组件。
## 10. 帮助与命令历史
| 命令 | 用途 |
| --- | --- |
| `man ls` | 查看完整手册 |
| `ls --help` | 查看简短帮助 |
| `history` | 查看命令历史 |
| `alias ll='ls -alF'` | 创建临时别名 |
| `echo $PATH` | 查看命令搜索路径 |

推荐学习方式：
```bash
man ls
man grep
ls --help
history | tail
```
# 二、从 C 语言到汇编语言
## 1. 准备实验目录
建议把本实验文件放在单独目录，避免和其他文件混在一起：
```bash
mkdir -p ~/linux-arm-lab/week2
cd ~/linux-arm-lab/week2
```
创建一个简单的 C 文件：
```bash
nano add.c
```
写入：
```c
int add(int a, int b)
{
    return a + b;
}
```
保存后确认：
```bash
cat add.c
```
原始截图参考：
![image.png](../crawl/feishu-wiki-JC4qwwvWtiaXV0k15wvc5Dcln8I/assets/WlsmbZWUKohBqKx4qTKccrOLnne.png)
## 2. 查看 x86-64 汇编
在普通 PC/虚拟机上，默认 `gcc` 通常生成 x86-64 架构代码：
```bash
gcc -S -O1 -o add-x86.s add.c
```
查看生成的汇编：
```bash
less add-x86.s
```
或：
```bash
nano add-x86.s
```
原始截图参考：
![image.png](../crawl/feishu-wiki-JC4qwwvWtiaXV0k15wvc5Dcln8I/assets/AjsKbYm6vo64SzxAoPScVnM8nvc.png)
常见 x86-64 输出可能类似：
```asm
add:
        leal    (%rdi,%rsi), %eax
        ret
```
含义简要说明：
- `add:` 是函数标签，对应 C 函数 `add` 的入口。
- `%rdi`、`%rsi` 通常用于传递前两个整型参数。
- `%eax` 通常用于保存整型返回值。
- `leal (%rdi,%rsi), %eax` 在这里完成 `a + b`。
- `ret` 表示函数返回。
> [!note]
> `-S` 表示只生成汇编文件，不继续汇编和链接。  
> `-O1` 是一级优化，会让汇编更简洁。若使用 `-O0`，通常会看到更完整的栈帧和局部变量保存过程。
可以对比无优化版本：
```bash
gcc -S -O0 -o add-x86-O0.s add.c
diff add-x86.s add-x86-O0.s
```
## 3. 编译成目标文件并查看文件类型
生成目标文件：
```bash
gcc -c -O1 -o add-x86.o add.c
```
查看文件类型：
```bash
file add-x86.o
```
可能看到：
```text
add-x86.o: ELF 64-bit LSB relocatable, x86-64, ...
```
这说明 `add-x86.o` 是 x86-64 架构的 ELF 目标文件。
反汇编目标文件：
```bash
objdump -d add-x86.o
```
`objdump -d` 会显示机器码字节和对应的汇编指令。
# 三、ARM64/AArch64 交叉编译
## 1. 为什么需要交叉编译
大多数同学的电脑或虚拟机是 x86-64 架构，而课堂可能讨论 ARM 架构。直接运行 `gcc` 时，默认生成当前机器架构的程序。若要在 x86-64 机器上生成 ARM64 程序，就需要使用 ARM64 交叉编译工具链。
常见名称：
- `ARM64`：常用泛称。
- `AArch64`：ARMv8 之后的 64 位执行状态名称。
- `aarch64-linux-gnu-gcc`：在 Linux 上生成 AArch64 程序的 GCC 交叉编译器。
安装：
```bash
sudo apt update
sudo apt install crossbuild-essential-arm64 gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu
```
确认安装：
```bash
aarch64-linux-gnu-gcc --version
aarch64-linux-gnu-objdump --version
```
## 2. 生成 AArch64 汇编
```bash
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
```
查看：
```bash
less add-arm64.s
```
可能得到类似内容：
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
        .section        .note.GNU-stack,"",@progbits
```
解释：
- `.arch armv8-a`：说明目标架构。
- `.text`：代码段。
- `.global add`：把 `add` 暴露为全局符号。
- `add:`：函数入口标签。
- `add w0, w0, w1`：把 `w0 + w1` 的结果放回 `w0`。
- `ret`：函数返回。
> [!note]
> 以 `.` 开头的多是汇编器伪指令或元信息，不是 CPU 真正执行的机器指令。真正关键的指令是 `add w0, w0, w1` 和 `ret`。
## 3. AArch64 常见寄存器
| 寄存器 | 含义 |
| --- | --- |
| `x0`-`x30` | 64 位通用寄存器 |
| `w0`-`w30` | 对应 `x0`-`x30` 的低 32 位 |
| `sp` | stack pointer，栈指针 |
| `x30` | link register，保存返回地址，常写作 `lr` |
| `x0`/`w0` | 常用于第 1 个参数和返回值 |
| `x1`/`w1` | 常用于第 2 个参数 |

对于 `int add(int a, int b)`：
- `a` 通常放在 `w0`。
- `b` 通常放在 `w1`。
- 返回值放在 `w0`。
所以：
```asm
add w0, w0, w1
ret
```
就对应：
```c
return a + b;
```
## 4. 生成 ARM64 目标文件并反汇编
```bash
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
file add-arm64.o
aarch64-linux-gnu-objdump -d add-arm64.o
```
可能看到类似输出：
```text
add-arm64.o: ELF 64-bit LSB relocatable, ARM aarch64, ...
```
反汇编中可能看到：
```asm
0000000000000000 <add>:
   0:   0b010000        add     w0, w0, w1
   4:   d65f03c0        ret
```
注意左侧的 `0:`、`4:` 是地址偏移。每条 AArch64 指令通常占 4 字节，所以地址从 `0` 到 `4`。
# 四、完整程序示例：hello.c
前面的 `add.c` 没有 `main` 函数，适合观察单个函数的汇编。如果想生成完整可执行程序，可以创建：
```bash
nano hello.c
```
写入：
```c
#include <stdio.h>
int add(int a, int b)
{
    return a + b;
}
int main(void)
{
    int result = add(3, 4);
    printf("result = %d\n", result);
    return 0;
}
```
## 1. 本机 x86-64 编译运行
```bash
gcc -O1 -o hello-x86 hello.c
file hello-x86
./hello-x86
```
预期输出：
```text
result = 7
```
反汇编：
```bash
objdump -d hello-x86 | less
```
只看 `main` 和 `add` 附近：
```bash
objdump -d hello-x86 | grep -A20 "<add>"
objdump -d hello-x86 | grep -A40 "<main>"
```
## 2. ARM64 交叉编译
```bash
aarch64-linux-gnu-gcc -O1 -o hello-arm64 hello.c
file hello-arm64
```
可能输出：
```text
hello-arm64: ELF 64-bit LSB pie executable, ARM aarch64, ...
```
反汇编：
```bash
aarch64-linux-gnu-objdump -d hello-arm64 | less
```
> [!warning]
> 在 x86-64 主机上，`hello-arm64` 一般不能直接运行，因为它是 ARM64 程序。若要运行，需要 ARM64 真机、虚拟机，或 QEMU 用户态模拟器。
如需使用 QEMU：
```bash
sudo apt install qemu-user
qemu-aarch64 ./hello-arm64
```
如果程序是动态链接，可能还需要指定 ARM64 库路径；入门实验中通常只要求能编译和反汇编即可。
# 五、CISC 与 RISC：指令长度对比
## 1. CISC：复杂指令集
CISC 是 Complex Instruction Set Computer 的缩写，代表架构之一是 x86/x86-64。
特点：
- 指令长度可变。
- 一条指令可能完成较复杂的操作。
- 历史包袱较重，但兼容性强。
- 反汇编时同一函数的不同指令可能占用不同字节数。
x86-64 示例：
```asm
leal    (%rdi,%rsi), %eax
ret
```
在机器码层面，每条指令长度不一定相同。
## 2. RISC：精简指令集
RISC 是 Reduced Instruction Set Computer 的缩写，ARM 是典型代表之一。
特点：
- 指令格式更规整。
- 很多 ARM64 指令固定为 4 字节。
- 通常强调 load/store 模型，即内存访问和算术运算分开。
- 便于流水线和硬件实现。
AArch64 示例：
```asm
add     w0, w0, w1
ret
```
在 AArch64 中，上面两条指令通常各占 4 字节。
## 3. 用 objdump 观察指令字节
查看 x86-64：
```bash
objdump -d add-x86.o
```
查看 ARM64：
```bash
aarch64-linux-gnu-objdump -d add-arm64.o
```
对比时重点看：
- 左侧地址偏移是否按固定步长增加。
- 中间机器码字节长度是否一致。
- 右侧汇编指令是否来自不同指令集。
# 六、常见编译选项说明
| 选项 | 含义 |
| --- | --- |
| `-S` | 只生成汇编文件 `.s` |
| `-c` | 只编译/汇编为目标文件 `.o`，不链接 |
| `-o 文件名` | 指定输出文件 |
| `-O0` | 不优化，适合观察完整栈帧 |
| `-O1` | 轻度优化，适合观察核心逻辑 |
| `-O2` | 常用优化级别 |
| `-g` | 生成调试信息 |
| `-Wall` | 打开常见警告 |

示例：
```bash
gcc -Wall -g -O0 -o hello-debug hello.c
gcc -S -O1 -o hello.s hello.c
gcc -c -O1 -o hello.o hello.c
```
# 七、推荐实验步骤
按下面顺序完成，最不容易混乱：
1. 创建实验目录。
2. 写 `add.c`。
3. 用本机 `gcc` 生成 `add-x86.s`。
4. 用 `gcc -c` 生成 `add-x86.o`。
5. 用 `file` 和 `objdump -d` 查看 x86-64 目标文件。
6. 安装 AArch64 交叉编译工具链。
7. 用 `aarch64-linux-gnu-gcc -S` 生成 `add-arm64.s`。
8. 用 `aarch64-linux-gnu-gcc -c` 生成 `add-arm64.o`。
9. 用 `file` 和 `aarch64-linux-gnu-objdump -d` 查看 ARM64 目标文件。
10. 对比 x86-64 与 AArch64 汇编的参数寄存器、返回寄存器和指令长度。
完整命令清单：
```bash
mkdir -p ~/linux-arm-lab/week2
cd ~/linux-arm-lab/week2
cat > add.c <<'EOF'
int add(int a, int b)
{
    return a + b;
}
EOF
gcc -S -O1 -o add-x86.s add.c
gcc -c -O1 -o add-x86.o add.c
file add-x86.o
objdump -d add-x86.o
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
file add-arm64.o
aarch64-linux-gnu-objdump -d add-arm64.o
```
# 八、常见问题与排错
## 1. `aarch64-linux-gnu-gcc: command not found`
说明交叉编译器未安装。
解决：
```bash
sudo apt update
sudo apt install gcc-aarch64-linux-gnu
```
## 2. `Permission denied`
如果运行脚本时报权限不足：
```bash
chmod +x script.sh
./script.sh
```
如果访问系统目录时报权限不足，不要盲目加 `sudo`，先确认自己是否真的需要修改该目录。
## 3. ARM64 程序无法直接运行
现象可能是：
```text
cannot execute binary file: Exec format error
```
原因：当前机器是 x86-64，目标程序是 ARM64。
解决思路：
- 只做编译和反汇编，不运行。
- 使用 ARM64 机器运行。
- 使用 QEMU 模拟运行。
## 4. `objdump` 反汇编结果不对
如果用普通 `objdump` 反汇编 ARM64 文件，可能显示不正确或不支持目标架构。建议使用：
```bash
aarch64-linux-gnu-objdump -d add-arm64.o
```
## 5. 汇编文件里很多以点开头的行看不懂
例如：
```asm
.arch armv8-a
.text
.global add
.type add, %function
```
这些通常是汇编器伪指令、段信息、符号信息或调试/元数据。初学时可以先重点看真正的 CPU 指令，例如：
```asm
add w0, w0, w1
ret
```
# 九、实验记录建议
建议在实验报告中记录：
## 1. Linux 命令练习
- 当前路径：`pwd`
- 创建的实验目录：`mkdir`
- 创建和查看文件：`touch`、`echo`、`cat`
- 复制/移动/删除文件：`cp`、`mv`、`rm`
- 查找文件：`find`
- 查看系统信息：`uname -a`、`df -h`、`free -h`
## 2. 编译与汇编观察
记录以下命令和结果：
```bash
gcc -S -O1 -o add-x86.s add.c
gcc -c -O1 -o add-x86.o add.c
file add-x86.o
objdump -d add-x86.o
```
```bash
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
file add-arm64.o
aarch64-linux-gnu-objdump -d add-arm64.o
```
## 3. 对比结论
可写成：
- x86-64 和 AArch64 使用不同的寄存器命名方式。
- x86-64 常见参数寄存器包括 `%rdi`、`%rsi`，返回值常在 `%eax`/`%rax`。
- AArch64 中前几个参数常用 `w0/x0`、`w1/x1` 等寄存器，返回值常放在 `w0/x0`。
- AArch64 指令格式更规整，常见指令固定 4 字节。
- x86-64 指令长度可变，是 CISC 架构的典型特点。
# 十、提交检查清单
提交前检查：
- [ ] 能说出 `pwd`、`ls`、`cd`、`cp`、`mv`、`rm`、`grep`、`find` 的基本用法。
- [ ] 已成功生成 `add-x86.s` 和 `add-arm64.s`。
- [ ] 已用 `file` 确认 x86-64 与 ARM64 目标文件架构不同。
- [ ] 已用 `objdump -d` 或 `aarch64-linux-gnu-objdump -d` 查看反汇编。
- [ ] 能解释 `add w0, w0, w1` 对应 C 语言中的 `return a + b;`。
- [ ] 能说明为什么 ARM64 程序通常不能直接在 x86-64 主机上运行。
- [ ] 实验报告中有关键命令、关键输出和个人理解。
# 附：命令速查
```bash
# 文件目录
pwd
ls -lah
cd ..
mkdir -p test/a/b
touch file.txt
cp file.txt file2.txt
mv file2.txt new.txt
rm new.txt
# 查看文本
cat file.txt
less file.txt
head -20 file.txt
tail -20 file.txt
grep -n "hello" file.txt
# 系统信息
uname -a
df -h
du -sh .
free -h
ps aux
# 编译
gcc -S -O1 -o add-x86.s add.c
gcc -c -O1 -o add-x86.o add.c
objdump -d add-x86.o
# ARM64 交叉编译
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
aarch64-linux-gnu-objdump -d add-arm64.o
```

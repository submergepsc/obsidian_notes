title: "第二周实验：Linux 常用命令与 ARM 汇编语言 codex 版"
rewritten_by: codex
# 第二周实验：Linux 常用命令与 ARM 汇编语言
这是一个更详细的拆分版实验文档。每个主题单独成文，方便在 Obsidian 里阅读、跳转和补充截图。
## 阅读顺序
1. [[00-实验总览与环境准备]]
2. [[01-Linux终端基础与帮助系统]]
3. [[02-文件目录与路径操作]]
4. [[03-文本查看查找与处理]]
5. [[04-压缩解压与打包命令]]
6. [[05-系统信息进程网络与权限]]
7. [[06-C语言到x86汇编]]
8. [[07-ARM64交叉编译与AArch64汇编]]
9. [[08-实验报告模板与常见错误]]
## 本实验要掌握什么
```text
Linux 命令基础
  -> 会在终端里管理文件、查看文本、查找内容、压缩解压、查看系统状态
C 语言到汇编
  -> 会用 gcc -S 生成汇编文件
  -> 会用 objdump -d 查看目标文件/可执行文件的反汇编
ARM64 交叉编译
  -> 理解为什么 x86 主机上需要 aarch64-linux-gnu-gcc
  -> 能生成 AArch64 汇编和目标文件
  -> 能对比 x86-64 与 AArch64 的参数寄存器、返回值寄存器、指令长度
```
## 快速命令索引
### Linux 基础
```bash
pwd
ls -lah
cd ..
mkdir -p lab/week2
touch note.txt
cp note.txt note-copy.txt
mv note-copy.txt backup.txt
rm backup.txt
```
### 文本处理
```bash
cat file.txt
less file.txt
head -20 file.txt
tail -20 file.txt
grep -n "error" app.log
find . -name "*.c"
wc -l file.txt
```
### 压缩解压
```bash
tar -czvf project.tar.gz project/
tar -xzvf project.tar.gz
zip -r project.zip project/
unzip project.zip
```
### 编译与汇编
```bash
gcc -S -O1 -o add-x86.s add.c
gcc -c -O1 -o add-x86.o add.c
objdump -d add-x86.o
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
aarch64-linux-gnu-objdump -d add-arm64.o
```
## 与原文件的关系
- 原始文件：`../第二周实验：Linux常用命令与ARM汇编语言 1.md`
- 单文件改写版：`../第二周实验：Linux常用命令与ARM汇编语言 1 codex.md`
- 当前目录：拆分后的详细版，适合继续扩展。

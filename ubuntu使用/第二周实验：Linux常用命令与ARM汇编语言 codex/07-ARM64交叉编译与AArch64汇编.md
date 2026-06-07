title: "07 ARM64 交叉编译与 AArch64 汇编"
# 07 ARM64 交叉编译与 AArch64 汇编
## 1. 为什么需要交叉编译
如果你的电脑是 x86-64，那么直接运行：
```bash
gcc -o hello hello.c
```
生成的通常是 x86-64 程序。
但课堂学习的是 ARM64/AArch64，如果想在 x86-64 电脑上生成 ARM64 程序，就需要交叉编译器：
```bash
aarch64-linux-gnu-gcc
```
一句话总结：
```text
gcc                         给当前机器编译
aarch64-linux-gnu-gcc       给 ARM64 Linux 编译
```
## 2. 安装工具链
```bash
sudo apt update
sudo apt install crossbuild-essential-arm64 gcc-aarch64-linux-gnu binutils-aarch64-linux-gnu
```
检查：
```bash
aarch64-linux-gnu-gcc --version
aarch64-linux-gnu-objdump --version
```
## 3. 生成 ARM64 汇编
源文件 `add.c`：
```c
int add(int a, int b)
{
    return a + b;
}
```
生成汇编：
```bash
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
```
查看：
```bash
less add-arm64.s
```
可能看到：
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
## 4. 哪些是真正的 CPU 指令
以点开头的行通常是汇编器伪指令：
```asm
.arch armv8-a
.text
.align 2
.global add
.type add, %function
.size add, .-add
```
这些不是 CPU 直接执行的指令。
真正关键的是：
```asm
add     w0, w0, w1
ret
```
解释：

| 指令 | 含义 |
| --- | --- |
| `add w0, w0, w1` | 把 `w0 + w1` 的结果写回 `w0` |
| `ret` | 函数返回 |

## 5. AArch64 寄存器入门
常见寄存器：

| 寄存器 | 含义 |
| --- | --- |
| `x0`-`x30` | 64 位通用寄存器 |
| `w0`-`w30` | 对应 `x0`-`x30` 的低 32 位 |
| `sp` | stack pointer，栈指针 |
| `x30` | link register，返回地址寄存器，也叫 `lr` |

函数参数和返回值常见规则：

| 内容 | 常用寄存器 |
| --- | --- |
| 第 1 个参数 | `x0`/`w0` |
| 第 2 个参数 | `x1`/`w1` |
| 第 3 个参数 | `x2`/`w2` |
| 返回值 | `x0`/`w0` |

所以：
```c
int add(int a, int b)
{
    return a + b;
}
```
对应：
```text
a      -> w0
b      -> w1
返回值 -> w0
```
因此：
```asm
add w0, w0, w1
ret
```
就是：
```c
return a + b;
```
## 6. 生成 ARM64 目标文件
```bash
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
```
查看文件类型：
```bash
file add-arm64.o
```
可能输出：
```text
add-arm64.o: ELF 64-bit LSB relocatable, ARM aarch64, ...
```
这说明它不是 x86-64 文件，而是 ARM64/AArch64 文件。
## 7. ARM64 反汇编
```bash
aarch64-linux-gnu-objdump -d add-arm64.o
```
可能看到：
```asm
0000000000000000 <add>:
   0:   0b010000        add     w0, w0, w1
   4:   d65f03c0        ret
```
注意：
```text
地址从 0 到 4
说明两条指令之间相差 4 字节
```
AArch64 很多普通指令固定 4 字节，这是 RISC 架构常见特点。
## 8. 和 x86-64 对比
x86-64 可能是：
```asm
0000000000000000 <add>:
   0:   8d 04 37                lea    (%rdi,%rsi,1),%eax
   3:   c3                      ret
```
AArch64 可能是：
```asm
0000000000000000 <add>:
   0:   0b010000        add     w0, w0, w1
   4:   d65f03c0        ret
```
对比：

| 项目 | x86-64 | AArch64 |
| --- | --- | --- |
| 架构类型 | CISC 代表 | RISC 代表 |
| 参数寄存器 | `%rdi`, `%rsi` 等 | `x0/w0`, `x1/w1` 等 |
| 返回值 | `%rax/%eax` | `x0/w0` |
| 指令长度 | 可变长 | 常见固定 4 字节 |
| 示例加法 | `lea (%rdi,%rsi), %eax` | `add w0, w0, w1` |

## 9. ARM64 程序为什么不能直接运行
如果你在 x86-64 主机运行 ARM64 程序：
```bash
./hello-arm64
```
可能报错：
```text
cannot execute binary file: Exec format error
```
原因：
```text
当前 CPU 是 x86-64
程序机器码是 ARM64
CPU 不认识这种指令
```
解决方式：
- 在 ARM64 真机上运行。
- 在 ARM64 虚拟机里运行。
- 用 QEMU 模拟运行。
- 本实验只要求编译和反汇编，不一定要求运行。
## 10. 可选：QEMU 运行 ARM64 程序
安装：
```bash
sudo apt install qemu-user
```
编译静态 ARM64 程序：
```bash
aarch64-linux-gnu-gcc -static -O1 -o hello-arm64 hello.c
```
运行：
```bash
qemu-aarch64 ./hello-arm64
```
> [!note]
> 加 `-static` 可以减少动态库路径问题，更适合初学者测试。
## 11. 本节命令清单
```bash
aarch64-linux-gnu-gcc -S -O1 -o add-arm64.s add.c
aarch64-linux-gnu-gcc -c -O1 -o add-arm64.o add.c
file add-arm64.o
aarch64-linux-gnu-objdump -d add-arm64.o
```

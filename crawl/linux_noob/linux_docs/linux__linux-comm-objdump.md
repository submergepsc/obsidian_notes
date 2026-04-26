# Linux objdump 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

objdump 是 GNU Binutils 工具集中的一个重要命令行工具，用于显示目标文件（object files）和可执行文件的各种信息。它是 Linux 系统下进行二进制分析、逆向工程和调试的利器。

objdump 的主要功能包括：

  * 反汇编二进制文件
  * 查看文件头部信息
  * 显示节区（section）内容
  * 查看符号表
  * 显示重定位信息
  * 分析文件结构



* * *

## 基本语法

objdump 的基本命令格式如下：

```bash
objdump [选项] 文件名
```


如果不指定任何选项，objdump 会显示文件的节区头部信息。

* * *

## 常用选项详解

### 反汇编相关选项

## 实例

```bash
-d, \--disassemble # 反汇编包含代码的节区 -D, \--disassemble-all # 反汇编所有节区 -S, \--source # 混合显示源代码和汇编代码（需要编译时使用-g选项） \--prefix-addresses # 在反汇编时显示完整地址 \--no-addresses # 不显示地址信息
```


### 节区信息选项

## 实例

```bash
-h, \--section-headers # 显示节区头部信息 -j, \--section =名称 # 仅显示指定节区的内容
```


### 符号表选项

## 实例

```bash
-t, \--syms # 显示符号表 -T, \--dynamic-syms # 显示动态符号表
```


### 文件头部信息

```bash
-f, --file-headers # 显示文件头部信息
```


### 其他实用选项

## 实例

```bash
-l, \--line-numbers # 显示行号信息（需要调试信息） -r, \--reloc # 显示重定位条目 -R, \--dynamic-reloc # 显示动态重定位条目 -s, \--full-contents # 显示所有节区的完整内容
```


* * *

## 实用示例

### 示例1：查看可执行文件的结构

```bash
objdump -h /bin/ls
```


输出示例：

```bash
/bin/ls: file format elf64-x86-64 Sections: Idx Name Size VMA LMA File off Algn 0 .interp 0000001c 0000000000400238 0000000000400238 00000238 2**0 CONTENTS, ALLOC, LOAD, READONLY, DATA 1 .note.ABI-tag 00000020 0000000000400254 0000000000400254 00000254 2**2 CONTENTS, ALLOC, LOAD, READONLY, DATA ...
```


### 示例2：反汇编可执行文件

```bash
objdump -d /bin/ls
```


输出示例（部分）：

```bash
0000000000405a50 : 405a50: 31 ed xor %ebp,%ebp 405a52: 49 89 d1 mov %rdx,%r9 405a55: 5e pop %rsi 405a56: 48 89 e2 mov %rsp,%rdx 405a59: 48 83 e4 f0 and $0xfffffffffffffff0,%rsp ...
```


### 示例3：查看符号表

```bash
objdump -t myprogram.o
```


输出示例：

```bash
myprogram.o: file format elf64-x86-64 SYMBOL TABLE: 0000000000000000 l df *ABS* 0000000000000000 myprogram.c 0000000000000000 l d .text 0000000000000000 .text 0000000000000000 g F .text 0000000000000015 main 0000000000000000 *UND* 0000000000000000 printf
```


### 示例4：混合显示源代码和汇编代码

```bash
objdump -S myprogram
```


输出示例：

## 实例

```bash
int main ( ) { 400526 : 55 push % rbp 400527 : 48 89 e5 mov % rsp ,% rbp printf ( "Hello, World!n" ) ; 40052a : bf d4 05 40 00 mov $ 0x4005d4 ,% edi 40052f : e8 cc fe ff ff callq 400400 return 0 ; 400534 : b8 00 00 00 00 mov $ 0x0 ,% eax }
```


* * *

## 实际应用场景

### 场景1：调试程序崩溃

当程序崩溃时，可以使用 objdump 查看崩溃地址附近的代码：

```bash
objdump -d --start-address=0x400526 --stop-address=0x400536 myprogram
```


### 场景2：分析库函数调用

查看程序调用了哪些动态库函数：

```bash
objdump -T myprogram | grep UND
```


### 场景3：学习汇编语言

通过反汇编简单的C程序来学习汇编语言：

## 实例

```bash
gcc -o simple simple.c objdump -d simple
```


* * *

## 注意事项

  1. **调试信息** ：要获得源代码级别的信息，编译时需要加上 `-g` 选项
  2. **优化影响** ：编译器优化会影响生成的汇编代码，分析时需注意
  3. **架构差异** ：不同CPU架构的汇编指令不同，确保使用正确的反汇编选项
  4. **权限问题** ：分析系统文件可能需要root权限
  5. **文件格式** ：objdump 主要针对ELF格式文件，其他格式可能需要特殊处理



* * *

## 进阶技巧

### 结合其他工具使用

## 实例

```bash
# 使用grep过滤特定函数 objdump -d myprogram | grep -A20 "main>:" # 统计函数大小 objdump -d myprogram | awk '/^[0-9a-f]+ :/ {print $1,$2}'
```


### 创建反汇编脚本

## 实例

```bash
#!/bin/bash # 反汇编脚本示例 if [ $# -ne 1 ] ; then echo "Usage: $0 " exit 1 fi echo "=== 文件头部信息 ===" objdump -f $1 echo -e "n=== 节区信息 ===" objdump -h $1 echo -e "n=== 反汇编代码 ===" objdump -d $1
```


* * *

## 总结

objdump 是Linux系统下强大的二进制分析工具，掌握它可以：

  * 深入理解程序运行机制
  * 快速定位程序问题
  * 学习汇编语言和系统知识
  * 进行基础的逆向工程分析



通过本文介绍的基本用法和实用示例，你应该已经能够开始使用 objdump 进行基本的二进制文件分析了。随着实践经验的积累，你会发现它在系统编程和调试中的更多妙用。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

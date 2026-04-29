# Linux nm 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

`nm` 是 Linux 系统中的一个重要命令行工具，全称是 "Name List"。它用于显示二进制目标文件（如库文件、可执行文件）中的符号信息，是程序员和分析二进制文件时常用的工具。

### 主要功能

  * 列出目标文件中的符号（函数、变量等）
  * 显示符号的类型和属性
  * 帮助分析程序链接问题
  * 辅助调试和逆向工程



* * *

## 基本语法

```bash
nm [选项] 文件名
```


### 常用选项参数说明

选项 | 说明  
---|---  
`-a` | 显示所有符号，包括调试符号  
`-g` | 只显示外部（全局）符号  
`-u` | 只显示未定义的符号  
`-D` | 显示动态符号（用于共享库）  
`-C` | 解码（demangle）C++符号名称  
`-l` | 显示符号所在的行号（需要调试信息）  
`-S` | 显示符号大小  
`-t` | 指定输出格式（d-十进制，o-八进制，x-十六进制）  
`--size-sort` | 按符号大小排序  
`--defined-only` | 只显示已定义的符号  
  
* * *

## 符号类型说明

`nm` 输出的符号类型用一个字母表示，常见的有：

类型 | 说明  
---|---  
A | 绝对符号，链接时不会被改变  
B/b | 未初始化数据段（BSS段）中的符号  
D/d | 已初始化数据段中的符号  
T/t | 代码段中的符号（T表示全局，t表示局部）  
U | 未定义的符号（需要从其他文件链接）  
W/w | 弱符号（weak symbol）  
R/r | 只读数据段中的符号  
C | 公共符号（common symbol）  
I | 间接引用其他符号  
  
* * *

## 实际应用示例

### 示例1：查看可执行文件的符号表

```bash
nm /bin/ls
```


输出示例：

```bash
0000000000000000 A _IO_stdin_used 0000000000000000 R _fp_hw 0000000000000000 T _init 0000000000000000 W _ITM_deregisterTMCloneTable 0000000000000000 W _ITM_registerTMCloneTable 0000000000000000 W __cxa_finalize 0000000000000000 W __gmon_start__ 0000000000000000 T __libc_csu_fini 0000000000000000 T __libc_csu_init ...
```


### 示例2：只查看未定义的符号

```bash
nm -u /bin/ls
```


输出示例：

```bash
U __ctype_toupper_loc U __errno_location U __overflow U __stack_chk_fail U __strtoul_internal U _obstack_begin U _obstack_newchunk U abort U access ...
```


### 示例3：查看C++程序的符号（解码名称）

```bash
nm -C my_program
```


输出示例：

```bash
0000000000000000 T main 0000000000000000 T std::cout 0000000000000000 T std::basic_ostream&lt;char, std::char_traits &gt;&amp; std::operator&lt;&lt; &lt;std::char_traits &gt;(std::basic_ostream&lt;char, std::char_traits &gt;&amp;, char const*) ...
```


### 示例4：查看符号大小并按大小排序

```bash
nm -S --size-sort my_library.so
```


输出示例：

```bash
0000000000000001 0000000000000001 T func1 0000000000000002 0000000000000002 T func2 0000000000000004 0000000000000004 D global_var 0000000000000008 0000000000000008 B large_buffer ...
```


* * *

## 常见使用场景

### 1\. 解决链接错误

当遇到"undefined reference"错误时，可以使用 `nm` 检查哪些符号未定义：

```bash
nm -u my_program.o
```


### 2\. 分析库文件内容

查看共享库导出的符号：

```bash
nm -D libexample.so
```


### 3\. 比较两个版本的二进制文件

## 实例

```bash
nm old_version & gt; old.txt nm new_version & gt; new.txt diff old.txt new.txt
```


### 4\. 查找特定符号

```bash
nm my_program | grep "main"
```


* * *

## 注意事项

  1. 对于剥离（stripped）过的二进制文件，`nm` 可能无法显示有用的信息
  2. 不同架构的二进制文件可能需要使用交叉编译工具链中的 `nm`
  3. 动态符号（在共享库中）需要使用 `-D` 选项查看
  4. 对于C++程序，建议总是使用 `-C` 选项解码符号名称



* * *

## 进阶技巧

### 结合其他工具使用

## 实例

```bash
# 使用objdump查看更详细的符号信息 objdump -t my_program # 使用readelf查看ELF文件头信息 readelf -s my_program
```


### 编写脚本分析符号

## 实例

```bash
#!/bin/bash # 统计符号类型分布 nm $1 | awk '{print $2}' | sort | uniq -c | sort -nr
```


### 创建符号映射文件

```bash
nm -n my_program &gt; symbol_map.txt
```


* * *

## 总结

`nm` 命令是Linux开发者的重要工具之一，掌握它可以：

  * 更好地理解程序结构
  * 快速定位链接问题
  * 分析第三方库的内容
  * 辅助调试和逆向工程



通过本文介绍的基本用法和实际示例，你应该已经掌握了 `nm` 命令的核心功能。在实际工作中，可以结合具体需求灵活运用各种选项参数。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

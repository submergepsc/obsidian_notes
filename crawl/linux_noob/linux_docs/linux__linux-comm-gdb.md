# Linux gdb 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

GDB (GNU Debugger) 是 Linux 系统下最常用的程序调试工具，它可以帮助开发者：

  * 跟踪程序执行流程
  * 设置断点暂停程序运行
  * 查看和修改变量值
  * 分析程序崩溃原因
  * 检查函数调用栈



GDB 支持多种编程语言，包括 C、C++、Objective-C、Fortran、Ada 等，是 Linux 开发者不可或缺的调试利器。

* * *

## 安装 gdb

在大多数 Linux 发行版中，gdb 可以通过包管理器轻松安装：

## 实例

```bash
# Ubuntu/Debian sudo apt-get install gdb # CentOS/RHEL sudo yum install gdb # Fedora sudo dnf install gdb # Arch Linux sudo pacman -S gdb
```


安装完成后，可以通过以下命令验证安装是否成功：

```bash
gdb --version
```


* * *

## 编译可调试程序

要使用 gdb 调试程序，需要在编译时添加 `-g` 选项生成调试信息：

```bash
gcc -g program.c -o program
```


`-g` 选项会在可执行文件中嵌入源代码信息，使 gdb 能够将机器指令与源代码对应起来。

* * *

## 基本 gdb 命令

### 启动和退出 gdb

## 实例

```bash
# 启动 gdb 并加载程序 gdb . / program # 启动 gdb 并附加到正在运行的进程 gdb -p PID # 退出 gdb ( gdb ) quit # 或简写 ( gdb ) q
```


### 运行程序

## 实例

```bash
# 运行程序 ( gdb ) run # 或简写 ( gdb ) r # 带参数运行 ( gdb ) run arg1 arg2
```


### 断点管理

## 实例

```bash
# 在指定行设置断点 ( gdb ) break 10 # 或简写 ( gdb ) b 10 # 在函数入口设置断点 ( gdb ) break main ( gdb ) break function_name # 查看所有断点 ( gdb ) info breakpoints # 删除断点 ( gdb ) delete 1 # 删除编号为1的断点 ( gdb ) delete # 删除所有断点
```


### 程序执行控制

## 实例

```bash
# 继续执行直到下一个断点 ( gdb ) continue # 或简写 ( gdb ) c # 单步执行（进入函数） ( gdb ) step # 或简写 ( gdb ) s # 单步执行（不进入函数） ( gdb ) next # 或简写 ( gdb ) n # 执行完当前函数并返回 ( gdb ) finish
```


### 查看代码

## 实例

```bash
# 查看当前行附近的代码 ( gdb ) list # 或简写 ( gdb ) l # 查看指定行附近的代码 ( gdb ) list 15 # 查看指定函数的代码 ( gdb ) list main
```


### 检查变量和内存

## 实例

```bash
# 打印变量值 ( gdb ) print variable_name # 或简写 ( gdb ) p variable_name # 修改变量值 ( gdb ) print variable_name = new_value # 查看变量类型 ( gdb ) ptype variable_name # 查看内存内容 ( gdb ) x / 10xw & amp;variable # 以16进制查看10个字(word)
```


### 调用栈分析

## 实例

```bash
# 查看调用栈 ( gdb ) backtrace # 或简写 ( gdb ) bt # 切换到指定栈帧 ( gdb ) frame 2 # 或简写 ( gdb ) f 2
```


* * *

## 高级调试技巧

### 条件断点

## 实例

```bash
# 当i等于5时触发断点 ( gdb ) break 10 if i == 5
```


### 观察点

## 实例

```bash
# 当变量被修改时暂停 ( gdb ) watch variable_name # 当变量被读取时暂停 ( gdb ) rwatch variable_name # 当变量被读取或修改时暂停 ( gdb ) awatch variable_name
```


### 多线程调试

## 实例

```bash
# 查看所有线程 ( gdb ) info threads # 切换到指定线程 ( gdb ) thread 2 # 只允许当前线程执行 ( gdb ) set scheduler-locking on
```


### 调试核心转储文件

## 实例

```bash
# 加载核心转储文件 gdb . / program core # 查看崩溃时的调用栈 ( gdb ) bt
```


* * *

## gdb 图形界面

gdb 也支持图形界面模式，可以使用 `-tui` 选项启动：

```bash
gdb -tui ./program
```


或者在使用过程中切换：

## 实例

```bash
( gdb ) layout src # 显示源代码窗口 ( gdb ) layout asm # 显示汇编窗口 ( gdb ) layout regs # 显示寄存器窗口 ( gdb ) layout split # 同时显示源代码和汇编
```


* * *

## 实用 gdb 配置

可以将常用配置添加到 `~/.gdbinit` 文件中：

## 实例

```bash
# 显示漂亮的打印 set print pretty on # 设置历史记录大小 set history save on set history size 1000 # 自定义命令 define printarray set $i = 0 while $i & lt; $arg0 printf & quot;array [ % d ] = % dn & quot;, $i , $arg1 [ $i ] set $i = $i \+ 1 end end
```


* * *

## 常见问题解决

### 调试时看不到源代码

  1. 确保编译时使用了 `-g` 选项
  2. 检查源代码是否在编译时的位置
  3. 使用 `directory` 命令添加源代码路径：

```bash
(gdb) directory /path/to/source
```


### 调试优化过的代码

优化可能会改变代码执行顺序，使调试变得困难。建议调试时关闭优化：

```bash
gcc -O0 -g program.c -o program
```


* * *

## 总结

gdb 是 Linux 下功能强大的调试工具，掌握它可以显著提高调试效率。本文介绍了 gdb 的基本用法和常用命令，建议读者通过实际调试练习来巩固这些知识。随着经验的积累，你会发现 gdb 能帮助你解决各种复杂的调试问题。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

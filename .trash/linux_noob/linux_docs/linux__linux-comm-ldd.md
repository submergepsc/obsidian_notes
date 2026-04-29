# Linux ldd 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

ldd（List Dynamic Dependencies）是 Linux 系统中一个非常有用的命令行工具，用于显示程序或共享库所依赖的动态链接库。当你在 Linux 上运行一个程序时，系统需要加载该程序依赖的各种共享库（.so 文件），ldd 就是用来查看这些依赖关系的工具。

* * *

## ldd 命令的基本语法

```bash
ldd [选项] 可执行文件或共享库
```


### 常用选项参数说明

选项 | 描述  
---|---  
-v | 显示详细版本信息  
-u | 显示未使用的直接依赖  
-d | 执行重定位并报告丢失的函数  
-r | 执行重定位并报告丢失的函数和数据  
\--help | 显示帮助信息  
  
* * *

## ldd 命令的工作原理

ldd 实际上是一个脚本，它通过设置特殊的环境变量来运行目标程序，使得程序在加载时显示其依赖的库信息而不是正常执行。具体来说：

  1. 对于 ELF 格式的可执行文件，ldd 会解析其动态段（dynamic segment）
  2. 检查 DT_NEEDED 条目以确定所需的共享库
  3. 在系统库路径中查找这些库文件
  4. 显示每个库的完整路径和内存地址映射



* * *

## 使用示例

### 示例 1：查看简单程序的依赖

```bash
ldd /bin/ls
```


典型输出：

```bash
linux-vdso.so.1 (0x00007ffd5a3f0000) libselinux.so.1 => /lib/x86_64-linux-gnu/libselinux.so.1 (0x00007f8e4a3b0000) libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f8e4a1c0000) libpcre2-8.so.0 => /usr/lib/x86_64-linux-gnu/libpcre2-8.so.0 (0x00007f8e4a130000) libdl.so.2 => /lib/x86_64-linux-gnu/libdl.so.2 (0x00007f8e4a120000) /lib64/ld-linux-x86-64.so.2 (0x00007f8e4a400000) libpthread.so.0 => /lib/x86_64-linux-gnu/libpthread.so.0 (0x00007f8e4a100000)
```


### 示例 2：检查未使用的直接依赖

```bash
ldd -u /usr/bin/python3
```


### 示例 3：详细模式查看依赖

```bash
ldd -v /usr/bin/gcc
```


* * *

## 实际应用场景

### 场景 1：解决 "library not found" 错误

当程序因缺少库而无法运行时，ldd 可以帮助快速定位问题：

```bash
ldd ./my_program | grep "not found"
```


### 场景 2：检查库版本冲突

```bash
ldd -r ./my_program
```


### 场景 3：验证库路径是否正确

```bash
ldd /path/to/your/executable | awk '{print $3}' | xargs ls -la
```


* * *

## 注意事项与常见问题

  1. **安全警告** ：不要对不受信任的可执行文件使用 ldd，因为它实际上会尝试执行程序的部分代码

     * 替代方案：`objdump -p /path/to/program | grep NEEDED`
  2. **静态链接程序** ：对于完全静态链接的程序，ldd 会显示 "not a dynamic executable"

  3. **交叉编译环境** ：在交叉编译环境中，需要使用对应平台的 ldd 工具

  4. **常见错误** ：

     * `ldd: ./program: No such file or directory` → 可能是缺少解释器或程序本身不存在
     * `ldd: exited with unknown exit code` → 程序可能在运行期间崩溃



* * *

## 进阶技巧

### 1\. 结合 readelf 查看更详细的依赖信息

```bash
readelf -d /path/to/program | grep NEEDED
```


### 2\. 使用 LD_TRACE_LOADED_OBJECTS 环境变量

```bash
LD_TRACE_LOADED_OBJECTS=1 /path/to/program
```


### 3\. 检查库的依赖树

```bash
ldd /path/to/library.so | awk '{print $3}' | xargs ldd
```


* * *

## 总结

ldd 是 Linux 系统管理和程序调试中不可或缺的工具，它能够：

  * 快速显示程序的动态库依赖关系
  * 帮助解决库缺失或版本冲突问题
  * 验证程序运行环境是否完整
  * 辅助进行软件打包和部署



掌握 ldd 命令的使用，能够大大提高你在 Linux 环境下解决依赖问题的效率。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

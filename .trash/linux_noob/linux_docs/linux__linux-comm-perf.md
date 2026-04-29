# Linux perf 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

perf 是 Linux 系统性能分析工具集，全称是 Performance Event Counters。它基于 Linux 内核的 perf_events 子系统，能够提供硬件和软件层面的性能分析能力。

perf 的主要功能包括：

  * CPU 性能分析
  * 函数调用追踪
  * 硬件事件统计
  * 软件事件监控
  * 系统调用跟踪



* * *

## perf 基本语法

perf 命令的基本语法格式为：

```bash
perf [--version] [--help] COMMAND [ARGS]
```


常用子命令包括：

  * `stat`：性能计数器统计
  * `record`：记录性能数据
  * `report`：分析记录的数据
  * `top`：实时性能监控
  * `list`：列出可用事件
  * `annotate`：源代码级分析



* * *

## perf 常用子命令详解

### perf stat

统计命令执行过程中的各种硬件和软件事件。

```bash
perf stat [options] command [command-options]
```


常用选项：

  * `-e`：指定要监控的事件
  * `-p`：监控指定进程ID
  * `-a`：监控所有CPU
  * `-r`：重复运行并显示平均值
  * `-d`：显示更多详细事件



示例：

## 实例

```bash
# 统计 ls 命令的执行情况 perf stat ls # 监控指定进程 perf stat -p 1234 # 监控特定事件 perf stat -e cycles,instructions,cache-misses ls
```


### perf record

记录性能数据到文件（默认 perf.data）。

```bash
perf record [options] command [command-options]
```


常用选项：

  * `-g`：记录调用图（call graph）
  * `-F`：采样频率（Hz）
  * `-p`：记录指定进程
  * `-o`：指定输出文件
  * `-e`：指定要记录的事件



示例：

## 实例

```bash
# 记录 ls 命令的执行情况 perf record ls # 以99Hz频率记录进程1234 perf record -F 99 -p 1234 -g
```


### perf report

分析 perf record 记录的数据。

```bash
perf report [options]
```


常用选项：

  * `-i`：指定输入文件
  * `-n`：显示样本数量
  * `--stdio`：文本模式输出
  * `-g`：显示调用图
  * `-s`：按指定字段排序



示例：

## 实例

```bash
# 分析默认的 perf.data 文件 perf report # 分析指定文件并以文本模式输出 perf report -i perf.data.old \--stdio
```


### perf top

实时显示系统中最消耗资源的函数。

```bash
perf top [options]
```


常用选项：

  * `-e`：指定监控事件
  * `-p`：监控指定进程
  * `-K`：隐藏内核符号
  * `-U`：隐藏用户空间符号
  * `-g`：显示调用图



示例：

## 实例

```bash
# 实时监控系统性能 perf top # 监控特定事件 perf top -e cache-misses
```


### perf list

列出所有可监控的事件。

```bash
perf list [hw|sw|cache|tracepoint|pmu|event_glob]
```


示例：

## 实例

```bash
# 列出所有事件 perf list # 列出硬件缓存事件 perf list cache
```


* * *

## perf 事件类型

perf 可以监控多种类型的事件：

事件类型 | 描述 | 示例  
---|---|---  
Hardware | CPU硬件事件 | cycles, instructions  
Software | 内核软件事件 | context-switches, page-faults  
Cache | 缓存相关事件 | cache-references, cache-misses  
Tracepoints | 内核静态跟踪点 | syscalls, block, sched  
PMU | 处理器特定事件 | (vendor specific)  
Breakpoints | 断点事件 | mem:[:access]  
  
* * *

## perf 实际应用示例

### 1\. 分析程序性能瓶颈

## 实例

```bash
# 记录程序执行 perf record -g . / my_program # 分析结果 perf report -g
```


### 2\. 查找CPU热点函数

```bash
perf top -p $(pidof my_program)
```


### 3\. 比较两次运行的性能差异

## 实例

```bash
# 第一次运行 perf record -o perf.data.1 . / my_program input1 # 第二次运行 perf record -o perf.data.2 . / my_program input2 # 比较差异 perf diff perf.data.1 perf.data.2
```


### 4\. 分析系统调用

## 实例

```bash
# 列出可用的系统调用跟踪点 perf list 'syscalls:*' # 跟踪open系统调用 perf stat -e 'syscalls:sys_enter_open' -a sleep 10
```


* * *

## perf 使用技巧

  1. **减少开销** ：对于长时间运行的性能分析，适当降低采样频率（如 -F 99）

  2. **符号解析** ：确保调试符号可用，可以通过安装调试包或使用-g编译程序

  3. **火焰图生成** ：结合FlameGraph工具生成直观的性能分析图

  4. **多核分析** ：使用 -a 选项监控所有CPU，或使用 -C 指定特定CPU

  5. **用户/内核空间分离** ：使用 -k 和 -u 选项分别分析内核和用户空间




* * *

## 常见问题解决

  1. **权限问题** ：

```bash
echo -1 &gt; /proc/sys/kernel/perf_event_paranoid
```


或使用sudo运行perf

  2. **缺少符号信息** ：

     * 确保程序使用-g选项编译
     * 安装调试符号包
  3. **采样数据过大** ：

     * 减少采样频率
     * 缩短采样时间
     * 使用--no-call-graph减少调用图信息
  4. **无法解析Java/Python等高级语言** ：

     * 需要特定语言的perf工具支持
     * 考虑使用语言特定的分析工具



* * *

## 进阶学习资源

  1. **官方文档** ：Linux内核源码中的tools/perf/Documentation目录

  2. **书籍推荐** ：

     * 《Systems Performance: Enterprise and the Cloud》
     * 《性能之巅：洞悉系统、企业与云计算》
  3. **在线资源** ：

     * Brendan Gregg的博客和工具集
     * perf-tools工具集
  4. **相关工具** ：

     * FlameGraph：可视化性能数据
     * bpftrace：更灵活的动态追踪



通过掌握perf命令，你可以深入分析Linux系统的性能特征，快速定位性能瓶颈，优化应用程序和系统配置。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

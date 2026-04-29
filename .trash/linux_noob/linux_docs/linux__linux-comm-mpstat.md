# Linux mpstat 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 一、mpstat 命令概述

mpstat（Multi-Processor Statistics）是 Linux 系统中的一个性能监控工具，属于 sysstat 工具包的一部分。它主要用于监控 CPU 的使用情况，能够显示每个 CPU 核心的详细统计信息。

### 1.1 主要功能

  * 显示 CPU 使用率的详细统计
  * 监控单个 CPU 核心或所有核心的性能
  * 提供用户态、内核态、空闲等状态的 CPU 时间占比
  * 支持间隔采样和多次采样功能



### 1.2 适用场景

  * 系统性能调优
  * CPU 瓶颈分析
  * 多核 CPU 负载均衡检查
  * 系统监控和故障排查



* * *

## 二、安装与基本使用

### 2.1 安装方法

大多数 Linux 发行版可以通过包管理器安装：

```bash
# Ubuntu/Debian sudo apt install sysstat # CentOS/RHEL sudo yum install sysstat # Arch Linux sudo pacman -S sysstat
```


### 2.2 基本命令格式

```bash
mpstat [选项] [间隔时间] [采样次数]
```


#### 简单示例

## 实例

```bash
# 显示所有 CPU 核心的当前统计信息 mpstat # 每2秒采样一次，共采样5次 mpstat 2 5
```


* * *

## 三、命令选项详解

选项 | 说明  
---|---  
-P {ALL|CPU编号} | 指定要显示的 CPU 核心（ALL 表示所有核心）  
-u | 显示 CPU 使用率（默认选项）  
-I {SUM|CPU|SCPU|ALL} | 显示中断统计信息  
-V | 显示版本信息  
-o JSON | 以 JSON 格式输出结果  
  
### 3.1 常用选项组合

## 实例

```bash
# 监控所有 CPU 核心，每1秒刷新一次 mpstat -P ALL 1 # 只监控第一个 CPU 核心（CPU0） mpstat -P 0 1 5
```


* * *

## 四、输出结果解析

执行 `mpstat -P ALL 1` 的典型输出：

```bash
Linux 5.4.0-91-generic (hostname) 03/15/2023 _x86_64_ (4 CPU) 10:30:45 AM CPU %usr %nice %sys %iowait %irq %soft %steal %guest %gnice %idle 10:30:46 AM all 5.25 0.00 1.25 0.25 0.00 0.25 0.00 0.00 0.00 93.00 10:30:46 AM 0 6.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 93.00 10:30:46 AM 1 4.00 0.00 1.00 1.00 0.00 1.00 0.00 0.00 0.00 93.00 10:30:46 AM 2 6.00 0.00 2.00 0.00 0.00 0.00 0.00 0.00 0.00 92.00 10:30:46 AM 3 5.00 0.00 1.00 0.00 0.00 0.00 0.00 0.00 0.00 94.00
```


### 4.1 各字段含义

字段 | 说明  
---|---  
%usr | 用户态程序执行时间占比  
%nice | 低优先级用户态程序执行时间占比  
%sys | 内核态程序执行时间占比  
%iowait | CPU 等待 I/O 操作的时间占比  
%irq | 处理硬件中断的时间占比  
%soft | 处理软件中断的时间占比  
%steal | 虚拟 CPU 等待实际 CPU 的时间占比  
%guest | 运行虚拟处理器的时间占比  
%gnice | 运行低优先级客户机的时间占比  
%idle | CPU 空闲时间占比  
  
* * *

## 五、实际应用案例

### 5.1 监控 CPU 使用率

## 实例

```bash
# 监控所有 CPU 核心，每2秒刷新，共显示5次 mpstat -P ALL 2 5
```


### 5.2 识别 CPU 瓶颈

重点关注：

  * %usr 过高：用户态程序消耗大量 CPU
  * %sys 过高：系统调用频繁
  * %iowait 过高：可能存在 I/O 瓶颈



### 5.3 生成性能报告

## 实例

```bash
# 将输出重定向到文件 mpstat -P ALL 1 60 > cpu_stats.log
```


* * *

## 六、常见问题解答

### 6.1 mpstat 和 top 命令有什么区别？

  * `top`：实时动态显示系统整体状态
  * `mpstat`：专注于 CPU 统计，提供更详细的每个核心数据



### 6.2 %idle 很低说明什么？

表示 CPU 很忙，需要结合其他指标判断：

  * 如果 %usr 高：应用程序消耗大量 CPU
  * 如果 %sys 高：系统调用过多
  * 如果 %iowait 高：I/O 成为瓶颈



### 6.3 如何监控特定 CPU 核心？

## 实例

```bash
# 只监控 CPU 核心 2 mpstat -P 2 1
```


* * *

## 七、总结

mpstat 是 Linux 系统性能监控的重要工具，特别适合分析多核 CPU 的使用情况。通过本文的学习，你应该能够：

  1. 理解 mpstat 的基本原理和使用场景
  2. 掌握 mpstat 的常用命令选项
  3. 正确解读 mpstat 的输出结果
  4. 在实际工作中应用 mpstat 进行性能分析



建议结合其他工具如 `vmstat`、`iostat` 一起使用，可以更全面地分析系统性能问题。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

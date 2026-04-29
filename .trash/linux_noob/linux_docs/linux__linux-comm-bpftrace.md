# Linux bpftrace 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

bpftrace 是一个基于 eBPF (扩展伯克利包过滤器) 的高级追踪工具，它允许开发者在不修改内核代码的情况下，动态地观察和分析 Linux 系统的运行状态。

eBPF 是 Linux 内核中的一项革命性技术，它提供了一个安全的虚拟机环境，可以在内核中运行用户定义的代码。bpftrace 构建在 eBPF 之上，提供了一个更简单、更高级的抽象层。

* * *

## bpftrace 的核心优势

### 实时系统观测

  * 无需重启系统或应用
  * 极低的性能开销
  * 可以观测内核和用户空间程序



### 灵活的探测能力

  * 支持多种探测点类型：函数入口/出口、定时器、硬件事件等
  * 可以追踪系统调用、网络事件、磁盘 I/O 等



### 简单的脚本语言

  * 类似 AWK 的语法，学习曲线平缓
  * 内置丰富的函数和变量
  * 支持条件过滤和聚合统计



* * *

## bpftrace 安装与配置

### 安装方法

## 实例

```bash
# Ubuntu/Debian sudo apt install bpftrace # CentOS/RHEL sudo yum install bpftrace # 从源码编译 git clone https: // github.com / iovisor / bpftrace.git mkdir bpftrace / build & amp; & amp; cd bpftrace / build cmake .. make sudo make install
```


### 验证安装

```bash
sudo bpftrace -e 'BEGIN { printf("Hello, bpftrace!n"); }'
```


* * *

## bpftrace 基本语法

bpftrace 程序由探测点(probe)和关联的动作(action)组成，基本结构如下：

```bash
probe /filter/ { action }
```


### 探测点类型

探测点类型 | 描述 | 示例  
---|---|---  
`kprobe` | 内核函数入口 | `kprobe:vfs_read`  
`kretprobe` | 内核函数返回 | `kretprobe:vfs_read`  
`uprobe` | 用户空间函数入口 | `uprobe:/bin/bash:readline`  
`tracepoint` | 内核静态追踪点 | `tracepoint:syscalls:sys_enter_open`  
`interval` | 定时触发 | `interval:s:5`  
`software` | 软件事件 | `software:faults:major`  
  
### 常用内置变量

  * `pid`：当前进程 ID
  * `tid`：当前线程 ID
  * `comm`：当前进程名
  * `nsecs`：纳秒级时间戳
  * `arg0`-`argN`：函数参数
  * `retval`：函数返回值



* * *

## bpftrace 实用示例

### 1\. 追踪系统调用

## 实例

```bash
# 统计 open 系统调用的次数 sudo bpftrace -e 'tracepoint:syscalls:sys_enter_open { @[comm] = count(); }'
```


### 2\. 分析函数执行时间

## 实例

```bash
# 测量 vfs_read 的执行时间 sudo bpftrace -e ' kprobe:vfs_read { @start[tid] = nsecs; } kretprobe:vfs_read /@start[tid]/ { @times = hist(nsecs - @start[tid]); delete(@start[tid]); }'
```


### 3\. 监控进程的文件访问

## 实例

```bash
# 跟踪指定进程打开的文件 sudo bpftrace -e 'tracepoint:syscalls:sys_enter_openat /pid == 1234/ { printf("%s -> %sn", comm, str(args->filename)); }'
```


### 4\. 统计 TCP 连接

## 实例

```bash
# 按进程统计 TCP 连接数 sudo bpftrace -e 'kprobe:tcp_connect { @[comm] = count(); }'
```


* * *

## bpftrace 高级特性

### 1\. 地图(Map)功能

bpftrace 提供了多种内置地图类型用于数据聚合：

## 实例

```bash
# 统计直方图 @ hist = hist ( nsecs ) ; # 计算平均值 @ avg = avg ( nsecs ) ; # 统计唯一值 @ unique = count ( ) ;
```


### 2\. 条件过滤

## 实例

```bash
# 只追踪特定进程的 read 调用 tracepoint:syscalls:sys_enter_read / pid == 1234 / { printf ( "PID %d reading %d bytesn" , pid, args- > count ) ; }
```


### 3\. 多探针组合

## 实例

```bash
# 跟踪从 socket 创建到连接的全过程 kprobe:sock_alloc { @ socket [ tid ] = 1 ; } kprobe:tcp_connect /@ socket [ tid ] / { printf ( "socket %d connecting to %s:%dn" , args- > sock- > __sk_common.skc_dport, ntop ( args- > sock- > __sk_common.skc_daddr ) , args- > sock- > __sk_common.skc_dport ) ; delete ( @ socket [ tid ] ) ; }
```


* * *

## bpftrace 最佳实践

  1. **限制追踪范围** ：使用 PID 或命令名过滤，减少系统开销
  2. **避免过度打印** ：过多的 printf 会影响性能
  3. **使用聚合** ：尽量使用 count()、sum() 等聚合函数
  4. **清理资源** ：长时间运行的脚本要定期清理地图数据
  5. **安全考虑** ：bpftrace 需要 root 权限，谨慎运行未知脚本



* * *

## bpftrace 与其他工具对比

工具 | 优点 | 缺点  
---|---|---  
**bpftrace** | 灵活、高性能、易用 | 需要 root 权限  
**strace** | 简单、无需编译 | 性能开销大  
**perf** | 功能全面、低开销 | 学习曲线陡峭  
**SystemTap** | 功能强大 | 需要编译、配置复杂  
  
* * *

## 学习资源推荐

  1. [bpftrace 官方文档](https://github.com/iovisor/bpftrace/blob/master/docs/reference_guide.md)
  2. [bpftrace 单行教程](https://github.com/iovisor/bpftrace/blob/master/docs/tutorial_one_liners.md)
  3. [bpftrace 示例仓库](https://github.com/iovisor/bpftrace/tree/master/tools)



bpftrace 是系统性能分析和故障排查的强大工具，通过实践这些示例和掌握其核心概念，你将能够更深入地理解和优化 Linux 系统的运行行为。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

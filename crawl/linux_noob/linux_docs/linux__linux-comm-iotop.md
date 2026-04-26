# Linux iotop 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

iotop是一个类似于top命令的Linux系统监控工具，但它专注于显示磁盘I/O使用情况。它能实时监控系统中各个进程的磁盘读写活动，帮助系统管理员识别I/O密集型进程。

与iostat等工具不同，iotop提供了基于进程的I/O监控，可以精确到每个进程的读写速度和累计I/O量。

* * *

## 安装iotop

大多数Linux发行版默认不安装iotop，需要手动安装：

## 实例

```bash
# Debian/Ubuntu系统 sudo apt-get install iotop # RHEL/CentOS系统 sudo yum install iotop # Fedora系统 sudo dnf install iotop # Arch Linux sudo pacman -S iotop
```


* * *

## 基本语法

iotop的基本命令格式如下：

```bash
sudo iotop [选项]
```


注意：iotop需要root权限才能运行，因为它需要访问内核的I/O统计信息。

* * *

## 常用选项参数

选项 | 说明  
---|---  
`-o` 或 `--only` | 只显示实际进行I/O操作的进程  
`-b` 或 `--batch` | 非交互式模式，适合脚本中使用  
`-n NUM` | 在非交互模式下运行的迭代次数  
`-d SEC` | 设置刷新间隔时间（秒）  
`-p PID` | 只监控指定PID的进程  
`-u USER` | 只监控指定用户的进程  
`-P` 或 `--processes` | 只显示进程，不显示线程  
`-a` 或 `--accumulated` | 显示累计I/O而不是带宽  
`-k` 或 `--kilobytes` | 使用KB/s而不是B/s作为单位  
`-t` 或 `--time` | 在输出中添加时间戳  
`-q` 或 `--quiet` | 减少头部信息（在非交互模式下自动启用）  
  
* * *

## 交互模式下的快捷键

在交互模式下，iotop支持以下快捷键操作：

快捷键 | 功能  
---|---  
左右箭头 | 改变排序字段  
r | 反向排序  
o | 只显示活跃I/O进程（相当于-o选项）  
p | 进程/线程显示模式切换  
a | 累计/实时显示模式切换  
q | 退出iotop  
i | 改变优先级过滤（只显示更高优先级的进程）  
任意键 | 强制刷新显示  
  
* * *

## 输出字段解释

iotop的输出包含多个字段，每个字段的含义如下：

  1. **TID/PID** ：线程ID/进程ID
  2. **PRIO** ：I/O优先级（Linux的ionice值）
  3. **USER** ：进程所有者
  4. **DISK READ** ：磁盘读取速度
  5. **DISK WRITE** ：磁盘写入速度
  6. **SWAPIN** ：交换空间使用百分比
  7. **IO >**：I/O占用百分比
  8. **COMMAND** ：进程名称



* * *

## 使用示例

### 示例1：基本监控

```bash
sudo iotop
```


这会启动交互式界面，显示所有进程的I/O活动，按I/O使用量排序。

### 示例2：只显示活跃I/O进程

```bash
sudo iotop -o
```


或者运行iotop后按`o`键，只显示当前正在进行I/O操作的进程。

### 示例3：监控特定用户的进程

```bash
sudo iotop -u apache
```


只监控用户apache的进程I/O活动。

### 示例4：非交互模式输出

```bash
sudo iotop -b -n 3 -d 2
```


以非交互模式运行，每2秒刷新一次，共输出3次结果后退出。

### 示例5：监控特定进程

```bash
sudo iotop -p 1234
```


只监控PID为1234的进程的I/O活动。

* * *

## 实际应用场景

### 场景1：识别系统变慢的原因

当系统响应变慢时，运行：

```bash
sudo iotop -o
```


可以快速找出哪些进程正在大量读写磁盘，导致系统I/O瓶颈。

### 场景2：监控数据库性能

对于MySQL等数据库服务器：

```bash
sudo iotop -u mysql -o
```


专门监控mysql用户的I/O活动，分析数据库的磁盘负载。

### 场景3：定时记录I/O情况

```bash
sudo iotop -b -t -n 5 -d 10 &gt; iotop_log.txt
```


每10秒记录一次I/O情况，共记录5次，结果保存到文件中供后续分析。

* * *

## 注意事项

  1. iotop需要内核支持I/O accounting功能，在较新的Linux内核中通常已启用。
  2. 在某些虚拟化环境中，iotop可能无法准确报告I/O统计信息。
  3. 频繁刷新（如间隔小于1秒）可能会影响系统性能。
  4. 累计I/O统计（-a选项）在系统重启后会重置。
  5. 对于SSD设备，高I/O等待时间可能表明设备已达到性能极限。



* * *

## 替代工具

如果iotop不可用，可以考虑以下替代方案：

  1. **dstat** ：综合性能监控工具，包含磁盘I/O统计
  2. **atop** ：高级系统监控工具，包含进程级I/O统计
  3. **nmon** ：AIX/Linux性能监控工具
  4. **pidstat** ：sysstat工具包的一部分，可以报告进程I/O



* * *

## 总结

iotop是Linux系统管理员监控磁盘I/O活动的强大工具，通过进程级的I/O监控，可以快速定位性能瓶颈。掌握iotop的使用方法，能够有效诊断和解决与磁盘I/O相关的系统性能问题。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

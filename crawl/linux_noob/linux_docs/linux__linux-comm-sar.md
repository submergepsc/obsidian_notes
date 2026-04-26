# Linux sar 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 一、什么是 sar 命令

sar（System Activity Reporter）是 Linux 系统下一个强大的性能监控工具，属于 sysstat 工具包的一部分。它能够收集、报告和保存系统的各种活动信息，包括：

  * CPU 使用情况
  * 内存利用率
  * I/O 活动
  * 网络统计
  * 进程活动
  * 设备负载等



### 1.1 sar 命令的优势

  1. **历史数据分析** ：可以查看过去任意时间点的系统状态
  2. **全面监控** ：覆盖系统各个关键性能指标
  3. **低开销** ：数据收集对系统性能影响极小
  4. **自动化** ：可以配置为定期自动收集数据



* * *

## 二、安装与基本配置

### 2.1 安装 sysstat 包

在大多数 Linux 发行版中，sar 命令需要通过安装 sysstat 包来获取：

```bash
# Ubuntu/Debian sudo apt-get install sysstat # CentOS/RHEL sudo yum install sysstat # Fedora sudo dnf install sysstat
```


### 2.2 启用数据收集

安装后需要启用数据收集服务：

## 实例

```bash
# 编辑配置文件 sudo vi / etc / default / sysstat # 将 ENABLED="false" 改为 ENABLED = "true" # 重启服务 sudo systemctl restart sysstat
```


默认情况下，sar 每10分钟收集一次数据，并保存在 `/var/log/sysstat/` 目录下。

* * *

## 三、基本语法与常用参数

### 3.1 基本语法格式

```bash
sar [选项] [间隔时间] [次数]
```


### 3.2 常用参数说明

参数 | 说明  
---|---  
-A | 显示所有报告  
-u | 显示 CPU 利用率  
-r | 显示内存使用情况  
-b | 显示 I/O 和传输速率统计  
-n DEV | 显示网络设备统计  
-q | 显示系统负载和队列长度  
-d | 显示磁盘活动  
-P ALL | 显示每个 CPU 的统计  
-s | 指定开始时间  
-e | 指定结束时间  
-f | 从指定文件读取数据  
  
* * *

## 四、实际应用示例

### 4.1 实时监控 CPU 使用率

## 实例

```bash
# 每2秒刷新一次，共显示5次 sar -u 2 5
```


输出示例：

```bash
Linux 5.4.0-91-generic (hostname) 03/15/2023 _x86_64_ (4 CPU) 10:30:01 AM CPU %user %nice %system %iowait %steal %idle 10:30:03 AM all 5.12 0.00 1.02 0.51 0.00 93.35 10:30:05 AM all 6.23 0.00 1.34 0.23 0.00 92.20
```


### 4.2 查看历史内存使用情况

## 实例

```bash
# 查看今天的内存使用情况 sar -r # 查看指定日期的数据（需指定文件） sar -r -f / var / log / sysstat / sa15 # 15号的数据
```


### 4.3 监控磁盘 I/O 活动

## 实例

```bash
# 监控磁盘活动，每1秒刷新，共10次 sar -d 1 10
```


### 4.4 查看网络接口统计

## 实例

```bash
# 监控网络接口活动 sar -n DEV 1 5
```


* * *

## 五、高级用法与技巧

### 5.1 组合监控多个指标

## 实例

```bash
# 同时监控CPU、内存和磁盘 sar -urdb 1 5
```


### 5.2 生成特定时间段的报告

## 实例

```bash
# 查看上午9点到10点的CPU使用情况 sar -u -s 09:00:00 -e 10 :00:00
```


### 5.3 将输出保存到文件

## 实例

```bash
# 将监控结果保存到文件 sar -A 1 10 > system_report.log
```


### 5.4 监控特定CPU核心

## 实例

```bash
# 监控CPU0的使用情况 sar -P 0 1 5
```


* * *

## 六、数据解读指南

### 6.1 CPU 指标解读

指标 | 含义 | 健康范围  
---|---|---  
%user | 用户空间CPU使用率 | <70%  
%system | 内核空间CPU使用率 | <30%  
%iowait | CPU等待I/O时间 | <5%  
%idle | CPU空闲时间 | >20%  
  
### 6.2 内存指标解读

指标 | 含义  
---|---  
kbmemfree | 空闲物理内存(KB)  
kbmemused | 已用物理内存(KB)  
%memused | 内存使用率  
kbbuffers | 缓冲区使用的内存(KB)  
kbcached | 缓存使用的内存(KB)  
  
### 6.3 磁盘指标解读

指标 | 含义  
---|---  
tps | 每秒传输次数  
rd_sec/s | 每秒读取的扇区数  
wr_sec/s | 每秒写入的扇区数  
%util | 设备利用率  
  
* * *

## 七、常见问题排查

### 7.1 CPU 瓶颈识别

如果 `%user` 或 `%system` 持续高于80%，可能表明：

  * 应用程序计算密集
  * 系统调用过多
  * 需要优化代码或增加CPU资源



### 7.2 内存不足判断

当以下情况同时出现时，可能存在内存不足：

  * `%memused` 持续高于90%
  * `kbcached` 值很低
  * 交换分区(`kbswpused`)使用量高



### 7.3 I/O 瓶颈识别

`%iowait` 高和磁盘 `%util` 高表明：

  * 磁盘I/O成为瓶颈
  * 可能需要更快的存储设备
  * 或优化I/O密集型操作



* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

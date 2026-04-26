# Linux nethogs 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

nethogs 是一个开源的 Linux 命令行工具，用于按进程实时监控网络带宽使用情况。与传统的网络监控工具（如 iftop）不同，nethogs 不是基于端口或协议来统计流量，而是直接显示每个进程的网络活动。

* * *

## 为什么使用 nethogs

在 Linux 系统中，当网络出现异常时，管理员通常需要快速定位是哪个进程占用了大量带宽。nethogs 提供了以下优势：

  1. **进程级监控** ：直接显示每个进程的网络流量
  2. **实时更新** ：默认每秒刷新一次数据
  3. **无需配置** ：开箱即用，不需要复杂的设置
  4. **轻量级** ：资源占用低，适合在生产环境使用



* * *

## 安装 nethogs

### Ubuntu/Debian 系统

## 实例

```bash
sudo apt-get update sudo apt-get install nethogs
```


### CentOS/RHEL 系统

## 实例

```bash
sudo yum install epel-release sudo yum install nethogs
```


### 从源码编译安装

## 实例

```bash
git clone https: // github.com / raboof / nethogs cd nethogs make & amp; & amp; sudo make install
```


* * *

## 基本使用方法

### 监控所有网络接口

```bash
sudo nethogs
```


输出示例：

```bash
PID USER PROGRAM DEV SENT RECEIVED 1234 root /usr/bin/ssh eth0 12.456 5.678 KB/sec 5678 bob /usr/bin/firefox wlan0 45.789 32.123 KB/sec
```


### 监控特定网络接口

```bash
sudo nethogs eth0
```


### 刷新间隔设置（秒）

```bash
sudo nethogs -d 5 # 每5秒刷新一次
```


* * *

## 常用命令选项

选项 | 说明  
---|---  
`-d` | 设置刷新间隔时间（秒）  
`-c` | 刷新指定次数后退出  
`-t` | 追踪模式（显示累计流量）  
`-p` | 混杂模式（监听所有流量）  
`-V` | 显示版本信息  
`-h` | 显示帮助信息  
  
* * *

## 高级用法

### 1\. 追踪特定进程

```bash
sudo nethogs -p | grep "进程名"
```


### 2\. 保存监控结果到文件

```bash
sudo nethogs -t &gt; network_log.txt
```


### 3\. 监控特定用户进程

```bash
sudo nethogs -u username
```


### 4\. 组合使用选项

```bash
sudo nethogs -d 10 -c 6 eth0 # 每10秒刷新一次，共刷新6次后退出
```


* * *

## 输出字段解释

nethogs 的输出包含以下关键信息：

  1. **PID** ：进程ID
  2. **USER** ：运行该进程的用户
  3. **PROGRAM** ：进程名称或命令行
  4. **DEV** ：使用的网络接口
  5. **SENT** ：该进程发送的数据速率（KB/sec）
  6. **RECEIVED** ：该进程接收的数据速率（KB/sec）



* * *

## 实际应用场景

### 场景1：诊断网络缓慢问题

```bash
sudo nethogs
```


通过查看哪个进程占用最多带宽，快速定位问题源头。

### 场景2：监控服务器异常流量

```bash
sudo nethogs -d 30 -c 12 &gt; /var/log/nethogs.log
```


每30秒记录一次，共记录6分钟的网络活动。

### 场景3：限制特定进程带宽

## 实例

```bash
# 先使用nethogs找出高流量进程 sudo nethogs # 然后使用tc或wondershaper限制带宽 sudo wondershaper eth0 1024 512 # 限制上传1024Kbps，下载512Kbps
```


* * *

## 常见问题解决

### 问题1：权限不足

```bash
Error: opening device eth0: Operation not permitted
```


**解决方案** ：使用sudo或以root用户运行nethogs。

### 问题2：无法识别进程名

```bash
PID USER PROGRAM DEV SENT RECEIVED 1234 - - eth0 12.456 5.678 KB/sec
```


**解决方案** ：可能是进程已结束，或nethogs没有足够权限获取进程信息。

### 问题3：不支持特定网络接口

```bash
Error: No such device exists (device_name)
```


**解决方案** ：使用`ifconfig`或`ip a`命令确认正确的接口名称。

* * *

## 替代工具比较

工具 | 特点 | 适用场景  
---|---|---  
**nethogs** | 按进程显示流量 | 快速定位问题进程  
**iftop** | 按连接显示流量 | 分析具体网络连接  
**nload** | 按接口显示总流量 | 监控整体带宽使用  
**bmon** | 图形化界面 | 直观查看流量趋势  
  
* * *

## 总结

nethogs 是 Linux 系统管理员工具箱中不可或缺的网络诊断工具，特别适合：

  1. 快速识别异常网络活动的进程
  2. 监控服务器上各服务的带宽使用
  3. 排查网络性能问题



通过本文介绍的基本用法和高级技巧，您应该能够熟练使用 nethogs 来监控和管理系统网络流量。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

# Linux mtr 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

mtr（My Traceroute）是一个结合了 `traceroute` 和 `ping` 功能的强大网络诊断工具。它能够实时显示数据包在网络中的传输路径，并提供详细的统计信息，是网络管理员和开发人员排查网络问题的利器。

### mtr 的主要特点

  * **实时更新** ：持续显示路由和延迟信息
  * **双向诊断** ：可以同时显示发送和接收方向的路径
  * **综合统计** ：提供丢包率、延迟等关键指标
  * **可视化界面** ：交互式显示网络路径状况



* * *

## 安装 mtr 命令

### 在常见 Linux 发行版上安装

## 实例

```bash
# Debian/Ubuntu 系统 sudo apt-get install mtr # CentOS/RHEL 系统 sudo yum install mtr # Fedora 系统 sudo dnf install mtr # Arch Linux 系统 sudo pacman -S mtr
```


### 在 macOS 上安装

## 实例

```bash
# 使用 Homebrew 安装 brew install mtr
```


* * *

## mtr 基本语法

mtr 命令的基本语法格式如下：

```bash
mtr [选项] 目标主机
```


### 常用选项参数说明

选项 | 说明  
---|---  
`-4` | 强制使用 IPv4  
`-6` | 强制使用 IPv6  
`-c COUNT` | 设置发送的ping包数量  
`-i SECONDS` | 设置ping间隔时间（秒）  
`-n` | 不解析主机名，显示IP地址  
`-r` | 生成报告模式（非交互式）  
`-s BYTES` | 设置ping包大小（字节）  
`-w` | 宽输出模式，显示完整主机名  
`-z` | 显示AS（自治系统）编号  
`--report` | 等同于 `-r`，生成报告后退出  
`--report-wide` | 宽格式报告  
  
* * *

## mtr 使用示例

### 基础用法：诊断到目标主机的网络路径

```bash
mtr google.com
```


执行后会显示一个实时更新的界面，包含以下信息：

  * 跳数（Hop）
  * 主机名或IP地址
  * 丢包率（Loss%）
  * 最近延迟（Last）
  * 平均延迟（Avg）
  * 最佳延迟（Best）
  * 最差延迟（Wrst）
  * 标准差（StDev）



### 生成报告模式（适合脚本调用）

```bash
mtr -r -c 10 google.com > mtr_report.txt
```


这个命令会发送10个ping包到google.com，然后将结果保存到mtr_report.txt文件中。

### 设置ping包大小和间隔

```bash
mtr -s 100 -i 0.5 example.com
```


这个命令设置每个ping包大小为100字节，间隔时间为0.5秒。

### 同时显示AS编号

```bash
mtr -z example.com
```


这个命令会在结果中显示每个节点的AS（自治系统）编号，有助于识别网络归属。

* * *

## mtr 输出解读

### 交互式界面说明

当运行mtr时，你会看到类似下面的输出：

```bash
My traceroute [v0.92] example.com (192.0.2.1) 2022-01-01T12:00:00+0000 Keys: Help Display mode Restart statistics Order of fields quit Packets Pings Host Loss% Snt Last Avg Best Wrst StDev 1\. 192.168.1.1 0.0% 10 2.1 2.2 1.9 2.5 0.2 2\. 10.0.0.1 0.0% 10 5.3 5.5 5.1 6.0 0.3 3\. 203.0.113.1 0.0% 10 15.2 15.5 15.0 16.1 0.4 4\. example.com 0.0% 10 20.1 20.3 20.0 21.0 0.3
```


### 关键指标解释

  1. **Loss%** ：丢包率，数值越高表示网络越不稳定
  2. **Snt** ：已发送的探测包数量
  3. **Last** ：最近一次探测的延迟（毫秒）
  4. **Avg** ：平均延迟（毫秒）
  5. **Best** ：最佳延迟（毫秒）
  6. **Wrst** ：最差延迟（毫秒）
  7. **StDev** ：延迟的标准差，反映网络稳定性



* * *

## 高级用法与技巧

### 1\. 同时追踪IPv4和IPv6路径

## 实例

```bash
mtr -4 example.com # IPv4路径 mtr -6 example.com # IPv6路径
```


### 2\. 使用TCP SYN代替ICMP（绕过某些防火墙）

```bash
mtr --tcp example.com
```


### 3\. 指定源端口（用于特定路由测试）

```bash
mtr --port 8080 example.com
```


### 4\. 保存结果到CSV格式

```bash
mtr --csv example.com > result.csv
```


### 5\. 比较两个时间点的网络状况

## 实例

```bash
mtr -c 60 -i 1 -w example.com > result1.txt # 一段时间后 mtr -c 60 -i 1 -w example.com > result2.txt diff result1.txt result2.txt
```


* * *

## 常见问题排查

### 1\. 高丢包率问题

如果在某个节点出现高丢包率：

  * 可能是该节点过载
  * 可能是网络设备配置问题
  * 可能是ISP之间的互联问题



### 2\. 延迟突增问题

如果在某个节点延迟突然增加：

  * 可能是网络拥塞
  * 可能是路由变化
  * 可能是设备性能问题



### 3\. 星号(*)显示

如果看到星号(*)而不是IP地址：

  * 可能是该节点不响应ICMP请求
  * 可能是防火墙阻止了探测包



* * *

## mtr 与其他工具对比

工具 | 实时更新 | 双向诊断 | 丢包统计 | 延迟统计 | 交互式界面  
---|---|---|---|---|---  
ping | ❌ | ❌ | ✔️ | ✔️ | ❌  
traceroute | ❌ | ❌ | ❌ | ✔️ | ❌  
mtr | ✔️ | ✔️ | ✔️ | ✔️ | ✔️  
  
* * *

## 实践练习

  1. 使用mtr检查到你常用网站的网络路径
  2. 比较Wi-Fi和有线连接的网络质量差异
  3. 尝试用不同大小的ping包测试网络性能
  4. 设置一个定时任务，定期生成网络质量报告



## 实例

```bash
# 示例：每天生成网络状况报告 ( crontab -l 2 >/ dev / null; echo "0 2 * * * /usr/sbin/mtr -r -c 100 google.com > ~/network_report_ $(date +%Y%m%d) .txt" ) | crontab -
```


* * *

## 总结

mtr是一个功能强大的网络诊断工具，它结合了traceroute和ping的优点，提供了实时、全面的网络路径分析能力。通过本文的学习，你应该能够：

  1. 理解mtr的基本原理和工作方式
  2. 熟练使用mtr进行网络问题诊断
  3. 解读mtr输出的各项指标
  4. 应用mtr解决实际网络问题



掌握mtr命令将大大提升你排查网络问题的效率，是每个系统管理员和开发人员都应该具备的技能。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

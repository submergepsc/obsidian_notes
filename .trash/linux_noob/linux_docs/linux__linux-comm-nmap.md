# Linux nmap 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

nmap（Network Mapper）是 Linux 系统中最强大的网络探测和安全审计工具之一。它能够帮助系统管理员和网络安全专家：

  * 发现网络中的活动主机
  * 扫描开放的端口和服务
  * 识别操作系统类型和版本
  * 检测网络服务的漏洞



nmap 因其灵活性、强大功能和跨平台特性，被广泛应用于网络安全评估、系统管理、网络监控等领域。

* * *

## 基本语法

nmap 的基本命令格式如下：

```bash
nmap [扫描类型] [选项] {目标规范}
```


其中：

  * `扫描类型`：指定 nmap 使用的扫描技术
  * `选项`：配置扫描行为的各种参数
  * `目标规范`：可以是一个IP地址、主机名或IP范围



* * *

## 常用扫描类型

### TCP SYN 扫描 (-sS)

最常用且默认的扫描方式，也称为"半开扫描"：

```bash
nmap -sS 192.168.1.1
```


特点：

  * 快速且隐蔽
  * 不完成TCP三次握手
  * 需要root权限



### TCP 连接扫描 (-sT)

标准的TCP连接扫描：

```bash
nmap -sT 192.168.1.1
```


特点：

  * 不需要root权限
  * 会建立完整TCP连接
  * 速度较慢且容易被检测



### UDP 扫描 (-sU)

扫描UDP端口：

```bash
nmap -sU 192.168.1.1
```


特点：

  * UDP扫描速度较慢
  * 许多UDP服务不响应
  * 需要root权限



### 操作系统检测 (-O)

识别目标主机的操作系统：

```bash
nmap -O 192.168.1.1
```


* * *

## 常用选项参数

### 端口指定 (-p)

扫描特定端口或端口范围：

## 实例

```bash
nmap -p 80 , 443 192.168.1.1 # 扫描80和443端口 nmap -p 1 \- 100 192.168.1.1 # 扫描1-100端口 nmap -p- 192.168.1.1 # 扫描所有65535个端口
```


### 服务版本检测 (-sV)

探测服务的详细版本信息：

```bash
nmap -sV 192.168.1.1
```


### 扫描速度 (-T)

控制扫描速度（0-5，数字越大越快）：

```bash
nmap -T4 192.168.1.1 # 较快的扫描速度
```


### 输出格式

多种输出格式选项：

## 实例

```bash
nmap -oN result.txt 192.168.1.1 # 普通文本格式 nmap -oX result.xml 192.168.1.1 # XML格式 nmap -oG result.gnmap 192.168.1.1 # grepable格式
```


* * *

## 实用示例

### 基本网络扫描

```bash
nmap 192.168.1.1
```


输出示例：

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2023-05-01 10:00 UTC Nmap scan report for 192.168.1.1 Host is up (0.045s latency). Not shown: 998 closed ports PORT STATE SERVICE 22/tcp open ssh 80/tcp open http 443/tcp open https
```


### 全面扫描（操作系统+服务版本）

```bash
nmap -A 192.168.1.1
```


### 扫描整个子网

```bash
nmap 192.168.1.0/24
```


### 从文件读取目标列表

```bash
nmap -iL targets.txt
```


* * *

## 扫描结果解读

nmap 输出中的端口状态含义：

状态 | 说明  
---|---  
open | 端口开放且有应用程序监听  
closed | 端口关闭（主机可达，但没有应用程序监听）  
filtered | 端口被防火墙/网络过滤，无法确定状态  
unfiltered | 端口可访问，但无法确定开放或关闭（用于ACK扫描）  
open|filtered | 无法确定端口是开放还是被过滤（UDP扫描常见）  
closed|filtered | 无法确定端口是关闭还是被过滤  
  
* * *

## 安全与法律注意事项

  1. **合法使用** ：仅扫描你有权限扫描的网络和系统
  2. **获取授权** ：在企业网络中使用前，确保获得书面授权
  3. **避免滥用** ：大量快速扫描可能被视为攻击行为
  4. **尊重隐私** ：不要扫描不属于你的网络资源



* * *

## 进阶技巧

### 绕过防火墙

## 实例

```bash
nmap -f \--mtu 24 192.168.1.1 # 使用分片 nmap \--data-length 100 192.168.1.1 # 添加随机数据 nmap -D RND: 5 192.168.1.1 # 诱饵扫描
```


### 定时扫描脚本

## 实例

```bash
#!/bin/bash DATE =$ ( date \+ % Y % m % d ) nmap -sS -p- -T4 -oN scan_ $DATE .log 192.168.1.0 / 24
```


### 结果比较

```bash
ndiff scan1.xml scan2.xml
```


* * *

## 常见问题解答

**Q: nmap 扫描为什么需要 root 权限？** A: 某些扫描类型（如SYN扫描）需要直接操作网络数据包，这需要root权限。

**Q: 如何加快扫描速度？** A: 使用 `-T4` 或 `-T5` 选项，减少超时时间，或限制扫描端口范围。

**Q: nmap 扫描会被防火墙检测到吗？** A: 取决于扫描类型和防火墙配置。SYN扫描比全连接扫描更隐蔽。

**Q: 如何扫描IPv6地址？** A: 直接使用IPv6地址即可：`nmap 2001:db8::1`

* * *

## 学习资源推荐

  1. 官方文档：`man nmap`
  2. Nmap官方书籍：《Nmap Network Scanning》
  3. 在线教程：<https://nmap.org/book/toc.html>
  4. 交互式学习：<https://tryhackme.com/room/furthernmap>



通过掌握nmap，你将拥有强大的网络探测能力，为系统管理和网络安全工作打下坚实基础。建议从简单扫描开始，逐步尝试更复杂的选项和技巧。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

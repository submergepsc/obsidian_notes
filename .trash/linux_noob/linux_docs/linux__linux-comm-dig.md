# Linux dig 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

dig (Domain Information Groper) 是 Linux 系统中一个功能强大的 DNS 查询工具，用于查询 DNS 域名服务器。与传统的 nslookup 相比，dig 提供了更详细的查询结果和更灵活的查询选项。

dig 命令的主要特点：

  * 显示完整的 DNS 查询过程
  * 支持所有 DNS 记录类型查询
  * 可以指定查询特定的 DNS 服务器
  * 输出格式清晰易读



* * *

## dig 命令基本语法

```bash
dig [@server] [domain] [query-type] [query-class] [query-options]
```


### 参数说明

参数 | 说明  
---|---  
`@server` | 指定要查询的 DNS 服务器（如 `@8.8.8.8`）  
`domain` | 要查询的域名（如 `example.com`）  
`query-type` | 查询的记录类型（如 `A`, `MX`, `NS` 等）  
`query-class` | 查询的类别（通常为 `IN` 表示 Internet）  
`query-options` | 额外的查询选项  
  
* * *

## 常用查询类型

dig 支持查询多种 DNS 记录类型，以下是常见的记录类型：

记录类型 | 说明 | 示例  
---|---|---  
A | IPv4 地址记录 | `dig example.com A`  
AAAA | IPv6 地址记录 | `dig example.com AAAA`  
MX | 邮件交换记录 | `dig example.com MX`  
NS | 域名服务器记录 | `dig example.com NS`  
CNAME | 规范名称记录 | `dig www.example.com CNAME`  
TXT | 文本记录 | `dig example.com TXT`  
SOA | 授权起始记录 | `dig example.com SOA`  
ANY | 所有记录 | `dig example.com ANY`  
  
* * *

## dig 命令输出解析

执行一个简单的 dig 查询：

```bash
dig example.com
```


典型输出包含以下几个部分：

  1. **HEADER 部分** ：显示查询的基本信息

     * `opcode`：操作码
     * `status`：响应状态
     * `id`：查询 ID
     * `flags`：标志位（如 qr, rd, ra 等）
  2. **QUESTION 部分** ：显示查询的问题

     * 包含查询的域名和记录类型
  3. **ANSWER 部分** ：查询结果

     * 包含实际的 DNS 记录信息
  4. **AUTHORITY 部分** ：权威域名服务器信息

     * 显示负责该域名的权威 DNS 服务器
  5. **ADDITIONAL 部分** ：附加信息

     * 可能包含额外的有用信息
  6. **STATISTICS 部分** ：查询统计

     * 显示查询耗时、服务器等信息



* * *

## 实用查询示例

### 1\. 查询特定 DNS 服务器

```bash
dig @8.8.8.8 example.com
```


这个命令会向 Google 的公共 DNS 服务器 (8.8.8.8) 查询 example.com 的 A 记录。

### 2\. 查询 MX 记录

```bash
dig example.com MX
```


查询域名的邮件服务器信息。

### 3\. 查询域名解析的完整过程

```bash
dig +trace example.com
```


`+trace` 选项会显示从根域名服务器开始的完整解析过程。

### 4\. 简短输出模式

```bash
dig +short example.com
```


只显示查询结果，不显示其他详细信息。

### 5\. 反向 DNS 查询

```bash
dig -x 8.8.8.8
```


通过 IP 地址查询对应的域名。

### 6\. 批量查询多个域名

```bash
dig -f domains.txt +short
```


其中 domains.txt 包含要查询的域名列表，每行一个。

* * *

## 高级选项

### 1\. 控制输出格式

```bash
dig +noall +answer example.com
```


`+noall` 隐藏所有部分，`+answer` 只显示 ANSWER 部分。

### 2\. 设置查询超时

```bash
dig +time=5 example.com
```


设置查询超时时间为 5 秒。

### 3\. 指定查询端口

```bash
dig @dns.server.example.com -p 5353 example.com
```


在非标准端口 (5353) 上查询 DNS 服务器。

### 4\. 显示 TTL 信息

```bash
dig +ttlid example.com
```


显示记录的 TTL (Time To Live) 值。

### 5\. 显示查询统计

```bash
dig +stats example.com
```


显示详细的查询统计信息。

* * *

## 常见问题解答

### 1\. dig 和 nslookup 有什么区别？

dig 提供了比 nslookup 更详细的输出和更多的查询选项，是更专业的 DNS 查询工具。nslookup 已经逐渐被 dig 取代。

### 2\. 如何安装 dig 命令？

在大多数 Linux 发行版中，dig 是 bind-utils 或 dnsutils 包的一部分：

  * Debian/Ubuntu:

```bash
sudo apt install dnsutils
```

  * CentOS/RHEL:

```bash
sudo yum install bind-utils
```




### 3\. 为什么我的 dig 查询没有返回 ANSWER 部分？

可能的原因：

  * 查询的记录类型不存在
  * 域名不存在
  * DNS 服务器没有该域名的记录
  * 网络连接问题



可以尝试使用 `+trace` 选项查看完整的解析过程。

* * *

## 实际应用场景

### 1\. 排查 DNS 解析问题

当网站无法访问时，可以使用 dig 检查 DNS 解析是否正常：

```bash
dig +trace example.com
```


### 2\. 检查邮件服务器配置

验证域名的邮件服务器配置是否正确：

```bash
dig example.com MX
```


### 3\. 监控 DNS 记录变更

通过定期执行 dig 查询并比较结果，可以监控 DNS 记录的变更：

## 实例

```bash
dig example.com A | grep -v ";" > current.txt diff current.txt previous.txt
```


### 4\. 测试 DNS 服务器响应时间

比较不同 DNS 服务器的响应速度：

## 实例

```bash
time dig @ 8.8.8.8 example.com time dig @ 1.1.1.1 example.com
```


* * *

## 总结

dig 命令是 Linux 系统管理员和网络工程师必备的 DNS 诊断工具。通过本文的学习，你应该能够：

  1. 理解 dig 命令的基本语法和常用选项
  2. 查询各种类型的 DNS 记录
  3. 解析 dig 命令的输出结果
  4. 使用 dig 解决实际的 DNS 相关问题
  5. 掌握 dig 的高级用法和技巧



要深入了解 dig 命令，可以查看其手册页：

```bash
man dig
```


或者使用帮助选项：

```bash
dig -h
```


* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

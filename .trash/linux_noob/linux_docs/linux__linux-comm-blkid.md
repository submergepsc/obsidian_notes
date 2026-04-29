# Linux blkid 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 什么是 blkid 命令

`blkid` 是 Linux 系统中一个用于识别块设备属性的实用工具。它可以显示块设备（如硬盘、分区、USB 设备等）的文件系统类型、UUID（通用唯一标识符）、标签（LABEL）以及其他相关信息。

### 主要功能

  * 识别存储设备的文件系统类型
  * 获取设备的唯一标识符（UUID）
  * 查看设备的分区标签（LABEL）
  * 显示块设备的大小和其他属性



* * *

## 基本语法

```bash
blkid [选项] [设备...]
```


### 常用选项参数说明

选项 | 说明  
---|---  
`-c <缓存文件>` | 指定缓存文件（默认为 /etc/blkid.tab）  
`-g` | 收集垃圾数据到缓存文件  
`-o <格式>` | 指定输出格式（full, value, list, device, udev）  
`-p` | 低级别超级块探测（绕过缓存）  
`-s <标签>` | 显示指定标签的信息（如 UUID, TYPE, LABEL 等）  
`-U <UUID>` | 根据 UUID 查找对应的设备  
`-L <标签>` | 根据 LABEL 查找对应的设备  
`-i` | 显示有关 I/O 限制的信息  
`-h` | 显示帮助信息  
`-V` | 显示版本信息  
  
* * *

## 使用示例

### 1\. 查看所有块设备信息

## 实例

```bash
sudo blkid
```


输出示例：

```bash
/dev/sda1: UUID=&quot;5a3a1e7b-1a2b-4c3d-8e9f-0a1b2c3d4e5f&quot; TYPE=&quot;ext4&quot; /dev/sda2: UUID=&quot;6b4c5d6e-7f8g-9h0i-1j2k-3l4m5n6o7p8q&quot; TYPE=&quot;swap&quot; /dev/sdb1: LABEL=&quot;DATA&quot; UUID=&quot;9a8b7c6d-5e4f-3g2h-1i0j-9k8l7m6n5o4p&quot; TYPE=&quot;xfs&quot;
```


### 2\. 查看特定设备信息

## 实例

```bash
sudo blkid / dev / sda1
```


输出示例：

```bash
/dev/sda1: UUID=&quot;5a3a1e7b-1a2b-4c3d-8e9f-0a1b2c3d4e5f&quot; TYPE=&quot;ext4&quot;
```


### 3\. 仅显示 UUID 信息

## 实例

```bash
sudo blkid -s UUID -o value / dev / sda1
```


输出示例：

```bash
5a3a1e7b-1a2b-4c3d-8e9f-0a1b2c3d4e5f
```


### 4\. 根据 UUID 查找设备

## 实例

```bash
sudo blkid -U 5a3a1e7b-1a2b-4c3d-8e9f-0a1b2c3d4e5f
```


输出示例：

```bash
/dev/sda1
```


### 5\. 使用列表格式输出

## 实例

```bash
sudo blkid -o list
```


输出示例：

```bash
device fs_type label mount point UUID \------------------------------------------------------------------------------- /dev/sda1 ext4 / 5a3a1e7b-1a2b-4c3d-8e9f-0a1b2c3d4e5f /dev/sda2 swap [SWAP] 6b4c5d6e-7f8g-9h0i-1j2k-3l4m5n6o7p8q /dev/sdb1 xfs DATA /mnt/data 9a8b7c6d-5e4f-3g2h-1i0j-9k8l7m6n5o4p
```


* * *

## 实际应用场景

### 1\. 在 fstab 中使用 UUID 挂载

编辑 `/etc/fstab` 文件时，使用 UUID 比使用设备名更可靠，因为设备名可能会变化：

## 实例

```bash
UUID =5a3a1e7b-1a2b-4c3d-8e9f-0a1b2c3d4e5f / ext4 defaults 0 1
```


### 2\. 自动化脚本中识别设备

在脚本中，可以使用 blkid 来识别特定设备：

## 实例

```bash
#!/bin/bash DATA_PARTITION =$ ( sudo blkid -L "DATA" ) if [ -n " $DATA_PARTITION " ] ; then echo "找到数据分区: $DATA_PARTITION " mount $DATA_PARTITION / mnt / data else echo "未找到数据分区" fi
```


### 3\. 检测未挂载的文件系统

## 实例

```bash
sudo blkid | grep -v " $(mount | awk '{print $1}') "
```


* * *

## 常见问题解答

### Q1: 为什么需要使用 sudo 执行 blkid？

A: 普通用户可能没有权限访问某些设备信息，使用 sudo 可以确保获取完整的设备信息。

### Q2: blkid 和 lsblk 有什么区别？

A: 

  * `lsblk` 主要显示块设备的层次结构和基本信息（名称、大小、挂载点等）
  * `blkid` 专注于显示文件系统相关的详细信息（UUID、TYPE、LABEL 等）



### Q3: 如何更新 blkid 的缓存？

A: 可以使用以下命令更新缓存：

## 实例

```bash
sudo blkid -g
```


或者完全绕过缓存使用低级探测：

## 实例

```bash
sudo blkid -p
```


* * *

## 总结

`blkid` 命令是 Linux 系统管理中非常有用的工具，特别是在处理存储设备和文件系统时。通过本文的学习，你应该能够：

  1. 理解 blkid 的基本功能和语法
  2. 使用各种选项获取特定的设备信息
  3. 在实际场景中应用 blkid 命令
  4. 解决与设备识别相关的常见问题



掌握 blkid 命令将帮助你更有效地管理 Linux 系统中的存储设备。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

# Linux lsblk 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 1\. 基本概念

`lsblk` 是 Linux 系统中的一个实用命令，用于列出系统中所有可用的块设备信息。块设备是指以块为单位进行数据读写的存储设备，如硬盘、SSD、U盘等。

### 1.1 命令名称含义

  * `ls`：list 的缩写，表示列出
  * `blk`：block 的缩写，表示块设备
  * 组合起来就是"列出块设备"的意思



### 1.2 主要功能

  * 显示所有块设备的树状结构
  * 展示设备的基本信息（名称、大小、类型等）
  * 显示设备的分区情况
  * 展示设备的挂载点信息



* * *

## 2\. 命令语法

```bash
lsblk [选项] [设备...]
```


### 2.1 参数说明

  * 如果不指定任何参数，`lsblk` 会列出所有块设备
  * 可以指定一个或多个设备名称作为参数，只显示这些设备的信息



### 2.2 常用选项

选项 | 说明  
---|---  
`-a` | 显示所有设备（包括空设备）  
`-b` | 以字节为单位显示设备大小  
`-d` | 仅显示设备本身，不显示分区  
`-e` | 排除指定主设备号的设备  
`-f` | 显示文件系统信息  
`-i` | 使用 ASCII 字符显示树状结构  
`-J` | 以 JSON 格式输出  
`-l` | 使用列表格式输出（非树状）  
`-m` | 显示设备的所有者信息和权限  
`-n` | 不显示标题行  
`-o` | 指定要显示的列  
`-P` | 以键值对格式输出  
`-r` | 使用原始格式输出  
`-S` | 仅显示 SCSI 设备  
`-t` | 显示设备的拓扑信息  
`-x` | 按指定列排序  
  
* * *

## 3\. 输出字段说明

默认情况下，`lsblk` 命令会显示以下列：

列名 | 说明  
---|---  
NAME | 设备名称  
MAJ:MIN | 主设备号和次设备号  
RM | 是否为可移动设备（1表示是，0表示否）  
SIZE | 设备大小  
RO | 是否为只读设备（1表示是，0表示否）  
TYPE | 设备类型（disk, part, rom等）  
MOUNTPOINT | 设备的挂载点  
  
* * *

## 4\. 实用示例

### 4.1 基本用法：列出所有块设备

## 实例

```bash
lsblk
```


示例输出：

```bash
NAME MAJ:MIN RM SIZE RO TYPE MOUNTPOINT sda 8:0 0 238.5G 0 disk ├─sda1 8:1 0 512M 0 part /boot/efi ├─sda2 8:2 0 732M 0 part /boot └─sda3 8:3 0 237.3G 0 part └─sda3_crypt 253:0 0 237.3G 0 crypt ├─vgubuntu-root │ 253:1 0 236.3G 0 lvm / └─vgubuntu-swap_1 253:2 0 976M 0 lvm [SWAP] sr0 11:0 1 1024M 0 rom
```


### 4.2 显示文件系统信息

## 实例

```bash
lsblk -f
```


示例输出：

```bash
NAME FSTYPE LABEL UUID MOUNTPOINT sda ├─sda1 vfat 67E3-17ED /boot/efi ├─sda2 ext4 5b3e5a5e-2a9d-4a3e-9b1e-1e1e1e1e1e1e /boot └─sda3 crypto_LUKS 6c3e5a5e-3a9d-5b3e-9b1e-2e2e2e2e2e2e └─sda3_crypt LVM2_member ├─vgubuntu-root │ ext4 7d3e5a5e-4a9d-6c3e-9b1e-3e3e3e3e3e3e / └─vgubuntu-swap_1 swap 8e3e5a5e-5a9d-7d3e-9b1e-4e4e4e4e4e4e [SWAP]
```


### 4.3 自定义输出列

## 实例

```bash
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT,FSTYPE
```


### 4.4 以列表格式显示

## 实例

```bash
lsblk -l
```


### 4.5 显示设备所有者信息

## 实例

```bash
lsblk -m
```


### 4.6 仅显示磁盘设备（不显示分区）

## 实例

```bash
lsblk -d
```


### 4.7 以 JSON 格式输出

## 实例

```bash
lsblk -J
```


* * *

## 5\. 实际应用场景

### 5.1 查看新插入的U盘或移动硬盘

## 实例

```bash
# 插入U盘前先执行 lsblk > before.txt # 插入U盘后执行 lsblk > after.txt # 比较差异 diff before.txt after.txt
```


### 5.2 查找未挂载的分区

## 实例

```bash
lsblk -f | grep -v "MOUNTPOINT" | grep -v "FSTYPE"
```


### 5.3 查看设备的物理拓扑结构

## 实例

```bash
lsblk -t
```


### 5.4 监控设备变化

## 实例

```bash
watch -n 1 lsblk
```


* * *

## 6\. 常见问题解答

### 6.1 lsblk 和 df 命令有什么区别？

  * `lsblk` 显示的是块设备及其分区结构
  * `df` 显示的是已挂载文件系统的磁盘空间使用情况
  * `lsblk` 更适合查看设备物理结构，`df` 更适合查看磁盘空间使用情况



### 6.2 为什么有些设备没有显示大小？

可能是这些设备没有有效的分区表或未被系统识别。可以尝试使用 `-a` 选项查看所有设备。

### 6.3 如何只显示特定类型的设备？

## 实例

```bash
# 只显示磁盘 lsblk -d -o NAME,RO,TYPE,SIZE,MOUNTPOINT | grep disk # 只显示分区 lsblk -o NAME,RO,TYPE,SIZE,MOUNTPOINT | grep part
```


* * *

## 7\. 总结

`lsblk` 是 Linux 系统管理员和用户必备的磁盘管理工具，它提供了直观的树状视图来展示块设备及其分区关系。通过不同的选项组合，可以获取各种详细的设备信息，对于磁盘管理、故障排查和系统维护都非常有用。

记住常用选项：

  * `-f` 查看文件系统信息
  * `-o` 自定义输出列
  * `-J` 获取 JSON 格式输出
  * `-m` 查看权限信息



掌握 `lsblk` 命令，可以让你更高效地管理 Linux 系统中的存储设备。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

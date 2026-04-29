# Linux parted 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 一、parted 命令概述

parted 是 Linux 系统中一个功能强大的磁盘分区工具，它支持多种分区表类型（如 GPT 和 MBR），能够创建、删除、调整和管理磁盘分区。与传统的 fdisk 相比，parted 特别适合处理大容量磁盘（超过 2TB）和现代分区需求。

### 主要特点

  * **交互式与非交互式** ：支持命令行直接操作和交互式操作两种模式
  * **即时生效** ：大多数操作会立即写入磁盘，无需额外确认
  * **多种文件系统支持** ：ext2/3/4、xfs、btrfs、fat、ntfs 等
  * **无损调整** ：可以调整分区大小而不丢失数据（需文件系统支持）



* * *

## 二、安装与基本语法

### 安装 parted

大多数 Linux 发行版已预装 parted，如需安装：

```bash
# Debian/Ubuntu sudo apt install parted # CentOS/RHEL sudo yum install parted
```


### 基本命令语法

## 实例

```bash
parted [ 选项 ] [ 设备 ] [ 命令 [ 参数 ] ]
```


### 常用选项

选项 | 说明  
---|---  
`-l` | 列出所有块设备的分区信息  
`-s` | 脚本模式（非交互式）  
`-a` | 设置对齐类型（min/opt/none）  
`-f` | 抑制部分警告信息  
  
* * *

## 三、交互式操作模式

### 进入交互模式

## 实例

```bash
sudo parted / dev / sdX
```


将 `/dev/sdX` 替换为你的实际设备名（如 `/dev/sda`）

### 交互模式常用命令

**查看帮助**

## 实例

```bash
help [命令名]
```


**查看分区表**

## 实例

```bash
print
```


**切换单位**

## 实例

```bash
unit GB # 切换为GB显示 unit MB # 切换为MB显示
```


**创建新分区**

## 实例

```bash
mkpart [分区类型] [文件系统类型] 起始位置 结束位置
```


示例：

## 实例

```bash
mkpart primary ext4 1GB 10GB
```


**删除分区**

## 实例

```bash
rm [分区号]
```


**调整分区大小**

## 实例

```bash
resizepart [分区号] 结束位置
```


**设置分区标志**

## 实例

```bash
set [分区号] [标志] on/off
```


常用标志：`boot`, `lvm`, `raid`, `swap` 等

**退出**

## 实例

```bash
quit
```


* * *

## 四、常用操作示例

### 示例1：查看所有磁盘分区

## 实例

```bash
sudo parted -l
```


输出示例：

```bash
Model: ATA ST1000DM010-2EP1 (scsi) Disk /dev/sda: 1000GB Sector size (logical/physical): 512B/4096B Partition Table: gpt Disk Flags: Number Start End Size File system Name Flags 1 1049kB 538MB 537MB fat32 boot, esp 2 538MB 1000GB 999GB ext4
```


### 示例2：创建新分区表（GPT格式）

## 实例

```bash
sudo parted / dev / sdb mklabel gpt
```


### 示例3：创建主分区（非交互式）

## 实例

```bash
sudo parted -s / dev / sdb mkpart primary ext4 1MiB 10GiB
```


### 示例4：调整分区大小

## 实例

```bash
sudo parted -s / dev / sdb resizepart 2 20GiB
```


### 示例5：设置启动标志

## 实例

```bash
sudo parted -s / dev / sda set 1 boot on
```


* * *

## 五、高级功能与注意事项

### 1\. 分区对齐优化

现代磁盘（特别是SSD）需要正确的分区对齐以获得最佳性能：

## 实例

```bash
sudo parted -a optimal / dev / sdb mkpart primary ext4 0 % 100 %
```


### 2\. 转换分区表类型

## 实例

```bash
sudo parted / dev / sdb mklabel msdos # 转换为MBR sudo parted / dev / sdb mklabel gpt # 转换为GPT
```


⚠️ 注意：这会删除磁盘上所有分区！

### 3\. 文件系统操作

parted 只管理分区，创建文件系统需要额外命令：

## 实例

```bash
sudo mkfs.ext4 / dev / sdb1
```


### 4\. 注意事项

  * **数据安全** ：分区操作可能导致数据丢失，务必提前备份
  * **分区使用中** ：不能修改已挂载的分区
  * **大小单位** ：明确指定单位（如GB/MB），否则默认使用字节
  * **GPT vs MBR** ：超过2TB的磁盘必须使用GPT分区表



* * *

## 六、parted 与 fdisk/gdisk 对比

特性 | parted | fdisk | gdisk  
---|---|---|---  
交互模式 | 支持 | 支持 | 支持  
脚本模式 | 支持 | 不支持 | 不支持  
GPT支持 | 是 | 有限支持 | 是  
大磁盘支持 | 是 | 否（仅MBR） | 是  
即时写入 | 是 | 否（需w命令） | 否（需w命令）  
调整分区大小 | 是 | 否 | 否  
  
[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

# Linux btrfs 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

Btrfs（B-tree File System）是一种先进的 Linux 文件系统，由 Oracle 开发并于 2007 年首次发布。它的设计目标是解决传统文件系统的局限性，提供更好的扩展性、可靠性和管理功能。

### 核心特性

  * **写时复制（CoW）** ：所有写入操作都不会覆盖原有数据，而是创建新副本
  * **快照功能** ：可以快速创建文件系统的即时快照，几乎不占用额外空间
  * **子卷管理** ：支持将文件系统划分为多个独立的子卷
  * **数据校验和** ：自动检测数据损坏
  * **透明压缩** ：支持文件数据的实时压缩和解压
  * **RAID 支持** ：内置多种 RAID 级别支持



* * *

## btrfs 基本命令语法

```bash
btrfs [选项] [子命令选项] [参数]
```


### 常用选项

选项 | 描述  
---|---  
`-v` | 详细输出模式  
`--help` | 显示帮助信息  
`--version` | 显示版本信息  
  
* * *

## 主要子命令详解

### 文件系统创建与管理

#### 创建 btrfs 文件系统

## 实例

```bash
# 在设备上创建 btrfs 文件系统 sudo mkfs.btrfs / dev / sdX # 创建带标签的文件系统 sudo mkfs.btrfs -L mylabel / dev / sdX # 使用多个设备创建 RAID1 sudo mkfs.btrfs -m raid1 -d raid1 / dev / sdX / dev / sdY
```


#### 挂载 btrfs 文件系统

## 实例

```bash
# 基本挂载 sudo mount / dev / sdX / mnt / btrfs # 启用压缩（推荐 lzo 或 zstd） sudo mount -o compress =lzo / dev / sdX / mnt / btrfs # 显示挂载选项 mount | grep btrfs
```


### 子卷操作

#### 创建子卷

## 实例

```bash
# 创建子卷 sudo btrfs subvolume create / mnt / btrfs / subvol1 # 列出子卷 sudo btrfs subvolume list / mnt / btrfs # 删除子卷 sudo btrfs subvolume delete / mnt / btrfs / subvol1
```


#### 快照管理

## 实例

```bash
# 创建快照 sudo btrfs subvolume snapshot / mnt / btrfs / mnt / btrfs / snapshot_$ ( date \+ % Y % m % d ) # 只读快照 sudo btrfs subvolume snapshot -r / mnt / btrfs / mnt / btrfs / readonly_snap # 删除快照 sudo btrfs subvolume delete / mnt / btrfs / snapshot_20230101
```


### 空间管理

#### 查看文件系统使用情况

## 实例

```bash
# 显示详细空间信息 sudo btrfs filesystem usage / mnt / btrfs # 显示磁盘使用情况 sudo btrfs filesystem df / mnt / btrfs # 平衡数据分布（谨慎使用，可能耗时） sudo btrfs balance start / mnt / btrfs
```


#### 调整文件系统大小

## 实例

```bash
# 扩大文件系统 sudo btrfs filesystem resize +10G / mnt / btrfs # 缩小文件系统 sudo btrfs filesystem resize -5G / mnt / btrfs
```


### 数据完整性检查

#### 检查文件系统

## 实例

```bash
# 只读检查 sudo btrfs check / dev / sdX # 尝试修复（谨慎使用） sudo btrfs check \--repair / dev / sdX
```


#### 清理和修复

## 实例

```bash
# 清理空闲空间 sudo btrfs filesystem defrag / mnt / btrfs # 检查并修复文件系统 sudo btrfs scrub start / mnt / btrfs # 查看修复状态 sudo btrfs scrub status / mnt / btrfs
```


* * *

## 实际应用示例

### 示例 1：设置带压缩的 btrfs 主目录

## 实例

```bash
# 创建分区 sudo mkfs.btrfs -L home / dev / sdX # 挂载并启用压缩 sudo mount -o compress =zstd / dev / sdX / mnt / newhome # 复制现有数据 sudo rsync -avx / home / / mnt / newhome / # 更新 fstab 实现自动挂载 echo "UUID= $(blkid -s UUID -o value /dev/sdX) /home btrfs defaults,compress=zstd 0 2" | sudo tee -a / etc / fstab # 重新挂载 sudo umount / mnt / newhome sudo mount -a
```


### 示例 2：定期快照和清理

## 实例

```bash
#!/bin/bash # 创建每日快照 SNAP_DIR = "/mnt/btrfs/.snapshots" mkdir -p " $SNAP_DIR " sudo btrfs subvolume snapshot -r / mnt / btrfs " $SNAP_DIR / $(date +%Y%m%d) " # 保留最近7天的快照 find " $SNAP_DIR " -mindepth 1 -maxdepth 1 -type d -name "2*" | sort -r | tail -n \+ 8 | xargs -r sudo btrfs subvolume delete
```


* * *

## 常见问题解决

### 问题 1：空间不足但 df 显示有空间

## 实例

```bash
# 检查未删除的快照占用空间 sudo btrfs subvolume list -s / mnt / btrfs # 清理不需要的快照 sudo btrfs subvolume delete / mnt / btrfs / old_snapshot
```


### 问题 2：平衡操作卡住

## 实例

```bash
# 查看平衡状态 sudo btrfs balance status / mnt / btrfs # 暂停平衡操作 sudo btrfs balance pause / mnt / btrfs # 恢复平衡操作 sudo btrfs balance resume / mnt / btrfs
```


### 问题 3：挂载失败

## 实例

```bash
# 检查文件系统 sudo btrfs check / dev / sdX # 尝试修复 sudo btrfs rescue zero-log / dev / sdX sudo mount / dev / sdX / mnt / btrfs
```


* * *

## 最佳实践建议

  1. **启用压缩** ：特别是对于文本、日志等可压缩数据

```bash
# 推荐使用 zstd 压缩算法 mount -o compress=zstd /dev/sdX /mnt/btrfs
```

  2. **定期创建快照** ：重要操作前手动创建快照

  3. **监控空间使用** ：btrfs 的空间报告与传统文件系统不同

  4. **避免 100% 满** ：保持至少 5-10% 的可用空间

  5. **谨慎使用 balance** ：仅在必要时执行，可能非常耗时

  6. **考虑 RAID 配置** ：对于重要数据使用 RAID1 或 RAID10

  7. **定期执行 scrub** ：检查数据完整性

```bash
# 每月执行一次数据检查 sudo btrfs scrub start /mnt/btrfs
```




* * *

通过本文，您应该已经掌握了 btrfs 文件系统的基本操作和管理方法。btrfs 的强大功能使其成为现代 Linux 系统的理想选择，特别适合需要高级存储功能的场景。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

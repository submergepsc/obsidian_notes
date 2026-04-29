# Linux partprobe 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

partprobe 是 Linux 系统中一个用于通知操作系统重新读取分区表的实用工具。当你在不重启系统的情况下修改了磁盘分区表后，partprobe 可以帮助内核识别这些变更。

* * *

## 为什么需要 partprobe

在 Linux 系统中，当你使用 fdisk、parted 等工具修改磁盘分区后，这些变更不会立即被内核识别。传统做法是重启系统，但这在生产环境中往往不可行。partprobe 提供了一种无需重启就能让内核重新读取分区表的方法。

* * *

## 命令语法

```bash
partprobe [选项] [设备...]
```


* * *

## 常用选项参数

选项 | 说明  
---|---  
`-d` | 不更新内核  
`-s` | 显示摘要信息  
`-h` | 显示帮助信息  
`-v` | 显示版本信息  
  
* * *

## 使用示例

### 基本用法

重新读取指定磁盘的分区表：

```bash
sudo partprobe /dev/sda
```


### 显示摘要信息

```bash
sudo partprobe -s
```


输出示例：

```bash
/dev/sda: msdos partitions 1 2 3
```


### 重新读取所有磁盘的分区表

```bash
sudo partprobe
```


* * *

## 工作原理

partprobe 通过向内核发送 BLKRRPART ioctl 请求来触发分区表重读。这个过程涉及以下步骤：

## 实例

```bash
sequenceDiagram 用户-&gt;&gt;partprobe: 执行命令 partprobe-&gt;&gt;内核: 发送BLKRRPART请求 内核-&gt;&gt;磁盘驱动: 重新读取分区表 磁盘驱动--&gt;&gt;内核: 返回新分区信息 内核--&gt;&gt;partprobe: 操作结果 partprobe--&gt;&gt;用户: 显示结果或错误
```


* * *

## 注意事项

  1. **权限要求** ：partprobe 通常需要 root 权限
  2. **使用场景** ：主要在使用分区工具修改分区表后使用
  3. **替代方案** ：也可以使用 `blockdev --rereadpt` 命令
  4. **风险提示** ：不当使用可能导致系统不稳定



* * *

## 常见问题解答

### Q: partprobe 和 partx 有什么区别？

A: partprobe 是通知内核重新读取整个分区表，而 partx 可以更精细地控制添加或删除特定分区。

### Q: 为什么执行 partprobe 后我的分区仍然不可见？

A: 可能原因包括：

  1. 分区表修改未正确写入磁盘
  2. 设备被其他进程占用
  3. 内核不支持新的分区类型



* * *

## 实际应用场景

### 场景1：扩展LVM物理卷

## 实例

```bash
# 1. 使用fdisk删除旧分区并创建更大的新分区 sudo fdisk / dev / sdb # 2. 让内核识别新分区表 sudo partprobe / dev / sdb # 3. 扩展物理卷 sudo pvresize / dev / sdb1
```


### 场景2：添加新分区后的处理

## 实例

```bash
# 1. 使用parted创建新分区 sudo parted / dev / sdc mkpart primary ext4 1GB 5GB # 2. 通知内核 sudo partprobe / dev / sdc # 3. 格式化新分区 sudo mkfs.ext4 / dev / sdc1
```


* * *

## 最佳实践

  1. 在执行分区操作前备份重要数据
  2. 使用 `lsblk` 或 `fdisk -l` 验证分区变更
  3. 在生产环境中，先在测试系统上验证分区方案
  4. 考虑使用 `-s` 选项先查看摘要信息



* * *

## 总结

partprobe 是 Linux 系统管理员维护磁盘分区的重要工具，它解决了修改分区表后需要重启系统的问题。掌握 partprobe 的使用方法可以显著提高磁盘管理的效率，特别是在需要频繁调整分区的环境中。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

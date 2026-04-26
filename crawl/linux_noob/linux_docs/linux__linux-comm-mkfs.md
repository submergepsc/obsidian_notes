# Linux mkfs 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux mkfs（英文全拼：make file system）命令用于在特定的分区上建立 linux 文件系统。

**使用方式** : 

```bash
mkfs [-V] [-t fstype] [fs-options] filesys [blocks]
```


**参数** ：

  * device ： 预备检查的硬盘分区，例如：/dev/sda1
  * -V : 详细显示模式
  * -t : 给定档案系统的型式，Linux 的预设值为 ext2
  * -c : 在制做档案系统前，检查该partition 是否有坏轨
  * -l bad_blocks_file : 将有坏轨的block资料加到 bad_blocks_file 里面
  * block : 给定 block 的大小



### 实例

在 /dev/hda5 上建一个 msdos 的档案系统，同时检查是否有坏轨存在，并且将过程详细列出来 :

```bash
mkfs -V -t msdos -c /dev/hda5
```


将sda6分区格式化为ext3格式

```bash
mkfs -t ext3 /dev/sda6
```


**注意** ：这里的文件系统是要指定的，比如 ext3 ；reiserfs ；ext2 ；fat32 ；msdos 等。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

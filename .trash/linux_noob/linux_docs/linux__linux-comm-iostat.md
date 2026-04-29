# Linux iostat 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 一、iostat 命令概述

iostat（Input/Output Statistics）是Linux系统下一个强大的性能监控工具，属于sysstat工具包的一部分。它主要用于监控系统的磁盘I/O活动情况和CPU使用情况。

### 1.1 基本功能

  * 监控系统磁盘I/O的读写速度
  * 查看CPU利用率
  * 统计设备负载情况
  * 识别I/O性能瓶颈



### 1.2 典型应用场景

  * 服务器性能调优
  * 存储设备性能分析
  * 系统瓶颈排查
  * 容量规划



* * *

## 二、安装与基本使用

### 2.1 安装方法

大多数Linux发行版默认不安装iostat，需要先安装sysstat包：

## 实例

```bash
# Ubuntu/Debian sudo apt-get install sysstat # CentOS/RHEL sudo yum install sysstat # Fedora sudo dnf install sysstat
```


### 2.2 基本命令格式

## 实例

```bash
iostat [ 选项 ] [ 时间间隔 ] [ 次数 ]
```


#### 简单示例

## 实例

```bash
# 显示一次所有设备的统计信息 iostat # 每2秒刷新一次，共显示5次 iostat 2 5
```


* * *

## 三、命令选项详解

### 3.1 常用选项

选项 | 说明  
---|---  
-c | 只显示CPU使用情况  
-d | 只显示磁盘使用情况  
-h | 以人类可读格式显示（如KB, MB, GB）  
-k | 以KB为单位显示数据  
-m | 以MB为单位显示数据  
-N | 显示设备映射名称  
-p | 显示指定设备或分区的统计信息  
-t | 显示时间戳  
-x | 显示扩展统计信息  
-y | 跳过首次统计（通常与时间间隔一起使用）  
  
### 3.2 高级选项

选项 | 说明  
---|---  
-z | 省略零活动设备的输出  
-j ID | 显示指定设备的持久名称  
\--dec={0|1|2} | 指定小数位数  
  
* * *

## 四、输出结果解读

### 4.1 CPU统计部分

```bash
avg-cpu: %user %nice %system %iowait %steal %idle 5.32 0.00 1.06 0.25 0.00 93.37
```


  * **%user** ：用户级别(应用程序)的CPU使用率
  * **%nice** ：优先级调整过的进程的CPU使用率
  * **%system** ：系统级别(内核)的CPU使用率
  * **%iowait** ：CPU等待I/O操作完成的时间百分比
  * **%steal** ：虚拟环境中的"被偷走"时间
  * **%idle** ：CPU空闲时间百分比



### 4.2 磁盘统计部分（基础）

```bash
Device: tps kB_read/s kB_wrtn/s kB_read kB_wrtn sda 1.02 12.34 5.67 1234567 567890
```


  * **tps** ：每秒传输次数(transfers per second)
  * **kB_read/s** ：每秒读取的数据量(KB)
  * **kB_wrtn/s** ：每秒写入的数据量(KB)
  * **kB_read** ：读取的总数据量(KB)
  * **kB_wrtn** ：写入的总数据量(KB)



### 4.3 扩展统计信息（-x选项）

```bash
Device: rrqm/s wrqm/s r/s w/s rkB/s wkB/s avgrq-sz avgqu-sz await r_await w_await svctm %util sda 0.00 0.50 1.00 0.50 12.00 4.00 21.33 0.02 10.00 8.00 14.00 6.00 0.90
```


  * **rrqm/s** ：每秒合并的读请求数
  * **wrqm/s** ：每秒合并的写请求数
  * **r/s** ：每秒完成的读I/O次数
  * **w/s** ：每秒完成的写I/O次数
  * **rkB/s** ：每秒读取的KB数
  * **wkB/s** ：每秒写入的KB数
  * **avgrq-sz** ：平均每次I/O操作的数据大小(扇区)
  * **avgqu-sz** ：平均I/O队列长度
  * **await** ：平均每次I/O操作的等待时间(毫秒)
  * **r_await** ：读操作的平均等待时间(毫秒)
  * **w_await** ：写操作的平均等待时间(毫秒)
  * **svctm** ：平均每次I/O操作的服务时间(毫秒)
  * **%util** ：设备带宽利用率百分比



* * *

## 五、实用示例分析

### 5.1 监控特定磁盘

## 实例

```bash
# 监控sda磁盘，每2秒刷新，共显示3次 iostat -d -x sda 2 3
```


### 5.2 综合监控CPU和磁盘

## 实例

```bash
# 监控CPU和磁盘，每5秒刷新，持续显示 iostat -c -d -x -t 5
```


### 5.3 以MB为单位显示

## 实例

```bash
# 以MB为单位显示磁盘统计信息 iostat -d -m
```


### 5.4 监控所有分区

## 实例

```bash
# 监控所有分区，包括LVM iostat -p ALL
```


* * *

## 六、性能指标解读与优化建议

### 6.1 关键性能指标

  1. **%util** ：设备利用率

     * > 80% 表示设备接近饱和

     * 持续100% 表示设备已成为瓶颈
  2. **await** ：I/O等待时间

     * 正常情况下应 < 10ms
     * > 50ms 表示可能存在性能问题

  3. **avgqu-sz** ：队列长度

     * > 1 表示设备可能过载




### 6.2 常见问题诊断

#### 问题1：高%util但低吞吐量

  * 可能原因：随机I/O过多
  * 解决方案：优化应用I/O模式，考虑使用SSD



#### 问题2：高await但低%util

  * 可能原因：控制器或总线瓶颈
  * 解决方案：检查HBA卡或存储控制器



#### 问题3：rkB/s或wkB/s异常高

  * 可能原因：应用大量读写
  * 解决方案：优化应用或增加缓存



* * *

## 七、与其他工具配合使用

### 7.1 结合vmstat

## 实例

```bash
# 同时监控内存和I/O vmstat 1 5 & iostat -x 1 5
```


### 7.2 结合sar

## 实例

```bash
# 查看历史I/O数据 sar -d
```


### 7.3 结合iotop

## 实例

```bash
# 找出具体的高I/O进程 iotop
```


* * *

## 八、总结与最佳实践

### 8.1 使用建议

  1. 生产环境监控时，建议使用-x选项获取详细数据
  2. 长期监控应结合sar收集历史数据
  3. 分析性能问题时，应同时关注CPU和I/O数据
  4. 比较不同时间段的统计数据更有意义



### 8.2 常用命令组合

## 实例

```bash
# 综合监控命令 iostat -c -d -x -t -m 5 # 只监控磁盘扩展信息 iostat -d -x 2 # 监控特定分区 iostat -p sda1 -x 1 10
```


通过掌握iostat命令，系统管理员可以有效地监控和分析Linux系统的I/O性能，及时发现和解决存储相关的性能瓶颈问题。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

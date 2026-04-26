# Linux dstat 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

dstat 是一个功能强大的 Linux 系统监控工具，它可以实时显示系统资源使用情况，包括 CPU、内存、磁盘、网络等关键指标。dstat 的设计目标是替代传统的 vmstat、iostat、netstat 等工具，提供一个统一的监控界面。

### dstat 的主要特点

  * **多功能集成** ：整合了多种系统监控工具的功能
  * **实时显示** ：可以持续刷新显示系统状态
  * **可定制性** ：允许用户选择要监控的特定指标
  * **彩色输出** ：默认使用彩色显示，便于识别异常值
  * **CSV 导出** ：支持将监控数据导出为 CSV 格式



* * *

## dstat 基本语法

dstat 的基本命令格式如下：

```bash
dstat [选项] [间隔时间] [执行次数]
```


### 常用参数说明

参数 | 说明  
---|---  
`-c` | 显示 CPU 使用情况  
`-d` | 显示磁盘读写情况  
`-m` | 显示内存使用情况  
`-n` | 显示网络状态  
`-l` | 显示系统负载  
`-p` | 显示进程状态  
`-s` | 显示交换分区使用情况  
`-t` | 显示时间戳  
`--output` | 将输出保存到 CSV 文件  
`--top-cpu` | 显示最耗 CPU 的进程  
`--top-mem` | 显示最耗内存的进程  
  
* * *

## 常用监控场景示例

### 1\. 基本系统监控

```bash
dstat -cdlmnpsy
```


这个命令会显示：

  * CPU 使用率
  * 磁盘读写
  * 系统负载
  * 内存使用
  * 网络状态
  * 进程状态
  * 交换分区使用情况



### 2\. 监控特定资源

## 实例

```bash
graph TD A[开始监控] --&gt; B{选择监控项} B --&gt;|CPU| C[dstat -c] B --&gt;|内存| D[dstat -m] B --&gt;|磁盘| E[dstat -d] B --&gt;|网络| F[dstat -n]
```


### 3\. 带时间戳的监控

```bash
dstat -t -cdm
```


输出示例：

```bash
\----system---- ----total-cpu-usage---- -dsk/total- ---memory-usage---- time |usr sys idl wai hiq siq| read writ| used buff cach free 12-05 14:30:01| 2 1 96 0 0 1| 12k 25k| 3.2G 1.1G 5.6G 2.4G 12-05 14:30:02| 3 1 95 0 0 1| 24k 18k| 3.2G 1.1G 5.6G 2.4G
```


### 4\. 保存监控结果到文件

```bash
dstat -cdm --output /tmp/dstat_output.csv 5 10
```


这个命令会：

  * 监控 CPU、磁盘和内存
  * 每 5 秒刷新一次
  * 共执行 10 次
  * 将结果保存到 /tmp/dstat_output.csv



* * *

## 高级用法

### 1\. 监控特定进程

```bash
dstat --top-cpu --top-mem
```


### 2\. 自定义监控项

```bash
dstat -c -d -n -N eth0,total
```


这个命令会监控：

  * CPU 使用情况
  * 磁盘活动
  * 网络流量（特定网卡 eth0 和总计）



### 3\. 组合使用插件

dstat 支持多种插件，可以通过逗号分隔：

```bash
dstat --time,proc,disk,net,tcp,load,sys
```


* * *

## 常见问题解答

### 1\. dstat 与 top 命令有什么区别？

特性 | dstat | top  
---|---|---  
显示方式 | 表格形式 | 列表形式  
监控范围 | 系统全局 | 主要是进程  
刷新方式 | 可自定义间隔 | 固定间隔  
数据导出 | 支持 CSV | 不支持  
  
### 2\. 如何安装 dstat？

在大多数 Linux 发行版中，可以通过包管理器安装：

## 实例

```bash
# Ubuntu/Debian sudo apt-get install dstat # CentOS/RHEL sudo yum install dstat # Fedora sudo dnf install dstat
```


### 3\. 如何解读 dstat 的输出？

  * **CPU 部分** ：usr(用户空间)、sys(系统空间)、idl(空闲)、wai(IO 等待)
  * **内存部分** ：used(已用)、buff(缓冲区)、cach(缓存)、free(空闲)
  * **磁盘部分** ：read(读取)、writ(写入)，单位通常是 KB/s



* * *

## 最佳实践建议

  1. **长期监控** ：对于服务器，建议使用 `--output` 参数将监控数据保存下来
  2. **问题诊断** ：当系统出现性能问题时，使用 `dstat -tcdmn` 快速查看各资源使用情况
  3. **基准测试** ：在进行系统调优前后，使用 dstat 记录性能数据对比
  4. **自定义视图** ：根据实际需求创建自己的 dstat 监控组合，保存为别名方便使用



* * *

## 总结

dstat 是 Linux 系统管理员和开发人员的强大工具，它提供了全面的系统监控能力，并且高度可定制。通过熟练掌握 dstat，你可以：

  1. 快速识别系统性能瓶颈
  2. 监控关键资源使用趋势
  3. 收集性能数据用于分析
  4. 替代多个单一功能的监控工具



建议读者在实际工作中多尝试不同的参数组合，找到最适合自己工作场景的监控方案。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

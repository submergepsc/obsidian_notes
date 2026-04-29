# Linux glances 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

glances 是一款跨平台的命令行系统监控工具，它能够以直观的方式展示 Linux 系统的各项性能指标。与传统的 top 或 htop 命令相比，glances 提供了更丰富的监控维度和更友好的用户界面。

**主要特点** ：

  * 实时监控 CPU、内存、磁盘、网络等核心指标
  * 支持彩色显示和动态刷新
  * 可通过 Web 界面远程访问
  * 低资源占用，适合长期运行
  * 支持插件扩展功能



* * *

## 安装 glances

### Ubuntu/Debian 系统

## 实例

```bash
sudo apt update sudo apt install glances
```


### CentOS/RHEL 系统

## 实例

```bash
sudo yum install epel-release sudo yum install glances
```


### 使用 pip 安装（所有 Linux 发行版）

```bash
pip install glances
```


* * *

## 基本使用方法

启动 glances 最简单的方式是直接输入命令：

```bash
glances
```


启动后，你会看到一个类似这样的动态监控界面：

```bash
CPU[|||||||||||||||||||||||||90.5%] RAM[|||||||||||||||||65.2%] SWAP[|3.1%] Load average: 1.78 1.23 0.89 NETWORK Rx/s Tx/s DISK I/O R/s W/s eth0 1.2Mb 560Kb sda 450Kb 1.2Mb wlan0 320Kb 120Kb sdb 0Kb 0Kb Processes: 156 total, 3 running, 153 sleeping
```


* * *

## 常用快捷键和交互命令

在 glances 运行界面中，可以使用以下快捷键：

快捷键 | 功能描述  
---|---  
`q` 或 `ESC` | 退出 glances  
`c` | 按 CPU 使用率排序进程  
`m` | 按内存使用率排序进程  
`i` | 显示/隐藏 I/O 速率  
`d` | 显示/隐藏磁盘 I/O  
`n` | 显示/隐藏网络信息  
`f` | 显示/隐藏文件系统信息  
`s` | 显示/隐藏传感器信息  
`w` | 删除警告日志  
`h` | 显示帮助信息  
  
* * *

## 重要命令行选项

glances 提供了丰富的命令行选项来定制监控行为：

### 显示控制选项

## 实例

```bash
glances -t 2 # 设置刷新间隔为2秒（默认1秒） glances \--disable-plugins fs, ip # 禁用文件系统和IP插件 glances \--percpu # 显示每个CPU核心的使用情况
```


### 输出格式选项

## 实例

```bash
glances \--csv # CSV格式输出 glances \--json # JSON格式输出 glances \--export influxdb # 输出到InfluxDB数据库
```


### 远程监控选项

## 实例

```bash
glances -s # 启动glances服务器模式 glances -c @ 192.168.1.100 # 连接到远程glances服务器 glances -w # 启用Web服务器模式（默认端口61208）
```


* * *

## 实际应用示例

### 示例1：监控特定进程

```bash
glances --process-name nginx # 只监控nginx相关进程
```


### 示例2：生成系统快照

```bash
glances --export csv --export-csv-file /tmp/system_stats.csv
```


### 示例3：设置告警阈值

```bash
glances --alert cpu:80,mem:90 # CPU超过80%或内存超过90%时告警
```


### 示例4：远程Web监控

## 实例

```bash
glances -w & amp; # 启动Web服务 firefox http: // localhost: 61208 # 在浏览器中查看
```


* * *

## glances 配置文件

glances 的配置文件通常位于 `~/.config/glances/glances.conf`，你可以通过编辑这个文件来永久修改默认设置。

**常见配置项** ：

## 实例

```bash
[ global ] refresh = 2 # 刷新间隔 ( 秒 ) theme = white # 界面主题 ( white/dark ) disable_plugin = fs # 禁用的插件
```


* * *

## glances 与类似工具对比

工具 | 特点 | 适用场景  
---|---|---  
**glances** | 功能全面，界面友好，支持扩展 | 日常系统监控，远程监控  
**top** | Linux 内置，功能基础 | 快速查看进程信息  
**htop** | 增强版 top，交互性好 | 进程管理和监控  
**nmon** | 专业性能监控，支持历史数据 | 性能测试和分析  
**vmstat** | 专注于系统资源统计 | 系统瓶颈分析  
  
* * *

## 最佳实践建议

  1. **长期监控** ：对于需要长期监控的系统，考虑使用 `glances --export` 将数据导出到文件或数据库
  2. **远程管理** ：在服务器上使用 `glances -s` 启动服务端，方便从本地连接查看
  3. **告警设置** ：结合 `--alert` 参数设置合理的阈值，及时发现系统异常
  4. **插件利用** ：根据需求启用/禁用插件，减少不必要的资源消耗
  5. **颜色识别** ：注意界面中的颜色提示（绿色正常，黄色警告，红色危险）



* * *

## 常见问题解答

**Q1：glances 和 top 有什么区别？** A：glances 提供了更全面的系统监控视图（包括网络、磁盘等），而 top 主要关注进程级别的CPU和内存使用情况。

**Q2：如何监控远程服务器？** A：先在远程服务器运行 `glances -s`，然后在本地使用 `glances -c @远程IP` 连接。

**Q3：glances 会占用很多系统资源吗？** A：glances 设计为轻量级工具，通常只占用很少的系统资源（<1% CPU）。

**Q4：如何自定义显示的监控项？** A：可以通过命令行选项禁用不需要的插件，或者编辑配置文件永久修改显示设置。

**Q5：glances 支持Windows系统吗？** A：是的，glances 是跨平台工具，在Windows上也可以通过pip安装使用。

* * *

通过本文的学习，你应该已经掌握了 glances 这一强大系统监控工具的基本使用方法和高级技巧。无论是日常系统维护还是性能问题排查，glances 都能提供全面而直观的系统状态视图。建议在实际工作中多加练习，逐步探索 glances 的更多高级功能。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

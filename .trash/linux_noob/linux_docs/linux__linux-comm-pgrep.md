# Linux pgrep 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

pgrep 是 Linux 系统中一个非常实用的进程查找工具，它是 procps 或 procps-ng 软件包的一部分。这个命令的名称来源于 "process grep"，顾名思义，它能够像 grep 命令搜索文本那样搜索系统中的进程。

pgrep 的主要功能是根据给定的条件查找正在运行的进程，并返回这些进程的 PID（进程 ID）。与传统的 ps 命令结合 grep 的方式相比，pgrep 更加简洁高效。

* * *

## pgrep 基本语法

pgrep 命令的基本语法格式如下：

```bash
pgrep [选项] [匹配模式]
```


其中：

  * `选项`：用于指定搜索条件或输出格式的各种参数
  * `匹配模式`：用于匹配进程名的正则表达式模式



* * *

## 常用选项参数

pgrep 提供了多种选项来精确控制搜索行为，以下是常用的选项：

选项 | 说明  
---|---  
`-l` | 同时显示进程名和 PID  
`-a` | 显示完整命令行而不仅是进程名  
`-f` | 匹配完整命令行（包括参数）而不仅是进程名  
`-u` | 只匹配指定用户拥有的进程  
`-x` | 精确匹配整个进程名  
`-n` | 只显示最新（最近启动）的匹配进程  
`-o` | 只显示最旧（最早启动）的匹配进程  
`-c` | 只返回匹配进程的数量而不显示 PID  
`-d` | 指定输出分隔符（默认为换行符）  
`-P` | 只匹配指定父进程 ID 的子进程  
`-g` | 只匹配指定进程组 ID 的进程  
`-t` | 只匹配指定终端（tty）的进程  
  
* * *

## 使用示例

### 基本进程查找

查找名为 "nginx" 的所有进程：

```bash
pgrep nginx
```


这个命令会返回所有进程名包含 "nginx" 的进程 ID。

### 显示进程名

查找 "ssh" 进程并显示进程名：

```bash
pgrep -l ssh
```


输出示例：

```bash
1234 sshd 5678 ssh-agent
```


### 精确匹配进程名

只匹配完全名为 "bash" 的进程（不包括 "bashrc" 等）：

```bash
pgrep -x bash
```


### 匹配完整命令行

查找包含特定参数的进程，例如查找使用特定端口的 sshd 进程：

```bash
pgrep -f "sshd -p 2222"
```


### 按用户过滤

查找用户 "www-data" 运行的所有进程：

```bash
pgrep -u www-data
```


### 组合条件查找

查找用户 "mysql" 运行的名为 "mysqld" 的进程：

```bash
pgrep -u mysql mysqld
```


### 统计进程数量

统计正在运行的 "chrome" 进程数量：

```bash
pgrep -c chrome
```


### 查找最新/最旧的进程

查找最新启动的 "python" 进程：

```bash
pgrep -n python
```


查找最早启动的 "python" 进程：

```bash
pgrep -o python
```


* * *

## 高级用法

### 结合 pkill 使用

pgrep 经常与 pkill 命令配合使用，可以先使用 pgrep 查看将要终止的进程，确认无误后再使用 pkill：

## 实例

```bash
# 先查看匹配的进程 pgrep -l apache2 # 确认后终止这些进程 pkill apache2
```


### 使用自定义分隔符

默认情况下，pgrep 使用换行符分隔多个 PID。可以改为使用逗号分隔：

```bash
pgrep -d, nginx
```


输出示例：

```bash
1234,5678,9012
```


### 查找特定终端上的进程

查找在 tty1 终端上运行的所有进程：

```bash
pgrep -t tty1
```


### 查找子进程

查找 PID 为 1234 的进程的所有子进程：

```bash
pgrep -P 1234
```


* * *

## 常见问题解答

### pgrep 和 ps | grep 有什么区别？

  1. **效率** ：pgrep 直接查询内核进程信息，比 ps | grep 更高效
  2. **安全性** ：pgrep 不会匹配自身进程，而 ps | grep 可能会匹配到 grep 进程本身
  3. **功能** ：pgrep 提供了更多专门的进程搜索选项



### 为什么 pgrep 有时找不到我知道正在运行的进程？

可能的原因：

  1. 进程名拼写错误
  2. 没有使用 `-f` 选项匹配完整命令行
  3. 进程属于其他用户，而你没有足够的权限查看
  4. 进程已经终止



### 如何查看 pgrep 的版本？

```bash
pgrep -V
```


* * *

## 实际应用场景

### 监控服务状态

在脚本中检查某个服务是否运行：

## 实例

```bash
if pgrep -x "nginx" & gt; / dev / null; then echo "Nginx is running" else echo "Nginx is not running" fi
```


### 批量操作进程

获取所有 Java 进程的 PID 并执行操作：

## 实例

```bash
for pid in $ ( pgrep java ) ; do echo "Processing Java process $pid " # 其他操作... done
```


### 系统资源监控

统计特定类型进程的数量和资源使用：

## 实例

```bash
count =$ ( pgrep -c chrome ) memory =$ ( ps -o rss = -p $ ( pgrep chrome ) | awk '{sum+=$1} END {print sum}' ) echo "Chrome processes: $count , Total memory: ${memory} KB"
```


* * *

## 总结

pgrep 是 Linux 系统管理中一个强大而高效的工具，它简化了进程查找和管理的操作。通过掌握 pgrep 的各种选项和用法，你可以：

  1. 快速准确地定位特定进程
  2. 编写更可靠的系统管理脚本
  3. 提高日常系统维护工作的效率



记住，在使用 pgrep 查找进程后，特别是准备终止进程时，务必先确认找到的是正确的进程，以避免意外终止重要服务。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

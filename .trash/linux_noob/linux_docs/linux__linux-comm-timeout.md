# Linux timeout 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

timeout 是 Linux 系统中的一个实用命令，用于在指定时间后终止正在运行的命令。这个命令特别适用于以下几种场景：

  * 限制长时间运行的进程
  * 防止脚本或程序无限期执行
  * 为关键操作设置执行时间上限
  * 自动化测试中的超时控制



timeout 命令属于 GNU coreutils 包的一部分，在大多数 Linux 发行版中都是预装的。

* * *

## 命令语法

timeout 命令的基本语法格式如下：

```bash
timeout [选项] 持续时间 命令 [参数...]
```


### 参数说明

  1. **持续时间** ：

     * 可以是纯数字（默认单位为秒）
     * 也可以指定单位：`10s`（10秒）、`5m`（5分钟）、`1h`（1小时）
     * 支持小数：`0.5s`（500毫秒）、`1.5m`（1分30秒）
  2. **命令** ：

     * 要执行的命令或程序
     * 可以是内置命令或外部程序
  3. **参数** ：

     * 传递给命令的参数



* * *

## 常用选项

选项 | 说明 | 示例  
---|---|---  
`-s` 或 `--signal` | 指定超时后发送的信号（默认为 TERM） | `timeout -s KILL 5s command`  
`-k` 或 `--kill-after` | 如果初始信号无效，在指定时间后发送 KILL 信号 | `timeout -k 5s 10s command`  
`--preserve-status` | 返回被终止命令的退出状态 | `timeout --preserve-status 5s command`  
`--foreground` | 在前台运行命令（默认在后台） | `timeout --foreground 5s command`  
`-v` 或 `--verbose` | 显示详细输出 | `timeout -v 5s command`  
  
* * *

## 使用示例

### 基础用法

## 实例

```bash
# 5秒后终止 ping 命令 timeout 5s ping example.com # 1分钟后终止脚本执行 timeout 1m . / long_script.sh
```


### 指定信号类型

## 实例

```bash
# 3秒后发送 INT 信号（相当于 Ctrl+C） timeout -s INT 3s command # 10秒后发送 KILL 信号（强制终止） timeout -s KILL 10s command
```


### 组合使用

## 实例

```bash
# 先发送 TERM 信号，5秒后发送 KILL 信号 timeout -k 5s 10s command
```


### 获取退出状态

## 实例

```bash
# 保留被终止命令的退出状态 timeout \--preserve-status 5s command echo $? # 查看退出状态码
```


* * *

## 实际应用场景

### 1\. 防止脚本无限执行

## 实例

```bash
# 限制数据库备份脚本最多运行2小时 timeout 2h . / backup_database.sh
```


### 2\. 自动化测试中的超时控制

## 实例

```bash
# 测试用例最多运行30秒 timeout 30s . / run_test_case.sh
```


### 3\. 网络操作超时

## 实例

```bash
# 下载文件最多尝试1分钟 timeout 1m wget http: // example.com / large_file.zip
```


### 4\. 交互式程序的超时处理

## 实例

```bash
# 给用户最多10秒输入选择 timeout 10s read -p "请输入您的选择: " choice
```


* * *

## 注意事项

  1. **信号处理** ：

     * 某些程序可能会捕获并忽略 TERM 信号，此时需要使用 KILL 信号
     * 重要数据操作时应谨慎使用 KILL 信号，可能导致数据损坏
  2. **子进程处理** ：

     * timeout 默认只终止直接启动的进程，不一定会终止所有子进程
     * 如需终止整个进程树，可以考虑结合 `kill` 命令
  3. **时间精度** ：

     * Linux 内核的时间精度通常为毫秒级
     * 非常短的时间（如 0.001s）可能无法精确控制
  4. **返回值** ：

     * 如果命令在超时前完成，返回命令的退出状态
     * 如果因超时被终止，返回 124
     * 如果 timeout 本身出错，返回 125-128



* * *

## 高级技巧

### 1\. 结合其他命令使用

## 实例

```bash
# 超时后执行清理操作 timeout 30s command || echo "命令已超时，执行清理..."
```


### 2\. 在脚本中使用

## 实例

```bash
#!/bin/bash if timeout 10s command ; then echo "命令成功完成" else echo "命令超时或失败" fi
```


### 3\. 监控资源使用

## 实例

```bash
# 限制CPU时间（需要结合 ulimit） ( ulimit -t 10 ; timeout 20s command )
```


* * *

## 常见问题解答

### Q1: timeout 和 sleep 有什么区别？

A: sleep 是简单地等待指定时间，而 timeout 是限制另一个命令的执行时间。

### Q2: 如何终止 timeout 启动的所有子进程？

A: 可以使用进程组方式：

```bash
timeout --foreground 10s sh -c 'command &amp; wait'
```


### Q3: 为什么我的程序在超时后没有立即终止？

A: 可能是因为程序捕获了默认的 TERM 信号，尝试使用 `-s KILL` 选项。

### Q4: 如何判断命令是因超时而终止的？

A: 检查退出状态码是否为 124：

## 实例

```bash
timeout 5s slow_command if [ $? -eq 124 ] ; then echo "命令因超时被终止" fi
```


* * *

## 总结

timeout 命令是 Linux 系统管理中非常有用的工具，它可以帮助我们：

  1. 控制程序执行时间，防止资源被长时间占用
  2. 提高脚本的健壮性，避免无限等待
  3. 在自动化任务中实现超时机制
  4. 处理不可预测执行时间的操作



通过合理使用 timeout 命令，可以使你的 Linux 系统管理更加高效和可靠。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

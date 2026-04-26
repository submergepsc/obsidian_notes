# Linux systemctl 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

## 什么是 systemctl

systemctl 是 Linux 系统中用于控制 systemd 系统和服务管理器的命令行工具。作为现代 Linux 发行版的核心组件，它取代了传统的 init 系统和 service 命令。

### systemd 简介

systemd 是一个系统和服务管理器，它：

  * 作为 PID 1 运行（第一个启动的进程）
  * 负责启动、停止和管理其他所有进程
  * 提供并行启动能力，显著加快系统启动速度
  * 支持按需启动服务
  * 提供日志收集功能（通过 journald）



* * *

## systemctl 基本语法

```bash
systemctl [选项] [命令] [单元名称]
```


### 常用选项

选项 | 说明  
---|---  
-t, --type | 指定单元类型（service, socket, device 等）  
-a, --all | 显示所有单元，包括不活跃的  
\--state | 按状态过滤单元  
-l, --full | 显示完整的单元信息  
-H, --host | 操作远程主机  
  
* * *

## 服务管理命令

### 启动/停止/重启服务

## 实例

```bash
# 启动服务 sudo systemctl start [ 服务名 ] # 停止服务 sudo systemctl stop [ 服务名 ] # 重启服务 sudo systemctl restart [ 服务名 ] # 重新加载配置（不重启服务） sudo systemctl reload [ 服务名 ]
```


### 查看服务状态

## 实例

```bash
# 查看单个服务状态 systemctl status [ 服务名 ] # 查看所有运行中的服务 systemctl list-units \--type =service \--state =running # 查看失败的服务 systemctl \--failed
```


### 启用/禁用服务

## 实例

```bash
# 启用服务（开机自启） sudo systemctl enable [ 服务名 ] # 禁用服务（取消开机自启） sudo systemctl disable [ 服务名 ] # 查看服务是否启用 systemctl is-enabled [ 服务名 ]
```


* * *

## 单元文件管理

### 单元文件位置

  * 系统单元：`/usr/lib/systemd/system/`
  * 管理员自定义单元：`/etc/systemd/system/`



### 常用单元文件操作

## 实例

```bash
# 重新加载所有单元文件（修改配置后需要执行） sudo systemctl daemon-reload # 显示单元文件内容 systemctl cat [ 单元名 ] # 编辑单元文件（会创建覆盖文件） sudo systemctl edit [ 单元名 ] \--full
```


* * *

## 系统状态管理

### 系统电源管理

## 实例

```bash
# 关机 sudo systemctl poweroff # 重启 sudo systemctl reboot # 挂起 sudo systemctl suspend # 休眠 sudo systemctl hibernate
```


### 系统运行级别

## 实例

```bash
# 获取当前目标（运行级别） systemctl get-default # 设置默认目标 sudo systemctl set-default [ 目标名 ] # 切换目标（立即生效） sudo systemctl isolate [ 目标名 ]
```


常见目标：

  * graphical.target - 图形界面模式
  * multi-user.target - 多用户文本模式
  * rescue.target - 救援模式
  * emergency.target - 紧急模式



* * *

## 实战示例

### 示例1：管理 Nginx 服务

## 实例

```bash
# 启动 Nginx sudo systemctl start nginx # 设置开机自启 sudo systemctl enable nginx # 检查状态 systemctl status nginx # 测试配置后重新加载 sudo nginx -t # 先测试配置 sudo systemctl reload nginx
```


### 示例2：创建自定义服务

  1. 创建服务文件 `/etc/systemd/system/myapp.service`：



## 实例

```bash
[ Unit ] Description = My Custom Application After = network.target [ Service ] ExecStart = /usr/bin/python3 /opt/myapp/app.py WorkingDirectory = /opt/myapp User = myappuser Group = myappgroup Restart = always [ Install ] WantedBy = multi-user.target
```


  2. 启用并启动服务：



## 实例

```bash
sudo systemctl daemon-reload sudo systemctl enable myapp sudo systemctl start myapp
```


* * *

## 常见问题排查

### 服务启动失败

  1. 查看详细日志：

```bash
journalctl -u [服务名] -xe
```

  2. 检查依赖关系：

```bash
systemctl list-dependencies [服务名]
```

  3. 在调试模式下运行：

```bash
systemctl status [服务名] -l --no-pager
```




### 性能分析

## 实例

```bash
# 显示系统启动耗时 systemd-analyze # 显示每个服务的启动时间 systemd-analyze blame # 生成启动流程图（需要图形界面） systemd-analyze plot > boot.svg
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

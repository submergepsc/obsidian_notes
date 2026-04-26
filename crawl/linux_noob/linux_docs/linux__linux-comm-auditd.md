# Linux auditd 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

auditd 是 Linux 系统上的审计守护进程，它是 Linux 审计框架的核心组件。auditd 的主要功能是监控和记录系统活动，包括：

  * 文件和目录访问
  * 系统调用
  * 用户登录/登出
  * 特权命令执行
  * 系统配置变更



这些审计日志对于系统安全监控、合规性检查和故障排查都非常重要。

* * *

## auditd 核心组件

### auditd 守护进程

持续运行的守护进程，负责收集和存储审计事件。

### auditctl 工具

用于配置审计规则和控制审计系统的命令行工具。

### ausearch 工具

用于查询审计日志的命令行工具。

### aureport 工具

生成审计日志的汇总报告。

* * *

## auditd 安装与启动

### 安装 auditd

在大多数 Linux 发行版上，auditd 通常已经预装。如果需要手动安装：

## 实例

```bash
# Ubuntu/Debian sudo apt-get install auditd # CentOS/RHEL sudo yum install audit
```


### 启动和启用 auditd 服务

## 实例

```bash
# 启动服务 sudo systemctl start auditd # 设置开机自启 sudo systemctl enable auditd # 检查服务状态 sudo systemctl status auditd
```


* * *

## auditd 配置文件

auditd 的主要配置文件位于 `/etc/audit/auditd.conf`，包含以下重要参数：

参数 | 说明 | 默认值  
---|---|---  
`log_file` | 审计日志文件路径 | `/var/log/audit/audit.log`  
`max_log_file` | 单个日志文件最大大小(MB) | `8`  
`num_logs` | 保留的日志文件数量 | `5`  
`flush` | 日志写入方式 | `INCREMENTAL`  
`freq` | 如果 flush=INCREMENTAL，多久同步一次 | `20`  
  
修改配置后需要重启服务：

```bash
sudo systemctl restart auditd
```


* * *

## auditctl 命令详解

`auditctl` 是配置审计规则的主要工具。

### 基本语法

```bash
auditctl [选项] [规则]
```


### 常用选项

选项 | 说明  
---|---  
`-l` | 列出当前所有规则  
`-D` | 删除所有规则  
`-s` | 显示审计系统状态  
`-R <file>` | 从文件加载规则  
  
### 规则类型

**文件系统规则** ：监控文件/目录访问

## 实例

```bash
# 监控 /etc/passwd 文件的读写和属性修改 auditctl -w / etc / passwd -p rwxa -k passwd_access
```


  * `-w`：监控路径
  * `-p`：权限(r=读, w=写, x=执行, a=属性变更)
  * `-k`：关键词(用于日志过滤)



**系统调用规则** ：监控特定系统调用

## 实例

```bash
# 监控所有使用 sudo 的命令 auditctl -a always, exit -F arch =b64 -S execve -F path = / usr / bin / sudo -k sudo_cmds
```


  * `-a`：动作和列表(always,exit 表示在退出系统调用时记录)
  * `-F`：过滤条件
  * `-S`：系统调用名称



**用户规则** ：监控特定用户行为

## 实例

```bash
# 监控UID大于500的用户删除文件 auditctl -a always, exit -S unlink -S unlinkat -S rename -S renameat -F auid & gt;= 500 -F auid ! = 4294967295 -k delete_files
```


* * *

## 审计日志分析

### ausearch 命令

用于查询审计日志。

## 实例

```bash
# 查找特定关键词的日志 ausearch -k passwd_access # 查找特定时间的日志 ausearch -ts today ausearch -ts 10 :00:00 -te 11 :00:00 # 查找特定用户的日志 ausearch -ua 1000
```


### aureport 命令

生成审计日志的汇总报告。

## 实例

```bash
# 生成用户登录报告 aureport -l # 生成文件访问报告 aureport -f # 生成所有事件的总结报告 aureport \--summary
```


* * *

## 实际应用示例

### 示例1：监控敏感文件

## 实例

```bash
# 监控 /etc/shadow 文件 auditctl -w / etc / shadow -p wa -k shadow_mod # 查看相关日志 ausearch -k shadow_mod | less
```


### 示例2：监控用户提权

## 实例

```bash
# 监控所有使用 sudo 或 su 的命令 auditctl -a always, exit -F arch =b64 -S execve -F path = / usr / bin / sudo -k priv_esc auditctl -a always, exit -F arch =b64 -S execve -F path = / usr / bin / su -k priv_esc # 生成提权报告 aureport \--start today \--event \--summary -i | grep priv_esc
```


### 示例3：监控 SSH 登录

## 实例

```bash
# 监控 SSH 登录成功和失败 auditctl -a always, exit -F arch =b64 -S execve -F path = / usr / sbin / sshd -k sshd_login # 查看 SSH 登录记录 ausearch -k sshd_login | grep 'acct="user"' | grep 'res=success'
```


* * *

## 最佳实践

**合理设置日志轮转** ：确保日志不会填满磁盘

## 实例

```bash
# 编辑 /etc/audit/auditd.conf max_log_file = 50 num_logs = 10
```


**集中管理审计规则** ：将规则保存在文件中

## 实例

```bash
# 创建规则文件 /etc/audit/rules.d/my.rules -w / etc / passwd -p wa -k passwd_changes -w / etc / group -p wa -k group_changes # 加载规则 auditctl -R / etc / audit / rules.d / my.rules
```


**定期审查日志** ：设置 cron 任务定期分析日志

## 实例

```bash
# 每天生成报告并发送给管理员 0 0 * * * / usr / sbin / aureport \--summary \--start yesterday \--end now | mail -s "Daily Audit Report" admin @ example.com
```


**保护审计日志** ：防止日志被篡改

## 实例

```bash
chmod 600 / var / log / audit / audit.log chown root:root / var / log / audit / audit.log
```


* * *

## 常见问题排查

### 问题1：auditd 服务无法启动

**解决方案** ：

  1. 检查配置文件语法：`auditd -f /etc/audit/auditd.conf`
  2. 查看系统日志：`journalctl -u auditd`



### 问题2：没有生成审计日志

**解决方案** ：

  1. 确认服务正在运行：`systemctl status auditd`
  2. 检查规则是否加载：`auditctl -l`
  3. 验证内核支持：`grep "audit" /boot/config-$(uname -r)`



### 问题3：日志文件过大

**解决方案** ：

  1. 调整日志大小和数量：修改 `/etc/audit/auditd.conf` 中的 `max_log_file` 和 `num_logs`
  2. 设置日志压缩：添加 `compress = yes` 到配置文件中



* * *

## 总结

auditd 是 Linux 系统强大的审计工具，通过合理配置可以：

  * 监控关键文件和目录的访问
  * 跟踪特权命令的使用
  * 记录用户登录和系统活动
  * 满足合规性要求



掌握 auditd 的使用对于系统管理员和安全专业人员至关重要，它可以帮助你更好地理解和保护你的 Linux 系统。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

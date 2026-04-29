# Linux fail2ban 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

* * *

fail2ban 是一个开源的入侵防御工具，用于保护 Linux 服务器免受暴力破解攻击。它通过监控系统日志文件（如 /var/log/auth.log）来检测恶意行为，如多次失败的 SSH 登录尝试，然后自动更新防火墙规则来阻止这些攻击者的 IP 地址。

* * *

## fail2ban 核心功能

### 实时监控日志

fail2ban 持续监控指定的日志文件，寻找预定义模式的恶意行为。

### 自动封禁 IP

当检测到来自同一 IP 的多次失败尝试（可配置阈值），fail2ban 会自动将该 IP 添加到防火墙阻止列表中。

### 可配置的封禁时间

管理员可以设置初始封禁时间和多次违规后的递增封禁时间。

### 多服务支持

不仅支持 SSH，还支持 Apache、Nginx、FTP、邮件服务等多种服务的防护。

### 邮件通知

可配置在封禁 IP 时发送邮件通知给管理员。

* * *

## fail2ban 安装与配置

### 安装方法

在基于 Debian/Ubuntu 的系统上：

## 实例

```bash
sudo apt update sudo apt install fail2ban
```


在基于 RHEL/CentOS 的系统上：

## 实例

```bash
sudo yum install epel-release sudo yum install fail2ban
```


### 基本配置

fail2ban 的主要配置文件位于：

  * `/etc/fail2ban/jail.conf` \- 主配置文件（不建议直接修改）
  * `/etc/fail2ban/jail.local` \- 用户自定义配置（推荐在此修改）



创建自定义配置文件：

```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```


* * *

## fail2ban 常用命令

### 启动/停止/重启服务

## 实例

```bash
sudo systemctl start fail2ban # 启动服务 sudo systemctl stop fail2ban # 停止服务 sudo systemctl restart fail2ban # 重启服务 sudo systemctl enable fail2ban # 设置开机自启
```


### 查看服务状态

```bash
sudo systemctl status fail2ban
```


### 查看被封禁的 IP

```bash
sudo fail2ban-client status sshd
```


### 解封特定 IP

```bash
sudo fail2ban-client set sshd unbanip 192.168.1.100
```


### 手动封禁 IP

```bash
sudo fail2ban-client set sshd banip 192.168.1.100
```


* * *

## fail2ban 配置文件详解

### 主要配置参数

## 实例

```bash
[ DEFAULT ] # 忽略的 IP 地址（白名单） ignoreip = 127.0.0.1/8 ::1 192.168.1.0/24 # 封禁时间（秒） bantime = 600 # 检测时间窗口（秒） findtime = 600 # 最大尝试次数 maxretry = 3 # 使用的防火墙后端 banaction = iptables-multiport [ sshd ] # 是否启用 SSH 保护 enabled = true # 日志文件路径 logpath = % ( sshd_log ) s # 过滤器名称 filter = sshd # 端口号 port = ssh
```


### 自定义过滤器

过滤器定义在 `/etc/fail2ban/filter.d/` 目录中。例如，创建自定义 SSH 过滤器：

  1. 复制默认 SSH 过滤器：

```bash
sudo cp /etc/fail2ban/filter.d/sshd.conf /etc/fail2ban/filter.d/sshd-custom.conf
```

  2. 编辑自定义过滤器，修改正则表达式以匹配特定的失败模式。




* * *

## fail2ban 实战示例

### 保护 SSH 服务

  1. 编辑 jail.local 文件：

```bash
sudo nano /etc/fail2ban/jail.local
```

  2. 添加或修改以下内容：

```bash
[sshd] enabled = true port = ssh filter = sshd logpath = /var/log/auth.log maxretry = 3 bantime = 3600 findtime = 600
```

  3. 重启 fail2ban 服务：

```bash
sudo systemctl restart fail2ban
```




### 保护 Apache 服务

  1. 确保 jail.local 中包含以下内容：

```bash
[apache] enabled = true port = http,https filter = apache-auth logpath = /var/log/apache2/error.log maxretry = 3 bantime = 86400
```

  2. 重启服务使配置生效。




* * *

## fail2ban 高级用法

### 使用 fail2ban 保护自定义服务

  1. 创建自定义过滤器文件：

```bash
sudo nano /etc/fail2ban/filter.d/myapp.conf
```

  2. 添加过滤规则（示例）：

```bash
[Definition] failregex = ^.* .* "POST /login.php.* 401 ignoreregex =
```

  3. 在 jail.local 中添加对应的 jail：

```bash
enabled = true port = http,https filter = myapp logpath = /var/log/myapp/access.log maxretry = 5 bantime = 3600
```




### 设置邮件通知

  1. 编辑 jail.local 文件：

```bash
[DEFAULT] destemail = admin@example.com sender = fail2ban@example.com mta = sendmail action = %(action_mwl)s
```

  2. 确保系统已安装并配置了邮件发送工具（如 sendmail 或 postfix）。




* * *

## fail2ban 日志与故障排除

### 查看 fail2ban 日志

```bash
sudo tail -f /var/log/fail2ban.log
```


### 常见问题解决

#### fail2ban 不工作

  * 检查服务是否运行：`sudo systemctl status fail2ban`
  * 检查日志是否有错误：`sudo journalctl -u fail2ban`



#### IP 未被封禁

  * 确认日志路径正确
  * 检查过滤器正则表达式是否匹配日志条目
  * 增加日志级别调试：在 jail.local 中设置 `loglevel = DEBUG`



#### 误封 IP

  * 将可信 IP 添加到 ignoreip 列表
  * 减少 maxretry 或增加 findtime



* * *

## fail2ban 最佳实践

  1. **定期更新** ：保持 fail2ban 更新以获取最新的安全修复和功能改进。

  2. **合理配置** ：

     * 设置适当的 maxretry 和 bantime
     * 不要将 bantime 设置过长，以免误封合法用户
     * 也不要设置过短，否则防护效果有限
  3. **监控与审查** ：

     * 定期检查被封禁的 IP 列表
     * 分析日志了解攻击模式
  4. **多层防护** ：

     * 结合 fail2ban 与其他安全措施（如防火墙、强密码策略）
     * 考虑修改 SSH 默认端口
  5. **备份配置** ：

     * 备份自定义配置文件和过滤器
     * 记录所有修改以便故障恢复



* * *

## 总结

fail2ban 是 Linux 系统安全的重要工具，通过自动检测和阻止恶意行为，有效防止暴力破解攻击。正确配置和使用 fail2ban 可以显著提高服务器的安全性，同时减少管理员手动干预的工作量。通过本文的介绍，您应该已经掌握了 fail2ban 的基本用法和高级配置技巧，能够根据实际需求定制自己的安全防护策略。

* * *

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

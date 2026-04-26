# Linux su 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux su（英文全拼：switch user）命令用于切换用户身份的命令，除 root 外，需要键入该使用者的密码。

使用权限：所有使用者。

### 语法

```bash
su [选项] [用户名]
```


例如：

```bash
su # 切换到root，保持当前环境 su - # 切换到root，加载root的完整环境 su root # 明确指定切换到root用户
```


切换到其他用户：

```bash
su username su - username su -l username
```


**参数说明** ：

  * `-` 或 `-l` 或 `--login`: 提供类似直接登录的环境
  * `-c command`: 执行指定命令后退出
  * `-s shell`: 指定要使用的shell
  * `-p` 或 `--preserve-environment`: 保留当前环境变量



### 实例

临时以 root 身份执行命令：

```bash
su -c "apt update && apt upgrade" root
```


切换到服务用户进行调试：

```bash
su - www-data su -s /bin/bash www-data # 如果默认shell是/bin/false
```


在脚本中使用：

```bash
su - postgres -c "psql -c 'SELECT version();'"
```


退出 su 会话:

```bash
exit # 退出当前su会话 Ctrl+D # 同样可以退出
```


* * *

## su 与 su - 的区别

**`su`（非登录切换）：**

  * 保持当前用户的环境变量
  * 工作目录不变
  * PATH等环境变量不变



**`su -`（登录切换）：**

  * 加载目标用户的完整环境
  * 切换到目标用户的家目录
  * 重新设置PATH、HOME等环境变量
  * 执行目标用户的登录脚本



### 示例对比

```bash
# 当前用户：john，工作目录：/home/john pwd # /home/john echo $HOME # /home/john su root pwd # /home/john (目录未变) echo $HOME # /home/john (环境未变) exit su - root pwd # /root (切换到root家目录) echo $HOME # /root (完整环境) exit
```


* * *

## su vs sudo 的区别

特性 | su | sudo  
---|---|---  
需要密码 | 目标用户密码 | 当前用户密码  
会话持续 | 直到手动exit | 单次命令或短时间缓存  
配置复杂度 | 简单 | 需要配置sudoers  
安全性 | 需要知道root密码 | 更细粒度的权限控制  
审计 | 有限 | 更详细的日志  
  
su 命令虽然简单直接，但在现代系统管理中，sudo 通常是更推荐的选择，因为它提供了更好的安全性和审计能力。

* * *

## 安全注意事项

  * 避免共享root密码
  * 使用 `su -` 确保完整的环境切换
  * 及时退出su会话
  * 在生产环境中优先考虑使用sudo
  * 监控su的使用日志（通常在/var/log/auth.log）



[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

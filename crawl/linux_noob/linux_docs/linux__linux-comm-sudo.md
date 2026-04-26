# Linux sudo 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

sudo 全称为 Super User DO，允许授权用户以其他用户（通常是 root 用户）的身份执行命令，也就是说，经由 sudo 所执行的指令就好像是 root 亲自执行。

使用权限：在 /etc/sudoers 中有出现的使用者。

### 语法

```bash
sudo [选项] 命令
```


**例如：**

```bash
sudo apt update # 以 root 权限更新软件包列表 sudo vim /etc/hosts # 编辑需要 root 权限的文件
```


**参数说明** ：

  * `-i`: 模拟初始登录，加载目标用户的环境
  * `-s`: 运行shell
  * `-u` user: 以指定用户身份运行
  * `-l`: 列出当前用户可执行的sudo命令
  * `-v`: 验证用户凭据（延长sudo会话）
  * `-k`: 撤销sudo凭据缓存



### 实例

以 root 权限执行单个命令：

```bash
sudo apt update sudo systemctl restart nginx sudo mkdir /opt/myapp
```


切换到 root 用户shell：

```bash
sudo -i # 登录shell，加载root环境变量 sudo -s # 非登录shell sudo su - # 另一种方式
```


以其他用户身份执行命令：

```bash
sudo -u username command ``` ```bash sudo -u postgres psql # 以 postgres 用户运行 psql
```


检查可用权限：

```bash
sudo -l
```


编辑系统文件：

```bash
sudo nano /etc/hosts sudo vim /etc/nginx/nginx.conf
```


###  配置文件

sudo 的配置存储在 /etc/sudoers 文件中，应该使用 visudo 命令编辑：

```bash
sudo visudo
```


常见配置示例：

```bash
# 允许用户免密码执行所有命令 username ALL=(ALL) NOPASSWD: ALL # 允许用户组执行特定命令 %wheel ALL=(ALL) /bin/systemctl, /usr/bin/apt
```


### 常见问题

**用户不在 sudoers 文件：**

```bash
# 需要 root 用户将目标用户加入 sudo 组： usermod -aG sudo username # Ubuntu/Debian usermod -aG wheel username # CentOS/RHEL
```


**缓存时间调整：**

修改 /etc/sudoers 中的 timestamp_timeout（单位：分钟）：

```bash
Defaults timestamp_timeout=30
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

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

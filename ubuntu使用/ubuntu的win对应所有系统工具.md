## Linux 中对应的实现思路
你提供的内容列出了 Windows 的注册表、组策略、服务管理、任务管理器、事件查看器、磁盘管理、设备管理器和 Sysinternals 等工具。
在 Linux 中，这些能力通常**不是集中在一套 GUI 管理工具里**，而是拆分为：
- **文本配置文件**：`/etc/`、`~/.config/`
- **服务与启动管理**：`systemd`、`systemctl`
- **日志系统**：`journald`、`journalctl`、`auditd`
- **内核运行状态接口**：`/proc`、`/sys`
- **设备管理机制**：`udev`
- **资源隔离与统计**：`cgroups`
- **诊断工具**：`ps`、`top`、`ss`、`lsof`、`strace`、`perf`、eBPF 工具
`/proc` 会暴露进程和部分内核状态，`/sys` 会暴露设备、驱动等内核对象，`/sys/fs/cgroup` 会暴露控制组层级；systemd 则作为 PID 1 管理服务和它们对应的 cgroup。([man7.org](https://man7.org/linux/man-pages/man5/proc.5.html?utm_source=chatgpt.com "proc(5) - Linux manual page"))
# 1. 注册表编辑器 `regedit`：Linux 没有统一注册表
## Windows 思路
Windows 把大量系统配置、软件配置、启动项和策略集中存放在注册表中。
## Linux 实现
Linux 通常将不同类别的配置分别保存：

|配置类型|Linux 中的位置或机制|常用命令|
|---|---|---|
|系统服务配置|`/etc/<软件名>/`、`/etc/systemd/system/`|`systemctl edit`、文本编辑器|
|用户配置|`~/.config/`、`~/.local/`|文本编辑器|
|环境变量|`/etc/environment`、`/etc/profile.d/*.sh`、`~/.bashrc`|`printenv`、`export`|
|内核参数|`/proc/sys/`、`/etc/sysctl.d/*.conf`|`sysctl`|
|桌面设置|GNOME 的 dconf / GSettings|`gsettings`|
|设备规则|`/etc/udev/rules.d/*.rules`|`udevadm`|

其中，`sysctl` 只对应**内核运行参数**，不是注册表的完整替代品。Linux 内核文档明确指出，`/proc/sys/kernel` 中的文件可用于监控和调整内核运行参数，但修改错误可能破坏系统运行。([Linux内核文档](https://docs.kernel.org/admin-guide/sysctl/kernel.html?utm_source=chatgpt.com "Documentation for /proc/sys/kernel"))
## 示例：修改内核参数
查看是否允许 IPv4 转发：
```bash
sysctl net.ipv4.ip_forward
```
临时开启：
```bash
sudo sysctl -w net.ipv4.ip_forward=1
```
永久保存：
```bash
echo 'net.ipv4.ip_forward = 1' | sudo tee /etc/sysctl.d/90-ip-forward.conf
sudo sysctl --system
```
对应关系可以理解为：
```text
Windows 注册表中的系统级开关
        ↓
Linux 的 /etc 配置文件 + sysctl + systemd 配置 + udev 规则
```
# 2. 本地组策略 `gpedit.msc`：Linux 由多个策略系统共同实现
Linux 没有一个完全等价于本地组策略编辑器的统一工具。策略通常分散在以下组件中：

| Windows 组策略用途 | Linux 中的实现方式                    |
| ------------- | ------------------------------- |
| 禁止用户执行某些操作    | 文件权限、`sudoers`、Polkit           |
| 限制服务权限        | `systemd` 沙箱参数、SELinux、AppArmor |
| 防火墙策略         | `nftables`、`firewalld`          |
| 登录与认证规则       | PAM、SSSD                        |
| 系统审计          | `auditd`                        |
| 批量配置部署        | Ansible、Puppet、Salt、脚本          |
| 强制安全访问控制      | SELinux 或 AppArmor              |

在 SELinux 环境中，内核会根据加载的安全策略拦截与检查安全相关访问；操作被拒绝时，通常会写入审计日志。Linux Audit 则按照预先配置的规则记录安全相关事件，例如认证、文件变更和策略违规。([红帽文档](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/system_design_guide/using_selinux?utm_source=chatgpt.com "Chapter 19. Using SELinux | System Design Guide"))
## 示例：限制某个服务的权限
Linux 中可以直接在 systemd 服务配置中增加隔离策略：
```bash
sudo systemctl edit myapp.service
```
加入：
```ini
[Service]
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ProtectHome=yes
```
然后应用：
```bash
sudo systemctl daemon-reload
sudo systemctl restart myapp.service
```
这相当于把一部分“组策略式限制”直接绑定到指定服务上。
# 3. 服务管理器 `services.msc`：`systemd` 与 `systemctl`
现代主流 Linux 发行版通常使用 `systemd` 管理服务。systemd 以 PID 1 运行，负责启动系统服务，并将服务进程放入对应的 cgroup 中管理。([systemd.io](https://systemd.io/?utm_source=chatgpt.com "Systemd"))
## 常用命令
|Windows 操作|Linux 命令|
|---|---|
|查看服务列表|`systemctl list-units --type=service`|
|查看运行中的服务|`systemctl list-units --type=service --state=running`|
|查看失败服务|`systemctl --failed`|
|查看服务状态|`systemctl status nginx`|
|启动服务|`sudo systemctl start nginx`|
|停止服务|`sudo systemctl stop nginx`|
|设置开机启动|`sudo systemctl enable nginx`|
|取消开机启动|`sudo systemctl disable nginx`|
|禁止任何方式启动|`sudo systemctl mask nginx`|

## Linux 服务是如何定义的
一个服务通常由 `.service` 单元文件定义：
```ini
# /etc/systemd/system/myapp.service
[Unit]
Description=My Application
After=network-online.target
Wants=network-online.target
[Service]
Type=simple
User=myapp
ExecStart=/opt/myapp/bin/server
Restart=on-failure
EnvironmentFile=-/etc/myapp/myapp.env
[Install]
WantedBy=multi-user.target
```
启用并启动：
```bash
sudo systemctl daemon-reload
sudo systemctl enable --now myapp.service
```
查看日志：
```bash
journalctl -u myapp.service -f
```
## 底层机制
```text
systemctl
   ↓
systemd PID 1
   ↓
读取 .service 单元文件
   ↓
启动进程并放入独立 cgroup
   ↓
记录生命周期、资源占用和日志
```
# 4. 任务管理器 `taskmgr`：`top`、`htop`、`ps` 与 `/proc`
Linux 中每个进程的信息都会出现在：
```bash
/proc/<PID>/
```
例如：
```bash
/proc/1234/status
/proc/1234/cmdline
/proc/1234/fd/
/proc/1234/maps
```
`/proc` 是内核暴露运行状态的伪文件系统，用户态工具会读取它来展示进程、内存和系统状态。([man7.org](https://man7.org/linux/man-pages/man5/proc.5.html?utm_source=chatgpt.com "proc(5) - Linux manual page"))
## 对应工具
|Windows 任务管理器功能|Linux 工具|
|---|---|
|查看 CPU / 内存占用|`top`、`htop`、`btop`|
|查看进程列表|`ps aux`|
|查看进程树|`pstree -p`|
|结束进程|`kill`、`pkill`|
|调整优先级|`nice`、`renice`|
|限制 CPU 核心|`taskset`|
|按服务查看资源|`systemd-cgtop`|

## 常见命令
按 CPU 占用排序：
```bash
ps -eo pid,ppid,user,%cpu,%mem,cmd --sort=-%cpu | head
```
按内存占用排序：
```bash
ps -eo pid,user,%mem,rss,cmd --sort=-%mem | head
```
查看进程打开了哪些文件：
```bash
sudo lsof -p 1234
```
查看进程树：
```bash
pstree -ap
```
结束进程：
```bash
kill 1234
```
强制结束：
```bash
kill -9 1234
```
# 5. 资源监视器 `resmon`：多个专用工具组合
Windows 资源监视器把 CPU、磁盘、内存和网络放在一个界面中。Linux 更常见的做法是使用多个专门工具。

|监控对象|Linux 工具|
|---|---|
|CPU 与进程|`top`、`htop`、`pidstat`|
|内存|`free -h`、`vmstat`、`smem`|
|磁盘吞吐|`iostat`、`iotop`|
|网络连接|`ss`、`lsof -i`|
|网络带宽|`iftop`、`nethogs`|
|系统调用|`strace`|
|性能热点|`perf`、eBPF 工具|

## 定位磁盘高占用
```bash
sudo iotop -o
```
或者：
```bash
iostat -xz 1
```
## 定位高 CPU 进程
```bash
top
```
或者：
```bash
pidstat -u 1
```
## 查看内存状态
```bash
free -h
vmstat 1
```
# 6. 事件查看器 `eventvwr.msc`：`journalctl`、`dmesg` 与 `auditd`
Linux 日志通常分为三类：

|日志类别|工具|典型内容|
|---|---|---|
|服务与系统日志|`journalctl`|服务启动失败、应用错误、系统事件|
|内核日志|`dmesg`、`journalctl -k`|驱动、硬件、内核崩溃|
|安全审计日志|`auditd`、`ausearch`|登录、权限、敏感文件变更|

`journalctl` 用于读取 `systemd-journald` 存储的日志，并可按服务、时间、启动批次等字段过滤。([man7.org](https://man7.org/linux/man-pages/man1/journalctl.1.html?utm_source=chatgpt.com "journalctl(1) - Linux manual page"))
## 常用日志命令
查看本次启动的严重错误：
```bash
journalctl -b -p err..alert
```
查看某个服务日志：
```bash
journalctl -u nginx.service
```
实时追踪服务日志：
```bash
journalctl -u nginx.service -f
```
查看内核日志：
```bash
journalctl -k
```
查看上一次启动的日志：
```bash
journalctl -b -1
```
## 审计敏感文件修改
例如监控 `/etc/passwd` 是否被修改：
```bash
sudo auditctl -w /etc/passwd -p wa -k passwd_changes
```
查询结果：
```bash
sudo ausearch -k passwd_changes
```
Audit 系统可以基于规则监控文件访问、系统调用和安全相关事件。([红帽文档](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/security_guide/sec-defining_audit_rules_and_controls?utm_source=chatgpt.com "7.5. Defining Audit Rules | Security Guide"))
# 7. 磁盘管理 `diskmgmt.msc`：块设备、分区、文件系统与挂载
Linux 把磁盘看作**块设备**，一般位于：
```bash
/dev/sda
/dev/sda1
/dev/nvme0n1
/dev/nvme0n1p1
```
`lsblk` 会从 sysfs 和 udev 数据库中读取块设备信息。([man7.org](https://man7.org/linux/man-pages/man8/lsblk.8.html?utm_source=chatgpt.com "lsblk(8) - Linux manual page"))
## 对应工具
|Windows 磁盘管理功能|Linux 工具|
|---|---|
|查看磁盘和分区|`lsblk`、`blkid`|
|新建/修改分区|`fdisk`、`parted`、`gdisk`|
|创建文件系统|`mkfs.ext4`、`mkfs.xfs`|
|挂载分区|`mount`、`umount`|
|永久挂载|`/etc/fstab`|
|逻辑卷管理|LVM：`pvcreate`、`vgcreate`、`lvcreate`|
|GUI 磁盘工具|GNOME Disks、GParted|

## 查看磁盘布局
```bash
lsblk -o NAME,SIZE,FSTYPE,UUID,MOUNTPOINTS,MODEL
```
查看文件系统 UUID：
```bash
blkid
```
查看磁盘空间：
```bash
df -h
```
查看目录占用：
```bash
du -sh /var/*
```
## 一个典型挂载流程
假设新分区为 `/dev/sdb1`：
```bash
sudo mkfs.ext4 /dev/sdb1
sudo mkdir -p /data
sudo mount /dev/sdb1 /data
```
永久挂载一般写入：
```bash
/etc/fstab
```
例如：
```fstab
UUID=xxxx-xxxx  /data  ext4  defaults  0  2
```
> `fdisk`、`parted`、`mkfs` 都可能破坏数据。对现有磁盘操作前应先用 `lsblk`、`blkid` 和备份确认设备身份。
# 8. 设备管理器 `devmgmt.msc`：`sysfs`、`udev` 与内核模块
Linux 设备管理的基本路径是：
```text
硬件插入或移除
   ↓
Linux 内核检测设备
   ↓
在 /sys 中暴露设备信息
   ↓
触发设备事件
   ↓
udev 创建 /dev 节点、设置权限、建立符号链接
```
`udev` 会接收设备事件，管理设备节点权限，也可以创建额外的 `/dev` 符号链接或重命名网络接口。([man7.org](https://man7.org/linux/man-pages/man7/udev.7.html?utm_source=chatgpt.com "udev(7) - Linux manual page"))
## 常用命令
|目标|命令|
|---|---|
|查看 PCI 设备|`lspci -k`|
|查看 USB 设备|`lsusb -t`|
|查看块设备|`lsblk`|
|查看内核模块|`lsmod`|
|加载驱动模块|`sudo modprobe <module>`|
|卸载模块|`sudo modprobe -r <module>`|
|查看设备属性|`udevadm info`|
|查看驱动加载错误|`dmesg` 或 `journalctl -k`|

## 示例：查看显卡使用的驱动
```bash
lspci -k | grep -A 3 -i 'vga\|display'
```
## 示例：查看 USB 设备事件
```bash
sudo udevadm monitor --environment --udev
```
然后插入 USB 设备，即可看到事件流。
# 9. 系统信息 `msinfo32`：多个系统查询命令组合
Linux 没有强制统一的 `msinfo32` 窗口，通常按项目查询。

|查询内容|Linux 命令|
|---|---|
|操作系统版本|`cat /etc/os-release`|
|内核版本|`uname -a`|
|主机信息|`hostnamectl`|
|CPU|`lscpu`|
|内存|`free -h`、`dmidecode --type memory`|
|BIOS / 主板|`sudo dmidecode`|
|磁盘|`lsblk`|
|PCI 硬件|`lspci -k`|
|USB 硬件|`lsusb`|
|启动日志|`journalctl -b`|
|固件启动模式|`test -d /sys/firmware/efi && echo UEFI|

## 一组系统概览命令
```bash
cat /etc/os-release
uname -a
hostnamectl
lscpu
free -h
lsblk -o NAME,SIZE,FSTYPE,MOUNTPOINTS,MODEL
lspci -k
```
# 10. Process Explorer：`ps`、`pstree`、`lsof`、`strace`
Process Explorer 的能力在 Linux 中通常由多个工具组合实现。

|Process Explorer 功能|Linux 工具|
|---|---|
|查看父子进程树|`pstree -ap`|
|查看 CPU / 内存|`top`、`htop`|
|查看进程命令行|`ps -fp <PID>`、`/proc/<PID>/cmdline`|
|查看加载库|`lsof -p <PID>`、`/proc/<PID>/maps`|
|查看打开句柄|`lsof -p <PID>`、`/proc/<PID>/fd/`|
|跟踪系统调用|`strace`|
|查看线程|`ps -T -p <PID>`|
|性能分析|`perf`|

## 示例：查看某进程打开的文件
```bash
sudo lsof -p 1234
```
## 示例：查看某个程序为何打不开配置文件
```bash
strace -f -e trace=file ./myapp
```
如果程序不断访问不存在的文件，通常会看到：
```text
openat(..., "/some/path/config.ini", ...) = -1 ENOENT
```
这与 Procmon 中查看 `NAME NOT FOUND` 的思路非常接近。
# 11. Autoruns：systemd、cron、自启动目录与 Shell 配置
Windows 的 Autoruns 会枚举几乎所有启动位置。Linux 中也存在多个启动入口。

|启动方式|查看方法|
|---|---|
|系统服务自启动|`systemctl list-unit-files --state=enabled`|
|用户级服务|`systemctl --user list-unit-files --state=enabled`|
|定时器|`systemctl list-timers --all`|
|用户 cron|`crontab -l`|
|系统 cron|`/etc/crontab`、`/etc/cron.*`|
|桌面自启动|`~/.config/autostart/`、`/etc/xdg/autostart/`|
|Shell 登录脚本|`~/.bashrc`、`~/.profile`、`/etc/profile.d/`|
|动态库预加载|`/etc/ld.so.preload`|
|开机加载模块|`/etc/modules-load.d/`|

## 排查自启动项
```bash
systemctl list-unit-files --state=enabled
systemctl --user list-unit-files --state=enabled
systemctl list-timers --all
crontab -l
find ~/.config/autostart /etc/xdg/autostart -type f 2>/dev/null
```
## 查看服务实际启动命令
```bash
systemctl cat suspicious.service
```
# 12. Process Monitor：`strace`、`auditd`、`inotifywait`、`perf` 与 eBPF
Windows Procmon 会实时捕获进程、注册表、文件和网络事件。Linux 中没有完全相同的单一默认工具，通常按需求选择：

|观察内容|Linux 工具|
|---|---|
|程序系统调用|`strace`|
|文件变化事件|`inotifywait`|
|安全审计|`auditd`|
|CPU 性能热点|`perf`|
|内核/用户态动态跟踪|`bpftrace`、BCC、eBPF 工具|
|打开文件与连接|`lsof`|

## 示例：跟踪服务启动失败原因
```bash
sudo strace -ff -o /tmp/myapp.trace /opt/myapp/bin/server
```
然后检索错误：
```bash
grep -E 'ENOENT|EACCES|EPERM' /tmp/myapp.trace*
```
含义通常为：

|错误|含义|
|---|---|
|`ENOENT`|文件或目录不存在|
|`EACCES`|权限不足|
|`EPERM`|操作不允许|

# 13. TCPView：`ss` 与 `lsof`
Linux 中最接近 TCPView 的命令是：
```bash
ss
```
## 常用命令
查看所有监听端口及进程：
```bash
sudo ss -tulpn
```
查看 TCP 连接：
```bash
ss -tanp
```
查看 UDP 套接字：
```bash
ss -uanp
```
查找谁占用了 8080 端口：
```bash
sudo ss -lntp '( sport = :8080 )'
```
或者：
```bash
sudo lsof -nP -iTCP:8080 -sTCP:LISTEN
```
## 典型输出含义
```text
LISTEN 0 4096 0.0.0.0:8080 users:(("java",pid=3210,fd=42))
```
表示：
- 端口：`8080`
- 状态：监听中
- 进程：`java`
- PID：`3210`
- 文件描述符：`42`
# 14. Windows 工具到 Linux 工具的完整映射表
|Windows 工具|Linux 对应工具|Linux 底层机制|
|---|---|---|
|`regedit`|`/etc/*`、`sysctl`、`gsettings`、`udev` 配置|文本配置、`/proc/sys`、桌面配置数据库|
|`gpedit.msc`|SELinux / AppArmor、Polkit、PAM、sudoers、Ansible|内核安全模块与配置管理|
|`services.msc`|`systemctl`|systemd unit 与 cgroups|
|`taskmgr`|`top`、`htop`、`ps`|`/proc/<PID>`、cgroups|
|`resmon`|`iotop`、`iostat`、`vmstat`、`ss`|`/proc`、块设备统计、网络接口|
|`eventvwr.msc`|`journalctl`、`dmesg`、`auditd`|journald、内核 ring buffer、Audit|
|`diskmgmt.msc`|`lsblk`、`fdisk`、`parted`、LVM|块设备、文件系统、挂载机制|
|`devmgmt.msc`|`lspci`、`lsusb`、`udevadm`、`modprobe`|`/sys`、udev、内核模块|
|`msinfo32`|`hostnamectl`、`lscpu`、`dmidecode`、`lsblk`|sysfs、DMI、procfs|
|Process Explorer|`htop`、`pstree`、`lsof`、`strace`|procfs、系统调用跟踪|
|Autoruns|`systemctl`、cron、自启动目录|unit、timer、cron、Shell 脚本|
|Procmon|`strace`、`auditd`、`perf`、eBPF|syscall、audit、tracepoints|
|TCPView|`ss`、`lsof -i`|socket 与网络状态接口|

# 15. Linux 中一套常用排障流程
## 第一步：检查失败服务
```bash
systemctl --failed
```
## 第二步：检查本次启动的错误日志
```bash
journalctl -b -p warning..alert
```
## 第三步：检查 CPU 与内存热点
```bash
top
ps -eo pid,user,%cpu,%mem,cmd --sort=-%cpu | head
```
## 第四步：检查磁盘和 I/O
```bash
lsblk
df -h
sudo iotop -o
```
## 第五步：检查监听端口
```bash
sudo ss -tulpn
```
## 第六步：检查硬件或驱动异常
```bash
journalctl -k -p warning..alert
lspci -k
lsusb -t
```
## 第七步：对单个异常程序做深度跟踪
```bash
strace -f -o /tmp/program.trace ./program
```
## 最核心的区别
Windows 更偏向：
```text
注册表 + 管理控制台 + 统一 GUI 工具
```
Linux 更偏向：
```text
/etc 文本配置
+ systemd 服务体系
+ /proc 与 /sys 内核接口
+ udev 设备管理
+ journal/audit 日志
+ 多个可组合的命令行诊断工具
```
因此，在 Linux 中“实现 Windows 系统工具功能”的关键，不是寻找一个一模一样的程序，而是理解：
1. **配置写在哪里**：`/etc`、`sysctl`、用户配置目录。
2. **服务由谁启动和约束**：`systemd` 与 cgroups。
3. **状态从哪里读取**：`/proc`、`/sys`、日志与审计。
4. **问题如何定位**：`journalctl`、`ss`、`lsof`、`strace`、`perf`。
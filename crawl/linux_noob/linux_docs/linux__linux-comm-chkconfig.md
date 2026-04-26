# Linux chkconfig 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux chkconfig 命令用于检查，设置系统的各种服务。

这是Red Hat公司遵循GPL规则所开发的程序，它可查询操作系统在每一个执行等级中会执行哪些系统服务，其中包括各类常驻服务。

### 语法

```bash
chkconfig [--add][--del][--list][系统服务] 或 chkconfig [--level <等级代号>][系统服务][on/off/reset]
```


**参数** ：

  * \--add 增加所指定的系统服务，让 chkconfig 指令得以管理它，并同时在系统启动的叙述文件内增加相关数据。
  * \--del 删除所指定的系统服务，不再由 chkconfig 指令管理，并同时在系统启动的叙述文件内删除相关数据。
  * \--level<等级代号> 指定读系统服务要在哪一个执行等级中开启或关闭。



### 实例

列出c hkconfig 所知道的所有命令。

```bash
# chkconfig --list
```


开启服务。

```bash
# chkconfig telnet on //开启 Telnet 服务 # chkconfig --list //列出 chkconfig 所知道的所有的服务的情况
```


关闭服务

```bash
# chkconfig telnet off // 关闭 Telnet 服务 # chkconfig --list // 列出 chkconfig 所知道的所有的服务的情况
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

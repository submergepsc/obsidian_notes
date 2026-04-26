# Linux mkkickstart命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux mkkickstart命令用于建立安装的组态文件。

mkkickstart可根据目前系统的设置来建立组态文件，供其他电脑在安装时使用。组态文件的内容包括使用语言，网络环境，系统磁盘状态，以及X Windows的设置等信息。

### 语法

```bash
mkkickstart [--bootp][--dhcp][--nonet][--nox][--version][--nfs <远端电脑:路径>]
```


**参数** ：

  * \--bootp 安装与开机时，使用BOOTP。
  * \--dhcp 安装与开机时，使用DHCP。
  * \--nfs<远端电脑:路径> 使用指定的网络路径安装。
  * \--nonet 不要进行网络设置，即假设在没有网络环境的状态下。
  * \--nox 不要进行X Windows的环境设置。
  * \--version 显示版本信息。



### 实例

构建一个安装组态文件：

```bash
# mkkickstart --nonet -bootp
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

# Linux uname 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux uname（英文全拼：unix name）命令用于显示操作系统信息，例如内核版本、主机名、处理器类型等。。

uname 可显示电脑以及操作系统的相关信息。

### 语法

```bash
uname [-amnrsv][--help][--version]
```


**参数说明** ：

  * -a 或--all 显示全部的信息，包括内核名称、主机名、操作系统版本、处理器类型和硬件架构等。。
  * -m 或--machine 显示处理器类型。
  * -n 或--nodename 显示主机名。
  * -r 或--release 显示内核版本号。
  * -s 或--sysname 显示操作系统名称。
  * -v 显示操作系统的版本。
  * \--help 显示帮助。
  * \--version 显示版本信息。
  * -p 显示处理器类型（与 -m 选项相同）。



### 实例

显示系统信息：

```bash
# uname -a Linux iZbp19byk2t6khuqj437q6Z 4.11.0-14-generic #20~16.04.1-Ubuntu SMP Wed Aug 9 09:06:22 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
```


显示计算机类型：

```bash
# uname -m x86_64
```


显示计算机名：

```bash
# uname -n runoob-linux
```


显示操作系统发行编号：

```bash
# uname -r 4.11.0-14-generic
```


显示操作系统名称：

```bash
# uname -s Linux
```


显示系统版本与时间：

```bash
# uname -v #20~16.04.1-Ubuntu SMP Wed Aug 9 09:06:22 UTC 2017
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

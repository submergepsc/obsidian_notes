# Linux uuname命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux uname 命令用于显示关于当前系统的信息。

uname 是 "UNIX name" 的缩写，它提供了一种快速查看系统信息的方法。

uname 命令可以提供系统的名称、版本、硬件架构等信息，帮助用户快速了解当前操作系统的配置。

### 语法

```bash
uname [选项]
```


uname 命令的输出内容和详细信息会根据不同的选项有所不同。

**参数说明** ：

  * `-a, --all`：显示所有可用的信息，包括内核名称、节点名称、内核版本、机器类型、处理器类型、硬件平台、操作系统。
  * `-s, --kernel-name`：显示内核名称。
  * `-n, --nodename`：显示网络节点名称。
  * `-r, --kernel-release`：显示内核发行版本。
  * `-v, --kernel-version`：显示内核版本。
  * `-m, --machine`：显示计算机的硬件架构。
  * `-p, --processor`：显示处理器类型。
  * `-i, --hardware-platform`：显示硬件平台。
  * `-o, --operating-system`：显示操作系统名称。



### 实例

1、显示所有系统信息：

```bash
uname -a
```


输出示例：

```bash
Linux myhostname 5.8.0-53-generic #60~18.04.1-Ubuntu SMP Tue Apr 13 20:37:32 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```


**解释：**

  * `Linux`：操作系统名称
  * `myhostname`：主机名
  * `5.8.0-53-generic`：内核版本
  * `#60~18.04.1-Ubuntu SMP Tue Apr 13 20:37:32 UTC 2021`：内核编译信息和时间
  * `x86_64`：机器架构
  * `GNU/Linux`：操作系统类型



2、查看内核版本：

```bash
uname -r
```


输出示例：

```bash
5.8.0-53-generic
```


3、查看操作系统名称：

```bash
uname -s
```


输出示例：

```bash
Linux
```


4、查看硬件架构：

```bash
uname -m
```


输出示例：

```bash
x86_64
```

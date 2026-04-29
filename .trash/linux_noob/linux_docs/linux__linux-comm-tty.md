# Linux tty命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux tty命令用于显示终端机连接标准输入设备的文件名称。

在Linux操作系统中，所有外围设备都有其名称与代号，这些名称代号以特殊文件的类型存放于/dev目录下。你可以执行tty(teletypewriter)指令查询目前使用的终端机的文件名称。

### 语法

```bash
tty [-s][--help][--version]
```


**参数说明** ：

  * -s或--silent或--quiet 不显示任何信息，只回传状态代码。
  * \--help 在线帮助。
  * \--version 显示版本信息。



### 实例

显示当前终端

```bash
# tty /dev/pts/4
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

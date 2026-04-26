# Linux lastb命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux **lastb** 命令用于列出登入系统失败的用户相关信息。

单独执行 `lastb` 指令，它会读取位于 **/var/log** 目录下，名称为 **btmp** 的文件，并把该文件记录登入失败的用户名，全部显示出来。

### 语法

```bash
lastb [-adRx][-f <记录文件>][-n <显示行数>][帐号名称...][终端机编号...]
```


**参数说明** ：

options:

  * -R 省略主机名 hostname 的列
  * -a 把从何处登入系统的主机名称或IP地址显示在最后一行。
  * -d 将IP地址转换成主机名称。
  * -f<记录文件> 指定记录文件。
  * -n<显示行数>或-<显示行数> 显示名单的行数。
  * -R 不显示登入系统的主机名称或IP地址。
  * -x 显示系统关机，重新开机，以及执行等级的改变等信息。



username:

  * username： 显示指定用户 username 的登录信息。



tty:

  * tty 设置登录的终端，tty 的名称可以缩写， `last 0` 与 `last tty0` 相同。



### 实例

显示属于登录失败的用户信息：

```bash
# lastb ... zgg ssh:notty 143.198.176.57 Thu Apr 7 11:27 - 11:27 (00:00) zgg ssh:notty 143.198.176.57 Thu Apr 7 11:27 - 11:27 (00:00) zf ssh:notty 143.198.176.57 Thu Apr 7 11:27 - 11:27 (00:00) za ssh:notty 143.198.176.57 Thu Apr 7 11:27 - 11:27 (00:00) zeng ssh:notty 143.198.176.57 Thu Apr 7 11:27 - 11:27 (00:00) zf ssh:notty 143.198.176.57 Thu Apr 7 11:27 - 11:27 (00:00) zette ssh:notty 143.198.176.57 Thu Apr 7 11:27 - 11:27 (00:00) z310 ssh:notty 143.198.176.57 Thu Apr 7 11:27 - 11:27 (00:00) btmp begins Fri Apr 1 07:38:45 2022
```


显示 5 行登录失败的用户信息：

```bash
# lastb -n 5 mos ssh:notty 194.31.98.204 Thu Apr 28 16:52 - 16:52 (00:00) user ssh:notty 194.31.98.204 Thu Apr 28 16:52 - 16:52 (00:00) user ssh:notty 194.31.98.204 Thu Apr 28 16:52 - 16:52 (00:00) user ssh:notty 194.31.98.204 Thu Apr 28 16:52 - 16:52 (00:00) user ssh:notty 194.31.98.204 Thu Apr 28 16:52 - 16:52 (00:00) btmp begins Fri Apr 1 07:38:45 2022
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

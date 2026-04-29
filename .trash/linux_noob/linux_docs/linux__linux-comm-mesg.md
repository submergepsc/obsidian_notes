# Linux mesg命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux mesg命令用于设置终端机的写入权限。

将mesg设置y时，其他用户可利用write指令将信息直接显示在您的屏幕上。

### 语法

```bash
mesg [ny]
```


**参数** ：

  * n 不允许其他用户将信息直接显示在你的屏幕上。
  * y 允许其他用户将信息直接显示在你的屏幕上。



### 实例

允许其他用户发信息到当前终端。 

root 的终端

```bash
# mesg y //在这个终端设置允许发送消息
```


其他普通用户的终端：

```bash
$ write root pts/4 hello hello EOF //Ctrl+D 结束输入
```


root 的终端 终端显示 

```bash
# Message from root@w3cschool.cc (as hnlinux) on pts/5 at 14:48 ... hello EOF
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

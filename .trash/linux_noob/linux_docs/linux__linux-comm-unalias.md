# Linux unalias命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux unalias命令用于删除别名。

unalias为shell内建指令，可删除别名设置。

### 语法

```bash
unalias [-a][别名]
```


**参数** ：

  * -a 删除全部的别名。



### 实例

给命令设置别名

```bash
[root@runoob.com ~]# alias lx=ls [root@runoob.com ~]# lx anaconda-ks.cfg Desktop install.log install.log.syslog qte
```


删除别名

```bash
[root@runoob.com ~]# alias lx //显示别名 alias lx='ls' [root@runoob.com ~]# unalias lx //删除别名 [root@runoob.com ~]# lx -bash: lx: command not found
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

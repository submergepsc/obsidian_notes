# Linux groupmod命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux groupmod命令用于更改群组识别码或名称。

需要更改群组的识别码或名称时，可用groupmod指令来完成这项工作。

### 语法

```bash
groupmod [-g <群组识别码> <-o>][-n <新群组名称>][群组名称]
```


**参数** ：

  * -g <群组识别码> 设置欲使用的群组识别码。
  * -o 重复使用群组识别码。
  * -n <新群组名称> 设置欲使用的群组名称。



### 实例

修改组名 

```bash
[root@runoob.com ~]# groupadd linuxso [root@runoob.com ~]# tail -1 /etc/group linuxso:x:500: [root@runoob.com ~]# tail -1 /etc/group linuxso:x:500: [root@runoob.com ~]# groupmod -n linux linuxso [root@runoob.com ~]# tail -1 /etc/group linux:x:500:
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

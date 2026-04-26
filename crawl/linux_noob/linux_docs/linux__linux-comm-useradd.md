# Linux useradd 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux useradd 命令用于建立用户帐号。

useradd 可用来建立用户帐号。帐号建好之后，再用 passwd 设定帐号的密码。而可用 userdel 删除帐号。使用 useradd 指令所建立的帐号，实际上是保存在 /etc/passwd 文本文件中。

### 语法

```bash
useradd [-mMnr][-c <备注>][-d <登入目录>][-e <有效期限>][-f <缓冲天数>][-g <群组>][-G <群组>][-s <shell>][-u <uid>][用户帐号]
```


或

```bash
useradd -D [-b][-e <有效期限>][-f <缓冲天数>][-g <群组>][-G <群组>][-s <shell>]
```


**参数说明** ：

  * -c<备注> 加上备注文字。备注文字会保存在passwd的备注栏位中。
  * -d<登入目录> 指定用户登入时的起始目录。
  * -D 变更预设值．
  * -e<有效期限> 指定帐号的有效期限。
  * -f<缓冲天数> 指定在密码过期后多少天即关闭该帐号。
  * -g<群组> 指定用户所属的群组。
  * -G<群组> 指定用户所属的附加群组。
  * -m 制定用户的登入目录。
  * -M 不要自动建立用户的登入目录。
  * -n 取消建立以用户名称为名的群组．
  * -r 建立系统帐号。
  * -s<shell> 指定用户登入后所使用的shell。
  * -u<uid> 指定用户ID。



### 实例

添加一般用户

```bash
# useradd tt
```


为添加的用户指定相应的用户组

```bash
# useradd -g root tt
```


创建一个系统用户

```bash
# useradd -r tt
```


为新添加的用户指定home目录

```bash
# useradd -d /home/myd tt
```


建立用户且制定ID

```bash
# useradd caojh -u 544
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

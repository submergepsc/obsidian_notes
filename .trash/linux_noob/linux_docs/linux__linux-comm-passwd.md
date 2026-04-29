# Linux passwd命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux passwd命令用来更改使用者的密码

### 语法

```bash
passwd [-k] [-l] [-u [-f]] [-d] [-S] [username]
```


**必要参数** ：

  * -d 删除密码
  * -f 强迫用户下次登录时必须修改口令
  * -w 口令要到期提前警告的天数
  * -k 更新只能发送在过期之后
  * -l 停止账号使用
  * -S 显示密码信息
  * -u 启用已被停止的账户
  * -x 指定口令最长存活期
  * -g 修改群组密码
  * 指定口令最短存活期
  * -i 口令过期后多少天停用账户



**选择参数** ：

  * \--help 显示帮助信息
  * \--version 显示版本信息



### 实例

修改用户密码 

```bash
# passwd runoob //设置runoob用户的密码 Enter new UNIX password: //输入新密码，输入的密码无回显 Retype new UNIX password: //确认密码 passwd: password updated successfully #
```


显示账号密码信息

```bash
# passwd -S runoob runoob P 05/13/2010 0 99999 7 -1
```


删除用户密码

```bash
# passwd -d lx138 passwd: password expiry information changed.
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

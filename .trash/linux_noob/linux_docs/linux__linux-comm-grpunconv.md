# Linux grpunconv命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux grpunconv命令用于关闭群组的投影密码。

执行grpunconv指令可关闭群组投影密码，它会把密码从gshadow文件内，回存到group文件里。

### 语法

```bash
grpunconv
```


### 实例

未关闭的情况

```bash
cat /etc/gshadow | grep cdy cdy:123456::
```


关闭影子密码

```bash
cat /etc/gshadow cat: /etc/gshadow: 没有那个文件或目录
```


查看密码已经复制到 /etc/group 中了。

```bash
cat /etc/group | grep cdy cdy:123456:1000:
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

# Linux wall命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux wall命令会将讯息传给每一个 mesg 设定为 yes 的上线使用者。当使用终端机介面做为标准传入时, 讯息结束时需加上 EOF (通常用 Ctrl+D)。

使用权限：所有使用者。

### 语法

```bash
wall [ message ]
```


### 实例

传讯息"hi" 给每一个使用者

```bash
wall hi
```


广播消息

```bash
# wall Ilove Broadcast message from root (pts/4) (Thu May 27 16:41:09 2014): Ilove
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

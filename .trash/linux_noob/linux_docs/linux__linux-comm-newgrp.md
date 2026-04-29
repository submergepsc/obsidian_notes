# Linux newgrp命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux newgrp 命令用于登入另一个群组。

newgrp 指令类似 login 指令，当它是以相同的帐号，另一个群组名称，再次登入系统。欲使用 newgrp 指令切换群组，您必须是该群组的用户，否则将无法登入指定的群组。单一用户要同时隶属多个群组，需利用交替用户的设置。若不指定群组名称，则 newgrp 指令会登入该用户名称的预设群组。

### 语法

```bash
newgrp [群组名称]
```


### 实例

改变群组

```bash
# newgrp root
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

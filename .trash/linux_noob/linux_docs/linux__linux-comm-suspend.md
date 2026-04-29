# Linux suspend命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux suspend命令用于暂停执行shell。

suspend为shell内建指令，可暂停目前正在执行的shell。若要恢复，则必须使用SIGCONT信息。

### 语法

```bash
suspend [-f]
```


**参数说明** ：

  * -f 若目前执行的shell为登入的shell，则suspend预设无法暂停此shell。若要强迫暂停登入的shell，则必须使用-f参数。



### 实例

暂停shell

```bash
# suspend -bash: suspend: 无法挂起一个登录 shell # suspend -f
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

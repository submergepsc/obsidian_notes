# Linux id 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux id命令用于显示用户的ID，以及所属群组的ID。

id 会显示用户以及所属群组的实际与有效 ID，若两个 ID 相同，则仅显示实际 ID，若仅指定用户名称，则显示目前用户的 ID。

该命令会显示用户的 UID（User ID）、GID（Group ID）以及附属于用户的所有组 ID。

### 语法

```bash
id [-gGnru][--help][--version][用户名称]
```


**参数说明** ：

  * -g 或 --group 显示用户所属群组的ID。
  * -G 或 --groups 显示用户所属附加群组的ID。
  * -n 或 --name 显示用户，所属群组或附加群组的名称。
  * -r 或 --real 显示实际ID。
  * -u 或 --user 显示用户ID。
  * -help 显示帮助。
  * -version 显示版本信息。



### 实例

显示当前用户信息：

```bash
# id //显示当前用户ID uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel) context=root:system_r:unconfined_t
```


显示用户群组的 ID：

```bash
# id -g 0
```


显示所有群组的 ID：

```bash
# id -G 0 1 2 3 4 5 6 10
```


显示指定用户信息

```bash
# id hnlinux
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

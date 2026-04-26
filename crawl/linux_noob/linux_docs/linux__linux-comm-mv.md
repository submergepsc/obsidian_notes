# Linux mv 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux mv（英文全拼：move file）命令用来为文件或目录改名、或将文件或目录移入其它位置。

### 语法

```bash
mv [options] source dest mv [options] source... directory
```


**参数说明** ：

  * **-b** : 当目标文件或目录存在时，在执行覆盖前，会为其创建一个备份。
  * **-i** : 如果指定移动的源目录或文件与目标的目录或文件同名，则会先询问是否覆盖旧文件，输入 y 表示直接覆盖，输入 n 表示取消该操作。
  * **-f** : 如果指定移动的源目录或文件与目标的目录或文件同名，不会询问，直接覆盖旧文件。
  * **-n** : 不要覆盖任何已存在的文件或目录。
  * **-u** ：当源文件比目标文件新或者目标文件不存在时，才执行移动操作。



mv 参数设置与运行结果

命令格式|  运行结果  
---|---  
```bash mv source_file(文件) dest_file(文件) ``` |  将源文件名 source_file 改为目标文件名 dest_file  
```bash mv source_file(文件) dest_directory(目录) ``` |  将文件 source_file 移动到目标目录 dest_directory 中  
```bash mv source_directory(目录) dest_directory(目录) ``` |  目录名 dest_directory 已存在，将 source_directory 移动到目录名 dest_directory 中；目录名 dest_directory 不存在则 source_directory 改名为目录名 dest_directory  
```bash mv source_directory(目录) dest_file(文件) ``` |  出错  
  
### 实例

将文件 aaa 改名为 bbb :

```bash
mv aaa bbb
```


将 info 目录放入 logs 目录中。注意，如果 logs 目录不存在，则该命令将 info 改名为 logs。

```bash
mv info/ logs
```


再如将 **/usr/runoob** 下的所有文件和目录移到当前目录下，命令行为：

```bash
$ mv /usr/runoob/* .
```


[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

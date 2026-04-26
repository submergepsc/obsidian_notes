# Linux uudecode 命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux uudecode 命令用于将由 [uuencode](https://www.runoob.com/linux/linux-comm-uuencode.html) 命令生成的 ASCII 编码文件还原为原始的二进制文件。

uudecode 通常与 uuencode 配合使用，在接收到一个 uuencoded 文件时，可以使用 uudecode 将其解码回原始的文件格式。

###  语法

```bash
uudecode [input-file]</p>
```


**参数** ：

  * `input-file`：要解码的 ASCII 编码文件。如果未指定文件，`uudecode` 将从标准输入读取数据。



### 实例

假设你有一个通过 uuencode 编码后的文件 encoded.txt，你想将其还原为原始的二进制文件：

```bash
uudecode encoded.txt
```


执行这条命令后，uudecode 会解码 encoded.txt，并生成一个原始文件，其名称与编码时指定的名称相同。

###  自动解码文件名

uudecode 会自动识别编码文件中的文件名，并使用该文件名来创建解码后的文件。例如，如果 encoded.txt 中编码的是 example.bin 文件，那么解码后会自动生成一个名为 example.bin 的文件。

###  从标准输入解码

你还可以使用管道，将 uudecode 与其他命令结合使用，从标准输入解码数据。例如：

```bash
cat encoded.txt | uudecode
```


这种方式适用于需要从标准输入读取编码内容并进行解码的场景。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

# Linux uuencode命令

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

Linux uuencode 命令用于将二进制文件转换为 ASCII 文本格式，以便通过电子邮件或其他传输方式发送。

这种转换使得文件能够通过仅支持文本传输的通道（如电子邮件）进行发送，并在接收端使用 uudecode 命令将其还原为原始的二进制文件。

### 语法

```bash
uuencode [input-file] [output-file]
```


**参数说明：**

  * `input-file`：要转换的二进制文件。
  * `output-file`：转换后的文件名，也可以是邮件中的附件名。



解码文件:

```bash
uudecode <encoded_filename>
```


这里 <encoded_filename> 是编码后的文件名。

### 实例

假设你有一个二进制文件 example.bin，你想将其转换为 ASCII 格式并保存到 encoded.txt 文件中：

```bash
uuencode example.bin example.bin > encoded.txt
```


这条命令会将 example.bin 文件转换为 ASCII 编码，并将输出重定向到 encoded.txt 文件中。

###  解码

你可以使用 uudecode 来解码这个文件：

```bash
uudecode encoded.txt
```


这条命令会读取 encoded.txt 文件，并生成原始的 example.bin 文件。

[![Linux 命令大全](./images/up.gif) Linux 命令大全](linux-command-manual.html)

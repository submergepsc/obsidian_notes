# Cmdlet 文件系统操作

- Source: https://www.runoob.com/powershell/cmdlet-file-system-operations.html

文件系统操作是 PowerShell 中最常见、最实用的任务之一。

从创建、复制、移动、删除文件，到获取文件属性、批量处理目录结构，PowerShell 提供了大量简洁而强大的 Cmdlet 来完成这些操作。


---


## 一、查看目录内容：Get-ChildItem


```
Get-ChildItem
```


这是 PowerShell 中查看目录内容（相当于 `ls` 或 `dir`）的命令。默认列出当前目录下的所有文件和子目录。


你也可以使用路径参数：


```
Get-ChildItem -Path C:\Test
```


查看所有子目录（递归）：


```
Get-ChildItem -Path C:\Test -Recurse
```


按文件类型筛选：


```
Get-ChildItem -Path C:\Test -Filter *.txt
```


---


## 二、创建文件和目录：New-Item


创建新目录：


```
New-Item -Path "C:\Demo" -ItemType Directory
```


创建新文件：


```
New-Item -Path "C:\Demo\example.txt" -ItemType File
```


**

提示：如路径中父目录不存在，将报错。需先手动或脚本创建上级目录。


---


## 三、复制与移动：Copy-Item 和 Move-Item


复制文件：


```
Copy-Item -Path "C:\Demo\example.txt" -Destination "D:\Backup"
```


复制整个文件夹（包含内容）：


```
Copy-Item -Path "C:\Demo" -Destination "D:\Backup" -Recurse
```


移动文件：


```
Move-Item -Path "C:\Demo\example.txt" -Destination "C:\Demo2"
```


---


## 四、删除文件和目录：Remove-Item


删除文件：


```
Remove-Item -Path "C:\Demo\example.txt"
```


删除文件夹及其内容：


```
Remove-Item -Path "C:\Demo" -Recurse -Force
```


说明：


- `-Recurse`：删除目录下的所有内容
- `-Force`：强制删除隐藏或只读文件


---


## 五、读取和写入文件：Get-Content / Set-Content / Add-Content


读取文件内容：


```
Get-Content -Path "C:\Demo\example.txt"
```


写入内容（覆盖）：


```
Set-Content -Path "C:\Demo\example.txt" -Value "Hello PowerShell"
```


追加内容：


```
Add-Content -Path "C:\Demo\example.txt" -Value "Another line"
```


---


## 六、文件重命名与存在性判断


重命名文件：


```
Rename-Item -Path "C:\Demo\example.txt" -NewName "renamed.txt"
```


判断文件是否存在：


```
Test-Path -Path "C:\Demo\renamed.txt"
```


如果存在返回 True，否则返回 False。


---


## 七、获取文件属性：Get-Item


```
$item = Get-Item -Path "C:\Demo\renamed.txt"
$item.Length         # 文件大小（字节）
$item.CreationTime   # 创建时间
$item.Extension      # 扩展名
```


> 注意：返回的是 `System.IO.FileInfo` 类型对象，可进一步使用对象属性。


---


## 八、组合操作示例：批量处理文件


### .log 文件大小总和：">批量列出目录下所有 .log 文件大小总和：


```
Get-ChildItem -Path "C:\Logs" -Filter *.log | Measure-Object -Property Length -Sum
```


输出结果示例：


```
Count    : 15
Sum      : 1289345
Property : Length
```


将所有 .txt 文件内容追加到一个新文件中：


```
Get-ChildItem -Path "C:\TextFiles" -Filter *.txt | ForEach-Object {
    Get-Content $_.FullName | Add-Content -Path "C:\AllText.txt"
}
```


---


## 九、注意事项与常见坑


| 问题 | 说明 |
| --- | --- |
| 路径中包含空格 | 使用引号 " 括起来整个路径字符串 |
| 区分目录和文件 | New-Item 必须指定 -ItemType File 或 Directory |
| 文件不存在时操作报错 | 使用 Test-Path 检查再处理 |
| 删除命令需小心 | Remove-Item 使用 -Recurse 时慎重，避免误删 |


---


## 十、小结与建议


PowerShell 在文件系统操作方面表现非常强大，具备以下优势：


- 命令直观、统一，学习成本低
- 支持对象操作，可与其他命令组合
- 可用于批量任务和自动化脚本


建议学习方式：


- 在临时目录中反复练习各类命令
- 熟练掌握五个核心命令：`New-Item`、`Remove-Item`、`Copy-Item`、`Get-Content`、`Set-Content`
- 尝试将命令封装为脚本，批量处理多个文件









	  AI 思考中...





			** [PowerShell 基本语法](https://www.runoob.com/powershell-basic-syntax.html)
			[Cmdlet 进程和服务管理](https://www.runoob.com/cmdlet-process-and-service-management.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **
# ASP TextStream 对象

- Source: https://www.runoob.com/asp/asp-ref-textstream.html

---


TextStream 对象用于访问文本文件的内容。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[读取文本文件](https://www.runoob.com/try/showasp.php?filename=demo_readtextfile)** 本例演示如何从文本文件中读取内容。


[读取文本文件中的一个部分](https://www.runoob.com/try/showasp.php?filename=demo_readpartoftextfile) 本例演示如何仅仅读取一个文本流文件的部分内容。


[读取文本文件中的一行](https://www.runoob.com/try/showasp.php?filename=demo_readline) 本例演示如何从一个文本流文件中读取一行内容。


[读取文本文件的所有行](https://www.runoob.com/try/showasp.php?filename=demo_readlines) 本例演示如何从文本流文件中读取所有的行。


[略过文本文件中的一部分](https://www.runoob.com/try/showasp.php?filename=demo_skip) 本例演示如何在读取文本流文件时跳过指定的字符数。


[略过文本文件中的一行](https://www.runoob.com/try/showasp.php?filename=demo_skipline) 本例演示如何在读取文本流文件时跳过一行。


[返回行数](https://www.runoob.com/try/showasp.php?filename=demo_line) 本例演示如何返回在文本流文件中的当前行号。


[取得列数](https://www.runoob.com/try/showasp.php?filename=demo_column) 本例演示如何取得在文件中当前字符的列号。


---


## TextStream 对象


TextStream 对象用于访问文本文件的内容。


下面的代码会创建一个文本文件 (c:\test.txt)，然后向此文件写一些文本（变量 f 是 TextStream 对象的一个实例）：


<%

dim fs,f

set fs=Server.CreateObject("Scripting.FileSystemObject")

set f=fs.CreateTextFile("c:\test.txt",true)

f.WriteLine("Hello World!")

f.Close

set f=nothing

set fs=nothing

%>


如需创建 TextStream 对象的一个实例，您可以使用 FileSystemObject 对象的 CreateTextFile 方法或者 OpenTextFile 方法，也可以使用 File 对象的 OpenAsTextStream 方法。


TextStream 对象的属性和方法描述如下：


### 属性


| 属性 | 描述 |
| --- | --- |
| AtEndOfLine | 如果文件指针正好位于 TextStream 文件中行尾标记的前面，则该属性值返回 True；否则返回 False。 |
| AtEndOfStream | 如果文件指针在 TextStream 文件末尾，则该属性值返回 True；否则返回 False。 |
| Column | 返回 TextStream 文件输入流中的当前字符位置的列号。 |
| Line | 返回 TextStream 文件中的当前行号。 |


### 方法


| 方法 | 描述 |
| --- | --- |
| Close | 关闭一个打开的 TextStream 文件。 |
| Read | 从一个 TextStream 文件中读取指定数量的字符并返回结果。 |
| ReadAll | 读取整个 TextStream 文件并返回结果。 |
| ReadLine | 从一个 TextStream 文件读取一整行（到换行符但不包括换行符）并返回结果。 |
| Skip | 当读取一个 TextStream 文件时跳过指定数量的字符。 |
| SkipLine | 当读取一个 TextStream 文件时跳过下一行。 |
| Write | 写入指定的文本到一个 TextStream 文件中。 |
| WriteLine | 写入指定的文本和换行符到一个 TextStream 文件中。 |
| WriteBlankLines | 写入指定数量的换行符到一个 TextStream 文件中。 |










	  AI 思考中...





			** [ASP FileSystem 对象](https://www.runoob.com/asp-ref-filesystem.html)
			[ASP Drive 对象](https://www.runoob.com/asp-ref-drive.html) **













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
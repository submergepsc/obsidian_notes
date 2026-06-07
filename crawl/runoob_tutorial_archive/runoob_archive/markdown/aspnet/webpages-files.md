# ASP.NET Web Pages - 文件

- Source: https://www.runoob.com/aspnet/webpages-files.html

---


本章介绍有关使用文本文件的知识。


---


## 使用文本文件


在前面的章节中，我们已经了解到网页数据是存储在数据库中的。


您也可以把站点数据存储在文本文件中。


用来存储数据的文本文件通常被称为平面文件。常见的文本文件格式是 .txt、.xml 和 .csv（逗号分隔值）。


**在本章中，您将学习到：**


- 如何从文本文件中读取并显示数据


---


## 手动添加一个文本文件


在下面的例子中，您将需要一个文本文件。


在您的网站上，如果没有 App_Data 文件夹，请创建一个。在 App_Data 文件夹中，创建一个名为 Persons.txt 的文件。


添加以下内容到文件中：


## Persons.txt


```csharp
George,Lucas
Steven,Spielberg
Alfred,Hitchcock
```


**
---


## 显示文本文件中的数据


下面的实例演示了如何显示一个文本文件中的数据：


## 实例


```csharp
@{var dataFile = Server.MapPath("~/App_Data/Persons.txt");
	Array userData = File.ReadAllLines(dataFile);}<!DOCTYPE
	html><html><body><h1>Reading Data from a File</h1>@foreach (string dataLine in userData) {  foreach
	(string dataItem in dataLine.Split(','))   {@dataItem <text>&nbsp;</text>}
	<br />}</body></html>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_webpages_cs_019)


## 实例解释


使用 Server.MapPath** 找到确切的文本文件的路径。


使用 **File.ReadAllLines** 打开文本文件，并读取文件中的所有行到一个数组中。


数组中的每个**数据行**中的**数据项**的数据被显示。


---


## 显示 Excel 文件中的数据


使用 Microsoft Excel，您可以将一个电子表格保存为一个逗号分隔的文本文件（.csv 文件）。此时，电子表格中的每一行保存为一个文本行，每个数据列由逗号分隔。


你可以使用上面的实例读取一个 Excel .csv 文件（只需将文件名改成相应的 Excel 文件的名称）。


**







	  AI 思考中...





			** [ASP.NET Web Pages 对象](https://www.runoob.com/webpages-objects.html)
			[ASP.NET Web Pages 帮助器](https://www.runoob.com/webpages-helpers.html) **













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
# ASP File 对象

- Source: https://www.runoob.com/asp/asp-ref-file.html

---


File 对象用于返回关于指定文件的信息。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[文件最后被修改的时间？](https://www.runoob.com/try/showasp.php?filename=demo_datelastmodified)** 本例演示如何使用 DateLastModified 属性来取得指定文件最后被修改的日期和时间。


[文件最后被访问的时间？](https://www.runoob.com/try/showasp.php?filename=demo_datelastaccessed) 此例演示如何使用 DateLastAccessed 属性来取得指定文件最后被访问的日期和时间。


[返回指定文件的属性](https://www.runoob.com/try/showasp.php?filename=demo_attributes) 本例演示如何使用 Attributes 来返回指定文件的属性。


---


## File 对象


File 对象用于返回关于指定文件的信息。


如需操作 File 对象的相关属性和方法，您需要通过 FileSystemObject 对象来创建 File 对象的实例。首先，创建一个 FileSystemObject 对象，然后通过 FileSystemObject 对象的 GetFile 方法，或者通过 Folder 对象的 Files 属性来实例化 File 对象。


下面的代码使用 FileSystemObject 对象的 GetFile 方法来实例化 File 对象，并使用 DateCreated 属性来返回指定文件的创建日期：


## 实例


```
<%
Dim fs,f
Set fs=Server.CreateObject("Scripting.FileSystemObject")
Set f=fs.GetFile("c:\test.txt")
Response.Write("File created: " & f.DateCreated)
set f=nothing
set fs=nothing
%>
```


[演示实例 »](https://www.runoob.com/try/showasp.php?filename=demo_datecreated)


File 对象的属性和方法描述如下：


### 属性


| 属性 | 描述 |
| --- | --- |
| Attributes | 设置或返回指定文件的属性。 |
| DateCreated | 返回指定文件被创建的日期和时间。 |
| DateLastAccessed | 返回指定文件最后被访问的日期和时间。 |
| DateLastModified | 返回指定文件最后被修改的日期和时间。 |
| Drive | 返回指定文件或文件夹所在的驱动器的驱动器字母。 |
| Name | 设置或返回指定文件的名称。 |
| ParentFolder | 返回指定文件的父文件夹对象。 |
| Path | 返回指定文件的路径。 |
| ShortName | 返回指定文件的短名称（8.3 命名约定）。 |
| ShortPath | 返回指定文件的短路径（8.3 命名约定）。 |
| Size | 返回指定文件的尺寸（字节）。 |
| Type | 返回指定文件的类型。 |


### 方法


| 方法 | 描述 |
| --- | --- |
| Copy | 把指定文件从一个位置拷贝到另一个位置。 |
| Delete | 删除指定文件。 |
| Move | 把指定文件从一个位置移动到另一个位置。 |
| OpenAsTextStream | 打开指定文件，并返回一个 TextStream 对象来访问此文件。 |










	  AI 思考中...





			** [ASP Drive 对象](https://www.runoob.com/asp-ref-drive.html)
			[ASP Folder 对象](https://www.runoob.com/asp-ref-folder.html) **













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
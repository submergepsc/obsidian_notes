# ASP Content Linking 组件

- Source: https://www.runoob.com/asp/asp-contentlinking.html

---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[Content Linking 组件](https://www.runoob.com/try/showasp.php?filename=demo_contentlinking)** 本例构建一个内容列表。


[Content Linking 组件 2](https://www.runoob.com/try/showasp.php?filename=demo_contentlinking2) 本例使用 Content Linking 组件在一个文本文件所列的页面间进行导航。


---


## ASP Content Linking 组件


ASP Content Linking 组件用于创建快捷便利的导航系统！


Content Linking 组件会返回一个 Nextlink 对象，这个对象用于容纳需要导航网页的一个列表。


### 语法


<%

Set nl=Server.CreateObject("MSWC.NextLink")

%>


---


## ASP Content Linking 实例


首先，我们会创建一个文本文件 - "links.txt"：


asp_intro.asp	ASP 简介

asp_syntax.asp	ASP 语法

asp_variables.asp	ASP 变量

asp_procedures.asp	ASP 程序


上面的文本文件包含需要导航的页面。页面的排列顺序应该与它们的显示顺序相同，并包含对每个文件名的描述（使用制表符来分隔文件名和描述信息）。


注释：**如果您希望向列表添加页面，或者改变在列表中的页面顺序，那么您需要做的仅仅是修改这个文本文件而已！导航会自动更新！


然后我们创建一个引用文件，"nlcode.inc"。.inc 文件创建一个 NextLink 对象来在 "links.txt" 中列出的页面间进行导航。


"nlcode.inc":


<%**
dim nl

Set nl=Server.CreateObject("MSWC.NextLink")

if (nl.GetListIndex("links.txt")>1) then


  Response.Write("<a href='" & nl.GetPreviousURL("links.txt"))


  Response.Write("'>Previous Page</a>")

end if

Response.Write("<a href='" & nl.GetNextURL("links.txt"))

Response.Write("'>Next Page</a>")

%>


请在文本文件 "links.txt" 列出的每个 .asp 页面中放置一行代码：**。这行代码会在 "links.txt" 中列出每个页面上引用 "nlcode.inc" 中的代码，这样导航就可以工作了。


---


## ASP Content Linking 组件的方法


| 方法 | 描述 | 实例 |
| --- | --- | --- |
| GetListCount | 返回内容链接列表文件中所列项目的数量。 | dim nl,c Set nl=Server.CreateObject("MSWC.NextLink") c=nl.GetListCount("links.txt") Response.Write("There are ") Response.Write(c) Response.Write(" items in the list") %>输出： There are 4 items in the list |
| GetListIndex | 返回在内容链接列表文件中当前条目的索引号。第一个条目的索引号是 1。如果当前页面不在内容链接列表文件中，则返回 0。 | dim nl,c Set nl=Server.CreateObject("MSWC.NextLink") c=nl.GetListIndex("links.txt") Response.Write("Item number ") Response.Write(c) %>输出： Item number 3 |
| GetNextDescription | 返回在内容链接列表文件中所列的下一个条目的文本描述。如果在列表文件中没有找到当前文件，则返回列表中最后一个页面的文本描述。 | dim nl,c Set nl=Server.CreateObject("MSWC.NextLink") c=nl.GetNextDescription("links.txt") Response.Write("Next ") Response.Write("description is: ") Response.Write(c) %>输出：Next description is: ASP Variables |
| GetNextURL | 返回在内容链接列表文件中所列的下一个条目的 URL。如果在列表文件中没有找到当前文件，则返回列表中最后一个页面的 URL。 | dim nl,c Set nl=Server.CreateObject("MSWC.NextLink") c=nl.GetNextURL("links.txt") Response.Write("Next ") Response.Write("URL is: ") Response.Write(c) %>输出：Next URL is: asp_variables.asp |
| GetNthDescription | 返在内容链接列表文件中所列的第 N 个页面的描述信息。 | dim nl,c Set nl=Server.CreateObject("MSWC.NextLink") c=nl.GetNthDescription("links.txt",3) Response.Write("Third ") Response.Write("description is: ") Response.Write(c) %>输出：Third description is: ASP Variables |
| GetNthURL | 返回在内容链接列表文件中所列的第 N 个页面的 URL。 | dim nl,c Set nl=Server.CreateObject("MSWC.NextLink") c=nl.GetNthURL("links.txt",3) Response.Write("Third ") Response.Write("URL is: ") Response.Write(c) %>输出：Third URL is: asp_variables.asp |
| GetPreviousDescription | 返回在内容链接列表文件中所列的前一个条目的文本描述。如果在列表文件中没有找到当前文件，则返回列表中第一个页面的文本描述。 | dim nl,c Set nl=Server.CreateObject("MSWC.NextLink") c=nl.GetPreviousDescription("links.txt") Response.Write("Previous ") Response.Write("description is: ") Response.Write(c) %>输出：Previous description is: ASP Variables |
| GetPreviousURL | 返回在内容链接列表文件中所列的前一个条目的 URL。如果在列表文件中没有找到当前文件，则返回列表中第一个页面的 URL。 | dim nl,c Set nl=Server.CreateObject("MSWC.NextLink") c=nl.GetPreviousURL("links.txt") Response.Write("Previous ") Response.Write("URL is: ") Response.Write(c) %>输出：Previous URL is: asp_variables.asp |

**







	  AI 思考中...





			** [ASP Browser Capabilities](https://www.runoob.com/asp-browser.html)
			[ASP Content Rotator](https://www.runoob.com/asp-contentrotator.html) **













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
# ASP.NET Web Pages - 文件夹

- Source: https://www.runoob.com/aspnet/webpages-folders.html

---


本章介绍有关文件夹和文件夹路径的知识。


---


在本章中，您将学到：


- 逻辑文件夹结构和物理文件夹结构
- 虚拟名称和物理名称
- Web URL 和 Web 路径


---


## 逻辑文件夹结构


下面是典型的 ASP.NET 网站文件夹结构：

![Folders](https://www.runoob.com/wp-content/uploads/2013/07/31.jpg)
- "Account" 文件夹包含登录和安全文件
- "App_Data" 文件夹包含数据库和数据文件
- "Images" 文件夹包含图片
- "Scripts" 文件夹包含浏览器脚本
- "Shared" 文件夹包含公共的文件（比如布局和样式文件）


---


## 物理文件夹结构


在上述网站中的"Images"文件夹在计算机上的物理文件夹结构可能如下：


C:\Documents\MyWebSites\Demo\Images **


---


## 虚拟名称和物理名称


以上面的例子为例：


网站图片的虚拟名称可能是"Images/pic31.jpg"。


对应的物理名称是"C:\Documents\MyWebSites\Demo\Images\pic31.jpg"。


---


## URL 和路径


URL 是用来访问网站中的文件： [http://www.runoob.com/html/html-tutorial.html](https://www.runoob.com/../html/html-tutorial.html)


URL 对应于服务器上的物理文件：C:\MyWebSites\runoob\html\html-tutorial.html


虚拟路径是物理路径的一种简写表示。如果您使用虚拟路径，当您更改域名或者将您的网页移到其他服务器上时，您可以不用更新路径。


| URL | http://www.runoob.com/html/html-tutorial.html |
| --- | --- |
| 服务器名称 | RUNOOB |
| 虚拟路径 | /html/html-tutorial.html |
| 物理路径 | C:\MyWebSites\runoob\html\html-tutorial.html |


磁盘驱动器的根目录如下书写 C: ，但是网站的根目录是 / （斜线）。


Web 文件夹的虚拟路径通常是与物理文件夹不相同。


在您的代码中，根据您的编码需要决定使用物理路径和和虚拟路径。


ASP.NET 文件夹路径有 3 种工具：~ 运算符、Server.MapPath 方法 和 Href 方法。


---


## ~ 运算符


使用 ~ 运算符，在编程代码中规定虚拟路径。


如果您使用 ~ 运算符，在您的站点迁移到其他不同的文件夹或者位置时，您可以不用更改您的任何代码：


var myImagesFolder = "~/images";

var myStyleSheet = "~/styles/StyleSheet.css";


---


## Server.MapPath 方法


Server.MapPath 方法将虚拟路径（/index.html）转换成服务器能理解的物理路径（C:\Documents\MyWebSites\Demo\default.html）。


当您需要打开服务器上的数据文件时，您可以使用这个方法（只有提供完整的物理路径才能访问数据文件）：


	var pathName = "~/dataFile.txt";
var fileName = Server.MapPath(pathName);

在本教程的下一章中，您会学到更多关于读取（和写入）服务器上的数据文件的知识。


---


## Href 方法


Href 方法将代码中的使用的路径转换成浏览器可以理解的路径（浏览器无法理解 ~ 运算符）。


您可以使用 Href 方法创建资源（比如图像文件 和 CSS 文件）的路径。


一般会在 HTML 中的 、 和  元素中使用此方法:


@{var myStyleSheet = "~/Shared/Site.css";}

<!-- This creates a link
to the CSS file. -->
<link rel="stylesheet" type="text/css" href="@Href(myStyleSheet)"
/>

<!-- Same as : -->
<link rel="stylesheet" type="text/css" href="/Shared/Site.css"
/>


Href 方法是 WebPage 对象的一种方法。










	  AI 思考中...





			** [ASP.NET Web Pages 布局](https://www.runoob.com/webpages-layout.html)
			[ASP.NET Web Pages 全局文件](https://www.runoob.com/webpages-global.html) **













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
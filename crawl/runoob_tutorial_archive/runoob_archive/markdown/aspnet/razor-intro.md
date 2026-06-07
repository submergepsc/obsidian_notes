# ASP.NET Razor - 标记

- Source: https://www.runoob.com/aspnet/razor-intro.html

---


Razor 不是一种编程语言。它是服务器端的标记语言。


---


## 什么是 Razor？


Razor 是一种标记语法，可以让您将基于服务器的代码（Visual Basic 和 C#）嵌入到网页中。


基于服务器的代码可以在网页传送给浏览器时，创建动态 Web 内容。当一个网页被请求时，服务器在返回页面给浏览器之前先执行页面中的基于服务器的代码。通过服务器的运行，代码能执行复杂的任务，比如进入数据库。


Razor 是基于 ASP.NET 的，是为创建 Web 应用程序而设计的。它具有传统 ASP.NET 的功能，但更容易使用并且更容易学习。**


---


## Razor 语法


Razor 使用了与 PHP 和经典 ASP 相似的语法。


Razor：


	<ul>
@for (int i = 0; i < 10; i++) {
<li>@i</li>
}
</ul>


PHP：


	<ul>
<?php
for ($i = 0; $i < 10; $i++) {
echo("<li>$i</li>");
}

?>
</ul>


Web Forms（经典 ASP）：


<ul>
<% for (int i = 0; i < 10; i++) { %>
<li><% =i %></li>
<% } %>

</ul>


---


## Razor 帮助器


ASP.NET 帮助器是通过几行简单的 Razor 代码即可访问的组件。


您可以使用 Razor 语法构建自己的帮助器，或者使用内建的 ASP.NET 帮助器。


下面是一些有用的 Razor 帮助器的简短说明：


- Web Grid（Web 网格）
- Web Graphics（Web 图形）
- Google Analytics（Google 分析）
- Facebook Integration（Facebook 集成）
- Twitter Integration（Twitter 集成）
- Sending Email（发送电子邮件）
- Validation（验证）


---


## Razor 编程语言


Razor 支持 C# (C sharp) 和 VB (Visual Basic)。










	  AI 思考中...





			** [ASP.NET WebPages 帮助器参考手册](https://www.runoob.com/webpages-ref-helpers.html)
			[ASP.NET Razor 语法](https://www.runoob.com/razor-syntax.html) **













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
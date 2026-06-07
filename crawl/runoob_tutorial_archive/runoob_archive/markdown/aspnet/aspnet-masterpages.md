# ASP.NET Web Forms - 母版页

- Source: https://www.runoob.com/aspnet/aspnet-masterpages.html

---


母版页为您的网站的其他页面提供模版。


---


## 母版页


母版页允许您为您的 web 应用程序中的所有页面（或页面组）创建一致的外观和行为。


母版页为其他页面提供模版，带有共享的布局和功能。母版页为内容定义了可被内容页覆盖的占位符。输出结果是母版页和内容页的组合。


内容页包含您想要显示的内容。


当用户请求内容页时，ASP.NET 会对页面进行合并以生成结合了母版页布局和内容页内容的输出。


---


## 母版页实例


<%@ Master %>**

<html>

<body>

<h1>Standard Header From Masterpage</h1>
<asp:ContentPlaceHolder id="CPH1" runat="server">

</asp:ContentPlaceHolder>
</body>

</html>


上面的母版页是一个为其他页面设计的普通 HTML 模版页。


@ Master** 指令定义它为一个母版页。


母版页为单独的内容包含占位标签 ****。


**id="CPH1"** 属性标识占位符，在相同母版页中允许多个占位符。


这个母版页被保存为 **"master1.master"**。


![lamp](https://www.runoob.com/images/lamp.gif) 注释：母版页也能够包含代码，允许动态的内容。


---


## 内容页实例


<%@ Page MasterPageFile="master1.master" %>**

<asp:Content
ContentPlaceHolderId="CPH1" runat="server">

<h2>Individual Content</h2>


<p>Paragraph 1</p>


<p>Paragraph 2</p>

</asp:Content>


上面的内容页是站点中独立的内容页中的一个。


@ Page** 指令定义它为一个标准的内容页。


内容页包含内容标签 ****，该标签引用了母版页（ContentPlaceHolderId="CPH1"）。


这个内容页被保存为 **"mypage1.aspx"**。


当用户请求该页面时，ASP.NET 就会将母版页与内容页进行合并。


[点击这里显示 mypage1.aspx](https://www.runoob.com/try/demo_source/mypage1.aspx.htm)


![lamp](https://www.runoob.com/images/lamp.gif)注释：内容文本必须位于  标签内部。标签外的内容文本是不允许的。


---


## 带控件的内容页


<%@ Page MasterPageFile="master1.master" %>**

<asp:Content
ContentPlaceHolderId="CPH1" runat="server">

<h2>RUNOOB</h2>


<form runat="server">


<asp:TextBox id="textbox1" runat="server" />


<asp:Button id="button1" runat="server" text="Button" />


</form>

</asp:Content>


上面的内容页演示了如何把 .NET 控件插入内容页，就像插入一个普通的页面中。


[点击这里显示 mypage2.aspx](https://www.runoob.com/try/demo_source/mypage2.aspx.htm)










	  AI 思考中...





			** [ASP.NET 数据库连接](https://www.runoob.com/aspnet-dbconnection.html)
			[ASP.NET 导航](https://www.runoob.com/aspnet-navigation.html) **













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
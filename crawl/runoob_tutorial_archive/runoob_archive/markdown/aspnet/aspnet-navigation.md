# ASP.NET Web Forms - 导航

- Source: https://www.runoob.com/aspnet/aspnet-navigation.html

---


ASP.NET 带有内建的导航控件。


---


## 网站导航


维护大型网站的菜单是困难而且费时的。


在 ASP.NET 中，菜单可存储在文件中，这样易于维护。文件通常名为 **web.sitemap**，并且被存放在网站的根目录下。


此外，ASP.NET 有三个新的导航控件：


- Dynamic menus
- TreeViews
- Site Map Path


---


## Sitemap 文件


在本教程中，使用下面的 sitemap 文件：


<?xml version="1.0" encoding="ISO-8859-1" ?>**
<siteMap>


  <siteMapNode title="Home" url="/aspnet/w3home.aspx">


  <siteMapNode title="Services" url="/aspnet/w3services.aspx">


    <siteMapNode title="Training" url="/aspnet/w3training.aspx"/>


    <siteMapNode title="Support" url="/aspnet/w3support.aspx"/>


  </siteMapNode>


  </siteMapNode>

</siteMap>


创建 sitemap 文件的规则：


- XML 文件必须包含 围绕内容的  标签
-  标签只能有一个  子节点（ "home" 页面）
- 每个  可以有多个子节点（网页）
- 每个  带有定义页面标题和 URL 的属性


![lamp](https://www.runoob.com/images/lamp.gif)注释：**sitemap 文件必须位于站点根目录下，URL 属性必须相对于该根目录。


---


## 动态菜单


 控件可显示标准的站点导航菜单。


**代码实例：**


<asp:SiteMapDataSource id="nav1" runat="server" />**

<form runat="server">

<asp:Menu runat="server" DataSourceId="nav1" />

</form>


上面实例中的 ** 控件是一个供服务器创建导航菜单的占位符。


控件的数据源由 **DataSourceId** 属性定义。 **id="nav1"** 把数据源连接到 **** 控件。


**** 控件自动连接默认的 sitemap 文件（**web.sitemap**）。


---


## TreeView


 控件可显示多级导航菜单。


这种菜单看上去像一棵带有枝叶的树，可通过 + 或 - 符号来打开或关闭。


**代码实例：**


<asp:SiteMapDataSource id="nav1" runat="server" />**

<form runat="server">

<asp:TreeView runat="server" DataSourceId="nav1" />

</form>


上面实例中的 ** 控件是一个供服务器创建导航菜单的占位符。


控件的数据源由 **DataSourceId** 属性定义。 **id="nav1"** 把数据源连接到 **** 控件。


**** 控件自动连接默认的 sitemap 文件（**web.sitemap**）。


---


## SiteMapPath


SiteMapPath 控件可显示指向当前页面的指针（导航路径）。该路径显示为指向上级页面的可点击链接。


与 TreeView 和 Menu 控件不同，SiteMapPath 控件**不使用** SiteMapDataSource。SiteMapPath 控件默认使用 web.sitemap 文件。


![lamp](https://www.runoob.com/images/lamp.gif)提示：如果 SiteMapPath 没有正确显示，很可能是由于 web.sitemap 文件中存在 URL 错误（打印错误）。


**代码实例：**


<form runat="server">**
<asp:SiteMapPath runat="server" />

</form>


上面实例中的 ** 控件是一个供服务器创建导航菜单的占位符。









	  AI 思考中...





			** [ASP.NET 母版页](https://www.runoob.com/aspnet-masterpages.html)
			[ASP.NET 实例](https://www.runoob.com/aspnet-examples.html) **













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
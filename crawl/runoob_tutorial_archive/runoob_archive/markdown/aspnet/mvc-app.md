# ASP.NET MVC - Internet 应用程序

- Source: https://www.runoob.com/aspnet/mvc-app.html

---


为了学习 ASP.NET MVC，我们将构建一个 Internet 应用程序。


第 1 部分：创建应用程序。


---


## 我们将构建什么


我们将构建一个支持添加、编辑、删除和列出数据库存储信息的 Internet 应用程序。


---


## 我们将做什么


Visual Web Developer 提供了构建 Web 应用程序的不同模板。


我们将使用 **Visual Web Developer** 来创建一个带 **HTML5 标记**的空的 MVC Internet 应用程序。


当这个空白的 Internet 应用程序被创建之后，我们将逐步向该应用添加代码，直到全部完成。我们将使用 **C#** 作为编程语言，并使用最新的 **Razor** 服务器代码标记。


沿着这个思路，我们将讲解这个应用程序的内容、代码和所有组件。


---


## 创建 Web 应用程序


如果您已经安装了 Visual Web Developer ，请启动 Visual Web Developer 并选择 **New Project** 来新建项目。 否则您就只能通过阅读教程来学习了。


![New Project](https://www.runoob.com/wp-content/uploads/2013/07/pic_mvc_new_project.jpg)


在 New Project 对话框中：


- 打开**Visual C#**模板
- 选择模板 **ASP.NET MVC 3 Web Application**
- 设置项目名称为 **MvcDemo**
- 设置磁盘位置，比如 **c:\runoob_demo**
- 点击 **OK**


当 New Project 对话框打开时：


- 选择 **Internet Application** 模板
- 选择 **Razor Engine**（Razor 引擎）
- 选择 **HTML5 Markup**（HTML5 标记）
- 点击 **OK**


Visual Studio Express 将创建一个如下所示的类似项目：


![Mvc Explorer](https://www.runoob.com/wp-content/uploads/2013/07/pic_mvc_explorer.jpg)


我们将在本教程的下一章中探究有关文件和文件夹的内容。

**







	  AI 思考中...





			** [ASP.NET MVC 简介](https://www.runoob.com/mvc-intro.html)
			[ASP.NET MVC 文件夹](https://www.runoob.com/mvc-folders.html) **













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
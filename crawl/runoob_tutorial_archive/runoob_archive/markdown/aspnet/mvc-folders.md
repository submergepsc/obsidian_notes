# ASP.NET MVC - 应用程序文件夹

- Source: https://www.runoob.com/aspnet/mvc-folders.html

---


为了学习 ASP.NET MVC，我们将构建一个 Internet 应用程序。


第 2 部分：探究应用程序文件夹。


---


## MVC 文件夹


一个典型的 ASP.NET MVC Web 应用程序的文件夹内容如下所示：


|  |  | 应用程序信息 PropertiesReferences 应用程序文件夹 App_Data 文件夹Content 文件夹 Controllers 文件夹 Models 文件夹 Scripts 文件夹 Views 文件夹配置文件 Global.asaxpackages.configWeb.config |
| --- | --- | --- |


所有的 MVC 应用程序的文件夹名称都是相同的。MVC 框架是基于默认的命名。控制器写在 Controllers 文件夹中，视图写在 Views 文件夹中，模型写在 Models 文件夹中。您不必在应用程序代码中使用文件夹名称。


标准化的命名减少了代码量，同时有利于开发人员对 MVC 项目的理解。


下面是对每个文件夹内容的简短概述：


---


## App_Data 文件夹


**App_Data** 文件夹用于存储应用程序数据。


我们将在本教程后面的章节中介绍添加 SQL 数据库到 App_Data 文件夹。


---


## Content 文件夹


**Content** 文件夹用于存放静态文件，比如样式表（CSS 文件）、图标和图像。


Visual Web Developer 会自动添加一个 **themes** 文件夹到 Content 文件夹中。themes 文件夹存放 jQuery 样式和图片。在项目中，您可以删除这个 themes 文件夹。


Visual Web Developer 同时也会添加一个标准的样式表文件到项目中：即 content 文件夹中的 **Site.css** 文件。这个样式表文件是您想要改变应用程序样式时需要编辑的文件。


![Content](https://www.runoob.com/wp-content/uploads/2013/07/pic_mvc_content.jpg)


我们将在本教程的下一章中编辑这个样式表文件（Site.css）。


---


## Controllers 文件夹


Controllers 文件夹包含负责处理用户输入和响应的控制器类。


MVC 要求所有控制器文件的名称以 "Controller" 结尾。


Visual Web Developer 已经创建好一个 Home 控制器（用于 Home 页面和 About 页面）和一个 Account 控制器（用于 Login 页面）：


![Controllers](https://www.runoob.com/wp-content/uploads/2013/07/pic_mvc_controllers.jpg)


我们将在本教程后面的章节中创建更多的控制器。


---


## Models 文件夹


Models 文件夹包含表示应用程序模型的类。模型控制并操作应用程序的数据。


我们将在本教程后面的章节中创建模型（类）。


---


## Views 文件夹


Views 文件夹用于存储与应用程序的显示相关的 HTML 文件（用户界面）。


Views 文件夹中包含每个控制器对应的一个文件夹。


在 Views 文件夹中，Visual Web Developer 已经创建了一个 Account 文件夹、一个 Home 文件夹、一个 Shared 文件夹。


Account 文件夹包含用于用户账号注册和登录的页面。


Home 文件夹用于存储诸如 home 页和 about 页之类的应用程序页面。


Shared 文件夹用于存储控制器间分享的视图（母版页和布局页）。


![Views](https://www.runoob.com/wp-content/uploads/2013/07/pic_mvc_views.jpg)


我们将在本教程的下一章中编辑这些布局文件。


---


## Scripts 文件夹


Scripts 文件夹存储应用程序的 JavaScript 文件。


默认情况下，Visual Web Developer 在这个文件夹中存放标准的 MVC、Ajax 和 jQuery 文件：


![Scripts](https://www.runoob.com/wp-content/uploads/2013/07/pic_mvc_scripts.jpg)


**注释：**名为 "modernizr" 的文件时用于在应用程序中支持 HTML5 和 CSS3 的 JavaScript 文件。


**







	  AI 思考中...





			** [ASP.NET MVC Web 应用程序](https://www.runoob.com/mvc-app.html)
			[ASP.NET MVC 页面和布局](https://www.runoob.com/mvc-layout.html) **













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
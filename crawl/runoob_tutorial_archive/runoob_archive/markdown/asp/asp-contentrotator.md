# ASP Content Rotator 组件 (ASP 3.0)

- Source: https://www.runoob.com/asp/asp-contentrotator.html

---


## ASP Content Rotator 组件


ASP Content Rotator 组件创建一个 ContentRotator 对象，每当访客进入网站或刷新页面时，该对象就会显示一段不同的内容字符串。


有关内容字符串的信息是包含在一个名为内容目录文件（Content Schedule File）的文本文件中。


内容字符串可包含 HTML 标签，这样您就可以显示 HTML 可呈现的任何类型的内容：文本、图像、颜色或者超链接。


### 语法


<%**
Set cr=Server.CreateObject("MSWC.ContentRotator")

%>


---


## ASP Content Rotator 实例


每当访客浏览网页时，下面的实例就会显示不同的内容。


首先，创建一个名为 "textads.txt" 的文本文件，并把它放置在名为 "text" 的子文件夹中。


"textads.txt":


%% #3

<h2>This is a great day!!</h2>


%% #3

<img src="smiley.gif">


%% #4

<a href="http://www.runoob.com">Visit RUNOOB</a>


请注意在每个内容字符串起始位置的 # 号码。这个号码是一个可选的参数，用来指示 HTML 内容字符串的相对权重。在上面的文本文件中，Content Rotator 有十分之三的几率显示第一个内容字符串，有十分之三的几率显示第二个内容字符串，有十分之四的几率显示第三个字符串。


然后，创建一个 ASP 文件，并插入下面的代码：


## 实例


```
<html>
<body>
<%
set cr=server.createobject("MSWC.ContentRotator")
response.write(cr.ChooseContent("text/textads.txt"))
%>
</body>
</html>
```


[演示实例 »](https://www.runoob.com/try/showasp.php?filename=demo_contentrotator)


---


## ASP Content Rotator 组件的方法


| 方法 | 描述 | 实例 |
| --- | --- | --- |
| ChooseContent | 获取并显示某个内容字符串。 | dim cr Set cr=Server.CreateObject("MSWC.ContentRotator") response.write(cr.ChooseContent("text/textads.txt")) %>输出： |
| GetAllContent | 取回并显示文本文件中所有的内容字符串。 | dim cr Set cr=Server.CreateObject("MSWC.ContentRotator") response.write(cr.GetAllContent("text/textads.txt")) %> 输出： ## This is a great day!! Visit RUNOOB |










	  AI 思考中...





			** [ASP Content Linking](https://www.runoob.com/asp-contentlinking.html)
			[AJAX 简介](https://www.runoob.com/asp-ajax-intro.html) **













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
# JSP 点击量统计

- Source: https://www.runoob.com/jsp/jsp-hits-counter.html

有时候我们需要知道某个页面被访问的次数，这时我们就需要在页面上添加页面统计器，页面访问的统计一般在用户第一次载入时累加该页面的访问数上。


要实现一个计数器，您可以利用应用程序隐式对象和相关方法getAttribute()和setAttribute()来实现。


这个对象表示JSP页面的整个生命周期中。当JSP页面初始化时创建此对象，当JSP页面调用jspDestroy()时删除该对象。


以下是在应用中创建变量的语法：


```
application.setAttribute(String Key, Object Value);
```


您可以使用上述方法来设置一个计数器变量及更新该变量的值。读取该变量的方法如下：


```
application.getAttribute(String Key);
```


在页面每次被访问时，你可以读取计数器的当前值，并递增1，然后重新设置，在下一个用户访问时就将新的值显示在页面上。


---


## 实例演示


该实例将介绍如何使用JSP来计算特定页面访问的总人数。如果你要计算你网站使用页面的总点击量，那么你就必须将该代码放在所有的JSP页面上。


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.io.*,java.util.*" %>
<html>
<html>
<head>
<title>访问量统计</title>
</head>
<body>
<%
    Integer hitsCount =
      (Integer)application.getAttribute("hitCounter");
    if( hitsCount ==null || hitsCount == 0 ){
       /* 第一次访问 */
       out.println("欢迎访问菜鸟教程!");
       hitsCount = 1;
    }else{
       /* 返回访问值 */
       out.println("欢迎再次访问菜鸟教程!");
       hitsCount += 1;
    }
    application.setAttribute("hitCounter", hitsCount);
%>

<p>页面访问量为: <%= hitsCount%></p>


</body>
</html>
```


现在我们将上面的代码放置于main.jsp文件上，并访问*http://localhost:8080/testjsp/main.jsp*文件。你会看到页面会生成个计数器，在我们每次刷新页面时，计数器都会发生变化（每次刷新增加1）。

你也可以通过不同的浏览器访问，计数器会在每次访问后增加1。如下所示：

![](https://www.runoob.com/wp-content/uploads/2014/01/jsp7.gif)


---


## 复位计数器


使用以上方法，在 web 服务器重启后，计数器会被复位为 0，即前面保留的数据都会消失，你可以使用以下几种方式解决该问题:


- 在数据库中定义一个用于统计网页访问量的数据表 count，字段为 hitcount，hitcount 默认值为0，将统计数据写入到数据表中。
- 在每次访问时我们读取表中 hitcount 字段。
- 每次访问时让 hitcount 自增 1。
- 在页面上显示新的 hitcount 值作为页面的访问量。
- 如果你需要统计每个页面的访问量，你可以使用以上逻辑将代码添加到所有页面上。









	  AI 思考中...





			** [JSP 页面重定向](https://www.runoob.com/jsp-page-redirect.html)
			[JSP 自动刷新](https://www.runoob.com/jsp-auto-refresh.html) **













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
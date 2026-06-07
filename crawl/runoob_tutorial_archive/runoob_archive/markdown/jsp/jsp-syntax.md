# JSP 语法

- Source: https://www.runoob.com/jsp/jsp-syntax.html

本小节将会简单地介绍一下JSP开发中的基础语法。


---


## 脚本程序


脚本程序可以包含任意量的Java语句、变量、方法或表达式，只要它们在脚本语言中是有效的。


脚本程序的语法格式：


```
<% 代码片段 %>
```


或者，您也可以编写与其等价的XML语句，就像下面这样：


```
<jsp:scriptlet>
   代码片段
</jsp:scriptlet>
```


任何文本、HTML标签、JSP元素必须写在脚本程序的外面。


下面给出一个示例，同时也是本教程的第一个JSP示例：


```
<html>
<head><title>Hello World</title></head>
<body>
Hello World!<br/>
<%
out.println("Your IP address is " + request.getRemoteAddr());
%>
</body>
</html>
```


**注意：**请确保Apache Tomcat已经安装在C:\apache-tomcat-7.0.2目录下并且运行环境已经正确设置。


将以上代码保存在hello.jsp中，然后将它放置在 C:\apache-tomcat-7.0.2\webapps\ROOT目录下，打开浏览器并在地址栏中输入http://localhost:8080/hello.jsp。运行后得到以下结果：


![](https://www.runoob.com/wp-content/uploads/2014/01/jsp_hello_world.jpg)


### 中文编码问题


如果我们要在页面正常显示中文，我们需要在 JSP 文件头部添加以下代码：
```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
```
 接下来我们将以上程序修改为：


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
Hello World!<br/>
<%
out.println("你的 IP 地址 " + request.getRemoteAddr());
%>
</body>
</html>
```


这样中文就可以正常显示了。


---


## JSP声明


一个声明语句可以声明一个或多个变量、方法，供后面的Java代码使用。在JSP文件中，您必须先声明这些变量和方法然后才能使用它们。


JSP声明的语法格式：


```
<%! declaration; [ declaration; ]+ ... %>
```


或者，您也可以编写与其等价的XML语句，就像下面这样：


```
<jsp:declaration>
   代码片段
</jsp:declaration>
```


程序示例：


```
<%! int i = 0; %>
<%! int a, b, c; %>
<%! Circle a = new Circle(2.0); %>
```


---


## JSP表达式

一个JSP表达式中包含的脚本语言表达式，先被转化成String，然后插入到表达式出现的地方。

由于表达式的值会被转化成String，所以您可以在一个文本行中使用表达式而不用去管它是否是HTML标签。

表达式元素中可以包含任何符合Java语言规范的表达式，但是不能使用分号来结束表达式。

JSP表达式的语法格式：


```
<%= 表达式 %>
```


同样，您也可以编写与之等价的XML语句：


```
<jsp:expression>
   表达式
</jsp:expression>
```


程序示例：


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<p>
   今天的日期是: <%= (new java.util.Date()).toLocaleString()%>
</p>
</body>
</html>
```


运行后得到以下结果：


```
今天的日期是: 2016-6-25 13:40:07
```


---


## JSP注释


JSP注释主要有两个作用：为代码作注释以及将某段代码注释掉。


JSP注释的语法格式：


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<%-- 该部分注释在网页中不会被显示--%>
<p>
   今天的日期是: <%= (new java.util.Date()).toLocaleString()%>
</p>
</body>
</html>
```


运行后得到以下结果：


```
今天的日期是: 2016-6-25 13:41:26
```


不同情况下使用注释的语法规则：


| 语法 | 描述 |
| --- | --- |
|  | JSP注释，注释内容不会被发送至浏览器甚至不会被编译 |
|  | HTML注释，通过浏览器查看网页源代码时可以看见注释内容 |
|  | 代表静态 %> 常量 |
| \' | 在属性中使用的单引号 |
| \" | 在属性中使用的双引号 |


---


## JSP指令


JSP指令用来设置与整个JSP页面相关的属性。


JSP指令语法格式：


```
<%@ directive attribute="value" %>
```


这里有三种指令标签：


| 指令 | 描述 |
| --- | --- |
|  | 定义页面的依赖属性，比如脚本语言、error页面、缓存需求等等 |
|  | 包含其他文件 |
|  | 引入标签库的定义，可以是自定义标签 |


---


## JSP行为


JSP行为标签使用XML语法结构来控制servlet引擎。它能够动态插入一个文件，重用JavaBean组件，引导用户去另一个页面，为Java插件产生相关的HTML等等。


行为标签只有一种语法格式，它严格遵守XML标准：


```
<jsp:action_name attribute="value" />
```


行为标签基本上是一些预先就定义好的函数，下表罗列出了一些可用的JSP行为标签：：


| 语法 | 描述 |
| --- | --- |
| jsp:include | 用于在当前页面中包含静态或动态资源 |
| jsp:useBean | 寻找和初始化一个JavaBean组件 |
| jsp:setProperty | 设置 JavaBean组件的值 |
| jsp:getProperty | 将 JavaBean组件的值插入到 output中 |
| jsp:forward | 从一个JSP文件向另一个文件传递一个包含用户请求的request对象 |
| jsp:plugin | 用于在生成的HTML页面中包含Applet和JavaBean对象 |
| jsp:element | 动态创建一个XML元素 |
| jsp:attribute | 定义动态创建的XML元素的属性 |
| jsp:body | 定义动态创建的XML元素的主体 |
| jsp:text | 用于封装模板数据 |


---


## JSP 隐含对象

JSP 支持九个自动定义的变量，江湖人称隐含对象，它们是在 JSP 页面中自动可用的对象，无需额外的声明或初始化。

这九个隐含对象的简介见下表：


| 对象 | 描述 |
| --- | --- |
| request | HttpServletRequest类的实例，代表 HTTP 请求的对象，包含客户端发送到服务器的信息，如表单数据、URL参数等。 |
| response | HttpServletResponse类的实例，代表 HTTP 响应的对象，用于向客户端发送数据和响应。 |
| out | JspWriter类的实例，用于向客户端输出文本内容的对象，通常用于生成HTML。 |
| session | HttpSession类的实例，代表用户会话的对象，可用于存储和检索用户特定的数据，跨多个页面。 |
| application | ServletContext类的实例，代表 Web 应用程序的上下文，可以用于存储和检索全局应用程序数据。 |
| config | ServletConfig类的实例，包含有关当前 JSP 页面的配置信息，例如初始化参数。 |
| pageContext | PageContext类的实例，提供对JSP页面所有对象以及命名空间的访问 |
| page | 类似于 Java 类中的 this 关键字，代表当前 JSP 页面的实例，可以用于调用页面的方法。 |
| exception | exception 类的对象，代表发生错误的 JSP 页面中对应的异常对象，用于处理 JSP 页面中的异常情况，可用于捕获和处理页面中发生的异常。 |


---


## 控制流语句

JSP提供对Java语言的全面支持。您可以在JSP程序中使用Java API甚至建立Java代码块，包括判断语句和循环语句等等。


## 判断语句

**if…else** 块，请看下面这个例子：


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%! int day = 3; %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h3>IF...ELSE 实例</h3>
<% if (day == 1 || day == 7) { %>
      <p>今天是周末</p>
<% } else { %>
      <p>今天不是周末</p>
<% } %>
</body>
</html>
```


运行后得到以下结果：


```
IF...ELSE 实例
今天不是周末
```


现在来看看switch…case块，与if…else块有很大的不同，它使用out.println()，并且整个都装在脚本程序的标签中，就像下面这样：


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%! int day = 3; %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h3>SWITCH...CASE 实例</h3>
<%
switch(day) {
case 0:
   out.println("星期天");
   break;
case 1:
   out.println("星期一");
   break;
case 2:
   out.println("星期二");
   break;
case 3:
   out.println("星期三");
   break;
case 4:
   out.println("星期四");
   break;
case 5:
   out.println("星期五");
   break;
default:
   out.println("星期六");
}
%>
</body>
</html>
```


浏览器访问，运行后得出以下结果：


```
SWITCH...CASE 实例

星期三
```



---

## 循环语句


在JSP程序中可以使用Java的三个基本循环类型：for，while，和 do…while。

让我们来看看for循环的例子，以下输出的不同字体大小的"菜鸟教程"：


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%! int fontSize; %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h3>For 循环实例</h3>
<%for ( fontSize = 1; fontSize <= 3; fontSize++){ %>
   <font color="green" size="<%= fontSize %>">
    菜鸟教程
   </font><br />
<%}%>
</body>
</html>
```


运行后得到以下结果：


![](https://www.runoob.com/wp-content/uploads/2014/01/7B4B85CF-FE4B-43CB-AAFF-F8594AD4342C.jpg)


将上例改用 while 循环来写：


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%! int fontSize=0; %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h3>While 循环实例</h3>
<%while ( fontSize <= 3){ %>
   <font color="green" size="<%= fontSize %>">
    菜鸟教程
   </font><br />
<%fontSize++;%>
<%}%>
</body>
</html>
```


浏览器访问，输出结果为（fontSize 初始化为0，所以多输出了一行）：**

![](https://www.runoob.com/wp-content/uploads/2014/01/4F744CC9-E484-45BA-AF18-27AFCF4AD45C.jpg)

	JSP运算符
JSP支持所有Java逻辑和算术运算符。

下表罗列出了JSP常见运算符，优先级从高到底：


| 类别 | 操作符 | 结合性 |
| --- | --- | --- |
| 后缀 | () [] . (点运算符) | 左到右 |
| 一元 | ++ - - ! ~ | 右到左 |
| 可乘性 | * / % | 左到右 |
| 可加性 | + - | 左到右 |
| 移位 | >> >>>  >= >=







	  AI 思考中...





			** [JSP 生命周期](https://www.runoob.com/jsp-life-cycle.html)
			[JSP 指令](https://www.runoob.com/jsp-directives.html) **













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
# JSP 客户端请求

- Source: https://www.runoob.com/jsp/jsp-client-request.html

当浏览器请求一个网页时，它会向网络服务器发送一系列不能被直接读取的信息，因为这些信息是作为HTTP信息头的一部分来传送的。您可以查阅HTTP协议来获得更多的信息。


下表列出了浏览器端信息头的一些重要内容，在以后的网络编程中将会经常见到这些信息：


| 信息 | 描述 |
| --- | --- |
| Accept | 指定浏览器或其他客户端可以处理的MIME类型。它的值通常为 image/png 或 image/jpeg |
| Accept-Charset | 指定浏览器要使用的字符集。比如 ISO-8859-1 |
| Accept-Encoding | 指定编码类型。它的值通常为 gzip 或compress |
| Accept-Language | 指定客户端首选语言，servlet会优先返回以当前语言构成的结果集，如果servlet支持这种语言的话。比如 en，en-us，ru等等 |
| Authorization | 在访问受密码保护的网页时识别不同的用户 |
| Connection | 表明客户端是否可以处理HTTP持久连接。持久连接允许客户端或浏览器在一个请求中获取多个文件。Keep-Alive 表示启用持久连接 |
| Content-Length | 仅适用于POST请求，表示 POST 数据的字节数 |
| Cookie | 返回先前发送给浏览器的cookies至服务器 |
| Host | 指出原始URL中的主机名和端口号 |
| If-Modified-Since | 表明只有当网页在指定的日期被修改后客户端才需要这个网页。 服务器发送304码给客户端，表示没有更新的资源 |
| If-Unmodified-Since | 与If-Modified-Since相反， 只有文档在指定日期后仍未被修改过，操作才会成功 |
| Referer | 标志着所引用页面的URL。比如，如果你在页面1，然后点了个链接至页面2，那么页面1的URL就会包含在浏览器请求页面2的信息头中 |
| User-Agent | 用来区分不同浏览器或客户端发送的请求，并对不同类型的浏览器返回不同的内容 |

---


## HttpServletRequest类

request对象是javax.servlet.http.HttpServletRequest类的实例。每当客户端请求一个页面时，JSP引擎就会产生一个新的对象来代表这个请求。


request对象提供了一系列方法来获取HTTP信息头，包括表单数据，cookies，HTTP方法等等。


接下来将会介绍一些在JSP编程中常用的获取HTTP信息头的方法。详细内容请见下表：


| 序号 | 方法& 描述 |
| --- | --- |
| 1 | Cookie[] getCookies() 返回客户端所有的Cookie的数组 |
| 2 | Enumeration getAttributeNames() 返回request对象的所有属性名称的集合 |
| 3 | Enumeration getHeaderNames() 返回所有HTTP头的名称集合 |
| 4 | Enumeration getParameterNames() 返回请求中所有参数的集合 |
| 5 | HttpSession getSession() 返回request对应的session对象，如果没有，则创建一个 |
| 6 | HttpSession getSession(boolean create) 返回request对应的session对象，如果没有并且参数create为true，则返回一个新的session对象 |
| 7 | Locale getLocale() 返回当前页的Locale对象，可以在response中设置 |
| 8 | Object getAttribute(String name) 返回名称为name的属性值，如果不存在则返回null。 |
| 9 | ServletInputStream getInputStream() 返回请求的输入流 |
| 10 | String getAuthType() 返回认证方案的名称，用来保护servlet，比如 "BASIC" 或者 "SSL" 或 null 如果 JSP没设置保护措施 |
| 11 | String getCharacterEncoding() 返回request的字符编码集名称 |
| 12 | String getContentType() 返回request主体的MIME类型，若未知则返回null |
| 13 | String getContextPath() 返回request URI中指明的上下文路径 |
| 14 | String getHeader(String name) 返回name指定的信息头 |
| 15 | String getMethod() 返回此request中的HTTP方法，比如 GET,，POST，或PUT |
| 16 | String getParameter(String name) 返回此request中name指定的参数，若不存在则返回null |
| 17 | String getPathInfo() 返回任何额外的与此request URL相关的路径 |
| 18 | String getProtocol() 返回此request所使用的协议名和版本 |
| 19 | String getQueryString() 返回此 request URL包含的查询字符串 |
| 20 | String getRemoteAddr() 返回客户端的IP地址 |
| 21 | String getRemoteHost() 返回客户端的完整名称 |
| 22 | String getRemoteUser() 返回客户端通过登录认证的用户，若用户未认证则返回null |
| 23 | String getRequestURI() 返回request的URI |
| 24 | String getRequestedSessionId() 返回request指定的session ID |
| 25 | String getServletPath() 返回所请求的servlet路径 |
| 26 | String[] getParameterValues(String name) 返回指定名称的参数的所有值，若不存在则返回null |
| 27 | boolean isSecure() 返回request是否使用了加密通道，比如HTTPS |
| 28 | int getContentLength() 返回request主体所包含的字节数，若未知的返回-1 |
| 29 | int getIntHeader(String name) 返回指定名称的request信息头的值 |
| 30 | int getServerPort() 返回服务器端口号 |

---


## HTTP信息头示例

在这个例子中，我们会使用HttpServletRequest类的getHeaderNames()方法来读取HTTP信息头。这个方法以枚举的形式返回当前HTTP请求的头信息。


获取Enumeration对象后，用标准的方式来遍历Enumeration对象，用hasMoreElements()方法来确定什么时候停止，用nextElement()方法来获得每个参数的名字。


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.io.*,java.util.*" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<h2>HTTP 头部请求实例</h2>
<table width="100%" border="1" align="center">
<tr bgcolor="#949494">
<th>Header Name</th><th>Header Value(s)</th>
</tr>
<%
   Enumeration headerNames = request.getHeaderNames();
   while(headerNames.hasMoreElements()) {
      String paramName = (String)headerNames.nextElement();
      out.print("<tr><td>" + paramName + "</td>\n");
      String paramValue = request.getHeader(paramName);
      out.println("<td> " + paramValue + "</td></tr>\n");
   }
%>
</table>
</body>
</html>
```


访问main.jsp，将会得到以下结果：


![](https://www.runoob.com/wp-content/uploads/2014/01/jspheadmsg.jpg)


您可以在上面代码中尝试HttpServletRequest类的其它方法。








	  AI 思考中...





			** [JSP 隐式对象](https://www.runoob.com/jsp-implicit-objects.html)
			[JSP 服务器响应](https://www.runoob.com/jsp-server-response.html) **













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
# Servlet 包

- Source: https://www.runoob.com/servlet/servlet-packaging.html

涉及到 WEB-INF 子目录的 Web 应用程序结构是所有的 Java web 应用程序的标准，并由 Servlet API 规范指定。给定一个顶级目录名 myapp，目录结构如下所示：


```
/myapp
    /images
    /WEB-INF
        /classes
        /lib
```


WEB-INF 子目录中包含应用程序的部署描述符，名为 web.xml。所有的 HTML 文件都位于顶级目录 *myapp* 下。对于 admin 用户，您会发现 ROOT 目录是 myApp 的父目录。


## 创建包中的 Servlet


WEB-INF/classes 目录包含了所有的 Servlet 类和其他类文件，类文件所在的目录结构与他们的包名称匹配。例如，如果您有一个完全合格的类名称 **com.myorg.MyServlet**，那么这个 Servlet 类必须位于以下目录中：


```
/myapp/WEB-INF/classes/com/myorg/MyServlet.class
```


下面的例子创建包名为 *com.myorg* 的 MyServlet 类。


```
// 为包命名
package com.myorg;

// 导入必需的 java 库
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

@WebServlet("/MyServlet")
public class MyServlet extends HttpServlet {

  private String message;

  public void init() throws ServletException
  {
      // 执行必需的的初始化
      message = "Hello World";
  }

  public void doGet(HttpServletRequest request,
                    HttpServletResponse response)
            throws ServletException, IOException
  {
      // 设置响应内容类型
      response.setContentType("text/html;charset=UTF-8");

      // 实际的逻辑是在这里
      PrintWriter out = response.getWriter();
      out.println("<h1>" + message + "</h1>");
  }

  public void destroy()
  {
      // 什么也不做
  }
}
```


## 编译包中的 Servlet


编译包中的类与编译其他的类没有什么大的不同。最简单的方法是让您的 java 文件保留完全限定路径，如上面提到的类，将被保留在 com.myorg 中。您还需要在 CLASSPATH 中添加该目录。


假设您的环境已正确设置，进入 **/webapps/ROOT/WEB-INF/classes** 目录，并编译 MyServlet.java，如下所示：


```
$ javac MyServlet.java
```


如果 Servlet 依赖于其他库，那么您必须在 CLASSPATH 中也要引用那些 JAR 文件。这里我只引用了 servlet-api.jar JAR 文件，因为我在 Hello World 程序中并没有使用任何其他库。


该命令行使用内置的 javac 编译器，它是 Sun Microsystems Java 软件开发工具包（JDK，全称 Java Software Development Kit）附带的。 Microsystems的Java软件开发工具包（JDK）。为了让该命令正常工作，必须包括您在 PATH 环境变量中所使用的 Java SDK 的位置。


如果一切顺利，上述编译会在同一目录下生成 **MyServlet.class** 文件。下一节将解释如何把一个已编译的 Servlet 部署到生产中。


## Servlet 打包部署


默认情况下，Servlet 应用程序位于路径 /webapps/ROOT 下，且类文件放在 /webapps/ROOT/WEB-INF/classes 中。


如果您有一个完全合格的类名称 **com.myorg.MyServlet**，那么这个 Servlet 类必须位于 WEB-INF/classes/com/myorg/MyServlet.class 中，您需要在位于 /webapps/ROOT/WEB-INF/ 的 web.xml 文件中创建以下条目：


```
<servlet>
        <servlet-name>MyServlet</servlet-name>
        <servlet-class>com.myorg.MyServlet</servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>MyServlet</servlet-name>
        <url-pattern>/MyServlet</url-pattern>
    </servlet-mapping>
```


上面的条目要被创建在 web.xml 文件中的 ... 标签内。在该文件中可能已经有各种可用的条目，但不要在意。


到这里，您基本上已经完成了，现在让我们使用 \bin\startup.bat（在 Windows 上）或 /bin/startup.sh（在 Linux/Solaris 等上）启动 tomcat 服务器，最后在浏览器的地址栏中输入 **http://localhost:8080/MyServlet**。如果一切顺利，您会看到下面的结果：


| # Hello World |
| --- |








	  AI 思考中...





			** [Servlet 发送电子邮件](https://www.runoob.com/servlet-sending-email.html)
			[Servlet 调试](https://www.runoob.com/servlet-debugging.html) **













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
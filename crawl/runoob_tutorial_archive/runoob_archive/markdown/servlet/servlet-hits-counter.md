# Servlet 点击计数器

- Source: https://www.runoob.com/servlet/servlet-hits-counter.html

## 网页点击计数器


很多时候，您可能有兴趣知道网站的某个特定页面上的总点击量。使用 Servlet 来计算这些点击量是非常简单的，因为一个 Servlet 的生命周期是由它运行所在的容器控制的。


以下是实现一个简单的基于 Servlet 生命周期的网页点击计数器需要采取的步骤：


- 在 init() 方法中初始化一个全局变量。
- 每次调用 doGet() 或 doPost() 方法时，都增加全局变量。
- 如果需要，您可以使用一个数据库表来存储全局变量的值在 destroy() 中。在下次初始化 Servlet 时，该值可在 init() 方法内被读取。这一步是可选的。
- 如果您只想对一个 session 会话计数一次页面点击，那么请使用 isNew() 方法来检查该 session 会话是否已点击过相同页面。这一步是可选的。
- 您可以通过显示全局计数器的值，来在网站上展示页面的总点击量。这一步是可选的。


在这里，我们假设 Web 容器将无法重新启动。如果是重新启动或 Servlet 被销毁，计数器将被重置。


## 实例


本实例演示了如何实现一个简单的网页点击计数器：


```
package com.runoob.test;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class PageHitCounter
 */
@WebServlet("/PageHitCounter")
public class PageHitCounter extends HttpServlet {
    private static final long serialVersionUID = 1L;
    private int hitCount;

    public void init()
    {
        // 重置点击计数器
        hitCount = 0;
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        response.setContentType("text/html;charset=UTF-8");
        // 增加 hitCount
        hitCount++;
        PrintWriter out = response.getWriter();
        String title = "总点击量";
        String docType = "<!DOCTYPE html> \n";
        out.println(docType +
            "<html>\n" +
            "<head><title>" + title + "</title></head>\n" +
            "<body bgcolor=\"#f0f0f0\">\n" +
            "<h1 align=\"center\">" + title + "</h1>\n" +
            "<h2 align=\"center\">" + hitCount + "</h2>\n" +
            "</body></html>");
    }

    public void destroy()
    {
        // 这一步是可选的，但是如果需要，您可以把 hitCount 的值写入到数据库
    }

}
```


现在让我们来编译上面的 Servlet，并在 web.xml 文件中创建以下条目：


```
<?xml version="1.0" encoding="UTF-8"?>
<web-app>
  <servlet>
    <servlet-name>PageHitCounter</servlet-name>
    <servlet-class>com.runoob.test.PageHitCounter</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>PageHitCounter</servlet-name>
    <url-pattern>/TomcatTest/PageHitCounter</url-pattern>
  </servlet-mapping>
</web-app>
```


现在通过访问 http://localhost:8080/TomcatTest/PageHitCounter 来调用这个 Servlet。这将会在每次页面刷新时，把计数器的值增加 1，结果如下所示：


| # 总点击量 ## 6 |
| --- |

**

## 网站点击计数器


很多时候，您可能有兴趣知道整个网站的总点击量。在 Servlet 中，这也是非常简单的，我们可以使用过滤器做到这一点。


以下是实现一个简单的基于过滤器生命周期的网站点击计数器需要采取的步骤：


- 在过滤器的 init() 方法中初始化一个全局变量。
- 每次调用 doFilter 方法时，都增加全局变量。
- 如果需要，您可以在过滤器的 destroy() 中使用一个数据库表来存储全局变量的值。在下次初始化过滤器时，该值可在 init() 方法内被读取, 这一步是可选的。


在这里，我们假设 Web 容器将无法重新启动。如果是重新启动或 Servlet 被销毁，点击计数器将被重置。


## 实例


本实例演示了如何实现一个简单的网站点击计数器：


```
// 导入必需的 java 库
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
import java.util.*;

public class SiteHitCounter implements Filter{

  private int hitCount;

  public void  init(FilterConfig config)
                    throws ServletException{
     // 重置点击计数器
     hitCount = 0;
  }

  public void  doFilter(ServletRequest request,
              ServletResponse response,
              FilterChain chain)
              throws java.io.IOException, ServletException {

      // 把计数器的值增加 1
      hitCount++;

      // 输出计数器
      System.out.println("网站访问统计："+ hitCount );

      // 把请求传回到过滤器链
      chain.doFilter(request,response);
  }
  public void destroy()
  {
      // 这一步是可选的，但是如果需要，您可以把 hitCount 的值写入到数据库
  }
}
```


现在让我们来编译上面的 Servlet，并在 web.xml 文件中创建以下条目：


```
....
<filter>
   <filter-name>SiteHitCounter</filter-name>
   <filter-class>SiteHitCounter</filter-class>
</filter>

<filter-mapping>
   <filter-name>SiteHitCounter</filter-name>
   <url-pattern>/*</url-pattern>
</filter-mapping>

....
```


现在访问网站的任意页面，比如 http://localhost:8080/。这将会在每次任意页面被点击时，把计数器的值增加 1，它会在日志中显示以下消息：


```
网站访问统计： 1
网站访问统计： 2
网站访问统计： 3
网站访问统计： 4
网站访问统计： 5
..................
```









	  AI 思考中...





			** [Servlet 网页重定向](https://www.runoob.com/servlet-page-redirect.html)
			[Servlet 自动刷新页面](https://www.runoob.com/servlet-auto-refresh.html) **













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
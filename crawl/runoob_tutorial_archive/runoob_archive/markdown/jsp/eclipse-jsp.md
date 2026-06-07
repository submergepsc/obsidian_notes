# Eclipse JSP/Servlet 环境搭建

- Source: https://www.runoob.com/jsp/eclipse-jsp.html

本文假定你已安装了 JDK 环境，如未安装，可参阅 [Java 开发环境配置](https://www.runoob.com/../java/java-environment-setup.html)。


我们可以使用 Eclipse 来搭建 JSP 开发环境，首先我们分别下载一下软件包：


- **Eclipse J2EE：**[http://www.eclipse.org/downloads/](http://www.eclipse.org/downloads/)
- **Tomcat：**[http://tomcat.apache.org/download-70.cgi](http://tomcat.apache.org/download-70.cgi)


---


## Tomcat 下载安装


你可以根据你的系统下载对应的包(以下以Window系统为例)：

![](https://www.runoob.com/wp-content/uploads/2016/01/232104286524890.png)


下载之后，将压缩包解压到D盘（你可以自己选择）：

![](https://www.runoob.com/wp-content/uploads/2016/01/232104410586765.png)


注意目录名不能有中文和空格。目录介绍如下： - bin：二进制执行文件。里面最常用的文件是**startup.bat**，如果是 Linux 或 Mac 系统启动文件为 **startup.sh**。 - conf:配置目录。里面最核心的文件是**server.xml**。可以在里面改端口号等。默认端口号是8080，也就是说，此端口号不能被其他应用程序占用。 - lib：库文件。tomcat运行时需要的jar包所在的目录 - logs：日志 - temp：临时产生的文件，即缓存 - webapps：web的应用程序。**web应用放置到此目录下浏览器可以直接访问** - work：编译以后的class文件。 接着我们可以双击 startup.bat 启动 Tomcat，弹出如下界面：


![](https://www.runoob.com/wp-content/uploads/2016/01/232105392158264.png)


这个时候，本地的服务器就已经搭建起来了。如果想关闭服务器，可以直接关闭上面的窗口，或者在里面输入Ctrl+C禁止服务。


接着我们在浏览器中输入 **http://localhost:8080/**，如果弹出如下界面，表示tomcat安装成功并且启动起来了：


![](https://www.runoob.com/wp-content/uploads/2016/01/tomcat-index.jpg)


我们现在在浏览器上测试一下它吧：

首先在D:\apache-tomcat-8.0.14\webapps\ROOT目录中新建一个jsp文件：


![](https://www.runoob.com/wp-content/uploads/2016/01/232106198557249.jpg)


test.jsp 文件代码如下：


```
<%@ page contentType="text/html;charset=UTF-8" %>
<%
out.print("菜鸟教程 : http://www.runoob.com");
%>
```


接着在浏览器中访问地址 **http://localhost:8080/test.jsp**, 输出结果如下：


![](https://www.runoob.com/wp-content/uploads/2016/01/test-jsp.jpg)


---


## 将 Tomcat 和 Eclipse 相关联


Eclipse J2EE下载后，解压即可使用，我们打开Java EE ，选择菜单栏Windows-->preferences（Mac 系统为 Eclipse-->偏好设置），弹出如下界面：


![](https://www.runoob.com/wp-content/uploads/2016/01/232111301681549.png)


上图中，点击"add"的添加按钮，弹出如下界面：


![](https://www.runoob.com/wp-content/uploads/2016/01/232111442933866.png)


在选项中，我们选择对应的 Tomcat 版本，接着点击 "Next"，选择 Tomcat 的安装目录，并选择我们安装的 Java 环境：

![](https://www.runoob.com/wp-content/uploads/2016/01/232112245587963.png)


点击 "Finish"，完成配置。


### 创建实例


选择 "File-->New-->Dynamic Web Project"，创建 TomcatTest 项目：

![](https://www.runoob.com/wp-content/uploads/2016/01/232112541213100.png)

![](https://www.runoob.com/wp-content/uploads/2016/01/302044303245040.png)


点开上图中的红框部分，弹出如下界面：


![](https://www.runoob.com/wp-content/uploads/2016/01/8998BEC1-D622-4BD4-A9E6-8B18D2A5F29C.jpg)


注意如果已默认选择了我们之前安装的 Tomcat 和 JDK 则可跳过此步。


然后，单击finish, 继续：


![](https://www.runoob.com/wp-content/uploads/2016/01/232113121219000.png)


![](https://www.runoob.com/wp-content/uploads/2016/01/232113256216676.png)


工程文件结构：


![](https://www.runoob.com/wp-content/uploads/2016/01/232113367466511.png)


上图中各个目录解析：


- deployment descriptor：部署的描述。
- Web App Libraries：自己加的包可以放在里面。
- build：放入编译之后的文件。
- WebContent:放进写入的页面。


在WebContent文件夹下新建一个test.jsp文件。在下图中可以看到它的默认代码：


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>

</body>
</html>
```


接着我们修改下test.jsp文件代码如下所示：


```
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>菜鸟教程</title>
</head>
<body>
<%
    out.println("Hello World!");
%>
</body>
</html>
```


程序运行之前，我们先修改一下浏览器选项:

![](https://www.runoob.com/wp-content/uploads/2016/01/testjsp1.png)


接着我们运行该项目:

![](https://www.runoob.com/wp-content/uploads/2016/01/runas.png)

运行时，弹出如下错误：(如果没有此错误，请忽略)

![](https://www.runoob.com/wp-content/uploads/2016/01/232120047932694.png)

原因是，我们之前点击了Tomcat安装包中的​startup.bat，这样一来就手动打开了Tomcat服务器，这明显是多余的，因为程序运行时，eclipse会自动开启Tomcat服务器。所以我们先手动关掉tomcat软件，再次运行程序，就行了。控制台信息如下：

![](https://www.runoob.com/wp-content/uploads/2016/01/232120199803353.png)


浏览器访问 **http://localhost:8080/TomcatTest/test.jsp**, 即可输出正常结果：


![](https://www.runoob.com/wp-content/uploads/2016/01/A72F19CD-4FEA-4AE3-8D91-43B34623EC37.jpg)


---


## Servlet 实例创建


我们也可以使用以上环境创建 Servlet 文件，选择 "File-->New-->Servlet":

![](https://www.runoob.com/wp-content/uploads/2016/01/sns.png)


位于 TomcatTest项目的 /TomcatTest/src 目录下创建 "HelloServlet" 类，包为 "com.runoob.test":


![](https://www.runoob.com/wp-content/uploads/2016/01/22D8CED0-F2DD-4554-BFBD-2B19D1685FB9.jpg)


HelloServlet.java 代码如下所示：


```
package com.runoob.test;

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class HelloServlet
 */
@WebServlet("/HelloServlet")
public class HelloServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    /**
     * @see HttpServlet#HttpServlet()
     */
    public HelloServlet() {
        super();
        // TODO Auto-generated constructor stub
    }

    /**
     * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // 使用 GBK 设置中文正常显示
        response.setCharacterEncoding("GBK");
        response.getWriter().write("菜鸟教程：http://www.runoob.com");
    }

    /**
     * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
     */
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        // TODO Auto-generated method stub
        doGet(request, response);
    }

}
```


创建 /TomcatTest/WebContent/WEB-INF/web.xml 文件（如果没有），代码如下所示：


```
<?xml version="1.0" encoding="UTF-8"?>
<web-app version="2.5"
    xmlns="http://java.sun.com/xml/ns/javaee"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
    http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">
  <servlet>
     <!-- 类名 -->
    <servlet-name>HelloServlet</servlet-name>
    <!-- 所在的包 -->
    <servlet-class>com.runoob.test.HelloServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>HelloServlet</servlet-name>
    <!-- 访问的网址 -->
    <url-pattern>/TomcatTest/HelloServlet</url-pattern>
    </servlet-mapping>
</web-app>
```


接着重启 Tomcat，浏览器访问 **http://localhost:8080/TomcatTest/HelloServlet**：

![](https://www.runoob.com/wp-content/uploads/2016/01/3E00DBEA-85CA-4F66-A7E9-24C43BC9C756.jpg)


参考文章：http://www.cnblogs.com/smyhvae/p/4046862.html








	  AI 思考中...





			** [JSP 标准标签库（JSTL）](https://www.runoob.com/jsp-jstl.html)
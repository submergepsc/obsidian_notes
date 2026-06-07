# ASP Request 对象

- Source: https://www.runoob.com/asp/asp-ref-request.html

---


Request 对象用于从访客那里获取信息。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## QueryString 集合实例


[当用户点击链接时发送查询信息](https://www.runoob.com/try/showasp.php?filename=demo_simplequerystring)** 本例演示如何在链接中向页面发送查询信息，并在目标页面中取回这些信息（在本例中是同一页面）。


[QueryString 集合的简单应用](https://www.runoob.com/try/showasp.php?filename=demo_simplereqquery) 本例演示如何使用 QueryString 集合从表单取回值。（此表单使用 GET 方法，这意味着所发送的信息对用户来说是可见的。）


[如何使用来自表单的信息](https://www.runoob.com/try/showasp.php?filename=demo_simplereqquery) 本例演示如何使用从表单取回的值。此表单使用 GET 方法。


[来自表单的更多信息](https://www.runoob.com/try/showasp.php?filename=demo_reqquery2) 本例演示如果输入字段包含若干相同的名称，QueryString 集合会包含什么内容。它将展示如何使用 Count 关键词来对 "name" 属性进行计数。此表单使用 GET 方法。


![Examples](https://www.runoob.com/images/tryitimg.gif)
## Form 集合实例


[Form 集合的简单应用](https://www.runoob.com/try/showasp.php?filename=demo_simpleform1) 本例演示如何使用 Form 集合从表单取回值。（此表单使用 POST 方法，这意味着所发送的信息对用户来说是不可见的。）


[如何使用来自表单的信息](https://www.runoob.com/try/showasp.php?filename=demo_simpleform) 本例演示如何使用从表单取回的值。此表单使用了 POST 方法。


[来自表单的更多信息](https://www.runoob.com/try/showasp.php?filename=demo_form2) 本例演示如果输入字段包含若干相同的名称，Form 集合会包含什么内容。它将展示如何使用 Count 关键词来对 "name" 属性进行计数。此表单使用了 POST 方法。


[带有单选按钮的表单](https://www.runoob.com/try/showasp.php?filename=demo_radiob) 本例演示如何使用 Form 集合通过单选按钮与用户进行交互。此表单使用 POST 方法。


[带有复选框的表单](https://www.runoob.com/try/showasp.php?filename=demo_checkboxes) 本例演示如何使用 Form 集合通过复选框与用户进行交互。此表单使用 POST 方法。


![实例](https://www.runoob.com/images/tryitimg.gif)
## 其他实例


[获取服务器变量](https://www.runoob.com/try/showasp.php?filename=demo_server) 本例演示如何取得访客的浏览器类型、IP 地址等信息。


[创建 welcome cookie](https://www.runoob.com/try/showasp.php?filename=demo_cookies) 本例演示如何创建一个 Welcome Cookie。


[探测用户发送的字节总数](https://www.runoob.com/try/showasp.php?filename=demo_totalbytes) 本例演示如何探测用户在 Request 对象中发送的字节总数。


---


## Request 对象


当浏览器向服务器请求页面时，这个行为就被称为一个 request（请求）。Request 对象用于从用户那里获取信息。它的集合、属性和方法描述如下：


### 集合


| 集合 | 描述 |
| --- | --- |
| ClientCertificate | 包含了存储在客户证书中的所有的字段值。 |
| Cookies | 包含了 HTTP 请求中发送的所有的 cookie 值。 |
| Form | 包含了使用 post 方法由表单发送的所有的表单（输入）值。 |
| QueryString | 包含了 HTTP 查询字符串中所有的变量值。 |
| ServerVariables | 包含了所有的服务器变量值。 |


### 属性


| 属性 | 描述 |
| --- | --- |
| TotalBytes | 返回在请求正文中客户端发送的字节总数。 |


### 方法


| 方法 | 描述 |
| --- | --- |
| BinaryRead | 取回作为 post 请求的一部分而从客户端发送至服务器的数据，并把它存储在一个安全的数组中。 |










	  AI 思考中...





			** [ASP Response 对象](https://www.runoob.com/asp-ref-response.html)
			[ASP Application 对象](https://www.runoob.com/asp-ref-application.html) **













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
# ASP.NET Web Pages - WebMail 帮助器

- Source: https://www.runoob.com/aspnet/webpages-email.html

---


WebMail 帮助器 - 众多有用的 ASP.NET Web 帮助器之一。


---


## WebMail 帮助器


WebMail 帮助器让发送邮件变得更简单，它按照 SMTP（Simple Mail Transfer Protocol 简单邮件传输协议）从 Web 应用程序发送邮件。


---


## 前提：电子邮件支持


为了演示如何使用电子邮件，我们将创建一个输入页面，让用户提交一个页面到另一个页面，并发送一封关于支持问题的邮件。


---


## 第一：编辑您的 AppStart 页面


如果在本教程中您已经创建了 Demo 应用程序，那么您已经有一个名为 _AppStart.cshtml 的页面，内容如下：


## _AppStart.cshtml


```csharp
@{WebSecurity.InitializeDatabaseConnection("Users", "UserProfile", "UserId",
"Email", true);}
```


**


要启动 WebMail 帮助器，向您的 AppStart 页面中增加如下所示的 WebMail 属性：


## _AppStart.cshtml


```csharp
@{WebSecurity.InitializeDatabaseConnection("Users", "UserProfile", "UserId",
"Email", true);WebMail.SmtpServer = "smtp.example.com";WebMail.SmtpPort = 25;
WebMail.EnableSsl = false;WebMail.UserName = "[email protected]";
WebMail.Password = "password-goes-here";WebMail.From = "[email protected]";}
```


属性解释：


SmtpServer:** 用于发送电子邮件的 SMTP 服务器的名称。


**SmtpPort:** 服务器用来发送 SMTP 事务（电子邮件）的端口。


**EnableSsl:** 如果服务器使用 SSL（Secure Socket Layer 安全套接层）加密，则值为 true。


**UserName:** 用于发送电子邮件的 SMTP 电子邮件账户的名称。


**Password:** SMTP 电子邮件账户的密码。


**From:** 在发件地址栏显示的电子邮件（通常与 UserName 相同）。


---


## 第二：创建一个电子邮件输入页面


接着创建一个输入页面，并将它命名为 Email_Input：


## Email_Input.cshtml


```csharp
<!DOCTYPE html> <html> <body> <h1>Request for
Assistance</h1> <form method="post" action="EmailSend.cshtml">
<label>Username:</label><input type="text name="customerEmail" />
<label>Details about the problem:</label> <textarea name="customerRequest"
cols="45" rows="4"></textarea> <p><input type="submit" value="Submit"
/></p> </form> </body> </html>
```


**


输入页面的目的是手机信息，然后提交数据到可以将信息作为电子邮件发送的一个新的页面。


---


## 第三：创建一个电子邮件发送页面


接着创建一个用来发送电子邮件的页面，并将它命名为 Email_Send：


## Email_Send.cshtml


```csharp
@{ // Read input
var customerEmail = Request["customerEmail"];
var customerRequest = Request["customerRequest"];
try
{
// Send email
WebMail.Send(to:"[email protected]", subject: "Help request from - " + customerEmail, body:
customerRequest );
}
catch (Exception ex )
{
<text>@ex</text>

}}
```


想了解更多关于 ASP.NET Web Pages 应用程序发送电子邮件的信息，请查阅：[WebMail 对象参考手册](https://www.runoob.com/webpages-ref-webmail.html)。










	  AI 思考中...





			** [ASP.NET Web Pages 图表](https://www.runoob.com/webpages-chart.html)
			[ASP.NET Web Pages PHP](https://www.runoob.com/webpages-php.html) **













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
# ASP.NET Web Pages - WebMail 对象

- Source: https://www.runoob.com/aspnet/webpages-ref-webmail.html

---


通过 WebMail 对象，您可以很容易地从网页上发送电子邮件。


---


## 描述


**WebMail 对象**为 ASP.NET Web Pages 提供了使用 SMTP（Simple Mail Transfer Protocol 简单邮件传输协议）发送邮件的功能。


---


## 实例


请查看 [WebPages Email](https://www.runoob.com/webpages-email.html) 章节中的实例。


---


## WebMail 对象参考手册 - 属性


| 属性 | 描述 |
| --- | --- |
| SmtpServer | 用于发送电子邮件的 SMTP 服务器的名称。 |
| SmtpPort | 服务器用来发送 SMTP 电子邮件的端口。 |
| EnableSsl | 如果服务器使用 SSL（Secure Socket Layer 安全套接层）加密，则值为 true。 |
| UserName | 用于发送电子邮件的 SMTP 电子邮件账户的名称。 |
| Password | SMTP 电子邮件账户的密码。 |
| From | 在发件地址栏显示的电子邮件（通常与 UserName 相同）。 |

**
---


## WebMail 对象参考手册 - 方法


| 方法 | 描述 |
| --- | --- |
| Send() | 向 SMTP 服务器发送需要传送的电子邮件信息。 |


Send() 方法有以下参数：


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| to | String | 收件人（用分号分隔） |
| subject | String | 邮件主题 |
| body | String | 邮件正文 |


Send() 方法有以下可选参数：


| 参数 | 类型 | 描述 |
| --- | --- | --- |
| from | String | 发件人 |
| cc | String | 需要抄送的电子邮件地址（用分号分隔） |
| filesToAttach | Collection | 附件名 |
| isBodyHtml | Boolean | 如果邮件正文是 HTML 格式的，则为 true |
| additionalHeaders | Collection | 附加的标题 |


---


## 技术数据


| 名称 | 值 |
| --- | --- |
| Class | System.Web.Helpers.WebMail |
| Namespace | System.Web.Helpers |
| Assembly | System.Web.Helpers.dll |


---


## 初始化 WebMail 帮助器


要使用 WebMail 帮助器，您必须能访问 SMTP 服务器。SMTP 是电子邮件的"输出"部分。如果您使用的是虚拟主机，您可能已经知道 SMTP 服务器的名称。如果您使用的是公司网络工作，您公司的 IT 部门会给您一个名称。如果您是在家工作，你也许可以使用普通的电子邮件服务提供商。


为了发送一封电子邮件，您将需要：


- SMTP 服务器的名称
- 端口号（通常是 25 ）
- 电子邮件的用户名
- 电子邮件的密码


在您的 Web 根目录下，创建一个名为 _AppStart.cshtml** 的页面（如果已存在，则直接编辑页面）。


将下面的代码复制到文件中：


## _AppStart.cshtml


```csharp
@{WebMail.SmtpServer = "smtp.example.com";WebMail.SmtpPort = 25;
WebMail.EnableSsl = false;WebMail.UserName = "[email protected]";
WebMail.Password = "password";WebMail.From = "[email protected]"}
```


上面的代码将在每次网站（应用程序）启动时运行。它对 **WebMail 对象**赋了初始值。


请替换：


将 **smtp.example.com** 替换成您要用来发送电子邮件的 SMTP 服务器的名称。


将 **25** 替换成服务器用来发送 SMTP 事务（电子邮件）的端口号。


如果服务器使用 SSL（Secure Socket Layer 安全套接层）加密，请将 **false** 替换成 true。


将 **[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)** 替换成用来发送电子邮件的 SMTP 电子邮件账户的名称。


将 **password** 替换成 SMTP 电子邮件账户的密码。


将 **john@example ** 替换成显示在发件地址栏中的电子邮件。


|  | 在您的 AppStart 文件中，您不需要启动 WebMail 对象，但是在调用 WebMail.Send() 方法之前，您必须设置这些属性。 |
| --- | --- |

**








	  AI 思考中...





			** [ASP.NET Web Pages Database 参考手册](https://www.runoob.com/webpages-ref-database.html)
			[ASP.NET WebPages 帮助器参考手册](https://www.runoob.com/webpages-ref-helpers.html) **













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
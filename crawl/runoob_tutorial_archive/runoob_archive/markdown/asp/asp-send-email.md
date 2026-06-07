# ASP 使用 CDOSYS 发送电子邮件

- Source: https://www.runoob.com/asp/asp-send-email.html

---


CDOSYS 是 ASP 中的内建组件。此组件用于通过 ASP 发送电子邮件。


---


## 使用 CDOSYS 发送电子邮件


CDO (Collaboration Data Objects) 是一项微软的技术，设计目的是用来简化通讯应用程序的创建。


CDOSYS 是 ASP 中的内建组件。我们将向您演示如何通过 ASP 使用该组件来发送电子邮件。


## CDONTs 怎么样？


微软已经在 Windows 2000、Windows XP 和 Windows 2003 中淘汰了 CDONTs。如果您已经在您的 ASP 应用程序中使用 CDONTs，那么您需要更新代码，并使用新的 CDO 技术。


## 使用 CDOSYS 的实例


发送文本电子邮件：


<%**
Set myMail=CreateObject("CDO.Message")

myMail.Subject="Sending email with CDO"

myMail.From="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.To="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.TextBody="This is a message."

myMail.Send

set myMail=nothing

%>


发送带有 Bcc 和 CC 字段的文本电子邮件：


<%

Set myMail=CreateObject("CDO.Message")

myMail.Subject="Sending email with CDO"

myMail.From="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.To="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.Bcc="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.Cc="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.TextBody="This is a message."

myMail.Send

set myMail=nothing

%>


发送 HTML 电子邮件：


<%

Set myMail=CreateObject("CDO.Message")

myMail.Subject="Sending email with CDO"

myMail.From="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.To="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.HTMLBody = "<h1>This is a message.</h1>"

myMail.Send

set myMail=nothing

%>


发送一封内容为某个网站的某个网页的 HTML 电子邮件：


<%

Set myMail=CreateObject("CDO.Message")

myMail.Subject="Sending email with CDO"

myMail.From="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.To="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.CreateMHTMLBody "http://www.w3cschool.cc/asp/"

myMail.Send

set myMail=nothing

%>


发送一封内容为您的计算机中某个文件的某个网页的 HTML 电子邮件：


<%

Set myMail=CreateObject("CDO.Message")

myMail.Subject="Sending email with CDO"

myMail.From="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.To="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.CreateMHTMLBody "file://c:/mydocuments/test.htm"

myMail.Send

set myMail=nothing

%>


发送一封带有附件的文本电子邮件：


<%

Set myMail=CreateObject("CDO.Message")

myMail.Subject="Sending email with CDO"

myMail.From="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.To="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.TextBody="This is a message."

myMail.AddAttachment "c:mydocumentstest.txt"

myMail.Send

set myMail=nothing

%>


使用远程服务器发送一封文本电子邮件：


<%

Set myMail=CreateObject("CDO.Message")

myMail.Subject="Sending email with CDO"

myMail.From="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.To="[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

myMail.TextBody="This is a message."

myMail.Configuration.Fields.Item _

("http://schemas.microsoft.com/cdo/configuration/sendusing")=2

'Name or IP of remote SMTP server

myMail.Configuration.Fields.Item _

("http://schemas.microsoft.com/cdo/configuration/smtpserver")="smtp.server.com"

'Server port

myMail.Configuration.Fields.Item _

("http://schemas.microsoft.com/cdo/configuration/smtpserverport")=25

myMail.Configuration.Fields.Update

myMail.Send

set myMail=nothing

%>









	  AI 思考中...





			** [ASP Global.asa](https://www.runoob.com/asp-globalasa.html)
			[ASP Response 对象](https://www.runoob.com/asp-ref-response.html) **













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
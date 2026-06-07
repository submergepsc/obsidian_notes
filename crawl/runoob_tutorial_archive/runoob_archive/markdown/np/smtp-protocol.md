# SMTP 协议

- Source: https://www.runoob.com/np/smtp-protocol.html

SMTP（Simple Mail Transfer Protocol，简单邮件传输协议）是一种用于发送电子邮件的网络协议。

SMTP 是互联网上电子邮件传输的核心协议之一，负责将邮件从发送方传递到接收方的邮件服务器。


---


## SMTP 的工作原理


SMTP 使用客户端-服务器模型，通过明文或加密的通信通道传输邮件。它的核心功能是发送邮件和传递邮件。


### 1. SMTP 连接建立


![](https://www.runoob.com/wp-content/uploads/2025/02/smtp-1.png)


- 客户端连接到服务器的 25 端口（默认的 SMTP 端口）。
- 服务器返回状态码 220，表示服务已就绪。
- 客户端发送 HELO 或 EHLO 命令，告知服务器自己的域名。
- 服务器返回状态码 250，表示命令成功。


### 2. 邮件发送


在连接建立后，客户端可以发送邮件。以下是典型的邮件发送流程：


![](https://www.runoob.com/wp-content/uploads/2025/02/smtp-2.png)


- **MAIL FROM**：客户端指定发件人邮箱。
- **RCPT TO**：客户端指定收件人邮箱。
- **DATA**：客户端开始输入邮件内容。
- **邮件内容**：客户端发送邮件正文。
- **.**：客户端用单独一行的句点表示邮件输入结束。
- 服务器返回状态码 250，表示邮件接收成功。


### 3. 连接关闭 在邮件发送完成后，客户端可以关闭连接： 客户端发送 QUIT 命令，请求关闭连接。 服务器返回状态码 221，表示连接已关闭。 SMTP 的关键特性 文本协议： SMTP 是基于文本的协议，命令和响应都是可读的字符串。 可靠性： 通过状态码和重试机制确保邮件传输的可靠性。 扩展性： 支持扩展命令（如 EHLO）和扩展功能（如身份验证、加密）。 安全性： 支持 STARTTLS 命令，将明文连接升级为加密连接。 SMTP 的应用场景 SMTP 广泛应用于以下场景： 邮件发送：将邮件从发送方传递到接收方的邮件服务器。 邮件中继：通过多个 SMTP 服务器传递邮件。 邮件客户端：Outlook、Thunderbird 等邮件客户端使用 SMTP 发送邮件。 SMTP 的安全性 SMTP 本身是不安全的，因为它在传输过程中使用明文传输数据。为了提高安全性，可以使用以下扩展： STARTTLS：将明文连接升级为加密连接，使用 TLS/SSL 加密数据。 SMTP AUTH：通过身份验证机制（如 PLAIN、LOGIN）验证用户身份。 SMTP 的替代方案 在某些场景下，可以使用以下替代方案： API 发送邮件：通过邮件服务提供商（如 SendGrid、Mailgun）的 API 发送邮件。 Web 邮件服务：通过 Web 界面（如 Gmail、Outlook.com）发送邮件。 总结来说，SMTP 是一种用于发送电子邮件的协议，通过客户端-服务器模型将邮件从发送方传递到接收方的邮件服务器。它支持扩展功能和安全性改进，但需要注意其明文传输的问题。如果你对 SMTP 的某个具体特性或应用场景感兴趣，可以进一步探讨！ AI 思考中... TCP 协议 DNS 协议 点我分享笔记







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
# POP3 协议

- Source: https://www.runoob.com/np/pop3-protocol.html

POP3（Post Office Protocol version 3，邮局协议第3版）是一种用于从邮件服务器下载电子邮件的协议。


POP3 允许用户通过客户端（如 Outlook、Thunderbird）从服务器获取邮件，并将邮件存储到本地设备。


## POP3 的工作原理


POP3 使用客户端-服务器模型，通过明文或加密的通信通道传输邮件。它的核心功能是从服务器下载邮件。


### 1. POP3 连接建立


![](https://www.runoob.com/wp-content/uploads/2025/02/export_6p2pp.png)


- 客户端连接到服务器的 110 端口（默认的 POP3 端口）。
- 服务器返回 `+OK`，表示服务已就绪。
- 客户端发送用户名（USER 命令），服务器返回 `+OK`，表示需要密码。
- 客户端发送密码（PASS 命令），服务器返回 `+OK`，表示登录成功。


---


### 2. 邮件下载


在连接建立后，客户端可以下载邮件。以下是典型的邮件下载流程：

![](https://www.runoob.com/wp-content/uploads/2025/02/pop3-1_9g0klf.png)


- **STAT**：客户端获取邮件的数量和总大小。
- **LIST**：客户端获取邮件列表。
- **RETR**：客户端下载指定邮件。
- **DELE**：客户端标记邮件为删除状态（邮件在 QUIT 命令后删除）。


---


### 3. 连接关闭


在邮件下载完成后，客户端可以关闭连接：


![](https://www.runoob.com/wp-content/uploads/2025/02/pop3-2_30gt4o.png)


- 客户端发送 QUIT 命令，请求关闭连接。
- 服务器返回 `+OK`，表示连接已关闭，并删除标记为删除的邮件。


---


## POP3 的关键特性


- **简单易用**： - 协议简单，易于实现和使用。
- **邮件下载**： - 将邮件从服务器下载到本地设备。
- **删除机制**： - 支持在下载后删除服务器上的邮件。
- **无状态协议**： - 服务器不会保存客户端的状态。


---


## POP3 的应用场景


POP3 广泛应用于以下场景：


- **邮件客户端**：Outlook、Thunderbird 等邮件客户端使用 POP3 下载邮件。
- **离线访问**：用户可以在离线状态下访问下载的邮件。
- **存储管理**：通过删除服务器上的邮件，节省服务器存储空间。


---


## POP3 的安全性问题


POP3 本身是不安全的，因为它在传输过程中使用明文传输数据，容易受到以下攻击：


- **窃听**：攻击者可以窃听传输的数据。
- **篡改**：攻击者可以篡改传输的数据。
- **伪装**：攻击者可以伪装成服务器或客户端。


为了提高安全性，可以使用 POP3S（POP3 Secure），即 POP3 over TLS/SSL，通过加密通信保护数据传输。


---


## POP3 的替代方案


在某些场景下，可以使用以下替代方案：


- **IMAP**：支持在服务器上管理邮件，适合多设备访问。
- **Web 邮件服务**：通过 Web 界面（如 Gmail、Outlook.com）访问邮件。


---


总结来说，POP3 是一种用于下载电子邮件的协议，通过客户端-服务器模型将邮件从服务器下载到本地设备。它简单易用，适合离线访问和存储管理，但需要注意其安全性问题。如果你对 POP3 的某个具体特性或应用场景感兴趣，可以进一步探讨！








	  AI 思考中...





			** [HTTPS 协议](https-protocol.html)
			[IMAP 协议](https://www.runoob.com/imap-protocol.html) **













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
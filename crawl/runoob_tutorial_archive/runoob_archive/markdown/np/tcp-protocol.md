# TCP 协议

- Source: https://www.runoob.com/np/tcp-protocol.html

TCP（Transmission Control Protocol，传输控制协议）是互联网协议套件中的核心协议之一，位于传输层。它提供了一种可靠的、面向连接的、基于字节流的数据传输服务。TCP 的主要特点是确保数据在传输过程中不丢失、不重复，并且按顺序到达。以下是 TCP 的工作原理和关键特性的详细解释。


---


## TCP 的工作原理


TCP 通过"三次握手"建立连接，通过"四次挥手"终止连接，并在数据传输过程中使用确认机制、重传机制和流量控制来保证可靠性。


### 1. 三次握手建立连接


![](https://www.runoob.com/wp-content/uploads/2025/02/tcp-1.png)


- **SYN**：客户端发送一个 SYN 包（同步请求）给服务器，表示请求建立连接。
- **SYN-ACK**：服务器收到 SYN 包后，回复一个 SYN-ACK 包（同步确认），表示同意建立连接。
- **ACK**：客户端收到 SYN-ACK 包后，发送一个 ACK 包（确认），表示连接已建立。


### 2. 数据传输


在连接建立后，TCP 通过以下机制确保数据的可靠传输：


- **序列号和确认号**：每个数据包都有一个序列号，接收方通过确认号告知发送方哪些数据已成功接收。
- **重传机制**：如果发送方未收到确认，会重新发送数据包。
- **流量控制**：通过滑动窗口机制，动态调整发送速率，避免接收方缓冲区溢出。
- **拥塞控制**：通过慢启动、拥塞避免等算法，动态调整发送速率，避免网络拥塞。


### 3. 四次挥手终止连接


![](https://www.runoob.com/wp-content/uploads/2025/02/tcp-2.png)


- **FIN**：客户端发送一个 FIN 包，表示请求关闭连接。
- **ACK**：服务器收到 FIN 包后，回复一个 ACK 包，表示确认。
- **FIN**：服务器发送一个 FIN 包，表示服务器也准备关闭连接。
- **ACK**：客户端收到 FIN 包后，回复一个 ACK 包，表示确认。连接正式关闭。


---


## TCP 的关键特性


- **可靠性**： - 通过确认机制和重传机制，确保数据不丢失、不重复。 - 通过校验和检查数据完整性。
- **面向连接**： - 在数据传输前需要建立连接，传输结束后需要关闭连接。
- **有序性**： - 数据按发送顺序到达接收方。
- **流量控制**： - 通过滑动窗口机制，动态调整发送速率。
- **拥塞控制**： - 通过慢启动、拥塞避免等算法，避免网络拥塞。


---


### TCP 的应用场景


TCP 广泛应用于需要可靠传输的场景，例如：


- 网页浏览（HTTP/HTTPS）
- 文件传输（FTP）
- 电子邮件（SMTP/POP3/IMAP）
- 远程登录（SSH/Telnet）


---


总结来说，TCP 是一种可靠的、面向连接的协议，通过三次握手建立连接、四次挥手关闭连接，并在数据传输过程中使用确认、重传、流量控制和拥塞控制等机制来保证数据的可靠传输。如果你对 TCP 的某个具体机制或应用场景感兴趣，可以进一步探讨！









	  AI 思考中...





			** [Telnet 协议](https://www.runoob.com/telnet-protocol.html)
			[SMTP 协议](https://www.runoob.com/smtp-protocol.html) **













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
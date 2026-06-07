# FTP 协议

- Source: https://www.runoob.com/np/ftp-protocol.html

FTP（File Transfer Protocol，文件传输协议）是一种用于在网络上传输文件的协议。


FTP 允许用户从一台计算机（客户端）向另一台计算机（服务器）上传或下载文件。

FTP 是互联网上最早使用的协议之一，至今仍然广泛用于文件传输。


---


## FTP 的工作原理

FTP 使用客户端-服务器模型，通过两个独立的连接进行通信：



- 控制连接：用于发送命令和接收响应。
- 数据连接：用于实际传输文件。


### 1. FTP 连接建立


![](https://www.runoob.com/wp-content/uploads/2025/02/export_ggzj7e.png)


- 客户端连接到服务器的 21 端口（默认的控制连接端口）。
- 服务器返回状态码 220，表示服务已就绪。
- 客户端发送用户名（USER 命令），服务器返回 331，表示需要密码。
- 客户端发送密码（PASS 命令），服务器返回 230，表示登录成功。


### 2. 文件传输

FTP 支持两种模式传输文件：


- 主动模式：服务器主动连接到客户端的数据端口。
- 被动模式：客户端连接到服务器的数据端口。


**主动模式**


![](https://www.runoob.com/wp-content/uploads/2025/02/export_dqjr9g.png)


- 客户端发送 PORT 命令，告知服务器自己的 IP 地址和数据端口。
- 服务器连接到客户端的数据端口，开始传输文件。


**被动模式**


![](https://www.runoob.com/wp-content/uploads/2025/02/export_hk7amh.png)


- 客户端发送 PASV 命令，请求进入被动模式。
- 服务器返回自己的 IP 地址和数据端口。
- 客户端连接到服务器的数据端口，开始传输文件。

### FTP 的关键特性


- **双连接模型**： - 控制连接用于发送命令和接收响应。 - 数据连接用于实际传输文件。
- **支持多种传输模式**： - 主动模式：服务器主动连接客户端。 - 被动模式：客户端连接服务器。
- **支持匿名访问**： - 允许用户以"anonymous"身份登录，无需密码。
- **支持文件操作**： - 上传、下载、删除、重命名文件等。
- **支持目录操作**： - 列出目录内容、创建目录、删除目录等。


---


### FTP 的应用场景


FTP 广泛应用于以下场景：


- 网站维护：上传和下载网站文件。
- 文件共享：在组织内部或外部共享文件。
- 软件分发：提供软件下载服务。


---


### FTP 的安全性


FTP 本身是不安全的，因为它在传输过程中使用明文传输用户名、密码和数据。为了提高安全性，可以使用以下替代方案：


- **SFTP**：基于 SSH 的文件传输协议，加密传输数据。
- **FTPS**：基于 SSL/TLS 的 FTP，加密传输数据。


---


总结来说，FTP 是一种用于文件传输的协议，通过控制连接和数据连接实现文件的上传和下载。它支持主动模式和被动模式，但需要注意其安全性问题。如果你对 FTP 的某个具体特性或应用场景感兴趣，可以进一步探讨！








	  AI 思考中...





			** [常见网络设备](https://www.runoob.com/network-devices.html)
			[SSH 协议](https://www.runoob.com/secure-shell.html) **













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
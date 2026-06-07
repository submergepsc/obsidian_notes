# SFTP 协议

- Source: https://www.runoob.com/np/sftp-protocol.html

SFTP（SSH File Transfer Protocol，SSH 文件传输协议）是一种基于 SSH（Secure Shell）的文件传输协议，用于在客户端和服务器之间安全地传输文件。


与传统的 [FTP](https://www.runoob.com/ftp-protocol.html) 不同，SFTP 通过加密通信保护数据传输，适合传输敏感信息。


---


## SFTP 的工作原理

SFTP 使用客户端-服务器模型，通过 SSH 的加密通道传输文件。它的核心功能是安全地传输文件。


### 1. SFTP 连接建立


![](https://www.runoob.com/wp-content/uploads/2025/02/sftp-n-1.png)


- 客户端连接到服务器的 22 端口（默认的 SSH 端口）。
- 服务器发送公钥给客户端。
- 客户端验证服务器公钥。
- 客户端和服务器协商加密算法。
- 客户端生成会话密钥，用服务器公钥加密后发送。
- 双方使用会话密钥加密后续通信。


---


### 2. 文件传输


在连接建立后，客户端可以通过 SFTP 传输文件。以下是典型的文件传输流程：


![](https://www.runoob.com/wp-content/uploads/2025/02/sftp-n-2.png)


- **上传文件**：客户端将本地文件上传到服务器。
- **下载文件**：客户端从服务器下载文件到本地。


---


### 3. 连接关闭


在文件传输完成后，客户端可以关闭连接：


![](https://www.runoob.com/wp-content/uploads/2025/02/sftp-n-3.png)


- 客户端请求退出 SFTP 会话。
- 服务器关闭连接。


---


## SFTP 的关键特性


- **加密通信**： - 使用 SSH 的加密通道保护数据传输的安全。
- **身份验证**： - 支持密码认证和公钥认证。
- **文件操作**： - 支持上传、下载、删除、重命名文件等。
- **目录操作**： - 支持列出目录内容、创建目录、删除目录等。
- **跨平台支持**： - 支持多种操作系统（如 Windows、Linux、Mac）。


---


## SFTP 的应用场景


SFTP 广泛应用于以下场景：


- **文件传输**：安全地传输敏感文件。
- **备份和恢复**：将备份文件传输到远程服务器。
- **软件分发**：安全地分发软件和更新。
- **数据交换**：在组织内部或外部交换数据。


---


## SFTP 的安全性


SFTP 通过以下机制提高安全性：


- **加密传输**：防止数据被窃听。
- **身份验证**：通过密码或公钥验证用户身份。
- **数据完整性**：使用哈希算法确保数据未被篡改。


---


## SFTP 的替代方案


在某些场景下，可以使用以下替代方案：


- **FTP**：传统的文件传输协议，但不安全。
- **FTPS**：基于 SSL/TLS 的 FTP，加密传输数据。
- **SCP**：基于 SSH 的文件传输协议，但不支持目录操作。


---


总结来说，SFTP 是一种基于 SSH 的安全文件传输协议，通过加密通信和身份验证机制保护数据传输。它广泛应用于文件传输、备份和恢复等场景，是传输敏感信息的理想选择。如果你对 SFTP 的某个具体特性或应用场景感兴趣，可以进一步探讨！








	  AI 思考中...





			** [RDP 协议](https://www.runoob.com/rdp-protocol.html)
			[UDP 协议](https://www.runoob.com/udp-protocol.html) **













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
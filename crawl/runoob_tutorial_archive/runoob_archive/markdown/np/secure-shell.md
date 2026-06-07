# SSH 协议

- Source: https://www.runoob.com/np/secure-shell.html

SSH（Secure Shell，安全外壳协议）是一种用于安全远程登录和其他网络服务的加密协议。


SSH 通过加密通信来保护数据在传输过程中的安全性，广泛应用于系统管理、文件传输和远程命令执行等场景。


## SSH 的工作原理

SSH 使用客户端-服务器模型，通过加密技术确保通信的安全性。

以下是 SSH 连接建立和数据传输的基本流程：


### 1. 连接建立


![](https://www.runoob.com/wp-content/uploads/2025/02/export_z8jd8.png)


- 客户端连接到服务器的 22 端口（默认的 SSH 端口）。
- 服务器发送自己的公钥给客户端。
- 客户端验证服务器公钥（通常通过已知的主机密钥指纹）。
- 客户端和服务器协商加密算法（如 AES、RSA 等）。
- 客户端生成一个会话密钥，用服务器的公钥加密后发送给服务器。
- 双方使用会话密钥加密后续通信。


---


### 2. 用户认证


SSH 支持多种用户认证方式，常见的有：


- **密码认证**：用户输入用户名和密码。
- **公钥认证**：用户使用私钥进行认证，服务器验证对应的公钥。


**密码认证**


![](https://www.runoob.com/wp-content/uploads/2025/02/export_h704t.png)


- 客户端发送用户名。
- 服务器请求密码。
- 客户端发送加密的密码。
- 服务器验证密码，返回认证结果。


**公钥认证**


![](https://www.runoob.com/wp-content/uploads/2025/02/export_bwnsgb.png)


- 客户端发送用户名和公钥。
- 服务器发送一个随机数。
- 客户端使用私钥对随机数进行签名，发送给服务器。
- 服务器使用公钥验证签名，返回认证结果。


---


### 3. 数据传输


在身份验证成功后，SSH 会建立一个加密的会话通道，支持以下功能：


- 远程登录：在远程服务器上执行命令。
- 文件传输：通过 SCP 或 SFTP 传输文件。
- 端口转发：将本地端口转发到远程服务器，或反之。


---


## SSH 的关键特性


- **加密通信**： - 使用对称加密（如 AES）加密数据。 - 使用非对称加密（如 RSA）交换会话密钥。
- **身份验证**： - 支持密码认证和公钥认证。 - 公钥认证更安全，无需传输密码。
- **数据完整性**： - 使用哈希算法（如 SHA）确保数据未被篡改。
- **多功能性**： - 支持远程登录、文件传输、端口转发等。


---


## SSH 的应用场景


SSH 广泛应用于以下场景：


- **远程管理**：登录到远程服务器执行命令。
- **文件传输**：通过 SCP 或 SFTP 安全地传输文件。
- **端口转发**：将本地服务暴露到远程服务器，或反之。
- **自动化任务**：通过 SSH 脚本执行远程命令。


---


## SSH 的安全性


SSH 的安全性依赖于以下因素：


- **密钥管理**：保护私钥，定期更新公钥。
- **强密码**：使用复杂的密码，避免暴力破解。
- **防火墙**：限制 SSH 端口的访问范围。
- **禁用 root 登录**：减少安全风险。


---


总结来说，SSH 是一种安全的远程登录协议，通过加密通信和多种身份验证方式保护数据传输的安全。它广泛用于远程管理、文件传输和端口转发等场景。如果你对 SSH 的某个具体特性或应用场景感兴趣，可以进一步探讨！









	  AI 思考中...





			** [FTP 协议](https://www.runoob.com/ftp-protocol.html)
			[Telnet 协议](https://www.runoob.com/telnet-protocol.html) **













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
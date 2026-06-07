# HTTPS 协议

- Source: https://www.runoob.com/np/https-protocol.html

HTTPS（HyperText Transfer Protocol Secure，安全超文本传输协议）是 HTTP 的安全版本，通过在 HTTP 和传输层之间加入 TLS/SSL 加密层，保护数据传输的安全性和完整性。

HTTPS 广泛用于保护敏感信息（如登录凭证、支付信息）的传输。


---


## HTTPS 的工作原理


HTTPS 的核心是在 HTTP 的基础上增加了 TLS/SSL 加密层，通过加密和身份验证机制保护数据传输。


### 1. HTTPS 连接建立


![](https://www.runoob.com/wp-content/uploads/2025/02/https-1.png)


- **ClientHello**：客户端发送支持的加密算法列表。
- **ServerHello**：服务器选择加密算法并发送服务器证书。
- **证书验证**：客户端验证服务器证书的有效性。
- **密钥交换**：客户端生成预主密钥，用服务器公钥加密后发送。
- **会话密钥**：双方根据预主密钥生成会话密钥，用于加密后续通信。


---


### 2. HTTP 通信


在加密通道建立后，客户端和服务器通过 HTTPS 进行 HTTP 通信：


![](https://www.runoob.com/wp-content/uploads/2025/02/https-2.png)


- 客户端发送加密的 HTTP 请求。
- 服务器返回加密的 HTTP 响应。


---


## HTTPS 的关键特性


- **加密通信**： - 使用对称加密（如 AES）加密数据。 - 使用非对称加密（如 RSA）交换密钥。
- **身份验证**： - 通过服务器证书验证服务器的身份。 - 可选地通过客户端证书验证客户端的身份。
- **数据完整性**： - 使用哈希算法（如 SHA）确保数据未被篡改。
- **兼容性**： - 与 HTTP 完全兼容，支持相同的请求方法和响应格式。


---


## HTTPS 的应用场景


HTTPS 广泛应用于以下场景：


- **网页浏览**：保护用户隐私和敏感信息。
- **在线支付**：保护支付信息的安全。
- **API 调用**：保护数据传输的机密性和完整性。
- **登录认证**：保护登录凭证的安全。


---


## HTTPS 的安全性


HTTPS 通过以下机制提高安全性：


- **加密传输**：防止数据被窃听。
- **身份验证**：防止服务器被伪装。
- **数据完整性**：防止数据被篡改。


---


## HTTPS 的证书


HTTPS 的安全性依赖于服务器证书，证书由受信任的证书颁发机构（CA）签发，包含以下信息：


- **域名**：证书绑定的域名。
- **公钥**：用于加密通信。
- **有效期**：证书的有效期限。
- **签名**：CA 对证书的签名，用于验证证书的真实性。


---


## HTTPS 的部署


部署 HTTPS 需要以下步骤：


- **获取证书**：从 CA 申请服务器证书。
- **配置服务器**：在服务器上安装证书并启用 HTTPS。
- **重定向 HTTP 到 HTTPS**：确保所有流量通过 HTTPS 传输。


---


## HTTPS 的替代方案


在某些场景下，可以使用以下替代方案：


- **V**N**：通过加密隧道保护数据传输。
- **SSH 隧道**：通过 SSH 加密通信。








	  AI 思考中...





			** [HTTP 协议](http-protocol.html)
			[POP3 协议](https://www.runoob.com/pop3-protocol.html) **













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
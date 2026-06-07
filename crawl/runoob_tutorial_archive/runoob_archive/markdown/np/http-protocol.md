# HTTP 协议

- Source: https://www.runoob.com/np/http-protocol.html

HTTP（HyperText Transfer Protocol，超文本传输协议）是互联网上应用最广泛的协议之一，用于在客户端（如浏览器）和服务器之间传输超文本（如网页）。


HTTP 是万维网（WWW）的基础，支持网页浏览、文件下载、API 调用等应用场景。


---


## HTTP 的工作原理


HTTP 使用客户端-服务器模型，通过请求-响应的方式传输数据。它的核心功能是客户端向服务器发送请求，服务器返回响应。


### 1. HTTP 请求-响应流程


![](https://www.runoob.com/wp-content/uploads/2025/02/http-1.png)


- **客户端**：向服务器发送 HTTP 请求（如 `GET /index.html`）。
- **服务器**：处理请求并返回 HTTP 响应（如 `200 OK` 和网页内容）。


### 2. HTTP 请求结构


HTTP 请求由以下部分组成：


- **请求行**：包括请求方法（如 GET、POST）、请求资源（如 `/index.html`）和协议版本（如 HTTP/1.1）。
- **请求头**：包含附加信息（如 `Host`、`User-Agent`、`Accept`）。
- **请求体**：可选，用于传输数据（如 POST 请求的表单数据）。


示例：


```
GET /index.html HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0
Accept: text/html
```


---


### 3. HTTP 响应结构


HTTP 响应由以下部分组成：


- **状态行**：包括协议版本（如 HTTP/1.1）、状态码（如 200）和状态消息（如 OK）。
- **响应头**：包含附加信息（如 `Content-Type`、`Content-Length`）。
- **响应体**：包含实际数据（如 HTML 内容）。


示例：


```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```


---


## HTTP 的关键特性


- **无状态协议**： - 每次请求都是独立的，服务器不会保存客户端的状态。 - 通过 Cookie 或 Session 实现状态管理。
- **支持多种请求方法**： - **GET**：获取资源。 - **POST**：提交数据。 - **PUT**：更新资源。 - **DELETE**：删除资源。
- **支持多种数据类型**： - 通过 `Content-Type` 头指定数据类型（如 `text/html`、`application/json`）。
- **缓存机制**： - 通过 `Cache-Control` 和 `ETag` 头实现缓存，提高性能。
- **可扩展性**： - 支持自定义请求头和响应头，扩展功能。


---


## HTTP 的应用场景


HTTP 广泛应用于以下场景：


- **网页浏览**：通过浏览器访问网页。
- **API 调用**：通过 RESTful API 传输数据。
- **文件下载**：下载文件或资源。
- **表单提交**：提交用户输入的数据。


---


## HTTP 的安全性问题


HTTP 本身是不安全的，因为它在传输过程中使用明文传输数据，容易受到以下攻击：


- **窃听**：攻击者可以窃听传输的数据。
- **篡改**：攻击者可以篡改传输的数据。
- **伪装**：攻击者可以伪装成服务器或客户端。


为了提高安全性，可以使用 HTTPS（HTTP Secure），即 HTTP over TLS/SSL，通过加密通信保护数据传输。


---


## HTTP 的版本


HTTP 有多个版本，主要区别在于性能和功能：


- **HTTP/1.0**： - 每次请求需要建立新的连接，性能较差。
- **HTTP/1.1**： - 支持持久连接和管道化，性能提升。
- **HTTP/2**： - 支持多路复用、二进制帧和头部压缩，性能显著提升。
- **HTTP/3**： - 基于 QUIC 协议，进一步优化性能和安全性。









	  AI 思考中...





			** [DNS 协议](https://www.runoob.com/dns-protocol.html)
			[HTTPS 协议](https-protocol.html) **













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
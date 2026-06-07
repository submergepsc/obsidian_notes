# HTTP2

- Source: https://www.runoob.com/http/http2-tutorial.html

![](https://static.jyshare.com/images/svg/http2.svg)

HTTP/2（超文本传输协议第2版，最初命名为HTTP 2.0），简称为h2（基于TLS/1.2或以上版本的加密连接）或h2c（非加密连接）， HTTP/2 是 HTTP 协议的第二个主要版本，用于在 Web 服务器和客户端之间传输数据。


HTTP/2 是 HTTP 协议自 1999 年 HTTP 1.1 的改进版 RFC 发布后的首个更新，主要基于 SPDY 协议。


多数主流浏览器已经在 2015 年底支持了该协议。

HTTP/2是一种网络协议，是HTTP/1.1的升级版，由IETF在2015年发布。HTTP/2旨在提高Web性能，减少延迟，增加安全性，使Web应用更加快速、高效和可靠。


![](https://www.runoob.com/wp-content/uploads/2023/03/http-timeline.png)


---

## HTTP/2 特点


下面是 HTTP/2 的一些特点和改进之处：


- 多路复用：HTTP/2 允许同时发送多个请求和响应，而不是像 HTTP/1.1 一样只能一个一个地处理。这样可以减少延迟，提高效率，提高网络吞吐量。
- 二进制传输：HTTP/2 使用二进制协议，与 HTTP/1.1 使用的文本协议不同。二进制协议可以更快地解析，更有效地传输数据，减少了传输过程中的开销和延迟。
- 头部压缩：HTTP/2 使用 HPACK 算法对 HTTP 头部进行压缩，减少了头部传输的数据量，从而减少了网络延迟。
- 服务器推送：HTTP/2 支持服务器推送，允许服务器在客户端请求之前推送资源，以提高性能。
- 改进的安全性：HTTP/2 默认使用 TLS（Transport Layer Security）加密传输数据，提高了安全性。
- 兼容 HTTP/1.1：HTTP/2 可以与 HTTP/1.1 共存，服务器可以同时支持 HTTP/1.1 和 HTTP/2。如果客户端不支持 HTTP/2，服务器可以回退到 HTTP/1.1。


总的来说，HTTP/2在性能、安全性和可用性方面都有显著的改进，可以使 Web 应用更加快速、高效和可靠。


对数据传输采用多路复用，让多个请求合并在同一 TCP 连接内，如下图所示：


![](https://www.runoob.com/wp-content/uploads/2023/03/6149cbd7fd4bdd7c82f55cc6_http1-vs-http2.png)


HTTP/2 减少网络延迟，提高浏览器的页面加载速度：


![](https://www.runoob.com/wp-content/uploads/2023/03/6149cc3eca0fb2c370604259_http1-vs-http2-responce-time.png)


HTTP/2 使用二进制格式来传输数据，而不是像 HTTP/1.1 一样使用文本格式。这提高了效率并降低了数据传输的延迟。


![](https://www.runoob.com/wp-content/uploads/2023/03/http2-binaryprotocol_lyaaiq.png)


HTTP/2 使用头部压缩来减少传输数据的大小。这有助于减少网络带宽的使用量，并提高页面加载速度。


![](https://www.runoob.com/wp-content/uploads/2023/03/133_0.jpeg)


HTTP/2 允许服务器在不被请求的情况下主动向客户端发送数据。这有助于减少请求延迟，并提高页面加载速度。


![](https://www.runoob.com/wp-content/uploads/2023/03/http2-push.png)








	  AI 思考中...





			** [MIME 类型](https://www.runoob.com/mime-types.html)
			[SSL 免费证书申请 – Certbot](https://www.runoob.com/ssl-certbot.html) **













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
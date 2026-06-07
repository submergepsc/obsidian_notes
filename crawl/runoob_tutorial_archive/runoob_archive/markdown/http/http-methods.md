# HTTP 请求方法

- Source: https://www.runoob.com/http/http-methods.html

HTTP 请求方法定义了客户端和服务器之间的通信方式。


根据 HTTP 标准，HTTP 请求可以使用多种请求方法。


以下是常见的 HTTP 请求方法列表：


| 序号 | 方法 | 描述 |
| --- | --- | --- |
| 1 | GET | 从服务器获取资源。用于请求数据而不对数据进行更改。例如，从服务器获取网页、图片等。 |
| 2 | POST | 向服务器发送数据以创建新资源。常用于提交表单数据或上传文件。发送的数据包含在请求体中。 |
| 3 | PUT | 向服务器发送数据以更新现有资源。如果资源不存在，则创建新的资源。与 POST 不同，PUT 通常是幂等的，即多次执行相同的 PUT 请求不会产生不同的结果。 |
| 4 | DELETE | 从服务器删除指定的资源。请求中包含要删除的资源标识符。 |
| 5 | PATCH | 对资源进行部分修改。与 PUT 类似，但 PATCH 只更改部分数据而不是替换整个资源。 |
| 6 | HEAD | 类似于 GET，但服务器只返回响应的头部，不返回实际数据。用于检查资源的元数据（例如，检查资源是否存在，查看响应的头部信息）。 |
| 7 | OPTIONS | 返回服务器支持的 HTTP 方法。用于检查服务器支持哪些请求方法，通常用于跨域资源共享（CORS）的预检请求。 |
| 8 | TRACE | 回显服务器收到的请求，主要用于诊断。客户端可以查看请求在服务器中的处理路径。 |
| 9 | CONNECT | 建立一个到服务器的隧道，通常用于 HTTPS 连接。客户端可以通过该隧道发送加密的数据。 |


## 各个版本定义的请求方法


### HTTP/1.0


HTTP/1.0 定义了以下三种请求方法：


- **GET** - 请求指定的资源。
- **POST** - 提交数据以处理请求。
- **HEAD** - 请求资源的响应头信息。


### HTTP/1.1


HTTP/1.1 引入了更多的方法：


- **GET** - 请求指定的资源。
- **POST** - 提交数据以处理请求。
- **HEAD** - 请求资源的响应头信息。
- **PUT** - 上传文件或者更新资源。
- **DELETE** - 删除指定的资源。
- **OPTIONS** - 请求获取服务器支持的请求方法。
- **TRACE** - 回显服务器收到的请求，主要用于诊断。
- **CONNECT** - 建立一个隧道用于代理服务器的通信，通常用于 HTTPS。


### HTTP/2


HTTP/2 基本上沿用了 HTTP/1.1 的方法，但对协议进行了优化，提高了传输效率和速度。HTTP/2 也引入了新的特性，如多路复用、头部压缩和服务器推送等。


### HTTP/3


HTTP/3 基于 QUIC 协议实现，继续使用 HTTP/2 的方法。HTTP/3 主要改进了传输层，使用 UDP 代替 TCP 以提高传输速度和可靠性。








	  AI 思考中...





			** [HTTP 消息结构](http-messages.html)
			[HTTP 响应头信息](http-header-fields.html) **













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
# SOAP HTTP 协议

- Source: https://www.runoob.com/soap/soap-httpbinding.html

---


## HTTP 协议


HTTP 在 TCP/IP 之上进行通信。HTTP 客户机使用 TCP 连接到 HTTP 服务器。在建立连接之后，客户机可向服务器发送 HTTP 请求消息：


```
POST /item HTTP/1.1
Host: 189.123.255.239
Content-Type: text/plain
Content-Length: 200
```


随后服务器会处理此请求，然后向客户机发送一个 HTTP 响应。此响应包含了可指示请求状态的状态代码：


```
200 OK
Content-Type: text/plain
Content-Length: 200
```


在上面的例子中，服务器返回了一个 200 的状态代码。这是 HTTP 的标准成功代码。


假如服务器无法对请求进行解码，它可能会返回类似这样的信息：


```
400 Bad Request
Content-Length: 0
```


**
---


## SOAP HTTP Binding


SOAP 方法指的是遵守 SOAP 编码规则的 HTTP 请求/响应。


### HTTP + XML = SOAP


SOAP 请求可能是 HTTP POST 或 HTTP GET 请求。


HTTP POST 请求规定至少两个 HTTP 头：Content-Type 和 Content-Length。


---


## Content-Type


SOAP 的请求和响应的 Content-Type 头可定义消息的 MIME 类型，以及用于请求或响应的 XML 主体的字符编码（可选）。


### 语法


```
Content-Type: MIMEType; charset=character-encoding
```


### 实例


```
POST /item HTTP/1.1
Content-Type: application/soap+xml; charset=utf-8
```


---


## Content-Length


SOAP 的请求和响应的 Content-Length 头规定请求或响应主体的字节数。


### 语法


```
Content-Length: bytes
```


### 实例


```
POST /item HTTP/1.1
Content-Type: application/soap+xml; charset=utf-8
Content-Length: 250
```









	  AI 思考中...





			** [SOAP Fault 元素](https://www.runoob.com/soap-fault.html)
			[SOAP 实例](https://www.runoob.com/soap-example.html) **













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
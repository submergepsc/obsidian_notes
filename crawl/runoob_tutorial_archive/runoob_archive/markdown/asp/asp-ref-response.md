# ASP Response 对象

- Source: https://www.runoob.com/asp/asp-ref-response.html

---


ASP Response 对象用于从服务器向用户发送输出的结果。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[使用 ASP 写文本](https://www.runoob.com/try/showasp.php?filename=demo_text)** 本例演示如何使用 ASP 来写文本。


[在 ASP 中使用 HTML 标签格式化文本](https://www.runoob.com/try/showasp.php?filename=demo_formatting) 本例演示如何使用 ASP 将文本和 HTML 标签结合起来。


[将用户重定向至一个不同的 URL](https://www.runoob.com/try/showasp.php?filename=demo_redirect) 本例演示如何将用户重定向至一个不同的 URL。


[显示随机的链接](https://www.runoob.com/try/showasp.php?filename=demo_randomlink) 本例演示如何创建一个随机的链接。


[控制缓冲区](https://www.runoob.com/try/showasp.php?filename=demo_buffer) 本例演示如何控制缓冲区。


[清空缓冲区](https://www.runoob.com/try/showasp.php?filename=demo_bufferclear) 本例演示如何清空缓冲区。


[在处理过程中终止脚本并返回结果](https://www.runoob.com/try/showasp.php?filename=demo_end) 本例演示如何在处理过程中终止脚本。


[设置页面在失效前在浏览器中缓存时间](https://www.runoob.com/try/showasp.php?filename=demo_expires) 本例演示如何规定页面在失效前在浏览器中的缓存时间。


[设置页面缓存在浏览器中的失效日期或时间](https://www.runoob.com/try/showasp.php?filename=demo_expiresabs) 本例演示如何规定页面缓存在浏览器中的失效时间日期或时间。


[检查用户是否仍然与服务器连接](https://www.runoob.com/try/showasp.php?filename=demo_isclientconnected) 本例演示如何检查用户是否已与服务器断开。


[设置内容类型](https://www.runoob.com/try/showasp.php?filename=demo_contenttype) 本例演示如何规定内容的类型。


[设置字符集名称](https://www.runoob.com/try/showasp.php?filename=demo_charset) 本例演示如何规定字符集的名称。


---


## Response 对象


ASP Response 对象用于从服务器向用户发送输出的结果。它的集合、属性和方法描述如下：


### 集合


| 集合 | 描述 |
| --- | --- |
| Cookies | 设置 cookie 的值。如果 cookie 不存在，则创建 cookie ，并设置指定的值。 |


### 属性


| 属性 | 描述 |
| --- | --- |
| Buffer | 规定是否缓冲页面的输出。 |
| CacheControl | 设置代理服务器是否可以缓存由 ASP 产生的输出。 |
| Charset | 将字符集的名称追加到 Response 对象中的 content-type 报头。 |
| ContentType | 设置 Response 对象的 HTTP 内容类型。 |
| Expires | 设置页面在失效前的浏览器缓存时间（分钟）。 |
| ExpiresAbsolute | 设置浏览器上页面缓存失效的日期和时间。 |
| IsClientConnected | 指示客户端是否已从服务器断开。 |
| Pics | 向 response 报头的 PICS 标签追加值。 |
| Status | 规定由服务器返回的状态行的值。 |


### 方法


| 方法 | 描述 |
| --- | --- |
| AddHeader | 向 HTTP 响应添加新的 HTTP 报头和值。 |
| AppendToLog | 向服务器日志条目的末端添加字符串。 |
| BinaryWrite | 在没有任何字符转换的情况下直接向输出写数据。 |
| Clear | 清除已缓冲的 HTML 输出。 |
| End | 停止处理脚本，并返回当前的结果。 |
| Flush | 立即发送已缓冲的 HTML 输出。 |
| Redirect | 把用户重定向到一个不同的 URL。 |
| Write | 向输出写指定的字符串。 |








	  AI 思考中...





			** [ASP 使用 CDOSYS 发送电子邮件](https://www.runoob.com/asp-send-email.html)
			[ASP Request 对象](https://www.runoob.com/asp-ref-request.html) **













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
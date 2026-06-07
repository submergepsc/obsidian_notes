# ASP Buffer 属性

- Source: https://www.runoob.com/asp/prop-buffer.html

---

[![Response 对象参考手册](https://www.runoob.com/images/up.gif) 完整的 Response 对象参考手册](https://www.runoob.com/asp-ref-response.html)

---


Buffer 属性可规定是否对输出进行缓冲。通常情况下，ASP 脚本在服务器端执行，每句的执行结果都会发送到客户端的浏览器上显示出来。当输出设置缓存时，服务器会阻止向浏览器的响应，直到所有的服务器脚本均被处理，或者直到脚本调用了 Flush 或 End 方法。


**注意：**如果要设置此属性，它应当位于 .asp 文件中的  标签之前。


## 语法


response.Buffer[=flag]


**
| 参数 | 描述 |
| --- | --- |
| flag | 布尔值，规定是否缓冲页面输出。 False 指示不缓存，服务器会一边处理一边发送输出。IIS version 4.0 默认为 False，而 IIS version 5.0 及更高的版本默认为 True。 True 指示缓冲。服务器不会发送输出，直到页面上的所有脚本被处理，或者直到 Flush 或 End 方法被调用。 |


## 实例


### 实例 1


在这个实例中，在循环结束前不会被浏览器发送输出。如果 buffer 被设置为 False ，则每循环一次就向浏览器输出一行。


<%response.Buffer=true%>

<html>

<body>

<%

for i=1 to 100

  response.write(i & "<br>")

next

%>

</body>

</html>


### 实例 2


<%response.Buffer=true%>

<html>

<body>

<p>I write some text, but I will control when

the text will be sent to the browser.</p>

<p>The text is not sent yet. I hold it back!</p>

<p>OK, let it go!</p>

<%response.Flush%>

</body>

</html>


### 实例 3


<%response.Buffer=true%>

<html>

<body>

<p>This is some text I want to send to the user.</p>

<p>No, I changed my mind. I want to clear the text.</p>

<%response.Clear%>

</body>

</html>


---

[![Response 对象参考手册](https://www.runoob.com/images/up.gif) 完整的 Response 对象参考手册](https://www.runoob.com/asp-ref-response.html)







	  AI 思考中...





			** [ASP Cookies 集合](https://www.runoob.com/coll-cookies-response.html)
			[ASP CacheControl 属性](https://www.runoob.com/prop-cachecontrol.html) **













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
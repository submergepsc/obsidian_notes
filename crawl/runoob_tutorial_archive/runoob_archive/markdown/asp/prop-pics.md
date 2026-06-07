# ASP PICS 属性

- Source: https://www.runoob.com/asp/prop-pics.html

---

[![Response 对象参考手册](https://www.runoob.com/images/up.gif) 完整的 Response 对象参考手册](https://www.runoob.com/asp-ref-response.html)

---


PICS 属性可向响应头部的 PICS 标记追加值。


**注意：**此属性可接受任何字符串值，无论是否是合法的 PICS 标记。


### 什么是 PICS ？


PICS（Platform for Internet Content Selection）分级系统用于对网站内的内容进行分级。它看起来类似这样：


PICS-1.1 "http://www.rsac.org/ratingsv01.html" by "[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)" for "http://www.somesite.com" on "2002.10.05T02:15-0800" r (n 0 s 0 v 0 l 0)


| 部分 | 描述 |
| --- | --- |
| PICS-1.1 | PICS 版本号 |
| "http://www.rsac.org/ratingsv01.html" | 分级机构 |
| by "[email protected]" | 标签的作者 |
| for "http://www.somesite.com" | 已被分级的文档的 URL |
| on "2002.10.05T02:15-0800" | 失效日期 |
| r (n 0 s 0 v 0 l 0) | 等级 |


最流行的分级系统之一是 RSACi（Recreational Software Advisory Council on the Internet）。RSACi 使用四种类型：violence（暴力）、nudity（裸体）、sex（性）以及 language（不雅言论）。数字从 0 到 4分别分配给了这四种类型。0 表示页面不包含任何攻击性的内容，4 表示潜在攻击性内容的最高级别。


| 级别 | 暴力分级 | 裸体分级 | 性分级 | 言论分级 |
| --- | --- | --- | --- | --- |
| 0 | None of the below or sports related | None of the below | None of the below or innocent kissing; romance | None of the below |
| 1 | Injury to human being | Revealing attire | Passionate kissing | Mild expletives |
| 2 | Destruction of realistic objects | Partial nudity | Clothed sexual touching | Moderate expletives or profanity |
| 3 | Aggressive violence or death to humans | Frontal nudity | Non-explicit sexual acts | Strong language or hate speech |
| 4 | Rape or wanton, gratuitous violence | Frontal nudity (qualifying as provocative display) | Explicit sexual acts or sex crimes | Crude, vulgar language or extreme hate speech |


您有两种方式为您的网站获得评级。您可以自己为网站评级，或者利用一个评级提供者，比如 RSACi 。他们会要求您填写一些问题。在填写完成后，您会得到用于您的网站的分级标签。


Microsoft IE 3.0 及更高的版本和 Netscape 4.5 及更高的版本均支持内容分级。您可以在 IE 5 中设置分级，选择工具菜单中的 Internet 选项。选择内容选项卡，然后单击启用。当等级超过了所定义的级别，内容顾问就会阻止此网站。在 Netscape 4.7 中，您可以通过选择 Help 和 NetWatch 来设置分级。


我们可以使用 META 标签或者 response.PICS 属性为网站添加分级。


### 语法


response.PICS(picslabel)


**
| 参数 | 描述 |
| --- | --- |
| picslabel | 格式正确的 PICS 标签。 |


### 实例

ASP 文件包含以下代码：

注意：**由于 PICS 标签含有引号，您必须把引号替换为 " & chr(34) & ".


<%**
response.PICS("(PICS-1.1 <http://www.rsac.org/ratingv01.html>

by " & chr(34) & "[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)" & chr(34) &

" for " & chr(34) & "http://www.somesite.com" & chr(34) &

" on " & chr(34) & "2002.10.05T02:15-0800" & chr(34) &

" r (n 2 s 0 v 1 l 2))")

%>


被添加的头部：


PICS-label:(PICS-1.1 <http://www.rsac.org/ratingv01.html>

by "[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)"

for "http://www.somesite.com"

on "2002.10.05T02:15-0800"

r (n 2 s 0 v 1 l 2))


---

[![Response 对象参考手册](https://www.runoob.com/images/up.gif) 完整的 Response 对象参考手册](https://www.runoob.com/asp-ref-response.html)







	  AI 思考中...





			** [ASP IsClientConnected 属性](https://www.runoob.com/prop-isclientconnected.html)
			[ASP Status 属性](https://www.runoob.com/prop-status.html) **













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
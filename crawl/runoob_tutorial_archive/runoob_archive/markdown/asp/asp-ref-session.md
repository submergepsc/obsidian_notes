# ASP Session 对象

- Source: https://www.runoob.com/asp/asp-ref-session.html

---


Session 对象用于存储关于用户会话（session）的信息，或者更改用户会话（session）的设置。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[设置并返回 LCID](https://www.runoob.com/try/showasp.php?filename=demo_lcid)** 本例演示 "LCID" 属性。该属性设置并返回一个指示位置或者地区的整数。类似于日期、时间和货币等内容都要根据位置或者地区来显示。


[返回 SessionID](https://www.runoob.com/try/showasp.php?filename=demo_sessionid) 本例演示 "SessionID" 属性。该属性为每位用户返回一个唯一的 id。这个 id 由服务器生成。


[session 的超时](https://www.runoob.com/try/showasp.php?filename=demo_gettimeout) 本例演示 "Timeout" 属性。该属性设置并返回 session 的超时时间（分钟）。


---


## Session 对象


当您在计算机上操作某个应用程序时，您打开它，做些更改，然后关闭它。这很像一次对话（Session）。计算机知道您是谁。它清楚您在何时打开和关闭应用程序。然而，在因特网上问题出现了：由于 HTTP 地址无法保持状态，Web 服务器并不知道您是谁以及您做了什么。


ASP 通过为每个用户创建一个唯一的 cookie 来解决这个问题。cookie 被传送至用户的计算机上，它含有可识别用户的信息。这种接口被称作 Session 对象。


Session 对象用于存储关于用户会话（session）的信息，或者更改用户会话（session）的设置。


存储于 Session 对象中的变量存储单一用户的信息，并且对于应用程序中的所有页面都是可用的。存储于 session 变量中的公共信息通常是 name、id 和参数。服务器会为每个新的用户创建一个新的 Session，并在 session 失效时撤销掉这个 Session 对象。


Session 对象的集合、属性、方法和事件的描述如下：


### 集合


| 集合 | 描述 |
| --- | --- |
| Contents | 包含所有通过脚本命令追加到 session 的条目。 |
| StaticObjects | 包含了所有使用 HTML 的 标签追加到 session 的对象。 |


### 属性


| 属性 | 描述 |
| --- | --- |
| CodePage | 规定显示动态内容时使用的字符集。 |
| LCID | 设置或返回指定位置或者地区的一个整数。诸如日期、时间好以及货币的内容会根据位置或者地区来显示。 |
| SessionID | 为每个用户返回一个唯一的 id。此 id 由服务器生成。 |
| Timeout | 设置或返回应用程序中的 Session 对象的超时时间（分钟）。 |


### 方法


| 方法 | 描述 |
| --- | --- |
| Abandon | 撤销一个用户的 session。 |
| Contents.Remove | 从 Contents 集合删除一个项目。 |
| Contents.RemoveAll() | 从 Contents 集合删除所有项目。 |


### 事件


| 事件 | 描述 |
| --- | --- |
| Session_OnEnd | 当一个会话结束时此事件发生。 |
| Session_OnStart | 当一个会话开始时此事件发生。 |










	  AI 思考中...





			** [ASP Application 对象](https://www.runoob.com/asp-ref-application.html)
			[ASP Server 对象](https://www.runoob.com/asp-ref-server.html) **













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
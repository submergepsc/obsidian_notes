# ASP Application 对象

- Source: https://www.runoob.com/asp/asp-ref-application.html

---


在一起协同工作以完成某项任务的一组 ASP 文件称为一个应用程序。Application 对象用于把这些文件捆绑在一起。


---


## Application 对象


Web 上的一个应用程序可以是一组 ASP 文件。这些 ASP 文件一起协同工作来完成某项任务。Application 对象用于把这些文件捆绑在一起。


Application 对象用于存储和访问来自任何页面的变量，类似于 Session 对象。不同之处在于，所有的用户分享一个 Application 对象，而 Session 对象和用户的关系是一一对应的。


Application 对象存有会被应用程序中的许多页面使用的信息（比如数据库连接信息）。可以从任何的页面访问这些信息。同时您也可以在一个地方改变这些信息，随后这些改变会自动反映在所有的页面上。


Application 对象的集合、方法和事件的描述如下：


### 集合


| 集合 | 描述 |
| --- | --- |
| Contents | 包含所有通过脚本命令追加到应用程序中的项目。 |
| StaticObjects | 包含所有使用 HTML 的 标签追加到应用程序中的对象。 |


### 方法


| 方法 | 描述 |
| --- | --- |
| Contents.Remove | 从 Contents 集合中删除一个项目。 |
| Contents.RemoveAll() | 从 Contents 集合中删除所有的项目。 |
| Lock | 防止其他的用户修改 Application 对象中的变量。 |
| Unlock | 使其他的用户可以修改 Application 对象中的变量（在被 Lock 方法锁定之后）。 |


### 事件


| 事件 | 描述 |
| --- | --- |
| Application_OnEnd | 当所有用户的 session 都结束，并且应用程序结束时，此事件发生。 |
| Application_OnStart | 在第一个新的 session 被创建之前（即 Application 对象第一次被引用时），此事件会发生。 |

**







	  AI 思考中...





			** [ASP Request 对象](https://www.runoob.com/asp-ref-request.html)
			[ASP Session 对象](https://www.runoob.com/asp-ref-session.html) **













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
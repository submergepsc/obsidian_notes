# ASP ASPError 对象

- Source: https://www.runoob.com/asp/asp-ref-error.html

---


ASPError 对象用于显示在 ASP 文件的脚本中发生的错误信息。


---


## ASPError 对象


ASPError 对象在 ASP 3.0 中生效，且在 IIS5 及更高版本中可用。


ASPError 对象用于显示在 ASP 文件的脚本中发生的任何错误的详细信息。


**注释：**当 Server.GetLastError 被调用时，ASPError 对象就会被创建，因此只能通过使用 Server.GetLastError 方法来访问错误信息。


ASPError 对象的属性描述如下（所有属性都是可读的）：


### 属性


| 属性 | 描述 |
| --- | --- |
| ASPCode | 返回由 IIS 生成的错误代码。 |
| ASPDescription | 返回错误的详细信息（如果错误和 ASP 相关）。 |
| Category | 返回错误来源。(错误是由 ASP、脚本语言还是对象引起的？） |
| Column | 返回在出错文件中的列位置。 |
| Description | 返回关于错误的简短描述。 |
| File | 返回出错 ASP 文件的名称。 |
| Line | 返回错误所在的行数。 |
| Number | 返回关于错误的标准 COM 错误代码。 |
| Source | 返回错误所在行的实际的源代码。 |

**







	  AI 思考中...





			** [ASP Server 对象](https://www.runoob.com/asp-ref-server.html)
			[ASP FileSystem 对象](https://www.runoob.com/asp-ref-filesystem.html) **













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
# ASP AddHeader 方法

- Source: https://www.runoob.com/asp/met-addheader.html

---

[![Response 对象参考手册](https://www.runoob.com/images/up.gif) 完整的 Response 对象参考手册](https://www.runoob.com/asp-ref-response.html)

---


AddHeader 方法向 HTTP 响应添加一个新的 HTTP 头部和值。


**注意：**一旦头部被添加，就无法删除。


**注意：**在 IIS 4.0 中，您调用此方法需要在任何的输出送往浏览器之前。在 IIS 5.0 中，您可以在脚本中的任何点调用 AddHeader 方法，只要它先于对 response.Flush 方法的调用。


### 语法


response.AddHeader name,value


**
| 参数 | 描述 |
| --- | --- |
| name | 必需。新头部变量的名称（不能包含下划线）。 |
| value | 必需。新头部变量的初始值。 |


---


### 实例


<%Response.AddHeader "WARNING","Error message text"%>


---

[![Response 对象参考手册](https://www.runoob.com/images/up.gif) 完整的 Response 对象参考手册](https://www.runoob.com/asp-ref-response.html)







	  AI 思考中...





			** [ASP Status 属性](https://www.runoob.com/prop-status.html)
			[ASP AppendToLog 方法](https://www.runoob.com/met-appendtolog.html) **













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
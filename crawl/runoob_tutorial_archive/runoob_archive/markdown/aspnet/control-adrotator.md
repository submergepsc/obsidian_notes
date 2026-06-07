# ASP.NET AdRotator 控件

- Source: https://www.runoob.com/aspnet/control-adrotator.html

---

[![Web Server Controls](https://www.runoob.com/images/up.gif) Web 服务器控件](https://www.runoob.com/aspnet-ref-webcontrols.html)

---


## 定义和用法


AdRotator 控件用于显示图像序列。


该控件使用 XML 文件来存储 ad 信息。XML 文件使用  开始和结束。在  标签内部，应该有若干个定义每条 ad 的  标签。


 标签中预定义的元素被列在下面：


| 元素 | 描述 |
| --- | --- |
|  | 可选。图像文件的路径。 |
|  | 可选。用户点击该 ad 时所链接的 URL。 |
|  | 可选。图像的可选文本。 |
|  | 可选。ad 的类别。 |
|  | 可选。显示概率。 |

**
---


## 属性


| 属性 | 描述 | .NET |
| --- | --- | --- |
| AdvertisementFile | 包含 ad 信息的 XML 文件的路径。 | 1.0 |
| AlternateTextField | 代替广告的 Alt 文本而使用的数据字段。 | 2.0 |
| ImageUrlField | 代替广告的 ImageURL 属性而使用的数据字段。 | 2.0 |
| KeywordFilter | 根据类别对广告进行过滤。 | 1.0 |
| NavigateUrlField | 代替广告的 NavigateUrl 属性而使用的数据字段。 | 2.0 |
| runat | 规定该控件是服务器控件。必须设置为 "server"。 | 1.0 |
| Target | 规定在何处打开 URL。 | 1.0 |


## Web 控件标准属性


AccessKey, Attributes, BackColor, BorderColor, BorderStyle, BorderWidth, CssClass, Enabled, Font, EnableTheming,
ForeColor, Height, IsEnabled, SkinID, Style, TabIndex, ToolTip, Width

如需完整描述，请访问 [Web 控件标准属性](https://www.runoob.com/prop-webcontrol-standard.html)。


## 控件标准属性


AppRelativeTemplateSourceDirectory, BindingContainer, ClientID, Controls, EnableTheming, EnableViewState, ID, NamingContainer,
Page, Parent, Site, TemplateControl, TemplateSourceDirectory, UniqueID, Visible

如需完整描述，请访问 [控件标准属性](https://www.runoob.com/prop-control-standard.html)。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[AdRotator](https://www.runoob.com/try/showaspx.php?filename=demo_adrotator) 在本例中，我们在 .aspx 文件中声明了一个 AdRotator 控件。然后我们在 .aspx 文件中为 AdCreated 事件创建了一个事件句柄，来覆盖 XML 文件中 NavigateUrl 元素的值。


---

[![Web Server Controls](https://www.runoob.com/images/up.gif) Web 服务器控件](https://www.runoob.com/aspnet-ref-webcontrols.html)







	  AI 思考中...





			** [ASP.NET HTML 服务器控件](https://www.runoob.com/aspnet-ref-htmlcontrols.html)
			[ASP.NET Button 控件](https://www.runoob.com/control-button.html) **













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
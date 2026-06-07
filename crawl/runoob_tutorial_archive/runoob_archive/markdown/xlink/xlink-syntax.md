# XLink 和 XPointer 语法

- Source: https://www.runoob.com/xlink/xlink-syntax.html

---


## XLink 语法


在 HTML 中，我们知道  元素可定义超级链接。不过 XML 不是这样工作的。在 XML 文档中，您可以使用任何你需要的名称 - 因此对于浏览器来说是无法预知在 XML 文档中可调用何种超级链接元素。


在 XML 文档中定义超级链接的方法是在元素上放置可用作超级链接的标记。


下面是在 XML 文档中使用 XLink 来创建链接的简单实例：


<?xml version="1.0"?>**

<homepages xmlns:xlink="http://www.w3.org/1999/xlink">


  <homepage xlink:type="simple"

  xlink:href="http://www.runoob.com">Visit Runoob</homepage>


  <homepage xlink:type="simple"

  xlink:href="http://www.w3.org">Visit W3C</homepage>


</homepages>


为了访问 XLink 的属性和特性，我们必须在文档的顶端声明 XLink 命名空间。


XLink 的命名空间是："http://www.w3.org/1999/xlink"。


 元素中的 xlink:type 和 xlink:href 属性定义了来自 XLink 命名空间的 type 和 href 属性。


xlink:type="simple" 可创建一个简单的两端链接（意思是"从这里到哪里"）。稍后我们会研究多端链接（多方向）。


---


## XPointer 语法


在 HTML 中，我们可创建一个既指向某个 HTML 页面又指向 HTML 页面内某个书签的超级链接（使用#）。


有时，可指向更多具体的内容会更有好处。举例，我们需要指向某个特定的列表的第三个项目，或者指向第五段的第二行。通过 XPointer 是很容易做到的。


假如超级链接指向某个 XML 文档，我们可以在 xlink:href 属性中把 XPointer 部分添加到 URL 后面，这样就可以导航（通过 XPath 表达式）到文档中某个具体的位置了。


举例，在下面的例子中，我们通过唯一的 id "rock" 使用 XPointer 指向某个列表中的第五个项目。


href="http://www.example.com/cdlist.xml#id('rock').child(5,item)"








	  AI 思考中...





			** [XLink 和 XPointer 简介](https://www.runoob.com/xlink-intro.html)
			[XLink 实例](https://www.runoob.com/xlink-example.html) **













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
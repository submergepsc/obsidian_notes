# XLink 实例

- Source: https://www.runoob.com/xlink/xlink-example.html

---


让我们通过研究一个实例来学习一些基础的 XLink 语法。


---


## XML 实例文档


请看下面的 XML 文档，"bookstore.xml"，它用来呈现书籍：


<?xml version="1.0" encoding="ISO-8859-1"?>**

<bookstore xmlns:xlink="http://www.w3.org/1999/xlink">


<book title="Harry Potter">


  <description


  xlink:type="simple"


  xlink:href="http://book.com/images/HPotter.gif"


  xlink:show="new">


  As his fifth year at Hogwarts School of Witchcraft and


  Wizardry approaches, 15-year-old Harry Potter is.......


  </description>

</book>


<book title="XQuery Kick Start">


  <description


  xlink:type="simple"


  xlink:href="http://book.com/images/XQuery.gif"


  xlink:show="new">


  XQuery Kick Start delivers a concise introduction


  to the XQuery standard.......


  </description>

</book>


</bookstore>


在您的浏览器查看 "bookstore.xml" [bookstore.xml](https://www.runoob.com/try/xml/bookstore.xml)文件。


在上面的例子中，XLink 文档命名空间(xmlns:xlink="http://www.w3.org/1999/xlink")被声明于文档的顶部。 这意味着文档可访问 XLink 的属性和特性。


xlink:type="simple" 可创建简单的类似 HTML 的链接。您也可以规定更多的复杂的链接（多方向链接），但是目前，我们仅使用简易链接。


xlink:href 属性规定了要链接的 URL，而 xlink:show 属性规定了在何处打开链接。xlink:show="new" 意味着链接（在此例中，是一幅图像）会在新窗口打开。


---


## XLink - 深入学习


在上面的例子中，我们只展示了简单的链接。当我们要访问远程位置的资源，而不是独立的页面时，XLink是变得更有趣。在上面的例子元素集的XLINK属性显示的值为："new"。这意味着，应该在新窗口打开链接。我们可以设置XLINK中的值：显示属性"embed"。这意味着资源应嵌入到页面处理。你认为这可能是另一个XML文档，而不是只是一个图像，你可以建立一个XML文档中层次结构的例子。


使用XLink，你还可以指定资源时才显示。这是由XLink的actuate属性处理。XLINK：actuate"="onLoad"指定的资源文件应加载和显示。XLINK：actuate="onRequest"意味着链接被点击之前无法读取或显示资源。这对低带宽设置非常方便。









	  AI 思考中...





			** [XLink 和 XPointer 语法](https://www.runoob.com/xlink-syntax.html)
			[XPointer 实例](https://www.runoob.com/xpointer-example.html) **













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
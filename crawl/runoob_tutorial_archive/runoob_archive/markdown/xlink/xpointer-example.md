# XPointer 实例

- Source: https://www.runoob.com/xlink/xpointer-example.html

---


让我们通过研究一个实例来学习一些基础的 XPointer 语法。


---


## XPointer 实例


在本例中，我们会为您展示如何使用 XPointer 并结合 XLink 来指向另外一个文档的某个具体的部分。


我们将通过研究目标 XML 文档开始（即我们要链接的那个文档）。


---


## 目标XML文档


目标XML文档名为 "dogbreeds.xml"，它列出了一些不同的狗种类：


<?xml version="1.0" encoding="ISO-8859-1"?>**

<dogbreeds>


<dog breed="Rottweiler" id="Rottweiler">


  <picture url="http://dog.com/rottweiler.gif" />


  <history>The Rottweiler's ancestors were probably Roman


  drover dogs.....</history>


  <temperament>Confident, bold, alert and imposing, the Rottweiler


  is a popular choice for its ability to protect....</temperament>

</dog>


<dog breed="FCRetriever" id="FCRetriever">


  <picture url="http://dog.com/fcretriever.gif" />


  <history>One of the earliest uses of retrieving dogs was to


  help fishermen retrieve fish from the water....</history>


  <temperament>The flat-coated retriever is a sweet, exuberant,


  lively dog that loves to play and retrieve....</temperament>

</dog>


</dogbreeds>


在您的浏览器查看 ["dogbreeds.xml" 文件](https://www.runoob.com/try/xml/dogbreeds.xml)。


注意上面的 XML 文档在每个我们需要链接的元素上使用了 id 属性！**


---


## XML 链接文档


不止能够链接到整个文档（当使用 XLink 时），XPointer 允许您链接到文档的特定部分。如需链接到页面的某个具体的部分，请在 xlink:href 属性中的 URL 后添加一个井号 (#) 以及一个 XPointer 表达式。


表达式：*#xpointer(id("Rottweiler"))* 可引用目标文档中 id 值为 "Rottweiler" 的元素。


因此，xlink:href 属性会类似这样：*xlink:href="http://dog.com/dogbreeds.xml#xpointer(id('Rottweiler'))"*


不过，当使用 id 链接到某个元素时，XPointer 允许简写形式。您可以直接使用 id 的值，就像这样：*xlink:href="http://dog.com/dogbreeds.xml#Rottweiler"*。


下面的 XML 文档可引用每条狗的品种信息，均通过 XLink 和 XPointer 来引用：


<?xml version="1.0" encoding="ISO-8859-1"?>**

<mydogs xmlns:xlink="http://www.w3.org/1999/xlink">


<mydog xlink:type="simple"


  xlink:href="http://dog.com/dogbreeds.xml#Rottweiler">


  <description xlink:type="simple"


  xlink:href="http://myweb.com/mydogs/anton.gif">


  Anton is my favorite dog. He has won a lot of.....


  </description>

</mydog>


<mydog xlink:type="simple"


  xlink:href="http://dog.com/dogbreeds.xml#FCRetriever">


  <description xlink:type="simple"


  xlink:href="http://myweb.com/mydogs/pluto.gif">


  Pluto is the sweetest dog on earth......


  </description>

</mydog>


</mydogs>








	  AI 思考中...





			** [XLink 实例](https://www.runoob.com/xlink-example.html)
			[XLink 总结](https://www.runoob.com/xlink-summary.html) **













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
# DTD 简介

- Source: https://www.runoob.com/dtd/dtd-intro.html

---


文档类型定义（DTD）可定义合法的XML文档构建模块。它使用一系列合法的元素来定义文档的结构。


DTD 可被成行地声明于 XML 文档中，也可作为一个外部引用。


---


## 内部的 DOCTYPE 声明


假如 DTD 被包含在您的 XML 源文件中，它应当通过下面的语法包装在一个 DOCTYPE 声明中：


<!DOCTYPE root-element [element-declarations]>


带有 DTD 的 XML 文档实例（请在 IE5 以及更高的版本打开，并选择查看源代码）：


<?xml version="1.0"?>**
<!DOCTYPE note [

  <!ELEMENT note (to,from,heading,body)>

  <!ELEMENT to      (#PCDATA)>

  <!ELEMENT from    (#PCDATA)>

  <!ELEMENT heading (#PCDATA)>

  <!ELEMENT body    (#PCDATA)>

]>

<note>

  <to>Tove</to>

  <from>Jani</from>

  <heading>Reminder</heading>

  <body>Don't forget me this weekend</body>

</note>


[在您的浏览器中打开此 XML 文件，并选择"查看源代码"命令。](https://www.runoob.com/try/xml/note_in_dtd.xml)


以上 DTD 解释如下：


- **!DOCTYPE note** (第二行)定义此文档是 **note** 类型的文档。
- **!ELEMENT note** (第三行)定义 **note** 元素有四个元素："to、from、heading,、body"
- **!ELEMENT to** (第四行)定义 **to** 元素为 "#PCDATA" 类型
- **!ELEMENT from** (第五行)定义 **from** 元素为 "#PCDATA" 类型
- **!ELEMENT heading** (第六行)定义 **heading** 元素为 "#PCDATA" 类型
- **!ELEMENT body** (第七行)定义 **body** 元素为 "#PCDATA" 类型


---


## 外部文档声明


假如 DTD 位于 XML 源文件的外部，那么它应通过下面的语法被封装在一个 DOCTYPE 定义中：


<!DOCTYPE root-element SYSTEM "filename">


这个 XML 文档和上面的 XML 文档相同，但是拥有一个外部的 DTD: （[点击打开该文件](https://www.runoob.com/try/xml/note_ex_dtd.xml)，并选择"查看源代码"命令。）


<?xml version="1.0"?>

<!DOCTYPE note SYSTEM "note.dtd">

<note>


<to>Tove</to>


<from>Jani</from>


<heading>Reminder</heading>


<body>Don't forget me this weekend!</body>

</note>


这是包含 DTD 的 "note.dtd" 文件：


<!ELEMENT note (to,from,heading,body)>

<!ELEMENT to (#PCDATA)>

<!ELEMENT from (#PCDATA)>

<!ELEMENT heading (#PCDATA)>

<!ELEMENT body (#PCDATA)>


---


## 为什么使用 DTD？


通过 DTD，您的每一个 XML 文件均可携带一个有关其自身格式的描述。


通过 DTD，独立的团体可一致地使用某个标准的 DTD 来交换数据。


而您的应用程序也可使用某个标准的 DTD 来验证从外部接收到的数据。


您还可以使用 DTD 来验证您自身的数据。









	  AI 思考中...





			** [DTD 实例](https://www.runoob.com/dtd-examples.html)
			[DTD 构建模块](https://www.runoob.com/dtd-building.html) **













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
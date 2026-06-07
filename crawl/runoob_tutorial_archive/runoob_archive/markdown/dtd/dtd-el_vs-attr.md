# XML 元素 vs. 属性

- Source: https://www.runoob.com/dtd/dtd-el_vs-attr.html

---


在XML中，并没有规定何时使用属性，以及何时使用子元素。


---


## 使用元素 vs. 属性


数据可以存储在子元素或属性。


让我们来看下这些实例:


<person sex="female">**

<firstname>Anna</firstname>


<lastname>Smith</lastname>

</person>


<person>


<sex>female</sex>


<firstname>Anna</firstname>


<lastname>Smith</lastname>

</person>


在第一个例子中"sex"是一个属性。在后面一个例子中，"sex"是一个子元素。但是两者都提供了相同的信息。


没有特别规定何时使用属性，以及何时使用子元素。我的经验是在 HTML 中多使用属性，但在XML中，使用子元素，会感觉更像数据信息。


---


## 我喜欢的方式


我喜欢在子元素中存储数据**


下面的三个XML文档包含完全相同的信息：


本例中使用"date"属性：


<note date="12/11/2002">**

<to>Tove</to>


<from>Jani</from>


<heading>Reminder</heading>


<body>Don't forget me this weekend!</body>

</note>


本例中使用"date"元素：


<note>


<date>12/11/2002</date>


<to>Tove</to>


<from>Jani</from>


<heading>Reminder</heading>


<body>Don't forget me this weekend!</body>

</note>


本例中使用了扩展的"date" 元素: (这是我最喜欢的方式):


<note>


<date>


  <day>12</day>


  <month>11</month>


  <year>2002</year>


</date>


<to>Tove</to>


<from>Jani</from>


<heading>Reminder</heading>


<body>Don't forget me this weekend!</body>

</note>


---


## 避免使用属性?


你应该避免使用属性?


一些属性具有以下问题:


- 属性不能包含多个值（子元素可以）
- 属性不容易扩展（为以后需求的变化）
- 属性无法描述结构（子元素可以）
- 属性更难以操纵程序代码
- 属性值是不容易测试，针对DTD


如果您使用属性作为数据容器，最终的XML文档将难以阅读和维护。 尝试使用元素**来描述数据。只有在提供的数据是不相关信息时我们才建议使用属性。


不要这个样子结束（这不是XML应该使用的）：


<note day="12" month="11" year="2002"**
to="Tove" from="Jani" heading="Reminder"

body="Don't forget me this weekend!">

</note>


---


## 一个属性规则的例外


规则总是有另外的


关于属性的规则我有一个例外情况。


有时我指定的 ID 应用了元素。这些 ID 应用可在HTML中的很多相同的情况下可作为 NAME 或者 ID 属性来访问 XML 元素。以下实例展示了这种方式：


<messages>

  <note id="p501">


    <to>Tove</to>


    <from>Jani</from>


    <heading>Reminder</heading>


    <body>Don't forget me this weekend!</body>

  </note>


  <note id="p502">


    <to>Jani</to>


    <from>Tove</from>


    <heading>Re: Reminder</heading>


    <body>I will not!</body>

  </note>

</messages>


以上实例的 XML 文件中，ID 是只是一个计数器，或一个唯一的标识符，来识别不同的便签而不是作为数据的一部分。


在这里我想说的是，元数据（关于数据的数据）应当存储为属性，而数据本身应当存储为元素。








	  AI 思考中...





			** [DTD 属性](https://www.runoob.com/dtd-attributes.html)
			[DTD 实体](https://www.runoob.com/dtd-entities.html) **













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
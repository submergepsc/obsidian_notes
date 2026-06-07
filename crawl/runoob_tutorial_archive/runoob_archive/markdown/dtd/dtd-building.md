# DTD - XML 构建模块

- Source: https://www.runoob.com/dtd/dtd-building.html

---


XML 和 HTML文档的主要的构建模块是元素标签。


---


## XML 文档构建模块


所有的 XML 文档（以及 HTML 文档）均由以下简单的构建模块构成：


- 元素
- 属性
- 实体
- PCDATA
- CDATA


---


## 元素


元素是 XML 以及 HTML 文档的**主要构建模块**。


HTML 元素的例子是 "body" 和 "table"。XML 元素的例子是 "note" 和 "message" 。元素可包含文本、其他元素或者是空的。空的 HTML 元素的例子是 "hr"、"br" 以及 "img"。


实例:



    <body>some text</body>**

	<message>some text</message>



---


属性可提供有关元素的额外信息**。


属性总是被置于某元素的开始标签中。属性总是以**名称/值**的形式成对出现的。下面的 "img" 元素拥有关于源文件的额外信息：



    <img src="computer.gif" />



元素的名称是 "img"。属性的名称是 "src"。属性的值是 "computer.gif"。由于元素本身为空，它被一个 " /" 关闭。


---


## 实体


实体是用来定义普通文本的变量。实体引用是对实体的引用。


大多数同学都了解这个 HTML 实体引用：" "。这个"无折行空格"实体在 HTML 中被用于在某个文档中插入一个额外的空格。


当文档被 XML 解析器解析时，实体就会被展开。


| 实体引用 | 字符 |
| --- | --- |
| < |  |
| & | & |
| " | " |
| ' | ' |


---


## PCDATA


PCDATA 的意思是被解析的字符数据（parsed character data）。


可把字符数据想象为 XML 元素的开始标签与结束标签之间的文本。


**PCDATA 是会被解析器解析的文本。这些文本将被解析器检查实体以及标记。**


文本中的标签会被当作标记来处理，而实体会被展开。


不过，被解析的字符数据不应当包含任何 &、 字符；需要使用 &、< 以及 > 实体来分别替换它们。


---


## CDATA


CDATA 的意思是字符数据（character data）。


**CDATA 是不会被解析器解析的文本。**在这些文本中的标签不会被当作标记来对待，其中的实体也不会被展开。









	  AI 思考中...





			** [DTD 简介](https://www.runoob.com/dtd-intro.html)
			[DTD 元素](https://www.runoob.com/dtd-elements.html) **













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
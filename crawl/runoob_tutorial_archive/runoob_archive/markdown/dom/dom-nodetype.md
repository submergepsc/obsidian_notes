# XML DOM 节点类型

- Source: https://www.runoob.com/dom/dom-nodetype.html

---


DOM 是一个代表节点对象层次的文档。


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


下面的实例使用 XML 文件 [books.xml](https://www.runoob.com/try/demo_source/books.xml)。** 函数 [loadXMLDoc()](https://www.runoob.com/dom-loadxmldoc.html)，位于外部 JavaScript 中，用于加载 XML 文件。


[显示所有元素的 nodeName 和 nodeType](https://www.runoob.com/try/try.php?filename=try_dom_nodetype)


[显示所有元素的 nodeName 和 nodeValue](https://www.runoob.com/try/try.php?filename=try_dom_nodevalue)


---


## 节点类型


下面的表格列举了不同的 W3C 节点类型，每个节点类型中可能会包含子类：


| 节点类型 | 描述 | 子类 |
| --- | --- | --- |
| Document | 代表整个文档（DOM 树的根节点） | Element (max. one), ProcessingInstruction, Comment, DocumentType |
| DocumentFragment | 代表"轻量级"的 Document 对象，它可以保留文档中的一部分 | Element, ProcessingInstruction, Comment, Text, CDATASection, Entity参考手册 |
| DocumentType | 为文档中定义的实体提供了一个接口 | None |
| ProcessingInstruction | 代表一个处理指令 | None |
| EntityReference | 代表一个实体引用 | Element, ProcessingInstruction, Comment, Text, CDATASection, EntityReference |
| Element | 表示一个元素 | Element, Text, Comment, ProcessingInstruction, CDATASection, EntityReference |
| Attr | 代表一个属性 | Text, EntityReference |
| Text | 代表元素或属性的文本内容 | None |
| CDATASection | 代表文档中的 CDATA 区段（文本不会被解析器解析） | None |
| Comment | 代表一个注释 | None |
| Entity | 代表一个实体 | Element, ProcessingInstruction, Comment, Text, CDATASection, EntityReference |
| Notation | 定义一个在 DTD 中声明的符号 | None |


## 节点类型 - 返回值


下面的表格列举了每个节点类型（nodetype）所返回的节点名称（nodeName）和节点值（nodeValue）：


| 节点类型 | 返回的节点名称 | 返回的节点值 |
| --- | --- | --- |
| Document | #document | null |
| DocumentFragment | #document fragment | null |
| DocumentType | 文档类型名称 | null |
| Entity参考手册 | 实体引用名称 | null |
| Element | 元素名称 | null |
| Attr | 属性名称 | 属性值 |
| ProcessingInstruction | 目标 | 节点的内容 |
| Comment | #comment | 注释文本 |
| Text | #text | 节点的内容 |
| CDATASection | #cdata-section | 节点的内容 |
| Entity | 实体名称 | null |
| Notation | 符号名称 | null |


## 节点类型 - 命名常量


| 节点类型 | 命名常量 |
| --- | --- |
| 1 | ELEMENT_NODE |
| 2 | ATTRIBUTE_NODE |
| 3 | TEXT_NODE |
| 4 | CDATA_SECTION_NODE |
| 5 | ENTITY_REFERENCE_NODE |
| 6 | ENTITY_NODE |
| 7 | PROCESSING_INSTRUCTION_NODE |
| 8 | COMMENT_NODE |
| 9 | DOCUMENT_NODE |
| 10 | DOCUMENT_TYPE_NODE |
| 11 | DOCUMENT_FRAGMENT_NODE |
| 12 | NOTATION_NODE |










	  AI 思考中...





			** [XML DOM – HttpRequest 对象](https://www.runoob.com/dom-httprequest.html)
			[XML DOM – Node 对象](https://www.runoob.com/dom-node.html) **













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
# XML Schema 参考手册

- Source: https://www.runoob.com/schema/schema-elements-ref.html

---


# XSD 元素


| 元素 | 解释 |
| --- | --- |
| all | 规定子元素能够以任意顺序出现，每个子元素可出现零次或一次。 |
| annotation | annotation 元素是一个顶层元素，规定 schema 的注释。 |
| any | 使创作者可以通过未被 schema 规定的元素来扩展 XML 文档。 |
| anyAttribute | 使创作者可以通过未被 schema 规定的属性来扩展 XML 文档。 |
| appInfo | 规定 annotation 元素中应用程序要使用的信息。 |
| attribute | 定义一个属性。 |
| attributeGroup | 定义在复杂类型定义中使用的属性组。 |
| choice | 仅允许在 声明中包含一个元素出现在包含元素中。 |
| complexContent | 定义对复杂类型（包含混合内容或仅包含元素）的扩展或限制。 |
| complexType | 定义复杂类型。 |
| documentation | 定义 schema 中的文本注释。 |
| element | 定义元素。 |
| extension | 扩展已有的 simpleType 或 complexType 元素。 |
| field | 规定 XPath 表达式，该表达式规定用于定义标识约束的值。 |
| group | 定义在复杂类型定义中使用的元素组。 |
| import | 向一个文档添加带有不同目标命名空间的多个 schema。 |
| include | 向一个文档添加带有相同目标命名空间的多个 schema。 |
| key | 指定属性或元素值（或一组值）必须是指定范围内的键。 |
| keyref | 规定属性或元素值（或一组值）对应指定的 key 或 unique 元素的值。 |
| list | 把简单类型定义为指定数据类型的值的一个列表。 |
| notation | 描述 XML 文档中非 XML 数据的格式。 |
| redefine | 重新定义从外部架构文件中获取的简单和复杂类型、组和属性组。 |
| restriction | 定义对 simpleType、simpleContent 或 complexContent 的约束。 |
| schema | 定义 schema 的根元素。 |
| selector | 指定 XPath 表达式，该表达式为标识约束选择一组元素。 |
| sequence | 要求子元素必须按顺序出现。每个子元素可出现 0 到任意次数。 |
| simpleContent | 包含对 complexType 元素的扩展或限制且不包含任何元素。 |
| simpleType | 定义一个简单类型，规定约束以及关于属性或仅含文本的元素的值的信息。 |
| union | 定义多个 simpleType 定义的集合。 |
| unique | 指定属性或元素值（或者属性或元素值的组合）在指定范围内必须是唯一的。 |

**
---


# XSD 限定/Facets


[参阅 XSD 限定 / Facets](https://www.runoob.com/schema-facets.html)


| 限定 | 描述 |
| --- | --- |
| enumeration | 定义可接受值的一个列表 |
| fractionDigits | 定义所允许的最大的小数位数。必须大于等于0。 |
| length | 定义所允许的字符或者列表项目的精确数目。必须大于或等于0。 |
| maxExclusive | 定义数值的上限。所允许的值必须小于此值。 |
| maxInclusive | 定义数值的上限。所允许的值必须小于或等于此值。 |
| maxLength | 定义所允许的字符或者列表项目的最大数目。必须大于或等于0。 |
| minExclusive | 定义数值的下限。所允许的值必需大于此值。 |
| minInclusive | 定义数值的下限。所允许的值必需大于或等于此值。 |
| minLength | 定义所允许的字符或者列表项目的最小数目。必须大于或等于0。 |
| pattern | 定义可接受的字符的精确序列。 |
| totalDigits | 定义所允许的阿拉伯数字的精确位数。必须大于0。 |
| whiteSpace | 定义空白字符（换行、回车、空格以及制表符）的处理方式。 |








	  AI 思考中...





			** [XML Schema restriction 元素](https://www.runoob.com/el-restriction.html)














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
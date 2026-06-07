# XSD 字符串 数据类型

- Source: https://www.runoob.com/schema/schema-dtypes-string.html

---


字符串数据类型用于可包含字符串的值。


---


## 字符串数据类型（String Data Type）


字符串数据类型可包含字符、换行、回车以及制表符。


下面是一个关于某个 scheme 中字符串声明的例子：


<xs:element name="customer" type="xs:string"/>


文档中的元素看上去应该类似这样：


<customer>John Smith</customer>


或者类似这样：


<customer>       John Smith    	</customer>


**注意：**如果您使用字符串数据类型，XML 处理器就不会更改其中的值。


---


## 规格化字符串数据类型（NormalizedString Data Type）


规格化字符串数据类型源自于字符串数据类型。


规格化字符串数据类型同样可包含字符，但是 XML 处理器会移除折行，回车以及制表符。


下面是一个关于在某个 schema 中规格化字符串数据类型的例子：


<xs:element name="customer" type="xs:normalizedString"/>


文档中的元素看上去应该类似这样：


<customer>John Smith</customer>


或者类似这样：


<customer>     John Smith     </customer>


**注意：**在上面的例子中，XML 处理器会使用空格替换所有的制表符。


---


## Token 数据类型（Token Data Type）


Token 数据类型同样源自于字符串数据类型。


Token 数据类型同样可包含字符，但是 XML 处理器会移除换行符、回车、制表符、开头和结尾的空格以及（连续的）空格。


下面是在 schema 中一个有关 token 声明的例子：


<xs:element name="customer" type="xs:token"/>


文档中的元素看上去应该类似这样：


<customer>John Smith</customer>


或者类似这样：


<customer>     John Smith     </customer>


**注意：**>在上面这个例子中，XML 解析器会移除制表符。


---


## 字符串数据类型


请注意，所有以下的数据类型均衍生于字符串数据类型（除了字符串数据类型本身）！


| 名称 | 描述 |
| --- | --- |
| ENTITIES |  |
| ENTITY |  |
| ID | 在 XML 中提交 ID 属性的字符串 (仅与 schema 属性一同使用) |
| IDREF | 在 XML 中提交 IDREF 属性的字符串(仅与 schema 属性一同使用) |
| IDREFS language | 包含合法的语言 id 的字符串 |
| Name | 包含合法 XML 名称的字符串 |
| NCName |  |
| NMTOKEN | 在 XML 中提交 NMTOKEN 属性的字符串 (仅与 schema 属性一同使用) |
| NMTOKENS |  |
| normalizedString | 不包含换行符、回车或制表符的字符串 |
| QName |  |
| string | 字符串 |
| token | 不包含换行符、回车或制表符、开头或结尾空格或者多个连续空格的字符串 |


**
---


## 对字符串数据类型的限定（Restriction）


可与字符串数据类型一同使用的限定：


- enumeration
- length
- maxLength
- minLength
- pattern (NMTOKENS、IDREFS 以及 ENTITIES 无法使用此约束)
- whiteSpace









	  AI 思考中...





			** [XML Schema 实例](https://www.runoob.com/schema-example.html)
			[XML Schema 日期/时间 数据类型](https://www.runoob.com/schema-dtypes-date.html) **













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
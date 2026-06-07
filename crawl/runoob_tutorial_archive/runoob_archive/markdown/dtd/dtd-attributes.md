# DTD - 属性

- Source: https://www.runoob.com/dtd/dtd-attributes.html

---


在 DTD 中，属性通过 ATTLIST 声明来进行声明。


---


## 声明属性


属性声明使用下列语法：


<!ATTLIST element-name attribute-name attribute-type attribute-value>**

DTD 实例:


<!ATTLIST payment type CDATA "check">


XML 实例:


<payment type="check" />


以下是 属性类型**的选项：


| 类型 | 描述 |
| --- | --- |
| CDATA | 值为字符数据 (character data) |
| (en1\|en2\|..) | 此值是枚举列表中的一个值 |
| ID | 值为唯一的 id |
| IDREF | 值为另外一个元素的 id |
| IDREFS | 值为其他 id 的列表 |
| NMTOKEN | 值为合法的 XML 名称 |
| NMTOKENS | 值为合法的 XML 名称的列表 |
| ENTITY | 值是一个实体 |
| ENTITIES | 值是一个实体列表 |
| NOTATION | 此值是符号的名称 |
| xml: | 值是一个预定义的 XML 值 |



默认**属性值**可使用下列值 :


| 值 | 解释 |
| --- | --- |
| 值 | 属性的默认值 |
| #REQUIRED | 属性值是必需的 |
| #IMPLIED | 属性不是必需的 |
| #FIXED value | 属性值是固定的 |


**
---


## 默认属性值


DTD:

<!ELEMENT square EMPTY>

<!ATTLIST square width CDATA "0">


合法的 XML:

<square width="100" />


在上面的例子中，"square" 被定义为带有 CDATA 类型的 "width" 属性的空元素。如果宽度没有被设定，其默认值为0 。


---


## #REQUIRED


### 语法


<!ATTLIST element-name attribute-name attribute-type #REQUIRED>


### 实例


DTD:

<!ATTLIST person number CDATA #REQUIRED>


合法的 XML:

<person number="5677" />


非法的 XML:

<person />


假如您没有默认值选项，但是仍然希望强制作者提交属性的话，请使用关键词 #REQUIRED。


---


## #IMPLIED


### 语法


<!ATTLIST element-name attribute-name attribute-type #IMPLIED>


### 实例


DTD:

<!ATTLIST contact fax CDATA #IMPLIED>


合法的 XML:

<contact fax="555-667788" />


合法的 XML:

<contact />


假如您不希望强制作者包含属性，并且您没有默认值选项的话，请使用关键词 #IMPLIED。


---


## #FIXED


### 语法


<!ATTLIST element-name attribute-name attribute-type #FIXED "value">


### 实例


DTD:

<!ATTLIST sender company CDATA #FIXED "Microsoft">


合法的 XML:

<sender company="Microsoft" />


非法的 XML:

<sender company="W3Schools" />


如果您希望属性拥有固定的值，并不允许作者改变这个值，请使用 #FIXED 关键词。如果作者使用了不同的值，XML 解析器会返回错误。


---


## 列举属性值


### 语法


<!ATTLIST element-name attribute-name (en1|en2|..) default-value>


### 实例


DTD:

<!ATTLIST payment type (check|cash) "cash">


XML 例子:

<payment type="check" />

或

<payment type="cash" />


如果您希望属性值为一系列固定的合法值之一，请使用列举属性值。








	  AI 思考中...





			** [DTD 元素](https://www.runoob.com/dtd-elements.html)
			[XML 元素和属性比较](https://www.runoob.com/dtd-el_vs-attr.html) **













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
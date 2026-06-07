# XSD 杂项 数据类型

- Source: https://www.runoob.com/schema/schema-dtypes-misc.html

---


其他杂项数据类型包括布尔、base64Binary、十六进制、浮点、双精度、anyURI、anyURI 以及 NOTATION。


---


## 布尔数据类型（Boolean Data Type）


布尔数据性用于规定 true 或 false 值。


下面是一个关于某个 scheme 中逻辑声明的例子：


<xs:attribute name="disabled" type="xs:boolean"/>


文档中的元素看上去应该类似这样：


<prize disabled="true">999</prize>


**注意：** 合法的布尔值是 true、false、1（表示 true） 以及 0（表示 false）。


---


## 二进制数据类型（Binary Data Types）


二进制数据类型用于表达二进制形式的数据。


我们可使用两种二进制数据类型：


- base64Binary (Base64 编码的二进制数据)
- hexBinary (十六进制编码的二进制数据)


下面是一个关于某个 scheme 中 hexBinary 声明的例子：


<xs:element name="blobsrc" type="xs:hexBinary"/>

**
---


## AnyURI 数据类型（AnyURI Data Type）


anyURI 数据类型用于规定 URI。


下面是一个关于某个 scheme 中 anyURI 声明的例子：


<xs:attribute name="src" type="xs:anyURI"/>


文档中的元素看上去应该类似这样：


<pic src="http://www.w3schools.com/images/smiley.gif" />


注意：** 如果某个 URI 含有空格，请用 %20 替换它们。


---


## 杂项数据类型


| 名称 | 描述 |
| --- | --- |
| anyURI |  |
| base64Binary |  |
| boolean |  |
| double |  |
| float |  |
| hexBinary |  |
| NOTATION |  |
| QName |  |

**
---


## 对杂项数据类型的限定（Restriction）


可与杂项数据类型一同使用的限定：


- enumeration (布尔数据类型无法使用此约束*)
- length (布尔数据类型无法使用此约束)
- maxLength (布尔数据类型无法使用此约束)
- minLength (布尔数据类型无法使用此约束)
- pattern
- whiteSpace


*译者注：约束指 constraint。









	  AI 思考中...





			** [XML Schema 数值数据类型](https://www.runoob.com/schema-dtypes-numeric.html)
			[XML 编辑器](https://www.runoob.com/schema-editor.html) **













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
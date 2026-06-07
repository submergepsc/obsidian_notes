# 为什么使用 XML Schemas?

- Source: https://www.runoob.com/schema/schema-why.html

---


XML Schema 比 DTD 更强大。


---


## XML Schema 支持数据类型


XML Schema 最重要的能力之一就是对数据类型的支持。


### 通过对数据类型的支持：


- 可更容易地描述允许的文档内容
- 可更容易地验证数据的正确性
- 可更容易地与来自数据库的数据一并工作
- 可更容易地定义数据约束（data facets）
- 可更容易地定义数据模型（或称数据格式）
- 可更容易地在不同的数据类型间转换数据


编者注：数据约束，或称 facets，是 XML Schema 原型中的一个术语，中文可译为"面"，用来约束数据类型的容许值。


---


## XML Schema 使用 XML 语法


另一个关于 XML Schema 的重要特性是，它们由 XML 编写。


### 由 XML 编写 XML Schema 有很多好处：


- 不必学习新的语言
- 可使用 XML 编辑器来编辑 Schema 文件
- 可使用 XML 解析器来解析 Schema 文件
- 可通过 XML DOM 来处理 Schema
- 可通过 XSLT 来转换 Schema


---


## XML Schema 可保护数据通信


当数据从发送方被发送到接受方时，其要点是双方应有关于内容的相同的"期望值"。


通过 XML Schema，发送方可以用一种接受方能够明白的方式来描述数据。


一种数据，比如 "03-11-2004"，在某些国家被解释为11月3日，而在另一些国家为当作3月11日。


但是一个带有数据类型的 XML 元素，比如：2004-03-11，可确保对内容一致的理解，这是因为 XML 的数据类型 "date" 要求的格式是 "YYYY-MM-DD"。


---


## XML Schema 可扩展


XML Schema 是可扩展的，因为它们由 XML 编写。


### 通过可扩展的 Schema 定义，您可以：


- 在其他 Schema 中重复使用您的 Schema
- 创建由标准类型衍生而来的您自己的数据类型
- 在相同的文档中引用多重的 Schema


---


## 形式良好是不够的


我们把符合 XML 语法的文档称为形式良好的 XML 文档，比如：


- 它必须以 XML 声明开头
- 它必须拥有唯一的根元素
- 开始标签必须与结束标签相匹配
- 元素对大小写敏感
- 所有的元素都必须关闭
- 所有的元素都必须正确地嵌套
- 必须对特殊字符使用实体


即使文档的形式良好，仍然不能保证它们不会包含错误，并且这些错误可能会产生严重的后果。


请考虑下面的情况：您订购的了 5 打激光打印机，而不是 5 台。通过 XML Schema，大部分这样的错误会被您的验证软件捕获到。









	  AI 思考中...





			** [XML Schemas 简介](https://www.runoob.com/schema-intro.html)
			[如何使用 XML Schema](https://www.runoob.com/schema-howto.html) **













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
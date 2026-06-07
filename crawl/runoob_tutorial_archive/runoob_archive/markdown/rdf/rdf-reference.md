# RDF 参考手册

- Source: https://www.runoob.com/rdf/rdf-reference.html

---


## RDF 命名空间


RDF 命名空间(xmlns:rdf):: [http://www.w3.org/1999/02/22-rdf-syntax-ns#](https://www.runoob.com/rdf-syntax-ns.xml)


RDF 命名空间(xmlns:rdfs ):: [http://www.w3.org/2000/01/rdf-schema#](https://www.runoob.com/rdf-schema.xml)


---


## RDF 扩展名和MIME 类型


RDF 文件的推荐扩展名为**.rdf**,然而，扩展名**.XML**是经常被用来兼容旧的XML解析器。


MIME 类型：**"application/rdf+xml"**。


---


## RDFS / RDF 类


| 元素 | 类 | 子类 |
| --- | --- | --- |
| rdfs:Class | All classes |  |
|  |  |  |
| rdfs:Datatype | Data types | Class |
| rdfs:Resource | All resources | Class |
|  |  |  |
| rdfs:Container | Containers | Resource |
| rdfs:Literal | Literal values (text and numbers) | Resource |
|  |  |  |
| rdf:List | Lists | Resource |
| rdf:Property | Properties | Resource |
| rdf:Statement | Statements | Resource |
|  |  |  |
| rdf:Alt | Containers of alternatives | Container |
| rdf:Bag | Unordered containers | Container |
| rdf:Seq | Ordered containers | Container |
|  |  |  |
| rdfs:ContainerMembershipProperty | Container membership properties | Property |
| rdf:XMLLiteral | XML literal values | Literal |

**
---


## RDFS / RDF 属性


| 元素 | 领域 | 范围 | 描述 |
| --- | --- | --- | --- |
| rdfs:domain | Property | Class | 资源域 |
| rdfs:range | Property | Class | 资源的范围 |
| rdfs:subPropertyOf | Property | Property | 该属性是一个属性的子属性 |
|  |  |  |  |
| rdfs:subClassOf | Class | Class | 资源是一个类的子类 |
| rdfs:comment | Resource | Literal | 人类可读的资源描述 |
| rdfs:label | Resource | Literal | 人类可读的资源标签（名称） |
| rdfs:isDefinedBy | Resource | Resource | 资源的定义 |
| rdfs:seeAlso | Resource | Resource | 关于资源的其他信息 |
| rdfs:member | Resource | Resource | 资源的成员 |
|  |  |  |  |
| rdf:first | List | Resource |  |
| rdf:rest | List | List |  |
| rdf:subject | Statement | Resource | 一个RDF陈述的资源主体 |
| rdf:predicate | Statement | Resource | 在一个RDF陈述的资源的谓词 |
| rdf:object | Statement | Resource | 一个RDF陈述的资源客体 |
| rdf:value | Resource | Resource | value属性 |
| rdf:type | Resource | Class | 资源是一个类的实例 |


## RDF 属性


| 元素 | 领域 | 范围 | 描述 |
| --- | --- | --- | --- |
|  |  |  |  |
| rdf:about |  |  | 定义所描述的资源 |
| rdf:Description |  |  | 资源描述的容器 |
| rdf:resource |  |  | 定义资源，以确定一个属性 |
| rdf:datatype |  |  | 定义一个元素的数据类型 |
| rdf:ID |  |  | 定义元素的ID |
| rdf:li |  |  | 定义列表 |
| rdf:_n |  |  | 定义一个节点 |
| rdf:nodeID |  |  | 定义元素节点的ID |
| rdf:parseType |  |  | 定义元素应如何解析 |
| rdf:RDF |  |  | 一个RDF文档的根 |
| xml:base |  |  | 定义了XML基础 |
| xml:lang |  |  | 定义元素内容的语言 |
|  |  |  |  |
| rdf:aboutEach |  |  | （删除） |
| rdf:aboutEachPrefix |  |  | （删除） |
| rdf:bagID |  |  | （删除） |


描述为"删除" 的为最近从RDF标准删除元素。








	  AI 思考中...





			** [OWL 简介](https://www.runoob.com/rdf-owl.html)














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
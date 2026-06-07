# WSDL 文档

- Source: https://www.runoob.com/wsdl/wsdl-documents.html

---


WSDL 文档仅仅是一个简单的 XML 文档。


它包含一系列描述某个 web service 的定义。


---


## WSDL 文档结构


WSDL 文档是利用这些主要的元素来描述某个 web service 的：


| 元素 | 定义 |
| --- | --- |
|  | web service 执行的操作 |
|  | web service 使用的消息 |
|  | web service 使用的数据类型 |
|  | web service 使用的通信协议 |


一个 WSDL 文档的主要结构是类似这样的：


## WSDL 文档实例


```
<definitions>

<types>
  data type definitions........
</types>

<message>
  definition of the data being communicated....
</message>

<portType>
  set of operations......
</portType>

<binding>
  protocol and data format specification....
</binding>

</definitions>
```


WSDL 文档可包含其它的元素，比如 extension 元素，以及一个 service 元素，此元素可把若干个 web services 的定义组合在一个单一的 WSDL 文档中。


---


## WSDL 端口


** 元素是最重要的 WSDL 元素。 它可描述一个 web service、可被执行的操作，以及相关的消息。 可以把  元素比作传统编程语言中的一个函数库（或一个模块、或一个类）。 --- ## WSDL 消息 ** 元素定义一个操作的数据元素。 每个消息均由一个或多个部件组成。可以把这些部件比作传统编程语言中一个函数调用的参数。 --- ## WSDL types ** 元素定义 web service 使用的数据类型。 为了最大程度的平台中立性，WSDL 使用 XML Schema 语法来定义数据类型。 --- ## WSDL Bindings ** 元素为每个端口定义消息格式和协议细节。 --- ## WSDL 实例 这是某个 WSDL 文档的简化的片段： ## 实例
```
<message name="getTermRequest">
  <part name="term" type="xs:string"/>
</message>

<message name="getTermResponse">
  <part name="value" type="xs:string"/>
</message>

<portType name="glossaryTerms">
  <operation name="getTerm">
    <input message="getTermRequest"/>
    <output message="getTermResponse"/>
  </operation>
</portType>
```
 在这个例子中，** 元素把 "glossaryTerms" 定义为某个*端口*的名称，把 "getTerm" 定义为某个*操作*的名称。


操作 "getTerm" 拥有一个名为 "getTermRequest" 的*输入消息*，以及一个名为 "getTermResponse" 的*输出消息*。


** 元素可定义每个消息的*部件*，以及相关联的数据类型。


对比传统的编程，glossaryTerms 是一个函数库，而 "getTerm" 是带有输入参数 "getTermRequest" 和返回参数 getTermResponse 的一个函数。









	  AI 思考中...





			** [WSDL 简介](https://www.runoob.com/wsdl-intro.html)
			[WSDL 端口](https://www.runoob.com/wsdl-ports.html) **













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
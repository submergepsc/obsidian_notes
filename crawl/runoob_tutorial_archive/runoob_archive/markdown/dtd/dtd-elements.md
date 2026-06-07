# DTD - 元素

- Source: https://www.runoob.com/dtd/dtd-elements.html

---


在一个 DTD 中，元素通过元素声明来进行声明。


---


## 声明一个元素


在 DTD 中，XML 元素通过元素声明来进行声明。元素声明使用下面的语法：


<!ELEMENT element-name category>**
或

<!ELEMENT element-name (element-content)>


---


## 空元素


空元素通过类别关键词EMPTY进行声明：


<!ELEMENT element-name EMPTY>


实例:


<!ELEMENT br EMPTY>


XML example:


<br />


---


## 只有 PCDATA 的元素


只有 PCDATA 的元素通过圆括号中的 #PCDATA 进行声明：


<!ELEMENT element-name (#PCDATA)>


实例:


<!ELEMENT from (#PCDATA)>


---

## 带有任何内容的元素


通过类别关键词 ANY 声明的元素，可包含任何可解析数据的组合：


<!ELEMENT element-name ANY>


实例:


<!ELEMENT note ANY>


---


## 带有子元素（序列）的元素


带有一个或多个子元素的元素通过圆括号中的子元素名进行声明：


<!ELEMENT element-name (child1)>

或

<!ELEMENT element-name (child1,child2,...)>


实例:


<!ELEMENT note (to,from,heading,body)>


当子元素按照由逗号分隔开的序列进行声明时，这些子元素必须按照相同的顺序出现在文档中。在一个完整的声明中，子元素也必须被声明，同时子元素也可拥有子元素。"note" 元素的完整声明是：


<!ELEMENT note (to,from,heading,body)>

<!ELEMENT to      (#PCDATA)>

<!ELEMENT from    (#PCDATA)>

<!ELEMENT heading (#PCDATA)>

<!ELEMENT body    (#PCDATA)>


---


## 声明只出现一次的元素


<!ELEMENT element-name (child-name)>


实例:


<!ELEMENT note (message)>


上面的例子声明了：message 子元素必须出现一次，并且必须只在 "note" 元素中出现一次。


---


## 声明最少出现一次的元素


<!ELEMENT element-name (child-name+)>


实例:


<!ELEMENT note (message+)>


上面的例子中的加号（+）声明了：message 子元素必须在 "note" 元素内出现至少一次。


---


## 声明出现零次或多次的元素


<!ELEMENT element-name (child-name*)>


实例:


<!ELEMENT note (message*)>


上面的例子中的星号（*）声明了：子元素 message 可在 "note" 元素内出现零次或多次。


---


## 声明出现零次或一次的元素


<!ELEMENT element-name (child-name?)>


实例:


<!ELEMENT note (message?)>


上面的例子中的问号(?)声明了：子元素 message 可在 "note" 元素内出现零次或一次。


---


## 声明"非.../即..."类型的内容


实例:


<!ELEMENT note (to,from,header,(message|body))>


上面的例子声明了："note" 元素必须包含 "to" 元素、"from" 元素、"header" 元素，以及非 "message" 元素即 "body" 元素。


---


## 声明混合型的内容


实例:


<!ELEMENT note (#PCDATA|to|from|header|message)*>


上面的例子声明了："note" 元素可包含出现零次或多次的 PCDATA、"to"、"from"、"header" 或者 "message"。










	  AI 思考中...





			** [DTD 构建模块](https://www.runoob.com/dtd-building.html)
			[DTD 属性](https://www.runoob.com/dtd-attributes.html) **













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
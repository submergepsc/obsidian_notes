# XQuery 函数

- Source: https://www.runoob.com/xquery/xquery-functions.html

---


XQuery 1.0、XPath 2.0 以及 XSLT 2.0 共享相同的函数库。


---


## XQuery 函数


XQuery 含有超过 100 个内建的函数。这些函数可用于字符串值、数值、日期以及时间比较、节点和 QName 操作、序列操作、逻辑值等等。您也可在 XQuery 中定义自己的函数。


---


## XQuery 内建函数


XQuery 函数命名空间的 URI：


http://www.w3.org/2005/02/xpath-functions


函数命名空间的默认前缀是 fn:。


提示：函数经常被通过 fn: 前缀进行调用，例如 fn:string()。不过，由于 fn: 是命名空间的默认前缀，所以函数名称不必在被调用时使用前缀。


您可以在我们的 XPath 教程中找到完整的《[内建 XQuery 函数参考手册](https://www.runoob.com/../xpath/xpath-tutorial.html)》。


---


## 函数调用实例


函数调用可与表达式一同使用。请看下面的例子：


### 例1：在元素中


<name>{upper-case($booktitle)}</name>


### 例2: 在路径表达式的谓语中


doc("books.xml")/bookstore/book[substring(title,1,5)='Harry']


### 例3: 在 let 语句中


let $name := (substring($booktitle,1,4))

**
---


## XQuery 用户定义函数


如果找不到所需的 XQuery 函数，你可以编写自己的函数。


可在查询中或独立的库中定义用户自定义函数。


### 语法


declare function *前缀:函数名*($*参数 *AS* 数据类型*)

AS *返回的数据类型*

{

 ...*函数代码*...

}


### 关于用户自定义函数的注意事项：


- 请使用 declare function 关键词
- 函数名须使用前缀
- 参数的数据类型通常与在 XML Schema 中定义的数据类型一致
- 函数主体须被花括号包围


### 一个在查询中声明的用户自定义函数的例子：


declare function local:minPrice($p as xs:decimal?,$d as xs:decimal?)

  AS xs:decimal?

{

let $disc := ($p * $d) div 100

return ($p - $disc)

}


Below is an example of how to call the function above:


<minPrice>{local:minPrice($book/price,$book/discount)}</minPrice>








	  AI 思考中...





			** [XQuery 选择和过滤](https://www.runoob.com/xquery-select.html)
			[XQuery 总结](https://www.runoob.com/xquery-summary.html) **













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
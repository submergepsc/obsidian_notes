# XQuery 语法

- Source: https://www.runoob.com/xquery/xquery-syntax.html

---


XQuery 对大小写敏感，XQuery 的元素、属性以及变量必须是合法的 XML 名称。


---


## XQuery 的基础语法规则：


一些基本的语法规则：


- XQuery 对大小写敏感
- XQuery 的元素、属性以及变量必须是合法的 XML 名称。
- XQuery 字符串值可使用单引号或双引号。
- XQuery 变量由 "$" 并跟随一个名称来进行定义，举例，$bookstore
- XQuery 注释被 (: 和 :) 分割，例如，(: XQuery 注释 :)


---


## XQuery 条件表达式


"If-Then-Else" 可以在 XQuery 中使用。


请看下面的例子：


for $x in doc("books.xml")/bookstore/book**
return	**if (**$x/@category="CHILDREN"**)**
**then** <child>{data($x/title)}</child>
**else** <adult>{data($x/title)}</adult>


请注意 "If-Then-Else" 的语法：if 表达式后的圆括号是必需的。else 也是必需的，不过只写 "else ()" 也可以。


上面的例子的结果：


<adult>Everyday Italian</adult>

<child>Harry Potter</child>

<adult>Learning XML</adult>

<adult>XQuery Kick Start</adult>


---


## XQuery 比较


在 XQuery 中，有两种方法来比较值。


- 通用比较：=, !=, , >=
- 值的比较：eq、ne、lt、le、gt、ge


### 这两种比较方法的差异如下：


请看下面的 XQuery 表达式：


$bookstore//book/@q > 10

如果 q 属性的值大于 10，上面的表达式的返回值为 true。


如下实例，如果仅返回一个 q，且它的值大于 10，那么表达式返回 true。如果不止一个 q 被返回，则会发生错误：


$bookstore//book/@q gt 10








	  AI 思考中...





			** [XQuery 术语](https://www.runoob.com/xquery-terms.html)
			[XQuery 添加元素和属性](https://www.runoob.com/xquery-add.html) **













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
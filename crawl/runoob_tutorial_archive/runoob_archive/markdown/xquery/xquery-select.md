# XQuery 选择 和 过滤

- Source: https://www.runoob.com/xquery/xquery-select.html

---


## XML实例文档


我们将在下面的例子中继续使用这个 "books.xml" 文档（和上面的章节所使用的 XML 文件相同）。


[在您的浏览器中查看 "books.xml" 文件](https://www.runoob.com/try/xml/books.xml)。


---


## 选择和过滤元素


正如在前面的章节所看到的，我们使用路径表达式或 FLWOR 表达式来选取和过滤元素。


请看下面的 FLWOR 表达式：


for $x in doc("books.xml")/bookstore/book**
where $x/price>30

order by $x/title

return $x/title


- for - （可选） 向每个由 in 表达式返回的项目捆绑一个变量
- let - （可选）
- where - （可选） 设定一个条件
- order by - （可选） 设定结果的排列顺序
- return - 规定在结果中返回的内容


## for 语句


for 语句可将变量捆绑到由 in 表达式返回的每个项目。for 语句可产生迭代。在同一个 FLWOR 表达式中可存在多重 for 语句。


如需在一个 for 语句中进行指定次数地循环，您可使用关键词 to ：


for $x in (1 to 5)

return <test>{$x}</test>


结果：


<test>1</test>

<test>2</test>

<test>3</test>

<test>4</test>

<test>5</test>


关键词 at **可用于计算迭代：


for $x at $i in doc("books.xml")/bookstore/book/title**
return <book>{$i}. {data($x)}</book>


结果：


<book>1. Everyday Italian</book>

<book>2. Harry Potter</book>

<book>3. XQuery Kick Start</book>

<book>4. Learning XML</book>


在 for 语句中同样允许多个 in 表达式。请使用逗号来分割每一个 in 表达式：


for $x in (10,20), $y in (100,200)

return <test>x={$x} and y={$y}</test>


结果：


<test>x=10 and y=100</test>

<test>x=10 and y=200</test>

<test>x=20 and y=100</test>

<test>x=20 and y=200</test>


## let 语句


let 语句可完成变量分配，并可避免多次重复相同的表达式。let 语句不会导致迭代。


let $x := (1 to 5)

return <test>{$x}</test>


结果：


<test>1 2 3 4 5</test>


## where 语句


where 语句用于为结果设定一个或多个条件（criteria）。


where $x/price>30 and $x/price<100


## order by 语句


order by 语句用于规定结果的排序次序。在这里，我们要根据 category 和 title 来对结果进行排序：


for $x in doc("books.xml")/bookstore/book

order by $x/@category, $x/title

return $x/title


结果：


<title lang="en">Harry Potter</title>

<title lang="en">Everyday Italian</title>

<title lang="en">Learning XML</title>

<title lang="en">XQuery Kick Start</title>


## return 语句：


return 语句规定要返回的内容。


for $x in doc("books.xml")/bookstore/book

return $x/title


结果：


<title lang="en">Everyday Italian</title>

<title lang="en">Harry Potter</title>

<title lang="en">XQuery Kick Start</title>

<title lang="en">Learning XML</title>








	  AI 思考中...





			** [XQuery 添加元素和属性](https://www.runoob.com/xquery-add.html)
			[XQuery 函数](https://www.runoob.com/xquery-functions.html) **













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
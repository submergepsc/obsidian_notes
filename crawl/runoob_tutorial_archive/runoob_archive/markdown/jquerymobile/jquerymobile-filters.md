# jQuery Mobile 过滤

- Source: https://www.runoob.com/jquerymobile/jquerymobile-filters.html

---

*

## 可过滤元素


所有的元素如果有一个或更多的子元素均可过滤。


**如何创建搜索字段:**


- 你想过滤的元素必须使用 data-filter="true" 属性。
- 创建  元素并指定 id，元素上加上 data-type="search" 属性。这样就能创建基本的搜索字段。将  元素放置于一个表单中，表单  元素使用 "ui-filterable" 类 - 该类会调整搜索字段与过滤元素的外边距。
- 接着为过滤的元素添加 data-input 属性。该值需要是  元素的 id。


接下来我们创建一个可过滤的列表：


## 列表中搜索元素



```javascript
<form class="ui-filterable">  <input id="myFilter"
	data-type="search"></form><ul data-role="listview"
	data-filter="true" data-input="#myFilter">  <li><a href="#">Adele</a></li>
	<li><a href="#">Billy</a></li>  <li><a href="#">Calvin</a></li>
	</ul>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_filter)


提示:** 可以在搜索字段中使用 placeholder 属性来设置提示信息：


## 实例



```javascript
<input
	id="myFilter" data-type="search" placeholder="根据名称搜索..">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_filter_placeholder)


---


## 自定义过滤


一般的插入到各个列表项的文本就是作为过滤的文本使用(如 A 对应 "Adele" 或 "B" 对应 "Billy")。 但是，如果你想指定自定义的过滤的文本，你需要在子元素中使用 data-filtertext 属性:


### 实例


```javascript
<li data-filtertext="fav"><a href="#">Adele</a></li>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lists_filtertext)


|  | 如果你在元素中使用了 data-filtertext 属性，元素的源文本内容在过滤时将被忽略， 这时你如果还要查找列表项"Adele"，需要使用的关键字为：f, a, v 或 fav。 |
| --- | --- |


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[过滤折叠列表](https://www.runoob.com/try/tryit.php?filename=tryjqmob_filters_collapsibles) 如何过滤折叠的列表。


[过滤表格](https://www.runoob.com/try/tryit.php?filename=tryjqmob_filters_tables) 如何过滤表格内容。


[过滤 元素](https://www.runoob.com/try/tryit.php?filename=tryjqmob_filters_div) 如何过滤  元素中包含的子  元素。








	  AI 思考中...





			* [jQuery Mobile 表格](https://www.runoob.com/jquerymobile-tables.html)
			[jQuery Mobile pagecontainerbeforeload 事件](https://www.runoob.com/event-pagecontainerbeforeload.html) **













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
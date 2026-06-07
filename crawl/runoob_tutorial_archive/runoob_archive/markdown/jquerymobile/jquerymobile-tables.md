# jQuery Mobile 表格

- Source: https://www.runoob.com/jquerymobile/jquerymobile-tables.html

---


## 响应式表格


响应式设计一般用于适配用户各种移动设备。


我们只需要使用一个简单的类名，jQuery Mobile 就能根据屏幕的尺寸自动调整页面内容。


响应式表格让页面内容在移动端和桌面设备上能够很好的适配。


响应式表格有两种类型： **reflow(回流)** 与 **列切换**。


---


## 回流表格


回流模型表格在屏幕尺寸足够大时是水平显示，而在屏幕尺寸达到足够小时，所有的数据会变成垂直显示。


创建表格，在  元素上添加 data-role="table" 和 "ui-responsive" 类:


## 实例



```javascript
<table data-role="table" class="ui-responsive">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_tables_reflow)


|  | 对于响应式表格，你必须包含 和 元素。不要使用 rowspan 或 colspan 属性; 响应式表格中是不支持这两个属性的。 |
| --- | --- |


---


## 列切换


列切换模型会在宽度不够时隐藏数据。


列切换的表格创建方式如下：


```
<table data-role="table" data-mode="columntoggle" class="ui-responsive" id="myTable">
```


默认情况下，jQuery Mobile 会先隐藏表格右侧的列。但是，你可以在表格头部()通过添加 data-priority 属性指定隐藏列的顺序，data-priority 的值可以是 1 (最高优先级) 到 6 (最低优先级):


```
<th>I will never be hidden</th>
<th data-priority="1">我是非常重要的列 - 我不会被隐藏</th>
<th data-priority="3">我是重要的列 - 我可能被隐藏</th>
<th data-priority="5">我是不怎么重要的列 - 我最先被隐藏</th>
```


|  | 如果你没为列指定优先级，则列会一直存在，不会被隐藏。 |
| --- | --- |


把上面的两段代码组合起来即可创建一个列切换的表格，这样用户就可以自定义要隐藏表格的哪些列：


## 实例



```javascript
<table data-role="table"
	data-mode="columntoggle" class="ui-responsive"
		id="myTable">
		<thead>    <tr>      <th
		data-priority="6">CustomerID</th>      <th>CustomerName</th>
		<th data-priority="1">ContactName</th>
		<th data-priority="2">Address</th>      <th
		data-priority="3">City</th>      <th
		data-priority="4">PostalCode</th>      <th
		data-priority="5">Country</th>    </tr>  </thead>
		<tbody>    <tr>      <td>1</td>      <td>Alfreds
		Futterkiste</td>      <td>Maria Anders</td>
		      <td>Obere Str. 57</td>

		<td>Berlin</td>      <td>12209</td>      <td>Germany</td>    </tr>
		</tbody></table>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_tables_columntoggle)


我们可以使用 data-column-btn-text 属性来修改切换表格的文本：


## 实例



```javascript
<table data-role="table"
	data-mode="columntoggle" class="ui-responsive"
		data-column-btn-text="点我显示或隐藏列!"
		id="myTable">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_tables_btntext)


---


## 表格样式


我们使用 "ui-shadow" 类来为表格添加阴影：


## 添加阴影



```javascript
<table data-role="table"
	data-mode="columntoggle" class="ui-responsive ui-shadow"
		id="myTable">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_tables_shadow)


使用 CSS 来进一步设置表格样式:


## 为所有行添加底部边框



```javascript
<style>tr {    border-bottom: 1px solid #d6d6d6;}
		</style>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_tables_border)


## 为 元素添加按钮及为偶数行添加背景



```javascript
<style>th {    border-bottom: 1px solid
		#d6d6d6;}tr:nth-child(even) {    background: #e9e9e9;}
		</style>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_tables_bgcolor)









	  AI 思考中...





			** [jQuery Mobile 面板](https://www.runoob.com/jquerymobile-panels.html)
			[jQuery Mobile 过滤](https://www.runoob.com/jquerymobile-filters.html) **













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
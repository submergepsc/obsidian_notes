# jQuery Mobile 表单

- Source: https://www.runoob.com/jquerymobile/jquerymobile-form-basic.html

---


jQuery Mobile 会自动为 HTML 表单自动添加样式，让它们看起来更具吸引力，触摸起来更具友好性。


---

*
**
---


## jQuery Mobile 表单结构


jQuery Mobile 使用 CSS 为 HTML 表单元素添加样式，让它们更具吸引力，更易于使用。


在 jQuery Mobile 中，您可以使用下列表单控件：


- 文本输入框
- 搜索输入框
- 单选按钮
- 复选框
- 选择菜单
- 滑动条
- 翻转拨动开关


当使用 jQuery Mobile 表单时，您应当知道：


-  元素必须有一个 method 和一个 action 属性
- 每个表单元素必须有一个唯一的 "id" 属性。id 必须是整个站点所有页面上唯一的。这是因为 jQuery Mobile 的单页导航机制使得多个不同页面在同一时间被呈现
- 每个表单元素必须有一个标签。设置标签的 **for** 属性来匹配元素的 id


## 实例



```javascript
<form method="post" action="demoform.html">  <label for="fname">姓名:</label>  <input
	type="text" name="fname" id="fname"></form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_label)


如需隐藏标签，请使用 class ui-hidden-accessible。这在您把元素的 placeholder 属性作为标签时经常用到：


## 实例



```javascript
<form method="post" action="demoform.html">  <label for="fname"
		class="ui-hidden-accessible">姓名:</label>  <input
		type="text" name="fname" id="fname" placeholder="姓名...">
		</form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_label_placeholder)


提示：** 我们可以使用 data-clear-btn="true" 属性来添加清除输入框内容的按钮 (一个在输入框右侧的 X 图标):



## 实例


```javascript
<label for="fname">姓名:</label><input type="text" name="fname"
	id="fname" data-clear-btn="true">
```

 **[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_clear)


|  | 清除输入框的按钮可以在 元素中使用，但不能在 中使用。 搜索框中 data-clear-btn 默认值为 "true" ，你可以使用 data-clear-btn="false" 移除该图标。 |
| --- | --- |


---


## jQuery Mobile 表单图标


表单中的按钮代码是标准的 HTML  元素 (button, reset, submit)。他们会自动渲染样式，可以自动适配移动设备与桌面设备：


## 实例


```javascript
<input type="button" value="按钮"><input type="reset" value="重置按钮"><input type="submit" value="提交按钮">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_buttons)


如果需要在  按钮中添加额外的样式，可以使用下表中的 data-* 属性：



| 属性 | 值 | 描述 |
| --- | --- | --- |
| data-corners | true \| false | 指定按钮是否有圆角 |
| data-icon | 图标参考手册 | 指定按钮图标 |
| data-iconpos | left \| right \| top \| bottom \| notext | 指定图标位置 |
| data-inline | true \| false | 指定是否内联按钮 |
| data-mini | true \| false | 指定是否为迷你按钮 |
| data-shadow | true \| false | 指定按钮是否添加阴影效果 |


## 按钮添加图标：


```javascript
<input type="button" value="按钮"><input type="reset" value="重置按钮"><input type="submit" value="提交按钮">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_buttons2)

---


## 字段容器


如需让标签和表单元素看起来更适应宽屏，请用带有 "ui-field-contain" 类的  或  元素包围 label/form 元素：


## 实例


```javascript
<form method="post" action="demoform.php">
	<div class="ui-field-contain">
	<label for="fname">姓:</label>    <input
	type="text" name="fname" id="fname">    <label for="lname">姓:</label>    <input type="text" name="lname" id="lname">
	  </div>
	</form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_fieldcontain)


|  | ui-field-contain 类基于页面的宽度为标签和表单控件添加样式。当页面的宽度大于 480px 时，它会自动把标签放置在与表单控件同一线上。当页面的宽度小于 480px 时，标签会被放置在表单元素的上面。 |
| --- | --- |


提示：**为了防止 jQuery Mobile 为可点击元素自动添加样式，请使用 data-role="none" 属性：


## 实例


```javascript
<label for="fname">姓名:</label><input type="text" name="fname"
	id="fname" data-role="none">
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_none)


|  | jQuery Mobile 中的表单提交jQuery Mobile 通过 AJAX 自动处理表单提交，并将试图集成服务器响应到应用程序的 DOM 中。 |
| --- | --- |








	  AI 思考中...





			* [jQuery Mobile 触摸事件](https://www.runoob.com/jquerymobile-events-touch.html)
			[jQuery Mobile 表单输入](https://www.runoob.com/jquerymobile-form-inputs.html) **













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
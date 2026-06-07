# jQuery Mobile 表单输入元素

- Source: https://www.runoob.com/jquerymobile/jquerymobile-form-inputs.html

---


## jQuery Mobile 文本输入框


输入字段是通过标准的 HTML 元素编码的，jQuery Mobile 将为它们添加样式使其看起来更具吸引力，在移动设备上更易使用。您也能使用新的 HTML5 的  类型：


## 实例


```javascript
<form method="post" action="demo_form.php">  <div class="ui-field-contain">
	<label for="fullname">全名:</label>    <input
	type="text" name="fullname" id="fullname">    <label
	for="bday">生日:</label>    <input type="date" name="bday"
	id="bday">    <label for="email">E-mail:</label>
	<input type="email" name="email" id="email" placeholder="你的电子邮箱..">
	</div></form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_inputs)


提示：**请使用 placeholder 来指定一个简短的描述，用来描述输入字段的期望值：


```
<input placeholder="sometext">
```


---


## 文本域


对于多行文本输入可使用  。


**注意：**当您键入一些文本时，文本域会自动调整大小以适应新增加的行。


## 实例


```javascript
<form method="post" action="demo_form.php">  <div class="ui-field-contain">
	<label for="info">附加信息:</label>    <textarea
	name="addinfo" id="info"></textarea>  </div></form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_textarea)


---


## 搜索输入框


type="search" 类型的输入框是在 HTML5 中新增的，它是为输入搜索定义文本字段：


## 实例



```javascript
<form method="post" action="demo_form.php">  <div class="ui-field-contain">
		<label for="search">搜索:</label>    <input
		type="search" name="search" id="search">  </div></form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_search)


---


## 单选按钮


当用户在有限数量的选择中仅选取一个选项时，使用单选按钮。


为了创建一系列单选按钮，请添加带有 type="radio" 的 input 以及相应的 label。把单选按钮包围在  元素内。您也可以添加一个  元素来定义  的标题。


提示：**请使用 data-role="controlgroup" 来把按钮组合在一起：


## 实例


```javascript
<form method="post" action="demo_form.php">  <fieldset
	data-role="controlgroup">    <legend>Choose your
	gender:</legend>      <label
	for="male">Male</label>      <input
	type="radio" name="gender" id="male" value="male">
	<label for="female">Female</label>      <input
	type="radio" name="gender" id="female" value="female">   </fieldset>
	</form>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_radio)


---


## 复选框


当用户在有限数量的选择中选取一个或多个选项时，使用复选框：


## 实例


```javascript
<form method="post" action="demo_form.php">  <fieldset
	data-role="controlgroup">    <legend>Choose as many
	favorite colors as you'd like:</legend>
	<label for="red">Red</label>      <input
	type="checkbox" name="favcolor" id="red" value="red">
	<label for="green">Green</label>      <input
	type="checkbox" name="favcolor" id="green" value="green">
	<label for="blue">Blue</label>      <input
	type="checkbox" name="favcolor" id="blue" value="blue">   </fieldset></form>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_checkbox)


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


如需水平组合单选按钮或复选框，请使用 data-type="horizontal"：


## 实例


```javascript
<fieldset data-role="controlgroup" data-type="horizontal">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_horizontal)


您也可以用一个 field 容器包围 ：


## 实例


```javascript
<div class="ui-field-contain">
	<fieldset data-role="controlgroup">
		<legend>请选择您的性别:</legend>
	</fieldset></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_radio_check_fieldcontain)


如果您想要您的按钮中的一个预先选中，请使用 HTML 中  的 checked 属性：


## 实例


```javascript
<input type="radio" checked><input type="checkbox" checked>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_checked)


你可以将表单放在弹窗中：


## 实例


```javascript
<a href="#myPopup" data-rel="popup" class="ui-btn ui-btn-inline">Show Popup Form</a><div
		data-role="popup" id="myPopup" class="ui-content">  <form method="post" action="demoform.php">
		<div>      <h3>登录信息</h3>
		<label for="usrnm" class="ui-hidden-accessible">用户名:</label>
		<input type="text" name="user" id="usrnm" placeholder="用户名">
		<label for="pswd" class="ui-hidden-accessible">密码:</label>
		<input type="password" name="passw" id="pswd" placeholder="密码">
		</div>  </form></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_forms_popup)







	  AI 思考中...





			** [jQuery Mobile 表单](https://www.runoob.com/jquerymobile-form-basic.html)
			[jQuery Mobile 表单选择](https://www.runoob.com/jquerymobile-form-select.html) **













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
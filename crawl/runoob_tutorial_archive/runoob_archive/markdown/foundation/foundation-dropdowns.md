# Foundation 下拉菜单

- Source: https://www.runoob.com/foundation/foundation-dropdowns.html

Foundation 下拉菜单允许用户从预定义的下拉列表中选取一个值：


### 实例


```
<!-- Trigger the Dropdown --><a href="#" data-dropdown="id01" class="button dropdown">Dropdown Button</a>
	<!-- Dropdown content --><ul id="id01" data-dropdown-content class="f-dropdown">  <li><a
	href="#">Link 1</a></li>  <li><a href="#">Link 2</a></li>
	<li><a href="#">Link 3</a></li></ul>
	<!-- Initialize Foundation JS --><script>
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_dropdown)


### 实例解析


`.dropdown` 类为按钮添加一个向下的箭头符号"图标。


使用按钮或链接的 `data-dropdown="*id*"` 属性来打开下拉菜单。


*id* 值需要与下拉菜单的内容 (id01) 匹配。


在 , , `` 中添加 `.f-dropdown` 类和 `data-dropdown-content` 属性来创建下拉菜单的内容。


最后初始化 Foundation JS。


注意:** 在小屏幕上，所有的下拉菜单的宽度是100%。


---


## 下拉菜单尺寸


使用 `.tiny`, `.small`, `.medium`, `.large` 或 `.mega` 来修改下拉菜单的宽度。


**注意:** 在小屏幕上，所有的下拉菜单的宽度是100%。


### 实例


```
<!-- Tiny Dropdown:
	max-width is 200px -->
	<ul id="id01" data-dropdown-content class="f-dropdown
	tiny">..<!-- Small Dropdown: max-width is 300px -->
	<ul id="id02" data-dropdown-content class="f-dropdown
	small">..<!-- Medium Dropdown: max-width is 500px -->
	<ul id="id03" data-dropdown-content class="f-dropdown
	medium"><!-- Large Dropdown: max-width is 800px -->
	<ul id="id04" data-dropdown-content class="f-dropdown
	large">..<!--
	Mega Dropdown: 100% width -->
	<ul id="id04" data-dropdown-content class="f-dropdown
	mega">..
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_dropdown_size)


---


## 下拉菜单边距


可以使用 `.content` 类为下拉菜单添加内边距：


### 实例


```
<!-- Default Dropdown --><ul id="id01" data-dropdown-content class="f-dropdown">..
	<!-- Dropdown with padding --><ul id="id02" data-dropdown-content class="f-dropdown
	content">..
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_dropdown_content)


---


## 其他实例


 下拉菜单中添加多媒体元素：


### 实例


```
<a href="#" data-dropdown="id01" class="button dropdown">Dropdown Button</a>
	<div id="id01" data-dropdown-content class="f-dropdown medium content">
	<h4>Paris Title</h4>  <p>Some text.. some text..</p>  <img
	src="paris.jpg" alt="Paris" width="400" height="300">  <p>Paris, je
	t'aime.</p></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_dropdown_content2)


---


## 下拉菜单方向


默认情况下下拉菜单在底部，可以通过添加 `data-options="align:left|right|top"` 来修改其方向：


### 实例


```
<a href="#" data-dropdown="id01" data-options="align:right" class="button
	dropdown">Right</a><a href="#" data-dropdown="id02" data-options="align:top"
	class="button dropdown">Top</a><a href="#" data-dropdown="id03"
	data-options="align:bottom" class="button dropdown">Bottom</a><a href="#"
	data-dropdown="id04" data-options="align:left" class="button
	dropdown">Left</a>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_dropdown_directions)


---


## 下拉菜单触发条件


默认情况下，下拉菜单在点击按钮后显示。如果你需要在鼠标移动上去后显示，可以在按钮上使用 `data-options="is_hover:true"` 属性:


### 实例


```
<a href="#" data-dropdown="id01" data-options="is_hover:true" class="button dropdown">Hover
	over me</a>
	<ul id="id01" data-dropdown-content class="f-dropdown">  <li><a
	href="#">Link 1</a></li>  <li><a href="#">Link 2</a></li>
	<li><a href="#">Link 3</a></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_dropdown_hover)


---


## 分割按钮


我们可以在按钮上添加 `.split` 类来设置一个分割效果的按钮，分割后会在  元素上生成一个方向向下的图标按钮:


### 实例


```
<button class="button split">Split Button   <span
	data-dropdown="id01"></span></button><ul id="id01" data-dropdown-content
	class="f-dropdown">  <li><a href="#">Link 1</a></li>
	<li><a href="#">Link 2</a></li>  <li><a href="#">Link 3</a></li>
	</ul>
	<!-- Initialize Foundation JS --><script>
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_button_split)








	  AI 思考中...





			** [Foundation 图片](https://www.runoob.com/foundation-images.html)
			[Foundation 折叠列表](https://www.runoob.com/foundation-collapse.html) **













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
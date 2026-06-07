# Foundation 按钮组

- Source: https://www.runoob.com/foundation/foundation-button-groups.html

---

## 按钮组


Foundation 可以在同一行内创建一系列的按钮。

可以使用 `` 元素并添加 `.button-group` 类来创建按钮组：


### 实例


```
<ul class="button-group">  <li><button type="button"
	class="button">Apple</button></li>  <li><button type="button"
	class="button">Samsung</button></li>  <li><button type="button"
	class="button">Sony</button></li></ul>
```

**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_button_group)

---


## 垂直按钮组


垂直按钮组使用 `.stack` 类来创建。注意，按钮会跨越父元素的整个宽度:


### 实例


```
<ul class="button-group stack">  <li><button type="button"
	class="button">Apple</button></li>  <li><button type="button"
	class="button">Samsung</button></li>  <li><button type="button"
	class="button">Sony</button></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_button_group_stack)


`.stack-for-small` 类用于小尺寸的屏幕，按钮有水平排列变为垂直排列：


### 实例


```
<ul class="button-group stack-for-small">  <li><button type="button"
	class="button">Apple</button></li>  <li><button type="button"
	class="button">Samsung</button></li>  <li><button type="button"
	class="button">Sony</button></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_button_group_stack2)


---


## 圆角按钮组


按钮组中使用 `.radius` 和 `.round` 类为按钮添加圆角效果：


### 实例


```
<ul class="button-group radius">
	<li><button type="button" class="button">Apple</button></li>
	<li><button type="button" class="button">Samsung</button></li>
	<li><button type="button" class="button">Sony</button></li></ul><ul class="button-group round">  <li><button
	type="button" class="button">Apple</button></li>  <li><button
	type="button" class="button">Samsung</button></li>  <li><button
	type="button" class="button">Sony</button></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_button_group_rounded)


---


## 均匀延展按钮组


`.even-num` 类用于在按钮组中均匀的分配按钮的宽度并跨越父元素 100% 宽度。


*num* 为按钮组中按钮的数量，从 1 到 8：


### 实例


```
<ul class="button-group even-3">  <li><button type="button"
	class="button">Apple</button></li>  <li><button type="button"
	class="button">Samsung</button></li>  <li><button type="button"
	class="button">Sony</button></li></ul><ul class="button-group
	even-5">  <li><button type="button"
	class="button">Apple</button></li>  <li><button type="button"
	class="button">Samsung</button></li>  <li><button type="button"
	class="button">Sony</button></li>  <li><button type="button"
	class="button">HTC</button></li>  <li><button type="button"
	class="button">Huawei</button></li></ul><ul class="button-group
	even-8">  <li><button type="button" class="button">A</button></li>
	<li><button type="button" class="button">B</button></li>
	<li><button type="button" class="button">C</button></li>
	<li><button type="button" class="button">D</button></li>
	<li><button type="button" class="button">E</button></li>
	<li><button type="button" class="button">F</button></li>
	<li><button type="button" class="button">G</button></li>
	<li><button type="button" class="button">H</button></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_button_group_even)


---


## 下拉菜单按钮


下拉菜单按钮可以让用户选取设定好的值：


### 实例


```
<!-- Trigger the dropdown --><a href="#" data-dropdown="id01" class="button dropdown">Dropdown Button</a>
	<!-- The actual dropdown --><ul id="id01" data-dropdown-content class="f-dropdown">  <li><a
	href="#">Link 1</a></li>  <li><a href="#">Link 2</a></li>
	<li><a href="#">Link 3</a></li></ul>
	<!-- Initialize Foundation JS --><script>
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_dropdown)


### 实例解析


`.dropdown` 类创建一个下拉菜单按钮。


使用带有 `data-dropdown="*id*"` 属性的按钮或链接打开下拉菜单。


*id* 值需要与下拉菜单的内容 (id01) 匹配。


在 `` 中添加 `.f-dropdown` 类和 `data-dropdown-content` 属性来创建下拉菜单的内容。


最后初始化 Foundation JS。


---


## 分割按钮


我们也可以创建一个分割按钮的下拉菜单。只需要在按钮中添加 `.split` 类并使用 span 元素生成一个方向箭的按钮：


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





			** [Foundation 按钮](https://www.runoob.com/foundation-buttons.html)
			[Foundation 图标](https://www.runoob.com/foundation-icons.html) **













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
# Foundation 顶部导航栏

- Source: https://www.runoob.com/foundation/foundation-topbar.html

顶部导航栏放在页面头部：

*


### 实例


```
<nav class="top-bar" data-topbar>  <ul class="title-area">
	<li class="name">      <!--
	如果你不需要标题或图标可以删掉它 -->      <h1><a href="#">WebSiteName</a></h1>
	</li>      <!-- 小屏幕上折叠按钮:
	去掉 .menu-icon 类，可以去除图标。
	如果需要只显示图片，可以删除 "Menu" 文本 -->    <li class="toggle-topbar menu-icon"><a href="#"><span>Menu</span></a></li>
	</ul>  <section class="top-bar-section">
	<ul class="left">      <li
	class="active"><a href="#">Home</a></li>
	<li><a href="#">Page 1</a></li>      <li><a
	href="#">Page 2</a></li>      <li><a href="#">Page
	3</a></li>     </ul>  </section></nav>
	<!-- 初始化 Foundation JS -->
	<script>
	$(document).ready(function() {
	$(document).foundation();})
	</script>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar)


### 实例解析


使用 `` 创建标准工具条。 `.title-area` 类定义了网站logo区域 (必须防止 `li.name` 内) 。屏幕变小后你就可以看到一个 "menu" 按钮。 Foundation 的菜单会根据屏幕尺寸自动折叠和延展：


小屏幕上，由于尺寸的原因很多选项会被隐藏。 `li.toggle-topbar menu.icon` 类创建了一个菜单的按钮，点击它可以显示被隐藏的选项。 提示:** 重置浏览器窗口查看效果。


`.top-bar-section` 定义了导航的链接部分。 `.left` 类指定链接左对齐。 `.active` 类用于显示选中的项，背景为蓝色。


**提示:** 如果你想导航链接右对齐可以将 `.left` 修改为 `.right` :


### 实例


```
<section class="top-bar-section">  <ul class="right">...
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_right)


你可以同时设置左边对齐与右边对齐：


### 实例


```
<section class="top-bar-section">  <ul
		class="left">    <li class="active"><a href="#">Home</a></li>
		<li><a href="#">Page 1</a></li>    <li><a href="#">Page
		2</a></li>  </ul>  <ul class="right">
		<li><a href="#">Sign Up</a></li>    <li><a href="#">Login</a></li>
		</ul></section>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_left_right)


导航栏可以通过 `.divider` 类来添加分割线 (大屏幕上是垂直的线，小屏幕上是水平线):


### 实例


```
<ul class="left">  <li class="active"><a href="#">Home</a></li>
	<li class="divider"></li>  <li><a href="#">Page 1</a></li>
	<li class="divider"></li>  <li><a href="#">Page 2</a></li>
	<li class="divider"></li>  <li><a href="#">Page 3</a></li>
	<li class="divider"></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_divider)


---


## 导航栏的下拉菜单


顶部导航栏可以设置下拉菜单。


可以通过在 `` 元素上添加 `.has-dropdown` 类来设置下拉菜单:


### 实例


```
<section class="top-bar-section">  <ul class="left">
	<li class="active"><a href="#">Home</a></li>    <li
	class="has-dropdown">      <a href="#">Dropdown</a>
	<ul class="dropdown">        <li><a
	href="#">First link in dropdown</a></li>
	<li><a href="#">Second link in dropdown</a></li>
	<li class="active"><a href="#">Active link in dropdown</a></li>
	</ul>    </li>  </ul></section>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_dropdown)


### 分割线


使用 `.divider` 类来设置下拉菜单的分割线:


### 实例


```
<ul class="dropdown">  <li><a href="#">Apple</a></li>
	<li><a href="#">Banana</a></li>  <li><a href="#">Orange</a></li>
	<li class="divider"></li>  <li><a href="#">Kale</a></li>  <li><a href="#">Spinach</a></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_dropdown_divider)


---


## 下拉菜单标签


在 `` 内添加 `` 元素来设置下拉菜单的标签(标题):


### 实例


```
<ul class="dropdown">  <li><label>Fruit</label></li>
	<li><a href="#">Apple</a></li>  <li><a href="#">Banana</a></li>
	<li><a href="#">Orange</a></li>
	<li class="divider"></li>  <li><label>Vegetable</label></li>
	<li><a href="#">Kale</a></li>  <li><a href="#">Spinach</a></li>
	</ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_dropdown_label)


### 内嵌下拉菜单


下拉菜单可以再嵌入一个下拉菜单：


### 实例


```
<section class="top-bar-section">  <ul class="left">
	<li class="has-dropdown">      <a href="#">Dropdown</a>
	<ul class="dropdown">
	<li><label>Level 1</label></li>
	<li><a href="#">Link</a></li>
	<li><a href="#">Link</a></li>
	<li class="has-dropdown">
	<a href="#">New dropdown</a>
	<ul class="dropdown">
	<li><label>Level 2</label></li>
	<li><a href="#">2nd level dropdown</a></li>
	<li><a href="#">2nd level dropdown</a></li>
	<li class="has-dropdown">
	<a href="#">New dropdown</a>
	<ul class="dropdown">
	<li><label>Level 3</label></li>
	<li><a href="#">3rd level dropdown</a></li>
	<li><a href="#">3rd level dropdown</a></li>
	</ul>
	</li>          </ul>
	</li>      </ul>    </li>
	</ul></section>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_dropdown_nested)

### 可点击


默认情况下导航栏的下拉菜单在鼠标移动过去后显示，我们可以使用 `data-options="is_hover: false"` 属性来设置导航栏在鼠标在点击后显示:


### 实例


```
<nav class="top-bar" data-topbar data-options="is_hover: false">
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_dropdown_click)


---


## 导航栏上的按钮及图标


你可以在导航栏上放置图标和按钮：


### 实例


```
<li><a href="#" class="button">Button Link</a></li>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_button)


你可以在导航栏上放上图标，更多图片样式可以查看 [Foundation 图标教程](https://www.runoob.com/foundation-icons.html):


### 实例


```
<head><!--  Foundation 图标样式 --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/[email protected]/foundation-icons.min.css">
		</head><ul class="left">  <li class="active"><a href="#"><i
		class="fi-home"></i> Home</a></li>  <li><a href="#"><i
		class="fi-torso"></i> Sign Up</a></li>  <li><a href="#"><i
		class="fi-magnifying-glass"></i> Search</a></li> </ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_icons)


---


## 固定导航栏


导航栏可以固定在页面顶部。


页面滚动时导航栏在顶部是不会动的。


要固定导航栏只需要将导航栏放在 `` 内即可:


### 实例


```
<div class="fixed">
	<nav class="top-bar" data-topbar>    ...  </nav>
	</div>
```




[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_fixed)


---


## 导航栏绝对定位


我们可以将导航栏放在 `` 内来设置导航栏的绝对定位，当滚动条滚到到该区域时，该导航栏就像固定导航栏一样在顶部不动:


### 实例


```
<div class="sticky">
	<nav class="top-bar" data-topbar>    ...  </nav>
	</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_topbar_sticky)


当你使用 `.sticky` 类时，顶部导航栏在所有屏幕尺寸上将固定不动。如果你需要在指定屏幕上设定只需要在 `` 上添加 `data-options="sticky_on: small|medium|large"` 属性即可：


### 实例


```
<div class="sticky">  <!-- 只有在大屏幕上 -->
	<nav class="top-bar" data-topbar data-options="sticky_on: large">
	..   </nav></div>
```


或者通过数组设置多个屏幕尺寸：


### 实例


```
<div class="sticky">  <!-- 小屏幕和大屏幕 (没有中等屏幕)-->
	<nav class="top-bar" data-topbar data-options="sticky_on:
	[small, large]">
	..   </nav></div>
```










	  AI 思考中...





			* [Foundation 价格表](https://www.runoob.com/foundation-pricing-tables.html)
			[Foundation 侧边栏](https://www.runoob.com/foundation-sidenav.html) **













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
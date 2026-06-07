# Bootstrap4 导航

- Source: https://www.runoob.com/bootstrap4/bootstrap4-navs.html

如果你想创建一个简单的水平导航栏，可以在 **** 元素上添加 **.nav**类，在每个 **** 选项上添加 **.nav-item** 类，在每个链接上添加 **.nav-link** 类:


## 实例


```css
<ul class="nav">
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" href="#">Disabled</a>
  </li>
</ul>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav)

---


## 导航对齐方式


**.justify-content-center** 类设置导航居中显示， **.justify-content-end** 类设置导航右对齐。


## 实例


```css
<!-- 导航居中 -->
<ul class="nav justify-content-center">

<!-- 导航右对齐 -->
<ul class="nav justify-content-end">
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav_align)

---


## 垂直导航


**.flex-column** 类用于创建垂直导航：


## 实例


```css
<ul class="nav flex-column">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav_vertical)


---


## 选项卡


使用 **.nav-tabs** 类可以将导航转化为选项卡。然后对于选中的选项使用 .active 类来标记。


## 实例


```css
<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" href="#">Disabled</a>
  </li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav_tabs)


---


## 胶囊导航


**.nav-pills** 类可以将导航项设置成胶囊形状。


## 实例


```css
<ul class="nav nav-pills">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" href="#">Disabled</a>
  </li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav_pills)


---


## 导航等宽


**.nav-justified** 类可以设置导航项齐行等宽显示。


## 实例


```css
<ul class="nav nav-pills nav-justified">..</ul>
<ul class="nav nav-tabs nav-justified">..</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav_justified)


---


## 胶囊下拉菜单


## 实例


```css
<ul class="nav nav-pills">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#">Dropdown</a>
    <div class="dropdown-menu">
      <a class="dropdown-item" href="#">Link 1</a>
      <a class="dropdown-item" href="#">Link 2</a>
      <a class="dropdown-item" href="#">Link 3</a>
    </div>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" href="#">Disabled</a>
  </li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav_pills_dropdown)


---


## 选项卡下拉菜单


## 实例


```css
<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" href="#">Active</a>
  </li>
  <li class="nav-item dropdown">
    <a class="nav-link dropdown-toggle" data-toggle="dropdown" href="#">Dropdown</a>
    <div class="dropdown-menu">
      <a class="dropdown-item" href="#">Link 1</a>
      <a class="dropdown-item" href="#">Link 2</a>
      <a class="dropdown-item" href="#">Link 3</a>
    </div>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="#">Link</a>
  </li>
  <li class="nav-item">
    <a class="nav-link disabled" href="#">Disabled</a>
  </li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav_tabs_dropdown)


---


## 动态选项卡


如果你要设置选项卡是动态可切换的，可以在每个链接上添加 **data-toggle="tab"** 属性。 然后在每个选项对应的内容的上添加 **.tab-pane** 类，对应选项卡内容的 **** 元素使用 **.tab-content** 类 。。


如果你希望有淡入效果可以在 **.tab-pane** 后添加 ** .fade**类:


## 实例


```css
<!-- Nav tabs -->
<ul class="nav nav-tabs">
  <li class="nav-item">
    <a class="nav-link active" data-toggle="tab" href="#home">Home</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" data-toggle="tab" href="#menu1">Menu 1</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" data-toggle="tab" href="#menu2">Menu 2</a>
  </li>
</ul>

<!-- Tab panes -->
<div class="tab-content">
  <div class="tab-pane active container" id="home">...</div>
  <div class="tab-pane container" id="menu1">...</div>
  <div class="tab-pane container" id="menu2">...</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav_tabs_toggleable)


---


## 胶囊状动态选项卡


胶囊状动态选项卡只需要将以上实例的代码中 data-toggle 属性设置为 **data-toggle="pill"**:


## 实例


```css
<!-- Nav pills -->
<ul class="nav nav-pills">
  <li class="nav-item">
    <a class="nav-link active" data-toggle="pill" href="#home">Home</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" data-toggle="pill" href="#menu1">Menu 1</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" data-toggle="pill" href="#menu2">Menu 2</a>
  </li>
</ul>

<!-- Tab panes -->
<div class="tab-content">
  <div class="tab-pane active container" id="home">...</div>
  <div class="tab-pane container" id="menu1">...</div>
  <div class="tab-pane container" id="menu2">...</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_nav_pills_toggleable)










	  AI 思考中...





			** [Bootstrap4 折叠](https://www.runoob.com/bootstrap4-collapse.html)
			[Bootstrap4 导航栏](https://www.runoob.com/bootstrap4-navbar.html) **













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
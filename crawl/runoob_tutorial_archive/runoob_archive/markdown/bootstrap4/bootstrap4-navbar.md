# Bootstrap4 导航栏

- Source: https://www.runoob.com/bootstrap4/bootstrap4-navbar.html

导航栏一般放在页面的顶部。


我们可以使用 **.navbar** 类来创建一个标准的导航栏，后面紧跟: **.navbar-expand-xl|lg|md|sm** 类来创建响应式的导航栏 (大屏幕水平铺开，小屏幕垂直堆叠)。


导航栏上的选项可以使用 **** 元素并添加 **class="navbar-nav"** 类。 然后在 **** 元素上添加 **.nav-item** 类， **** 元素上使用 **.nav-link** 类:


## 实例


```css
<!-- 小屏幕上水平导航栏会切换为垂直的 -->
<nav class="navbar navbar-expand-sm bg-light">

  <!-- Links -->
  <ul class="navbar-nav">
    <li class="nav-item">
      <a class="nav-link" href="#">Link 1</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Link 2</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Link 3</a>
    </li>
  </ul>

</nav>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar)

---


## 垂直导航栏


通过删除 **.navbar-expand-xl|lg|md|sm** 类来创建垂直导航栏:


## 实例


```css
<!-- 垂直导航栏 -->
<nav class="navbar bg-light">

  <!-- Links -->
  <ul class="navbar-nav">
    <li class="nav-item">
      <a class="nav-link" href="#">Link 1</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Link 2</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Link 3</a>
    </li>
  </ul>

</nav>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_vertical)


---


## 居中对齐的导航栏


通过添加 **.justify-content-center** 类来创建居中对齐的导航栏:


## 实例


```css
<nav class="navbar navbar-expand-sm bg-light justify-content-center">
  ...
</nav>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_centered)


---


## 不同颜色导航栏


可以使用以下类来创建不同颜色导航栏：**.bg-primary**, ** .bg-success**, **.bg-info**, **.bg-warning**, **.bg-danger**, **.bg-secondary**, **.bg-dark** 和 **.bg-light**)。


提示:** 对于暗色背景需要设置文本颜色为浅色的，对于浅色背景需要设置文本颜色为深色的。


## 实例


```css
<!-- 灰底黑字 -->
<nav class="navbar navbar-expand-sm bg-light navbar-light">
  <ul class="navbar-nav">
    <li class="nav-item active">
      <a class="nav-link" href="#">Active</a>
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
</nav>

<!-- 黑底白字 -->
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">...</nav>

<!-- 蓝底白字 -->
<nav class="navbar navbar-expand-sm bg-primary navbar-dark">...</nav>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_color)


激活和禁用状态**: 可以在 **** 元素上添加 **.active** 类来高亮显示选中的选项。 **.disabled** 类用于设置该链接是不可点击的。


---


## 品牌/Logo


**.navbar-brand** 类用于高亮显示品牌/Logo:


## 实例


```css
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <a class="navbar-brand" href="#">Logo</a>
  ...
</nav>
```


**[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_brand)


可以使用 **.navbar-brand** 类来设置图片自适应导航栏。


## 实例


```css
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
   <a class="navbar-brand" href="#">
    <img src="bird.jpg" alt="Logo" style="width:40px;">
  </a>
  ...
</nav>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_brand2)


---


## 折叠导航栏


通常，小屏幕上我们都会折叠导航栏，通过点击来显示导航选项。


要创建折叠导航栏，可以在按钮上添加 **class="navbar-toggler", data-toggle="collapse" 与 data-target="#*thetarget*"** 类。然后在设置了 **class="collapse navbar-collapse"** 类的 div 上包裹导航内容（链接）, div 元素上的 id 匹配按钮 **data-target** 的上指定的 id:


## 实例


```css
<nav class="navbar navbar-expand-md bg-dark navbar-dark">
  <!-- Brand -->
  <a class="navbar-brand" href="#">Navbar</a>

  <!-- Toggler/collapsibe Button -->
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#collapsibleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>

  <!-- Navbar links -->
  <div class="collapse navbar-collapse" id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Link</a>
      </li>
    </ul>
  </div>
</nav>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_navbar_collapse)


---


## 导航栏使用下拉菜单


导航栏上可以设置下拉菜单：


## 实例


```css
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <!-- Brand -->
  <a class="navbar-brand" href="#">Logo</a>

  <!-- Links -->
  <ul class="navbar-nav">
    <li class="nav-item">
      <a class="nav-link" href="#">Link 1</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Link 2</a>
    </li>

    <!-- Dropdown -->
    <li class="nav-item dropdown">
      <a class="nav-link dropdown-toggle" href="#" id="navbardrop" data-toggle="dropdown">
        Dropdown link
      </a>
      <div class="dropdown-menu">
        <a class="dropdown-item" href="#">Link 1</a>
        <a class="dropdown-item" href="#">Link 2</a>
        <a class="dropdown-item" href="#">Link 3</a>
      </div>
    </li>
  </ul>
</nav>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_dropdown)


---


## 导航栏的表单与按钮


导航栏的表单 **** 元素使用 **class="form-inline"** 类来排版输入框与按钮：


## 实例


```css
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <form class="form-inline">
    <input class="form-control" type="text" placeholder="Search">
    <button class="btn btn-success" type="submit">Search</button>
  </form>
</nav>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_form)

你也可以使用其他的输入框类，如 **.input-group-addon** 类用于在输入框前添加小标签。


## 实例


```css
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
  <form class="form-inline" action="/action_page.php">
    <div class="input-group">
      <div class="input-group-prepend">
        <span class="input-group-text">@</span>
      </div>
      <input type="text" class="form-control" placeholder="Username">
    </div>
  </form>
</nav>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_form_addon)


---


## 导航栏文本


使用 **.navbar-text** 类来设置导航栏上非链接文本，可以保证水平对齐，颜色与内边距一样。


## 实例


```css
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">

<!-- Links -->
  <ul class="navbar-nav">
    <li class="nav-item">
      <a class="nav-link" href="#">Link 1</a>
    </li>
    <li class="nav-item">
      <a class="nav-link" href="#">Link 2</a>
    </li>
  </ul>

  <!-- Navbar text-->
  <span class="navbar-text">
    Navbar text
  </span>

</nav>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_text)


---


## 固定导航栏


导航栏可以固定在头部或者底部。


我们使用 **.fixed-top** 类来实现导航栏的固定：


## 实例


```css
<nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
  ...
</nav>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_fixed)


**.fixed-bottom** 类用于设置导航栏固定在底部：


## 实例


```css
<nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-bottom">
  ...
</nav>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_navbar_fixed_bottom)










	  AI 思考中...





			** [Bootstrap4 导航](https://www.runoob.com/bootstrap4-navs.html)
			[Bootstrap4 表单](https://www.runoob.com/bootstrap4-forms.html) **













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
# Bootstrap5 下拉菜单

- Source: https://www.runoob.com/bootstrap5/bootstrap5-dropdowns.html

下拉菜单是可切换的，是以列表格式显示链接的上下文菜单。


## 实例


```css
<div class="dropdown">
  <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">
    下拉菜单按钮
  </button>
  <div class="dropdown-menu">
    <a class="dropdown-item" href="#">链接 1</a>
    <a class="dropdown-item" href="#">链接 2</a>
    <a class="dropdown-item" href="#">链接 3</a>
  </div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-menu)


### 实例解析


**.dropdown** 类用来指定一个下拉菜单。


我们可以使用一个按钮或链接来打开下拉菜单， 按钮或链接需要添加 **.dropdown-toggle** 和 **data-toggle="dropdown"** 属性。


**** 元素上添加 **.dropdown-menu** 类来设置实际下拉菜单，然后在下拉菜单的选项中添加 **.dropdown-item** 类。


---


## 下拉菜单中的分割线


**.dropdown-divider** 类用于在下拉菜单中创建一个水平的分割线：


## 实例


```css
<li><hr class="dropdown-divider"></hr></li>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-divider)


---


## 下拉菜单中的标题


**.dropdown-header** 类用于在下拉菜单中添加标题：


## 实例


```css
<li><h5 class="dropdown-header">标题 1</h5></li>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-header)

---


## 下拉菜单中的可用项与禁用项


.active 类会让下拉菜单的选项高亮显示 (添加蓝色背景)。


如果要禁用下拉菜单的选项，可以使用**.disabled** 类。


## 实例


```css
<a class="dropdown-item" href="#">常规项</a>
<a class="dropdown-item active" href="#">激活项</a>
<a class="dropdown-item disabled" href="#">禁用项</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-active)


---


## 下拉菜单的定位


如果我们想让下拉菜单右对齐，可以在元素上的 **.dropdown** 类后添加 **.dropend** 或 **.dropstart** 类。


**.dropend** 是右对齐， **.dropstart** 是左对齐。


## 实例


```css
<!-- 右对齐 -->
<div class="dropdown dropend">
...
</div>

<!-- 左对齐 -->
<div class="dropdown dropstart">
...
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-menu-right)

---


## 下拉菜单弹出方向设置


下拉菜单弹出方向默认为向下，当然我们也可以设置不同的方向。


### 指定向右弹出的下拉菜单


如果你希望下拉菜单向右下方弹出，可以在 div 元素上添加 **.dropdown-menu-end** 类:


## 实例


```css
<!-- 右下方拉菜单按钮 -->
<div class="dropdown dropdown-menu-end">
<button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">
  下拉菜单右下方弹出
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">链接 1</a></li>
    <li><a class="dropdown-item" href="#">链接 2</a></li>
    <li><a class="dropdown-item" href="#">链接 3</a></li>
  </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-menu-dropup-right)

### 指定向上弹出的上拉菜单


如果你希望上拉菜单向上弹出，可以在 div 元素上添加 **"dropup"** 类:


## 实例


```css
<!-- 向上菜单 -->
<div class="dropup">
  <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">
    下拉菜单
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">链接 1</a></li>
    <li><a class="dropdown-item" href="#">链接 2</a></li>
    <li><a class="dropdown-item" href="#">链接 3</a></li>
  </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-menu-dropup)

### 指定向左边弹出的下拉菜单


如果你希望下拉菜单向上弹出，可以在 div 元素上添加 **dropstart** 类:


## 实例


```css
<!-- 左边的下拉菜单 -->
<div class="dropstart">
  添加一些内容，用于测试向左边弹出效果。<button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">
  下拉菜单
  </button>
  <ul class="dropdown-menu">
    <li><a class="dropdown-item" href="#">链接 1</a></li>
    <li><a class="dropdown-item" href="#">链接 2</a></li>
    <li><a class="dropdown-item" href="#">链接 3</a></li>
  </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-menu-dropleft)


---


## 下拉菜单设置文本


**.dropdown-item-text** 类可以设置下拉菜单中的文本项：


## 实例


```css
<ul class="dropdown-menu">
  <li><a class="dropdown-item" href="#">链接 1</a></li>
  <li><a class="dropdown-item" href="#">链接 2</a></li>
  <li><a class="dropdown-item" href="#">链接 3</a></li>
  <li><a class="dropdown-item-text" href="#">文本链接</a></li>
  <li><span class="dropdown-item-text">仅仅是文本</span></li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-text)


---


## 按钮组中设置下拉菜单


我们可以在按钮中添加下拉菜单：


## 实例


```css
<div class="btn-group">
    <button type="button" class="btn btn-primary">Apple</button>
    <button type="button" class="btn btn-primary">Samsung</button>
    <div class="btn-group">
      <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">Sony</button>
      <ul class="dropdown-menu">
        <li><a class="dropdown-item" href="#">Tablet</a></li>
        <li><a class="dropdown-item" href="#">Smartphone</a></li>
      </ul>
    </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown-split)

垂直按钮组带下拉菜单：


## 实例


```css
<div class="btn-group-vertical">
  <button type="button" class="btn btn-primary">Apple</button>
  <button type="button" class="btn btn-primary">Samsung</button>
  <div class="btn-group">
    <button type="button" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown">Sony</button>
    <ul class="dropdown-menu">
      <li><a class="dropdown-item" href="#">Tablet</a></li>
      <li><a class="dropdown-item" href="#">Smartphone</a></li>
    </ul>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_button_group_v_dropdown-split)


---


## 导航栏案例


## 实例


```css

```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_dropdown_example)










	  AI 思考中...





			** [Bootstrap5 卡片](https://www.runoob.com/bootstrap5-cards.html)
			[Bootstrap5 折叠](https://www.runoob.com/bootstrap5-collapse.html) **













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
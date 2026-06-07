# Bootstrap4 下拉菜单

- Source: https://www.runoob.com/bootstrap4/bootstrap4-dropdowns.html

Bootstrap 4 下拉菜单（Dropdown） 是一个非常常见的 UI 组件，用于展示一系列可点击的选项或菜单项。


Bootstrap4 下拉菜单通常用于导航栏、表单或其他交互式界面中。


### 基本结构


Bootstrap 4 下拉菜单的核心是 **.dropdown** 类，它可以嵌套其他元素（如按钮、链接或文本）来触发菜单的显示。菜单项本身使用 .dropdown-menu 类来进行标识，具体选项使用 .dropdown-item 类。


Bootstrap4 下拉菜单依赖于 **popper.min.js**。


样式类说明：


| 类名 | 说明 | 示例用法 |
| --- | --- | --- |
| .dropdown | 下拉菜单的容器类，包裹按钮和菜单。 | ... |
| .dropdown-toggle | 用于创建触发下拉菜单的按钮，通常结合 .btn 类使用。 | ... |
| data-toggle="dropdown" | 使按钮或链接触发下拉菜单的显示和隐藏。 | Dropdown button |
| .dropdown-menu | 下拉菜单的容器类，包含菜单项。 | ... |
| .dropdown-item | 下拉菜单中的菜单项，通常是一个链接。 | Item |
| aria-haspopup="true" | 增加无障碍支持，指示该元素有一个弹出菜单。 | Dropdown |
| aria-expanded="false" | 增加无障碍支持，指示菜单的当前状态（展开或折叠）。 | Dropdown |


下拉菜单是可切换的，是以列表格式显示链接的上下文菜单。


## 实例


```css
<div class="dropdown">
  <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
    Dropdown button
  </button>
  <div class="dropdown-menu">
    <a class="dropdown-item" href="#">Link 1</a>
    <a class="dropdown-item" href="#">Link 2</a>
    <a class="dropdown-item" href="#">Link 3</a>
  </div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_dropdown-menu)


### 实例解析


**.dropdown** 类用来指定一个下拉菜单。


我们可以使用一个按钮或链接来打开下拉菜单， 按钮或链接需要添加 **.dropdown-toggle** 和 **data-toggle="dropdown"** 属性。


**** 元素上添加 **.dropdown-menu** 类来设置实现下拉菜单，然后在下拉菜单的选项中添加 **.dropdown-item** 类。


我们也可以在 **** 标签中使用：


## 实例


```css
<div class="dropdown">
  <a class="btn btn-secondary dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropdown link
  </a>

  <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
    <a class="dropdown-item" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_dropdown-menu-a)


---


## 下拉菜单中的分割线


**.dropdown-divider** 类用于在下拉菜单中创建一个水平的分割线：


## 实例


```css
<div class="dropdown-divider"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_dropdown-divider)


---


## 下拉菜单中的标题


**.dropdown-header** 类用于在下拉菜单中添加标题：


## 实例


```css
<div class="dropdown-header">Dropdown header 1</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_dropdown-header)

---


## 下拉菜单中的可用项与禁用项


.active 类会让下拉菜单的选项高亮显示 (添加蓝色背景)。


如果要禁用下拉菜单的选项，可以使用**.disabled** 类。


## 实例


```css
<a class="dropdown-item active" href="#">Active</a>
<a class="dropdown-item disabled" href="#">Disabled</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_dropdown-active)


---


## 下拉菜单的定位


如果我们想让下拉菜单右对齐，可以在元素上的 .dropdown-menu 类后添加 **.dropdown-menu-right** 类。


## 实例


```css
<div class="dropdown-menu dropdown-menu-right">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs_dropdown-menu-right)

---


## 下拉菜单弹出方向设置


下拉菜单弹出方向默认为向下，当然我们也可以设置不同的方向。


### 指定向右弹出的下拉菜单


如果你希望下拉菜单向右弹出，可以在 div 元素上添加 **"dropright"** 类:


## 实例


```css
<!-- Default dropright button -->
<div class="btn-group dropright">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropright
  </button>
  <div class="dropdown-menu">
    <!-- Dropdown menu links -->
  </div>
</div>

<!-- Split dropright button -->
<div class="btn-group dropright">
  <button type="button" class="btn btn-secondary">
    Split dropright
  </button>
  <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    <span class="sr-only">Toggle Dropright</span>
  </button>
  <div class="dropdown-menu">
    <!-- Dropdown menu links -->
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_dropdown-menu-dropup-right)

### 指定向上弹出的上拉菜单


如果你希望上拉菜单向上弹出，可以在 div 元素上添加 **"dropup"** 类:


## 实例


```css
<!-- Default dropup button -->
<div class="btn-group dropup">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropup
  </button>
  <div class="dropdown-menu">
    <!-- Dropdown menu links -->
  </div>
</div>

<!-- Split dropup button -->
<div class="btn-group dropup">
  <button type="button" class="btn btn-secondary">
    Split dropup
  </button>
  <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    <span class="sr-only">Toggle Dropdown</span>
  </button>
  <div class="dropdown-menu">
    <!-- Dropdown menu links -->
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_dropdown-menu-dropup)

### 指定向左边弹出的下拉菜单


如果你希望下拉菜单向上弹出，可以在 div 元素上添加 **"dropleft"** 类:


## 实例


```css
<!-- Default dropleft button -->
<div class="btn-group dropleft">
  <button type="button" class="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropleft
  </button>
  <div class="dropdown-menu">
    <!-- Dropdown menu links -->
  </div>
</div>

<!-- Split dropleft button -->
<div class="btn-group">
  <div class="btn-group dropleft" role="group">
    <button type="button" class="btn btn-secondary dropdown-toggle dropdown-toggle-split" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
      <span class="sr-only">Toggle Dropleft</span>
    </button>
    <div class="dropdown-menu">
      <!-- Dropdown menu links -->
    </div>
  </div>
  <button type="button" class="btn btn-secondary">
    Split dropleft
  </button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_dropdown-menu-dropleft)


---


## 下拉菜单设置文本


**.dropdown-item-text** 类可以设置下拉菜单中的文本项：


## 实例


```css
<div class="dropdown-menu">
  <a class="dropdown-item" href="#">链接 1</a>
  <a class="dropdown-item" href="#">链接 2</a>
  <a class="dropdown-item-text" href="#">文本链接</a>
  <span class="dropdown-item-text">仅仅是文本</span>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_dropdown-text)


---


## 按钮中设置下拉菜单


我们可以在按钮中添加下拉菜单：


## 实例


```css
<div class="btn-group">
  <button type="button" class="btn btn-primary">Sony</button>
  <button type="button" class="btn btn-primary dropdown-toggle dropdown-toggle-split" data-toggle="dropdown">
    <span class="caret"></span>
  </button>
  <div class="dropdown-menu">
    <a class="dropdown-item" href="#">Tablet</a>
    <a class="dropdown-item" href="#">Smartphone</a>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs_dropdown-split)


垂直按钮组带下拉菜单：


## 实例


```css
<div class="btn-group-vertical">
  <button type="button" class="btn btn-primary">Apple</button>
  <button type="button" class="btn btn-primary">Samsung</button>
  <div class="btn-group">
    <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
       Sony
    </button>
    <div class="dropdown-menu">
      <a class="dropdown-item" href="#">Tablet</a>
      <a class="dropdown-item" href="#">Smartphone</a>
    </div>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_button_group_v_dropdown-split)







	  AI 思考中...





			** [Bootstrap4 卡片](https://www.runoob.com/bootstrap4-cards.html)
			[Bootstrap4 折叠](https://www.runoob.com/bootstrap4-collapse.html) **













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
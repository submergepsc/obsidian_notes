# Bootstrap 导航元素

- Source: https://www.runoob.com/bootstrap/bootstrap-navigation-elements.html

本章我们将讲解 Bootstrap 提供的用于定义导航元素的一些选项。它们使用相同的标记和基类 **.nav**。Bootstrap 也提供了一个用于共享标记和状态的帮助器类。改变修饰的 class，可以在不同的样式间进行切换。


## 表格导航或标签


创建一个标签式的导航菜单：


- 以一个带有 class **.nav** 的无序列表开始。
- 添加 class **.nav-tabs**。


下面的实例演示了这点：


## 实例


```css
<p>标签式的导航菜单</p>
<ul class="nav nav-tabs">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li><a href="#">iOS</a></li>
  <li><a href="#">VB.Net</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navigation-tabs&basepath=0)


结果如下所示：


![标签式的导航菜单](https://www.runoob.com/wp-content/uploads/2014/06/tabs_demo.jpg)


## 胶囊式的导航菜单


### 基本的胶囊式导航菜单


如果需要把标签改成胶囊的样式，只需要使用 class .nav-pills** 代替 **.nav-tabs** 即可，其他的步骤与上面相同。


下面的实例演示了这点：


## 实例


```css
<p>基本的胶囊式导航菜单</p>
<ul class="nav nav-pills">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li><a href="#">iOS</a></li>
  <li><a href="#">VB.Net</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navigation-basicpills&basepath=0)


结果如下所示：


![基本的胶囊式导航菜单](https://www.runoob.com/wp-content/uploads/2014/06/basicpills_demo.jpg)


### 垂直的胶囊式导航菜单


您可以在使用 class .nav、.nav-pills** 的同时使用 class **.nav-stacked**，让胶囊垂直堆叠。


下面的实例演示了这点：


## 实例


```css
<p>垂直的胶囊式导航菜单</p>
<ul class="nav nav-pills nav-stacked">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li><a href="#">iOS</a></li>
  <li><a href="#">VB.Net</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navigation-verticalpills&basepath=0)


结果如下所示：


![垂直的胶囊式导航菜单](https://www.runoob.com/wp-content/uploads/2014/06/verticalpills_demo.jpg)


## 两端对齐的导航


您可以在屏幕宽度大于 768px 时，通过在分别使用 .nav、.nav-tabs** 或 **.nav、.nav-pills** 的同时使用 class **.nav-justified**，让标签式或胶囊式导航菜单与父元素等宽。在更小的屏幕上，导航链接会堆叠。


下面的实例演示了这点：


## 实例


```css
<p>两端对齐的导航元素</p>
<ul class="nav nav-pills nav-justified">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li><a href="#">iOS</a></li>
  <li><a href="#">VB.Net</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul><br><br><br>
<ul class="nav nav-tabs nav-justified">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li><a href="#">iOS</a></li>
  <li><a href="#">VB.Net</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navigation-justifiednav&basepath=0)


结果如下所示：


![两端对齐的导航元素](https://www.runoob.com/wp-content/uploads/2014/06/justifiednavelements_demo.jpg)


## 禁用链接


对每个 .nav** class，如果添加了 **.disabled** class，则会创建一个灰色的链接，同时禁用了该链接的 **:hover** 状态，如下面的实例所示：


## 实例


```css
<p>导航元素中的禁用链接</p>
<ul class="nav nav-pills">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li class="disabled"><a href="#">iOS（禁用链接）</a></li>
  <li><a href="#">VB.Net</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul><br><br>
<ul class="nav nav-tabs">
  <li class="active"><a href="#">Home</a></li>
  <li><a href="#">SVN</a></li>
  <li><a href="#">iOS</a></li>
  <li  class="disabled"><a href="#">VB.Net（禁用链接）</a></li>
  <li><a href="#">Java</a></li>
  <li><a href="#">PHP</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navigation-disabledlinksnav&basepath=0)


结果如下所示：


![导航元素中的禁用链接](https://www.runoob.com/wp-content/uploads/2014/06/disabledlinksnav_demo.jpg)


> ![](https://www.runoob.com/images/quote.png)该 class 只会改变  的外观，不会改变它的功能。在这里，您需要使用自定义的 JavaScript 来禁用链接。


## 下拉菜单


导航菜单与下拉菜单使用相似的语法。默认情况下，列表项的锚与一些数据属性协同合作来触发带有 .dropdown-menu** class 的无序列表。


### 带有下拉菜单的标签


向标签添加下拉菜单的步骤如下：


- 以一个带有 class **.nav** 的无序列表开始。
- 添加 class **.nav-tabs**。
- 添加带有 **.dropdown-menu** class 的无序列表。


## 实例


```css
<p>带有下拉菜单的标签</p>
  <ul class="nav nav-tabs">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="#">SVN</a></li>
    <li><a href="#">iOS</a></li>
    <li><a href="#">VB.Net</a></li>
    <li class="dropdown">
      <a class="dropdown-toggle" data-toggle="dropdown" href="#">
        Java <span class="caret"></span>
      </a>
      <ul class="dropdown-menu">
        <li><a href="#">Swing</a></li>
        <li><a href="#">jMeter</a></li>
        <li><a href="#">EJB</a></li>
        <li class="divider"></li>
        <li><a href="#">分离的链接</a></li>
      </ul>
    </li>
    <li><a href="#">PHP</a></li>
  </ul>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navigation-tabsdropdown&basepath=0)


结果如下所示：


![带有下拉菜单的标签](https://www.runoob.com/wp-content/uploads/2014/06/tabsdropdown_demo.jpg)


### 带有下拉菜单的胶囊


步骤与创建带有下拉菜单的标签相同，只是需要把 .nav-tabs** class 改为 **.nav-pills**，如下面的实例所示：


## 实例


```css
<p>带有下拉菜单的胶囊</p>
  <ul class="nav nav-pills">
    <li class="active"><a href="#">Home</a></li>
    <li><a href="#">SVN</a></li>
    <li><a href="#">iOS</a></li>
    <li><a href="#">VB.Net</a></li>
    <li class="dropdown">
      <a class="dropdown-toggle" data-toggle="dropdown" href="#">
        Java <span class="caret"></span>
      </a>
      <ul class="dropdown-menu">
        <li><a href="#">Swing</a></li>
        <li><a href="#">jMeter</a></li>
        <li><a href="#">EJB</a></li>
        <li class="divider"></li>
        <li><a href="#">分离的链接</a></li>
      </ul>
    </li>
    <li><a href="#">PHP</a></li>
  </ul>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navigation-pillsdropdown&basepath=0)


结果如下所示：


![带有下拉菜单的胶囊](https://www.runoob.com/wp-content/uploads/2014/06/pillsdropdown_demo.jpg)


---


## 更多导航元素组件实例


### 标签页与胶囊式标签页


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .nav nav-tabs | 标签页 | 尝试一下 |
| .nav nav-pills | 胶囊式标签页 | 尝试一下 |
| .nav nav-pills nav-stacked | 胶囊式标签页以垂直方向堆叠排列的 | 尝试一下 |
| .nav-justified | 两端对齐的标签页，在大于 768px 的屏幕上，通过 .nav-justified 类可以很容易的让标签页或胶囊式标签呈现出同等宽度。在小屏幕上，导航链接呈现堆叠样式。 | 尝试一下 |
| .disabled | 禁用的标签页 | 尝试一下 |
| 标签添加下拉菜单 | 尝试一下 |  |
| 带下拉菜单的胶囊式标签页 | 尝试一下 |  |
| .tab-content | 与 .tab-pane 和 data-toggle="tab" (data-toggle="pill" ) 一同使用, 设置标签页对应的内容随标签的切换而更改 | 尝试一下 |
| .tab-pane | 与 .tab-content 和 data-toggle="tab" (data-toggle="pill")一同使用, 设置标签页对应的内容随标签的切换而更改 | 尝试一下 |








	  AI 思考中...





			** [Bootstrap 输入框组](https://www.runoob.com/bootstrap-input-groups.html)
			[Bootstrap 导航栏](https://www.runoob.com/bootstrap-navbar.html) **













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
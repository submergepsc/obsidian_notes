# Bootstrap 下拉菜单（Dropdown）插件

- Source: https://www.runoob.com/bootstrap/bootstrap-dropdown-plugin.html

[Bootstrap 下拉菜单](https://www.runoob.com/bootstrap-dropdowns.html) 这一章讲解了下拉菜单，但是没有涉及到交互部分，本章将具体讲解下拉菜单的交互。使用下拉菜单（Dropdown）插件，您可以向任何组件（比如导航栏、标签页、胶囊式导航菜单、按钮等）添加下拉菜单。


如果您想要单独引用该插件的功能，那么您需要引用 **dropdown.js**。或者，正如 [Bootstrap 插件概览](https://www.runoob.com/bootstrap-plugins-overview.html) 一章中所提到，您可以引用 *bootstrap.js* 或压缩版的 *bootstrap.min.js*。


## 用法


您可以切换下拉菜单（Dropdown）插件的隐藏内容：


- **通过 data 属性**：向链接或按钮添加 **data-toggle="dropdown"** 来切换下拉菜单，如下所示：
```
<div class="dropdown">
  <a data-toggle="dropdown" href="#">下拉菜单（Dropdown）触发器</a>
  <ul class="dropdown-menu" role="menu" aria-labelledby="dLabel">
    ...
  </ul>
</div>
```
 如果您需要保持链接完整（在浏览器不启用 JavaScript 时有用），请使用 **data-target** 属性代替 **href="#"**：
```
<div class="dropdown">
  <a id="dLabel" role="button" data-toggle="dropdown" data-target="#" href="/page.html">
    下拉菜单（Dropdown） <span class="caret"></span>
  </a>


  <ul class="dropdown-menu" role="menu" aria-labelledby="dLabel">
    ...
  </ul>
</div>
```

- **通过 JavaScript**：通过 JavaScript 调用下拉菜单切换，请使用下面的方法：
```
$('.dropdown-toggle').dropdown()
```


### 实例


#### 在导航栏内


下面的实例演示了在导航栏内的下拉菜单的用法：


## 实例


```css
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <div>
        <ul class="nav navbar-nav">
            <li class="active"><a href="#">iOS</a></li>
            <li><a href="#">SVN</a></li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                    Java
                    <b class="caret"></b>
                </a>
                <ul class="dropdown-menu">
                    <li><a href="#">jmeter</a></li>
                    <li><a href="#">EJB</a></li>
                    <li><a href="#">Jasper Report</a></li>
                    <li class="divider"></li>
                    <li><a href="#">分离的链接</a></li>
                    <li class="divider"></li>
                    <li><a href="#">另一个分离的链接</a></li>
                </ul>
            </li>
        </ul>
    </div>
    </div>
</nav>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-plugin-dropdown-defaultnavbar)


结果如下所示：


![](https://www.runoob.com/wp-content/uploads/2014/06/C927D25C-CA7D-4FD1-8651-5680874BBE3E.jpg)


#### 在标签页内


下面的实例演示了在标签页内的下拉菜单的用法：


## 实例


```css
<p>带有下拉菜单的标签页</p>
<ul class="nav nav-tabs">
    <li class="active">
        <a href="#">Home</a></li>
    <li>
        <a href="#">SVN</a></li>
    <li>
        <a href="#">iOS</a></li>
    <li>
        <a href="#">VB.Net</a></li>
    <li class="dropdown">
        <a class="dropdown-toggle" data-toggle="dropdown" href="#">Java
            <span class="caret"></span></a>
        <ul class="dropdown-menu">
            <li>
                <a href="#">Swing</a></li>
            <li>
                <a href="#">jMeter</a></li>
            <li>
                <a href="#">EJB</a></li>
            <li class="divider"></li>
            <li>
                <a href="#">分离的链接</a></li>
        </ul>
    </li>
    <li>
        <a href="#">PHP</a></li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-plugin-dropdown-tabsdropdown)


结果如下所示：


![带有下拉菜单的标签页](https://www.runoob.com/wp-content/uploads/2014/07/tabsdropdown_demo.jpg)


## 选项


*没有选项。*


## 方法


下拉菜单切换有一个简单的方法用来显示或隐藏下拉菜单。


```
$().dropdown('toggle')
```


### 实例


下面的实例演示了下拉菜单（Dropdown）插件方法的用法：


## 实例


```css
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <div id="myexample">
        <ul class="nav navbar-nav">
            <li class="active">
                <a href="#">iOS</a>
            </li>
            <li>
                <a href="#">SVN</a>
            </li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">Java
                    <b class="caret"></b>
                </a>
                <ul class="dropdown-menu">
                    <li>
                        <a id="action-1" href="#">jmeter</a>
                    </li>
                    <li>
                        <a href="#">EJB</a>
                    </li>
                    <li>
                        <a href="#">Jasper Report</a>
                    </li>
                    <li class="divider"></li>
                    <li>
                        <a href="#">分离的链接</a>
                    </li>
                    <li class="divider"></li>
                    <li>
                        <a href="#">另一个分离的链接</a>
                    </li>
                </ul>
            </li>
        </ul>
    </div>
    </div>
</nav>
</div>
<script>
$(function() {
    $(".dropdown-toggle").dropdown('toggle');
});
</script>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-plugin-dropdown-method)


结果如下所示：


![固定到顶部](https://www.runoob.com/wp-content/uploads/2014/06/446D81D0-FED2-4237-A6EB-EECAF0E69E36.jpg)








	  AI 思考中...





			** [Bootstrap 模态框（Modal）插件](https://www.runoob.com/bootstrap-modal-plugin.html)
			[Bootstrap 滚动监听（Scrollspy）插件](https://www.runoob.com/bootstrap-scrollspy-plugin.html) **













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
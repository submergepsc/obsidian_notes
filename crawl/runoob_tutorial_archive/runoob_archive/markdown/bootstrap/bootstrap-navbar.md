# Bootstrap 导航栏

- Source: https://www.runoob.com/bootstrap/bootstrap-navbar.html

导航栏是一个很好的功能，是 Bootstrap 网站的一个突出特点。导航栏在您的应用或网站中作为导航页头的响应式基础组件。导航栏在移动设备的视图中是折叠的，随着可用视口宽度的增加，导航栏也会水平展开。在 Bootstrap 导航栏的核心中，导航栏包括了站点名称和基本的导航定义样式。


## 默认的导航栏


创建一个默认的导航栏的步骤如下：


- 向  标签添加 class **.navbar、.navbar-default**。
- 向上面的元素添加 **role="navigation"**，有助于增加可访问性。
- 向  元素添加一个标题 class **.navbar-header**，内部包含了带有 class **navbar-brand** 的  元素。这会让文本看起来更大一号。
- 为了向导航栏添加链接，只需要简单地添加带有 class **.nav、.navbar-nav** 的无序列表即可。


下面的实例演示了这点：


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
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-default)


结果如下所示：

![](https://www.runoob.com/wp-content/uploads/2014/06/C927D25C-CA7D-4FD1-8651-5680874BBE3E.jpg)
---


## 响应式的导航栏


为了给导航栏添加响应式特性，您要折叠的内容必须包裹在带有 class .collapse、.navbar-collapse** 的  中。折叠起来的导航栏实际上是一个带有 class **.navbar-toggle** 及两个 data- 元素的按钮。第一个是 **data-toggle**，用于告诉 JavaScript 需要对按钮做什么，第二个是 **data-target**，指示要切换到哪一个元素。三个带有 class **.icon-bar** 的  创建所谓的汉堡按钮。这些会切换为 **.nav-collapse**  中的元素。为了实现以上这些功能，您必须包含 [Bootstrap 折叠（Collapse）插件](https://www.runoob.com/bootstrap-collapse-plugin.html)。


下面的实例演示了这点：


## 实例


```css
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse"
                data-target="#example-navbar-collapse">
            <span class="sr-only">切换导航</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <div class="collapse navbar-collapse" id="example-navbar-collapse">
        <ul class="nav navbar-nav">
            <li class="active"><a href="#">iOS</a></li>
            <li><a href="#">SVN</a></li>
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                    Java <b class="caret"></b>
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
[尝试一下 »](https://www.runoob.com/try/try.php?filename=bootstrap3-navbar-responsive)

结果如下所示：


	![响应式的导航栏](https://www.runoob.com/wp-content/uploads/2014/06/98B4B325-7C69-4C93-8419-8B77D12395D5.jpg)


## 导航栏中的表单


导航栏中的表单不是使用 [Bootstrap 表单](https://www.runoob.com/bootstrap-forms.html) 章节中所讲到的默认的 class，它是使用 .navbar-form** class。这确保了表单适当的垂直对齐和在较窄的视口中折叠的行为。使用对齐方式选项（这将在组件对齐方式部分进行详细讲解）来决定导航栏中的内容放置在哪里。


下面的实例演示了这点：


## 实例


```css
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <form class="navbar-form navbar-left" role="search">
        <div class="form-group">
            <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">提交</button>
    </form>
    </div>
</nav>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-forms)

结果如下所示：


	![导航栏中的表单](https://www.runoob.com/wp-content/uploads/2014/06/E5A8B92D-C675-4DA5-B08C-D2F26F48928D.jpg)


## 导航栏中的按钮


您可以使用 class .navbar-btn** 向不在  中的  元素添加按钮，按钮在导航栏上垂直居中。**.navbar-btn** 可被使用在  和  元素上。

**![](https://www.runoob.com/images/quote.png)不要在 .navbar-nav** 内的 <a> 元素上使用 **.navbar-btn**，因为它不是标准的 [button class](https://www.runoob.com/bootstrap-buttons.html)。

下面的实例演示了这点：


## 实例


```css
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <div>
        <form class="navbar-form navbar-left" role="search">
            <div class="form-group">
                <input type="text" class="form-control" placeholder="Search">
            </div>
            <button type="submit" class="btn btn-default">提交按钮</button>
        </form>
        <button type="button" class="btn btn-default navbar-btn">
            导航栏按钮
        </button>
    </div>
    </div>
</nav>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-buttons)

结果如下所示：


	![导航栏中的按钮](https://www.runoob.com/wp-content/uploads/2014/06/CEEE093C-6F4D-4933-A240-561CD7A13EC7.jpg)


## 导航栏中的文本


如果需要在导航中包含文本字符串，请使用 class .navbar-text**。这通常与  标签一起使用，确保适当的前导和颜色。下面的实例演示了这点：


## 实例


```css
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <div>
        <p class="navbar-text">Runoob 用户登录</p>
    </div>
    </div>
</nav>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-text)

结果如下所示：


	![导航栏中的文本](https://www.runoob.com/wp-content/uploads/2014/06/1CE36FCE-22DF-4CFC-8310-17D66363DA15.jpg)


## 结合图标的导航链接


如果您想在常规的导航栏导航组件内使用图标，那么请使用 class glyphicon glyphicon-*** 来设置图标，更多请查看 [Bootstrap 图标](https://www.runoob.com/bootstrap-glyphicons.html)，如下面的实例所示：


## 实例


```css
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
        <div class="navbar-header">
            <a class="navbar-brand" href="#">菜鸟教程</a>
        </div>
        <ul class="nav navbar-nav navbar-right">
            <li><a href="#"><span class="glyphicon glyphicon-user"></span> 注册</a></li>
            <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> 登录</a></li>
        </ul>
    </div>
</nav>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-nonnavlinks)

结果如下所示：


	![结合图标的导航链接](https://www.runoob.com/wp-content/uploads/2014/06/64E5993E-ED1A-4B72-AE90-50076B78224D.jpg)


## 组件对齐方式


您可以使用实用工具 class .navbar-left** 或 **.navbar-right** 向左或向右对齐导航栏中的 *导航链接、表单、按钮或文本* 这些组件。这两个 class 都会在指定的方向上添加 CSS 浮动。下面的实例演示了这点：


## 实例


```css
<nav class="navbar navbar-default" role="navigation">
    <div class="container-fluid">
    <div class="navbar-header">
        <a class="navbar-brand" href="#">菜鸟教程</a>
    </div>
    <div>
        <!--向左对齐-->
        <ul class="nav navbar-nav navbar-left">
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
        <form class="navbar-form navbar-left" role="search">
            <button type="submit" class="btn btn-default">
                向左对齐-提交按钮
            </button>
        </form>
        <p class="navbar-text navbar-left">向左对齐-文本</p>
        <!--向右对齐-->
        <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">
                    Java <b class="caret"></b>
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
        <form class="navbar-form navbar-right" role="search">
            <button type="submit" class="btn btn-default">
                向右对齐-提交按钮
            </button>
        </form>
        <p class="navbar-text navbar-right">向右对齐-文本</p>
    </div>
    </div>
</nav>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-compalignment)

结果如下所示：


	![组件对齐方式](https://www.runoob.com/wp-content/uploads/2014/06/B4F6F15B-EFAC-44D7-A577-2F36ED59252C.jpg)


## 固定到顶部


Bootstrap 导航栏可以动态定位。默认情况下，它是块级元素，它是基于在 HTML 中放置的位置定位的。通过一些帮助器类，您可以把它放置在页面的顶部或者底部，或者您可以让它成为随着页面一起滚动的静态导航栏。


如果您想要让导航栏固定在页面的顶部，请向 .navbar class** 添加 class **.navbar-fixed-top**。下面的实例演示了这点：

**![](https://www.runoob.com/images/quote.png)为了防止导航栏与页面主体中的其他内容的顶部相交错，请向 <body> 标签添加至少 50 像素的内边距（padding），内边距的值可以根据您的需要进行设置。


## 实例


```css
<nav class="navbar navbar-default navbar-fixed-top" role="navigation">
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
                    Java <b class="caret"></b>
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


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-fixedtotop)

结果如下所示：


	![固定到顶部](https://www.runoob.com/wp-content/uploads/2014/06/446D81D0-FED2-4237-A6EB-EECAF0E69E36.jpg)


## 固定到底部


如果您想要让导航栏固定在页面的底部，请向 .navbar class** 添加 class **.navbar-fixed-bottom**。下面的实例演示了这点：


## 实例


```css
<nav class="navbar navbar-default navbar-fixed-bottom" role="navigation">
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
                    Java <b class="caret"></b>
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
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-fixedtobottom)

结果如下所示：


	![固定到底部](https://www.runoob.com/wp-content/uploads/2014/06/5D96CD7D-7665-4329-AEFA-A0D2829E3C38.jpg)


## 静态的顶部


如需创建能随着页面一起滚动的导航栏，请添加 .navbar-static-top** class。该 class 不要求向  添加内边距（padding）。


## 实例


```css
<nav class="navbar navbar-default navbar-static-top" role="navigation">
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
                    Java <b class="caret"></b>
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
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-statictop)

结果如下所示：


	![](https://www.runoob.com/wp-content/uploads/2014/06/446D81D0-FED2-4237-A6EB-EECAF0E69E36.jpg)


## 反色的导航栏


为了创建一个带有黑色背景白色文本的反色的导航栏，只需要简单地向 .navbar** class 添加 **.navbar-inverse** class 即可，如下面的实例所示：

**![](https://www.runoob.com/images/quote.png)为了防止导航栏与页面主体中的其他内容的顶部相交错，请向 <body> 标签添加至少 50 像素的内边距（padding），内边距的值可以根据您的需要进行设置。


## 实例


```css
<nav class="navbar navbar-inverse" role="navigation">
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
                    Java <b class="caret"></b>
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


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-navbar-inverted)

结果如下所示：


	![反色的导航栏](https://www.runoob.com/wp-content/uploads/2014/06/F7E88E85-A82C-4EC9-921F-C45CAFF9AD35.jpg)








	  AI 思考中...





			** [Bootstrap 导航元素](https://www.runoob.com/bootstrap-navigation-elements.html)
			[Bootstrap 面包屑导航](https://www.runoob.com/bootstrap-breadcrumbs.html) **













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
# Bootstrap 面板（Panels）

- Source: https://www.runoob.com/bootstrap/bootstrap-panels.html

本章将讲解 Bootstrap 面板（Panels）。面板组件用于把 DOM 组件插入到一个盒子中。创建一个基本的面板，只需要向  元素添加 class **.panel** 和 class **.panel-default** 即可，如下面的实例所示：


## 实例


```css
<div class="panel panel-default">
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-panel-deafult)

结果如下所示：


	![默认的面板](https://www.runoob.com/wp-content/uploads/2014/06/paneldeafult_demo.jpg)


## 面板标题


我们可以通过以下两种方式来添加面板标题：


- 使用 **.panel-heading** class 可以很简单地向面板添加标题容器。
- 使用带有 **.panel-title** class 的 - 来添加预定义样式的标题。


下面的实例演示了这两种方式：


## 实例


```css
<div class="panel panel-default">
    <div class="panel-heading">
        不带 title 的面板标题
    </div>
    <div class="panel-body">
        面板内容
    </div>
</div>

<div class="panel panel-default">
    <div class="panel-heading">
        <h3 class="panel-title">
            带有 title 的面板标题
        </h3>
    </div>
    <div class="panel-body">
        面板内容
    </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-panel-heading)

结果如下所示：


	![面板标题](https://www.runoob.com/wp-content/uploads/2014/06/panelheading_demo.jpg)


## 面板脚注


我们可以在面板中添加脚注，只需要把按钮或者副文本放在带有 class .panel-footer** 的  中即可。下面的实例演示了这点：


## 实例


```css
<div class="panel panel-default">
    <div class="panel-body">
        这是一个基本的面板
    </div>
    <div class="panel-footer">面板脚注</div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-panel-footer)

结果如下所示：


	![面板脚注](https://www.runoob.com/wp-content/uploads/2014/06/panelfooter_demo.jpg)


> ![](https://www.runoob.com/images/quote.png)面版脚注不会从带语境色彩的面板中继承颜色和边框，因为它不是前景中的内容。


## 带语境色彩的面板


使用语境状态类 panel-primary、panel-success、panel-info、panel-warning、panel-danger**，来设置带语境色彩的面板，实例如下：


## 实例


```css
<div class="panel panel-primary">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
<div class="panel panel-success">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
<div class="panel panel-info">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
<div class="panel panel-warning">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
<div class="panel panel-danger">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-panel-styles)

结果如下所示：


	![带语境色彩的面板](https://www.runoob.com/wp-content/uploads/2014/06/panelstyles_demo.jpg)


## 带表格的面板


为了在面板中创建一个无边框的表格，我们可以在面板中使用 class .table**。假设有个  包含 **.panel-body**，我们可以向表格的顶部添加额外的边框用来分隔。如果没有包含 **.panel-body** 的 ，则组件会无中断地从面板头部移动到表格。


下面的实例演示了这点：


## 实例


```css
<div class="panel panel-default">
    <div class="panel-heading">
        <h3 class="panel-title">面板标题</h3>
    </div>
    <div class="panel-body">
        这是一个基本的面板
    </div>
    <table class="table">
        <th>产品</th><th>价格 </th>
        <tr><td>产品 A</td><td>200</td></tr>
        <tr><td>产品 B</td><td>400</td></tr>
    </table>
</div>
<div class="panel panel-default">
    <div class="panel-heading">面板标题</div>
    <table class="table">
        <th>产品</th><th>价格 </th>
        <tr><td>产品 A</td><td>200</td></tr>
        <tr><td>产品 B</td><td>400</td></tr>
    </table>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-panel-table)

结果如下所示：


	![带表格的面板](https://www.runoob.com/wp-content/uploads/2014/06/paneltable_demo.jpg)


## 带列表组的面板


我们可以在任何面板中包含列表组，通过在  元素中添加 .panel** 和 **.panel-default** 类来创建面板，并在面板中添加列表组。您可以从 [列表组](https://www.runoob.com/bootstrap-list-group.html) 一章中学习如何创建列表组。


## 实例


```css
<div class="panel panel-default">
    <div class="panel-heading">面板标题</div>
    <div class="panel-body">
        <p>这是一个基本的面板内容。这是一个基本的面板内容。
            这是一个基本的面板内容。这是一个基本的面板内容。
            这是一个基本的面板内容。这是一个基本的面板内容。
            这是一个基本的面板内容。这是一个基本的面板内容。
        </p>
    </div>
    <ul class="list-group">
        <li class="list-group-item">免费域名注册</li>
        <li class="list-group-item">免费 Window 空间托管</li>
        <li class="list-group-item">图像的数量</li>
        <li class="list-group-item">24*7 支持</li>
        <li class="list-group-item">每年更新成本</li>
    </ul>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-panel-listgroups)

结果如下所示：


	![带列表组的面板](https://www.runoob.com/wp-content/uploads/2014/06/panellistgroups_demo.jpg)








	  AI 思考中...





			** [Bootstrap 列表组](https://www.runoob.com/bootstrap-list-group.html)
			[Bootstrap Well](https://www.runoob.com/bootstrap-wells.html) **













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
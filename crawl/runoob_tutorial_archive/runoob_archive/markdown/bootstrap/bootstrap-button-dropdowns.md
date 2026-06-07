# Bootstrap 按钮下拉菜单

- Source: https://www.runoob.com/bootstrap/bootstrap-button-dropdowns.html

本章将讲解如何使用 Bootstrap class 向按钮添加下拉菜单。如需向按钮添加下拉菜单，只需要简单地在一个 **.btn-group** 容器中放置按钮和下拉菜单即可。您也可以使用  来指示按钮作为下拉菜单。


下面的实例演示了一个基本的简单的按钮下拉菜单：


## 实例


```css
<div class="btn-group">
    <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">默认
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu">
        <li>
            <a href="#">功能</a>
        </li>
        <li>
            <a href="#">另一个功能</a>
        </li>
        <li>
            <a href="#">其他</a>
        </li>
        <li class="divider"></li>
        <li>
            <a href="#">分离的链接</a>
        </li>
    </ul>
</div>
<div class="btn-group">
    <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">原始
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu">
        <li>
            <a href="#">功能</a>
        </li>
        <li>
            <a href="#">另一个功能</a>
        </li>
        <li>
            <a href="#">其他</a>
        </li>
        <li class="divider"></li>
        <li>
            <a href="#">分离的链接</a>
        </li>
    </ul>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-buttondropdown-basic&basepath=0)


结果如下所示：


![基本的按钮下拉菜单](https://www.runoob.com/wp-content/uploads/2014/06/basicbuttondropdown_demo.jpg)


## 分割的按钮下拉菜单


分割的按钮下拉菜单使用与下拉菜单按钮大致相同的样式，但是对下拉菜单添加了原始的功能。分割按钮的左边是原始的功能，右边是显示下拉菜单的切换。


## 实例


```css
<div class="btn-group">
    <button type="button" class="btn btn-default">默认</button>
    <button type="button" class="btn btn-default dropdown-toggle"
        data-toggle="dropdown">
        <span class="caret"></span>
        <span class="sr-only">切换下拉菜单</span>
    </button>
    <ul class="dropdown-menu" role="menu">
        <li><a href="#">功能</a></li>
        <li><a href="#">另一个功能</a></li>
        <li><a href="#">其他</a></li>
        <li class="divider"></li>
        <li><a href="#">分离的链接</a></li>
    </ul>
</div>
<div class="btn-group">
    <button type="button" class="btn btn-primary">原始</button>
    <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">
        <span class="caret"></span>
        <span class="sr-only">切换下拉菜单</span>
    </button>
    <ul class="dropdown-menu" role="menu">
        <li><a href="#">功能</a></li>
        <li><a href="#">另一个功能</a></li>
        <li><a href="#">其他</a></li>
        <li class="divider"></li>
        <li><a href="#">分离的链接</a></li>
    </ul>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-buttondropdown-split&basepath=0)


结果如下所示：


![分割的按钮下拉菜单](https://www.runoob.com/wp-content/uploads/2014/06/splitbuttondropdown_demo.jpg)


## 按钮下拉菜单的大小


您可以使用带有各种大小按钮的下拉菜单：.btn-lg、.btn-sm **或 **.btn-xs**。


## 实例


```css
<div class="btn-group">
    <button type="button" class="btn btn-default dropdown-toggle btn-lg" data-toggle="dropdown">默认
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu">
        <li>
            <a href="#">功能</a>
        </li>
        <li>
            <a href="#">另一个功能</a>
        </li>
        <li>
            <a href="#">其他</a>
        </li>
        <li class="divider"></li>
        <li>
            <a href="#">分离的链接</a>
        </li>
    </ul>
</div>
<div class="btn-group">
    <button type="button" class="btn btn-primary dropdown-toggle btn-sm" data-toggle="dropdown">原始
        <span class="caret"></span>
    </button>
    <ul class="dropdown-menu" role="menu">
        <li>
            <a href="#">功能</a>
        </li>
        <li>
            <a href="#">另一个功能</a>
        </li>
        <li>
            <a href="#">其他</a>
        </li>
        <li class="divider"></li>
        <li>
            <a href="#">分离的链接</a>
        </li>
    </ul>
</div>
<div class="btn-group">
    <button type="button" class="btn btn-success dropdown-toggle btn-xs" data-toggle="dropdown">成功
        <span class="caret"></span></button>
    <ul class="dropdown-menu" role="menu">
        <li>
            <a href="#">功能</a>
        </li>
        <li>
            <a href="#">另一个功能</a>
        </li>
        <li>
            <a href="#">其他</a>
        </li>
        <li class="divider"></li>
        <li>
            <a href="#">分离的链接</a>
        </li>
    </ul>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-buttondropdown-size&basepath=0)


结果如下所示：


![按钮下拉菜单的大小](https://www.runoob.com/wp-content/uploads/2014/06/buttondropdownsize_demo.jpg)


## 按钮上拉菜单


菜单也可以往上拉伸的，只需要简单地向父 .btn-group** 容器添加 **.dropup** 即可。


## 实例


```css
<div class="row" style="margin-left:50px; margin-top:200px">
    <div class="btn-group dropup">
        <button type="button" class="btn btn-default dropdown-toggle" data-toggle="dropdown">默认
            <span class="caret"></span>
        </button>
        <ul class="dropdown-menu" role="menu">
            <li>
                <a href="#">功能</a>
            </li>
            <li>
                <a href="#">另一个功能</a>
            </li>
            <li>
                <a href="#">其他</a>
            </li>
            <li class="divider"></li>
            <li>
                <a href="#">分离的链接</a>
            </li>
        </ul>
    </div>
    <div class="btn-group dropup">
        <button type="button" class="btn btn-primary dropdown-toggle" data-toggle="dropdown">原始
            <span class="caret"></span>
        </button>
        <ul class="dropdown-menu" role="menu">
            <li>
                <a href="#">功能</a>
            </li>
            <li>
                <a href="#">另一个功能</a>
            </li>
            <li>
                <a href="#">其他</a>
            </li>
            <li class="divider"></li>
            <li>
                <a href="#">分离的链接</a>
            </li>
        </ul>
    </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-buttondropdown-dropupvariation&basepath=0)


结果如下所示：


![按钮上拉菜单](https://www.runoob.com/wp-content/uploads/2014/06/dropupvariation_demo.jpg)








	  AI 思考中...





			** [Bootstrap 按钮组](https://www.runoob.com/bootstrap-button-groups.html)
			[Bootstrap 输入框组](https://www.runoob.com/bootstrap-input-groups.html) **













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
# Bootstrap 按钮（Button）插件

- Source: https://www.runoob.com/bootstrap/bootstrap-button-plugin.html

按钮（Button）在 [Bootstrap 按钮](https://www.runoob.com/bootstrap-buttons.html) 一章中介绍过。通过按钮（Button）插件，您可以添加进一些交互，比如控制按钮状态，或者为其他组件（如工具栏）创建按钮组。


## 加载状态


如需向按钮添加加载状态，只需要简单地向 button 元素添加 **data-loading-text="Loading..."** 作为其属性即可，如下面实例所示：


## 实例


```css
<button id="fat-btn" class="btn btn-primary" data-loading-text="Loading..."
    type="button"> 加载状态
</button>
<script>
    $(function() {
        $(".btn").click(function(){
            $(this).button('loading').delay(1000).queue(function() {
            // $(this).button('reset');
            // $(this).dequeue();
            });
        });
    });
</script>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-plugin-button-loadingstate)


结果如下所示：


![按钮（Button）插件加载状态](https://www.runoob.com/wp-content/uploads/2014/07/loadingstatebutton_demo.jpg)


## 单个切换


如需激活单个按钮的切换（即改变按钮的正常状态为按压状态，反之亦然），只需向 button 元素添加 data-toggle="button"** 作为其属性即可，如下面实例所示：


## 实例


```css
<button type="button" class="btn btn-primary"
    data-toggle="button"> 单个切换
</button>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-plugin-button-sinlgetoggle)


结果如下所示：


![按钮（Button）插件单个切换](https://www.runoob.com/wp-content/uploads/2014/07/sinlgetogglebutton_demo.jpg)


## 复选框（Checkbox）


您可以创建复选框组，并通过向 btn-group** 添加 data 属性 **data-toggle="buttons"** 来添加复选框组的切换。


## 实例


```css
<div class="btn-group" data-toggle="buttons">
    <label class="btn btn-primary">
        <input type="checkbox"> 选项 1
    </label>
    <label class="btn btn-primary">
        <input type="checkbox"> 选项 2
    </label>
    <label class="btn btn-primary">
        <input type="checkbox"> 选项 3
    </label>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-plugin-button-checkbox)


结果如下所示：


![按钮（Button）插件复选框](https://www.runoob.com/wp-content/uploads/2014/07/checkboxbutton_demo.jpg)


## 单选按钮（Radio）


类似地，您可以创建单选按钮组，并通过向 btn-group** 添加 data 属性 **data-toggle="buttons"** 来添加单选按钮组的切换。


## 实例


```css
<div class="btn-group" data-toggle="buttons">
    <label class="btn btn-primary">
        <input type="radio" name="options" id="option1"> 选项 1
    </label>
    <label class="btn btn-primary">
        <input type="radio" name="options" id="option2"> 选项 2
    </label>
    <label class="btn btn-primary">
        <input type="radio" name="options" id="option3"> 选项 3
    </label>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-plugin-button-radio)


结果如下所示：


![按钮（Button）插件单选按钮](https://www.runoob.com/wp-content/uploads/2014/07/radiobutton_demo.jpg)


## 用法


您可以 通过 JavaScript** 启用按钮（Button）插件，如下所示：


```
$('.btn').button()
```


## 选项


*没有选项。*


## 方法


下面是一些按钮（Button）插件中有用的方法：


| 方法 | 描述 | 实例 |
| --- | --- | --- |
| button('toggle') | 切换按压状态。赋予按钮被激活的外观。您可以使用 data-toggle 属性启用按钮的自动切换。 |
```
$().button('toggle')
```
 |
| .button('loading') | 当加载时，按钮是禁用的，且文本变为 button 元素的 data-loading-text 属性的值。 |
```
$().button('loading')
```
 |
| .button('reset') | 重置按钮状态，文本内容恢复为最初的内容。当您想要把按钮返回为原始的状态时，该方法非常有用。 |
```
$().button('reset')
```
 |
| .button(string) | 该方法中的字符串是指由用户声明的任何字符串。使用该方法，重置按钮状态，并添加新的内容。 |
```
$().button(string)
```
 |


### 实例


下面的实例演示了上面方法的用法：


## 实例


```css
<h2>点击每个按钮查看方法效果</h2>
<h4>演示 .button('toggle') 方法</h4>
<div id="myButtons1" class="bs-example">
    <button type="button" class="btn btn-primary">原始</button>
</div>

<h4>演示 .button('loading') 方法</h4>
<div id="myButtons2" class="bs-example">
    <button type="button" class="btn btn-primary"
        data-loading-text="Loading...">原始
    </button>
</div>

<h4>演示 .button('reset') 方法</h4>
<div id="myButtons3" class="bs-example">
    <button type="button" class="btn btn-primary"
        data-loading-text="Loading...">原始
    </button>
</div>

<h4>演示 .button(string) 方法</h4>
<button type="button" class="btn btn-primary" id="myButton4"
    data-complete-text="Loading finished">请点击我
</button>
<script>
```


$(function () {
        $("#myButtons1 .btn").click(function(){
            $(this).button('toggle');
        });
    });
    $(function() {
        $("#myButtons2 .btn").click(function(){
            $(this).button('loading').delay(1000).queue(function() {
            });
        });
    });
    $(function() {
        $("#myButtons3 .btn").click(function(){
            $(this).button('loading').delay(1000).queue(function() {
                $(this).button('reset');
            });
        });
    });
   $(function() {
        $("#myButton4").click(function(){
            $(this).button('loading').delay(1000).queue(function() {
                $(this).button('complete');
            });
        });
    });
</script>
**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-plugin-button-method)


结果如下所示：


![按钮（Button）插件方法](https://www.runoob.com/wp-content/uploads/2014/07/buttonpluginmethods_demo.jpg)








	  AI 思考中...





			** [Bootstrap 警告框](https://www.runoob.com/bootstrap-alert-plugin.html)
			[Bootstrap 折叠（Collapse）插件](https://www.runoob.com/bootstrap-collapse-plugin.html) **













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
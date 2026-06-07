# Bootstrap 警告框（Alert）插件

- Source: https://www.runoob.com/bootstrap/bootstrap-alert-plugin.html

警告框（Alert）消息大多是用来向终端用户显示诸如警告或确认消息的信息。使用警告框（Alert）插件，您可以向所有的警告框消息添加可取消（dismiss）功能。


## 用法


您可以有以下两种方式启用警告框的可取消（dismissal）功能：


- **通过 data 属性**：通过数据 API（Data API）添加可取消功能，只需要向关闭按钮添加 **data-dismiss="alert"**，就会自动为警告框添加关闭功能。
```
<a class="close" data-dismiss="alert" href="#" aria-hidden="true">
    &times;
</a>
```

- **通过 JavaScript**：通过 JavaScript 添加可取消功能：
```
$(".alert").alert()
```


### 实例


下面的实例演示了通过 data 属性使用警告框（Alert）插件的用法。


## 实例


```css
<div class="alert alert-warning">
    <a href="#" class="close" data-dismiss="alert">
        &times;
    </a>
    <strong>警告！</strong>您的网络连接有问题。
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-plugin-alert)


结果如下所示：


![警告框（Alert）插件](https://www.runoob.com/wp-content/uploads/2014/07/alertmessages_demo.jpg)


## 选项


*没有选项。*


## 方法


下面是一些警告框（Alert）插件中有用的方法：


| 方法 | 描述 | 实例 |
| --- | --- | --- |
| .alert() | 该方法让所有的警告框都带有关闭功能。 |
```
$('#identifier').alert();
```
 |
| 关闭方法 .alert('close') | 关闭所有的警告框。 |
```
$('#identifier').alert('close');
```
 |


> 如需在关闭时启用动画效果，请确保添加了 .fade** 和 **.in** class。


### 实例


下面的实例演示了 **.alert()** 方法的用法：


## 实例


```css
<h3>警告框（Alert）插件 alert() 方法</h3>
<div id="myAlert" class="alert alert-success">
    <a href="#" class="close" data-dismiss="alert">&times;</a>
    <strong>成功！</strong>结果是成功的。
</div>
<div id="myAlert2" class="alert alert-warning">
    <a href="#" class="close" data-dismiss="alert">&times;</a>
    <strong>警告！</strong>您的网络连接有问题。
</div>

<script>
```


$(function(){
    $(".close").click(function(){
        $("#myAlert").alert();
        $("#myAlert2").alert();
    });
});
</script>
**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-plugin-alert-method1)


下面的实例演示了 .alert('close')** 方法的用法：


## 实例


```css
<h3>警告框（Alert）插件 alert('close') 方法</h3>
<div id="myAlert" class="alert alert-success">
    <a href="#" class="close" data-dismiss="alert">&times;</a>
    <strong>成功！</strong>结果是成功的。
</div>
<div id="myAlert2" class="alert alert-warning">
    <a href="#" class="close" data-dismiss="alert">&times;</a>
    <strong>警告！</strong>您的网络连接有问题。
</div>

<script>
```


$(function(){
    $(".close").click(function(){
        $("#myAlert").alert('close');
        $("#myAlert2").alert('close');
    });
});
</script>
**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-plugin-alert-method2)


您可以看到所有的警告框都应用了关闭功能，即关闭任意的警告框，其他剩余的警告框也会被关闭。


## 事件


下表列出了警告框（Alert）插件中要用到的事件。这些事件可在函数中当钩子使用。


| 事件 | 描述 | 实例 |
| --- | --- | --- |
| close.bs.alert | 当调用 close 实例方法时立即触发该事件。 |
```
$('#myalert').bind('close.bs.alert', function () {
  // 执行一些动作...
})
```
 |
| closed.bs.alert | 当警告框被关闭时触发该事件（将等待 CSS 过渡效果完成）。 |
```
$('#myalert').bind('closed.bs.alert', function () {
    // 执行一些动作...
})
```
 |


### 实例


下面的实例演示了警告框（Alert）插件的事件：


## 实例


```css
<div id="myAlert" class="alert alert-success">
    <a href="#" class="close" data-dismiss="alert">&times;</a>
    <strong>成功！</strong>结果是成功的。
</div>

<script>
```


$(function(){
    $("#myAlert").bind('closed.bs.alert', function () {
        alert("警告消息框被关闭。");
    });
});
</script>


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-plugin-alert-event)


结果如下所示：


![警告框（Alert）插件事件](https://www.runoob.com/wp-content/uploads/2014/07/alertpluginevents_demo.jpg)








	  AI 思考中...





			** [Bootstrap 弹出框（Popover）插件](https://www.runoob.com/bootstrap-popover-plugin.html)
			[Bootstrap 按钮（Button）插件](https://www.runoob.com/bootstrap-button-plugin.html) **













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
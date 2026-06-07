# Bootstrap 进度条

- Source: https://www.runoob.com/bootstrap/bootstrap-progress-bars.html

本章将讲解 Bootstrap 进度条。在本教程中，您将看到如何使用 Bootstrap 创建加载、重定向或动作状态的进度条。

**![](https://www.runoob.com/images/quote.png)Bootstrap 进度条使用 CSS3 过渡和动画来获得该效果。Internet Explorer 9 及之前的版本和旧版的 Firefox 不支持该特性，Opera 12 不支持动画。


## 默认的进度条


创建一个基本的进度条的步骤如下：


- 添加一个带有 class **.progress** 的 。
- 接着，在上面的  内，添加一个带有 class **.progress-bar** 的空的 。
- 添加一个带有百分比表示的宽度的 style 属性，例如 style="width: 60%"; 表示进度条在 60% 的位置。


让我们看看下面的实例，**.sr-only** 类可以隐藏文本内容：


## 实例


```css
<div class="progress">
    <div class="progress-bar" role="progressbar" aria-valuenow="60"
        aria-valuemin="0" aria-valuemax="100" style="width: 40%;">
        <span class="sr-only">40% 完成</span>
    </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-progressbar)


结果如下所示：


![进度条](https://www.runoob.com/wp-content/uploads/2014/06/progressbar_demo.jpg)


也可以在进度条中设置文本内容：


## 实例


```css
<div class="progress">
  <div class="progress-bar" role="progressbar" aria-valuenow="70"
  aria-valuemin="0" aria-valuemax="100" style="width:70%">
    70%
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-progressbar2)


结果如下所示：


![进度条](https://www.runoob.com/wp-content/uploads/2014/06/DD1BF526-648A-4270-B044-7AEC8FE446EF.jpg)


## 交替的进度条


创建不同样式的进度条的步骤如下：


- 添加一个带有 class **.progress** 的 。
- 接着，在上面的  内，添加一个带有 class **.progress-bar** 和 class **progress-bar-*** 的空的 。其中，* 可以是 **success、info、warning、danger**。
- 添加一个带有百分比表示的宽度的 style 属性，例如 style="60%"; 表示进度条在 60% 的位置。


让我们看看下面的实例：


## 实例


```css
<div class="progress">
    <div class="progress-bar progress-bar-success" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 90%;">
        <span class="sr-only">90% 完成（成功）</span>
    </div>
</div>
<div class="progress">
    <div class="progress-bar progress-bar-info" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 30%;">
        <span class="sr-only">30% 完成（信息）</span>
    </div>
</div>
<div class="progress">
    <div class="progress-bar progress-bar-warning" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 20%;">
        <span class="sr-only">20% 完成（警告）</span>
    </div>
</div>
<div class="progress">
    <div class="progress-bar progress-bar-danger" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 10%;">
        <span class="sr-only">10% 完成（危险）</span>
    </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-progressbar-alternate)


结果如下所示：


![交替的进度条](https://www.runoob.com/wp-content/uploads/2014/06/alternateprogressbar_demo.jpg)


显示进度条文本内容：


## 实例


```css
<div class="progress">
  <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="40"
  aria-valuemin="0" aria-valuemax="100" style="width:40%">
    40% Complete (success)
  </div>
</div>

<div class="progress">
  <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="50"
  aria-valuemin="0" aria-valuemax="100" style="width:50%">
    50% Complete (info)
  </div>
</div>

<div class="progress">
  <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="60"
  aria-valuemin="0" aria-valuemax="100" style="width:60%">
    60% Complete (warning)
  </div>
</div>

<div class="progress">
  <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="70"
  aria-valuemin="0" aria-valuemax="100" style="width:70%">
    70% Complete (danger)
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-progressbar-alternate2)


结果如下所示：


![交替的进度条](https://www.runoob.com/wp-content/uploads/2014/06/748A2918-2D67-435C-B544-250367389191.jpg)


## 条纹的进度条


创建一个条纹的进度条的步骤如下：


- 添加一个带有 class **.progress** 和 **.progress-striped** 的 。
- 接着，在上面的  内，添加一个带有 class **.progress-bar** 和 class **progress-bar-*** 的空的 。其中，* 可以是 **success、info、warning、danger**。
- 添加一个带有百分比表示的宽度的 style 属性，例如 style="60%"; 表示进度条在 60% 的位置。


让我们看看下面的实例：


## 实例


```css
<div class="progress progress-striped">
    <div class="progress-bar progress-bar-success" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 90%;">
        <span class="sr-only">90% 完成（成功）</span>
    </div>
</div>
<div class="progress progress-striped">
    <div class="progress-bar progress-bar-info" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 30%;">
        <span class="sr-only">30% 完成（信息）</span>
    </div>
</div>
<div class="progress progress-striped">
    <div class="progress-bar progress-bar-warning" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 20%;">
        <span class="sr-only">20% 完成（警告）</span>
    </div>
</div>
<div class="progress progress-striped">
    <div class="progress-bar progress-bar-danger" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 10%;">
        <span class="sr-only">10% 完成（危险）</span>
    </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-progressbar-striped)


结果如下所示：


![条纹的进度条](https://www.runoob.com/wp-content/uploads/2014/06/stripedprogressbar_demo.jpg)


## 动画的进度条


创建一个动画的进度条的步骤如下：


- 添加一个带有 class **.progress** 和 **.progress-striped** 的 。同时添加 class **.active**。
- 接着，在上面的  内，添加一个带有 class **.progress-bar** 的空的 。
- 添加一个带有百分比表示的宽度的 style 属性，例如 style="60%"; 表示进度条在 60% 的位置。


这将会使条纹具有从右向左的运动感。


让我们看看下面的实例：


## 实例


```css
<div class="progress progress-striped active">
    <div class="progress-bar progress-bar-success" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 40%;">
        <span class="sr-only">40% 完成</span>
    </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-progressbar-animated)


结果如下所示：


![动画的进度条](https://www.runoob.com/wp-content/uploads/2014/06/animatedprogressbar_demo.jpg)


## 堆叠的进度条


您甚至可以堆叠多个进度条。把多个进度条放在相同的 .progress** 中即可实现堆叠，如下面的实例所示：


## 实例


```css
<div class="progress">
    <div class="progress-bar progress-bar-success" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 40%;">
        <span class="sr-only">40% 完成</span>
    </div>
    <div class="progress-bar progress-bar-info" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 30%;">
        <span class="sr-only">30% 完成（信息）</span>
    </div>
    <div class="progress-bar progress-bar-warning" role="progressbar"
         aria-valuenow="60" aria-valuemin="0" aria-valuemax="100"
         style="width: 20%;">
        <span class="sr-only">20% 完成（警告）</span>
    </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-progressbar-stacked)


结果如下所示：


![堆叠的进度条](https://www.runoob.com/wp-content/uploads/2014/06/stackedprogressbar_demo.jpg)


---

## 进度条大小


我们可以通过通过 height 属性来设置进度条的大小：


## 实例


```css
<div class="progress" style="height: 1px;">
  <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>
<div class="progress" style="height: 20px;">
  <div class="progress-bar" role="progressbar" style="width: 25%;" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-progressbar-height)


结果如下所示：


![堆叠的进度条](https://www.runoob.com/wp-content/uploads/2014/06/D921493C-FABD-4A96-A53C-E82E7F538231.jpg)









	  AI 思考中...





			** [Bootstrap 警告](https://www.runoob.com/bootstrap-alerts.html)
			[Bootstrap 多媒体对象](https://www.runoob.com/bootstrap-media-object.html) **













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
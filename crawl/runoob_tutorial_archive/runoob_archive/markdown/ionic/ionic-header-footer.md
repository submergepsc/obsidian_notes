# ionic 头部与底部

- Source: https://www.runoob.com/ionic/ionic-header-footer.html

---


## Header(头部)


Header是固定在屏幕顶部的组件,可以包如标题和左右的功能按钮。


ionic 默认提供了许多种颜色样式，你可以调用不同的样式名，当然也可以自定义一个。


### bar-light


```
<div class="bar bar-header bar-light">
  <h1 class="title">bar-light</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_bar-light)


### bar-stable


```
<div class="bar bar-header bar-stable">
  <h1 class="title">bar-stable</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_bar-stable)


### bar-positive


```
<div class="bar bar-header bar-positive">
  <h1 class="title">bar-positive</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_bar-positive)


### bar-calm


```
<div class="bar bar-header bar-calm">
  <h1 class="title">bar-calm</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_bar-calm)


### bar-balanced


```
<div class="bar bar-header bar-balanced">
  <h1 class="title">bar-balanced</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_bar-balanced)


### bar-energized


```
<div class="bar bar-header bar-energized">
  <h1 class="title">bar-energized</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_bar-energized)


### bar-assertive


```
<div class="bar bar-header bar-assertive">
  <h1 class="title">bar-assertive</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_bar-assertive)


### bar-royal


```
<div class="bar bar-header bar-royal">
  <h1 class="title">bar-royal</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_bar-royal)


### bar-dark


```
<div class="bar bar-header bar-dark">
  <h1 class="title">bar-dark</h1>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_header_bar-dark)


---


## Sub Header（副标题）


Sub Header同样是固定在顶部，只是是在Header的下面，就算没有写Header这个，Sub Header这个样式也会距离顶部有一个Header的距离。颜色样式同 Header 。


```
<div class="bar bar-header">
  <h1 class="title">Header</h1>
</div>
<div class="bar bar-subheader">
  <h2 class="title">Sub Header</h2>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_sub_header)


---


## Footer(底部)


Footer 是在屏幕的最下方，可以包含多种内容类型。


```
<div class="bar bar-footer bar-balanced">
  <div class="title">Footer</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_footer)


Footer 同上面的 Header，只是把样式名 bar-header 换做 bar-footer 。


```
<div class="bar bar-footer">
  <button class="button button-clear">Left</button>
  <div class="title">Title</div>
  <button class="button button-clear">Right</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_bar_footer)


此外，如果底部没有标题，但是又需要右边的按钮，你需要在右侧按钮添加 pull-right如:


```
<div class="bar bar-footer">
  <button class="button button-clear pull-right">Right</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_bar_footer_pull-right)








	  AI 思考中...





			** [ionic 创建 APP](https://www.runoob.com/ionic-creat-app.html)
			[ionic 按钮](https://www.runoob.com/ionic-button.html) **













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
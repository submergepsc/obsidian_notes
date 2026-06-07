# ionic 按钮

- Source: https://www.runoob.com/ionic/ionic-button.html

按钮是移动app不可或缺的一部分，不同风格的app，需要的不同按钮的样式。


默认情况下，按钮显示样式为：**display: inline-block**。


```
<button class="button">
  Default
</button>

<button class="button button-light">
  button-light
</button>

<button class="button button-stable">
  button-stable
</button>

<button class="button button-positive">
  button-positive
</button>

<button class="button button-calm">
  button-calm
</button>

<button class="button button-balanced">
  button-balanced
</button>

<button class="button button-energized">
  button-energized
</button>

<button class="button button-assertive">
  button-assertive
</button>

<button class="button button-royal">
  button-royal
</button>

<button class="button button-dark">
  button-dark
</button>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_button)


button-block 样式按钮显示为：**display: block**，它将完全填充父元素的宽度，包含了内边距属性padding。


```
<button class="button button-block button-positive">
  Block Button
</button>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_button-block)


使用 button-full 类，可以让按钮显示完全宽度，且不包含内边距padding。


```
<button class="button button-full button-positive">
  Full Width Block Button
</button>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_button-full)


---


## 不同大小的按钮


button-large 设置为大按钮，button-small 设置为小按钮。


```
<button class="button button-small button-assertive">
  Small Button
</button>
<button class="button button-large button-positive">
  Large Button
</button>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_button-size)


---


## 无背景按钮


button-outline 设置背景为透明。


```
<button class="button button-outline button-positive">
  Outlined Button
</button>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_button-outline)


---


## 无背景与边框按钮


button-clear 设置按钮背景为透明，且无边框。


```
<button class="button button-clear button-positive">
  Clear Button
</button>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_button-clear)


---


## 图标按钮


我们可以在按钮上添加图标。


```
<button class="button icon-left ion-home">Home</button>

<button class="button icon-left ion-star button-positive">Favorites</button>

<a class="button icon-right ion-chevron-right button-calm">Learn More</a>

<a class="button icon-left ion-chevron-left button-clear button-dark">Back</a>

<button class="button icon ion-gear-a"></button>

<a class="button button-icon icon ion-settings"></a>

<a class="button button-outline icon-right ion-navicon button-balanced">Reorder</a>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_bar-header_icon)


---


## 头部/底部添加按钮


头部/底部可以添加按钮，按钮的样式根据头部/底部来设定，所以你不需要为按钮添加额外的样式。


```
<div class="bar bar-header">
  <button class="button icon ion-navicon"></button>
  <h1 class="title">Header Buttons</h1>
  <button class="button">Edit</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_bar-header)


button-clear 类可以设置无背景和边框的头部/底部按钮。


```
<div class="bar bar-header">
  <button class="button button-icon icon ion-navicon"></button>
  <div class="h1 title">Header Buttons</div>
  <button class="button button-clear button-positive">Edit</button>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_bar-header_button-clear)


---


## 按钮栏

我们可以使用 button-bar 类来设置按钮栏。以下实例中，我们在头部和内容中添加了按钮栏。


```
<div class="button-bar">
  <a class="button">First</a>
  <a class="button">Second</a>
  <a class="button">Third</a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_button-bar)








	  AI 思考中...





			** [ionic 头部与底部](https://www.runoob.com/ionic-header-footer.html)
			[ionic 列表](https://www.runoob.com/ionic-list.html) **













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
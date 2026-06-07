# ionic 网格(Grid)

- Source: https://www.runoob.com/ionic/ionic-grid.html

ionic 的网格(Grid)和其他大部分框架有所不同，它采用了弹性盒子模型(Flexible Box Model) 。而且在移动端，基本上的手机都支持。row 样式指定行，col 样式指定列。


### 同等大小网格 在带有 row 的样式的元素里如果包含了 col 的样式，col 就会设置为同等大小。 以下实例中 row 的样式包含了 5 个 col 样式，每个 col 的宽度为 20%。
```
<div class="row">
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
</div>
```
 尝试一下 » 指定列宽


你可以设定一行中各个列的大小不一样。默认情况下，列都会被划分为同等大小。但你也可以按百分比来设置列的宽度（一行为 12 个网格）。


```
<div class="row">
  <div class="col col-50">.col.col-50</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
</div>

<div class="row">
  <div class="col col-75">.col.col-75</div>
  <div class="col">.col</div>
</div>

<div class="row">
  <div class="col">.col</div>
  <div class="col col-75">.col.col-75</div>
</div>

<div class="row">
  <div class="col">.col</div>
  <div class="col">.col</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_col_percent)


注意：实例中，每个 col 样式会自动添加上边框和灰色背景。


下面列出了指定列宽的一些百分比的样式名:


| .col-10 | 10% |
| --- | --- |
| .col-20 | 20% |
| .col-25 | 25% |
| .col-33 | 33.3333% |
| .col-50 | 50% |
| .col-67 | 66.6666% |
| .col-75 | 75% |
| .col-80 | 80% |
| .col-90 | 90% |


### 有偏移量的网格


列可以设置左侧偏移量，实例如下：


```
<div class="row">
  <div class="col col-33 col-offset-33">.col</div>
  <div class="col">.col</div>
</div>

<div class="row">
  <div class="col col-33">.col</div>
  <div class="col col-33 col-offset-33">.col</div>
</div>

<div class="row">
  <div class="col col-33 col-offset-67">.col</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_col_offset)


下面是一些百分比的偏移量样式名：


| .col-offset-10 | 10% |
| --- | --- |
| .col-offset-20 | 20% |
| .col-offset-25 | 25% |
| .col-offset-33 | 33.3333% |
| .col-offset-50 | 50% |
| .col-offset-67 | 66.6666% |
| .col-offset-75 | 75% |
| .col-offset-80 | 80% |
| .col-offset-90 | 90% |


---


## 纵向对齐网格


弹性盒子模型可以很容易设置列纵向对齐。纵向对齐包含顶部，中间部分，底部，可以应用到每一行的列，或者指定的某列。


实例中，最后一列设置了最高的内容用于更好的演示纵向对齐网格。


```
<div class="row">
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">1<br>2<br>3<br>4</div>
</div>

<div class="row">
  <div class="col col-top">.col</div>
  <div class="col col-center">.col</div>
  <div class="col col-bottom">.col</div>
  <div class="col">1<br>2<br>3<br>4</div>
</div>

<div class="row row-top">
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">1<br>2<br>3<br>4</div>
</div>

<div class="row row-center">
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">1<br>2<br>3<br>4</div>
</div>

<div class="row row-bottom">
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">1<br>2<br>3<br>4</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_grid_vertically_align)


---


## 响应式网格


手持设备屏幕在切换时，例如横屏，竖屏等。就需要设置每行的网格可以实现根据不同宽度自适应大小。


不同设备响应式类的样式如下:


| 响应式类 | 描述 |
| --- | --- |
| .responsive-sm | 小于手机横屏 |
| .responsive-md | 小于平板竖屏 |
| .responsive-lg | 小于平板横屏 |


```
<div class="row responsive-sm">
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
  <div class="col">.col</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_grid_responsive)









	  AI 思考中...





			** [ionic tab(选项卡)](https://www.runoob.com/ionic-tab.html)
			[ionic 颜色](https://www.runoob.com/ionic-color.html) **













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
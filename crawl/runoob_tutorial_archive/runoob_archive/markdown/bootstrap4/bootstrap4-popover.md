# Bootstrap4 弹出框

- Source: https://www.runoob.com/bootstrap4/bootstrap4-popover.html

弹出框控件类似于提示框，它在鼠标点击到元素后显示，与提示框不同的是它可以显示更多的内容。


---


## 如何创建弹出框


通过向元素添加 **data-toggle="popover"** 来来创建弹出框。


**title** 属性的内容为弹出框的标题，**data-content** 属性显示了弹出框的文本内容：


```css
<a href="#" data-toggle="popover" title="弹出框标题" data-content="弹出框内容">多次点我</a>
```


**注意:** 弹出框要写在 jQuery 的初始化代码里: 然后在指定的元素上调用 **popover()** 方法。


以下实例可以在文档的任何地方使用弹出框：


## 实例


```css
$(document).ready(function(){
    $('[data-toggle="popover"]').popover();
});
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_popover)

---


## 指定弹出框的位置


默认情况下弹出框显示在元素右侧。


可以使用 **data-placement** 属性来设定弹出框显示的方向: top, bottom, left 或 right:


## 实例


```css
<a href="#" title="Header" data-toggle="popover" data-placement="top" data-content="Content">点我</a>
<a href="#" title="Header" data-toggle="popover" data-placement="bottom" data-content="Content">点我</a>
<a href="#" title="Header" data-toggle="popover" data-placement="left" data-content="Content">点我</a>
<a href="#" title="Header" data-toggle="popover" data-placement="right" data-content="Content">点我</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_popover_pos)

按钮中使用:


## 实例


```css
<button type="button" class="btn btn-secondary" data-container="body" data-toggle="popover" data-placement="top" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus.">
  Popover on top
</button>

<button type="button" class="btn btn-secondary" data-container="body" data-toggle="popover" data-placement="right" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus.">
  Popover on right
</button>

<button type="button" class="btn btn-secondary" data-container="body" data-toggle="popover" data-placement="bottom" data-content="Vivamus
sagittis lacus vel augue laoreet rutrum faucibus.">
  Popover on bottom
</button>

<button type="button" class="btn btn-secondary" data-container="body" data-toggle="popover" data-placement="left" data-content="Vivamus sagittis lacus vel augue laoreet rutrum faucibus.">
  Popover on left
</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_popover_pos2)


---


## 关闭弹出框


默认情况下，弹出框在再次点击指定元素后就会关闭，你可以使用 **data-trigger="focus"** 属性来设置在鼠标点击元素外部区域来关闭弹出框：


## 实例


```css
<a href="#" title="取消弹出框" data-toggle="popover" data-trigger="focus" data-content="点击文档的其他地方关闭我">点我</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_popover_focus)

提示:**如果你想实现在鼠标移动到元素上显示，移除后消失的效果，可以使用 **data-trigger** 属性，并设置值为 "hover":


## 实例


```css
<a href="#" title="Header" data-toggle="popover" data-trigger="hover" data-content="一些内容">鼠标移动到我这</a>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_popover_hover)







	  AI 思考中...





			** [Bootstrap4 提示框](https://www.runoob.com/bootstrap4-tooltip.html)
			[Bootstrap4 滚动监听](https://www.runoob.com/bootstrap4-scrollspy.html) **













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
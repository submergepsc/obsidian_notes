# Bootstrap4 提示框

- Source: https://www.runoob.com/bootstrap4/bootstrap4-tooltip.html

提示框是一个小小的弹窗，在鼠标移动到元素上显示，鼠标移到元素外就消失。


---


## 如何创建提示框


通过向元素添加 **data-toggle="tooltip"** 来来创建提示框。


**title** 属性的内容为提示框显示的内容：


```css
<a href="#" data-toggle="tooltip" title="我是提示内容!">鼠标移动到我这</a>
```


**注意:** 提示框要写在 jQuery 的初始化代码里: 然后在指定的元素上调用 **tooltip()** 方法。


以下实例可以在文档的任何地方使用提示框：


## 实例


```css
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();
});
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_tooltip)

---


## 指定提示框的位置


默认情况下提示框显示在元素上方。


可以使用 **data-placement** 属性来设定提示框显示的方向: top, bottom, left 或 right:


## 实例


```css
<a href="#" data-toggle="tooltip" data-placement="top" title="我是提示内容!">鼠标移动到我这</a>
<a href="#" data-toggle="tooltip" data-placement="bottom" title="我是提示内容!">鼠标移动到我这</a>
<a href="#" data-toggle="tooltip" data-placement="left" title="我是提示内容!">鼠标移动到我这</a>
<a href="#" data-toggle="tooltip" data-placement="right" title="我是提示内容!">鼠标移动到我这</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_tooltip_pos)


在按钮中使用:


## 实例


```css
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="top" title="Tooltip on top">
  Tooltip on top
</button>
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="right" title="Tooltip on right">
  Tooltip on right
</button>
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="bottom" title="Tooltip on bottom">
  Tooltip on bottom
</button>
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-placement="left" title="Tooltip on left">
  Tooltip on left
</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_tooltip_pos2)


提示内容添加 HTML 标签，设置 data-html="true"，内容放在 title 标签里头:


## 实例


```css
<button type="button" class="btn btn-secondary" data-toggle="tooltip" data-html="true" title="<em>Tooltip</em> <u>with</u> <b>HTML</b>">
  Tooltip with HTML
</button>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_tooltip_pos3)


禁用按钮：


## 实例


```css
<span class="d-inline-block" tabindex="0" data-toggle="tooltip" title="Disabled tooltip">
  <button class="btn btn-primary" style="pointer-events: none;" type="button" disabled>Disabled button</button>
</span>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_tooltip_pos4)









	  AI 思考中...





			** [Bootstrap4 模态框](https://www.runoob.com/bootstrap4-modal.html)
			[Bootstrap4 弹出框](https://www.runoob.com/bootstrap4-popover.html) **













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
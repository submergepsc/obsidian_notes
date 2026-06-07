# CSS 布局 - Overflow

- Source: https://www.runoob.com/css/css-overflow.html

CSS overflow 属性用于控制内容溢出元素框时显示的方式。


这里的文本内容是可以滚动的，滚动条方向是垂直方向。


这里的文本内容是可以滚动的，滚动条方向是垂直方向。


这里的文本内容是可以滚动的，滚动条方向是垂直方向。


这里的文本内容是可以滚动的，滚动条方向是垂直方向。


这里的文本内容是可以滚动的，滚动条方向是垂直方向。


这里的文本内容是可以滚动的，滚动条方向是垂直方向。


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_overflow_intro)


---


## CSS Overflow


CSS overflow 属性可以控制内容溢出元素框时在对应的元素区间内添加滚动条。


overflow属性有以下值：


| 值 | 描述 |
| --- | --- |
| visible | 默认值。内容不会被修剪，会呈现在元素框之外。 |
| hidden | 内容会被修剪，并且其余内容是不可见的。 |
| scroll | 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。 |
| auto | 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。 |
| inherit | 规定应该从父元素继承 overflow 属性的值。 |


**注意:**overflow 属性只工作于指定高度的块元素上。


**注意:** 在 OS X Lion ( Mac 系统) 系统上，滚动条默认是隐藏的，使用的时候才会显示 (设置 "overflow:scroll" 也是一样的)。


## overflow: visible


默认情况下，overflow 的值为 visible， 意思是内容溢出元素框：


这里的文本内容会溢出元素框。


这里的文本内容会溢出元素框。


这里的文本内容会溢出元素框。


这里的文本内容会溢出元素框。


这里的文本内容会溢出元素框。


这里的文本内容会溢出元素框。


这里的文本内容会溢出元素框。


## 实例


```css
div {
    width: 200px;
    height: 50px;
    background-color: #eee;
    overflow: visible;
}
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_overflow_visible)









	  AI 思考中...





			** [CSS 提示工具(Tooltip)](https://www.runoob.com/css-tooltip.html)
			[CSS 表单](https://www.runoob.com/css-form.html) **













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

      : ·[CSS 实例](https://www.runoob.com/css-examples.html)

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
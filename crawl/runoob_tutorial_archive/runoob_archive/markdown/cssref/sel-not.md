# CSS3 :not 选择器

- Source: https://www.runoob.com/cssref/sel-not.html

[![CSS完整选择器](https://www.runoob.com/images/up.gif)完整CSS选择器参考手册](https://www.runoob.com/css-selectors.html)


## 实例


为每个并非  元素的元素设置背景颜色：


```css
:not(p) {
    color: #ff0000;
}
```



**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_not)


---


## 定义和用法


:not(selector) 选择器匹配每个元素是不是指定的元素/选择器。

CSS 的 :not 伪类允许你选择除了指定选择器之外的所有元素。这是通过排除特定元素来应用样式的一种方式。


### 基本语法


```
css
:not(selector) {
  /* 样式规则 */
}
```


- selector：这是你想要排除的选择器。


1、排除特定类型的元素**


```
body :not(p) {
  color: blue;
}
```


这段代码将为 body 元素内除了 p 元素之外的所有元素设置文本颜色为蓝色。


**2、排除具有特定类的元素**


```
div :not(.highlight) {
  background-color: gray;
}
```


这段代码将为 div 元素内不具有 highlight 类的所有元素设置背景颜色为灰色。


** 3、排除多个选择器**


```
:not(div, span) {
  font-size: 14px;
}
```


这段代码将为页面上不是 div 也不是 span 的所有元素设置字体大小为 14 像素。


**4、排除伪类**


```
a:not(:hover) {
  color: black;
}
```


这段代码将为所有不是悬停状态的链接设置文本颜色为黑色。


** 5、排除属性选择器**


```
input:not([type="text"]) {
  border: none;
}
```


这段代码将为所有不是 type="text" 的 input 元素移除边框。


### 注意


- `:not` 伪类是 CSS3 选择器的一部分，并且得到了广泛的浏览器支持。
- `:not` 伪类可以提高 CSS 代码的灵活性，允许你更精确地控制样式的应用。
- 你可以在 `:not` 伪类中使用单个选择器或多个选择器，用逗号分隔。


---


## 浏览器支持


表格中的数字表示支持该选择器的第一个浏览器的版本号。


| 选择器 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| :not() | 4.0 | 9.0 | 3.5 | 3.2 | 9.6 |


---


[![CSS完整选择器](https://www.runoob.com/images/up.gif)完整CSS选择器参考手册](https://www.runoob.com/css-selectors.html)








	  AI 思考中...





			** [CSS3 :checked 选择器](https://www.runoob.com/sel-checked.html)
			[CSS3 ::selection 选择器](https://www.runoob.com/sel-selection.html) **













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
# CSS3 多媒体查询

- Source: https://www.runoob.com/css3/css3-mediaqueries.html

---


## CSS2 多媒体类型


`@media` 规则在 CSS2 中有介绍，针对不同媒体类型可以定制不同的样式规则。


例如：你可以针对不同的媒体类型(包括显示器、便携设备、电视机，等等)设置不同的样式规则。


但是这些多媒体类型在很多设备上支持还不够友好。


---


## CSS3 多媒体查询


CSS3 的多媒体查询继承了 CSS2 多媒体类型的所有思想： 取代了查找设备的类型，CSS3 根据设置自适应显示。


媒体查询可用于检测很多事情，例如：


- viewport(视窗) 的宽度与高度
- 设备的宽度与高度
- 朝向 (智能手机横屏，竖屏) 。
- 分辨率


目前很多针对苹果手机，Android 手机，平板等设备都会使用到多媒体查询。


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器的版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| @media | 21.0 | 9.0 | 3.5 | 4.0 | 9.0 |


---


## 多媒体查询语法


多媒体查询由多种媒体组成，可以包含一个或多个表达式，表达式根据条件是否成立返回 true 或 false。


```css
@media not|only mediatype and (expressions) {
    CSS 代码...;
}
```


如果指定的多媒体类型匹配设备类型则查询结果返回 true，文档会在匹配的设备上显示指定样式效果。


除非你使用了 not 或 only 操作符，否则所有的样式会适应在所有设备上显示效果。


- **not:** not是用来排除掉某些特定的设备的，比如 @media not print（非打印设备）。
- **only:** 用来定某种特别的媒体类型。对于支持Media Queries的移动设备来说，如果存在only关键字，移动设备的Web浏览器会忽略only关键字并直接根据后面的表达式应用样式文件。对于不支持Media Queries的设备但能够读取Media Type类型的Web浏览器，遇到only关键字时会忽略这个样式文件。
- **all:** 所有设备，这个应该经常看到。


你也可以在不同的媒体上使用不同的样式文件：


```css
<link rel="stylesheet" media="mediatype and|not|only (expressions)" href="print.css">
```


---


## CSS3 多媒体类型


| 值 | 描述 |
| --- | --- |
| all | 用于所有多媒体类型设备 |
| print | 用于打印机 |
| screen | 用于电脑屏幕，平板，智能手机等。 |
| speech | 用于屏幕阅读器 |


---


## 多媒体查询简单实例


使用多媒体查询可以在指定的设备上使用对应的样式替代原有的样式。


以下实例中在屏幕可视窗口尺寸小于 480 像素的设备上修改背景颜色:


### 实例


```css
@media screen and (max-width: 480px) {
    body {
        background-color: lightgreen;
    }
}
```


**
	[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_media_queries1)


以下实例在屏幕可视窗口尺寸大于 480 像素时将菜单浮动到页面左侧：


### 实例


```css
@media screen and (min-width: 480px) {
    #leftsidebar {width: 200px; float: left;}
    #main {margin-left:216px;}
}
```


	[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_media_queries2)


以下实例在屏幕可视窗口尺寸小于 600 像素时将 div 元素隐藏：


### 实例


```css
@media screen and (max-width: 600px) {
  div.example {
    display: none;
  }
}
```


	[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_media_queries3)


---


## CSS3 @media 参考


更多多媒体查询内容可以参考 [@media](https://www.runoob.com/../cssref/css3-pr-mediaquery.html) 规则。








	  AI 思考中...





			** [CSS3 弹性盒子](https://www.runoob.com/css3-flexbox.html)
			[CSS3 多媒体查询实例](https://www.runoob.com/css3-mediaqueries-ex.html) **













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
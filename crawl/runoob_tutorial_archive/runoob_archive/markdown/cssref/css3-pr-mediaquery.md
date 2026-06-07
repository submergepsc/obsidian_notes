# CSS3 @media 查询

- Source: https://www.runoob.com/cssref/css3-pr-mediaquery.html

**


## 实例


如果文档宽度小于 300 像素则修改背景颜色(background-color):


```css
@media screen and (max-width: 300px) {    body {

	background-color:lightblue;    }}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trycss3_media_example1)


---


## 定义和使用


使用 @media 查询，你可以针对不同的媒体类型定义不同的样式。


@media 可以针对不同的屏幕尺寸设置不同的样式，特别是如果你需要设置设计响应式的页面，@media 是非常有用的。


当你重置浏览器大小的过程中，页面也会根据浏览器的宽度和高度重新渲染页面。


---


## 浏览器支持


表格中的数字表示支持 @media 规则的第一个浏览器的版本号。


| 规则 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| @media | 21 | 9 | 3.5 | 4.0 | 9 |


---


## CSS 语法


```
@media not|only mediatype and (mediafeature and|or|not mediafeature) {
  CSS-Code;
}
```


not, and, 和 only 可用于联合构造复杂的媒体查询，您还可以通过用逗号分隔多个媒体查询，将它们组合为一个规则。


not, only 和 and 关键字含义:


- **not**: not 运算符用于否定媒体查询，如果不满足这个条件则返回 true，否则返回 false。 如果出现在以逗号分隔的查询列表中，它将仅否定应用了该查询的特定查询。 如果使用 not 运算符，则还必须指定媒体类型。
- **only**: only 运算符仅在整个查询匹配时才用于应用样式，并且对于防止较早的浏览器应用所选样式很有用。 当不使用 only 时，旧版本的浏览器会将 screen and (max-width: 500px) 简单地解释为 screen，忽略查询的其余部分，并将其样式应用于所有屏幕。 如果使用 only 运算符，则还必须指定媒体类型。
- **,** (逗号) 逗号用于将多个媒体查询合并为一个规则。 逗号分隔列表中的每个查询都与其他查询分开处理。 因此，如果列表中的任何查询为 true，则整个 media 语句均返回 true。 换句话说，列表的行为类似于逻辑或 or 运算符。
- **and**: and 操作符用于将多个媒体查询规则组合成单条媒体查询，当每个查询规则都为真时则该条媒体查询为真，它还用于将媒体功能与媒体类型结合在一起。


媒体类型（Media types）描述设备的一般类别。除非使用 not 或 only 逻辑操作符，媒体类型是可选的，并且会（隐式地）应用 all 类型。


你也可以针对不同的媒体使用不同样式文件 :


```
<!-- 宽度大于 900px 的屏幕使用该样式 -->
<link rel="stylesheet" media="screen and (min-width: 900px)" href="widescreen.css">
<!-- 宽度小于或等于 600px 的屏幕使用该样式 -->
<link rel="stylesheet" media="screen and (max-width: 600px)" href="smallscreen.css">
....
```


## 媒体类型


| 值 | 描述 |
| --- | --- |
| all | 用于所有设备 |
| aural | 已废弃。用于语音和声音合成器 |
| braille | 已废弃。 应用于盲文触摸式反馈设备 |
| embossed | 已废弃。 用于打印的盲人印刷设备 |
| handheld | 已废弃。 用于掌上设备或更小的装置，如PDA和小型电话 |
| print | 用于打印机和打印预览 |
| projection | 已废弃。 用于投影设备 |
| screen | 用于电脑屏幕，平板电脑，智能手机等。 |
| speech | 应用于屏幕阅读器等发声设备 |
| tty | 已废弃。 用于固定的字符网格，如电报、终端设备和对字符有限制的便携设备 |
| tv | 已废弃。 用于电视和网络电视 |


## 媒体功能


| 值 | 描述 |
| --- | --- |
| aspect-ratio | 定义输出设备中的页面可见区域宽度与高度的比率 |
| color | 定义输出设备每一组彩色原件的个数。如果不是彩色设备，则值等于0 |
| color-index | 定义在输出设备的彩色查询表中的条目数。如果没有使用彩色查询表，则值等于0 |
| device-aspect-ratio | 定义输出设备的屏幕可见宽度与高度的比率。 |
| device-height | 定义输出设备的屏幕可见高度。 |
| device-width | 定义输出设备的屏幕可见宽度。 |
| grid | 用来查询输出设备是否使用栅格或点阵。 |
| height | 定义输出设备中的页面可见区域高度。 |
| max-aspect-ratio | 定义输出设备的屏幕可见宽度与高度的最大比率。 |
| max-color | 定义输出设备每一组彩色原件的最大个数。 |
| max-color-index | 定义在输出设备的彩色查询表中的最大条目数。 |
| max-device-aspect-ratio | 定义输出设备的屏幕可见宽度与高度的最大比率。 |
| max-device-height | 定义输出设备的屏幕可见的最大高度。 |
| max-device-width | 定义输出设备的屏幕最大可见宽度。 |
| max-height | 定义输出设备中的页面最大可见区域高度。 |
| max-monochrome | 定义在一个单色框架缓冲区中每像素包含的最大单色原件个数。 |
| max-resolution | 定义设备的最大分辨率。 |
| max-width | 定义输出设备中的页面最大可见区域宽度。 |
| min-aspect-ratio | 定义输出设备中的页面可见区域宽度与高度的最小比率。 |
| min-color | 定义输出设备每一组彩色原件的最小个数。 |
| min-color-index | 定义在输出设备的彩色查询表中的最小条目数。 |
| min-device-aspect-ratio | 定义输出设备的屏幕可见宽度与高度的最小比率。 |
| min-device-width | 定义输出设备的屏幕最小可见宽度。 |
| min-device-height | 定义输出设备的屏幕的最小可见高度。 |
| min-height | 定义输出设备中的页面最小可见区域高度。 |
| min-monochrome | 定义在一个单色框架缓冲区中每像素包含的最小单色原件个数 |
| min-resolution | 定义设备的最小分辨率。 |
| min-width | 定义输出设备中的页面最小可见区域宽度。 |
| monochrome |  |
| orientation | 定义输出设备中的页面可见区域高度是否大于或等于宽度。 |
| resolution | 定义设备的分辨率。如：96dpi, 300dpi, 118dpcm |
| scan | 定义电视类设备的扫描工序。 |
| width | 定义输出设备中的页面可见区域宽度。 |


---


![实例](https://www.runoob.com/images/tryitimg.gif)

## 更多实例


## 实例


使用 @media 查询来制作响应式设计：


```css
@media only screen and (max-width: 500px) {    .gridmenu
	{        width:100%;    }    .gridmain
	{        width:100%;
	}    .gridright {
	width:100%;    }}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=trycss3_mediaquery)


### 更多实例

[CSS 多媒体查询，适配各种设备尺寸](https://c.runoob.com/codedemo/5371)


## 相关页面


CSS 教程: [CSS 媒体类型](https://www.runoob.com/../css/css-mediatypes.html)









	  AI 思考中...





			** [CSS unicode-bidi 属性](https://www.runoob.com/pr-text-unicode-bidi.html)
			[CSS all 属性](https://www.runoob.com/css3-pr-all.html) **













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
# CSS3 框大小

- Source: https://www.runoob.com/css3/css3-box-sizing.html

CSS3 `box-sizing` 属性可以设置 width 和 height 属性中包含了 padding(内边距) 和 border(边框)。


---

## 浏览器支持

表格中的数字表示支持该属性的第一个浏览器的版本号。

紧跟在数字后面的 -webkit- 或 -moz- 为指定浏览器的前缀。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| box-sizing | 10.04.0 -webkit- | 8.0 | 29.02.0 -moz- | 5.13.1 -webkit- | 9.5 |

---


## 不使用 CSS3 box-sizing 属性


默认情况下，元素的宽度与高度计算方式如下：


**width(宽) + padding(内边距) + border(边框) = 元素实际宽度**

** height(高) + padding(内边距) + border(边框) = 元素实际高度**


这就意味着我们在设置元素的 width/height 时，元素真实展示的高度与宽度会更大(因为元素的边框与内边距也会计算在 width/height 中)。


这个是个较小的框 (width 为 300px ，height 为 100px)。
**
这个是个较大的框 (width 为 300px ，height 为 100px)。


以上两个  元素虽然宽度与高度设置一样，但真实展示的大小不一致，因为 div2 指定了内边距:


### 实例


```css
.div1 {    width: 300px;    height:
	100px;    border: 1px solid blue; }
	.div2 {    width: 300px;
	height: 100px;    padding: 50px;
	border: 1px solid red;}
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_box-sizing_old)


使用这种方式如果想要获得较小的那个框且包含内边距，就不得不考虑到边框和内边距的宽度。


CSS3 的 `box-sizing` 属性很好的解决了这个问题。


---


## 使用 CSS3 box-sizing 属性


CSS3 `box-sizing` 属性在一个元素的 width 和 height 中包含 padding(内边距) 和 border(边框)。


如果在元素上设置了 `box-sizing: border-box;` 则 padding(内边距) 和 border(边框) 也包含在 width 和 height 中:


两个 div 现在是一样大小的!


菜鸟教程!


以下是两个  元素添加 `box-sizing: border-box;` 属性的简单实例。


### 实例


```css
.div1 {    width: 300px;    height:
	100px;    border: 1px solid blue;
	box-sizing: border-box;}
	.div2 {    width: 300px;
	height: 100px;    padding: 50px;
	border: 1px solid red;    box-sizing: border-box;}
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_box-sizing_new)


从结果上看 `box-sizing: border-box;` 效果更好，也正是很多开发人员需要的效果。


以下代码可以让所有元素以更直观的方式展示大小。很多浏览器已经支持 `box-sizing: border-box;` (但是并非所有 - 这就是为什么 input 和 text 元素设置了 width: 100%; 后的宽度却不一样)。


所有元素使用 box-sizing 是比较推荐的：


### 实例


```css
* {    box-sizing: border-box;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_box-sizing_all)










	  AI 思考中...





			** [CSS 分页实例](https://www.runoob.com/css3-pagination.html)
			[CSS3 弹性盒子](https://www.runoob.com/css3-flexbox.html) **













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
# CSS3 边框

- Source: https://www.runoob.com/css3/css3-borders.html

## CSS3 边框


用 CSS3，你可以创建圆角边框，添加阴影框，并作为边界的形象而不使用设计程序，如 Photoshop。


在本章中，您将了解以下的边框属性：


- border-radius
- box-shadow
- border-image


---


## CSS3 圆角


在 CSS2 中添加圆角棘手。我们不得不在每个角落使用不同的图像。


在 CSS3 中，很容易创建圆角。


在 CSS3 中 border-radius 属性被用于创建圆角：

这是圆角边框！
**
## 实例


在div中添加圆角元素：


```css
div
	{
	border:2px solid;
	border-radius:25px;
	}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_border-radius)


---


## CSS3 盒阴影


CSS3 中的 box-shadow 属性被用来添加阴影:


## 实例


在div中添加box-shadow属性


```css
div
	{
	box-shadow: 10px 10px 5px #888888;
	}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_box-shadow)


---


## CSS3 边界图片


有了 CSS3 的 border-image 属性，你可以使用图像创建一个边框：

border-image 属性允许你指定一个图片作为边框！
用于创建上文边框的原始图像：

在 div 中使用图片创建边框:

![Border](https://www.runoob.com/images/border.png)


## 实例


在 div 中使用图片创建边框


```css
div
	{
	border-image:url(border.png) 30 30 round;
	-webkit-border-image:url(border.png) 30 30 round; /* Safari 5 and older */
	-o-border-image:url(border.png) 30 30 round; /* Opera */
	}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_border-image)


---


## 新边框属性


| 属性 | 说明 | CSS |
| --- | --- | --- |
| border-image | 设置所有边框图像的速记属性。 | 3 |
| border-radius | 一个用于设置所有四个边框- *-半径属性的速记属性 | 3 |
| box-shadow | 附加一个或多个下拉框的阴影 | 3 |








	  AI 思考中...





			** [CSS3 简介](https://www.runoob.com/css3-intro.html)
			[CSS3 背景](https://www.runoob.com/css3-backgrounds.html) **













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
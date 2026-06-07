# CSS background 属性

- Source: https://www.runoob.com/cssref/css3-pr-background.html

**
## 实例


在一个div元素中设置多个背景图像（并指定他们的位置）：


```css
body
{
    background: #00ff00 url('smiley.gif') no-repeat fixed center;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_background)


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| background | 1.0 | 4.0 | 1.0 | 1.0 | 3.5 |


所有主流浏览器都支持 background 属性。


注意**：IE8和更早版本不支持一个元素多个背景图像。


**注意**：IE7和更早的版本不支持"继承"的值。 IE8 需要定义 **！DOCTYPE**。 IE9支持"继承"。


---


## 标签定义及使用说明


背景缩写属性可以在一个声明中设置所有的背景属性。


可以设置的属性分别是：background-color、background-position、background-size、background-repeat、background-origin、background-clip、background-attachment 和 background-image。


各值之间用空格分隔，不分先后顺序。可以只有其中的某些值，例如 **background：＃FF0000 URL（smiley.gif);** 是允许的。


| 默认值: | 请参阅单独的属性 |
| --- | --- |
| 继承: | no |
| 版本: | CSS1+ CSS3中的新的属性 |
| JavaScript 语法: | object object.style.background="red url(smiley.gif) top left no-repeat" |

**
---


## 语法


```css
background:bg-color bg-image position/bg-size bg-repeat bg-origin bg-clip bg-attachment initial|inherit;
```


| 值 | 说明 | CSS |
| --- | --- | --- |
| background-color | 指定要使用的背景颜色 | 1 |
| background-position | 指定背景图像的位置 | 1 |
| background-size | 指定背景图片的大小 | 3 |
| background-repeat | 指定如何重复背景图像 | 1 |
| background-origin | 指定背景图像的定位区域 | 3 |
| background-clip | 指定背景图像的绘画区域 | 3 |
| background-attachment | 设置背景图像是否固定或者随着页面的其余部分滚动。 | 1 |
| background-image | 指定要使用的一个或多个背景图像 | 1 |


---


## 相关文章


CSS 教程: [CSS 背景](https://www.runoob.com/../css/css-background.html)


CSS3 教程: [CSS3 背景](https://www.runoob.com/../css3/css3-backgrounds.html)








	  AI 思考中...





			** [CSS3 backface-visibility 属性](https://www.runoob.com/css3-pr-backface-visibility.html)
			[CSS background-attachment 属性](https://www.runoob.com/pr-background-attachment.html) **













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
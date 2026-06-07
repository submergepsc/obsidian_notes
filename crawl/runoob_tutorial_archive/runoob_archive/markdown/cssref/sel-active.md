# CSS :active 选择器

- Source: https://www.runoob.com/cssref/sel-active.html

[![CSS完整选择器](https://www.runoob.com/images/up.gif)完整CSS选择器参考手册](https://www.runoob.com/css-selectors.html)


## 实例


选择激活的链接样式：


```css
a:active
	{
	background-color:yellow;
	}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sel_active)


---


## 定义和用法


:active向活动的链接添加特殊的样式。


当你点击一个链接时它变成活动链接。


提示:** [:link](https://www.runoob.com/sel-link.html) 选择器设置了未访问过的页面链接样式, [:visited](https://www.runoob.com/sel-visited.html) 选择器设置访问过的页面链接的样式, [:hover](https://www.runoob.com/sel-hover.html) 选择器当有鼠标悬停在其上的链接样式。


**注意:** 为了产生预期的效果，在CSS定义中，:active必须位于:hover之后！！


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


| 选择器 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| :active | 4.0 | 7.0 | 2.0 | 3.1 | 9.6 |


**注意：**对所有元素IE8以及新版本浏览器均支持:active选择器。:active选择器对于IE7只支持链接。


---


## 相关文章


CSS 教程: [CSS Links](https://www.runoob.com/../css/css-link.html)


CSS tutorial: [CSS 伪类](https://www.runoob.com/../css/css-pseudo-classes.html)


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


**
## 实例


激活的、已访问的、未访问的或者当有鼠标悬停在其上的链接：


```css
a:link    {color:green;}
	a:visited {color:green;}
	a:hover   {color:red;}
	a:active  {color:yellow;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sel_link_more1)


## 实例


不同样式的链接样式：


```css
a.ex1:hover,a.ex1:active {color:red;}
	a.ex2:hover,a.ex2:active {font-size:150%;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_sel_link_more2)


---


[![CSS完整选择器](https://www.runoob.com/images/up.gif)完整CSS选择器参考手册](https://www.runoob.com/css-selectors.html)








	  AI 思考中...





			** [CSS :visited 选择器](https://www.runoob.com/sel-visited.html)
			[CSS :hover 选择器](https://www.runoob.com/sel-hover.html) **













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
# CSS3 :nth-of-type() Selector

- Source: https://www.runoob.com/cssref/sel-nth-of-type.html

[![CSS完整选择器](https://www.runoob.com/images/up.gif)完整CSS选择器参考手册](https://www.runoob.com/css-selectors.html)


## 实例


指定每个p元素匹配同类型中的第2个同级兄弟元素的背景色：


```css
p:nth-of-type(2)
	{
	background:#ff0000;
	}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_nth-of-type)


---


## 定义和用法


:nth-of-type(n)选择器匹配同类型中的第n个同级兄弟元素。


n可以是一个数字，一个关键字，或者一个公式。


提示:** 请参阅 [:nth-child()](https://www.runoob.com/sel-nth-child.html) 选择器。该选择器匹配父元素中的第n个子元素。Look at the [:nth-child()](https://www.runoob.com/sel_nth-child.html) 。


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


| 选择器 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| :nth-of-type() | 4.0 | 9.0 | 3.5 | 3.2 | 9.6 |


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


**
## 实例 1


奇数和偶数是可以作为关键字使用用于相匹配的子元素，其索引是奇数或偶数（该索引的第一个子节点是1）。


在这里，我们为奇数和偶数p元素指定两个不同的背景颜色：


```css
p:nth-of-type(odd)
	{
	background:#ff0000;
	}
	p:nth-of-type(even)
	{
	background:#0000ff;
	}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_nth-of-type_odd_even)


## Example 2


使用公式（an+ b）.描述：a代表一个循环的大小，N是一个计数器（从0开始），以及b是偏移量。


在这里，我们对所有索引是3的倍数的p元素指定了背景颜色：


```css
p:nth-of-type(3n+0)
	{
	background:#ff0000;
	}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss3_nth-of-type_formula)


---


[![CSS完整选择器](https://www.runoob.com/images/up.gif)完整CSS选择器参考手册](https://www.runoob.com/css-selectors.html)









	  AI 思考中...





			** [CSS3 :nth-last-child() 选择器](https://www.runoob.com/sel-nth-last-child.html)
			[CSS3 :nth-last-of-type() 选择器](https://www.runoob.com/sel-nth-last-of-type.html) **













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
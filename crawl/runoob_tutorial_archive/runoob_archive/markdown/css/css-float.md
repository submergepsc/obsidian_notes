# CSS Float(浮动)

- Source: https://www.runoob.com/css/css-float.html

---


## 什么是 CSS Float（浮动）？


![](https://www.runoob.com/images/klematis_small.jpg)**


![](https://www.runoob.com/images/klematis2_small.jpg)


![](https://www.runoob.com/images/klematis3_small.jpg)


![](https://www.runoob.com/images/klematis4_small.jpg)


CSS 的 Float（浮动），会使元素向左或向右移动，其周围的元素也会重新排列。


Float（浮动），往往是用于图像，但它在布局时一样非常有用。


---


## 元素怎样浮动


元素的水平方向浮动，意味着元素只能左右移动而不能上下移动。


一个浮动元素会尽量向左或向右移动，直到它的外边缘碰到包含框或另一个浮动框的边框为止。


浮动元素之后的元素将围绕它。


浮动元素之前的元素将不会受到影响。


如果图像是右浮动，下面的文本流将环绕在它左边：


## 实例


```css
img
{
    float:right;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_float)


---


## 彼此相邻的浮动元素


如果你把几个浮动的元素放到一起，如果有空间的话，它们将彼此相邻。


在这里，我们对图片廊使用 float 属性：


## 实例


```css
.thumbnail
{
    float:left;
    width:110px;
    height:90px;
    margin:5px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_float_elements)


---


## 清除浮动 - 使用 clear


元素浮动之后，周围的元素会重新排列，为了避免这种情况，使用 clear 属性。


clear 属性指定元素两侧不能出现浮动元素。


使用 clear 属性往文本中添加图片廊：


## 实例


```css
.text_line
{
    clear:both;
}
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trycss_float_clear)


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[为图像添加边框和边距并浮动到段落的右侧](https://www.runoob.com/try/try.php?filename=trycss_float2)


让我们为图像添加边框和边距并浮动到段落的右侧


[标题和图片向右侧浮动](https://www.runoob.com/try/try.php?filename=trycss_float3)


让标题和图片向右侧浮动。


[让段落的第一个字母浮动到左侧](https://www.runoob.com/try/try.php?filename=trycss_float4)


改变样式，让段落的第一个字母浮动到左侧。


[创建一个没有表格的网页](https://www.runoob.com/try/try.php?filename=trycss_float6)


使用 float 创建一个网页页眉、页脚、左边的内容和主要内容。


---


## CSS 中所有的浮动属性


"CSS" 列中的数字表示不同的 CSS 版本（CSS1 或 CSS2）定义了该属性。


| 属性 | 描述 | 值 | CSS |
| --- | --- | --- | --- |
| clear | 指定不允许元素周围有浮动元素。 | left right both none inherit | 1 |
| float | 指定一个盒子（元素）是否可以浮动。 | left right none inherit | 1 |








	  AI 思考中...





			** [CSS Position(定位)](https://www.runoob.com/css-positioning.html)
			[CSS 布局 – 水平 & 垂直对齐](https://www.runoob.com/css-align.html) **













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
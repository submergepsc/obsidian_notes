# CSS 列表

- Source: https://www.runoob.com/css/css-list.html

---


CSS 列表属性作用如下：


- 设置不同的列表项标记为有序列表
- 设置不同的列表项标记为无序列表
- 设置列表项标记为图像

**
---


## 列表


在 HTML中，有两种类型的列表：


- 无序列表 **ul** - 列表项标记用特殊图形（如小黑点、小方框等）
- 有序列表 **ol** - 列表项的标记有数字或字母


使用 CSS，可以列出进一步的样式，并可用图像作列表项标记。


### 无序列表如下所示:


- Coffee
- Tea
- Coca Cola


- Coffee
- Tea
- Coca Cola



### 有序列表如下所示:


- Coffee
- Tea
- Coca Cola


- Coffee
- Tea
- Coca Cola


---


## 不同的列表项标记


list-style-type属性指定列表项标记的类型是：


## 实例


```css
ul.a {list-style-type: circle;}
ul.b {list-style-type: square;}

ol.c {list-style-type: upper-roman;}
ol.d {list-style-type: lower-alpha;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_list-style-type_ex)


一些值是无序列表，以及有些是有序列表。


---


## 作为列表项标记的图像


要指定列表项标记的图像，使用列表样式图像属性：


## 实例


```css
ul
{
    list-style-image: url('sqpurple.gif');
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_list-style-image)


上面的例子在所有浏览器中显示并不相同，IE 和 Opera 显示图像标记比火狐，Chrome 和 Safari更高一点点。


如果你想在所有的浏览器放置同样的形象标志，就应使用浏览器兼容性解决方案，过程如下


## 浏览器兼容性解决方案


同样在所有的浏览器，下面的例子会显示的图像标记：


## 实例


```css
ul
{
    list-style-type: none;
    padding: 0px;
    margin: 0px;
}
ul li
{
    background-image: url(sqpurple.gif);
    background-repeat: no-repeat;
    background-position: 0px 5px;
    padding-left: 14px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_list-style-image_crossbrow)


例子解释：


- ul: 设置列表类型为没有列表项标记
- 设置填充和边距 0px（浏览器兼容性）


	ul 中所有 li:

- 设置图像的 URL，并设置它只显示一次（无重复）
- 您需要的定位图像位置（左 0px 和上下 5px）
- 用 padding-left 属性把文本置于列表中


---


## 列表 - 简写属性


在单个属性中可以指定所有的列表属性。这就是所谓的简写属性。


为列表使用简写属性，列表样式属性设置如下：


## 实例


```css
ul
{
    list-style: square url("sqpurple.gif");
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_list-style)


可以按顺序设置如下属性：


- list-style-type
- list-style-position (有关说明，请参见下面的CSS属性表)
- list-style-image


如果上述值丢失一个，其余仍在指定的顺序，就没关系。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[所有不同的列表项标记](https://www.runoob.com/try/try.php?filename=trycss_list-style-type_all) 这个例子演示了所有不同的 CSS 列表项标记。


---


## 移除默认设置


`list-style-type:none` 属性可以用于移除小标记。默认情况下列表  或  还设置了内边距和外边距，可使用 `margin:0` 和 `padding:0` 来移除:


## 实例


```css
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_list-style_none)


---


## 所有的CSS列表属性


| 属性 | 描述 |
| --- | --- |
| list-style | 简写属性。用于把所有用于列表的属性设置于一个声明中 |
| list-style-image | 将图像设置为列表项标志。 |
| list-style-position | 设置列表中列表项标志的位置。 |
| list-style-type | 设置列表项标志的类型。 |








	  AI 思考中...





			** [CSS 链接(link)](https://www.runoob.com/css-link.html)
			[CSS Table(表格)](https://www.runoob.com/css-table.html) **













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
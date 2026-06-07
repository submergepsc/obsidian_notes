# CSS 表格

- Source: https://www.runoob.com/css/css-table.html

---


使用 CSS 可以使 HTML 表格更美观。


| Company | Contact | Country |
| --- | --- | --- |
| Alfreds Futterkiste | Maria Anders | Germany |
| Berglunds snabbköp | Christina Berglund | Sweden |
| Centro comercial Moctezuma | Francisco Chang | Mexico |
| Ernst Handel | Roland Mendel | Austria |
| Island Trading | Helen Bennett | UK |
| Königlich Essen | Philip Cramer | Germany |
| Laughing Bacchus Winecellars | Yoshi Tannamuri | Canada |
| Magazzini Alimentari Riuniti | Giovanni Rovelli | Italy |
| North/South | Simon Crowther | UK |
| Paris spécialités | Marie Bertrand | France |
| The Big Cheese | Liz Nixon | USA |
| Vaffeljernet | Palle Ibsen | Denmark |


---


## 表格边框


指定CSS表格边框，使用border属性。


下面的例子指定了一个表格的Th和TD元素的黑色边框：


## 实例


```css
table, th, td
{
    border: 1px solid black;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_table_border)


请注意，在上面的例子中的表格有双边框。这是因为表和th/ td元素有独立的边界。


为了显示一个表的单个边框，使用 border-collapse属性。


## 折叠边框


border-collapse 属性设置表格的边框是否被折叠成一个单一的边框或隔开：


## 实例


```css
table
{
    border-collapse:collapse;
}
table,th, td
{
    border: 1px solid black;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_table_border-collapse)


---


## 表格宽度和高度


Width和height属性定义表格的宽度和高度。


下面的例子是设置100％的宽度，50像素的th元素的高度的表格：


## 实例


```css
table
{
    width:100%;
}
th
{
    height:50px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_table_width)


---


## 表格文字对齐


表格中的文本对齐和垂直对齐属性。


text-align属性设置水平对齐方式，向左，右，或中心：


## 实例


```css
td
{
    text-align:right;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_table_align)


垂直对齐属性设置垂直对齐，比如顶部，底部或中间：


## 实例


```css
td
{
    height:50px;
    vertical-align:bottom;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_table_vertical-align)


---


## 表格填充


如需控制边框和表格内容之间的间距，应使用td和th元素的填充属性：


## 实例


```css
td
{
    padding:15px;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_table_padding)


---


## 表格颜色


下面的例子指定边框的颜色，和th元素的文本和背景颜色：


## 实例


```css
table, td, th
{
    border:1px solid green;
}
th
{
    background-color:green;
    color:white;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_table_color)


---


![Examples](https://www.runoob.com/images/tryitimg.gif)

## 更多实例


[制作一个个性表格](https://www.runoob.com/try/try.php?filename=trycss_table_fancy) 这个例子演示了如何创建一个个性的表格。


[设置表格标题的位置](https://www.runoob.com/try/try.php?filename=trycss_table_caption-side) 这个例子演示了如何定位表格标题。








	  AI 思考中...





			** [CSS 列表](https://www.runoob.com/css-list.html)
			[CSS 盒子模型](https://www.runoob.com/css-boxmodel.html) **













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
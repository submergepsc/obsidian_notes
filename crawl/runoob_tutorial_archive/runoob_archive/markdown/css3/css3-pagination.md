# CSS 分页实例

- Source: https://www.runoob.com/css3/css3-pagination.html

本章节我们将为大家介绍如何通过使用 CSS 来创建分页的实例。


---


## 简单分页


如果你的网站有很多个页面，你就需要使用分页来为每个页面做导航。


以下实例演示了如何使用 HTML 和 CSS 来创建分页：


### CSS 实例


```css
ul.pagination {    display: inline-block;
	padding: 0;    margin: 0;}ul.pagination li
	{display: inline;}ul.pagination li a {    color:
	black;    float: left;    padding: 8px
	16px;    text-decoration: none;}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination)


---


## 点击及鼠标悬停分页样式


- «
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- »


如果点击当前页，可以使用 `.active` 来设置当前页样式，鼠标悬停可以使用 `:hover` 选择器来修改样式：


### CSS 实例


```css
ul.pagination li a.active {    background-color:
	#4CAF50;    color: white;}ul.pagination li
	a:hover:not(.active) {background-color: #ddd;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_active)


### CSS 实例


```css
ul.pagination li a.active {    background-color:
	#4CAF50;    color: white;}ul.pagination li
	a:hover:not(.active) {background-color: #ddd;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_active)


### 圆角样式


- «
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- »


可以使用 `border-radius` 属性为选中的页码来添加圆角样式:


### CSS 实例


```css
ul.pagination li a {    border-radius: 5px;}ul.pagination li a.active {
	border-radius: 5px;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_active_round)


### 鼠标悬停过渡效果


- «
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- »


我们可以通过添加 `transition` 属性来为鼠标移动到页码上时添加过渡效果:


### CSS 实例


```css
ul.pagination li a {    transition: background-color .3s;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_transition)


---


## 带边框分页


- «
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- »


我们可以使用 `border` 属性来添加带边框分页:


### CSS 实例


```css
ul.pagination li a {    border: 1px solid #ddd; /* Gray
	*/}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_border)


### 圆角边框


提示:** 在第一个分页链接和最后一个分页链接添加圆角：


- «
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- »


### CSS 实例


```css
.pagination li:first-child a {    border-top-left-radius:
	5px;    border-bottom-left-radius: 5px;}.pagination li:last-child a {
	border-top-right-radius: 5px;
	border-bottom-right-radius: 5px;}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_border_round)


### 分页间隔


提示:** 你可以使用 `margin` 属性来为每个页码直接添加空格：


- «
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- »


### CSS 实例


```css
ul.pagination li a {    margin: 0 4px; /* 0 对应的是头部与底部，可以修改它看看效果 */}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_margin)


---


## 分页字体大小


- «
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- »


我们可以使用 `font-size` 属性来设置分页的字体大小:


### CSS 实例


```css
ul.pagination li a {    font-size: 22px;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_size)


---


## 居中分页


- «
- 1
- 2
- 3
- 4
- 5
- 6
- 7
- »


如果要让分页居中，可以在容器元素上 (如 ) 添加 text-align:center** 样式：


### CSS 实例


```css
div.center {    text-align: center;}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_center)


---


## 更多实例


### CSS 实例


```css

```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_ex_pagination_nav)


---


## 面包屑导航


- 首页
- 前端
- HTML 教程
- HTML 段落


另外一种导航为面包屑导航，实例如下：


### CSS 实例


```css
ul.breadcrumb {    padding: 8px 16px;
	list-style: none;    background-color: #eee;}
	ul.breadcrumb li {display: inline;}ul.breadcrumb li+li:before {
	padding: 8px;    color: black;
	content: "/\00a0";}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_breadcrumbs)









	  AI 思考中...





			** [CSS 按钮](https://www.runoob.com/css3-buttons.html)
			[CSS3 框大小](https://www.runoob.com/css3-box-sizing.html) **













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
# Foundation 分页

- Source: https://www.runoob.com/foundation/foundation-pagination.html

如果你的网页有很多内容，就需要使用分页功能。

*


要创建一个基础的分页功能需要在 `` 元素上加上 `.pagination` 类:


### 实例


```
<ul class="pagination">  <li><a href="#">1</a></li>
	<li><a href="#">2</a></li>  <li><a href="#">3</a></li>
	<li><a href="#">4</a></li>  <li><a href="#">5</a></li></ul>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_pagination)


---


## 当前页面


可以在 `` 加上 `.current` 类来标注当前页面：


### 实例


```
<ul class="pagination">  <li class="current"><a href="#">1</a></li>
	<li><a href="#">2</a></li>  <li><a href="#">3</a></li>
	<li><a href="#">4</a></li>  <li><a href="#">5</a></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_pagination_current)


---


## 禁用分页


如果需要设置某个分页不可点击需要使用 `.unavailable` 类：


### 实例


```
<ul class="pagination">  <li><a href="#">1</a></li>
	<li><a href="#">2</a></li>  <li class="unavailable"><a href="#">3</a></li>
	<li><a href="#">4</a></li>  <li><a href="#">5</a></li></ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_pagination_unavailable)


---


## 分页方向


在第一个和最后一个 `` 元素上添加`.arrow` 类插入 HTML 实体符号 `«` 和 `»` 来创建分页方向符号：


### 实例


```
<ul class="pagination">  <li class="arrow"><a href="#">&laquo;</a></li>
	<li><a href="#">1</a></li>  <li><a href="#">2</a></li>
	<li><a href="#">3</a></li>  <li><a href="#">4</a></li>
	<li><a href="#">5</a></li>  <li class="arrow"><a href="#">&raquo;</a></li>
	</ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_pagination_arrow)


---


## 分页居中显示


我们可以在  外层添加 `` 元素，并在 `` 上添加`.pagination-centered` 类来实现分页居中显示 :


### 实例


```
<div class="pagination-centered">  <ul class="pagination">    <li class="arrow"><a href="#">&laquo;</a></li>    <li
	class="current"><a href="#">1</a></li>    <li><a href="#">2</a></li>    <li><a href="#">3</a></li>    <li><a href="#">4</a></li>    <li><a href="#">5</a></li>    <li class="arrow"><a href="#">&raquo;</a></li>

	</ul></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_pagination_center)


---


## 面包屑导航


面包屑导航用于展示当前页面的导航结构。


在 `` 元素上添加 `.breadcrumbs` 类来实现面包屑导航。你可以在  上添加 `.current` 或 `.unavailable` 类设置当前页与不可点击效果:


### 实例


```
<ul class="breadcrumbs">  <li><a href="#">Home</a></li>
	<li><a href="#">Private</a></li>  <li
	class="unavailable"><a href="#">Pictures</a></li>
	<li class="current">Vacation</li> </ul>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_breadcrumbs)


---


## 子导航


在页面切换上，子导航是非常有用的。


在 `` 元素上添加 `.sub-nav` 类来创建子导航。在 `
**` 元素上添加标题，为选中的选项 `` 添加 `.active` 类: ### 实例
```
<dl class="sub-nav">  <dt>Filter:</dt>  <dd
	class="active"><a href="#">All</a></dd>  <dd><a href="#">Active</a></dd>
	<dd><a href="#">Pending</a></dd>  <dd><a href="#">Suspended</a></dd>
	</dl>
```
 [尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_sub_nav) AI 思考中... * [Foundation 选项卡](https://www.runoob.com/foundation-tabs.html) [Foundation 价格表](https://www.runoob.com/foundation-pricing-tables.html) ** ### 点我分享笔记 ** 取消 * * 分享笔记 - 昵称昵称 (必填) - 邮箱邮箱 (必填) - 引用地址引用地址 在线实例**

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
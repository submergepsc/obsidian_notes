# Bootstrap 分页

- Source: https://www.runoob.com/bootstrap/bootstrap-pagination.html

本章将讲解 Bootstrap 支持的分页特性。分页（Pagination），是一种无序列表，Bootstrap 像处理其他界面元素一样处理分页。


## 分页（Pagination）


下表列出了 Bootstrap 提供的处理分页的 class。


| Class | 描述 | 示例代码 |
| --- | --- | --- |
| .pagination | 添加该 class 来在页面上显示分页。 |
```
<ul class="pagination">
  <li><a href="#">&laquo;</a></li>
  <li><a href="#">1</a></li>
  .......
</ul>
```
 |
| .disabled, .active | 您可以自定义链接，通过使用 .disabled 来定义不可点击的链接，通过使用 .active 来指示当前的页面。 |
```
<ul class="pagination">
  <li class="disabled"><a href="#">&laquo;</a></li>
  <li class="active"><a href="#">1<span class="sr-only">(current)</span></a></li>
  .......
</ul>
```
 |
| .pagination-lg, .pagination-sm | 使用这些 class 来获取不同大小的项。 |
```
<ul class="pagination pagination-lg">...</ul>
<ul class="pagination">...</ul>
<ul class="pagination pagination-sm">...</ul>
```
 |


### 默认的分页


下面的实例演示了上表中所讨论的 class **.pagination** 的用法：


## 实例


```css
<ul class="pagination">
    <li><a href="#">&laquo;</a></li>
    <li><a href="#">1</a></li>
    <li><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li><a href="#">&raquo;</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-pagination)


结果如下所示：


![默认的分页](https://www.runoob.com/wp-content/uploads/2014/06/pagination_demo.jpg)


### 分页的状态


下面的实例演示了上表中所讨论的 class .disabled、.active** 的用法：


## 实例


```css
<ul class="pagination">
    <li><a href="#">&laquo;</a></li>
    <li class="active"><a href="#">1</a></li>
    <li class="disabled"><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li><a href="#">&raquo;</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-pagination-state)


结果如下所示：


![分页的状态](https://www.runoob.com/wp-content/uploads/2014/06/paginationstate_demo.jpg)


### 分页的大小


下面的实例演示了上表中所讨论的 class .pagination-*** 的用法：


## 实例


```css
<ul class="pagination pagination-lg">
<li><a href="#">&laquo;</a></li>
    <li><a href="#">1</a></li>
    <li><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li><a href="#">&raquo;</a></li>
</ul><br>
<ul class="pagination">
    <li><a href="#">&laquo;</a></li>
    <li><a href="#">1</a></li>
    <li><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li><a href="#">&raquo;</a></li>
</ul><br>
<ul class="pagination pagination-sm">
    <li><a href="#">&laquo;</a></li>
    <li><a href="#">1</a></li>
    <li><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li><a href="#">&raquo;</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-pagination-size)


结果如下所示：


![分页的大小](https://www.runoob.com/wp-content/uploads/2014/06/paginationsize_demo.jpg)


## 翻页（Pager）


如果您想要创建一个简单的分页链接为用户提供导航，可通过翻页来实现。与分页链接一样，翻页也是无序列表。默认情况下，链接是居中显示。下表列出了 Bootstrap 处理翻页的 class。


| Class | 描述 | 示例代码 |
| --- | --- | --- |
| .pager | 添加该 class 来获得翻页链接。 |
```
<ul class="pager">
  <li><a href="#">Previous</a></li>
  <li><a href="#">Next</a></li>
</ul>
```
 |
| .previous, .next | 使用 class .previous 把链接向左对齐，使用 .next 把链接向右对齐。 |
```
<ul class="pager">
  <li class="previous"><a href="#">&larr; Older</a></li>
  <li class="next"><a href="#">Newer &rarr;</a></li>
</ul>
```
 |
| .disabled | 添加该 class 来设置对应按钮禁止使用。 |
```
<ul class="pager">
  <li class="previous disabled"><a href="#">&larr; Older</a></li>
  <li class="next"><a href="#">Newer &rarr;</a></li>
</ul>
```
 |


### 默认的翻页


下面的实例演示了上表中所讨论的 class .pager** 的用法：


## 实例


```css
<ul class="pager">
    <li><a href="#">Previous</a></li>
    <li><a href="#">Next</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-pager)


结果如下所示：


![默认的翻页](https://www.runoob.com/wp-content/uploads/2014/06/pager_demo.jpg)


### 对齐的链接


下面的实例演示了上表中所讨论的 class .previous、.next** 的用法：


## 实例


```css
<ul class="pager">
    <li class="previous"><a href="#">&larr; Older</a></li>
    <li class="next"><a href="#">Newer &rarr;</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-pager-align)


结果如下所示：


![翻页中对齐的链接](https://www.runoob.com/wp-content/uploads/2014/06/pageralign_demo.jpg)


### 翻页的状态


下面的实例演示了上表中所讨论的 class .disabled** 的用法：


## 实例


```css
<ul class="pager">
    <li class="previous disabled"><a href="#">&larr; Older</a></li>
    <li class="next"><a href="#">Newer &rarr;</a></li>
</ul>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-pager-state)


结果如下所示：


![翻页的状态](https://www.runoob.com/wp-content/uploads/2014/06/pagerstate_demo.jpg)


---


## 分页更多实例


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .pager | 一个简单的分页链接，链接居中对齐。 | 尝试一下 |
| .previous | .pager 中上一页的按钮样式，左对齐 | 尝试一下 |
| .next | .pager 中下一页的按钮样式，右对齐 | 尝试一下 |
| .disabled | 禁用链接 | 尝试一下 |
| .pagination | 分页链接 | 尝试一下 |
| .pagination-lg | 更大尺寸的分页链接 | 尝试一下 |
| .pagination-sm | 更小尺寸的分页链接 | 尝试一下 |
| .disabled | 禁用链接 | 尝试一下 |
| .active | 当前访问页面链接样式 | 尝试一下 |








	  AI 思考中...





			** [Bootstrap 面包屑导航](https://www.runoob.com/bootstrap-breadcrumbs.html)
			[Bootstrap 标签](https://www.runoob.com/bootstrap-labels.html) **













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
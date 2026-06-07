# Bootstrap4 卡片

- Source: https://www.runoob.com/bootstrap4/bootstrap4-cards.html

Bootstrap 4 卡片（Card）组件 是一种灵活且强大的内容容器，可以用于显示各种类型的内容，如文本、图像、列表等。

卡片组件是 Bootstrap 4 中非常常见的 UI 元素，通常用于展示信息、博客文章、产品或社交媒体帖子等。


### 基本结构

卡片组件是由多个嵌套元素组成的，主要包括以下几部分：

- **`.card`**：卡片的最外层容器。
- **`.card-body`**：包含卡片内容的容器，通常用于放置文本、标题或其他元素。
- **`.card-title`**：卡片的标题。
- **`.card-text`**：卡片的文本内容。
- **`.card-img-top`** 或 **`.card-img-bottom`**：用于展示图片，放在卡片的顶部或底部。


样式类说明：


| 类名 | 说明 | 示例用法 |
| --- | --- | --- |
| .card | 卡片的容器类，用来创建卡片的框架。 | ... |
| .card-body | 卡片内容的容器，用来包装卡片的主要内容部分。 | ... |
| .card-title | 卡片标题的类，用于定义卡片的标题。 | Card Title |
| .card-text | 卡片正文内容的类，用于添加卡片的文本。 | Some quick example text... |
| .card-img-top | 卡片顶部的图像类，通常用于显示卡片顶部的图像。 |  |
| .card-img-bottom | 卡片底部的图像类，通常用于显示卡片底部的图像。 |  |
| .card-header | 卡片的头部，用于放置标题、标签等。 | Card Header |
| .card-footer | 卡片的底部，通常用于放置作者、日期或版权信息等。 | Card Footer |
| .card-link | 用于创建卡片内的链接，通常与卡片的其他内容配合使用。 | Card link |
| .card-deck | 用于水平排列卡片，卡片间自动均匀分配间距。 | ... |
| .card-columns | 用于创建多列卡片布局，适用于卡片的杂志风格布局。 | ... |
| .no-gutters | 移除网格系统的列间距，用于去除卡片之间的默认间距。 | ... |
| .card-group | 将卡片组合在一起，并且它们会自动调整为相同的高度。 | ... |
| .card-img-overlay | 在卡片图像上叠加一个内容层，通常用于显示文本或其他元素。 | Overlay content |
| .card-subtitle | 卡片副标题，用于在标题下方显示额外的信息。 | Card subtitle |


## 简单的卡片


我们可以通过 Bootstrap4 的 **.card** 与 **.card-body** 类来创建一个简单的卡片，实例如下:


![](https://www.runoob.com/wp-content/uploads/2017/10/FA6285B4-62AA-453D-909E-755FC131A100.jpg)


## 实例


```css
<div class="card">
  <div class="card-body">简单的卡片</div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_card)

> Bootstrap4 的卡片类似 Bootstrap 3 中的面板、图片缩略图、well。


---


## 头部和底部

![](https://www.runoob.com/wp-content/uploads/2017/10/D4392D33-8328-4A18-BE0C-49F5104EE17A.jpg)


**.card-header**类用于创建卡片的头部样式， **.card-footer** 类用于创建卡片的底部样式：


## 实例


```css
<div class="card">
  <div class="card-header">头部</div>
  <div class="card-body">内容</div>
  <div class="card-footer">底部</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_card_header)


---


## 多种颜色卡片


Bootstrap 4 提供了多种卡片的背景颜色类： **.bg-primary**, ** .bg-success**, **.bg-info**, **.bg-warning**, **.bg-danger**, **.bg-secondary**, **.bg-dark** 和 **.bg-light**。


## 实例


```css
<div class="container">
  <h2>多种颜色卡片</h2>
  <div class="card">
    <div class="card-body">Basic card</div>
  </div>
  <br>
  <div class="card bg-primary text-white">
    <div class="card-body">Primary card</div>
  </div>
  <br>
  <div class="card bg-success text-white">
    <div class="card-body">Success card</div>
  </div>
  <br>
  <div class="card bg-info text-white">
    <div class="card-body">Info card</div>
  </div>
  <br>
  <div class="card bg-warning text-white">
    <div class="card-body">Warning card</div>
  </div>
  <br>
  <div class="card bg-danger text-white">
    <div class="card-body">Danger card</div>
  </div>
  <br>
  <div class="card bg-secondary text-white">
    <div class="card-body">Secondary card</div>
  </div>
  <br>
  <div class="card bg-dark text-white">
    <div class="card-body">Dark card</div>
  </div>
  <br>
  <div class="card bg-light text-dark">
    <div class="card-body">Light card</div>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_card_contextual)

---


## 标题、文本和链接


我们可以在头部元素上使用 **.card-title** 类来设置卡片的标题 。 **.card-text** 类用于设置卡片正文的内容。 **.card-link** 类用于给链接设置颜色。


## 实例


```css
<div class="card">
  <div class="card-body">
    <h4 class="card-title">Card title</h4>
    <p class="card-text">Some example text. Some example text.</p>
    <a href="#" class="card-link">Card link</a>
    <a href="#" class="card-link">Another link</a>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_card_title)


---


## 图片卡片


我们可以给 ** ** 添加 **.card-img-top**（图片在文字上方） 或 **.card-img-bottom**（图片在文字下方 来设置图片卡片：


## 实例


```css
<div class="card" style="width:400px">
  <img class="card-img-top" src="img_avatar1.png" alt="Card image">
  <div class="card-body">
    <h4 class="card-title">John Doe</h4>
    <p class="card-text">Some example text.</p>
    <a href="#" class="btn btn-primary">See Profile</a>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_card_image)

如果图片要设置为背景，可以使用 **.card-img-overlay** 类:


## 实例


```css
<div class="card" style="width:500px">
  <img class="card-img-top" src="img_avatar1.png" alt="Card image">
  <div class="card-img-overlay">
    <h4 class="card-title">John Doe</h4>
    <p class="card-text">Some example text.</p>
    <a href="#" class="btn btn-primary">See Profile</a>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs_card_image_overlay)


---


## 水平卡片


通过结合网格和工具类，可以以响应式适应移动端的方式将卡片设置为水平排列。


以下实例中，我们使用 **.no-gutters** 移除网格间距，并使用 **.col-md-*** 类在 **md** 屏幕断点处将卡片设置为水平排列。


## 实例


```css
<div class="card mb-3" style="max-width: 540px;">
  <div class="row no-gutters">
    <div class="col-md-4">
      <img src="..." class="card-img" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
      </div>
    </div>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs_card_no-gutters)

```css

```










	  AI 思考中...





			** [Bootstrap4 列表组](https://www.runoob.com/bootstrap4-list-groups.html)
			[Bootstrap4 下拉菜单](https://www.runoob.com/bootstrap4-dropdowns.html) **













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
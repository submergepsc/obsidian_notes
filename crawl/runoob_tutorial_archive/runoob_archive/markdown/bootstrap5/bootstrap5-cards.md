# Bootstrap5 卡片

- Source: https://www.runoob.com/bootstrap5/bootstrap5-cards.html

Bootstrap 5 卡片（Card）组件 是一种强大且灵活的容器，用于展示各种内容，如文本、图片、列表、按钮等。


卡片组件在 Bootstrap 5 中得到了改进和增强，提供了更多的定制选项和更灵活的布局方式。

卡片组件在 UI 设计中非常常见，尤其适用于博客、社交媒体、仪表盘和其他内容展示页面。

基
### 本结构

Bootstrap 5 的卡片组件包括以下常用元素：


- **`.card`**：卡片的最外层容器。
- **`.card-body`**：卡片的主要内容区域。
- **`.card-title`**：卡片的标题部分。
- **`.card-text`**：卡片的文本部分。
- **`.card-img-top`** 或 **`.card-img-bottom`**：卡片顶部或底部的图片。

卡片样式类说明：


| 类名 | 说明 | 示例用法 |
| --- | --- | --- |
| .card | 卡片的容器类，用于包装整个卡片。 | ... |
| .card-body | 包含卡片内容的容器，通常用于放置文本、标题等。 | ... |
| .card-title | 卡片标题类，通常包含卡片的主要标题。 | Card Title |
| .card-text | 卡片文本类，通常包含卡片的正文内容。 | Some quick example text... |
| .card-img-top | 卡片顶部的图片类，通常用于展示卡片顶部的图像。 |  |
| .card-img-bottom | 卡片底部的图片类，通常用于展示卡片底部的图像。 |  |
| .card-header | 卡片的头部区域，用于放置标题或其他内容。 | Card Header |
| .card-footer | 卡片的底部区域，用于放置额外的信息或操作按钮等。 | Card Footer |
| .card-link | 用于在卡片中创建链接。 | Card link |
| .card-deck | 在 Bootstrap 5 中已被废弃，使用 row 和 col 代替。 | ... |
| .card-group | 在 Bootstrap 5 中已被废弃，使用 row 和 col 代替。 | ... |
| .card-columns | 使用多列布局，卡片按照流式布局排列。 | ... |
| .card-subtitle | 卡片的副标题，通常显示在标题下方。 | Card subtitle |
| .card-img-overlay | 在卡片图片上叠加内容层，常用于显示文本或其他元素。 | Overlay content |


## 简单的卡片


我们可以通过 Bootstrap5 的 **.card** 与 **.card-body** 类来创建一个简单的卡片，卡片可以包含头部、内容、底部以及各种颜色设置，实例如下:


![](https://www.runoob.com/wp-content/uploads/2017/10/FA6285B4-62AA-453D-909E-755FC131A100.jpg)


## 实例


```css
<div class="card">
  <div class="card-body">简单的卡片</div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_card)


---


## 头部和底部


**.card-header**类用于创建卡片的头部样式， **.card-footer** 类用于创建卡片的底部样式：

![](https://www.runoob.com/wp-content/uploads/2017/10/D4392D33-8328-4A18-BE0C-49F5104EE17A.jpg)


## 实例


```css
<div class="card">
  <div class="card-header">头部</div>
  <div class="card-body">内容</div>
  <div class="card-footer">底部</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_card_header)


---


## 多种颜色卡片


Bootstrap 5 提供了多种卡片的背景颜色类： **.bg-primary**, ** .bg-success**, **.bg-info**, **.bg-warning**, **.bg-danger**, **.bg-secondary**, **.bg-dark** 和 **.bg-light**。


![](https://www.runoob.com/wp-content/uploads/2021/09/CA9CBB8F-B98B-42CA-A735-001FDF6D3BD4.jpeg)


## 实例


```css
<div class="container">
  <h2>多种颜色卡片</h2>
  <div class="card">
    <div class="card-body">基础卡片</div>
  </div>
  <br>
  <div class="card bg-primary text-white">
    <div class="card-body">主要卡片</div>
  </div>
  <br>
  <div class="card bg-success text-white">
    <div class="card-body">成功卡片</div>
  </div>
  <br>
  <div class="card bg-info text-white">
    <div class="card-body">信息卡片</div>
  </div>
  <br>
  <div class="card bg-warning text-white">
    <div class="card-body">警告卡片</div>
  </div>
  <br>
  <div class="card bg-danger text-white">
    <div class="card-body">危险卡片</div>
  </div>
  <br>
  <div class="card bg-secondary text-white">
    <div class="card-body">次要卡片</div>
  </div>
  <br>
  <div class="card bg-dark text-white">
    <div class="card-body">黑色卡片</div>
  </div>
  <br>
  <div class="card bg-light text-dark">
    <div class="card-body">浅色卡片</div>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_card_contextual)

---


## 标题、文本和链接


我们可以在头部元素上使用 **.card-title** 类来设置卡片的标题 。 **.card-body** 类用于设置卡片正文的内容。**.card-text** 类用于设置卡 **.card-body** 类中的  标签，如果说最后一行可以移除底部边距。 **.card-link** 类用于给链接设置颜色。


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


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_card_title)


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


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_card_image)

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


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_card_image_overlay)







	  AI 思考中...





			** [Bootstrap5 列表组](https://www.runoob.com/bootstrap5-list-groups.html)
			[Bootstrap5 下拉菜单](https://www.runoob.com/bootstrap5-dropdowns.html) **













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
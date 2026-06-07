# Bootstrap4 列表组

- Source: https://www.runoob.com/bootstrap4/bootstrap4-list-groups.html

大部分基础列表组都是无序的。


![](https://www.runoob.com/wp-content/uploads/2017/10/2D8ACDED-2C3C-4E1F-A92C-7BE161B59CC8.jpg)


要创建列表组，可以在 **** 元素上添加 **.list-group** 类, 在 **** 元素上添加 **.list-group-item** 类:


## 实例


```css
<ul class="list-group">
  <li class="list-group-item">First item</li>
  <li class="list-group-item">Second item</li>
  <li class="list-group-item">Third item</li>
</ul>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_list_group)


---


## 激活状态的列表项


通过添加 **.active** 类来设置激活状态的列表项：


## 实例


```css
<ul class="list-group">
  <li class="list-group-item active">Active item</li>
  <li class="list-group-item">Second item</li>
  <li class="list-group-item">Third item</li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_list_group_active)


---


## 禁用的列表项


**.disabled** 类用于设置禁用的列表项:


## 实例


```css
<ul class="list-group">
  <li class="list-group-item disabled">Disabled item</li>
  <li class="list-group-item">Second item</li>
  <li class="list-group-item">Third item</li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_list_group_disabled)

---


## 链接列表项


要创建一个链接的列表项，可以将 **** 替换为 **** ， **** 替换 ****。如果你想鼠标悬停显示灰色背景就添加**.list-group-item-action** 类:


## 实例


```css
<div class="list-group">
  <a href="#" class="list-group-item list-group-item-action">First item</a>
  <a href="#" class="list-group-item list-group-item-action">Second item</a>
  <a href="#" class="list-group-item list-group-item-action">Third item</a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_list_group_link)


---


## 移除列表边框


使用 **.list-group-flush** 类来删除列表的边框和圆角：


## 实例


```css
<ul class="list-group list-group-flush">
  <li class="list-group-item">First item</li>
  <li class="list-group-item">Second item</li>
  <li class="list-group-item">Third item</li>
  <li class="list-group-item">Fourth item</li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs_list_group_flush)

---


## 水平列表组


我们可以将 **.list-group-horizontal** 类添加到 **.list-group** 类后面来创建水平列表组：


## 实例


```css
<ul class="list-group list-group-horizontal">
  <li class="list-group-item">First item</li>
  <li class="list-group-item">Second item</li>
  <li class="list-group-item">Third item</li>
  <li class="list-group-item">Fourth item</li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_list_group_horizontal)


---


## 多种颜色列表项


![](https://www.runoob.com/wp-content/uploads/2017/10/41EFB157-7D83-4BB0-82E7-C98F05CB3C56.jpg)


列表项目的颜色可以通过以下列来设置：** .list-group-item-success**, **list-group-item-secondary**, **list-group-item-info**, ** list-group-item-warning**, **.list-group-item-danger**, **list-group-item-dark** 和 **list-group-item-light**:


## 实例


```css
<ul class="list-group">
  <li class="list-group-item list-group-item-success">成功列表项</li>
  <li class="list-group-item list-group-item-secondary">次要列表项</li>
  <li class="list-group-item list-group-item-info">信息列表项</li>
  <li class="list-group-item list-group-item-warning">警告列表项</li>
  <li class="list-group-item list-group-item-danger">危险列表项</li>
  <li class="list-group-item list-group-item-primary">主要列表项</li>
  <li class="list-group-item list-group-item-dark">深灰色列表项</li>
  <li class="list-group-item list-group-item-light">浅色列表项</li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_list_group_context)

### 链接的多种颜色列表项


## 实例


```css
<div class="list-group">
    <a href="#" class="list-group-item list-group-item-action">激活列表项</a>
    <a href="#" class="list-group-item list-group-item-success">成功列表项</a>
    <a href="#" class="list-group-item list-group-item-secondary">次要列表项</a>
    <a href="#" class="list-group-item list-group-item-info">信息列表项</a>
    <a href="#" class="list-group-item list-group-item-warning">警告列表项</a>
    <a href="#" class="list-group-item list-group-item-danger">危险列表项</a>
    <a href="#" class="list-group-item list-group-item-primary">主要列表项</a>
    <a href="#" class="list-group-item list-group-item-dark">深灰色列表项</a>
    <a href="#" class="list-group-item list-group-item-light">浅色列表项</a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_list_group_context_links)







	  AI 思考中...





			** [Bootstrap4 分页](https://www.runoob.com/bootstrap4-pagination.html)
			[Bootstrap4 卡片](https://www.runoob.com/bootstrap4-cards.html) **













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
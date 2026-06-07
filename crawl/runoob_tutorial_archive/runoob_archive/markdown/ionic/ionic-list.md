# ionic 列表

- Source: https://www.runoob.com/ionic/ionic-list.html

列表是一个应用广泛的界面元素，在所有移动app中几乎都会使用到。


列表可以是基本文字、按钮，开关，图标和缩略图等。


列表项可以是任何的HTML元素。容器元素需要list类，每个列表项需要使用item类。


ionList和ionItem可以很容易的支持各种交互方式，比如，滑动编辑，拖动排序，以及删除项。


### 基本用法:


```
<ul class="list">
    <li class="item">
      ...
    </li>
</ul>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_list&basepath=0)


### 列表分隔符


我们可以使用 item-divider 类来为列表创建分隔符，默认情况下，列表项以不同的背景颜色和字体加粗来区分，但你也可以很容易的定制他。


```
<div class="list">

  <div class="item item-divider">
    Candy Bars
  </div>

  <a class="item" href="#">
    Butterfinger
  </a>

  ...

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_list_item-divider&basepath=0)


---


## 带图标列表


我们可以在列表项的左侧或右侧指定图标。


使用 item-icon-left 图标在左侧， item-icon-right 设置图标在右侧。如果你需要在两边都有图标，则两个类都添加上即可。


以下实例中，我们在列表项中使用了  标签，使得每个列表项可点击。


列表项在使用 或 元素时，如果右侧未添加图标，则会自动添加上箭头号。


实例中，第一项只有左侧图标，第二项左右均有图标，第三项有右侧图标（还有注释 item-note），第四项有badge（标记）元素。


```
<div class="list">

  <a class="item item-icon-left" href="#">
    <i class="icon ion-email"></i>
    Check mail
  </a>

  <a class="item item-icon-left item-icon-right" href="#">
    <i class="icon ion-chatbubble-working"></i>
    Call Ma
    <i class="icon ion-ios-telephone-outline"></i>
  </a>

  <a class="item item-icon-left" href="#">
    <i class="icon ion-mic-a"></i>
    Record album
    <span class="item-note">
      Grammy
    </span>
  </a>

  <a class="item item-icon-left" href="#">
    <i class="icon ion-person-stalker"></i>
    Friends
    <span class="badge badge-assertive">0</span>
  </a>

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_list_item-icon&basepath=0)


---


## 按钮列表


使用 item-button-right 或 item-button-left 类将按钮放在列表项中。


```
<div class="list">

  <div class="item item-button-right">
    Call Ma
    <button class="button button-positive">
      <i class="icon ion-ios-telephone"></i>
    </button>
  </div>

  ...

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_list_item-button&basepath=0)


---


## 带头像列表


使用 item-avatar 来创建一个带头像的列表：


```
<div class="list">

    <a class="item item-avatar" href="#">
      <img src="venkman.jpg">
      <h2>Venkman</h2>
      <p>Back off, man. I'm a scientist.</p>
    </a>

    ...

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_list_item-avatar&basepath=0)


---


## 缩略图列表


item-thumbnail-left 类用于添加左侧对齐的缩略图， item-thumbnail-right 类用于添加右侧对齐的缩略图。


```
<div class="list">

    <a class="item item-thumbnail-left" href="#">
      <img src="cover.jpg">
      <h2>Pretty Hate Machine</h2>
      <p>Nine Inch Nails</p>
    </a>

    ...

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_list_item-thumbnail&basepath=0)


---


## 内嵌列表(inset list)


我们可以在容器当中内嵌列表，列表不会显示完整的宽度。


内嵌列表的样式为：list list-inset，与常规列表区别是，它设置了外边距（marign）,类似于选项卡。


内嵌列表是没有阴影效果的，滚动时效果会更好。


```
<div class="list list-inset">

    <div class="item">
      Raiders of the Lost Ark
    </div>

    ...

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_list_inset&basepath=0)








	  AI 思考中...





			** [ionic 按钮](https://www.runoob.com/ionic-button.html)
			[ionic 卡片](https://www.runoob.com/ionic-card.html) **













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
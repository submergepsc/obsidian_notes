# ionic 卡片

- Source: https://www.runoob.com/ionic/ionic-card.html

近年来卡片(card)的应用越来越流行，卡片提供了一个更好组织信息展示的工具。


针对移动端的应用，卡片会根据屏幕大小自适应大小。


我们可以很灵活的控制卡片的显示效果，甚至实现动画效果。


卡片一般放在页面顶部，当然也可以实现左右切换的功能。


```
<div class="card">
  <div class="item item-text-wrap">
    基本卡片，包含了文本信息。
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_card&basepath=0)


卡片(card)默认样式带有box-shadow(阴影)，由于性能的原因，和他类似的元素像 list list-inset 并没有阴影。


如果你有很多的卡片，每个卡片都有很多子元素，建议使用内嵌列表（inset list）。


---


## 卡片的头部与底部


我们可以通过添加 item-divider 类为卡片添加头部与底部：


```
<div class="card">
  <div class="item item-divider">
    卡片头部！
  </div>
  <div class="item item-text-wrap">
    基本卡片，包含了文本信息。
  </div>
  <div class="item item-divider">
    卡片底部！
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_card_item-divider&basepath=0)


---


## 卡片列表


使用 list card 类来设置卡片列表：


```
<div class="list card">

  <a href="#" class="item item-icon-left">
    <i class="icon ion-home"></i>
    Enter home address
  </a>

  <a href="#" class="item item-icon-left">
    <i class="icon ion-ios-telephone"></i>
    Enter phone number
  </a>

  <a href="#" class="item item-icon-left">
    <i class="icon ion-wifi"></i>
    Enter wireless password
  </a>

  <a href="#" class="item item-icon-left">
    <i class="icon ion-card"></i>
    Enter card information
  </a>

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_card_list&basepath=0)


---


## 带图片卡片


卡片中使用图片，效果会更好，实例如下：


```
<div class="list card">

  <div class="item item-avatar">
    <img src="avatar.jpg">
    <h2>Pretty Hate Machine</h2>
    <p>Nine Inch Nails</p>
  </div>

  <div class="item item-image">
    <img src="cover.jpg">
  </div>

  <a class="item item-icon-left assertive" href="#">
    <i class="icon ion-music-note"></i>
    Start listening
  </a>

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_card_item-image&basepath=0)


运行效果如下：

*

---


## 卡片展现


以下实例中使用几种不同的选项的卡片展现方式。 开始使用了 list card 元素，并使用了 item-avatar , item-body 元素用于展示图片和文本信息，底部使用 item-divider 类。


```
<div class="list card">

  <div class="item item-avatar">
    <img src="mcfly.jpg">
    <h2>Marty McFly</h2>
    <p>November 05, 1955</p>
  </div>

  <div class="item item-body">
    <img class="full-image" src="delorean.jpg">
    <p>
      菜鸟教程 -- 学的不仅是技术，更是梦想！<br>
      菜鸟教程 -- 学的不仅是技术，更是梦想！<br>
      菜鸟教程 -- 学的不仅是技术，更是梦想！<br>
      菜鸟教程 -- 学的不仅是技术，更是梦想！
    </p>
    <p>
      <a href="#" class="subdued">1 喜欢</a>
      <a href="#" class="subdued">5 评论</a>
    </p>
  </div>

  <div class="item tabs tabs-secondary tabs-icon-left">
    <a class="tab-item" href="#">
      <i class="icon ion-thumbsup"></i>
      喜欢
    </a>
    <a class="tab-item" href="#">
      <i class="icon ion-chatbox"></i>
      评论
    </a>
    <a class="tab-item" href="#">
      <i class="icon ion-share"></i>
      分享
    </a>
  </div>

</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_card_showcase&basepath=0)


运行效果如下：










	  AI 思考中...





			* [ionic 列表](https://www.runoob.com/ionic-list.html)
			[ionic 表单和输入框](https://www.runoob.com/ionic-form-input.html) **













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
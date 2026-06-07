# ionic tab(选项卡)

- Source: https://www.runoob.com/ionic/ionic-tab.html

ionic tab(选项卡) 是水平排列的按钮或者链接，用以页面间导航的切换。它可以包含文字和图标的组合，是一种移动设备上流行的导航方法。


以下选项卡容器使用了 tabs 类，每个选项卡使用 tab-item 类。默认情况下，选项卡是文本的，并没有图标。


### 实例


```
<div class="tabs">
  <a class="tab-item">
    主页
  </a>
  <a class="tab-item">
    收藏
  </a>
  <a class="tab-item">
    设置
  </a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_tab-item)


默认情况，选项卡颜色为默认，你可以设置以下不同颜色样式：tabs-default ，tabs-light ，tabs-stable ，tabs-positive ，tabs-calm ，tabs-balanced ，tabs-energized ，tabs-assertive ，tabs-royal ，tabs-dark。


要隐藏选项卡栏，可使用 tabs-item-hide 类。


### 图标选项卡


在 tabs 类后添加 tabs-icon-only 类可设置只显示图标选项卡。


```
<div class="tabs tabs-icon-only">
  <a class="tab-item">
    <i class="icon ion-home"></i>
  </a>
  <a class="tab-item">
    <i class="icon ion-star"></i>
  </a>
  <a class="tab-item">
    <i class="icon ion-gear-a"></i>
  </a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_tabs-icon-only)


### 顶部图标+文字选项卡


在 tabs 类后添加 tabs-icon-top 类可设置顶部图标+文字选项卡。


```
<div class="tabs tabs-icon-top">
  <a class="tab-item" href="#">
    <i class="icon ion-home"></i>
    主页
  </a>
  <a class="tab-item" href="#">
    <i class="icon ion-star"></i>
    收藏
  </a>
  <a class="tab-item" href="#">
    <i class="icon ion-gear-a"></i>
    设置
  </a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_tabs-icon-top)


### 左侧图标+文字选项卡


在 tabs 类后添加 tabs-icon-left 类可设置左侧图标+文字选项卡。


```
<div class="tabs tabs-icon-left">
  <a class="tab-item">
    <i class="icon ion-home"></i>
    主页
  </a>
  <a class="tab-item">
    <i class="icon ion-star"></i>
    收藏
  </a>
  <a class="tab-item">
    <i class="icon ion-gear-a"></i>
    设置
  </a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_tabs-icon-left)


### 条纹样式选项卡


可以在带有 tabs 的样式名的元素上添加 tabs-striped 来实现像 Android 风格的 tabs。也可以添加 tabs-top 来实现选项卡在页面顶部。

条纹选项卡颜色可通过 tabs-background-{color} 和 tabs-color-{color} 来控制， {color} 值可以是：default, light, stable, positive, calm, balanced, energized, assertive, royal, 或 dark。


注意：如果要再选项卡上设置头部标题，需要使用 has-tabs-top 类。


```
<div class="tabs-striped tabs-top tabs-background-positive tabs-color-light">
    <div class="tabs">
      <a class="tab-item active" href="#">
        <i class="icon ion-home"></i>
        Test
      </a>
      <a class="tab-item" href="#">
        <i class="icon ion-star"></i>
        Favorites
      </a>
      <a class="tab-item" href="#">
        <i class="icon ion-gear-a"></i>
        Settings
      </a>
    </div>
  </div>
  <div class="tabs-striped tabs-color-assertive">
    <div class="tabs">
      <a class="tab-item active" href="#">
        <i class="icon ion-home"></i>
        Test
      </a>
      <a class="tab-item" href="#">
        <i class="icon ion-star"></i>
        Favorites
      </a>
      <a class="tab-item" href="#">
        <i class="icon ion-gear-a"></i>
        Settings
      </a>
    </div>
  </div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_tabs-striped)


运行效果如下：

*







	  AI 思考中...





			* [ionic select](https://www.runoob.com/ionic-select.html)
			[ionic 网格(Grid)](https://www.runoob.com/ionic-grid.html) **













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
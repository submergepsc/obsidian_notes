# Bootstrap4 滚动监听(Scrollspy)

- Source: https://www.runoob.com/bootstrap4/bootstrap4-scrollspy.html

滚动监听（Scrollspy）插件，即自动更新导航插件，会根据滚动条的位置自动更新对应的导航目标。其基本的实现是随着您的滚动。

*


---


## 如何创建滚动监听


以下实例演示了如何创建滚动监听：


## 实例


```css
<!-- 可滚动区域 -->
<body data-spy="scroll" data-target=".navbar" data-offset="50">

<!-- The navbar - The <a> elements are used to jump to a section in the scrollable area -->
<nav class="navbar navbar-expand-sm bg-dark navbar-dark fixed-top">
...
  <ul class="navbar-nav">
    <li><a href="#section1">Section 1</a></li>
    ...
</nav>

<!-- 第一部分内容 -->
<div id="section1">
  <h1>Section 1</h1>
  <p>Try to scroll this page and look at the navigation bar while scrolling!</p>
</div>
...

</body>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_scrollspy)

### 实例解析


向您想要监听的元素（通常是 body）添加 **data-spy="scroll"** 。


然后添加 **data-target** 属性，它的值为导航栏的 id 或 class (**.navbar**)。这样就可以联系上可滚动区域。


注意可滚动项元素上的 id （****） 必须匹配导航栏上的链接选项 （****)。


可选项**data-offset** 属性用于计算滚动位置时，距离顶部的偏移像素。 默认为 10 px。



设置相对定位: **使用 data-spy="scroll" 的元素需要将其 CSS **position** 属性设置为 "relative" 才能起作用。


以下实例设置了垂直滚动监听：


## 实例


```css
<body data-spy="scroll" data-target="#myScrollspy" data-offset="1">

  <div class="container-fluid">
    <div class="row">
      <nav class="col-sm-3 col-4" id="myScrollspy">
        <ul class="nav nav-pills flex-column">
          <li class="nav-item">
            <a class="nav-link active" href="#section1">Section 1</a>
          </li>
          ...
        </ul>
      </nav>
      <div class="col-sm-9 col-8">
        <div id="section1">
          <h1>Section 1</h1>
          <p>Try to scroll this page and look at the navigation list while scrolling!</p>
        </div>
        ...
      </div>
    </div>
  </div>

</body>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_scrollspy2)







	  AI 思考中...





			* [Bootstrap4 弹出框](https://www.runoob.com/bootstrap4-popover.html)
			[Bootstrap4 小工具](https://www.runoob.com/bootstrap4-utilities.html) **













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
# 响应式 Web 设计 - 介绍

- Source: https://www.runoob.com/css/css-rwd-intro.html

---


## 什么是响应式 Web 设计?


响应式 Web 设计让你的网页能在所有设备上有好显示。


响应式 Web 设计只使用 HTML 和 CSS。


响应式 Web 设计不是一个程序或 Javascript 脚本。

响应式 Web 设计是一种能够适应不同设备和屏幕尺寸的网站设计方法，它可以提供一致的用户体验，并确保网站内容在任何设备上都能够完整显示和易于使用。


---


## 设计最好的用户体验


响应式 Web 设计是一种用于创建适应不同设备和屏幕尺寸的网站的方法。随着各种设备和屏幕尺寸的不断增多，如手机、平板电脑和桌面电脑，用户希望能够在任何设备上都能够正常浏览网站并获得良好的用户体验。


传统的网页设计通常是为桌面电脑设计的，但在移动设备上浏览时，页面可能会显示不完整或需要水平滚动。响应式 Web 设计通过使用灵活的网页布局、CSS 媒体查询和图像处理技术，使网站能够自适应不同的屏幕尺寸和设备。


实现响应式 Web 设计的关键是使用流式布局（Fluid Layout），即使用相对单位（如百分比）而不是固定单位（如像素）来定义页面元素的尺寸。此外，媒体查询（Media Queries）允许根据设备的特性（如屏幕宽度、分辨率和方向）应用不同的 CSS 样式。通过组合流式布局和媒体查询，可以根据屏幕尺寸动态调整页面的布局和样式，以提供最佳的用户体验。


响应式 Web 设计还包括针对移动设备优化的图像处理技术。例如，可以使用自适应图像（Responsive Images）来根据屏幕分辨率加载不同尺寸的图像，以减少页面加载时间和带宽使用。


网页应该根据设备的大小自动调整内容。


### 桌面设备

![](https://www.runoob.com/wp-content/uploads/2015/06/rwd_desktop.png)

### 平板设备

![](https://www.runoob.com/wp-content/uploads/2015/06/rwd_tablet.png)

### 手机设备

![](https://www.runoob.com/wp-content/uploads/2015/06/rwd_phone.png)


页面的设计与开发根据用户行为以及设备环境(系统平台、屏幕尺寸、屏幕定向等)进行相应的响应和调整称之为响应式 Web 设计。


### 简单实例

以下是一个简单的响应式 Web 设计的示例，假设我们要创建一个简单的导航栏，在不同屏幕尺寸下具有不同的布局和样式。


## HTML 代码：


```css
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <nav class="navbar">
        <a href="#" class="logo">Logo</a>
        <ul class="menu">
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact</a></li>
        </ul>
    </nav>
</body>
</html>
```


## CSS 代码


```css
/* 导航栏样式 */
.navbar {
    background-color: #333;
    padding: 10px;
    display: flex;
    justify-content: space-between;
}

/* Logo 样式 */
.logo {
    color: #fff;
    font-size: 20px;
    text-decoration: none;
}

/* 菜单样式 */
.menu {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: flex;
}

.menu li {
    margin-left: 10px;
}

.menu li a {
    color: #fff;
    text-decoration: none;
}

/* 媒体查询：在小屏幕上进行布局调整 */
@media screen and (max-width: 600px) {
    .navbar {
        flex-direction: column;
        align-items: center;
    }

    .menu {
        margin-top: 10px;
    }

    .menu li {
        margin-left: 0;
    }
}
```

**[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_rs_test)


在以上实例中，我们首先使用``标签设置视口（viewport），以确保网页在移动设备上以正确的比例显示。然后，我们通过``标签将样式表链接到 HTML 文件中。


在 CSS 中，我们定义了导航栏的样式（`.navbar`）以及 Logo（`.logo`）和菜单（`.menu`）的样式。菜单使用 Flexbox 布局实现水平排列。


接下来，我们使用媒体查询（`@media`）在小屏幕上进行布局调整。当屏幕宽度小于等于 600 像素时，媒体查询的样式将适用。在这种情况下，导航栏的方向将更改为垂直排列，菜单将居中对齐，并且菜单项的左边距将设置为 0。


通过这个简单的示例，当在不同设备上查看时，导航栏的布局和样式将根据屏幕尺寸自动调整，从而提供更好的用户体验。








	  AI 思考中...





			** [CSS 组合选择符](https://www.runoob.com/css-combinators.html)
			[响应式 Web 设计 – Viewport](https://www.runoob.com/css-rwd-viewport.html) **













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

      : ·[CSS 实例](https://www.runoob.com/css-examples.html)

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
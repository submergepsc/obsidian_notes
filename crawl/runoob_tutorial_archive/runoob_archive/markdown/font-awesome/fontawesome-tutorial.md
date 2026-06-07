# Font Awesome 图标

- Source: https://www.runoob.com/font-awesome/fontawesome-tutorial.html

Font Awesome 是一个流行的图标字体库，用于网页设计和开发。


Font Awesome 包含了一系列矢量图标，可以轻松地通过 CSS 进行调用和使用，它可以被定制大小、颜色、阴影等。


Font Awesome 最初是一个由 Dave Gandy 创建的开源项目，目的是提供一套灵活、易用且具有可扩展性的图标集，以替代传统的图像图标。

Font Awesome 更新了很多版本，目前主流是 **Font Awesome 6** 、**Font Awesome 5** 以及 **Font Awesome 4**，所有版本可以参考 ：[https://fontawesome.com/versions](https://fontawesome.com/versions)。


本站测试使用了 **Font Awesome 4**，图标列表： [https://fontawesome.com/v4/icons/](https://fontawesome.com/v4/icons/)。


要使用 Font Awesome 图标，请在 HTML 页面的 **** 部分中添加以下行：


1、国内推荐 CDN：


```css
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
```


2、海外推荐 CDN


```css
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/[email protected]/css/font-awesome.min.css">
```


3、直接下载到本地


[Download](https://static.runoob.com/download/font-awesome-4.7.0.zip)

**
注意：** 不太建议下载来安装，直接在 html 文档头部引用 CDN 文件即可。


**注意：** 本教程使用的是 4.7.0 版本。


您可以使用前缀 **fa** 和图标的名称来放置 Font Awesome 图标。


## 实例


```css
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>

<i class="fa fa-car"></i>
<i class="fa fa-car" style="font-size:48px;"></i>
<i class="fa fa-car" style="font-size:60px;color:red;"></i>

</body>
</html>
```


结果:


```css

```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryicons_awesome_intro_basic)

点击 "尝试一下" 按钮查看在线实例


Font Awesome 设计为与内联元素一起使用。 和  元素广泛用于图标。


另外注意，如果更改图标容器的字体大小或颜色，图标会更改。


---


## 大图标


fa-lg (增加33％)，fa-2x，fa-3x， fa-4x，或 fa-5x 类用于增加相对于其容器的图标大小。


## 实例


```css
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<body>

<i class="fa fa-car fa-lg"></i>
<i class="fa fa-car fa-2x"></i>
<i class="fa fa-car fa-3x"></i>
<i class="fa fa-car fa-4x"></i>
<i class="fa fa-car fa-5x"></i>

</body>
</html>
```


结果:


```css

```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryicons_awesome_intro_larger)


提示： 如果你的图标在顶部和底部被切断，请增加行高。


---

## 列表图标

fa-ul 和 fa-li 类用于替换无序列表中的默认前缀。


## 实例


```css
<ul class="fa-ul">
  <li><i class="fa-li fa fa-check-square"></i>List icons</li>
  <li><i class="fa-li fa fa-spinner fa-spin"></i>List icons</li>
  <li><i class="fa-li fa fa-square"></i>List icons</li>
</ul>
```


结果:


```css
List icons
  List icons
  List icons
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryicons_awesome_intro_list)


---


## 边界和被拉的图标


fa-border，fa-pull-right 或 fa-pull-left 类用于拉式引用或文章图标。


## 实例


```css
<i class="fa fa-quote-left fa-3x fa-pull-left fa-border"></i>
菜鸟教程 -- 学的不仅是技术，更是梦想！！！<br>
菜鸟教程 -- 学的不仅是技术，更是梦想！！！<br>
菜鸟教程 -- 学的不仅是技术，更是梦想！！！<br>
菜鸟教程 -- 学的不仅是技术，更是梦想！！！
```


结果:


```css
菜鸟教程 -- 学的不仅是技术，更是梦想！！！
菜鸟教程 -- 学的不仅是技术，更是梦想！！！
菜鸟教程 -- 学的不仅是技术，更是梦想！！！
菜鸟教程 -- 学的不仅是技术，更是梦想！！！
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryicons_awesome_intro_pull)


---


## 动态图标

fa-spin 类可以让图标旋转, fa-pulse 类可以使图标以 8 步为周期进行旋转。


## 实例


```css
<i class="fa fa-spinner fa-spin"></i>
<i class="fa fa-circle-o-notch fa-spin"></i>
<i class="fa fa-refresh fa-spin"></i>
<i class="fa fa-cog fa-spin"></i>
<i class="fa fa-spinner fa-pulse"></i>
```


结果:


```css

```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryicons_awesome_intro_animate)


注意:** IE8 和 IE9 不支持 CSS3 动画。


---

## 旋转和翻转的图标

fa-rotate-* 和 fa-flip-* 类用于旋转和翻转图标。


## 实例


```css
<i class="fa fa-shield"></i>
<i class="fa fa-shield fa-rotate-90"></i>
<i class="fa fa-shield fa-rotate-180"></i>
<i class="fa fa-shield fa-rotate-270"></i>
<i class="fa fa-shield fa-flip-horizontal"></i>
<i class="fa fa-shield fa-flip-vertical"></i>
```


结果:


```css

```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryicons_awesome_intro_rotate)


---

## 堆叠的图标

要堆叠多个图标，请使用父级上的 fa-stack 类，fa-stack-1x 类用于常规大小的图标，fa-stack-2x 用于较大的图标。

fa-inverse 类可以用作替代图标颜色。您还可以向父级添加更大的图标类，以进一步控制尺寸。


## 实例


```css
<span class="fa-stack fa-lg">
  <i class="fa fa-circle-thin fa-stack-2x"></i>
  <i class="fa fa-twitter fa-stack-1x"></i>
</span>
fa-twitter on fa-circle-thin<br>

<span class="fa-stack fa-lg">
  <i class="fa fa-circle fa-stack-2x"></i>
  <i class="fa fa-twitter fa-stack-1x fa-inverse"></i>
</span>
fa-twitter (inverse) on fa-circle<br>

<span class="fa-stack fa-lg">
  <i class="fa fa-camera fa-stack-1x"></i>
  <i class="fa fa-ban fa-stack-2x text-danger" style="color:red;"></i>
</span>
fa-ban on fa-camera
```


结果:


```css
fa-twitter on fa-circle-thin

fa-twitter (inverse) on fa-circle

fa-ban on fa-camera
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryicons_awesome_intro_stack)


---

## 固定宽度图标

fa-fw 类用于设置固定宽度的图标。 当不同的图标宽度偏离对齐时，此类非常有用。 特别适用于Bootstrap的导航列表和列表组。


## 实例


```css
<div class="list-group">
  <a href="#" class="list-group-item"><i class="fa fa-home fa-fw"></i> Home</a>
  <a href="#" class="list-group-item"><i class="fa fa-book fa-fw"></i> Library</a>
  <a href="#" class="list-group-item"><i class="fa fa-pencil fa-fw"></i> Applications</a>
  <a href="#" class="list-group-item"><i class="fa fa-cog fa-fw"></i> Settings</a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryicons_awesome_intro_fixed)









	  AI 思考中...






			[Font Awesome 品牌图标](https://www.runoob.com/fontawesome-icons-brand.html) **













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
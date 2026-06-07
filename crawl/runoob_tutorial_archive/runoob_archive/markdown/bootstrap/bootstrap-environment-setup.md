# Bootstrap 环境安装

- Source: https://www.runoob.com/bootstrap/bootstrap-environment-setup.html

Bootstrap 安装是非常容易的。本章将讲解如何下载并安装 Bootstrap，讨论 Bootstrap 文件结构，并通过一个实例演示它的用法。


## 下载 Bootstrap


您可以从 [http://getbootstrap.com/](https://getbootstrap.com/) 上下载 Bootstrap 的最新版本。当您点击这个链接时，您将看到如下所示的网页：

![Bootstrap 下载](https://www.runoob.com/wp-content/uploads/2014/06/bootstrapdowloadscreen.jpg)

您会看到两个按钮：


- *Download Bootstrap*：下载 Bootstrap。点击该按钮，您可以下载 Bootstrap CSS、JavaScript 和字体的预编译的压缩版本。不包含文档和最初的源代码文件。
- *Download Source*：下载源代码。点击该按钮，您可以直接从 from 上得到最新的 Bootstrap LESS 和 JavaScript 源代码。


如果您使用的是未编译的源代码，您需要编译 LESS 文件来生成可重用的 CSS 文件。对于编译 LESS 文件，Bootstrap 官方只支持 [Recess](http://twitter.github.io/recess/)，这是 Twitter 的基于 [less.js](http://lesscss.org/) 的 CSS 提示。


为了更好的了解和更方便的使用，我们将在本教程中使用 Bootstrap 的预编译版本。


由于文件是被编译过和压缩过的，在独立的功能开发中，您不必每次都包含这些独立的文件。

本教程编写时，使用的是最新版（Bootstrap 3）。


## 文件结构


### 预编译的 Bootstrap


当您下载了 Bootstrap 的已编译的版本，解压缩 ZIP 文件，您将看到下面的文件/目录结构：

![已编译的 Bootstrap 文件结构](https://www.runoob.com/wp-content/uploads/2014/06/compiledfilestructure.jpg)

如上图所示，可以看到已编译的 CSS 和 JS（bootstrap.*），以及已编译压缩的 CSS 和 JS（bootstrap.min.*）。同时也包含了 Glyphicons 的字体，这是一个可选的 Bootstrap 主题。


### Bootstrap 源代码


如果您下载了 Bootstrap 源代码，那么文件结构将如下所示：

![Bootstrap 源代码结构](https://www.runoob.com/wp-content/uploads/2014/06/sourcecodefilestructure.jpg)

- *less/*、*js/* 和 *fonts/* 下的文件分别是 Bootstrap CSS、JS 和图标字体的源代码。
- *dist/* 文件夹包含了上面预编译下载部分中所列的文件和文件夹。
- *docs-assets/*、*examples/* 和所有的 **.html* 文件是 Bootstrap 文档。


## HTML 模板


一个使用了 Bootstrap 的基本的 HTML 模板如下所示：


## 实例


```css
<!DOCTYPE html>
<html>
   <head>
      <title>Bootstrap 模板</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <!-- 引入 Bootstrap -->
      <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

      <!-- HTML5 Shiv 和 Respond.js 用于让 IE8 支持 HTML5元素和媒体查询 -->
      <!-- 注意： 如果通过 file://  引入 Respond.js 文件，则该文件无法起效果 -->
      <!--[if lt IE 9]>
         <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
         <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
      <![endif]-->
   </head>
   <body>
      <h1>Hello, world!</h1>

      <!-- jQuery (Bootstrap 的 JavaScript 插件需要引入 jQuery) -->
      <script src="https://code.jquery.com/jquery.js"></script>
      <!-- 包括所有已编译的插件 -->
      <script src="js/bootstrap.min.js"></script>
   </body>
</html>
```


在这里，您可以看到包含了 **jquery.js**、**bootstrap.min.js** 和 **bootstrap.min.css** 文件，用于让一个常规的 HTML 文件变为使用了 Bootstrap 的模板。


有关上面代码段中每个元素的细节将在 [Bootstrap CSS 概览](https://www.runoob.com/bootstrap-css-overview.html) 章节详细讲解。


## 实例


现在让我们尝试使用Bootstrap输出"Hello, world!"：


## 实例


```css
<h1>Hello, world!</h1>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=bootstrap3-environment-setup)


---


## Staticfile CDN 推荐


国内推荐使用 Staticfile CDN 上的库：


```css
<!-- 新 Bootstrap 核心 CSS 文件 -->
<link href="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
<script src="https://cdn.staticfile.org/jquery/2.1.1/jquery.min.js"></script>

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="https://cdn.staticfile.org/twitter-bootstrap/3.3.7/js/bootstrap.min.js"></script>
```


此外，你还可以使用以下的 CDN 服务：


- 国际推荐使用：[https://cdnjs.com/](https://cdnjs.com/)








	  AI 思考中...





			** [Bootstrap 简介](https://www.runoob.com/bootstrap-intro.html)
			[Bootstrap CSS 概览](https://www.runoob.com/bootstrap-css-overview.html) **













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
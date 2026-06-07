# Bootstrap4 安装使用

- Source: https://www.runoob.com/bootstrap4/bootstrap4-install.html

我们可以通过以下两种方式来安装 Bootstrap4：


- 使用 Bootstrap 4 CDN。
- 从官网 [getbootstrap.com](https://getbootstrap.com/docs/4.1/getting-started/download/) 下载 Bootstrap 4。 ![](https://www.runoob.com/wp-content/uploads/2017/10/4D026288-A0DB-4CB3-9921-5EABC450C650.jpg)


### Bootstrap 4 CDN


国内推荐使用字节跳动静态资源公共库：


## Bootstrap4 CDN


```css
<!-- 新 Bootstrap4 核心 CSS 文件 -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.1/css/bootstrap.min.css">

<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>

<!-- bootstrap.bundle.min.js 用于弹窗、提示、下拉菜单，包含了 popper.min.js -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/2.11.2/umd/popper.min.js"></script>

<!-- 最新的 Bootstrap4 核心 JavaScript 文件 -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.6.1/js/bootstrap.min.js"></script>
```


国内推荐使用 Staticfile CDN 上的库：


## Bootstrap4 CDN


```css
<!-- 新 Bootstrap4 核心 CSS 文件 -->
<link rel="stylesheet" href="https://cdn.staticfile.net/twitter-bootstrap/4.3.1/css/bootstrap.min.css">

<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
<script src="https://cdn.staticfile.net/jquery/3.2.1/jquery.min.js"></script>

<!-- bootstrap.bundle.min.js 用于弹窗、提示、下拉菜单，包含了 popper.min.js -->
<script src="https://cdn.staticfile.net/popper.js/1.15.0/umd/popper.min.js"></script>

<!-- 最新的 Bootstrap4 核心 JavaScript 文件 -->
<script src="https://cdn.staticfile.net/twitter-bootstrap/4.3.1/js/bootstrap.min.js"></script>
```


**
注意：**popper.min.js 用于设置弹窗、提示、下拉菜单，目前 bootstrap.bundle.min.js 已经包含了 [popper.min.js](https://github.com/FezVrasta/popper.js)。


此外，你还可以使用以下的 CDN 服务：


- 国内推荐使用 1：[https://cdn.bytedance.com/](https://cdn.bytedance.com/)
- 国内推荐使用 2：[https://www.staticfile.net/](https://www.staticfile.net/)
- 国际推荐使用：[https://cdnjs.com/](https://cdnjs.com/)


### 下载 Bootstrap 4


你可以去官网 [https://getbootstrap.com/](https://getbootstrap.com/) 下载 Bootstrap4 资源库。


**

注：**此外你还可以通过包的管理工具 npm、 gem、 composer 等来安装：


```
npm install [email protected]
gem 'bootstrap', '~> 4.0.0.beta2'
composer require twbs/bootstrap:4.0.0-beta.2
```


---


## 创建第一个 Bootstrap 4 页面


### 1、添加 HTML5 doctype


Bootstrap 要求使用 HTML5 文件类型，所以需要添加 HTML5 doctype 声明。


HTML5 doctype 在文档头部声明，并设置对应编码:


```css
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
</html>
```


### 移动设备优先


为了让 Bootstrap 开发的网站对移动设备友好，确保适当的绘制和触屏缩放，需要在网页的 head 之中添加 viewport meta 标签，如下所示：


```
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
```


`width=device-width` 表示宽度是设备屏幕的宽度。


`initial-scale=1` 表示初始的缩放比例。


shrink-to-fit=no 自动适应手机屏幕的宽度。


---


## 容器类


Bootstrap 4 需要一个容器元素来包裹网站的内容。


我们可以使用以下两个容器类：


- .container 类用于固定宽度并支持响应式布局的容器。
- .container-fluid 类用于 100% 宽度，占据全部视口（viewport）的容器。


![](https://www.runoob.com/wp-content/uploads/2017/10/176B67B9-013C-429C-8FD0-BC2409011545.jpg)


---

## 两个 Bootstrap 4 页面


## Bootstrap4 .container 实例


```css
<div class="container">
  <h1>我的第一个 Bootstrap 页面</h1>
  <p>这是一些文本。</p>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_gs_container)


以下实例展示了占据全部视口（viewport）的容器。


## Bootstrap4 .container-fluid 实例


```css
<div class="container-fluid">
  <h1>我的第一个 Bootstrap 页面</h1>
  <p>使用了 .container-fluid，100% 宽度，占据全部视口（viewport）的容器。</p>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_gs_container-fluid)








	  AI 思考中...





			** [Bootstrap4 教程](https://www.runoob.com/bootstrap4-tutorial.html)
			[Bootstrap4 网格系统](https://www.runoob.com/bootstrap4-grid-basic.html) **













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
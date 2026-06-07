# Foundation 起步

- Source: https://www.runoob.com/foundation/foundation-get-started.html

---


## 什么是 Foundation？


- Foundation 是一个免费的前端框架，用于快速开发。
- Foundation 包含了 HTML 和 CSS 的设计模板，提供多种 Web 上的 UI 组件，如表单、按钮、Tabs 等等。同时也提供了多种 JavaScript 插件。
- Foundation 移动优先，可创建响应式网页。
- Foundation 适用于初学者和专业人士。
- Foundation 已使用在 Facebook, eBay, Samsung, Amazon, Disney等。

**

|  | 什么是响应式网页设计？ 响应式Web设计(Responsive Web design)的理念是： 页面的设计与开发应当根据用户行为以及设备环境(系统平台、屏幕尺寸、屏幕定向等)进行相应的响应和调整。 |
| --- | --- |


---


## 从哪里下载 Foundation?


你可以通过以下两种方式来获取 Foundation：


1、从官网下载最新版本：[http://foundation.zurb.com/](http://foundation.zurb.com/)。


2、使用 Staticfile 提供的CDN（推荐）：


```
<!-- css 文件 -->
<link rel="stylesheet" href="https://cdn.staticfile.net/foundation/5.5.3/css/foundation.min.css">

<!-- jQuery 库 -->
<script src="https://cdn.staticfile.net/foundation/5.5.3/js/vendor/jquery.js"></script>

<!-- JavaScript 文件 -->
<script src="https://cdn.staticfile.net/foundation/5.5.3/js/foundation.min.js"></script>

<!-- modernizr.js 文件 -->
<script src="https://cdn.staticfile.net/foundation/5.5.3/js/vendor/modernizr.js"></script>
```


本站静态 CDN 基于阿里云服务。


|  | Foundation 使用 CDN 的优势: Foundation 使用 CDN 提高了企业站点(尤其含有大量图片和静态页面站点)的访问速度，并大大提高以上性质站点的稳定性 为什么使用 modernizr?Some Foundation 的组件使用了比较前前沿的 HTML5 和 CSS3 特性，但不是所有浏览器都支持。 Modernizr 是一个用于检测用户浏览器HTML5和CSS3特性的JavaScript库 - 让组件能在所有浏览器上正常运行。 |
| --- | --- |


---


## 使用 Foundation 创建页面


1. 添加 HTML5 doctype**


Foundation 使用 HTML 元素和 CSS 属性，所以需要添加 HTML5 doctype 文档类型声明。


同时我们可以设置文档的语言属性 lang 及字符编码：


```
<!DOCTYPE html><html lang="zh-cn">  <head>
  <meta charset="utf-8">   </head></html>
```


**2. Foundation 5 移动优先**


Foundation 5 为移动设备的响应式设计。框架的核心是移动优先。


为了确保页面可自由缩放可以在 `` 元素中添加以下 `` 标签:


```
<meta name="viewport" content="width=device-width, initial-scale=1">
```


- width：控制 viewport 的大小，可以指定的一个值，如果 600，或者特殊的值，如 device-width 为设备的宽度（单位为缩放为 100% 时的 CSS 的像素）。
- initial-scale：初始缩放比例，也即是当页面第一次 load 的时候缩放比例。


**3. 初始化组件**


一些 Foundation 组件是基于 jQuery 开发的，如：模态框、下拉菜单等。你可以使用以下脚本来初始化组件：


```
<script>$(document).ready(function() {
  $(document).foundation();})</script>
```


---


## 基本 Foundation 页面


如何创建一个基本的 foundation 页面:


### Foundation 实例


```
<div class="row">
  <div class="medium-12 columns">
    <div class="panel">
      <h1>Foundation 页面</h1>
      <p>重置窗口大小，查看效果！</p>
      <button type="button" class="button small">我是按钮!</button>
    </div>
  </div>
</div>

<div class="row">
  <div class="medium-4 columns">
    <h3>菜鸟教程</h3>
    <p>学的不仅是技术，更是梦想！！！</p>
  </div>
  <div class="medium-4 columns">
    <h3>菜鸟教程</h3>
    <p>学的不仅是技术，更是梦想！！！</p>
  </div>
  <div class="medium-4 columns">
    <h3>菜鸟教程</h3>
    <p>学的不仅是技术，更是梦想！！！</p>
  </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_default)







	  AI 思考中...





			** [Foundation 教程](https://www.runoob.com/foundation-tutorial.html)
			[Foundation 文本](https://www.runoob.com/foundation-typography.html) **













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
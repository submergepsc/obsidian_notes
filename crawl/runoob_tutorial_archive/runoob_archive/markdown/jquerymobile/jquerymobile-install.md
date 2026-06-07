# jQuery Mobile 安装

- Source: https://www.runoob.com/jquerymobile/jquerymobile-install.html

---


## 在你的网页中添加 jQuery Mobile


你可以通过以下几种方式将jQuery Mobile添加到你的网页中：


- 从 CDN 中加载 jQuery Mobile (推荐)
- 从jQuerymobile.com 下载 jQuery Mobile库


---


## 从 CDN 中加载 jQuery Mobile


|  | CDN的全称是Content Delivery Network，即内容分发网络。其基本思路是尽可能避开互联网上有可能影响数据传输速度和稳定性的瓶颈和环节，使内容传输的更快、更稳定。. |
| --- | --- |


使用 jQuery 内核, 你不需要在电脑上安装任何东西; 你仅仅需要在你的网页中加载以下层叠样式 (.css) 和 JavaScript 库 (.js) 就能够使用 jQuery Mobile:


## jQuery Mobile CDN:


```javascript
<head><!-- meta使用viewport以确保页面可自由缩放 --><meta name="viewport" content="width=device-width,
  initial-scale=1"><!-- 引入 jQuery Mobile 样式 -->
  <link rel="stylesheet" href="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.css">
  <!-- 引入 jQuery 库 -->
  <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
  <!-- 引入 jQuery Mobile 库 -->
  <script src="http://code.jquery.com/mobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
</head>
```

**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lib_jquery1)


国内用户推荐使用百度CDN：


## jQuery Mobile CDN(百度):


```javascript
<head><!-- meta使用viewport以确保页面可自由缩放 --><meta name="viewport" content="width=device-width,
  initial-scale=1"><!-- 引入 jQuery Mobile 样式 -->
  <link rel="stylesheet" href="http://apps.bdimg.com/libs/jquerymobile/1.4.5/jquery.mobile-1.4.5.min.css">
  <!-- 引入 jQuery 库 -->
  <script src="http://apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js"></script>
  <!-- 引入 jQuery Mobile 库 -->
  <script src="http://apps.bdimg.com/libs/jquerymobile/1.4.5/jquery.mobile-1.4.5.min.js"></script>
</head>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_lib_jquery)


本教程引用的库为百度 CDN 资源库。


---


## 下载 jQuery Mobile


如果你想将 jQuery Mobile 放于你的主机中,你可以从 [jQuerymobile.com](http://jquerymobile.com/download/)下载该文件。


```
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="jquery.mobile-1.4.5.css">
<script src="jquery.js"></script>
<script src="jquery.mobile-1.4.5.js"></script>
</head>
```


提示：** 将下载的文件放置于与网页同一目录下。**


|  | 你是否想知道为什么在 标签中 没有插入 type="text/javascript" ? 在 HTML5 已经不需要该属性。 JavaScript 在所有现代浏览器中是 HTML5 的默认脚本语言！ |
| --- | --- |








	  AI 思考中...





			** [jQuery Mobile 简介](https://www.runoob.com/jquerymobile-intro.html)
			[jQuery Mobile 页面](https://www.runoob.com/jquerymobile-pages.html) **













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
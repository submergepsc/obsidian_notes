# Sass 教程

- Source: https://www.runoob.com/sass/sass-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2019/09/sass.png)

Sass (英文全称：Syntactically Awesome Stylesheets) 是一个最初由 Hampton Catlin 设计并由 Natalie Weizenbaum 开发的层叠样式表语言。


Sass 是一个 CSS 预处理器。


Sass 是 CSS 扩展语言，可以帮助我们减少 CSS 重复的代码，节省开发时间。


Sass 完全兼容所有版本的 CSS。


Sass 扩展了 CSS3，增加了规则、变量、混入、选择器、继承、内置函数等等特性。


Sass 生成良好格式化的 CSS 代码，易于组织和维护。


Sass 文件后缀为 **.scss**。


## Sass 实例


```css
/* 定义变量与值 */
$bgcolor: lightblue;
$textcolor: darkblue;
$fontsize: 18px;

/* 使用变量 */
body {
  background-color: $bgcolor;
  color: $textcolor;
  font-size: $fontsize;
}
```


**
## 阅读本教程前，您需要了解的知识：


阅读本教程，您需要有以下基础：


- [HTML 教程](https://www.runoob.com/../html/html-tutorial.html)
- [CSS 教程](https://www.runoob.com/../css/css-tutorial.html)


---

## 为什么使用 Sass?

CSS 本身语法不够强大，导致重复编写一些代码，无法实现复用，而且在代码也不方便维护。


Sass 引入合理的样式复用机制，增加了规则、变量、混入、选择器、继承、内置函数等等特性。


我们可以举个例子，我们会在 CSS 中重复使用很多次十六进制的颜色代码，当有了变量之后，如果要改变颜色代码，只要修改变量的值就好了：


## Sass 实例


```css
/* 定义颜色变量，要修改颜色值，修改这里就可以了 */
$primary_1: #a2b9bc;
$primary_2: #b2ad7f;
$primary_3: #878f99;

/* 使用变量 */
.main-header {
  background-color: $primary_1;
}

.menu-left {
  background-color: $primary_2;
}

.menu-right {
  background-color: $primary_3;
}
```


---


## Sass 是如何工作的？


浏览器并不支持 Sass 代码。因此，你需要使用一个 Sass 预处理器将 Sass 代码转换为 CSS 代码。










	  AI 思考中...






			[Sass 安装](https://www.runoob.com/sass-install.html) **













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
# AngularJS 简介

- Source: https://www.runoob.com/angularjs/angularjs-intro.html

---


AngularJS 是一个 **JavaScript 框架**。它可通过  标签添加到 HTML 页面。


AngularJS 通过 **[指令](https://www.runoob.com/angularjs-directives.html)** 扩展了 HTML，且通过 **[表达式](https://www.runoob.com/angularjs-expressions.html)** 绑定数据到 HTML。


---


## AngularJS 是一个 JavaScript 框架


AngularJS 是一个 JavaScript 框架。它是一个以 JavaScript 编写的库。


AngularJS 是以一个 JavaScript 文件形式发布的，可通过 script 标签添加到网页中：


```javascript
<script src="https://cdn.staticfile.org/angular.js/1.4.6/angular.min.js"></script>
```


|  | 我们建议把脚本放在 元素的底部。 这会提高网页加载速度，因为 HTML 加载不受制于脚本加载。 |
| --- | --- |


各个 angular.js 版本下载： [https://github.com/angular/angular.js/releases](https://github.com/angular/angular.js/releases)


---


## AngularJS 扩展了 HTML


AngularJS 通过 **ng-directives** 扩展了 HTML。


**ng-app** 指令定义一个 AngularJS 应用程序。


**ng-model** 指令把元素值（比如输入域的值）绑定到应用程序。


**ng-bind** 指令把应用程序数据绑定到 HTML 视图。


## AngularJS 实例


```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://cdn.staticfile.org/angular.js/1.4.6/angular.min.js"></script>
</head>
<body>

<div ng-app="">
    <p>名字 : <input type="text" ng-model="name"></p>
    <h1>Hello {{name}}</h1>
    <p ng-bind="name"></p>
</div>

</body>
</html>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_ng_intro)


实例讲解：


当网页加载完毕，AngularJS 自动开启。


ng-app** 指令告诉 AngularJS， 元素是 AngularJS **应用程序** 的"所有者"。


**ng-model** 指令把输入域的值绑定到应用程序变量 **name**。


**ng-bind** 指令把应用程序变量 name 绑定到某个段落的 innerHTML。


|  | 如果您移除了 ng-app 指令，HTML 将直接把表达式显示出来，不会去计算表达式的结果。 |
| --- | --- |


---


## 什么是 AngularJS？


AngularJS 使得开发现代的单一页面应用程序（SPAs：Single Page Applications）变得更加容易。


- AngularJS 把应用程序数据绑定到 HTML 元素。
- AngularJS 可以克隆和重复 HTML 元素。
- AngularJS 可以隐藏和显示 HTML 元素。
- AngularJS 可以在 HTML 元素"背后"添加代码。
- AngularJS 支持输入验证。


---


## AngularJS 指令


正如您所看到的，AngularJS 指令是以 **ng** 作为前缀的 HTML 属性。


**ng-init** 指令初始化 AngularJS 应用程序变量。


## AngularJS 实例


```javascript
<div ng-app="" ng-init="firstName='John'">

<p>姓名为 <span ng-bind="firstName"></span></p>

</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_ng_intro_directives)


|  | HTML5 允许扩展的（自制的）属性，以 data- 开头。 AngularJS 属性以 ng- 开头，但是您可以使用 data-ng- 来让网页对 HTML5 有效。 |
| --- | --- |


带有有效的 HTML5：


## AngularJS 实例


```javascript
<div data-ng-app="" data-ng-init="firstName='John'">

<p>姓名为 <span data-ng-bind="firstName"></span></p>

</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_ng_intro_directives_html)


---


## AngularJS 表达式


AngularJS 表达式写在双大括号内：{{ expression }}**。


AngularJS 表达式把数据绑定到 HTML，这与 **ng-bind** 指令有异曲同工之妙。


AngularJS 将在表达式书写的位置"输出"数据。


**AngularJS 表达式** 很像 **JavaScript 表达式**：它们可以包含文字、运算符和变量。


实例 {{ 5 + 5 }} 或 {{ firstName + " " + lastName }}


## AngularJS 实例


```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script src="https://cdn.staticfile.org/angular.js/1.4.6/angular.min.js"></script>
</head>
<body>

<div ng-app="">
     <p>我的第一个表达式： {{ 5 + 5 }}</p>
</div>

</body>
</html>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_ng_intro_expression)


---


## AngularJS 应用


AngularJS 模块（Module）** 定义了 AngularJS 应用。


AngularJS **控制器（Controller）** 用于控制 AngularJS 应用。


**ng-app**指令指明了应用, **ng-controller** 指明了控制器。


## AngularJS 实例


```javascript
<div ng-app="myApp" ng-controller="myCtrl">

名: <input type="text" ng-model="firstName"><br>
姓: <input type="text" ng-model="lastName"><br>
<br>
姓名: {{firstName + " " + lastName}}

</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.firstName= "John";
    $scope.lastName= "Doe";
});
</script>
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_intro_controller)


AngularJS 模块定义应用:


## AngularJS 模块


```javascript
var app = angular.module('myApp', []);
```


AngularJS 控制器控制应用:


## AngularJS 控制器



```javascript
app.controller('myCtrl', function($scope) {
    $scope.firstName= "John";
    $scope.lastName= "Doe";
});
```


在接下来的教程中你将学习到更多的应用和模块的知识。









	  AI 思考中...





			** [AngularJS 教程](https://www.runoob.com/angularjs-tutorial.html)
			[AngularJS 表达式](https://www.runoob.com/angularjs-expressions.html) **













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
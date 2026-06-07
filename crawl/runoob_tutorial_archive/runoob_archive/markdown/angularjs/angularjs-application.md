# AngularJS 应用

- Source: https://www.runoob.com/angularjs/angularjs-application.html

---


现在是时候创建一个真正的 AngularJS 单页 Web 应用（single page web application，SPA）了。


---


## AngularJS 应用实例


您已经学习了足够多关于 AngularJS 的知识，现在可以开始创建您的第一个 AngularJS 应用程序：


## 我的笔记


**

保存
清除

剩余字数: 100**


**


---


## 应用程序讲解


## AngularJS 实例


```javascript
<html ng-app="myNoteApp">
<head>
<meta charset="utf-8">
<script src="https://cdn.staticfile.net/angular.js/1.4.6/angular.min.js"></script>
</head>
<body><div ng-controller="myNoteCtrl">
<h2>我的笔记</h2>
<p><textarea ng-model="message" cols="40" rows="10"></textarea></p>
<p>
<button ng-click="save()">保存</button>
<button ng-click="clear()">清除</button>
</p>
<p>Number of characters left: <span ng-bind="left()"></span></p>
</div><script src="myNoteApp.js"></script>
<script src="myNoteCtrl.js"></script>
	</body></html>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_note_app)


应用程序文件 "myNoteApp.js":


```javascript
var app = angular.module("myNoteApp", []);
```


控制器文件 "myNoteCtrl.js":


```javascript
app.controller("myNoteCtrl", function($scope) {
    $scope.message
= "";    $scope.left  = function() {return 100 -
$scope.message.length;};    $scope.clear = function()
{$scope.message = "";};
    $scope.save  = function() {alert("Note Saved");};
});
```


 元素是 AngularJS 应用: ng-app="myNoteApp**" 的容器:


```javascript
<html ng-app="myNoteApp">
```


 是 HTML 页面中控制器: ng-controller="**myNoteCtrl**" 的作用域:


```javascript
<div ng-controller="myNoteCtrl">
```


**ng-model** 指令绑定了  到控制器变量 ** message**:


```javascript
<textarea ng-model="message" cols="40" rows="10"></textarea>
```


两个 **ng-click** 事件调用了控制器函数 **clear()** 和 **save()**:


```javascript
<button ng-click="save()">Save</button>
<button ng-click="clear()">Clear</button>
```


**ng-bind** 指令绑定控制器函数 **left()** 到 ，用于显示剩余字符:


```javascript
Number of characters left: <span ng-bind="left()"></span>
```


应用库文件需要在 AngularJs 加载后才能执行：


```javascript
<script src="myNoteApp.js"></script>
<script src="myNoteCtrl.js"></script>
```


---

## AngularJS 应用架构


以上实例是一个完整的 AngularJS 单页Web应用（single page web application，SPA）。


 元素包含了 AngularJS 应用 (**ng-app=**)。


 元素定义了 AngularJS 控制器的作用域 (**ng-controller=**)。


在一个应用可以有很多控制器。


应用文件(**my...App.js**) 定义了应用模型代码。


一个或多个控制器文件 (**my...Ctrl.js**) 定义了控制器代码。


---


## 总结 - 它是如何工作的呢？


ng-app 指令位于应用的根元素下。


对于单页Web应用（single page web application，SPA），应用的根通常为  元素。


一个或多个 ng-controller 指令定义了应用的控制器。每个控制器有他自己的作用域：: 定义的 HTML 元素。


AngularJS 在 HTML DOMContentLoaded 事件中自动开始。如果找到 ng-app 指令 ， AngularJS 载入指令中的模块，并将 ng-app 作为应用的根进行编译。


应用的根可以是整个页面，或者页面的一小部分，如果是一小部分会更快编译和执行。









	  AI 思考中...





			** [AngularJS 模块](https://www.runoob.com/angularjs-modules.html)
			[AngularJS 实例](https://www.runoob.com/angularjs-examples.html) **













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
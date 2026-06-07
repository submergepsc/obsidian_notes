# AngularJS 动画

- Source: https://www.runoob.com/angularjs/angularjs-animations.html

AngularJS 提供了动画效果，可以配合 CSS 使用。


AngularJS 使用动画需要引入 angular-animate.min.js 库。


```
<script src="http://cdn.static.runoob.com/libs/angular.js/1.4.6/angular-animate.min.js"></script>
```


还需在应用中使用模型 ngAnimate：


```
<body ng-app="ngAnimate">
```


---


## 什么是动画？


动画是通过改变 HTML 元素产生的动态变化效果。


### 实例


勾选复选框隐藏 DIV:


```javascript
<body ng-app="ngAnimate">隐藏 DIV: <input type="checkbox" ng-model="myCheck">
	<div ng-hide="myCheck"></div></body>
```


	**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_animation)


|  | 应用中动画不宜太多，但合适的使用动画可以增加页面的丰富性，也可以更易让用户理解。 |
| --- | --- |


如果我们应用已经设置了应用名，可以把 ngAnimate 直接添加在模型中：


### 实例


```javascript
<body ng-app="myApp"><h1>隐藏 DIV: <input type="checkbox" ng-model="myCheck"></h1>
	<div ng-hide="myCheck"></div><script>
```


var app =
	angular.module('myApp', ['ngAnimate']);

</script>

[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_animation2)


---


## ngAnimate 做了什么?


ngAnimate 模型可以添加或移除 class 。


ngAnimate 模型并不能使 HTML 元素产生动画，但是 ngAnimate 会监测事件，类似隐藏显示 HTML 元素 ，如果事件发生 ngAnimate 就会使用预定义的 class 来设置 HTML 元素的动画。


AngularJS 添加/移除 class 的指令:


- `ng-show`
- `ng-hide`
- `ng-class`
- `ng-view`
- `ng-include`
- `ng-repeat`
- `ng-if`
- `ng-switch`


`ng-show` 和 `ng-hide` 指令用于添加或移除 `ng-hide` class 的值。


其他指令会在进入 DOM 会添加 `ng-enter` 类，移除 DOM 会添加 `ng-leave` 属性。


当 HTML 元素位置改变时，`ng-repeat` 指令同样可以添加 `ng-move` 类 。


此外， 在动画完成后，HTML 元素的类集合将被移除。例如： `ng-hide` 指令会添加以下类：


- `ng-animate`
- `ng-hide-animate`
- `ng-hide-add` (如果元素将被隐藏)
- `ng-hide-remove` (如果元素将显示)
- `ng-hide-add-active` (如果元素将隐藏)
- `ng-hide-remove-active` (如果元素将显示)


---


## 使用 CSS 动画


我们可以使用 CSS transition(过渡) 或 CSS 动画让 HTML 元素产生动画效果，该部分内容你可以参阅我们的 [CSS 过渡教程](https://www.runoob.com/../css/css3-transitions.html)， [CSS 动画教程](https://www.runoob.com/../css/css3-animations.html)。


---


## CSS 过渡


CSS 过渡可以让我们平滑的将一个 CSS 属性值修改为另外一个：


### 实例


在 DIV 元素设置了 `.ng-hide` 类时，过渡需要花费 0.5 秒，高度从 100px 变为 0:


```javascript
<style>div {    transition: all linear 0.5s;
	background-color: lightblue;    height: 100px;}.ng-hide
	{    height: 0;}</style>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_animation_css)


---


## CSS 动画


CSS 动画允许你平滑的修改 CSS 属性值:


### 实例


在 DIV 元素设置了 `.ng-hide` 类时, `myChange` 动画将执行，它会平滑的将高度从 100px 变为 0:


```javascript
<style>@keyframes myChange {    from {
	height: 100px;    } to {
	height: 0;    }}div {
	height: 100px;    background-color: lightblue;}
	div.ng-hide {    animation: 0.5s myChange;}</style>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_animation_css2)









	  AI 思考中...





			** [AngularJS 服务(Service)](https://www.runoob.com/angularjs-services.html)
			[AngularJS 依赖注入](https://www.runoob.com/angularjs-dependency-injection.html) **













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
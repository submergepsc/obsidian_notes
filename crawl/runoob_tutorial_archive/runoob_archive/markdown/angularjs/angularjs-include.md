# AngularJS 包含

- Source: https://www.runoob.com/angularjs/angularjs-include.html

---


在 AngularJS 中，你可以在 HTML 中包含 HTML 文件。


---


## 在 HTML 中包含 HTML 文件


在 HTML 中，目前还不支持包含 HTML 文件的功能。


---


## 服务端包含


大多服务端脚本都支持包含文件功能 (**SSI**： Server Side Includes)。


使用 SSI, 你可在 HTML 中包含 HTML 文件，并发送到客户端浏览器。


## PHP 实例


```javascript
<?php require("navigation.php"); ?>
```


---


## 客户端包含


通过 JavaScript 有很多种方式可以在 HTML 中包含 HTML 文件。


通常我们使用 http 请求 (**AJAX**) 从服务端获取数据，返回的数据我们可以通过 使用 **innerHTML** 写入到 HTML 元素中。


---


## AngularJS 包含


使用 AngularJS, 你可以使用 **ng-include** 指令来包含 HTML 内容:


## 实例


```javascript
<body ng-app="">

<div ng-include="'runoob.htm'"></div>

</body>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_ng_include)


步骤如下：


---


## runoob.htm 文件代码：


```javascript
<h1>菜鸟教程</h1>
<p>这是一个被包含的 HTML 页面，使用 ng-include 指令来实现！</p>
```




---


## 包含 AngularJS 代码


ng-include 指令除了可以包含 HTML 文件外，还可以包含 AngularJS 代码:


## sites.htm 文件代码：


```javascript
<table>
<tr ng-repeat="x in names">
<td>{{ x.Name }}</td>
<td>{{ x.Url }}</td>
</tr>
</table>
```




包含的文件 "sites.php" 中有 AngularJS 代码，它将被正常执行：


## 实例


```javascript
<div ng-app="myApp" ng-controller="sitesCtrl">
  <div ng-include="'sites.htm'"></div>
</div>

<script>
var app = angular.module('myApp', []);
app.controller('sitesCtrl', function($scope, $http) {
    $http.get("sites.php").then(function (response) {
        $scope.names = response.data.records;
    });
});
</script>
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_ng_include_table)


---


## 跨域包含


默认情况下， ng-include 指令不允许包含其他域名的文件。

如果你需要包含其他域名的文件，你需要设置域名访问白名单：


## sites.htm 文件代码：


```javascript
<body ng-app="myApp">

<div ng-include="'https://c.runoob.com/runoobtest/angular_include.php'"></div>

<script>
var app = angular.module('myApp', [])
app.config(function($sceDelegateProvider) {
    $sceDelegateProvider.resourceUrlWhitelist([
        'https://c.runoob.com/runoobtest/**'
    ]);
});
</script>

</body>
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=try_ng_include_crossdomain)


此外，你还需要设置服务端允许跨域访问，设置方法可参考：[PHP Ajax 跨域问题最佳解决方案。](https://www.runoob.com/w3cnote/php-ajax-cross-border.html)


## angular_include.php 文件代码：


```javascript
<?php
// 允许所有域名可以访问
header('Access-Control-Allow-Origin:*');

echo '<b style="color:red">我是跨域的内容</b>';
?>
```











	  AI 思考中...





			** [AngularJS Bootstrap](https://www.runoob.com/angularjs-bootstrap.html)
			[AngularJS API](https://www.runoob.com/angularjs-api.html) **













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
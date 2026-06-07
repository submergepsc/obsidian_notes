# AngularJS XMLHttpRequest

- Source: https://www.runoob.com/angularjs/angularjs-http.html

---


**$http** 是 AngularJS 中的一个核心服务，用于读取远程服务器的数据。


使用格式：


```
// 简单的 GET 请求，可以改为 POST
$http({
    method: 'GET',
    url: '/someUrl'
}).then(function successCallback(response) {
        // 请求成功执行代码
    }, function errorCallback(response) {
        // 请求失败执行代码
});
```


### 简写方法


POST 与 GET 简写方法格式：


```
$http.get('/someUrl', config).then(successCallback, errorCallback);
$http.post('/someUrl', data, config).then(successCallback, errorCallback);
```


此外还有以下简写方法：


- $http.get
- $http.head
- $http.post
- $http.put
- $http.delete
- $http.jsonp
- $http.patch


更详细内容可参见：[https://docs.angularjs.org/api/ng/service/$http](https://docs.angularjs.org/api/ng/service/$http)


---


## 读取 JSON 文件


以下是存储在web服务器上的 JSON 文件：


## https://www.runoob.com/try/angularjs/data/sites.php


```javascript
{
    "sites": [
        {
            "Name": "菜鸟教程",
            "Url": "www.runoob.com",
            "Country": "CN"
        },
        {
            "Name": "Google",
            "Url": "www.google.com",
            "Country": "USA"
        },
        {
            "Name": "Facebook",
            "Url": "www.facebook.com",
            "Country": "USA"
        },
        {
            "Name": "微博",
            "Url": "www.weibo.com",
            "Country": "CN"
        }
    ]
}
```


---


## AngularJS $http


AngularJS $http 是一个用于读取web服务器上数据的服务。


$http.get(url) 是用于读取服务器数据的函数。

**

### 废弃声明 (v1.5)



v1.5 中`$http` 的 `success` 和 `error` 方法已废弃。使用 `then` 方法替代。


### 通用方法实例


## AngularJS1.5 以上版本 - 实例


```javascript
var app = angular.module('myApp', []);

app.controller('siteCtrl', function($scope, $http) {
    $http({
        method: 'GET',
        url: 'https://www.runoob.com/try/angularjs/data/sites.php'
    }).then(function successCallback(response) {
            $scope.names = response.data.sites;
        }, function errorCallback(response) {
            // 请求失败执行代码
    });

});
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_customers_json3)


### 简写方法实例


## AngularJS1.5 以上版本 - 实例


```javascript
<div ng-app="myApp" ng-controller="siteCtrl">

<ul>
  <li ng-repeat="x in names">
    {{ x.Name + ', ' + x.Country }}
  </li>
</ul>

</div>

<script>
var app = angular.module('myApp', []);
app.controller('siteCtrl', function($scope, $http) {
  $http.get("https://www.runoob.com/try/angularjs/data/sites.php")
  .then(function (response) {$scope.names = response.data.sites;});
});
</script>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_customers_json2)


## AngularJS1.5 以下版本 - 实例


```javascript
<div ng-app="myApp" ng-controller="siteCtrl">

<ul>
  <li ng-repeat="x in names">
    {{ x.Name + ', ' + x.Country }}
  </li>
</ul>

</div>

<script>
var app = angular.module('myApp', []);
app.controller('siteCtrl', function($scope, $http) {
  $http.get("https://www.runoob.com/try/angularjs/data/sites.php")
  .success(function (response) {$scope.names = response.sites;});
});
</script>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_customers_json)


应用解析:**


注意：以上代码的 get 请求是本站的服务器，你不能直接拷贝到你本地运行，会存在跨域问题，解决办法就是将 Customers_JSON.php 的数据拷贝到你自己的服务器上，附：[PHP Ajax 跨域问题最佳解决方案](https://www.runoob.com/w3cnote/php-ajax-cross-border.html)。


AngularJS 应用通过 **ng-app** 定义。应用在  中执行。


**ng-controller** 指令设置了 **controller 对象** 名。


函数 **customersController** 是一个标准的 JavaScript ** 对象构造器**。


控制器对象有一个属性: **$scope.names**。


**$http.get()** 从web服务器上读取静态 **JSON 数据**。


服务器数据文件为： [** https://www.runoob.com/try/angularjs/data/sites.php**](https://www.runoob.com/try/angularjs/data/sites.php)。


当从服务端载入 JSON 数据时，**$scope.names** 变为一个数组。


|  | 以上代码也可以用于读取数据库数据。 |
| --- | --- |









	  AI 思考中...





			** [AngularJS 参考手册](https://www.runoob.com/angularjs-reference.html)
			[AngularJS 表格](https://www.runoob.com/angularjs-tables.html) **













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
# AngularJS API

- Source: https://www.runoob.com/angularjs/angularjs-api.html

---


API 意为 **A**pplication **P**rogramming **I**nterface（应用程序编程接口）。


---


## AngularJS 全局 API


AngularJS 全局 API 用于执行常见任务的 JavaScript 函数集合，如：


- 比较对象
- 迭代对象
- 转换对象


全局 API 函数使用 angular 对象进行访问。


以下列出了一些通用的 API 函数：


| API | 描述 |
| --- | --- |
| angular.lowercase ( angular.$$lowercase()（angular1.7+） | 转换字符串为小写 |
| angular.uppercase() ( angular.$$uppercase()（angular1.7+） | 转换字符串为大写 |
| angular.isString() | 判断给定的对象是否为字符串，如果是返回 true。 |
| angular.isNumber() | 判断给定的对象是否为数字，如果是返回 true。 |


**注意：**自 AngularJS 1.7 之后移除 angular.lowercase 和 angular.uppercase 方法, 改为 angular.$$lowercase 和 angular.$$uppercase


---


### angular.lowercase()


## 实例


```javascript
<div ng-app="myApp" ng-controller="myCtrl">
<p>{{ x1 }}</p>
<p>{{ x2 }}</p>
</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.x1 = "RUNOOB";
    $scope.x2 = angular.$$lowercase($scope.x1);
});
</script>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_api_lowercase)


### angular.uppercase()


## 实例


```javascript
<div ng-app="myApp" ng-controller="myCtrl">
<p>{{ x1 }}</p>
<p>{{ x2 }}</p>
</div>
​
<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
    $scope.x1 = "runoob";
    $scope.x2 = angular.$$uppercase($scope.x1);
});
</script>
​
```


 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_api_uppercase)


### angular.isString()


## 实例


```javascript
<div ng-app="myApp" ng-controller="myCtrl">
 <p>{{ x1 }}</p><p>{{ x2 }}</p></div>
<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
$scope.x1 = "RUNOOB";
$scope.x2 = angular.isString($scope.x1);
});
</script>
```


 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_api_isstring)


### angular.isNumber()


## 实例


```javascript
<div ng-app="myApp" ng-controller="myCtrl">
 <p>{{ x1 }}</p><p>{{ x2 }}</p></div>
<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope) {
$scope.x1 = "RUNOOB";
$scope.x2 = angular.isNumber($scope.x1);
});
</script>
```


 [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=try_ng_api_isnumber)








	  AI 思考中...





			** [AngularJS 包含](https://www.runoob.com/angularjs-include.html)
			[AngularJS ng-model 指令](https://www.runoob.com/angularjs-model.html) **
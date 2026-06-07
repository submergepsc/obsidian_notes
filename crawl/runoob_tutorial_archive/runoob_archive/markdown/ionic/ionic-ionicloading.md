# ionic 加载动作

- Source: https://www.runoob.com/ionic/ionic-ionicloading.html

$ionicLoading 是 ionic 默认的一个加载交互效果。里面的内容也是可以在模板里面修改。


### 用法


```
angular.module('LoadingApp', ['ionic'])
.controller('LoadingCtrl', function($scope, $ionicLoading) {
  $scope.show = function() {
    $ionicLoading.show({
      template: 'Loading...'
    });
  };
  $scope.hide = function(){
    $ionicLoading.hide();
  };
});
```


### 方法


显示一个加载效果。


```
show(opts)
```


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| opts | object | loading指示器的选项。可用属性： {string=} template 指示器的html内容。 {string=} templateUrl 一个加载html模板的url作为指示器的内容。 {boolean=} noBackdrop 是否隐藏背景。默认情况下它会显示。 {number=} delay 指示器延迟多少毫秒显示。默认为不延迟。 {number=} duration 等待多少毫秒后自动隐藏指示器。默认情况下，指示器会一直显示，直到触发.hide()。 |


隐藏一个加载效果。


```
hide()
```


### API


| 属性 | 类型 | 详情 |
| --- | --- | --- |
| delegate-handle (可选) | 字符串 | 该句柄定义带有$ionicListDelegate的列表。 |
| show-delete (可选) | 布尔值 | 列表项的删除按钮当前是显示还是隐藏。 |
| show-reorder (可选) | 布尔值 | 列表项的排序按钮当前是显示还是隐藏。 |
| can-swipe (可选) | 布尔值 | 列表项是否被允许滑动显示选项按钮。默认：true。 |


---


## 实例


### HTML 代码：


```
<html ng-app="ionicApp">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no, width=device-width">

    <title>Ionic Modal</title>

     <link href="http://www.runoob.com/static/ionic/css/ionic.min.css" rel="stylesheet">
    <script src="http://www.runoob.com/static/ionic/js/ionic.bundle.min.js"></script>
  </head>
  <body ng-controller="AppCtrl">

      <ion-view title="Home">
        <ion-header-bar>
          <h1 class="title">The Stooges</h1>
        </ion-header-bar>
        <ion-content has-header="true">
          <ion-list>
            <ion-item ng-repeat="stooge in stooges" href="#">{{stooge.name}}</ion-item>
          </ion-list>
        </ion-content>
      </ion-view>

  </body>
</html>
```


### JavaScript 代码


```
angular.module('ionicApp', ['ionic'])
.controller('AppCtrl', function($scope, $timeout, $ionicLoading) {

  // Setup the loader
  $ionicLoading.show({
    content: 'Loading',
    animation: 'fade-in',
    showBackdrop: true,
    maxWidth: 200,
    showDelay: 0
  });

  // Set a timeout to clear loader, however you would actually call the $ionicLoading.hide(); method whenever everything is ready or loaded.
  $timeout(function () {
    $ionicLoading.hide();
    $scope.stooges = [{name: 'Moe'}, {name: 'Larry'}, {name: 'Curly'}];
  }, 2000);

});
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_ionicloading)


---


## $ionicLoadingConfig


设置加载的默认选项:


### 用法:


```
var app = angular.module('myApp', ['ionic'])
app.constant('$ionicLoadingConfig', {
  template: '默认加载模板……'
});
app.controller('AppCtrl', function($scope, $ionicLoading) {
  $scope.showLoading = function() {
    $ionicLoading.show(); //配置选项在 $ionicLoadingConfig 设置
  };
});
```









	  AI 思考中...





			** [ionic 列表操作](https://www.runoob.com/ionic-ion-list.html)
			[ionic 模态窗口](https://www.runoob.com/ionic-ion-modal.html) **













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
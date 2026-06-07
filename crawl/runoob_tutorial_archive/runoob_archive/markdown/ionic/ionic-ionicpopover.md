# ionic 浮动框

- Source: https://www.runoob.com/ionic/ionic-ionicpopover.html

---


## $ionicPopover


$ionicPopover 是一个可以浮在app内容上的一个视图框。


可以实现以下功能点：


- 在当前页面显示更多信息。
- 选择一些工具或配置。
- 在页面提供一个操作列表。


### 方法


```
fromTemplate(templateString, options)
或
fromTemplateUrl(templateUrl, options)
```


参数说明：


templateString: 模板字符串。


templateUrl: 载入的模板 URL。


options: 初始化选项。


## 实例


## HTML 代码部分


```
<p>
<button ng-click="openPopover($event)">打开浮动框</button>
</p>
<script id="my-popover.html" type="text/ng-template">
<ion-popover-view>
  <ion-header-bar>
    <h1 class="title">我的浮动框标题</h1>
  </ion-header-bar>
  <ion-content>
    Hello!
  </ion-content>
</ion-popover-view>
</script>
```


## fromTemplateUrl 方法


```
angular.module('ionicApp', ['ionic'])
.controller( 'AppCtrl',['$scope','$ionicPopover','$timeout',function($scope,$ionicPopover,$timeout){

  $scope.popover = $ionicPopover.fromTemplateUrl('my-popover.html', {
    scope: $scope
  });

  // .fromTemplateUrl() 方法
  $ionicPopover.fromTemplateUrl('my-popover.html', {
    scope: $scope
  }).then(function(popover) {
    $scope.popover = popover;
  });

  $scope.openPopover = function($event) {
    $scope.popover.show($event);
  };
  $scope.closePopover = function() {
    $scope.popover.hide();
  };
  // 清除浮动框
  $scope.$on('$destroy', function() {
    $scope.popover.remove();
  });
  // 在隐藏浮动框后执行
  $scope.$on('popover.hidden', function() {
    // 执行代码
  });
  // 移除浮动框后执行
  $scope.$on('popover.removed', function() {
    // 执行代码
  });

}])
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=ionic_ionicpopover)


我们也可以把模板当作一个字符串，使用 .fromTemplate() 方法来实现弹框:


## fromTemplate 方法


```
angular.module('ionicApp', ['ionic'])
.controller( 'AppCtrl',['$scope','$ionicPopover','$timeout',function($scope,$ionicPopover,$timeout){

  $scope.popover = $ionicPopover.fromTemplateUrl('my-popover.html', {
    scope: $scope
  });
  // .fromTemplate() 方法
  var template = '<ion-popover-view><ion-header-bar> <h1 class="title">我的浮动框标题</h1> </ion-header-bar> <ion-content> Hello! </ion-content></ion-popover-view>';
      $scope.popover = $ionicPopover.fromTemplate(template, {
    scope: $scope
  });

  $scope.openPopover = function($event) {
    $scope.popover.show($event);
  };
  $scope.closePopover = function() {
    $scope.popover.hide();
  };
  // 清除浮动框
  $scope.$on('$destroy', function() {
    $scope.popover.remove();
  });
  // 在隐藏浮动框后执行
  $scope.$on('popover.hidden', function() {
    // 执行代码
  });
  // 移除浮动框后执行
  $scope.$on('popover.removed', function() {
    // 执行代码
  });

}])
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=ionic_ionicpopover1)








	  AI 思考中...





			** [ionic 平台](https://www.runoob.com/ionic-ionicplatform.html)
			[ionic 对话框](https://www.runoob.com/ionic-ionicpopup.html) **













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
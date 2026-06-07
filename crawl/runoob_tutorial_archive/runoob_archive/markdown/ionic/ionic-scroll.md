# ionic 滚动条

- Source: https://www.runoob.com/ionic/ionic-scroll.html

---


## ion-scroll


ion-scroll 用于创建一个可滚动的容器。


### 用法


```
<ion-scroll
    [delegate-handle=""]
    [direction=""]
    [paging=""]
    [on-refresh=""]
    [on-scroll=""]
    [scrollbar-x=""]
    [scrollbar-y=""]
    [zooming=""]
    [min-zoom=""]
    [max-zoom=""]>
    ...
</ion-scroll>
```


### API


| 属性 | 类型 | 详情 |
| --- | --- | --- |
| delegate-handle (可选) | 字符串 | 该句柄利用$ionicScrollDelegate指定滚动视图。 |
| direction (可选) | 字符串 | 滚动的方向。 'x' 或 'y'。 默认 'y'。 |
| paging (可选) | 布尔值 | 分页是否滚动。 |
| on-refresh (可选) | 表达式 | 调用下拉刷新， 由ionRefresher触发。 |
| on-scroll (可选) | 表达式 | 当用户滚动时触发。 |
| scrollbar-x (可选) | 布尔值 | 是否显示水平滚动条。默认为false。 |
| scrollbar-y (可选) | 布尔值 | 是否显示垂直滚动条。默认为true。 |
| zooming (可选) | 布尔值 | 是否支持双指缩放。 |
| min-zoom (可选) | 整数 | 允许的最小缩放量（默认为0.5） |
| max-zoom (可选) | 整数 | 允许的最大缩放量（默认为3） |


### 实例


### HTML 代码


```
<ion-scroll zooming="true" direction="xy" style="width: 500px; height: 500px">
    <div style="width: 5000px; height: 5000px; background: url('http://www.runoob.com/try/demo_source/Europe_geological_map-en.jpg') repeat"></div>
</ion-scroll>
```


### CSS 代码


```
body {
  cursor: url('http://www.runoob.com/try/demo_source/finger.png'), auto;
}
```


### JavaScript 代码


```
angular.module('ionicApp', ['ionic']);
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_ion-scroll)


---


## ion-infinite-scroll


当用户到达页脚或页脚附近时，ionInfiniteScroll指令允许你调用一个函数 。

当用户滚动的距离超出底部的内容时，就会触发你指定的on-infinite。


### 用法


```
<ion-content ng-controller="MyController">
  <ion-infinite-scroll
    on-infinite="loadMore()"
    distance="1%">
  </ion-infinite-scroll>
</ion-content>
```


```
function MyController($scope, $http) {
  $scope.items = [];
  $scope.loadMore = function() {
    $http.get('/more-items').success(function(items) {
      useItems(items);
      $scope.$broadcast('scroll.infiniteScrollComplete');
    });
  };

  $scope.$on('stateChangeSuccess', function() {
    $scope.loadMore();
  });
}
```


当没有更多数据加载时，就可以用一个简单的方法阻止无限滚动，那就是angular的ng-if 指令:


```
<ion-infinite-scroll
  ng-if="moreDataCanBeLoaded()"
  icon="ion-loading-c"
  on-infinite="loadMoreData()">
</ion-infinite-scroll>
```


### API


| 属性 | 类型 | 详情 |
| --- | --- | --- |
| on-infinite | 表达式 | 当滚动到底部时触发的事件。 |
| distance (可选) | 字符串 | 从底部滚动到触发on-infinite表达式的距离。默认: 1%。 |
| icon (可选) | 字符串 | 当加载时显示的图标。默认: 'ion-loading-d'。 |


---


## $ionicScrollDelegate


授权控制滚动视图（通过ion-content 和 ion-scroll指令创建）。

该方法直接被$ionicScrollDelegate服务触发，来控制所有滚动视图。用 $getByHandle方法控制特定的滚动视图。


### 用法


```
<body ng-controller="MainCtrl">
  <ion-content>
    <button ng-click="scrollTop()">滚动到顶部!</button>
  </ion-content>
</body>
```


```
function MainCtrl($scope, $ionicScrollDelegate) {
  $scope.scrollTop = function() {
    $ionicScrollDelegate.scrollTop();
  };
}
```


### 方法


```
resize()
```


告诉滚动视图重新计算它的容器大小。


```
scrollTop([shouldAnimate])
```


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| shouldAnimate (可选) | 布尔值 | 是否应用滚动动画。 |


```
scrollBottom([shouldAnimate])
```


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| shouldAnimate (可选) | 布尔值 | 是否应用滚动动画。 |








	  AI 思考中...





			** [ionic 对话框](https://www.runoob.com/ionic-ionicpopup.html)
			[ionic 侧栏菜单](https://www.runoob.com/ionic-ion-side-menus.html) **













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
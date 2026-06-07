# ionic 列表操作

- Source: https://www.runoob.com/ionic/ionic-ion-list.html

列表是一个应用广泛在几乎所有移动app中的界面元素。ionList 和 ionItem 这两个指令还支持多种多样的交互模式，比如移除其中的某一项，拖动重新排序，滑动编辑等等。


### 用法


```
<ion-list>
  <ion-item ng-repeat="item in items">
    Hello, {{item}}!
  </ion-item>
</ion-list>
```


### 高级用法: 缩略图，删除按钮，重新排序，滑动


```
<ion-list ng-controller="MyCtrl"
          show-delete="shouldShowDelete"
          show-reorder="shouldShowReorder"
          can-swipe="listCanSwipe">
  <ion-item ng-repeat="item in items"
            class="item-thumbnail-left">

    <img ng-src="{{item.img}}">
    <h2>{{item.title}}</h2>
    <p>{{item.description}}</p>
    <ion-option-button class="button-positive"
                       ng-click="share(item)">
      分享
    </ion-option-button>
    <ion-option-button class="button-info"
                       ng-click="edit(item)">
      编辑
    </ion-option-button>
    <ion-delete-button class="ion-minus-circled"
                       ng-click="items.splice($index, 1)">
    </ion-delete-button>
    <ion-reorder-button class="ion-navicon"
                        on-reorder="reorderItem(item, $fromIndex, $toIndex)">
    </ion-reorder-button>

  </ion-item>
</ion-list>
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
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>Ionic List Directive</title>

    <link href="http://www.runoob.com/static/ionic/css/ionic.min.css" rel="stylesheet">
    <script src="http://www.runoob.com/static/ionic/js/ionic.bundle.min.js"></script>
  </head>

  <body ng-controller="MyCtrl">

    <ion-header-bar class="bar-positive">
      <div class="buttons">
        <button class="button button-icon icon ion-ios-minus-outline"
          ng-click="data.showDelete = !data.showDelete; data.showReorder = false"></button>
      </div>
      <h1 class="title">Ionic Delete/Option Buttons</h1>
      <div class="buttons">
        <button class="button" ng-click="data.showDelete = false; data.showReorder = !data.showReorder">
            Reorder
        </button>
      </div>
    </ion-header-bar>

    <ion-content>

      <!-- The list directive is great, but be sure to also checkout the collection repeat directive when scrolling through large lists -->

      <ion-list show-delete="data.showDelete" show-reorder="data.showReorder">

        <ion-item ng-repeat="item in items"
                  item="item"
                  href="#/item/{{item.id}}" class="item-remove-animate">
          Item {{ item.id }}
          <ion-delete-button class="ion-minus-circled"
                             ng-click="onItemDelete(item)">
          </ion-delete-button>
          <ion-option-button class="button-assertive"
                             ng-click="edit(item)">
            Edit
          </ion-option-button>
          <ion-option-button class="button-calm"
                             ng-click="share(item)">
            Share
          </ion-option-button>
          <ion-reorder-button class="ion-navicon" on-reorder="moveItem(item, $fromIndex, $toIndex)"></ion-reorder-button>
        </ion-item>

      </ion-list>

    </ion-content>

  </body>
</html>
```


### CSS 代码


```
body {
  cursor: url('http://www.runoob.com/try/demo_source/finger.png'), auto;
}
```


### JavaScript 代码


```
angular.module('ionicApp', ['ionic'])

.controller('MyCtrl', function($scope) {

  $scope.data = {
    showDelete: false
  };

  $scope.edit = function(item) {
    alert('Edit Item: ' + item.id);
  };
  $scope.share = function(item) {
    alert('Share Item: ' + item.id);
  };

  $scope.moveItem = function(item, fromIndex, toIndex) {
    $scope.items.splice(fromIndex, 1);
    $scope.items.splice(toIndex, 0, item);
  };

  $scope.onItemDelete = function(item) {
    $scope.items.splice($scope.items.indexOf(item), 1);
  };

  $scope.items = [
    { id: 0 },
    { id: 1 },
    { id: 2 },
    { id: 3 },
    { id: 4 },
    { id: 5 },
    { id: 6 },
    { id: 7 },
    { id: 8 },
    { id: 9 },
    { id: 10 },
    { id: 11 },
    { id: 12 },
    { id: 13 },
    { id: 14 },
    { id: 15 },
    { id: 16 },
    { id: 17 },
    { id: 18 },
    { id: 19 },
    { id: 20 },
    { id: 21 },
    { id: 22 },
    { id: 23 },
    { id: 24 },
    { id: 25 },
    { id: 26 },
    { id: 27 },
    { id: 28 },
    { id: 29 },
    { id: 30 },
    { id: 31 },
    { id: 32 },
    { id: 33 },
    { id: 34 },
    { id: 35 },
    { id: 36 },
    { id: 37 },
    { id: 38 },
    { id: 39 },
    { id: 40 },
    { id: 41 },
    { id: 42 },
    { id: 43 },
    { id: 44 },
    { id: 45 },
    { id: 46 },
    { id: 47 },
    { id: 48 },
    { id: 49 },
    { id: 50 }
  ];

});
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_ion-list)








	  AI 思考中...





			** [ionic 头部和底部](https://www.runoob.com/ionic-ion-header-bar.html)
			[ionic 加载动作](https://www.runoob.com/ionic-ionicloading.html) **













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
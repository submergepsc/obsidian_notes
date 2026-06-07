# ionic 复选框

- Source: https://www.runoob.com/ionic/ionic-ion-checkbox.html

ionic 复选框（checkbox）与普通的 HTML 复选框没什么区别，以下实例演示了 ionic 复选框 ion-checkbox 的应用。


```
<ion-checkbox ng-model="isChecked">复选框标签</ion-checkbox>
```


---


## 实例

实例中，会根据复选框是否选中，修改 checked 值，true 为选中， false 为未选中。


### HTML 代码


```
<ion-header-bar class="bar-positive">
  <h1 class="title">复选框</h1>
</ion-header-bar>

<ion-content>

  <div class="list">

    <ion-checkbox ng-repeat="item in devList"
                  ng-model="item.checked"
                  ng-checked="item.checked">
      {{ item.text }}
    </ion-checkbox>

    <div class="item">
      <div ng-bind="devList | json"></div>
    </div>

    <div class="item item-divider">
      Notifications
    </div>

    <ion-checkbox ng-model="pushNotification.checked"
                  ng-change="pushNotificationChange()">
      Push Notifications
    </ion-checkbox>

    <div class="item">
      <div ng-bind="pushNotification | json"></div>
    </div>

    <ion-checkbox ng-model="emailNotification"
                  ng-true-value="'Subscribed'"
                  ng-false-value="'Unubscribed'">
      Newsletter
    </ion-checkbox>
    <div class="item">
      <div ng-bind="emailNotification | json"></div>
    </div>

  </div>

</ion-content>
```


### JavaScript 代码


```
angular.module('starter', ['ionic'])

.run(function($ionicPlatform) {
$ionicPlatform.ready(function() {
  // Hide the accessory bar by default (remove this to show the accessory bar above the keyboard
  // for form inputs)
  if(window.cordova && window.cordova.plugins.Keyboard) {
    cordova.plugins.Keyboard.hideKeyboardAccessoryBar(true);
  }
  if(window.StatusBar) {
    StatusBar.styleDefault();
  }
});
})

.controller( 'actionsheetCtl',['$scope',function($scope){

  $scope.devList = [
      { text: "HTML5", checked: true },
      { text: "CSS3", checked: false },
      { text: "JavaScript", checked: false }
    ];

    $scope.pushNotificationChange = function() {
      console.log('Push Notification Change', $scope.pushNotification.checked);
    };

    $scope.pushNotification = { checked: true };
    $scope.emailNotification = 'Subscribed';

}])
```


css 代码：


```
body {
  cursor: url('http://www.runoob.com/try/demo_source/finger.png'), auto;
}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_ion-checkbox)


效果如下所示：

*







	  AI 思考中...





			* [ionic 下拉刷新](https://www.runoob.com/ionic-ion-refresher.html)
			[ionic 单选框操作](https://www.runoob.com/ionic-ion-radio.html) **













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
# ionic 单选框操作

- Source: https://www.runoob.com/ionic/ionic-ion-radio.html

实例中，根据选中的不同选项，显示不同的值。


### HTML 代码


```
<ion-header-bar class="bar-positive">
  <h1 class="title">当选按钮</h1>
</ion-header-bar>

<ion-content>

  <div class="list">

    <div class="item item-divider">
      选取的值为: {{ data.clientSide }}
    </div>

    <ion-radio ng-repeat="item in clientSideList"
               ng-value="item.value"
               ng-model="data.clientSide">
      {{ item.text }}
    </ion-radio>

    <div class="item item-divider">
      Serverside, Selected Value: {{ data.serverSide }}
    </div>

    <ion-radio ng-repeat="item in serverSideList"
               ng-value="item.value"
               ng-model="data.serverSide"
               ng-change="serverSideChange(item)"
               name="server-side">
      {{ item.text }}
    </ion-radio>

  </div>

</ion-content>
```


### JavaScript 代码


```
angular.module('ionicApp', ['ionic'])

.controller('MainCtrl', function($scope) {

  $scope.clientSideList = [
    { text: "Backbone", value: "bb" },
    { text: "Angular", value: "ng" },
    { text: "Ember", value: "em" },
    { text: "Knockout", value: "ko" }
  ];

  $scope.serverSideList = [
    { text: "Go", value: "go" },
    { text: "Python", value: "py" },
    { text: "Ruby", value: "rb" },
    { text: "Java", value: "jv" }
  ];

  $scope.data = {
    clientSide: 'ng'
  };

  $scope.serverSideChange = function(item) {
    console.log("Selected Serverside, text:", item.text, "value:", item.value);
  };

});
```


css 代码：


```
body {
  cursor: url('http://www.runoob.com/try/demo_source/finger.png'), auto;
}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_ion-radio)


效果如下所示：

*







	  AI 思考中...





			* [ionic 复选框](https://www.runoob.com/ionic-ion-checkbox.html)
			[ionic 切换开关操作](https://www.runoob.com/ionic-ion-toggle.html) **













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
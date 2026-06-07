# ionic 选项卡栏操作

- Source: https://www.runoob.com/ionic/ionic-ion-tabs.html

---


## ion-tabs


ion-tabs 是有一组页面选项卡组成的选项卡栏。可以通过点击选项来切换页面。

对于 iOS，它会出现在屏幕的底部，Android会出现在屏幕的顶部(导航栏下面)。


### 用法


## 实例


```
<ion-tabs class="tabs-positive tabs-icon-only">

  <ion-tab title="首页" icon-on="ion-ios-filing" icon-off="ion-ios-filing-outline">
    <!-- 标签 1 内容 -->
  </ion-tab>

  <ion-tab title="关于" icon-on="ion-ios-clock" icon-off="ion-ios-clock-outline">
    <!-- 标签 2 内容 -->
  </ion-tab>

  <ion-tab title="设置" icon-on="ion-ios-gear" icon-off="ion-ios-gear-outline">
    <!-- 标签 3 内容 -->
  </ion-tab>
</ion-tabs>
```


**
[尝试一下 »](https://www.runoob.com/try/try.php?filename=ionic_ion-tabs)


效果如下所示：

*

### API


| 属性 | 类型 | 详情 |
| --- | --- | --- |
| delegate-handle (可选) | 字符串 | 该句柄用$ionicTabsDelegate来标识这些选项卡。 |


---


## ion-tab


隶属于ionTabs

包含一个选项卡内容。该内容仅存在于被选中的给定选项卡中。

每个ionTab都有自己的浏览历史。


### 用法


```
<ion-tab
  title="Tab!"
  icon="my-icon"
  href="#/tab/tab-link"
  on-select="onTabSelected()"
  on-deselect="onTabDeselected()">
</ion-tab>
```


### API


| 属性 | 类型 | 详情 |
| --- | --- | --- |
| title | 字符串 | 选项卡的标题。 |
| href (可选) | 字符串 | 当触碰的时候，该选项卡将会跳转的的链接。 |
| icon (可选) | 字符串 | 选项卡的图标。如果给定值，它将成为ion-on和ion-off的默认值。 |
| icon-on (可选) | 字符串 | 被选中标签的图标。 |
| icon-off (可选) | 字符串 | 没被选中标签的图标。 |
| badge (可选) | 表达式 | 选项卡上的徽章（通常是一个数字）。 |
| badge-style (可选) | 表达式 | 选项卡上微章的样式（例，tabs-positive ）。 |
| on-select (可选) | 表达式 | 选项卡被选中时触发。 |
| on-deselect (可选) | 表达式 | 选项卡取消选中时触发。 |
| ng-click (可选) | 表达式 | 通常，点击时选项卡会被选中。如果设置了 ng-Click，它将不会被选中。 你可以用$ionicTabsDelegate.select()来指定切换标签。 |


---


## $ionicTabsDelegate


授权控制ionTabs指令。

该方法直接调用$ionicTabsDelegate服务，控制所有ionTabs指令。用$getByHandle方法控制具体的ionTabs实例。


### 用法


```
<body ng-controller="MyCtrl">
  <ion-tabs>

    <ion-tab title="Tab 1">
      你好，标签1！
      <button ng-click="selectTabWithIndex(1)">选择标签2</button>
    </ion-tab>
    <ion-tab title="Tab 2">你好标签2！</ion-tab>

  </ion-tabs>
</body>
```


```
function MyCtrl($scope, $ionicTabsDelegate) {
  $scope.selectTabWithIndex = function(index) {
    $ionicTabsDelegate.select(index);
  }
}
```


### 方法


```
select(index, [shouldChangeHistory])
```


选择标签来匹配给定的索引。


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| index | 数值 | 选择标签的索引。 |
| shouldChangeHistory (可选) | 布尔值 | 此选项是否应该加载这个标签的浏览历史（如果存在），并使用，或仅加载默认页面。默认为false。提示：如果一个ion-nav-view在选项卡里，你可能需要设置它为true。 |


```
selectedIndex()
```


返回值: **数值, 被选中标签的索引，如 -1。


```
$getByHandle(handle)
```


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| handle | 字符串 |  |

例如:


```
$ionicTabsDelegate.$getByHandle('my-handle').select(0);
```









	  AI 思考中...





			* [ionic 加载动画](https://www.runoob.com/ionic-ion-spinner.html)














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
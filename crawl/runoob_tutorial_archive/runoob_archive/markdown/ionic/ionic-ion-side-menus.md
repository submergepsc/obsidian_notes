# ionic 侧栏菜单

- Source: https://www.runoob.com/ionic/ionic-ion-side-menus.html

一个容器元素包含侧边菜单和主要内容。通过把主要内容区域从一边拖动到另一边，来让左侧或右侧的侧栏菜单进行切换。


效果图如下所示：

![](https://www.runoob.com/wp-content/uploads/2015/08/sidemenu.gif)

### 用法

要使用侧栏菜单，添加一个父元素，一个中间内容 ，和一个或更多  指令。


```
<ion-side-menus>
  <!-- 中间内容 -->
  <ion-side-menu-content ng-controller="ContentController">
  </ion-side-menu-content>

  <!-- 左侧菜单 -->
  <ion-side-menu side="left">
  </ion-side-menu>

  <!-- 右侧菜单 -->
  <ion-side-menu side="right">
  </ion-side-menu>
</ion-side-menus>
```


```
function ContentController($scope, $ionicSideMenuDelegate) {
  $scope.toggleLeft = function() {
    $ionicSideMenuDelegate.toggleLeft();
  };
}
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_side-menus)


### API


| 属性 | 类型 | 详情 |
| --- | --- | --- |
| enable-menu-with-back-views (可选) | 布尔值 | 在返回按钮显示时，确认是否启用侧边栏菜单。 |
| delegate-handle | 字符串 | 该句柄用于标识带有$ionicScrollDelegate的滚动视图。 |


---


## ion-side-menu-content


一个可见主体内容的容器，同级的一个或多个ionSideMenu 指令。


### 用法


```
<ion-side-menu-content
  drag-content="true">
</ion-side-menu-content>
```


### API


| 属性 | 类型 | 详情 |
| --- | --- | --- |
| drag-content (可选) | 布尔值 | 内容是否可被拖动。默认为true。 |


---


## ion-side-menu


一个侧栏菜单的容器，同级的一个ion-side-menu-content 指令。


### 用法


```
<ion-side-menu
  side="left"
  width="myWidthValue + 20"
  is-enabled="shouldLeftSideMenuBeEnabled()">
</ion-side-menu>
```


### API


| 属性 | 类型 | 详情 |
| --- | --- | --- |
| side | 字符串 | 侧栏菜单当前在哪一边。可选的值有: 'left' 或 'right'。 |
| is-enabled (可选) | 布尔值 | 该侧栏菜单是否可用。 |
| width (可选) | 数值 | 侧栏菜单应该有多少像素的宽度。默认为275。 |


---


## menu-toggle


在一个指定的侧栏中切换菜单。


### 用法


下面是一个在导航栏内链接的例子。点击此链接会自动打开指定的侧栏菜单。


```
<ion-view>
  <ion-nav-buttons side="left">
   <button menu-toggle="left" class="button button-icon icon ion-navicon"></button>
  </ion-nav-buttons>
 ...
</ion-view>
```


## menu-close


关闭当前打开的侧栏菜单。


### 用法


下面是一个在导航栏内链接的例子。点击此链接会自动打开指定的侧栏菜单。


```
<a menu-close href="#/home" class="item">首页</a>
```


---


## $ionicSideMenuDelegate


该方法直接触发$ionicSideMenuDelegate服务，来控制所有侧栏菜单。用$getByHandle方法控制特定情况下的ionSideMenus。


### 用法


```
<body ng-controller="MainCtrl">
  <ion-side-menus>
    <ion-side-menu-content>
      内容!
      <button ng-click="toggleLeftSideMenu()">
        切换左侧侧栏菜单
      </button>
    </ion-side-menu-content>
    <ion-side-menu side="left">
      左侧菜单!
    <ion-side-menu>
  </ion-side-menus>
</body>
```


```
function MainCtrl($scope, $ionicSideMenuDelegate) {
  $scope.toggleLeftSideMenu = function() {
    $ionicSideMenuDelegate.toggleLeft();
  };
}
```


### 方法


```
toggleLeft([isOpen])
```


切换左侧侧栏菜单（如果存在）。


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| isOpen (可选) | 布尔值 | 是否打开或关闭菜单。默认：切换菜单。 |


```
toggleRight([isOpen])
```


切换右侧侧栏菜单（如果存在）。


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| isOpen (可选) | 布尔值 | 是否打开或关闭菜单。默认：切换菜单。 |


```
getOpenRatio()
```


获取打开菜单内容超出菜单宽度的比例。比如，一个宽度为100px的菜单被宽度为50px以50%的比例打开，将会返回一个比例值为0.5。

** 返回值: **浮点 0 表示没被打开，如果左侧菜单处于已打开或正在打开为0 到 1，如果右侧菜单处于已打开或正在打开为0 到-1。


```
isOpen()
```


** 返回值: **布尔值，判断左侧或右侧菜单是否已经打开。


```
isOpenLeft()
```


** 返回值: **布尔值左侧菜单是否已经打开。


```
isOpenRight()
```


** 返回值: **布尔值右侧菜单是否已经打开。


```
canDragContent([canDrag])
```


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| canDrag (可选) | 布尔值 | 设置是否可以拖动内容打开侧栏菜单。 |


**返回值:** 布尔值，是否可以拖动内容打开侧栏菜单。


```
$getByHandle(handle)
```


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| handle | 字符串 |  |


例如:


```
$ionicSideMenuDelegate.$getByHandle('my-handle').toggleLeft();
```










	  AI 思考中...





			** [ionic 滚动条](https://www.runoob.com/ionic-scroll.html)
			[ionic 滑动框](https://www.runoob.com/ionic-ion-slide-box.html) **













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
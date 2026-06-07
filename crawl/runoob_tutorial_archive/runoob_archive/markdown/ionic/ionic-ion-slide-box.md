# ionic 滑动框

- Source: https://www.runoob.com/ionic/ionic-ion-slide-box.html

---


## ion-slide-box


滑动框是一个包含多页容器的组件，每页滑动或拖动切换：


效果图如下：

![](https://www.runoob.com/wp-content/uploads/2015/08/slideBox.gif)

### 用法


```
<ion-slide-box on-slide-changed="slideHasChanged($index)">
  <ion-slide>
    <div class="box blue"><h1>BLUE</h1></div>
  </ion-slide>
  <ion-slide>
    <div class="box yellow"><h1>YELLOW</h1></div>
  </ion-slide>
  <ion-slide>
    <div class="box pink"><h1>PINK</h1></div>
  </ion-slide>
</ion-slide-box>
```


### API


| 属性 | 类型 | 详情 |
| --- | --- | --- |
| delegate-handle (可选) | 字符串 | 该句柄用$ionicSlideBoxDelegate来标识这个滑动框。 |
| does-continue (可选) | 布尔值 | 滑动框是否开启循环滚动。 |
| auto-play (可选) | boolean | 设置滑动框是否循环播放，如果 does-continue 为 true，默认也为 true。 |
| slide-interval (可选) | 数字 | 等待多少毫秒开始滑动（如果继续则为true）。默认为4000。 |
| show-pager (可选) | 布尔值 | 滑动框的页面是否显示。 |
| pager-click (可选) | 表达式 | 当点击页面时，触发该表达式（如果shou-pager为true）。传递一个'索引'变量。 |
| on-slide-changed (可选) | 表达式 | 当滑动时，触发该表达式。传递一个'索引'变量。 |
| active-slide (可选) | 表达式 | 将模型绑定到当前滑动框。 |


---


## 实例


### HTML 代码


```
<ion-slide-box active-slide="myActiveSlide">
    <ion-slide>
      <div class="box blue"><h1>BLUE</h1></div>
    </ion-slide>
    <ion-slide>
      <div class="box yellow"><h1>YELLOW</h1></div>
    </ion-slide>
    <ion-slide>
      <div class="box pink"><h1>PINK</h1></div>
    </ion-slide>
</ion-slide-box>
```


### CSS 代码


```
.slider {
  height: 100%;
}
.slider-slide {
  color: #000;
  background-color: #fff; text-align: center;
  font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial, "Lucida Grande", sans-serif; font-weight: 300; }
.blue {
  background-color: blue;
}

.yellow {
  background-color: yellow;
}

.pink {
  background-color: pink;
}
.box{
  height:100%;
}
.box h1{
  position:relative; top:50%; transform:translateY(-50%);
}
```


### JavaScript 代码


```
angular.module('ionicApp', ['ionic'])

.controller('SlideController', function($scope) {

  $scope.myActiveSlide = 1;

})
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_ion-slide-box)









	  AI 思考中...





			** [ionic 侧栏菜单](https://www.runoob.com/ionic-ion-side-menus.html)
			[ionic 加载动画](https://www.runoob.com/ionic-ion-spinner.html) **













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
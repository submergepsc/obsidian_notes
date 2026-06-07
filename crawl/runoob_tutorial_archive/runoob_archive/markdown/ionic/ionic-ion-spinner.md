# ionic 加载动画

- Source: https://www.runoob.com/ionic/ionic-ion-spinner.html

---


## ion-spinner


ionSpinner 提供了许多种旋转加载的动画图标。当你的界面加载时，你就可以呈现给用户相应的加载图标。

该图标采用的是SVG。


### 用法


```
<ion-spinner icon="spiral"></ion-spinner>    //默认用法
```


像大部分其他的ionic组件一样，spinner也可以使用ionic的标准颜色命名规则，就像下面这样：


```
<ion-spinner class="spinner-energized"></ion-spinner>
```


---

实例

### HTML 代码


```
<ion-content scroll="false" class="has-header">
  <p>
    <ion-spinner icon="android"></ion-spinner>
    <ion-spinner icon="ios"></ion-spinner>
    <ion-spinner icon="ios-small"></ion-spinner>
    <ion-spinner icon="bubbles" class="spinner-balanced"></ion-spinner>
    <ion-spinner icon="circles" class="spinner-energized"></ion-spinner>
  </p>

  <p>
    <ion-spinner icon="crescent" class="spinner-royal"></ion-spinner>

    <ion-spinner icon="dots" class="spinner-dark"></ion-spinner>
    <ion-spinner icon="lines" class="spinner-calm"></ion-spinner>
    <ion-spinner icon="ripple" class="spinner-assertive"></ion-spinner>
    <ion-spinner icon="spiral"></ion-spinner>
  </p>


</ion-content>
```


### CSS 代码


```
body {
  cursor: url('http://www.runob.com/try/demo_source/finger.png'), auto;
}
p {
  text-align: center;
  margin-bottom: 40px !important;
}
.spinner svg {
  width: 19% !important;
  height: 85px !important;
}
```


### JavaScript 代码


```
angular.module('ionicApp', ['ionic'])

.controller('MyCtrl', function($scope) {

});
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=ionic_ion-spinner)


效果如下所示：

*








	  AI 思考中...





			* [ionic 滑动框](https://www.runoob.com/ionic-ion-slide-box.html)
			[ionic 选项卡栏操作](https://www.runoob.com/ionic-ion-tabs.html) **













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
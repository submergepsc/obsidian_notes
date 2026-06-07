# ionic 平台

- Source: https://www.runoob.com/ionic/ionic-ionicplatform.html

---


## $ionicPlatform


$ionicPlatform 用来检测当前的平台，以及诸如在PhoneGap/Cordova中覆盖Android后退按钮。


### 方法


```
onHardwareBackButton(callback)
```


有硬件的后退按钮的平台，可以用这种方法绑定到它。


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| callback | function | 当该事件发生时，触发回调函数。 |


```
offHardwareBackButton(callback)
```


移除后退按钮的监听事件。


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| callback | function | 最初绑定的监视器函数。 |


```
registerBackButtonAction(callback, priority, [actionId])
```


注册硬件后退按钮动作。当点击按钮时，只有一个动作会执行，因此该方法决定了注册的后退按钮动作具有最高的优先级。

例如，如果一个上拉菜单已经显示，后退按钮应该关闭上拉菜单，而不是返回一个页面视图或关闭一个打开的模型。


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| callback | function | 当点击返回按钮时触发，如果该监视器具有最高的优先级。 |
| priority | number | 仅最高优先级的会执行。 |
| actionId (可选) | * | 该id指定这个动作。默认：一个随机且唯一的id。 |


**返回值:** 函数， 一个被触发的函数，将会注销 backButtonAction。


```
ready([callback])
```


设备准备就绪，则触发一个回调函数。


| 参数 | 类型 | 详情 |
| --- | --- | --- |
| callback (可选) | function= | 触发的函数。 |


返回: promise对象, 对象被构造 成功后得到解析。








	  AI 思考中...





			** [ionic 导航](https://www.runoob.com/ionic-ion-nav-view.html)
			[ionic 浮动框](https://www.runoob.com/ionic-ionicpopover.html) **













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
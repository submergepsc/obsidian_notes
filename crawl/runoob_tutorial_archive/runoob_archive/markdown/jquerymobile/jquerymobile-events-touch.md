# jQuery Mobile 触摸事件

- Source: https://www.runoob.com/jquerymobile/jquerymobile-events-touch.html

---


触摸事件在用户触摸屏幕（页面）时触发。

*

|  | 触摸事件同样可应用与桌面电脑上：点击或者滑动鼠标！ |
| --- | --- |

**
---


## jQuery Mobile 点击


点击事件在用户点击元素时触发。


如下实例：当点击  元素时，隐藏当前的  元素：


## 实例


```javascript
$("p").on("tap",function(){  $(this).hide();});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_tap)


---


## jQuery Mobile 点击不放（长按）


点击不放（长按） 事件在点击并不放（大约一秒）后触发


## 实例


```javascript
$("p").on("taphold",function(){  $(this).hide();});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_taphold)


---


## jQuery Mobile 滑动


滑动事件是在用户一秒内水平拖拽大于30PX，或者纵向拖曳小于20px的事件发生时触发的事件：


## 实例


```javascript
$("p").on("swipe",function(){  $("span").text("滑动检测!");});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_swipe)


---


## jQuery Mobile 向左滑动


向左滑动事件在用户向左拖动元素大于30px时触发：


## 实例


```javascript
$("p").on("swipeleft",function(){  alert("向左滑动!");});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_swipeleft)


---


## jQuery Mobile 向右滑动


向右滑动事件在用户向右拖动元素大于30px时触发：


## 实例


```javascript
$("p").on("swiperight",function(){  alert("向右滑动!");});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_swiperight)








	  AI 思考中...





			* [jQuery Mobile 事件](https://www.runoob.com/jquerymobile-events.html)
			[jQuery Mobile 表单](https://www.runoob.com/jquerymobile-form-basic.html) **













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
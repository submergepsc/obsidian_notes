# jQuery Mobile 方向改变事件

- Source: https://www.runoob.com/jquerymobile/jquerymobile-events-orientation.html

---


## jQuery Mobile 方向改变（orientationchange）事件


当用户垂直或水平旋转移动设备时，触发方向改变（orientationchange）事件。


**水平旋转
垂直旋转


![Mobile](https://www.runoob.com/wp-content/uploads/2013/10/iphone5.png)


如需使用方向改变（orientationchange）事件，请附加它到 window 对象：


```
$(window).on("orientationchange",function(){
    alert("方向有改变!");
});
```


回调函数可有一个参数，event 对象，返回移动设备的方向："纵向"（设备保持在垂直位置）或"横向"（设备保持在水平位置）：


## 实例


```javascript
$(window).on("orientationchange",function(event){
	alert("方向是: " + event.orientation);});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_orientationchange)


由于方向改变（orientationchange）事件绑定到 window 对象，我们可以使用 window.orientation 属性来设置不同的样式，以便区分纵向和横向的视图：


## 实例


```javascript
$(window).on("orientationchange",function(){  if(window.orientation
	== 0) // Portrait  {    $("p").css({"background-color":"yellow","font-size":"300%"});
	}  else // Landscape  {    $("p").css({"background-color":"pink","font-size":"200%"});
	}});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_orientationchange2)


|  | window.orientation 属性针对纵向视图返回 0，针对横向视图返回 90 或 -90。 |
| --- | --- |










	  AI 思考中...





			** [jQuery Mobile 滚屏事件](https://www.runoob.com/jquerymobile-events-scroll.html)
			[jQuery Mobile 实例](https://www.runoob.com/jquerymobile-examples.html) **













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
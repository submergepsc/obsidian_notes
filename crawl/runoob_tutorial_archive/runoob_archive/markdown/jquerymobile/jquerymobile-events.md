# jQuery Mobile 事件

- Source: https://www.runoob.com/jquerymobile/jquerymobile-events.html

---


事件 = 所有不同访问者访问页面的响应动作。


---


## jQuery Mobile 事件


在jQuery Mobile你可以使用任何标准的 [jQuery 事件](https://www.runoob.com/../jquery/jquery-ref-events.html) 。


除此之外, jQuery Mobile 也提供了针对移动端浏览器的事件：


- 触摸事件 - 当用户触摸屏幕时触发
- 滑动事件 - 当用户上下滑动时触发
- 定位事件 - 当设备水平或垂直翻转时触发
- 页面事件 - 当页面显示，隐藏，创建，加载或未加载时触发


---


## 初始化 jQuery Mobile 事件


在学习jQuery时我们学到了用$(document).ready()来使你的jQuery代码脚本在DOM元素加载完成后才开始执行：


## jQuery document ready 事件


```javascript
<script>$(document).ready(function(){   // 编写jQuery方法...
});</script>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_document_ready)


但是，在 jQuery Mobile 中, 使用pageinit 事件来设置代码脚本在DOM元素加载完成后开始执行，所以要在任何新页面加载并创建是执行脚本，就需要绑定pageinit事件。


第二个参数 ("*#pageone*")为指定事件的页面id：


## jQuery Mobile pagecreate 事件


```javascript
<script>$(document).on("pagecreate","#pageone",function(){   // jQuery 事件...});</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_pageinit)


|  | 注意： jQuery on() 方法用于绑定事件到选中的元素上。 |
| --- | --- |


下一章节我们将更详细介绍 jQuery Mobile 事件。








	  AI 思考中...





			** [jQuery Mobile 主题](https://www.runoob.com/jquerymobile-themes.html)
			[jQuery Mobile 触摸事件](https://www.runoob.com/jquerymobile-events-touch.html) **













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
# jQuery Mobile 滚屏事件

- Source: https://www.runoob.com/jquerymobile/jquerymobile-events-scroll.html

---


jQuery Mobile 提供了两种滚屏事件：滚屏开始时触发和滚动结束时触发。


---


## jQuery Mobile 滚屏开始（Scrollstart）


scrollstart 事件是在用户开始滚动页面时触发：


## 实例


```javascript
$(document).on("scrollstart",function(){  alert("开始滚动!");});
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_scrollstart)


|  | 注意：iOS 设备在滚屏时锁定 DOM 操作，这意味着当用户滚屏时不可能改变任何东西。然而，jQuery 团队正在为此寻找解决方案。 |
| --- | --- |


---


## jQuery Mobile 滚屏结束（Scrollstop）


scrollstop 事件是在用户停止滚动页面时触发：


## 实例


```javascript
$(document).on("scrollstop",function(){  alert("停止滚动!");});
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_events_scrollstop)










	  AI 思考中...





			** [jQuery Mobile 表单滑动条](https://www.runoob.com/jquerymobile-form-sliders.html)
			[jQuery Mobile 方向改变事件](https://www.runoob.com/jquerymobile-events-orientation.html) **













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
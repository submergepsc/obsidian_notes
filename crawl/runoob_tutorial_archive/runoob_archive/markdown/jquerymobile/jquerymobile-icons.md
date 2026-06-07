# jQuery Mobile 按钮图标

- Source: https://www.runoob.com/jquerymobile/jquerymobile-icons.html

---


jQuery Mobile 提供了一套让按钮看起来更称心如意的图标。


---

**
*


---


## 添加图标到 jQuery Mobile 按钮


我们可以使用 ui-icon 类将图标添加到按钮上，并可以使用指定类来设置按钮位置。


```
<a href="#anylink" class="ui-btn ui-icon-search ui-btn-icon-left">Search</a>
```


注意：** 在其他方式的按钮上，如列表或表单中的按钮需要使用 data-icon 属性。在接下来的章节中我们会具体介绍。


下面我们列出一些 jQuery Mobile 提供的可用图标：


| 按钮类 | 描述 | 按钮 | 实例 |
| --- | --- | --- | --- |
| ui-icon-arrow-l | 左箭头 |  | 尝试一下 |
| ui-icon-arrow-r | 右箭头 |  | 尝试一下 |
| ui-icon-info | 信息 |  | 尝试一下 |
| ui-icon-delete | 删除 |  | 尝试一下 |
| ui-icon-back | 后退 |  | 尝试一下 |
| ui-icon-audio | 扬声器 |  | 尝试一下 |
| ui-icon-lock | 挂锁 |  | 尝试一下 |
| ui-icon-search | 搜索 |  | 尝试一下 |
| ui-icon-alert | 警告 |  | 尝试一下 |
| ui-icon-grid | 网格 |  | 尝试一下 |
| ui-icon-home | 主页 |  | 尝试一下 |


如需查看所有 jQuery Mobile 按钮图标的完整参考手册，请访问我们的 [jQuery Mobile 图标参考手册](https://www.runoob.com/jquerymobile-ref-icons.html)。


---


## 定位图标


您也可以规定图标定位在按钮的什么部位：顶部（top）、右侧（right）、底部（bottom）、左侧（left）。


请使用 ui-btn-icon 属性来指定位置：


## 图标的位置：


```javascript
<a href="#anylink" class="ui-btn ui-icon-search ui-btn-icon-top">顶部</a><a href="#anylink"
  class="ui-btn ui-icon-search ui-btn-icon-right">右侧</a><a href="#anylink"
  class="ui-btn ui-icon-search ui-btn-icon-bottom">底部</a><a href="#anylink"
  class="ui-btn ui-icon-search ui-btn-icon-left">左侧</a>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_icon_positions)


|  | 如果你未指定按钮图片的位置，图标将不显示。 |
| --- | --- |


---


## 只显示图标


如果你只想显示图标，可以使用 "notext":


## 实例：


```javascript
<a href="#anylink" class="ui-btn ui-icon-search
  ui-btn-icon-notext">搜索</a>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjqmob_icon_notext)

---


## 移除圆圈


默认情况下，所有的图标都有一个灰色的圆圈。如果你不需要它，可以在元素中使用 "ui-nodisc-icon" 类：


## 实例


```javascript
<a href="#anylink" class="ui-btn ui-icon-search
  ui-btn-icon-left">使用圆圈 (默认)</a><a href="#anylink" class="ui-btn ui-icon-search
  ui-btn-icon-left ui-nodisc-icon">去掉圆圈</a>
```


  [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjqmob_icon_disc)

---


## 黑色、白色按钮


默认情况下，所有图标都是白色的。 如果需要改变图标颜色为黑色，可以在元素添加 "ui-alt-icon"：


## 实例


```javascript
<a href="#anylink" class="ui-btn ui-icon-search
  ui-btn-icon-left">白色</a><a href="#anylink" class="ui-btn ui-icon-search
  ui-btn-icon-left ui-alt-icon">黑色</a>
```


  [尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjqmob_icon_alt)

---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 更多实例


[向容器添加 "ui-nodisc-icon" 类](https://www.runoob.com/try/tryit.php?filename=tryjqmob_icon_disc2) 使用 "ui-nodisc-icon" 类的实例。


[向容器添加 "ui-alt-icon" 类](https://www.runoob.com/try/tryit.php?filename=tryjqmob_icon_alt2) 使用 "ui-alt-icon" 类的实例。








	  AI 思考中...





			* [jQuery Mobile 按钮](https://www.runoob.com/jquerymobile-buttons.html)
			[jQuery Mobile 工具栏](https://www.runoob.com/jquerymobile-toolbars.html) **













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
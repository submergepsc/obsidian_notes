# Bootstrap 警告（Alerts）

- Source: https://www.runoob.com/bootstrap/bootstrap-alerts.html

本章将讲解警告（Alerts）以及 Bootstrap 所提供的用于警告的 class。警告（Alerts）向用户提供了一种定义消息样式的方式。它们为典型的用户操作提供了上下文信息反馈。


您可以为警告框添加一个可选的关闭按钮。为了创建一个内联的可取消的警告框，请使用 [警告（Alerts） jQuery 插件](https://www.runoob.com/bootstrap-alert-plugin.html)。


您可以通过创建一个 ，并向其添加一个 **.alert** class 和四个上下文 class（即** .alert-success、.alert-info、.alert-warning、.alert-danger**）之一，来添加一个基本的警告框。下面的实例演示了这点：


## 实例


```css
<div class="alert alert-success">成功！很好地完成了提交。</div>
<div class="alert alert-info">信息！请注意这个信息。</div>
<div class="alert alert-warning">警告！请不要提交。</div>
<div class="alert alert-danger">错误！请进行一些更改。</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-alert)


结果如下所示：


![警告（Alerts）](https://www.runoob.com/wp-content/uploads/2014/06/alert_demo.jpg)


## 可取消的警告（Dismissal Alerts）


创建一个可取消的警告（Dismissal Alert）步骤如下：


- 通过创建一个 ，并向其添加一个 **.alert** class 和四个上下文 class（即** .alert-success、.alert-info、.alert-warning、.alert-danger**）之一，来添加一个基本的警告框。
- 同时向上面的  class 添加可选的 **.alert-dismissable**。
- 添加一个关闭按钮。


下面的实例演示了这点：


## 实例



```css
<div class="alert alert-success alert-dismissable">
            <button type="button" class="close" data-dismiss="alert"
                    aria-hidden="true">
                &times;
            </button>
            成功！很好地完成了提交。
        </div>
        <div class="alert alert-info alert-dismissable">
            <button type="button" class="close" data-dismiss="alert"
                    aria-hidden="true">
                &times;
            </button>
            信息！请注意这个信息。
        </div>
        <div class="alert alert-warning alert-dismissable">
            <button type="button" class="close" data-dismiss="alert"
                    aria-hidden="true">
                &times;
            </button>
            警告！请不要提交。
        </div>
        <div class="alert alert-danger alert-dismissable">
            <button type="button" class="close" data-dismiss="alert"
                    aria-hidden="true">
                &times;
            </button>
            错误！请进行一些更改。
        </div>
```





> ![](https://www.runoob.com/images/quote.png)请确保使用带有 *data-dismiss="alert"* data 属性的  元素。

	[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-alert-dismissal)


结果如下所示：


![可取消的警告（Dismissal Alerts）](https://www.runoob.com/wp-content/uploads/2014/06/dismissalalert_demo.jpg)


## 警告（Alerts）中的链接


在警告（Alerts）中创建链接的步骤如下：


- 通过创建一个 ，并向其添加一个 **.alert** class 和四个上下文 class（即** .alert-success、.alert-info、.alert-warning、.alert-danger**）之一，来添加一个基本的警告框。
- 使用 **.alert-link** 实体类来快速提供带有匹配颜色的链接。


## 实例


```css
<div class="alert alert-success">
    <a href="#" class="alert-link">成功！很好地完成了提交。</a>
</div>
<div class="alert alert-info">
    <a href="#" class="alert-link">信息！请注意这个信息。</a>
</div>
<div class="alert alert-warning">
    <a href="#" class="alert-link">警告！请不要提交。</a>
</div>
<div class="alert alert-danger">
    <a href="#" class="alert-link">错误！请进行一些更改。</a>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-alert-links)


结果如下所示：


![警告（Alerts）中的链接](https://www.runoob.com/wp-content/uploads/2014/06/linksinalert_demo.jpg)








	  AI 思考中...





			** [Bootstrap 缩略图](https://www.runoob.com/bootstrap-thumbnails.html)
			[Bootstrap 进度条](https://www.runoob.com/bootstrap-progress-bars.html) **













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
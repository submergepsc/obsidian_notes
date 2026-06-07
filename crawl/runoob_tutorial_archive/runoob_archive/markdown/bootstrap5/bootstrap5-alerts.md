# Bootstrap5 信息提示框

- Source: https://www.runoob.com/bootstrap5/bootstrap5-alerts.html

Bootstrap 5 可以很容易实现信息提示框。


![](https://www.runoob.com/wp-content/uploads/2017/10/06CC7655-91D9-4953-A8CC-33F50A21404E.jpg)


提示框可以使用 **.alert** 类, 后面加上 **.alert-success**, **.alert-info**, **.alert-warning**, **.alert-danger**, **.alert-primary**, **.alert-secondary**, **.alert-light** 或 **.alert-dark** 类来实现:


## 实例


```css
<div class="alert alert-success">
  <strong>成功!</strong> 指定操作成功提示信息。
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_alerts)


---


## 提示框添加链接


提示框中在链接的标签上添加 **alert-link** 类来设置匹配提示框颜色的链接：


## 实例


```css
<div class="alert alert-success">
  <strong>成功!</strong> 你应该认真阅读 <a href="#" class="alert-link">这条信息</a>。
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_alerts_link)

---


## 关闭提示框


我们可以在提示框中的 div 中添加 **.alert-dismissible** 类，然后在关闭按钮的链接上添加 **class="btn-close"** 和 **data-bs-dismiss="alert"** 类来设置提示框的关闭操作。


## 实例


```css
<div class="alert alert-success alert-dismissible">
  <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
  <strong>成功!</strong> 指定操作成功提示信息。
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_alerts_dismissible)


---


## 提示框动画


**.fade** 和 **.show** 类用于设置提示框在关闭时的淡出和淡入效果：


## 实例


```css
<div class="alert alert-danger alert-dismissible fade show">
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs5_alerts_fade)








	  AI 思考中...





			** [Bootstrap5 Jumbotron](https://www.runoob.com/bootstrap5-jumbotron.html)
			[Bootstrap5 按钮](https://www.runoob.com/bootstrap5-buttons.html) **













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
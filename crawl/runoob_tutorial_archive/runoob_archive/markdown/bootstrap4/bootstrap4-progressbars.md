# Bootstrap4 进度条

- Source: https://www.runoob.com/bootstrap4/bootstrap4-progressbars.html

![](https://www.runoob.com/wp-content/uploads/2017/10/2495A384-5619-40B2-8E29-FD5152CE01A9.jpg)


进度条可以显示用户任务的完成过程。


创建一个基本的进度条的步骤如下：


- 添加一个带有 **.progress** 类的 。
- 接着，在上面的  内，添加一个带有 class **.progress-bar** 的空的 。
- 添加一个带有百分比表示的宽度的 style 属性，例如** style="width:70%"** 表示进度条在 **70%** 的位置。


## 实例


```css
<div class="progress">
  <div class="progress-bar" style="width:70%"></div>
</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_progressbar1)


---


## 进度条高度


进度条高度默认为 16px。我们可以使用 CSS 的 `height` 属性来修改他：


## 实例


```css
<div class="progress" style="height:20px;">
  <div class="progress-bar" style="width:40%;"></div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_progressbar7)


---


## 进度条标签


可以在进度条内添加文本，如进度的百分比：


## 实例


```css
<div class="progress">
  <div class="progress-bar" style="width:70%">70%</div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_progressbar2)

---


## 不同颜色的进度条


默认情况下进度条为蓝色，Bootstrap4 还提供了以下颜色的进度条：


![](https://www.runoob.com/wp-content/uploads/2017/10/81DD86EA-1D06-4EE1-9A48-17D2F91FDF03.jpg)


## 实例


```css
<div class="progress">
  <div class="progress-bar bg-success" style="width:40%"></div>
</div>

<div class="progress">
  <div class="progress-bar bg-info" style="width:50%"></div>
</div>

<div class="progress">
  <div class="progress-bar bg-warning" style="width:60%"></div>
</div>

<div class="progress">
  <div class="progress-bar bg-danger" style="width:70%"></div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_progressbar3)

---


## 条纹的进度条


可以使用 `.progress-bar-striped` 类来设置条纹进度条：


## 实例


```css
<div class="progress">
  <div class="progress-bar progress-bar-striped" style="width:40%"></div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_progressbar4)


---


## 动画进度条


使用 `.progress-bar-animated` 类可以为进度条添加动画：


## 实例


```css
<div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 40%"></div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_progressbar5)


---


## 混合色彩进度条


进度条可以设置多种颜色：


## 实例


```css
<div class="progress">
  <div class="progress-bar bg-success" style="width:40%">
    Free Space
  </div>
  <div class="progress-bar bg-warning" style="width:10%">
    Warning
  </div>
  <div class="progress-bar bg-danger" style="width:20%">
    Danger
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_progressbar6)








	  AI 思考中...





			** [Bootstrap4 徽章（Badges）](https://www.runoob.com/bootstrap4-badges.html)
			[Bootstrap4 分页](https://www.runoob.com/bootstrap4-pagination.html) **













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
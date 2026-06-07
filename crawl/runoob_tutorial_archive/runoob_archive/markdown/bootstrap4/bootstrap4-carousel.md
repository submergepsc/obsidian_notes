# Bootstrap4 轮播

- Source: https://www.runoob.com/bootstrap4/bootstrap4-carousel.html

轮播是一个循环的幻灯片：

*

---


## 如何创建轮播


以下实例创建了一个简单的图片轮播效果 ：


## 实例


```css
<div id="demo" class="carousel slide" data-ride="carousel">

  <!-- 指示符 -->
  <ul class="carousel-indicators">
    <li data-target="#demo" data-slide-to="0" class="active"></li>
    <li data-target="#demo" data-slide-to="1"></li>
    <li data-target="#demo" data-slide-to="2"></li>
  </ul>

  <!-- 轮播图片 -->
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://static.jyshare.com/images/mix/img_fjords_wide.jpg">
    </div>
    <div class="carousel-item">
      <img src="https://static.jyshare.com/images/mix/img_nature_wide.jpg">
    </div>
    <div class="carousel-item">
      <img src="https://static.jyshare.com/images/mix/img_mountains_wide.jpg">
    </div>
  </div>

  <!-- 左右切换按钮 -->
  <a class="carousel-control-prev" href="#demo" data-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </a>
  <a class="carousel-control-next" href="#demo" data-slide="next">
    <span class="carousel-control-next-icon"></span>
  </a>

</div>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_carousel)

---


## 轮播图片上添加描述


在每个 **** 内添加 **** 来设置轮播图片的描述文本：:


## 实例


```css
<div class="carousel-item">
  <img src="https://static.jyshare.com/images/mix/img_fjords_wide.jpg">
  <div class="carousel-caption">
    <h3>第一张图片描述标题</h3>
    <p>描述文字!</p>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trybs4_carousel2)

### 以上实例中使用的类说明


| 类 | 描述 |
| --- | --- |
| .carousel | 创建一个轮播 |
| .carousel-indicators | 为轮播添加一个指示符，就是轮播图底下的一个个小点，轮播的过程可以显示目前是第几张图。 |
| .carousel-inner | 添加要切换的图片 |
| .carousel-item | 指定每个图片的内容 |
| .carousel-control-prev | 添加左侧的按钮，点击会返回上一张。 |
| .carousel-control-next | 添加右侧按钮，点击会切换到下一张。 |
| .carousel-control-prev-icon | 与 .carousel-control-prev 一起使用，设置左侧的按钮 |
| .carousel-control-next-icon | 与 .carousel-control-next 一起使用，设置右侧的按钮 |
| .slide | 切换图片的过渡和动画效果，如果你不需要这样的效果，可以删除这个类。 |








	  AI 思考中...





			* [Bootstrap4 表单控件](https://www.runoob.com/bootstrap4-forms-inputs.html)
			[Bootstrap4 模态框](https://www.runoob.com/bootstrap4-modal.html) **













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
# Bootstrap4 多媒体对象

- Source: https://www.runoob.com/bootstrap4/bootstrap4-media-objects.html

Bootstrap 提供了很好的方式来处理多媒体对象（图片或视频）和内容的布局。应用场景有博客评论、微博等:


## 基础多媒体对象


要创建一个多媒体对象，可以在容器元素上添加 .media 类，然后将多媒体内容放到子容器上，子容器需要添加 .media-body 类，然后添加外边距，内边距等效果:


## 实例


```css
<div class="media border p-3">
  <img src="mobile-icon.png" alt="John Doe" class="mr-3 mt-3 rounded-circle" style="width:60px;">
  <div class="media-body">
    <h4>菜鸟教程</h4>
    <p>学的不仅是技术，更是梦想！！！</p>
  </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_media)


---


## 多媒体对象嵌套


多媒体对象可以多个嵌套（一个多媒体对象中包含另外一个多媒体对象）


要嵌套多媒体对象，可以把新的 **.media** 容器放到 **.media-body** 容器中:


## 实例


```css
<div class="media border p-3">
  <img src="mobile-icon.png" alt="John Doe" class="mr-3 mt-3 rounded-circle" style="width:60px;">
  <div class="media-body">
    <h4>菜鸟教程</h4>
    <p>学的不仅是技术，更是梦想！！！</p>
    <div class="media p-3">
      <img src="mobile-icon.png" alt="Jane Doe" class="mr-3 mt-3 rounded-circle" style="width:45px;">
      <div class="media-body">
        <h4>菜鸟教程</h4>
        <p>学的不仅是技术，更是梦想！！！</p>
      </div>
    </div>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_media_nested)


---

## 多媒体对象图片显示在右边


如果你想将头像图片显示在右侧，可以在 **.media-body** 容器后添加图片:


## 实例


```css
<div class="media border p-3">
  <div class="media-body">
    <h4>菜鸟教程</h4>
    <p>学的不仅是技术，更是梦想！！！</p>
  </div>
  <img src="mobile-icon.png" alt="John Doe" class="ml-3 mt-3 rounded-circle" style="width:60px;">
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_media_right)


---


## 定位多媒体图片位置


我们可以使用 align-self-* 相关类来设置多媒体对象的图片显示位置：


## 实例


```css
<!-- 头部 -->
<div class="media">
  <img src="https://static.jyshare.com/images/mobile-icon.png" class="align-self-start mr-3" style="width:60px">
  <div class="media-body">
    <h4>头部 -- 菜鸟教程</h4>
    <p>学的不仅是技术，更是梦想！！！</p>
  </div>
</div>

<!-- 居中 -->
<div class="media">
  <img src="https://static.jyshare.com/images/mobile-icon.png" class="align-self-center mr-3" style="width:60px">
  <div class="media-body">
    <h4>居中 -- 菜鸟教程</h4>
    <p>学的不仅是技术，更是梦想！！！</p>
  </div>
</div>

<!-- 底部 -->
<div class="media">
  <img src="https://static.jyshare.com/images/mobile-icon.png" class="align-self-end mr-3" style="width:60px">
  <div class="media-body">
    <h4>底部 -- 菜鸟教程</h4>
    <p>学的不仅是技术，更是梦想！！！</p>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=trybs4_media_alignment)








	  AI 思考中...





			** [Bootstrap4 Flex（弹性）布局](https://www.runoob.com/bootstrap4-flex.html)
			[Bootstrap4 创建一个网页](https://www.runoob.com/bootstrap4-makeawebsite.html) **













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
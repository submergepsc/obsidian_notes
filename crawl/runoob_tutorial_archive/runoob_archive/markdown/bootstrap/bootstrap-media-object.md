# Bootstrap 多媒体对象（Media Object）

- Source: https://www.runoob.com/bootstrap/bootstrap-media-object.html

本章我们将讲解 Bootstrap 中的多媒体对象（Media Object），如：图像、视频、音频等。 多媒体对象的样式可用于创建各种类型的组件（比如：博客评论），我们可以在组件中使用图文混排，图像可以左对齐或者右对齐。媒体对象可以用更少的代码来实现媒体对象与文字的混排。


接下来我们先来看个实例：


## 实例


```css
<!-- 左对齐 -->
<div class="media">
  <div class="media-left">
    <img src="img_avatar1.png" class="media-object" style="width:60px">
  </div>
  <div class="media-body">
    <h4 class="media-heading">左对齐</h4>
    <p>这是一些示例文本...</p>
  </div>
</div>

<!-- 右对齐 -->
<div class="media">
  <div class="media-body">
    <h4 class="media-heading">左对齐</h4>
    <p>这是一些示例文本...</p>
  </div>
  <div class="media-right">
    <img src="img_avatar1.png" class="media-object" style="width:60px">
  </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-mediaobject)


结果如下所示：


![默认的媒体对象](https://www.runoob.com/wp-content/uploads/2014/06/CF5C7B48-F569-49D9-A712-E5425DA5630D.png)


### 实例解析


在  元素上添加 `.media` 类来创建一个多媒体对象。


使用 `.media-left` 类让多媒体对象(图片)来实现左对齐，同样 `.media-right` 类实现了右对齐。


文本内容放在 class="`media-body`" 的 div 中，图片左对齐则放在 class="`media-body`" 之前，图片右对齐则放在 class="`media-body`" 之后。


此外，你还可以使用 `.media-heading` 类来设置标题。


让我们来看看下面这个有关媒体对象列表 .media-list 的实例：


### 顶部、底部、居中对齐


## 实例


```css
<!-- 置顶 -->
<div class="media">
  <div class="media-left media-top">
    <img src="img_avatar1.png" class="media-object" style="width:60px">
  </div>
  <div class="media-body">
    <h4 class="media-heading">置顶</h4>
    <p>这是一些示例文本...</p>
  </div>
</div>

<!-- 居中对齐 -->
<div class="media">
  <div class="media-left media-middle">
    <img src="img_avatar1.png" class="media-object" style="width:60px">
  </div>
  <div class="media-body">
    <h4 class="media-heading">居中</h4>
    <p>这是一些示例文本...</p>
  </div>
</div>

<!-- 置底 -->
<div class="media">
  <div class="media-left media-bottom">
    <img src="img_avatar1.png" class="media-object" style="width:60px">
  </div>
  <div class="media-body">
    <h4 class="media-heading">置底</h4>
    <p>这是一些示例文本...</p>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-mediaobject-list)


结果如下所示：


![媒体对象列表](https://www.runoob.com/wp-content/uploads/2014/06/8F2C99DE-BFC0-411F-ADD8-23F64EDDD0B3.png)


### 内嵌多媒体对象


一个多媒体对象内还可以包含多个多媒体对象：


## 实例


```css
<div class="media">
  <div class="media-left">
    <img src="https://static.jyshare.com/images/mix/img_avatar.png" class="media-object" style="width:45px">
  </div>
  <div class="media-body">
    <h4 class="media-heading">RUNOOB-1 <small><i>Posted on February 19, 2016</i></small></h4>
    <p>这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。</p>

    <!-- 内嵌多媒体对象 -->
    <div class="media">
      <div class="media-left">
        <img src="https://static.jyshare.com/images/mix/img_avatar.png" class="media-object" style="width:45px">
      </div>
      <div class="media-body">
        <h4 class="media-heading">RUNOOB-2 <small><i>Posted on February 19, 2016</i></small></h4>
        <p>这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。</p>

        <!-- 内嵌多媒体对象 -->
        <div class="media">
          <div class="media-left">
            <img src="https://static.jyshare.com/images/mix/img_avatar.png" class="media-object" style="width:45px">
          </div>
          <div class="media-body">
            <h4 class="media-heading">RUNOOB-3 <small><i>Posted on February 19, 2016</i></small></h4>
            <p>这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。</p>
          </div>
        </div>

      </div>
    </div>

  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-mediaobject-list2)


## 实例


```css
<div class="media">
  <div class="media-left">
    <img src="https://static.jyshare.com/images/mix/img_avatar.png" class="media-object" style="width:45px">
  </div>
  <div class="media-body">
    <h4 class="media-heading">RUNOOB-1 <small><i>Posted on February 19, 2016</i></small></h4>
    <p>这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。</p>

    <!-- 内嵌多媒体对象 -->
    <div class="media">
      <div class="media-left">
        <img src="https://static.jyshare.com/images/mix/img_avatar.png" class="media-object" style="width:45px">
      </div>
      <div class="media-body">
        <h4 class="media-heading">RUNOOB-2 <small><i>Posted on February 20, 2016</i></small></h4>
        <p>这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。</p>

        <!-- 内嵌多媒体对象 -->
        <div class="media">
          <div class="media-left">
            <img src="https://static.jyshare.com/images/mix/img_avatar.png" class="media-object" style="width:45px">
          </div>
          <div class="media-body">
            <h4 class="media-heading">RUNOOB-3 <small><i>Posted on February 21, 2016</i></small></h4>
            <p>这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。</p>
          </div>
        </div>

      </div>

      <!-- 内嵌多媒体对象 -->
      <div class="media">
        <div class="media-left">
          <img src="https://static.jyshare.com/images/mix/img_avatar.png" class="media-object" style="width:45px">
        </div>
        <div class="media-body">
          <h4 class="media-heading">RUNOOB-4 <small><i>Posted on February 20, 2016</i></small></h4>
          <p>这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。</p>
        </div>
      </div>

    </div>
  </div>

  <!-- 内嵌多媒体对象 -->
  <div class="media">
    <div class="media-left">
      <img src="https://static.jyshare.com/images/mix/img_avatar.png" class="media-object" style="width:45px">
    </div>
    <div class="media-body">
      <h4 class="media-heading">RUNOOB-5 <small><i>Posted on February 19, 2016</i></small></h4>
      <p>这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。这是一些示例文本。</p>
    </div>
  </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=bootstrap3-mediaobject-list3)









	  AI 思考中...





			** [Bootstrap 进度条](https://www.runoob.com/bootstrap-progress-bars.html)
			[Bootstrap 列表组](https://www.runoob.com/bootstrap-list-group.html) **













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
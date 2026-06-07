# Bootstrap 缩略图

- Source: https://www.runoob.com/bootstrap/bootstrap-thumbnails.html

本章将讲解 Bootstrap 缩略图。大多数站点都需要在网格中布局图像、视频、文本等。Bootstrap 通过缩略图为此提供了一种简便的方式。使用 Bootstrap 创建缩略图的步骤如下：


- 在图像周围添加带有 class **.thumbnail** 的  标签。
- 这会添加四个像素的内边距（padding）和一个灰色的边框。
- 当鼠标悬停在图像上时，会动画显示出图像的轮廓。


下面的实例演示了默认的缩略图：


## 实例


```css
<div class="row">
    <div class="col-sm-6 col-md-3">
        <a href="#" class="thumbnail">
            <img src="/wp-content/uploads/2014/06/kittens.jpg"
                 alt="通用的占位符缩略图">
        </a>
    </div>
    <div class="col-sm-6 col-md-3">
        <a href="#" class="thumbnail">
            <img src="/wp-content/uploads/2014/06/kittens.jpg"
                 alt="通用的占位符缩略图">
        </a>
    </div>
    <div class="col-sm-6 col-md-3">
        <a href="#" class="thumbnail">
            <img src="/wp-content/uploads/2014/06/kittens.jpg"
                 alt="通用的占位符缩略图">
        </a>
    </div>
    <div class="col-sm-6 col-md-3">
        <a href="#" class="thumbnail">
            <img src="/wp-content/uploads/2014/06/kittens.jpg"
                 alt="通用的占位符缩略图">
        </a>
    </div>
</div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-thumbnail)


结果如下所示：


![缩略图](https://www.runoob.com/wp-content/uploads/2014/06/thumbnail_demo.jpg)


## 添加自定义的内容


现在我们有了一个基本的缩略图，我们可以向缩略图添加各种 HTML 内容，比如标题、段落或按钮。具体步骤如下：


- 把带有 class **.thumbnail** 的  标签改为 。
- 在该  内，您可以添加任何您想要添加的东西。由于这是一个 ，我们可以使用默认的基于 span 的命名规则来调整大小。
- 如果您想要给多个图像进行分组，请把它们放置在一个无序列表中，且每个列表项向左浮动。


下面的实例演示了这点：


## 实例


```css
<div class="row">
    <div class="col-sm-6 col-md-3">
         <div class="thumbnail">
            <img src="/wp-content/uploads/2014/06/kittens.jpg"
             alt="通用的占位符缩略图">
            <div class="caption">
                <h3>缩略图标签</h3>
                <p>一些示例文本。一些示例文本。</p>
                <p>
                    <a href="#" class="btn btn-primary" role="button">
                        按钮
                    </a>
                    <a href="#" class="btn btn-default" role="button">
                        按钮
                    </a>
                </p>
            </div>
         </div>
    </div>
    <div class="col-sm-6 col-md-3">
        <div class="thumbnail">
            <img src="/wp-content/uploads/2014/06/kittens.jpg"
            alt="通用的占位符缩略图">
            <div class="caption">
                <h3>缩略图标签</h3>
                <p>一些示例文本。一些示例文本。</p>
                <p>
                    <a href="#" class="btn btn-primary" role="button">
                        按钮
                    </a>
                    <a href="#" class="btn btn-default" role="button">
                        按钮
                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-md-3">
        <div class="thumbnail">
            <img src="/wp-content/uploads/2014/06/kittens.jpg"
            alt="通用的占位符缩略图">
            <div class="caption">
                <h3>缩略图标签</h3>
                <p>一些示例文本。一些示例文本。</p>
                <p>
                    <a href="#" class="btn btn-primary" role="button">
                        按钮
                    </a>
                    <a href="#" class="btn btn-default" role="button">
                        按钮
                    </a>
                </p>
            </div>
        </div>
    </div>
    <div class="col-sm-6 col-md-3">
        <div class="thumbnail">
            <img src="/wp-content/uploads/2014/06/kittens.jpg"
            alt="通用的占位符缩略图">
            <div class="caption">
                <h3>缩略图标签</h3>
                <p>一些示例文本。一些示例文本。</p>
                <p>
                    <a href="#" class="btn btn-primary" role="button">
                        按钮
                    </a>
                    <a href="#" class="btn btn-default" role="button">
                        按钮
                    </a>
                </p>
            </div>
        </div>
    </div>
</div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=bootstrap3-thumbnail-custom)


结果如下所示：


![自定义缩略图](https://www.runoob.com/wp-content/uploads/2014/06/bs-thumbnails.jpg)








	  AI 思考中...





			** [Bootstrap 页面标题](https://www.runoob.com/bootstrap-page-header.html)
			[Bootstrap 警告](https://www.runoob.com/bootstrap-alerts.html) **













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
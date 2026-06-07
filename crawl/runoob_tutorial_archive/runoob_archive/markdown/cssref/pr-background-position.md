# CSS background-position 属性

- Source: https://www.runoob.com/cssref/pr-background-position.html

**
## 实例


如何定位 background-image：


```css
body {
    background-image:url('smiley.gif');
    background-repeat:no-repeat;
    background-attachment:fixed;
    background-position:center;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_background-position)


---


## 标签定义及使用说明


background-position 属性设置背景图像的起始位置。


注意**对于这个工作在Firefox和Opera，background-attachment必须设置为 "fixed（固定）".


| 默认值: | 0% 0% |
| --- | --- |
| 继承: | no |
| 版本: | CSS1 |
| JavaScript 语法: | object object.style.backgroundPosition="center" |

**
---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| background-position | 1.0 | 4.0 | 1.0 | 1.0 | 3.5 |


注意:** IE8 及更早的浏览器版本不支持一个元素有多个背景图片。


---


## 属性值


| 值 | 描述 |
| --- | --- |
| left top left center left bottom right top right center right bottom center top center center center bottom | 如果仅指定一个关键字，其他值将会是"center" |
| x% y% | 第一个值是水平位置，第二个值是垂直。左上角是0％0％。右下角是100％100％。如果仅指定了一个值，其他值将是50％。 。默认值为：0％0％ |
| xpos ypos | 第一个值是水平位置，第二个值是垂直。左上角是0。单位可以是像素（0px0px）或任何其他 CSS单位。如果仅指定了一个值，其他值将是50％。你可以混合使用％和positions |
| inherit | 指定background-position属性设置应该从父元素继承 |

**
---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 在线实例


[如何设置页面背景图像](https://www.runoob.com/try/try.php?filename=trycss_background-position) 这个例子演示了如何在页面上设置background-image。


[如何使用％来定位背景图像](https://www.runoob.com/try/try.php?filename=trycss_background-position_percent) 这个例子演示了如何使用％设置页面上的图像位置。


[如何使用像素来定位背景图像](https://www.runoob.com/try/try.php?filename=trycss_background-position_pixel) 这个例子演示了如何使用像素设置页面上的图像位置。


---


## 相关文章


CSS 教程: [CSS Background](https://www.runoob.com/../css/css-background.html)


CSS 参考手册: [background-image 属性](https://www.runoob.com/pr-background-image.html)









	  AI 思考中...





			** [CSS background-image 属性](https://www.runoob.com/pr-background-image.html)
			[CSS background-repeat 属性](https://www.runoob.com/pr-background-repeat.html) **













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
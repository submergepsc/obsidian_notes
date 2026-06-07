# CSS background-repeat 属性

- Source: https://www.runoob.com/cssref/pr-background-repeat.html

**
## 实例


只有垂直方向重复 background-image：


```css
body
{
    background-image:url('paper.gif');
    background-repeat:repeat-y;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_background-repeaty)


---


## 标签定义及使用说明


设置如何平铺对象的 background-image 属性。


默认情况下，重复background-image的垂直和水平方向。


| 默认值: | repeat |
| --- | --- |
| 继承: | no |
| 版本: | CSS1 |
| JavaScript 语法: | object object.style.backgroundRepeat="repeat-y" |


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


紧跟在 -webkit-, -ms- 或 -moz- 前的数字为支持该前缀属性的第一个浏览器版本号。

<
| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| background-repeat | 1.0 | 4.0 | 1.0 | 1.0 | 3.5 |


IE8以及更早版本的浏览器不支持多个背景图像在一个元素。


注意** IE7 和更早的版本不支持 "inherit（继承）"的值。 IE8 需要定义 ！DOCTYPE。 IE9 支持 "inherit（继承）"。


---


## 提示和注释


**提示: **background-position 属性设置背景图像位置。如果指定的位置是没有任何背景，图像总是放在元素的左上角。


---


## 属性值


| 值 | 说明 |
| --- | --- |
| repeat | 背景图像将向垂直和水平方向重复。这是默认 |
| repeat-x | 只有水平位置会重复背景图像 |
| repeat-y | 只有垂直位置会重复背景图像 |
| no-repeat | background-image 不会重复 |
| inherit | 指定 background-repeat 属性设置应该从父元素继承 |

**
---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 在线实例


[如何在垂直和水平方向重复背景图像](https://www.runoob.com/try/try.php?filename=trycss_background-repeat) 这个例子演示了如何在垂直和水平方向重复背景图像。


[如何重复背景图像仅水平方向](https://www.runoob.com/try/try.php?filename=trycss_background-repeatx) 这个例子演示了如何重复背景图像仅水平方向。


[如何显示背景图像只有一次](https://www.runoob.com/try/try.php?filename=trycss_background-repeat_no-repeat) 这个例子演示了如何显示一个背景图片没有重复只有一次。


---


## 相关文章


CSS 教程: [CSS Background](https://www.runoob.com/../css/css-background.html)


CSS 参考手册: [background-position 属性](https://www.runoob.com/pr-background-position.html)








	  AI 思考中...





			** [CSS background-position 属性](https://www.runoob.com/pr-background-position.html)
			[CSS3 background-clip 属性](https://www.runoob.com/css3-pr-background-clip.html) **













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
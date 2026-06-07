# CSS clip 属性

- Source: https://www.runoob.com/cssref/pr-pos-clip.html

**
## 实例


裁剪一张图像：


```css
img
{
    position:absolute;
    clip:rect(0px,60px,200px,0px);
}
```




[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_clip)


---


## 属性定义及使用说明


如果图像大于包含它的元素，会发生什么？-clip属性，让你指定一个绝对定位的元素，该尺寸应该是可见的，该元素被剪裁成这种形状并显示。


注意：:** 如果先有"overflow：visible"，clip属性不起作用。


| 默认值: | auto |
| --- | --- |
| 继承: | no |
| 版本: | CSS2 |
| JavaScript 语法: | object.style.clip="rect(0px,50px,50px,0px)" |

**
---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| clip | 1.0 | 8.0 | 1.0 | 1.0 | 7.0 |


---


## 属性值


| 值 | 描述 |
| --- | --- |
| shape | 设置元素的形状。唯一合法的形状值是：rect (top, right, bottom, left) |
| auto | 默认值。不应用任何剪裁。 |
| inherit | 规定应该从父元素继承 clip 属性的值。 |


---


## 相关文章


CSS 教程: [CSS 定位](https://www.runoob.com/../css/css-positioning.html)









	  AI 思考中...





			** [CSS clear 属性](https://www.runoob.com/pr-class-clear.html)
			[CSS color 属性](https://www.runoob.com/pr-text-color.html) **













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
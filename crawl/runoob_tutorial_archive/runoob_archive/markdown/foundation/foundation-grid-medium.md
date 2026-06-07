# Foundation 网格 - 中型设备

- Source: https://www.runoob.com/foundation/foundation-grid-medium.html

上一章节我们介绍了小型设备上我们使用 `.small-*` 类来设置，网格比例为 25%/75%：


```
<div class="small-3 columns">....</div>
<div class="small-9 columns">....</div>
```


在中型设备上我们推荐的比例为 50%/50%。


**提示:** 中型设备的屏幕尺寸定义在 `40.0625em` 到 `64.0624em` 之间。


中型设备上使用 `.medium-*` 类。


现在我们在中型设备上添加两列：


```
<div class="small-3 medium-6 columns">....</div>
<div class="small-9 medium-6 columns">....</div>
```


以上实例设置了两个列，比例为 25% 和 75% (Foundation 是移动优先: 如果没有特别说明，在大型设备上会继承 .small 类的代码):


小型设备上使用的比例为 25%/75% (`.small-3` 和 `.small-9`)。但在中型设备上使用的比例为 50%/50% (`.medium-6` 和 `.medium-6`) 。


### 实例


```
<div
	class="row">  <div class="small-3
	medium-6 columns" style="background-color:yellow;">    <p>菜鸟教程</p>  </div>  <div class="small-9
	medium-6 columns" style="background-color:pink;">
	    <p>菜鸟教程</p>  </div></div>
```


**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_grid_medium)


|  | 注意: 要保证数列加起来是 12 列! |
| --- | --- |


---


## 仅在中型设备上使用


以下实例中我们指定了 `.medium-6` 类 (不是 `.small-*`)。这表明在中型或大型设备上比例为 50%/50%。但在小型设备上会水平堆叠 (100% 宽度):


### 实例


```
<div
	class="row">  <div class="medium-6
	columns" style="background-color:yellow;">    <p>菜鸟教程</p>  </div>  <div class="medium-6
	columns" style="background-color:pink;">
	    <p>菜鸟教程</p>  </div></div>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_grid_medium2)








	  AI 思考中...





			** [Foundation 网格 – 小型设备](https://www.runoob.com/foundation-grid-small.html)
			[Foundation 网格 – 大型设备](https://www.runoob.com/foundation-grid-large.html) **













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
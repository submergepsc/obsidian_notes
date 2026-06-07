# Foundation CSS 可见性

- Source: https://www.runoob.com/foundation/foundation-ref-visibility.html

---


## 根据屏幕尺寸显示元素


以下类会根据设备(屏幕尺寸)来显示元素。


| 类 | 描述 |
| --- | --- |
| .show-for-small-only | 只在小型设备上显示元素 (屏幕宽度小于 40.0625em ) |
| .show-for-medium-up | 在中型及以上设备上显示元素 (屏幕宽度大于 40.0625em) |
| .show-for-medium-only | 只在中型设备上显示元素 (屏幕宽度在 40.0625em 到 64.0625em 之间) |
| .show-for-large-up | 在大型及以上设备上显示元素 (屏幕宽度大于 64.0625em) |
| .show-for-large-only | 只在大型设备上显示元素 (屏幕宽度在 64.0625em 到 90.0625em 之间) |
| .show-for-xlarge-up | 在更大型及以上设备上显示元素 (屏幕宽度大于 90.0625em) |
| .show-for-xlarge-only | 只在更大型及以上设备上显示元素 (屏幕宽度在 90.0625em 到 120.0625em之间) |
| .show-for-xxlarge-up | 在超大型及以上设备上显示元素 (屏幕宽度大于 120.0625em) |


以下实例演示了以上所有 `.show-` 类的可见性。


```
<p class="show-for-small-only">你在小型设备上。</p>
<p class="show-for-medium-up">你在中型、大型、更大型、超大型的设备上。</p>
<p class="show-for-medium-only">你在中型设备上。</p>
<p class="show-for-large-up">你在大型、更大型、超大型的设备上</p>
<p class="show-for-large-only">你在大型设备上。</p>
<p class="show-for-xlarge-up">你在更大型、超大型的设备上。</p>
<p class="show-for-xlarge-only">你在更大型设备上。</p>
<p class="show-for-xxlarge-up">你在超大型设备上。</p>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_ref_visibility_show)

---


## 根据屏幕尺寸隐藏元素


以下类会根据设备(屏幕尺寸)来隐藏元素。


| 类 | 描述 |
| --- | --- |
| .hide-for-small-only | 只在小型设备上隐藏元素 (屏幕宽度小于 40.0625em ) |
| .hide-for-medium-up | 在中型及以上设备上隐藏元素 (屏幕宽度大于 40.0625em) |
| .hide-for-medium-only | 只在中型设备上隐藏元素 (屏幕宽度在 40.0625em 到 64.0625em 之间) |
| .hide-for-large-up | 在大型及以上设备上隐藏元素 (屏幕宽度大于 64.0625em) |
| .hide-for-large-only | 只在大型设备上隐藏元素 (屏幕宽度在 64.0625em 到 90.0625em 之间) |
| .hide-for-xlarge-up | 在更大型及以上设备上隐藏元素 (屏幕宽度大于 90.0625em) |
| .hide-for-xlarge-only | 只在更大型及以上设备上隐藏元素 (屏幕宽度在 90.0625em 到 120.0625em之间) |
| .hide-for-xxlarge-up | 在超大型及以上设备上隐藏元素 (屏幕宽度大于 120.0625em) |


```
<p class="hide-for-small-only">你不在小型设备上。</p>
<p class="hide-for-medium-up">你不在中型、大型、更大型、超大型的设备上。</p>
<p class="hide-for-medium-only">你不在中型设备上。</p>
<p class="hide-for-large-up">你不在大型、更大型、超大型的设备上。</p>
<p class="hide-for-large-only">你不在大型设备上。</p>
<p class="hide-for-xlarge-up">你不在更大型、超大型的设备上。</p>
<p class="hide-for-xlarge-only">你不在更大型设备上。</p>
<p class="hide-for-xxlarge-up">你不在超大型设备上。</p>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_ref_visibility_hide)

---


## 根据屏幕方向显示元素


以下类会根据设备(屏幕尺寸)来隐藏元素。


我们可以设置元素在不同方向是是否显示或隐藏。笔记本等桌面设备一般是横向的，但是手机和平板设备可以是横向或纵向，我们可以根据用户手机拿的方向来设置元素隐藏与显示：


| 类 | 描述 |
| --- | --- |
| .show-for-landscape | 在横向时显示元素（纵向隐藏） |
| .show-for-portrait | 在纵向时显示元素（横向隐藏） |


下面实例根据使用的方向显示文本内容：


### 实例


```
<p class="show-for-landscape">文本只在横向显示。</p><p class="show-for-portrait">文本只在纵向显示。</p>
```

**
[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_ref_visibility_orientation)

---


## 触屏设备的显示与隐藏


你可以根据设备是否支持触摸来显示与隐藏元素。


| 类 | 描述 |
| --- | --- |
| .show-for-touch | 在支持触屏的设备上显示(不支持的设备上隐藏) |
| .hide-for-touch | 在支持触屏的设备上隐藏(不支持的设备上显示) |


下面实例根据设备是否支持触摸来显示文本内容：


### 实例


```
<p class="show-for-touch">你的设备支持触屏。</p><p
		class="hide-for-touch">你的设备不支持触屏。</p>
```


[尝试一下 »](https://www.runoob.com/try/try2.php?filename=tryfoundation_ref_visibility_touch)








	  AI 思考中...





			** [Foundation CSS 参考手册](https://www.runoob.com/foundation-ref-helpers.html)














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
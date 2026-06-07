# CSS 单位

- Source: https://www.runoob.com/cssref/css-units.html

CSS 有几个不同的单位用于表示长度。

一些设置 CSS 长度的属性有 width, margin, padding, font-size, border-width, 等。

长度有一个数字和单位组成如 10px, 2em, 等。

数字与单位之间不能出现空格。如果长度值为 0，则可以省略单位。

对于一些 CSS 属性，长度可以是负数。

有两种类型的长度单位：相对和绝对。


---


## 浏览器支持


下表中的数字表示支持该长度单位的最低浏览器版本。


| 长度单位 | Chrome | IE | Firefox | Safari | Opera |
| --- | --- | --- | --- | --- | --- |
| em, ex, %, px, cm, mm, in, pt, pc | 1.0 | 3.0 | 1.0 | 1.0 | 3.5 |
| ch | 27.0 | 9.0 | 1.0 | 7.0 | 20.0 |
| rem | 4.0 | 9.0 | 3.6 | 4.1 | 11.6 |
| vh, vw | 20.0 | 9.0 | 19.0 | 6.0 | 20.0 |
| vmin | 20.0 | 9.0* | 19.0 | 6.0 | 20.0 |
| vmax | 26.0 | 不支持 | 19.0 | 不支持 | 20.0 |


**注意:** Internet Explorer 9 通过不标准的名称 vm 来支持 vmin 。

---


## 相对长度


相对长度单位指定了一个长度相对于另一个长度的属性。对于不同的设备相对长度更适用。


| 单位 | 描述 | 在线实例 |
| --- | --- | --- |
| em | 它是描述相对于应用在当前元素的字体尺寸，所以它也是相对长度单位。一般浏览器字体大小默认为16px，则2em == 32px； | 尝试一下 |
| ex | 依赖于英文字母小 x 的高度 | 尝试一下 |
| ch | 数字 0 的宽度 |  |
| rem | rem 是根 em（root em）的缩写，rem作用于非根元素时，相对于根元素字体大小；rem作用于根元素字体大小时，相对于其出初始字体大小。 | 尝试一下 |
| vw | Viewport Width，视窗宽度，1vw=视窗宽度的1% | 尝试一下 |
| vh | Viewport Height，视窗高度，1vh=视窗高度的1% | 尝试一下 |
| vmin | vw和vh中较小的那个。 | 尝试一下 |
| vmax | vw和vh中较大的那个。 | 尝试一下 |
| % |  |  |

**

|  | 提示: rem与em有什么区别呢？区别在于使用rem为元素设定字体大小时，仍然是相对大小，但相对的只是HTML根元素。 |
| --- | --- |


---


## 绝对长度


绝对长度单位是一个固定的值，它反应一个真实的物理尺寸。绝对长度单位视输出介质而定，不依赖于环境（显示器、分辨率、操作系统等）。


| 单位 | 描述 | 在线实例 |
| --- | --- | --- |
| cm | 厘米 | 尝试一下 |
| mm | 毫米 | 尝试一下 |
| in | 英寸 (1in = 96px = 2.54cm) | 尝试一下 |
| px * | 像素 (1px = 1/96th of 1in) | 尝试一下 |
| pt | point，大约1/72英寸； (1pt = 1/72in) | 尝试一下 |
| pc | pica，大约 12pt，1/6英寸； (1pc = 12 pt) | 尝试一下 |


像素或许被认为是最好的"设备像素"，而这种像素长度和你在显示器上看到的文字屏幕像素无关。px实际上是一个按角度度量的单位。








	  AI 思考中...





			** [CSS Web安全字体](https://www.runoob.com/css-websafe-fonts.html)
			[CSS 颜色](https://www.runoob.com/css-colors.html) **













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
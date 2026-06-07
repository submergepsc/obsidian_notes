# CSS color 属性

- Source: https://www.runoob.com/cssref/pr-text-color.html

**
## 实例


不同元素设置text-color：


```css
body {
    color:red;
}
h1 {
    color:#00ff00;
}
p {
    color:rgb(0,0,255);
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_color)


---


## 属性定义及使用说明


Color属性指定文本的颜色。


| 默认值: | 未指定 |
| --- | --- |
| 继承: | 是 |
| 版本: | CSS1 |
| JavaScript 语法: | object.style.color="#FF0000" |


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


紧跟在 -webkit-, -ms- 或 -moz- 前的数字为支持该前缀属性的第一个浏览器版本号。


| 属性 | | | | | | | --- | --- | --- | --- | --- | --- | | color | 1.0 | 3.0 | 1.0 | 1.0 | 3.5 | --- ## 提示和注释 提示:**请使用合理的背景颜色和文本颜色搭配，这样可以提高文本的可读性。


---


## 属性值


颜色值可以使用以下几种方式来设置：


| 值 | 描述 | 实例 |
| --- | --- | --- |
| 颜色的名称 | 颜色的名称，比如red, blue, brown, lightseagreen等，不区分大小写。 |
```
color:red;    /* 红色 */
color:black;  /* 黑色 */
color:gray;   /* 灰色 */
color:white;  /* 白色 */
color:purple; /* 紫色 */
```
 |
| 十六进制 | 十六进制符号 #RRGGBB 和 #RGB（比如 #ff0000）。"#" 后跟 6 位或者 3 位十六进制字符（0-9, A-F）。 |
```
#f03
#F03
#ff0033
#FF0033
rgb(255,0,51)
rgb(255, 0, 51)
```
 |
| RGB，红-绿-蓝（red-green-blue (RGB)） | 规定颜色值为 rgb 代码的颜色，函数格式为 rgb(R,G,B)，取值可以是 0-255 的整数或百分比。 |
```
rgb(255,0,51)
rgb(255, 0, 51)
rgb(100%,0%,20%)
rgb(100%, 0%, 20%)
```
 |
| RGBA，红-绿-蓝-阿尔法（RGBa） | RGBa 扩展了 RGB 颜色模式，它包含了阿尔法通道，允许设定一个颜色的透明度。a 表示透明度：0=透明；1=不透明。 |
```
rgba(255,0,0,0.1)    /* 10% 不透明 */
rgba(255,0,0,0.4)    /* 40% 不透明 */
rgba(255,0,0,0.7)    /* 70% 不透明 */
rgba(255,0,0,  1)    /* 不透明，即红色 */
```
 |
| HSL，色相-饱和度-明度（Hue-saturation-lightness） | 色相（Hue）表示色环（即代表彩虹的一个圆环）的一个角度。 饱和度和明度由百分数来表示。 100% 是满饱和度，而 0% 是一种灰度。 100% 明度是白色， 0% 明度是黑色，而 50% 明度是"一般的"。 |
```
hsl(120,100%,25%)    /* 深绿色 */
hsl(120,100%,50%)    /* 绿色 */
hsl(120,100%,75%)    /* 浅绿色 */
```
 |


---


## 更多实例


## 实例


颜色为 16 进制值：


```css
body {color: #92a8d1;}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_color2)


## 实例


颜色值为 RGB：


```css
body {color: rgb(255,0,51);}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_color3)


## 实例


颜色值为 RGBA：


```css
body {color: rgba(255,0,0,0.7);}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_color4)


## 实例


颜色值为 HSL：


```css
body {color: hsl(120,100%,25%) ;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_color5)


## 实例


颜色值为 HSLA：


```css
body {color: hsla(240,100%,50%, 0.7);}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_color6)


---


## 相关文章


CSS 教程: [CSS 文本格式](https://www.runoob.com/../css/css-text.html)









	  AI 思考中...





			** [CSS clip 属性](https://www.runoob.com/pr-pos-clip.html)
			[CSS3 column-count 属性](https://www.runoob.com/css3-pr-column-count.html) **













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
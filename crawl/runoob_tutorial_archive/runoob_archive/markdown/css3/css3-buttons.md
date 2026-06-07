# CSS 按钮

- Source: https://www.runoob.com/css3/css3-buttons.html

本章节我们为大家介绍使用 CSS 来制作按钮。


---


## 基本按钮样式


**默认按钮 CSS 按钮


## 实例


```css
.button {    background-color: #4CAF50; /* Green */    border: none;
    color: white;    padding: 15px 32px;    text-align: center;
    text-decoration: none;    display: inline-block;    font-size: 16px;
    }
```



[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_basic)


---


## 按钮颜色

Green
Blue
Red
Gray
Black

我们可以使用 `background-color` 属性来设置按钮颜色:


## 实例


```css
.button1 {background-color: #4CAF50;} /* 绿色 */
.button2 {background-color: #008CBA;} /* 蓝色 */
.button3 {background-color: #f44336;} /* 红色 */
.button4 {background-color: #e7e7e7; color: black;} /* 灰色 */
.button5 {background-color: #555555;} /* 黑色 */
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_color)


---


## 按钮大小


10px
12px
16px
20px
24px


我们可以使用 `font-size` 属性来设置按钮大小:


## 实例


```css
.button1 {font-size: 10px;}
.button2 {font-size: 12px;}
.button3 {font-size: 16px;}
.button4 {font-size: 20px;}
.button5 {font-size: 24px;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_font)


---


## 圆角按钮


2px
4px
8px
12px
50%


我们可以使用 `border-radius` 属性来设置圆角按钮:


## 实例


```css
.button1 {border-radius: 2px;}
.button2 {border-radius: 4px;}
.button3 {border-radius: 8px;}
.button4 {border-radius: 12px;}
.button5 {border-radius: 50%;}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_round)


---


## 按钮边框颜色


绿
蓝
红
灰
黑


我们可以使用 `border` 属性设置按钮边框颜色:


## 实例


```css
.button1 {
    background-color: white;
    color: black;
    border: 2px solid #4CAF50; /* Green */
}
...
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_border)


---


## 鼠标悬停按钮


绿
蓝
红
灰
黑


绿
蓝
红
灰
黑


我们可以使用 `:hover` 选择器来修改鼠标悬停在按钮上的样式。


提示:** 我们可以使用 `transition-duration` 属性来设置 "hover" 效果的速度:


## 实例


```css
.button {
    -webkit-transition-duration: 0.4s; /* Safari */
    transition-duration: 0.4s;
}

.button:hover {
    background-color: #4CAF50; /* Green */
    color: white;
}
...
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_hover)


---


## 按钮阴影


阴影按钮
鼠标悬停后显示阴影

我们可以使用 `box-shadow` 属性来为按钮添加阴影:


## 实例


```css
.button1 {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}

.button2:hover {
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_shadow)


---


## 禁用按钮


正常按钮
禁用按钮


我们可以使用 `opacity` 属性为按钮添加透明度 (看起来类似 "disabled" 属性效果)。


提示:** 我们可以添加 `cursor` 属性并设置为 "not-allowed" 来设置一个禁用的图片:


## 实例


```css
.disabled {
    opacity: 0.6;
    cursor: not-allowed;
}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_disabled)


---


## 按钮宽度


250px

50%
100%


默认情况下，按钮的大小由按钮上的文本内容决定( 根据文本内容匹配长度 )。 我们可以使用 `width` 属性来设置按钮的宽度:


提示:** 如果要设置固定宽度可以使用像素 (px) 为单位，如果要设置响应式的按钮可以设置为百分比。


## 实例


```css
.button1 {width: 250px;}
.button2 {width: 50%;}
.button3 {width: 100%;}
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_width)


---


## 按钮组


Button
Button
Button
Button


移除外边距并添加 `float:left` 来设置按钮组:


## 实例


```css
.button {
    float: left;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_group)


---


## 带边框按钮组


Button
Button
Button
Button


我们可以使用 `border` 属性来设置带边框的按钮组:


## 实例


```css
.button {
    float: left;
    border: 1px solid green
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_group_border)


## 实例


```css
.btn-group button {
    background-color: #04AA6D; /* 绿色背景 */
    border: 1px solid green; /* 绿色边框 */
    color: white; /* 白色文本 */
    padding: 10px 24px; /* 内边距离、 */
    cursor: pointer; /* 指针/手形图标 */
    float: left; /* 并排浮动按钮 */
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_group_border2)


---


## 按钮动画


## 实例


鼠标移动到按钮上后添加箭头标记:


```css
Hover
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_animate1)


## 实例


点击时添加 "波纹" 效果:


```css
Click
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_animate2)


## 实例


点击时添加 "压下" 效果:


```css
Click
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_buttons_animate3)


> 更多按钮样式可以使用 CSS 按钮生成器：[https://c.runoob.com/front-end/6222/](https://c.runoob.com/front-end/6222/)**










	  AI 思考中...





			** [CSS 图片](https://www.runoob.com/css3-images.html)
			[CSS 分页实例](https://www.runoob.com/css3-pagination.html) **













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
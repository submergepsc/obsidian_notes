# CSS text-decoration 属性

- Source: https://www.runoob.com/cssref/pr-text-text-decoration.html

**
## 实例


设置h1，h2，h3和h4元素文本装饰：


```css
h1 {text-decoration:overline}
h2 {text-decoration:line-through}
h3 {text-decoration:underline}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_text-decoration)


---


## 属性定义及使用说明


text-decoration 属性规定添加到文本的修饰，下划线、上划线、删除线等。


text-decoration 属性是以下三种属性的简写：


- [text-decoration-line](https://www.runoob.com/css3-pr-text-decoration-line.html)
- [text-decoration-color](https://www.runoob.com/css3-pr-text-decoration-color.html)
- [text-decoration-style](https://www.runoob.com/css3-pr-text-decoration-style.html)


### 语法


```
/*关键值*/
text-decoration: none;                     /*没有文本装饰*/
text-decoration: underline red;            /*红色下划线*/
text-decoration: underline wavy red;       /*红色波浪形下划线*/

/*全局值*/
text-decoration: inherit;
text-decoration: initial;
text-decoration: unset;
```


| 默认值： | none |
| --- | --- |
| 继承： | no |
| 版本： | CSS1 |
| JavaScript 语法： | object.style.textDecoration="overline" |


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| text-decoration | 1.0 | 3.0 | 1.0 | 1.0 | 3.5 |


---


## 属性值


| 值 | 描述 |
| --- | --- |
| none | 默认。定义标准的文本。 |
| underline | 定义文本下的一条线。 |
| overline | 定义文本上的一条线。 |
| line-through | 定义穿过文本下的一条线。 |
| blink | 定义闪烁的文本。 |
| inherit | 规定应该从父元素继承 text-decoration 属性的值。 |


---


## 更多实例


## 实例


```css
h1.under {
    text-decoration: underline;
}
h1.over {
    text-decoration: overline;
}
p.line {
    text-decoration: line-through;
}
p.blink {
    text-decoration: blink;
}
a.none {
    text-decoration: none;
}
p.underover {
    text-decoration: underline overline;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_text-decoration2)


## 实例


虚线与波浪线：


```css
h1 {
  text-decoration: underline overline dotted red;
}

h2 {
  text-decoration: underline overline wavy blue;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_text-decoration3)


---


## 相关文章


CSS 教程: [CSS 文本](https://www.runoob.com/../css/css-text.html)








	  AI 思考中...





			** [CSS text-align 属性](https://www.runoob.com/pr-text-text-align.html)
			[CSS text-indent 属性](https://www.runoob.com/pr-text-text-indent.html) **













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
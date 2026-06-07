# CSS counter-reset 属性

- Source: https://www.runoob.com/cssref/pr-gen-counter-reset.html

**
## 实例


对部分和子部分进行编号（比如 "Section 1"、"1.1"、"1.2"）的方法：


```css
body
{
    counter-reset:section;
}

h1
{
    counter-reset:subsection;
}

h1:before
{
    counter-increment:section;
    content:"Section " counter(section) ". ";
}

h2:before
{
    counter-increment:subsection;
    content:counter(section) "." counter(subsection) " ";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_gen_counter-reset)


---


## 属性定义及使用说明


counter-reset属性创建或重置一个或多个计数器。


counter-reset属性通常是和counter-increment属性，content属性一起使用。


| 默认值： | none |
| --- | --- |
| 继承： | no |
| 版本： | CSS2 |
| JavaScript 语法： | object.style.counterReset="subsection" |


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


所有主流浏览器都支持counter-reset属性。


注意：** IE8只有指定!DOCTYPE才支持counter-reset属性。


---


## 属性值


| 值 | 说明 |
| --- | --- |
| none | 默认。不能对选择器的计数器进行重置 |
| id number | id 定义重置计数器的选择器、id 或 class。 number 可设置此选择器出现次数的计数器的值。可以是正数、零或负数。 |
| inherit | 规定应该从父元素继承 counter-reset 属性的值 |

**
---


## 相关文章


CSS reference: [:before 伪元素](https://www.runoob.com/sel-before.html)


CSS reference: [:after 伪元素](https://www.runoob.com/sel-after.html)


CSS reference: [content 属性](https://www.runoob.com/pr-gen-content.html)


CSS reference: [counter-increment 属性](https://www.runoob.com/pr-gen-counter-increment.html)








	  AI 思考中...





			** [CSS counter-increment 属性](https://www.runoob.com/pr-gen-counter-increment.html)
			[CSS cursor 属性](https://www.runoob.com/pr-class-cursor.html) **













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
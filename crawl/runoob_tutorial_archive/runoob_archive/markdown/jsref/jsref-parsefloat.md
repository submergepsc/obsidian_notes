# JavaScript parseFloat() 函数

- Source: https://www.runoob.com/jsref/jsref-parsefloat.html

[![函数参考手册](https://www.runoob.com/images/up.gif) JavaScript 全局函数](https://www.runoob.com/jsref-obj-global.html)


---


## 定义和用法


parseFloat() 函数可解析一个字符串，并返回一个浮点数。


该函数指定字符串中的首个字符是否是数字。如果是，则对字符串进行解析，直到到达数字的末端为止，然后以数字返回该数字，而不是作为字符串。


## 语法


parseFloat(string)
**
| 参数 | 描述 |
| --- | --- |
| string | 必需。要被解析的字符串。 |


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


所有主要浏览器都支持 parseFloat() 函数


---


## 提示和注释


注意：** 字符串中只返回第一个数字。


**注意：** 开头和结尾的空格是允许的。


**注意：** 如果字符串的第一个字符不能被转换为数字，那么 parseFloat() 会返回 NaN。


---


## 实例


## 实例


使用 parseFloat() 来解析不同的字符串：


```
document.write(parseFloat("10") + "<br>");
document.write(parseFloat("10.33") + "<br>");
document.write(parseFloat("34 45 66") + "<br>");
document.write(parseFloat(" 60 ") + "<br>");
document.write(parseFloat("40 years") + "<br>");
document.write(parseFloat("He was 40") + "<br>");
```


以上实例输出结果:


```
10
10.33
34
60
40
NaN
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_parsefloat)


---


[![函数 参考手册](https://www.runoob.com/images/up.gif) JavaScript 全局函数](https://www.runoob.com/jsref-obj-global.html)








	  AI 思考中...





			** [JavaScript parseInt() 函数](https://www.runoob.com/jsref-parseint.html)
			[JavaScript Number() 函数](https://www.runoob.com/jsref-number.html) **













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
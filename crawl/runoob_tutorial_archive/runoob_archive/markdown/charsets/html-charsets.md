# HTML 字符集

- Source: https://www.runoob.com/charsets/html-charsets.html

---


要正确显示一个 HTML 页面，浏览器必须知道要使用的字符集（字符编码）。


---


## HTML 字符集


在 HTML 中，正确的字符编码是什么？


**HTML5 中默认的字符编码是 UTF-8。**


这并非总是如此。早期网络的字符编码是 ASCII 码。


后来，从 HTML 2.0 到 HTML 4.01，ISO-8859-1 被认定为标准。


随着 XML 和 HTML5 的出现，UTF-8 也终于到来了，解决了大量的字符编码问题。


下面是关于字符编码标准的简短概述。


---


## 在开始的时候：ASCII


计算机信息（数字、文字、图片）在电子中是以二进制 1 和 0（01000101）进行存储的。


为了规范字母数字字符的存储，创建了 ASCII（全称 American Standard Code for Information Interchange）。它为每个存储字符定义了一个独特的二元 7 位数字，支持 0-9 数字，大/小写英文字母（a-z、A-Z）和一些特殊的字符，比如 ! $ + - ( ) @  。


由于 ASCII 使用一个字节（7 位表示字符，1 位表示传输奇偶控制），所以它只能表示 128 个不同的字符。这些字符中有 32 个被保留作为其他控制目的使用。


ASCII 的最大的缺点是，它排除了非英文字母。


ASCII 今天仍然在广泛使用，尤其是在大型计算机系统中。


如需深入了解 ASCII，请查看[完整的 ASCII 参考手册](https://www.runoob.com/ref-html-ascii.html)。


---


## 在 Windows 中：ANSI


ANSI（也称为 Windows-1252），是 Windows 95 及其之前的 Windows 系统中默认的字符集。


ANSI 是 ASCII 的扩展，它加入了国际字符。它使用一个完整的字节（8 位）来表示 256 个不同字符。


自从 ANSI 成为 Windows 中默认的字符集，所有的浏览器都支持 ANSI。


如需深入了解 ANSI，请查看[完整的 ANSI 参考手册](https://www.runoob.com/ref-html-ansi.html)。


---


## 在 HTML 4 中：ISO-8859-1


由于大多数国家使用 ASCII 以外的字符，在 HTML 2.0 标准中，默认的字符编码更改为 ISO-8859-1。


ISO-8859-1 是 ASCII 的扩展，它加入了国际字符。与 ANSI 一样，它使用一个完整的字节（8 位）来表示 256 个不同字符。


|  | 当浏览器在网页中检测到 ISO-8859-1 时，通常默认为 ANSI，因为除了 ANSI 有 32 个额外的字符这一点，其他方面 ANSI 基本等同于 ISO-8859-1。 |
| --- | --- |


如果 HTML 4 网页使用了不同于 ISO-8859-1 的字符集，则需要在  标签中指定，如下所示：


## 实例


```
<meta http-equiv="Content-Type" content="text/html;charset=ISO-8859-8">
```


**
|  | HTML5 中默认的字符集是 UTF-8。所有的 HTML 4 处理器都支持 UTF-8，所有的 HTML5 和 XML 处理器都支持 UTF-8 和 UTF-16。 |
| --- | --- |


如需深入了解 ISO-8859-1，请查看[完整的 ISO-8859-1 参考手册](https://www.runoob.com/ref-html-8859.html)。


---


## 在 HTML5 中：Unicode（UTF-8）


由于以上所列的字符集是有限的，在多语言环境中是不兼容的，所以 Unicode 联盟（Unicode Consortium）开发了 Unicode 标准（Unicode Standard）。


Unicode 标准覆盖了（几乎）所有的字符、标点符号和符号。


Unicode 使文本的处理、存储和运输，独立于平台和语言。


HTML5 中默认的字符编码是 UTF-8。**


如需深入了解 Unicode（UTF-8），请查看[完整的 Unicode 参考手册](https://www.runoob.com/ref-html-utf8.html)。

**







	  AI 思考中...






			[HTML ASCII 参考手册](https://www.runoob.com/ref-html-ascii.html) **













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

      : · [HTML 字符集设置](https://www.runoob.com/html-charsets.html)

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
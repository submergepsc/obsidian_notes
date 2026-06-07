# HTML Unicode（UTF-8） 参考手册

- Source: https://www.runoob.com/charsets/ref-html-utf8.html

---


## Unicode 联盟（Unicode Consortium）


Unicode 联盟（Unicode Consortium）开发了 Unicode 标准（Unicode Standard）。他们的目标是使用标准的 Unicode 转换格式（即 UTF，全称 Unicode Transformation Format）取代现有的字符集。


Unicode 标准是一个成功的创举，在 HTML、XML、Java、JavaScript、E-mail、ASP、PHP 中都得到实现。Unicode 标准也得到许多操作系统和所有现代浏览器的支持。


Unicode 联盟与领先的标准开发组织合作，这些组织有 ISO、W3C 和 ECMA。


---


## Unicode 字符集


Unicode 可以由不同的字符集实现。最常用的编码是 UTF-8 和 UTF-16：


| 字符集 | 描述 |
| --- | --- |
| UTF-8 | UTF8 中的字符可以是 1 到 4 字节长。UTF-8 可以代表 Unicode 标准中的任何字符。UTF-8 向后兼容 ASCII。UTF-8 是电子邮件和网页的首选编码。 |
| UTF-16 | 16 位 Unicode 转换格式是一种可变长度的 Unicode 字符编码，能够编码整个 Unicode 指令表。UTF-16 主要用于操作系统和环境，如 Microsoft Windows、Java 和 .NET。 |


**提示：**Unicode 的前 128 个字符（与 ASCII 一一对应）使用一个与 ASCII二进制值相同的八位组进行编码，使有效的 ASCII 文本在进行 UTF-8 编码时也是有效的。


**提示：**所有的 HTML 4 处理器支持 UTF-8，所有的 HTML 5 和 XML 处理器支持 UTF-8 和 UTF-16！


---


## HTML5 标准：Unicode UTF-8


因为 ISO-8859 中字符集大小是有限的，且在多语言环境中不兼容，所以 Unicode 联盟开发了 Unicode 标准。


Unicode 标准覆盖了（几乎）所有的字符、标点符号和符号。


Unicode 使文本的处理、存储和运输，独立于平台和语言。


**HTML-5 中默认的字符编码是 UTF-8。**


下面列出了一些 HTML5 支持的 UTF-8 字符集：


| 字符集 | 十进制 | 十六进制 |
| --- | --- | --- |
| C0 控制与基本的 Latin（C0 Controls and Basic Latin） | 0-127 | 0000-007F |
| C1 控制与 Latin-1 的补充（C1 Controls and Latin-1 Supplement） | 128-255 | 0080-00FF |
| Latin 扩展 A（Latin Extended-A） | 256-383 | 0100-017F |
| Latin 扩展 B（Latin Extended-B） | 384-591 | 0180-024F |


如果 HTML5 网页使用不同于 UTF-8 的字符，则需要在  标签中指定，如下：


## 实例


```
<meta charset="ISO-8859-1">
```


**








	  AI 思考中...





			** [HTML ISO-8859-1 参考手册](https://www.runoob.com/ref-html-8859.html)
			[HTML 符号实体参考手册](https://www.runoob.com/ref-html-symbols.html) **













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
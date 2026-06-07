# Web 品质 - 国际化

- Source: https://www.runoob.com/quality/quality-international.html

---


网络无国界。


---


## 网络无国界。


*"With the Internet follows an absolute requirement to interchange data in a multiplicity of languages, which in turn utilize a bewildering number of characters."*


H. Alvestrand, Internet工程工作小组 (IETF), 1998年1月。


---


## 国际字符集


所有的 W3C 标准（自从1996年），包括 HTML、XHTML 和 XML 都定义了一个名为 Unicode (ISO 10646) 内部的内部字符集。


所有现代 web 浏览器都在原生地使用此字符集。而大多数在 internet 上传输的文档并没有使用这个 Unicode 字符集。


正因如此，Internet 客户（浏览器）与 Internet 服务器 之间必须有一种在通信中一致使用字符集的方法。


对每个文档在用的字符集进行标记，对于提升网站的品质来说至关重要。


请始终在  元素内使用下面的元素：


<meta charset="x">


把 X 替换为你所使用的字符集，比如ISO-8859-1、UTF-8 或者 UTF-16。


---


## 国际日期


请不要使用类似 "04-03-02" 的日期格式。


上面的日期可以表示为2004年3月2日，或者2002年3月4日，亦或者2002年4月3日。


国际标准化 (ISO) 为日期定义的国际标准格式是 "yyyy-mm-dd"，yyyy 是年，mm 是月，dd 是日。


如果您使用了 ISO 的格式，那么大多数访问者都能明白你的日期。









	  AI 思考中...





			** [Web 品质 – 重要的HTML元素](https://www.runoob.com/quality-elements.html)
			[Web 无障碍(WAI)](https://www.runoob.com/quality-accessibility.html) **













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
# XML 编码

- Source: https://www.runoob.com/xml/xml-encoding.html

---


XML 文档可以包含非 ASCII 字符，比如挪威语 æ ø å，或者法语 ê è é。


为了避免错误，需要规定 XML 编码，或者将 XML 文件存为 Unicode。


---


## XML 编码错误


如果您载入一个 XML 文档，您可以得到两个不同的错误，表示编码问题：


**在文本内容中发现无效字符。**


如果您的 XML 中包含非 ASCII 字符，且文件保存为没有指定编码的单字节 ANSI（或 ASCII），您会得到一个错误。


[单字节编码属性的 XML 文件](https://www.runoob.com/try/xml/singlebyte2.xml)。


[相同的单字节没有编码属性的 XML 文件](https://www.runoob.com/try/xml/singlebyte1.xml)。


**将当前编码切换为不被支持的指定编码**


如果您的 XML 文件保存为带有指定的单字节编码（WINDOWS-1252、ISO-8859-1、UTF-8）的双字节 Unicode（或 UTF-16），您会得到一个错误。


如果您的 XML 文件保存为带有指定的双字节编码（UTF-16）的单字节 ANSI（或 ASCII），您也会得到一个错误。


[双字节没有编码的 XML 文件](https://www.runoob.com/try/xml/doublebyte2.xml)。


[相同的双字节具有单字节编码的 XML 文件](https://www.runoob.com/try/xml/doublebyte1.xml)。


---


## Windows 记事本


Windows 记事本默认会将文件保存为单字节的 ANSI（ASCII）。


如果您选择 "另存为..."，就可以指定 ANSI、UTF-8、Unicode（UTF-16）或 Unicode Big。


将下面的 XML 保存为 ANSI、UTF-8 和 Unicode（注意文档不包含任何编码属性）。


<?xml version="1.0"?>**
<note>

  <from>Jani</from>

  <to>Tove</to>


  <message>Norwegian: æøå. French: êèé</message>

</note>


尝试将文件拖到您的浏览器，并查看结果。不同的浏览器会显示不同的结果。


不同编码的体验：


<?xml version="1.0" encoding="us-ascii"?>
<?xml version="1.0" encoding="windows-1252"?>
<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml version="1.0" encoding="UTF-8"?>
<?xml version="1.0" encoding="UTF-16"?>


请尝试：


[带有正确编码的保存](https://www.runoob.com/try/xml/note_with_right_encoding.xml)


[带有错误编码的保存](https://www.runoob.com/try/xml/note_with_wrong_encoding.xml)


---


## 结论


- 始终使用编码属性
- 使用支持编码的编辑器
- 确保您知道编辑器使用什么编码
- 在您的编码属性中使用相同的编码








	  AI 思考中...





			** [XML CDATA](https://www.runoob.com/xml-cdata.html)
			[服务器上的 XML](https://www.runoob.com/xml-server.html) **













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

      : ·[XML 实例](https://www.runoob.com/xml-examples.html)

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
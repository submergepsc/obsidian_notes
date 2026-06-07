# VBScript 用法

- Source: https://www.runoob.com/vbscript/vbscript-howto.html

---


HTML  标签被用来向 HTML 中插入 VBScript。


---


## HTML 中的 VBScript


如需在 HTML 中插入 VBScript，脚本必须写在标准的  和  标签之间。


在  标签中，请使用 type 属性来定义脚本语言 "text/vbscript"：


<html>**
<body>
**<script type="text/vbscript">

...

</script>
**</body>

</html>

IE 将解释和执行  和  之间的 VBScript 代码。


|  | VBScript 不应该被用作客户端脚本语言！ 在这里，我们使用仅适用于 IE 的 VBScript 的用于学习。 |
| --- | --- |


---


## VBScript 输出


当 VBScript 被用在 Web 服务器上的 ASP 页面时，语句 response.write()** 产生输出。


当我们使用 Internet Explorer 来测试 VBScript，我们使用 **document.write()** 来产生输出：


## 实例（仅适用于 Internet Explorer）


```
<html>
<body><script type="text/vbscript">
document.write("Hello World!")
</script></body>
</html>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_text)


在上面的实例中，浏览器输出 "Hello World!" 到 HTML 页面。










	  AI 思考中...





			** [VBScript 实例](https://www.runoob.com/vbscript-examples.html)
			[VBScript 变量](https://www.runoob.com/vbscript-variables.html) **













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
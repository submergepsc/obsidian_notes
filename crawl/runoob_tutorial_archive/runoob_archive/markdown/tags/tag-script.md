# HTML 标签

- Source: https://www.runoob.com/tags/tag-script.html

**
## 实例


通过 JavaScript 输出 "Hello world"：


```
<script>
document.write("Hello World!")
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryhtml_script)


---


## 浏览器支持


![Internet Explorer](https://www.runoob.com/images/compatible_ie.gif)![Firefox](https://www.runoob.com/images/compatible_firefox.gif)![Opera](https://www.runoob.com/images/compatible_opera.gif)![Google Chrome](https://www.runoob.com/images/compatible_chrome.gif)![Safari](https://www.runoob.com/images/compatible_safari.gif)


所有主流浏览器都支持  标签。


---


## 标签定义及使用说明


 标签用于定义客户端脚本，比如 JavaScript。


 元素既可包含脚本语句，也可以通过 "src" 属性指向外部脚本文件。


JavaScript 通常用于图像操作、表单验证以及动态内容更改。


---


## 提示和注释


注释：**如果使用 "src" 属性，则  元素必须是空的。


**提示：**请参阅 [](https://www.runoob.com/tag-noscript.html) 元素，对于那些在浏览器中禁用脚本或者其浏览器不支持客户端脚本的用户来说，该元素非常有用。


**注释：** 有多种执行外部脚本的方法：


- 如果 async="async"：脚本相对于页面的其余部分异步地执行（当页面继续进行解析时，脚本将被执行）
- 如果不使用 async 且 defer="defer"：脚本将在页面完成解析时执行
- 如果既不使用 async 也不使用 defer：在浏览器继续解析页面之前，立即读取并执行脚本


---


## HTML 4.01 与 HTML5之间的差异


在 HTML 4 中，"type" 属性是必需的，但在 HTML5 中是可选的。


"async" 属性是 HTML5 中的新属性。


HTML5 中不再支持 HTML 4.01 中的某些属性："xml:space"。


---


## HTML 与 XHTML 之间的差异


在 XHTML 中，脚本中的内容类型声明为 #PCDATA（代替 CDATA），就是说会对实体进行解析。


这意味着，在 XHTML 中，应该编码所有特殊的字符，或者把所有内容嵌套在 CDATA 部分中：


```
<script type="text/javascript">
//<![CDATA[
var i=10;
if (i<5)
{
    // 代码内容
}
//]]>
</script>
```


**

---


## 属性


New ：HTML5 中的新属性。


| 属性 | 值 | 描述 |
| --- | --- | --- |
| asyncNew | async | 规定异步执行脚本（仅适用于外部脚本）。 |
| charset | charset | 规定在脚本中使用的字符编码（仅适用于外部脚本）。 |
| defer | defer | 规定当页面已完成解析后，执行脚本（仅适用于外部脚本）。 |
| src | URL | 规定外部脚本的 URL。 |
| type | MIME-type | 规定脚本的 MIME 类型。 |
| xml:space | preserve | HTML5 不支持。规定是否保留代码中的空白。 |


---


## 全局属性


 标签支持 [HTML 的全局属性](https://www.runoob.com/ref-standardattributes.html)。


---


## 相关文章


HTML 教程：[HTML 脚本](https://www.runoob.com/../html/html-scripts.html)








	  AI 思考中...





			** [HTML  标签](https://www.runoob.com/tag-tt.html)
			[HTML  标签](https://www.runoob.com/tag-section.html) **













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

      : · [HTML ASCII 字符集](https://www.runoob.com/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/html-colorpicker.html)

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
# JavaScript JSON.stringify()

- Source: https://www.runoob.com/js/javascript-json-stringify.html

[![JavaScript JSON](https://www.runoob.com/images/up.gif) JavaScript JSON](https://www.runoob.com/js-json.html)


---


JSON.stringify() 方法用于将 JavaScript 值转换为 JSON 字符串。


### 语法


```
JSON.stringify(value[, replacer[, space]])
```


**参数说明：**


- **value:**必需， 要转换的 JavaScript 值（通常为对象或数组）。
- **replacer:** 可选。用于转换结果的函数或数组。 如果 replacer 为函数，则 JSON.stringify 将调用该函数，并传入每个成员的键和值。使用返回值而不是原始值。如果此函数返回 undefined，则排除成员。根对象的键是一个空字符串：""。 如果 replacer 是一个数组，则仅转换该数组中具有键值的成员。成员的转换顺序与键在数组中的顺序一样。
- **space:** 可选，文本添加缩进、空格和换行符，如果 space 是一个数字，则返回值文本在每个级别缩进指定数目的空格，如果 space 大于 10，则文本缩进 10 个空格。space 也可以使用非数字，如：\t。


### 返回值：


返回包含 JSON 文本的字符串。


### 实例


### 实例


```javascript
var str = {"name":"菜鸟教程", "site":"http://www.runoob.com"}
str_pretty1 = JSON.stringify(str)
document.write( "只有一个参数情况：" );
document.write( "<br>" );
document.write("<pre>" + str_pretty1 + "</pre>" );

document.write( "<br>" );
str_pretty2 = JSON.stringify(str, null, 4) //使用四个空格缩进
document.write( "使用参数情况：" );
document.write( "<br>" );
document.write("<pre>" + str_pretty2 + "</pre>" ); // pre 用于格式化输出
```


**
[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjson_stringify)


[![JavaScript JSON](https://www.runoob.com/images/up.gif) JavaScript JSON](https://www.runoob.com/js-json.html)









	  AI 思考中...





			** [JavaScript JSON.parse()](https://www.runoob.com/javascript-json-parse.html)
			[JavaScript 代码规范](https://www.runoob.com/js-conventions.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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
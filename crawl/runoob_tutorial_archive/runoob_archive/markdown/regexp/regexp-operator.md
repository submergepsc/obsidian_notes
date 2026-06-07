# 正则表达式 - 运算符优先级

- Source: https://www.runoob.com/regexp/regexp-operator.html

正则表达式从左到右进行计算，并遵循优先级顺序，这与算术表达式非常类似。


相同优先级的从左到右进行运算，不同优先级的运算先高后低。下表从最高到最低说明了各种正则表达式运算符的优先级顺序：


| 运算符 | 描述 |
| --- | --- |
| \ | 转义符 |
| (), (?:), (?=), [] | 圆括号和方括号 |
| *, +, ?, {n}, {n,}, {n,m} | 限定符 |
| ^, $, \任何元字符、任何字符 | 定位点和序列（即：位置和顺序） |
| \| | 替换，"或"操作 字符具有高于替换运算符的优先级，使得"m\|food"匹配"m"或"food"。若要匹配"mood"或"food"，请使用括号创建子表达式，从而产生"(m\|f)ood"。 |


以下是一些常见正则表达式运算符按照优先级从高到低的顺序：


- **转义符号：** `\` 是用于转义其他特殊字符的转义符号。它具有最高的优先级。示例：`\d`、`\.` 等，其中 `\d` 匹配数字，`\.` 匹配点号。
- **括号：** 圆括号 `()` 用于创建子表达式，具有高于其他运算符的优先级。示例：`(abc)+` 匹配 "abc" 一次或多次。
- **量词：** 量词指定前面的元素可以重复的次数。示例：`a*` 匹配零个或多个 "a"。
- **字符类：** 字符类使用方括号 `[]` 表示，用于匹配括号内的任意字符。示例：`[aeiou]` 匹配任何一个元音字母。
- **断言：** 断言是用于检查字符串中特定位置的条件的元素。示例：`^` 表示行的开头，`$` 表示行的结尾。
- **连接：** 连接在没有其他运算符的情况下表示字符之间的简单连接。示例：`abc` 匹配 "abc"。
- **管道：** 管道符号 `|` 表示"或"关系，用于在多个模式之间选择一个。示例：`cat|dog` 匹配 "cat" 或 "dog"。


接下来我们看下以下正则表达式的优先级说明：


```
\d{2,3}|[a-z]+(abc)*
```


- `\d{2,3}` 匹配两到三个数字。
- `|` 表示或。
- `[a-z]+` 匹配一个或多个小写字母。
- `(abc)*` 匹配零个或多个 "abc"。








	  AI 思考中...





			** [正则表达式 – 元字符](https://www.runoob.com/regexp-metachar.html)
			[正则表达式 – 匹配规则](https://www.runoob.com/regexp-rule.html) **













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
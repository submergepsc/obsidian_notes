# JavaScript RegExp 对象

- Source: https://www.runoob.com/jsref/jsref-obj-regexp.html

---


## RegExp 对象


正则表达式是描述字符模式的对象。


正则表达式用于对字符串模式匹配及检索替换，是对字符串执行模式匹配的强大工具。


## 语法


var patt=new RegExp(pattern,modifiers);**

或者更简单的方式:


var patt=/pattern/modifiers;


- pattern（模式） 描述了表达式的模式
- modifiers(修饰符) 用于指定全局匹配、区分大小写的匹配和多行匹配


> 注意：**当使用构造函数创造正则对象时，需要常规的字符转义规则（在前面加反斜杠 \）。比如，以下是等价的：
>
>
>
```
var re = new RegExp("\\w+");
var re = /\w+/;
```


更多关于 RegExp 对象请阅读我们的 [JavaScript RegExp 对象教程](https://www.runoob.com/../js/js-obj-regexp.html)。


---


## 修饰符


修饰符用于执行区分大小写和全局匹配:


| 修饰符 | 描述 |
| --- | --- |
| i | 执行对大小写不敏感的匹配。 |
| g | 执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。 |
| m | 执行多行匹配。 |


## 方括号


方括号用于查找某个范围内的字符：


| 表达式 | 描述 |
| --- | --- |
| [abc] | 查找方括号之间的任何字符。 |
| [^abc] | 查找任何不在方括号之间的字符。 |
| [0-9] | 查找任何从 0 至 9 的数字。 |
| [a-z] | 查找任何从小写 a 到小写 z 的字符。 |
| [A-Z] | 查找任何从大写 A 到大写 Z 的字符。 |
| [A-z] | 查找任何从大写 A 到小写 z 的字符。 |
| [adgk] | 查找给定集合内的任何字符。 |
| [^adgk] | 查找给定集合外的任何字符。 |
| (red\|blue\|green) | 查找任何指定的选项。 |


## 元字符


元字符（Metacharacter）是拥有特殊含义的字符：


| 元字符 | 描述 |
| --- | --- |
| . | 查找单个字符，除了换行和行结束符。 |
| \w | 查找数字、字母及下划线。 |
| \W | 查找非单词字符。 |
| \d | 查找数字。 |
| \D | 查找非数字字符。 |
| \s | 查找空白字符。 |
| \S | 查找非空白字符。 |
| \b | 匹配单词边界。 |
| \B | 匹配非单词边界。 |
| \0 | 查找 NULL 字符。 |
| \n | 查找换行符。 |
| \f | 查找换页符。 |
| \r | 查找回车符。 |
| \t | 查找制表符。 |
| \v | 查找垂直制表符。 |
| \xxx | 查找以八进制数 xxx 规定的字符。 |
| \xdd | 查找以十六进制数 dd 规定的字符。 |
| \uxxxx | 查找以十六进制数 xxxx 规定的 Unicode 字符。 |


## 量词


| 量词 | 描述 |
| --- | --- |
| n+ | 匹配任何包含至少一个 n 的字符串。 例如，/a+/ 匹配 "candy" 中的 "a"，"caaaaaaandy" 中所有的 "a"。 |
| n* | 匹配任何包含零个或多个 n 的字符串。例如，/bo*/ 匹配 "A ghost booooed" 中的 "boooo"，"A bird warbled" 中的 "b"，但是不匹配 "A goat grunted"。 |
| n? | 匹配任何包含零个或一个 n 的字符串。例如，/e?le?/ 匹配 "angel" 中的 "el"，"angle" 中的 "le"。 |
| n{X} | 匹配包含 X 个 n 的序列的字符串。 例如，/a{2}/ 不匹配 "candy," 中的 "a"，但是匹配 "caandy," 中的两个 "a"，且匹配 "caaandy." 中的前两个 "a"。 |
| n{X,} | X 是一个正整数。前面的模式 n 连续出现至少 X 次时匹配。 例如，/a{2,}/ 不匹配 "candy" 中的 "a"，但是匹配 "caandy" 和 "caaaaaaandy." 中所有的 "a"。 |
| n{X,Y} | X 和 Y 为正整数。前面的模式 n 连续出现至少 X 次，至多 Y 次时匹配。 例如，/a{1,3}/ 不匹配 "cndy"，匹配 "candy," 中的 "a"，"caandy," 中的两个 "a"，匹配 "caaaaaaandy" 中的前面三个 "a"。注意，当匹配 "caaaaaaandy" 时，即使原始字符串拥有更多的 "a"，匹配项也是 "aaa"。 |
| n$ | 匹配任何结尾为 n 的字符串。 |
| ^n | 匹配任何开头为 n 的字符串。 |
| ?=n | 匹配任何其后紧接指定字符串 n 的字符串。 |
| ?!n | 匹配任何其后没有紧接指定字符串 n 的字符串。 |


## RegExp 对象方法


| 方法 | 描述 |
| --- | --- |
| compile | 在 1.5 版本中已废弃。 编译正则表达式。 |
| exec | 检索字符串中指定的值。返回找到的值，并确定其位置。 |
| test | 检索字符串中指定的值。返回 true 或 false。 |
| toString | 返回正则表达式的字符串。 |


## 支持正则表达式的 String 对象的方法


| 方法 | 描述 | FF | IE |
| --- | --- | --- | --- |
| search | 检索与正则表达式相匹配的值。 | 1 | 4 |
| match | 找到一个或多个正则表达式的匹配。 | 1 | 4 |
| replace | 替换与正则表达式匹配的子串。 | 1 | 4 |
| split | 把字符串分割为字符串数组。 | 1 | 4 |


---


## RegExp 对象属性


| 属性 | 描述 |
| --- | --- |
| constructor | 返回一个函数，该函数是一个创建 RegExp 对象的原型。 |
| global | 判断是否设置了 "g" 修饰符 |
| ignoreCase | 判断是否设置了 "i" 修饰符 |
| lastIndex | 用于规定下次匹配的起始位置 |
| multiline | 判断是否设置了 "m" 修饰符 |
| source | 返回正则表达式的匹配模式 |








	  AI 思考中...





			** [RegExp [abc] 表达式](https://www.runoob.com/jsref-regexp-charset.html)
			[JavaScript unescape() 函数](https://www.runoob.com/jsref-unescape.html) **













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
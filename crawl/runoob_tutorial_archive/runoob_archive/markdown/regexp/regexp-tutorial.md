# 正则表达式 - 教程

- Source: https://www.runoob.com/regexp/regexp-tutorial.html

![](https://www.runoob.com/wp-content/uploads/2014/03/runoob-regex.png)


正则表达式（Regular Expression，简称 Regex 或 RegExp）是一种用来匹配字符串中字符组合的模式。


正则表达式是一种用于模式匹配和搜索文本的工具。


正则表达式提供了一种灵活且强大的方式来查找、替换、验证和提取文本数据。


正则表达式可以应用于各种编程语言和文本处理工具中，如 JavaScript、Python、Java、Perl 等。


入门视频：[正则表达式入门教程](https://mp.weixin.qq.com/s/TIub-jz9KU2ngoDg5FCnDQ)。


---


## 正则表达式可以做什么？

- **查找：**在文本中找到特定模式的内容
- **替换：**将符合某种模式的文本替换为其他内容
- **验证：**检查输入的数据是否符合预期格式
- **提取：**从复杂文本中提取需要的信息


---


## 实例


以下实例从字符串 str 中找出数字：


## 实例


从字符串 str 中提取数字部分的内容(匹配一次)：


```regex
var str = "abc123def";
var patt1 = /[0-9]+/;
document.write(str.match(patt1));
```


以下标记的文本是获得的匹配的表达式：


```regex
123
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_regexp1)


### 测试工具




修饰符：*



```
[0-9]+
```



匹配文本：



```
abc123def
```





## 正则表达式的模式


正则表达式的模式可以包括以下内容：


- 字面值字符：例如字母、数字、空格等，可以直接匹配它们自身。
- 特殊字符：例如点号 `.`、星号 `*`、加号 `+`、问号 `?` 等，它们具有特殊的含义和功能。
- 字符类：用方括号 `[ ]` 包围的字符集合，用于匹配方括号内的任意一个字符。
- 元字符：例如 `\d`、`\w`、`\s` 等，用于匹配特定类型的字符，如数字、字母、空白字符等。
- 量词：例如 `{n}`、`{n,}`、`{n,m}` 等，用于指定匹配的次数或范围。
- 边界符号：例如 `^`、`$`、`\b`、`\B` 等，用于匹配字符串的开头、结尾或单词边界位置。


## 内容列表


- [正则表达式 - 简介](https://www.runoob.com/../regex/regexp-intro.html)
- [正则表达式 - 语法](https://www.runoob.com/../regex/regexp-syntax.html)
- [正则表达式 - 元字符](https://www.runoob.com/../regex/regexp-metachar.html)
- [正则表达式 - 运算符优先级](https://www.runoob.com/../regex/regexp-operator.html)
- [正则表达式 - 匹配规则](https://www.runoob.com/../regex/regexp-rule.html)
- [正则表达式 - 示例](https://www.runoob.com/../regex/regexp-example.html)
- [正则表达式 - 在线工具](http://c.runoob.com/front-end/854)
- [正则表达式 - 可视化工具](https://c.runoob.com/front-end/7625/)


### 其他相关工具

- [测验工具！](https://www.runoob.com/try/try-regex.php)
- [AI 正则分析工具！](https://www.jyshare.com/front-end/9064/)
- [RegExr -- 正则表达式在线测试工具。](https://regexr.com/)
- [Regulex -- 正则表达式在线测试工具。](https://regex101.com/)










	  AI 思考中...






			[正则表达式 – 简介](https://www.runoob.com/regexp-intro.html) *













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
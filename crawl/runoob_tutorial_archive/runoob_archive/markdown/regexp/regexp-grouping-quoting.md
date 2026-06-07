# 正则表达式 - 分组和引用

- Source: https://www.runoob.com/regexp/regexp-grouping-quoting.html

在正则表达式中，**分组**（Grouping）允许我们将多个字符视为一个整体单元，就像数学中的括号一样。分组主要有两个作用：


- **将多个字符作为一个整体**：可以对这个整体应用量词（如 `*`、`+`、`?`、`{n}`）
- **捕获匹配的内容**：可以在后续引用或提取这部分匹配的内容


### 基本语法


使用圆括号 `()` 来创建分组：


```
(表达式)
```


例如，`(ab)+` 可以匹配 "ab"、"abab"、"ababab" 等，但不能匹配 "a" 或 "b"。


---


## 分组类型


正则表达式中有几种不同类型的分组：


### 1. 捕获分组（Capturing Group）


最常见的分组形式，会捕获匹配的内容并分配一个编号（从1开始）。


## 实例


```regex
(\d{4})-(\d{2})-(\d{2})  # 匹配日期格式 YYYY-MM-DD
```


这个表达式会创建3个分组：


- 分组1：4位数字的年份
- 分组2：2位数字的月份
- 分组3：2位数字的日期


### 2. 非捕获分组（Non-capturing Group）


使用 `(?:表达式)` 语法，表示只分组但不捕获。


## 实例


```regex
(?:Mr|Ms|Mrs)\. (\w+)  # 匹配 "Mr. Smith" 但只捕获 "Smith"
```


### 3. 命名分组（Named Capturing Group）


为分组指定名称，提高可读性（不同语言语法可能不同）。


Python 示例：


## 实例


```regex
(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})
```


JavaScript 示例：


## 实例


```regex
(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})
```


---


## 分组引用


分组最强大的功能之一是可以在正则表达式内部或外部引用已匹配的内容。


### 1. 反向引用（Backreference）


在正则表达式内部引用前面的分组，使用 `\数字` 语法：


## 实例


```regex
(\w+) \1  # 匹配重复的单词，如 "hello hello"
```


这个模式会匹配两个相同的单词，中间用空格分隔。


### 2. 命名反向引用


对于命名分组，可以使用名称来引用：


## 实例


```regex
(?P<word>\w+) (?P=word)  # Python 语法
\k<word>                 # JavaScript 语法
```


### 3. 替换引用


在替换操作中引用分组内容：


Python 示例：


## 实例


```regex
import re
text = "2023-05-15"
new_text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', text)
# 结果: "05/15/2023"
```


JavaScript 示例：


## 实例


```regex
let text = "2023-05-15";
let newText = text.replace(/(\d{4})-(\d{2})-(\d{2})/, '$2/$3/$1');
// 结果: "05/15/2023"
```


---


## 实际应用示例


### 示例1：匹配HTML标签


## 实例


```regex
<([a-z][a-z0-9]*)\b[^>]*>.*?</\1>
```


这个模式可以匹配成对的HTML标签（如 `...`），其中：


- `([a-z][a-z0-9]*)` 捕获标签名
- `\1` 引用前面捕获的标签名确保前后一致


### 示例2：验证重复单词


## 实例


```regex
\b(\w+)\b\s+\1\b
```


可以找出文本中连续重复的单词。


### 示例3：日期格式转换


Python 代码：


## 实例


```regex
import re

date = "2023-12-25"
# 将 YYYY-MM-DD 转换为 DD/MM/YYYY
new_date = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date)
print(new_date)  # 输出: 25/12/2023
```


---


## 分组的高级应用


### 1. 条件匹配


有些正则引擎支持基于分组的条件匹配：


## 实例


```regex
(?(1)true-pattern|false-pattern)
```


表示如果分组1已匹配，则匹配 true-pattern，否则匹配 false-pattern。


### 2. 平衡组（高级特性）


用于匹配嵌套结构（如括号），需要特定正则引擎支持。


---


## 常见问题与陷阱


- **过度使用分组**：不必要的分组会影响性能 - 坏例子：`(a)|(b)`（如果不需要捕获，应使用 `(?:a|b)`）
- **分组编号混淆**： - 分组编号按左括号的顺序从1开始 - 非捕获分组不参与编号
- **贪婪匹配问题**：
```
<(.*)>  # 会贪婪匹配到最后一个 >
```
 应使用：
```
<(.*?)>  # 非贪婪匹配
```


---


## 练习挑战


- 写一个正则表达式匹配重复的电子邮件用户名（如 `[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html);[[email protected]](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)`）
- 转换电话号码格式，从 `(123) 456-7890` 到 `123-456-7890`
- 提取HTML标签中的所有属性（如 `![...](https://www.runoob.com/...)` 中的 src 和 alt）


---


## 总结要点


| 概念 | 语法 | 用途 |
| --- | --- | --- |
| 捕获分组 | (pattern) | 捕获匹配内容并分配编号 |
| 非捕获分组 | (?:pattern) | 分组但不捕获 |
| 命名分组 | (?Ppattern) (Python) | 为分组指定名称 |
| 反向引用 | \1, \2 等 | 引用前面匹配的分组 |
| 命名反向引用 | (?P=name) (Python) | 按名称引用分组 |
| 替换引用 | $1, $2 或 \1, \2 | 在替换字符串中引用分组 |


掌握正则表达式的分组和引用功能，可以让你：


- 构建更复杂的匹配模式
- 提取和处理字符串中的特定部分
- 实现字符串的智能转换
- 验证复杂的文本结构









	  AI 思考中...





			** [正则表达式 – 位置匹配](https://www.runoob.com/regexp-positional-matching.html)
			[正则表达式 – 断言](https://www.runoob.com/regexp-assertions.html) **













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
# 正则表达式 - 修饰符（标记）

- Source: https://www.runoob.com/regexp/regexp-flags.html

正则表达式修饰符（也称为模式修饰符或标记）是用于改变正则表达式匹配行为的特殊指令。


标记也称为修饰符，正则表达式的标记用于指定额外的匹配策略。


标记不写在正则表达式里，标记位于表达式之外，格式如下：


```
/pattern/flags
```



---

## 常用修饰符


下表列出了正则表达式常用的修饰符：


### 1. i (ignore case) - 忽略大小写


- 使匹配不区分大小写
- 示例：`/abc/i` 可以匹配 "abc", "Abc", "ABC" 等
- 支持语言：几乎所有正则表达式实现（JavaScript、PHP、Python等）


### 2. g (global) - 全局匹配


- 查找所有匹配项，而不是在第一个匹配后停止
- 示例：在字符串 "ababab" 中，`/ab/g` 会匹配所有三个 "ab"
- 支持语言：JavaScript、PHP等


### 3. m (multiline) - 多行模式


- 改变 `^` 和 `$` 的行为，使其匹配每行的开头和结尾，而不仅是整个字符串的开头和结尾
- 示例：在多行字符串中，`/^abc/m` 会匹配每行开头的 "abc"
- 支持语言：JavaScript、PHP、Python、Perl等


### 4. s (single line/dotall) - 单行模式


- 使点号 `.` 匹配包括换行符在内的所有字符
- 在JavaScript中称为"dotall"模式，使用 `/s` 修饰符
- 示例：`/a.b/s` 可以匹配 "a\nb"
- 支持语言：PHP、Perl、Python(作为`re.DOTALL`)、JavaScript(ES2018+)


### 5. u (unicode) - Unicode模式


- 启用完整的Unicode支持
- 正确处理UTF-16代理对和Unicode字符属性
- 示例：`/\p{Script=Greek}/u` 可以匹配希腊字母
- 支持语言：JavaScript、PHP等


### 6. y (sticky) - 粘性匹配


- 从目标字符串的当前位置开始匹配（使用`lastIndex`属性）
- 类似于`^`锚点，但针对的是匹配的起始位置
- 示例：在JavaScript中，`/a/y` 会从`lastIndex`开始匹配 "a"
- 支持语言：JavaScript


### 7. x (extended) - 扩展模式


- 忽略模式中的空白和注释，使正则表达式更易读
- 示例：在PHP中，`/a b c/x` 等同于 `/abc/`
- 支持语言：PHP、Perl、Python(作为`re.VERBOSE`)


---


### g 修饰符

g 修饰符可以查找字符串中所有的匹配项：


![](https://www.runoob.com/wp-content/uploads/2020/08/D1A5F1E7-E25E-448E-9BE3-68508E058E99.jpg)


## 实例


在字符串中查找 "runoob":


```regex
var str="Google runoob taobao runoob";
var n1=str.match(/runoob/);   // 查找第一次匹配项
var n2=str.match(/runoob/g);  // 查找所有匹配项
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_match_regexp4)


### i 修饰符

i 修饰符为不区分大小写匹配，实例如下：

![](https://www.runoob.com/wp-content/uploads/2020/08/FF2D211D-0B88-492C-BAA4-04183278383E.jpg)


## 实例


在字符串中查找 "runoob":


```regex
var str="Google runoob taobao RUNoob";
var n1=str.match(/runoob/g);   // 区分大小写
var n2=str.match(/runoob/gi);  // 不区分大小写
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_match_regexp3)



### m 修饰符

m 修饰符可以使 **^** 和 **$** 匹配一段文本中每行的开始和结束位置。


g 只匹配第一行，添加 m 之后实现多行。


![](https://www.runoob.com/wp-content/uploads/2020/08/BC3E6D8A-21D2-44F8-A1AE-D90C4939D37A.jpg)


以下实例字符串中使用 **\n** 来换行：


## 实例


在字符串中查找 "runoob":


```regex
var str="runoobgoogle\ntaobao\nrunoobweibo";
var n1=str.match(/^runoob/g);   // 匹配一个
var n2=str.match(/^runoob/gm);  // 多行匹配
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_match_regexp6)


### s 修饰符

默认情况下的圆点 **.** 是 匹配除换行符 **\n** 之外的任何字符，加上 s 之后, **.** 中包含换行符 **\n**。


![](https://www.runoob.com/wp-content/uploads/2020/08/5CDFC964-F0C4-4ADE-80F3-17FB4748DE14.jpg)


s 修饰符实例如下：


## 实例


在字符串中查找:


```regex
var str="google\nrunoob\ntaobao";
var n1=str.match(/google./);   // 没有使用 s，无法匹配\n
var n2=str.match(/runoob./s);  // 使用 s，匹配\n
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_match_regexp5)


---

## 扩展说明


语言特定修饰符补充表：**



| 语言 | 特有修饰符 | 描述 |
| --- | --- | --- |
| PHP | A | 锚定模式到字符串开头 |
|  | D | $仅匹配字符串结尾（不包括结尾换行） |
|  | U | 反转量词的贪婪性（使所有量词变为非贪婪） |
| Python | re.A | 使\w,\W,\b,\B等仅匹配ASCII字符 |
|  | re.L | 根据本地化设置确定\w,\W等的含义 |
| JS(ES2022) | d | 为匹配结果生成indices属性（包含匹配位置的起止索引） |



**修饰符组合示例表：**



| 组合 | 效果 |
| --- | --- |
| gi | 全局匹配+忽略大小写（如查找所有格式的"email"单词） |
| ims | 忽略大小写+多行模式+点号匹配换行符（常用于日志分析） |
| gu | 全局匹配+Unicode支持（如查找所有Unicode表情符号） |



**内联修饰符表（PCRE/Perl风格）：**



| 语法 | 作用范围 | 示例 |
| --- | --- | --- |
| (?i) | 启用忽略大小写 | a(?i)bc → 匹配 "aBc"、"aBC" |
| (?-i) | 禁用忽略大小写 | a(?i)b(?-i)c → 只匹配 "aBc" |
| (?i:...) | 仅对括号内生效 | a(?i:b)c → 匹配 "aBc"、"abc" |


    **

注意：不同语言对修饰符的实现可能存在差异，建议使用时参考具体语言的文档。










	  AI 思考中...





			** [正则表达式 – 示例](https://www.runoob.com/regexp-example.html)
			[正则表达式 – 使用总结](https://www.runoob.com/regexp-usage-summary.html) **













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
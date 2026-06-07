# 正则表达式 - 位置匹配

- Source: https://www.runoob.com/regexp/regexp-positional-matching.html

位置匹配（也称为锚定或边界匹配）是指匹配字符串中的特定位置，而不是实际的字符。与普通字符匹配不同，位置匹配不消耗任何字符，它只是指定匹配必须发生的位置。


### 为什么需要位置匹配


- **精准定位**：可以精确指定匹配发生的位置
- **效率提升**：避免不必要的全文搜索
- **模式验证**：检查字符串是否符合特定格式要求


---


## 常用位置匹配元字符


### 1、行首与行尾匹配


#### ^ - 匹配行首


## 实例


```regex
// 匹配以"Hello"开头的行
const pattern = /^Hello/;
console.log(pattern.test("Hello World")); // true
console.log(pattern.test("Say Hello"));   // false
```


#### $ - 匹配行尾


## 实例


```regex
// 匹配以"World"结尾的行
const pattern = /World$/;
console.log(pattern.test("Hello World")); // true
console.log(pattern.test("World Peace")); // false
```


### 2、单词边界匹配


#### \b - 匹配单词边界


单词边界是指`\w`（[a-zA-Z0-9_]）和`\W`之间的位置，或字符串的开始/结束位置。


## 实例


```regex
// 匹配独立的"cat"单词
const pattern = /\bcat\b/;
console.log(pattern.test("cat"));        // true
console.log(pattern.test("concatenate")); // false
console.log(pattern.test("a cat"));      // true
```


#### \B - 匹配非单词边界


## 实例


```regex
// 匹配不在单词边界的"cat"
const pattern = /\Bcat\B/;
console.log(pattern.test("concatenate")); // true
console.log(pattern.test("cat"));        // false
```


### 3、其他位置匹配


#### \A 和 \Z（某些语言支持）


- `\A`：匹配字符串开头（不同于`^`，不受多行模式影响）
- `\Z`：匹配字符串结尾或结尾的换行符之前


---


## 位置匹配的实际应用


### 1. 验证输入格式


## 实例


```regex
// 验证手机号码（以1开头，共11位数字）
const phonePattern = /^1\d{10}$/;
console.log(phonePattern.test("13800138000")); // true
console.log(phonePattern.test("a13800138000")); // false
```


### 2. 提取特定位置的单词


## 实例


```regex
// 提取每行第一个单词
const text = "Apple Banana\nCherry Date";
const firstWords = text.match(/^\w+/gm);
console.log(firstWords); // ["Apple", "Cherry"]
```


### 3. 替换特定位置的文本


## 实例


```regex
// 在每个段落开头添加"> "
const text = "First line\nSecond line";
const result = text.replace(/^/gm, "> ");
console.log(result);
// > First line
// > Second line
```


---


## 高级位置匹配技巧


### 1. 多行模式下的位置匹配


使用 `m` 标志（多行模式）改变 `^` 和 `$` 的行为：


## 实例


```regex
const text = "Line 1\nLine 2\nLine 3";
// 普通模式
console.log(text.match(/^Line \d/g)); // ["Line 1"]
// 多行模式
console.log(text.match(/^Line \d/gm)); // ["Line 1", "Line 2", "Line 3"]
```


### 2. 前后断言（Lookaround）


虽然不是严格的位置匹配，但前后断言可以帮助实现更复杂的位置条件：


#### 正向先行断言（?=）


## 实例


```regex
// 匹配后面跟着"px"的数字
const pattern = /\d+(?=px)/;
console.log(pattern.exec("12px")); // ["12"]
```


#### 负向先行断言（?!）


## 实例


```regex
// 匹配后面不跟着"px"的数字
const pattern = /\d+(?!px)/;
console.log(pattern.exec("12em")); // ["12"]
```


---


## 常见错误与注意事项


- **混淆`^`在字符组中的用法**： - `[^abc]`表示"非a、b、c的字符" - `^abc`表示"以abc开头的字符串"
- **忽略多行模式的影响**： - 默认情况下`^`和`$`匹配整个字符串的开头和结尾 - 多行模式下它们匹配每行的开头和结尾
- **边界匹配不消耗字符**：
```
// 这个模式不会匹配任何内容，因为\b不消耗字符
const pattern = /\b\b/;
```


---


## 练习挑战


- 编写一个正则表达式，匹配所有以"Chapter"开头，后跟1-2位数字的字符串
- 创建一个模式，匹配字符串中所有独立的"the"单词（不匹配"there"中的"the"）
- 写一个正则表达式，验证字符串是否是一个合法的URL（以http://或https://开头）


---


## 总结要点


| 元字符 | 描述 | 示例 |
| --- | --- | --- |
| ^ | 匹配行/字符串开头 | ^Start |
| $ | 匹配行/字符串结尾 | end$ |
| \b | 匹配单词边界 | \bword\b |
| \B | 匹配非单词边界 | \Bword\B |
| \A | 匹配字符串开头（某些语言） | \AStart |
| \Z | 匹配字符串结尾（某些语言） | end\Z |


掌握位置匹配可以显著提升正则表达式的精确度和效率。记住：


- 位置匹配不消耗字符，只指定匹配发生的位置
- 合理使用边界匹配可以避免不必要的全文搜索
- 多行模式会改变 `^` 和 `$` 的行为









	  AI 思考中...





			** [正则表达式 – 测验](https://www.runoob.com/regexp-quiz.html)
			[正则表达式 – 分组和引用](https://www.runoob.com/regexp-grouping-quoting.html) **













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
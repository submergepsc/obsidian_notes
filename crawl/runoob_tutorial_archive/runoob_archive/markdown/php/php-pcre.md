# PHP 正则表达式(PCRE)

- Source: https://www.runoob.com/php/php-pcre.html

正则表达式(regular expression)描述了一种字符串匹配的模式，可以用来检查一个串是否含有某种子串、将匹配的子串做替换或者从某个串中取出符合某个条件的子串等。


更多正则表达式的内容可参考我们的：[正则表达式 - 教程](https://www.runoob.com/../regexp/regexp-tutorial.html)。


PHP 中使用正则表达式主要通过一组内置的函数，其中最常用的是:


- `preg_match()`: 在字符串中搜索匹配的模式，只返回第一个匹配项。
- `preg_match_all()`: 在字符串中搜索匹配的模式，返回所有匹配项。
- `preg_replace()`: 在字符串中搜索匹配的模式，然后进行替换。


### preg_match() 函数


preg_match() 函数用于在字符串中搜索匹配的模式，只返回第一个匹配项。


```
preg_match(pattern, subject, matches)
```


**参数说明：**



- pattern：正则表达式模式。
- subject：要搜索的字符串。
- matches：可选参数，用于存储匹配的结果。


## 实例


```php
<?php
$str = "Hello, World!";
$pattern = "/Hello/";
if (preg_match($pattern, $str, $matches)) {
    echo "匹配成功!" . PHP_EOL;
    print_r($matches);
} else {
    echo "没有匹配到!";
}
?>
```


以上代码输出结果为：


```
匹配成功!
Array
(
    [0] => Hello
)
```


### preg_match_all() 函数


preg_match_all() 函数用于在字符串中搜索匹配的模式，返回所有匹配项。


```
preg_match_all(pattern, subject, matches)
```


**参数说明：**


- 用于在字符串中搜索匹配的模式，返回所有匹配项。
- `pattern`：正则表达式模式。
- `subject`：要搜索的字符串。
- `matches`：用于存储所有匹配结果的数组。


## 实例


```php
<?php
$str = "The cat and the hat";
$pattern = "/[aeiou]/";
if (preg_match_all($pattern, $str, $matches)) {
    echo "匹配的元音字母: " . implode(", ", $matches[0]);
} else {
    echo "没有匹配到!";
}
?>
```


以上代码输出结果为：


```
匹配的元音字母: e, a, a, e, a
```





### preg_replace() 函数


preg_replace() 函数用于在字符串中搜索匹配的模式，然后进行替换。


```
preg_replace(pattern, replacement, subject)
```


**参数说明：**


- pattern：正则表达式模式。
- replacement：替换的字符串。
- subject：要搜索的字符串。


## 实例


```php
<?php
$str = "I love PHP";
$pattern = "/PHP/";
$replacement = "RUNOOB";
$new_str = preg_replace($pattern, $replacement, $str);
echo "替换后的字符串: " . $new_str;
?>
```


以上代码输出结果为：


```
替换后的字符串: I love RUNOOB
```




---


## PCRE 函数


PHP 中我们可以使用 PCRE 扩展来匹配字符串的模式。


| 函数 | 描述 |
| --- | --- |
| preg_filter | 执行一个正则表达式搜索和替换 |
| preg_grep | 返回匹配模式的数组条目 |
| preg_last_error | 返回最后一个PCRE正则执行产生的错误代码 |
| preg_match_all | 执行一个全局正则表达式匹配 |
| preg_match | 执行一个正则表达式匹配 |
| preg_quote | 转义正则表达式字符 |
| preg_replace_callback_array | 执行一个正则表达式搜索并且使用一个回调进行替换 |
| preg_replace_callback | 执行一个正则表达式搜索并且使用一个回调进行替换 |
| preg_replace | 执行一个正则表达式的搜索和替换 |
| preg_split | 通过一个正则表达式分隔字符串 |


---


## PREG 常量


| 常量 | 描述 | 自哪个版本起 |
| --- | --- | --- |
| PREG_PATTERN_ORDER | 结果按照"规则"排序，仅用于preg_match_all()， 即$matches[0]是完整规则的匹配结果， $matches[1]是第一个子组匹配的结果，等等。 | since |
| PREG_SET_ORDER | 结果按照"集合"排序，仅用于preg_match_all()， 即$matches[0]保存第一次匹配结果的所有结果(包含子组)信息, $matches[1]保存第二次的结果信息，等等。 |  |
| PREG_OFFSET_CAPTURE | 查看PREG_SPLIT_OFFSET_CAPTURE的描述。 | 4.3.0 |
| PREG_SPLIT_NO_EMPTY | 这个标记告诉 preg_split() 进返回非空部分。 |  |
| PREG_SPLIT_DELIM_CAPTURE | 这个标记告诉 preg_split() 同时捕获括号表达式匹配到的内容。 | 4.0.5 |
| PREG_SPLIT_OFFSET_CAPTURE | 如果设置了这个标记，每次出现的匹配子串的偏移量也会被返回。注意，这会改变返回数组中的值， 每个元素都是由匹配子串作为第0个元素，它相对目标字符串的偏移量作为第1个元素的数组。这个 标记只能用于 preg_split()。 | 4.3.0 |
| PREG_NO_ERROR | 没有匹配错误时调用 preg_last_error() 返回。 | 5.2.0 |
| PREG_INTERNAL_ERROR | 如果有PCRE内部错误时调用 preg_last_error() 返回。 | 5.2.0 |
| PREG_BACKTRACK_LIMIT_ERROR | 如果调用回溯限制超出，调用preg_last_error()时返回。 | 5.2.0 |
| PREG_RECURSION_LIMIT_ERROR | 如果递归限制超出，调用preg_last_error()时返回。 | 5.2.0 |
| PREG_BAD_UTF8_ERROR | 如果最后一个错误时由于异常的utf-8数据(仅在运行在 UTF-8 模式正则表达式下可用)。 导致的，调用preg_last_error()返回。 | 5.2.0 |
| PREG_BAD_UTF8_OFFSET_ERROR | 如果偏移量与合法的urf-8代码不匹配(仅在运行在 UTF-8 模式正则表达式下可用)。 调用preg_last_error()返回。 | 5.3.0 |
| PCRE_VERSION | PCRE版本号和发布日期(比如： "7.0 18-Dec-2006")。 | 5.2.4 |








	  AI 思考中...





			** [PHP 面向对象](https://www.runoob.com/php-oop.html)
			[PHP preg_filter() 函数](https://www.runoob.com/php-preg_filter.html) **













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
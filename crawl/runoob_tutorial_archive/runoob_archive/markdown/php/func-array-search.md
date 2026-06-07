# PHP array_search() 函数

- Source: https://www.runoob.com/php/func-array-search.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


在数组中搜索键值 "red"，并返回它的键名：


```php
<?php
$a=array("a"=>"red","b"=>"green","c"=>"blue");
echo array_search("red",$a);
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_search)


---


## 定义和用法


array_search() 函数用于在数组中搜索某个值，并返回对应的键名。如果找不到该值，则返回 false。


---


## 语法


```
array_search(mixed $needle, array $haystack, bool $strict = false): int|string|false
```


| 参数 | 描述 |
| --- | --- |
| $needle | 必需。规定在数组中搜索的键值。 |
| $haystack | 必需。规定被搜索的数组。 |
| $strict | 可选，默认是 false，只比较值，不比较类型。如果该参数被设置为 TRUE，则函数在数组中搜索数据类型和值都一致的元素。可能的值： true false - 默认 如果设置为 true，则在数组中检查给定值的类型，数字 5 和字符串 5 是不同的（参见实例 2）。 |


## 技术细节


| 返回值： | 如果在数组中找到指定的键值，则返回对应的键名，否则返回 FALSE。如果在数组中找到键值超过一次，则返回第一次找到的键值所匹配的键名。 |
| --- | --- |
| PHP 版本： | 4.0.5+ |
| 更新日志： | 如果向函数传递无效的参数，函数返回 NULL（这个适用于自 PHP 5.3.0 起的所有的 PHP 函数）。自 PHP 4.2.0 起，如果搜索失败，该函数返回 FALSE，而不是 NULL。 |


---


## 更多实例


## 实例


```php
<?php
$numbers = array(1, "2", 3);
$key = array_search(2, $numbers);        // 不启用严格模式，返回键名 1
$key_strict = array_search(2, $numbers, true);  // 启用严格模式，返回 false
?>
```


## 实例 1


在数组中搜索键值 5，并返回它的键名（注意 ""）：


```php
<?php
$a=array("a" => "5", "b" => 5, "c" => "5");
echo array_search(5,$a,true);
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_search2)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_reverse() 函数](https://www.runoob.com/func-array-reverse.html)
			[PHP array_shift() 函数](https://www.runoob.com/func-array-shift.html) **













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
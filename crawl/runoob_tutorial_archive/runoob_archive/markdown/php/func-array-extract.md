# PHP extract() 函数

- Source: https://www.runoob.com/php/func-array-extract.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


将键值 "Cat"、"Dog" 和 "Horse" 赋值给变量 $a、$b 和 $c：


```php
<?php
$a = "Original";
$my_array = array("a" => "Cat","b" => "Dog", "c" => "Horse");
extract($my_array);
echo "\$a = $a; \$b = $b; \$c = $c";
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_extract)


---


## 定义和用法


extract() 函数从数组中将变量导入到当前的符号表。


该函数使用数组键名作为变量名，使用数组键值作为变量值。针对数组中的每个元素，将在当前符号表中创建对应的一个变量。


该函数返回成功设置的变量数目。


---


## 语法


extract(*array,extract_rules,prefix*)


| 参数 | 描述 |
| --- | --- |
| array | 必需。规定要使用的数组。 |
| extract_rules | 可选。extract() 函数将检查每个键名是否为合法的变量名，同时也检查和符号表中已存在的变量名是否冲突。对不合法和冲突的键名的处理将根据此参数决定。可能的值： EXTR_OVERWRITE - 默认。如果有冲突，则覆盖已有的变量。 EXTR_SKIP - 如果有冲突，不覆盖已有的变量。 EXTR_PREFIX_SAME - 如果有冲突，在变量名前加上前缀 prefix。 EXTR_PREFIX_ALL - 给所有变量名加上前缀 prefix。 EXTR_PREFIX_INVALID - 仅在不合法或数字变量名前加上前缀 prefix。 EXTR_IF_EXISTS - 仅在当前符号表中已有同名变量时，覆盖它们的值。其它的都不处理。 EXTR_PREFIX_IF_EXISTS - 仅在当前符号表中已有同名变量时，建立附加了前缀的变量名，其它的都不处理。 EXTR_REFS - 将变量作为引用提取。导入的变量仍然引用了数组参数的值。 |
| prefix | 可选。如果 extract_rules 参数的值是 EXTR_PREFIX_SAME、EXTR_PREFIX_ALL、 EXTR_PREFIX_INVALID 或 EXTR_PREFIX_IF_EXISTS，则 prefix 是必需的。 该参数规定了前缀。前缀和数组键名之间会自动加上一个下划线。 |


## 技术细节


| 返回值： | 返回成功设置的变量数目。 |
| --- | --- |
| PHP 版本： | 4+ |
| 更新日志： | extract_rules 的值 EXTR_REFS 是在 PHP 4.3 中新增的。 extract_rules 的值 EXTR_IF_EXISTS 和 EXTR_PREFIX_IF_EXISTS 是在 PHP 4.2 中新增的。自 PHP 4.0.5 起，该函数返回成功设置的变量数目。extract_rules 的值 EXTR_PREFIX_INVALID 是在 PHP 4.0.5 中新增的。自 PHP 4.0.5 起，extract_rules 的值 EXTR_PREFIX_ALL 也包含数字变量。 |


---


## 更多实例


## 实例 1


使用所有的参数：


```php
<?php
$a = "Original";
$my_array = array("a" => "Cat", "b" => "Dog", "c" => "Horse");
extract($my_array, EXTR_PREFIX_SAME, "dup");
echo "$a = $a; $b = $b; $c = $c; $dup_a = $dup_a";?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_extract2)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP end() 函数](https://www.runoob.com/func-array-end.html)
			[PHP in_array() 函数](https://www.runoob.com/func-array-in-array.html) **













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
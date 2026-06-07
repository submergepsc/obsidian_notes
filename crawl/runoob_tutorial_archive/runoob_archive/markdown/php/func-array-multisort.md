# PHP array_multisort() 函数

- Source: https://www.runoob.com/php/func-array-multisort.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


返回一个升序排列的数组：


```php
<?php
$a=array("Dog","Cat","Horse","Bear","Zebra");
array_multisort($a);
print_r($a);
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_multisort)


---


## 定义和用法


array_multisort() 函数返回一个排序数组。您可以输入一个或多个数组。函数先对第一个数组进行排序，接着是其他数组，如果两个或多个值相同，它将对下一个数组进行排序。


注释：**字符串键名将被保留，但是数字键名将被重新索引，从 0 开始，并以 1 递增。


**注释：**您可以在每个数组后设置排序顺序和排序类型参数。如果没有设置，每个数组参数会使用默认值。


---


## 语法


array_multisort(*array1,sorting order,sorting type,array2,array3...*)

**
| 参数 | 描述 |
| --- | --- |
| array1 | 必需。规定数组。 |
| sorting order | 可选。规定排列顺序。可能的值： SORT_ASC - 默认。按升序排列 (A-Z)。 SORT_DESC - 按降序排列 (Z-A)。 |
| sorting type | 可选。规定排序类型。可能的值： SORT_REGULAR - 默认。把每一项按常规顺序排列（Standard ASCII，不改变类型）。 SORT_NUMERIC - 把每一项作为数字来处理。 SORT_STRING - 把每一项作为字符串来处理。 SORT_LOCALE_STRING - 把每一项作为字符串来处理，基于当前区域设置（可通过 setlocale() 进行更改）。 SORT_NATURAL - 把每一项作为字符串来处理，使用类似 natsort() 的自然排序。 SORT_FLAG_CASE - 可以结合（按位或）SORT_STRING 或 SORT_NATURAL 对字符串进行排序，不区分大小写。 |
| array2 | 可选。规定数组。 |
| array3 | 可选。规定数组。 |


## 技术细节


| 返回值： | 如果成功则返回 TRUE，如果失败则返回 FALSE。 |
| --- | --- |
| PHP 版本： | 4+ |
| 更新日志： | 排序类型 SORT_NATURAL 和 SORT_FLAG_CASE 是在 PHP 5.4 中新增的。排序类型 SORT_LOCALE_STRING 是在 PHP 5.3 中新增的。 |


---


## 更多实例


## 实例 1


返回一个升序排列的数组：


```php
<?php
$a1=array("Dog","Cat");
$a2=array("Fido","Missy");
array_multisort($a1,$a2);
print_r($a1);
print_r($a2);?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_multisort2)


## 实例 2


当两个值相同时如何排序：


```php
<?php
$a1=array("Dog","Dog","Cat");
$a2=array("Pluto","Fido","Missy");
array_multisort($a1,$a2);
print_r($a1);
print_r($a2);?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_multisort3)


## 实例 3


使用排序参数：


```php
<?php$a1=array("Dog","Dog","Cat");$a2=array("Pluto","Fido","Missy");array_multisort($a1,SORT_ASC,$a2,SORT_DESC);print_r($a1);print_r($a2);?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_multisort4)


## 实例 4


合并两个数组，并按数字降序排列：


```php
<?php
	$a1=array(1,30,15,7,25);$a2=array(4,30,20,41,66);$num=array_merge($a1,$a2);
	array_multisort($num,SORT_DESC,SORT_NUMERIC);print_r($num);?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_multisort5)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_merge_recursive() 函数](https://www.runoob.com/func-array-merge-recursive.html)
			[PHP array_pad() 函数](https://www.runoob.com/func-array-pad.html) **













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
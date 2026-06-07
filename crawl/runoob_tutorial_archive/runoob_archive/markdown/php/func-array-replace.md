# PHP array_replace() 函数

- Source: https://www.runoob.com/php/func-array-replace.html

[![PHP Array 参考手册](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


使用第二个数组（$a2）的值替换第一个数组（$a1）的值：


```php
<?php
	$a1=array("red","green");$a2=array("blue","yellow");
	print_r(array_replace($a1,$a2));
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_replace)


---


## 定义和用法


array_replace() 函数使用后面数组的值替换第一个数组的值。


提示：**您可以向函数传递一个数组，或者多个数组。


如果一个键存在于第一个数组 array1 同时也存在于第二个数组 array2，第一个数组 array1 中的值将被第二个数组 array2 中的值替换。如果一个键仅存在于第一个数组 array1，它将保持不变。（详见下面的实例 1）


如果一个键存在于第二个数组 array2，但是不存在于第一个数组 array1，则会在第一个数组 array1 中创建这个元素。（详见下面的实例 2）


如果传递了多个替换数组，它们将被按顺序依次处理，后面数组的值将覆盖之前数组的值。（详见下面的实例 3）


**提示：**请使用 [array_replace_recursive()](https://www.runoob.com/func-array-replace-recursive.html) 来递归地使用后面数组的值替换第一个数组的值。


---


## 语法


array_replace(*array1,array2,array3...*)

**


| 参数 | 描述 |
| --- | --- |
| array1 | 必需。指定一个数组。 |
| array2 | 可选。指定一个要替换 array1 的值的数组。 |
| array3,... | 可选。指定多个要替换 array1 和 array2, ... 的值的数组。后面数组的值将覆盖之前数组的值。 |


## 技术细节


| 返回值： | 返回被替换的数组，如果发生错误则返回 NULL。 |
| --- | --- |
| PHP 版本： | 5.3.0+ |


---


## 更多实例


## 实例 1


如果一个键存在于第一个数组 array1 同时也存在于第二个数组 array2，第一个数组 array1 中的值将被第二个数组 array2 中的值替换。如果一个键仅存在于第一个数组 array1，它将保持不变。


```php
<?php
	$a1=array("a"=>"red","b"=>"green");$a2=array("a"=>"orange","burgundy");
	print_r(array_replace($a1,$a2));?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_replace2)


## 实例 2


如果一个键存在于第二个数组 array2，但是不存在于第一个数组 array1，则会在第一个数组 array1 中创建这个元素。


```php
<?php
	$a1=array("a"=>"red","green");$a2=array("a"=>"orange","b"=>"burgundy");
	print_r(array_replace($a1,$a2));?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_replace3)


## 实例 3


使用三个数组 - 最后一个数组（$a3）将覆盖之前数组（$a1 和 $a2）：


```php
<?php
	$a1=array("red","green");$a2=array("blue","yellow");$a3=array("orange","burgundy");
	print_r(array_replace($a1,$a2,$a3));?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_replace4)


## 实例 4


使用数值键 - 如果一个键存在于第二个数组 array2，但是不存在于第一个数组 array1，则会在第一个数组 array1 中创建这个元素：


```php
<?php
	$a1=array("red","green","blue","yellow");
	$a2=array(0=>"orange",3=>"burgundy");print_r(array_replace($a1,$a2));?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_replace5)


---

[![PHP Array 参考手册](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_column() 函数](https://www.runoob.com/func-array-column.html)
			[PHP array_replace_recursive() 函数](https://www.runoob.com/func-array-replace-recursive.html) **













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
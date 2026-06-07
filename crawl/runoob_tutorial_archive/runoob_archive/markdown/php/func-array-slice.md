# PHP array_slice() 函数

- Source: https://www.runoob.com/php/func-array-slice.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


从数组的第三个元素（索引为 2）开始取出，并返回直到数组末端的所有元素：


```php
<?php
$a=array("red","green","blue","yellow","brown");
print_r(array_slice($a,2));
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_slice)


---


## 定义和用法


array_slice() 函数返回数组中的选定部分。


注释：**如果数组有字符串键名，所返回的数组将保留键名（参见实例 4）。


---


## 语法


array_slice(*array,start,length,preserve*)

**
| 参数 | 描述 |
| --- | --- |
| array | 必需。规定数组。 |
| start | 必需。数值。规定取出元素的开始位置。 0 = 第一个元素。 如果该值设置为正数，则从前往后开始取。如果该值设置为负数，则从后向前取 start 绝对值。 -2 意味着从数组的倒数第二个元素开始。 |
| length | 可选。数值。规定被返回数组的长度。 如果该值设置为整数，则返回该数量的元素。如果该值设置为负数，则函数将在举例数组末端这么远的地方终止取出。如果该值未设置，则返回从 start 参数设置的位置开始直到数组末端的所有元素。 |
| preserve | 可选。规定函数是保留键名还是重置键名。可能的值： true - 保留键名 false - 默认。重置键名 |


## 技术细节


| 返回值： | 返回数组中的选定部分。 |
| --- | --- |
| PHP 版本： | 4+ |
| 更新日志： | preserve 参数是在 PHP 5.0.2 中新增的。 |


---


## 更多实例


## 实例 1


从数组的第二个元素开始取出，并返回两个元素：


```php
<?php
$a=array("red","green","blue","yellow","brown");
print_r(array_slice($a,1,2));
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_slice2)


## 实例 2


使用负的 start 参数：


```php
<?php
$a=array("red","green","blue","yellow","brown");
print_r(array_slice($a,-2,1));
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_slice3)


## 实例 3


带有设置为 true 的 preserve 参数：


```php
<?php
// preserve 设置为 true，保留键名
$a=array("red","green","blue","yellow","brown");
print_r(array_slice($a,1,2,true));

// 不保留键名设置为 false（默认）
$a=array("red","green","blue","yellow","brown");
print_r(array_slice($a,1,2,false));

// 注意两个数组的键是不一样的
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_slice4)


## 实例 4


带有字符串和整数键名：


```php
<?php
$a=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow","e"=>"brown");
print_r(array_slice($a,1,2));

$a=array("0"=>"red","1"=>"green","2"=>"blue","3"=>"yellow","4"=>"brown");
print_r(array_slice($a,1,2));
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_slice5)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_shift() 函数](https://www.runoob.com/func-array-shift.html)
			[PHP array_splice() 函数](https://www.runoob.com/func-array-splice.html) **













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
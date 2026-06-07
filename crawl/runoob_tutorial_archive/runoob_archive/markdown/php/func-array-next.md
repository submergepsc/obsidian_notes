# PHP next() 函数

- Source: https://www.runoob.com/php/func-array-next.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


输出数组中的当前元素和下一个元素的值：


```php
<?php
$people = array("Peter", "Joe", "Glenn", "Cleveland");
echo current($people) . "<br>";
echo next($people);
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_next)


---


## 定义和用法


next() 函数将内部指针指向数组中的下一个元素，并输出。


相关的方法：


- [prev()](https://www.runoob.com/func-array-prev.html) - 将内部指针指向数组中的上一个元素，并输出。
- [current()](https://www.runoob.com/func-array-current.html) - 返回数组中的当前元素的值。
- [end()](https://www.runoob.com/func-array-end.html) - 将内部指针指向数组中的最后一个元素，并输出。
- [reset()](https://www.runoob.com/func-array-reset.html) - 将内部指针指向数组中的第一个元素，并输出。
- [each()](https://www.runoob.com/func-array-each.html) - 返回当前元素的键名和键值，并将内部指针向前移动。


---


## 语法


next(*array*)


| 参数 | 描述 |
| --- | --- |
| array | 必需。规定要使用的数组。 |


## 技术细节


| 返回值： | 如果成功则返回数组中下一个元素的值，如果没有更多的数组元素则返回 FALSE。 |
| --- | --- |
| PHP 版本： | 4+ |


---


## 更多实例


## 实例 1


所有相关方法的演示：


```php
<?php
	$people = array("Peter", "Joe", "Glenn", "Cleveland");echo
	current($people) . "<br>"; // The current element is Peterecho
	next($people) . "<br>"; // The next element of Peter is Joeecho
	current($people) . "<br>"; // Now the current element is Joeecho prev($people) . "<br>";
	// The previous element of Joe is Peterecho end($people) . "<br>"; //
	The last element is Clevelandecho prev($people) . "<br>"; // The
	previous element of Cleveland is Glennecho current($people) . "<br>"; //
	Now the current element is Glennecho reset($people) . "<br>"; // Moves
	the internal pointer to the first element of the array, which is Peter
	echo next($people) . "<br>"; // The next element of Peter is Joe
	print_r (each($people)); // Returns the key and value of the current element
	(now Joe), and moves the internal pointer forward?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_internal_pointer)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP natsort() 函数](https://www.runoob.com/func-array-natsort.html)
			[PHP pos() 函数](https://www.runoob.com/func-array-pos.html) **













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
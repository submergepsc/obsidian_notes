# PHP array_intersect_ukey() 函数

- Source: https://www.runoob.com/php/func-array-intersect-ukey.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


比较两个数组的**键名**（使用用户自定义函数比较键名），并返回交集：


```php
<?php
	function myfunction($a,$b){if ($a===$b)  {
	return 0;  }  return ($a>$b)?1:-1;}
	$a1=array("a"=>"red","b"=>"green","c"=>"blue");$a2=array("a"=>"blue","b"=>"black","e"=>"blue");$result=array_intersect_ukey($a1,$a2,"myfunction");print_r($result);?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_intersect_ukey)


---


## 定义和用法


array_intersect_ukey() 函数用于比较两个（或更多个）数组的键名** ，并返回交集。


**注释：**该函数使用用户自定义函数比较键名！


该函数比较两个（或更多个）数组的键名，并返回一个交集数组，该数组包括了所有在被比较的数组（*array1*）中，同时也在任何其他参数数组（*array2* 或 *array3* 等等）中的键名。

*array3*, etc.

---


## 语法


array_intersect_ukey(*array1,array2,array3...,myfunction*)


**
| 参数 | 描述 |
| --- | --- |
| array1 | 必需。与其他数组进行比较的第一个数组。 |
| array2 | 必需。与第一个数组进行比较的数组。 |
| array3,... | 可选。与第一个数组进行比较的其他数组。 |
| myfunction | 必需。一个定义了可调用比较函数的字符串。如果第一个参数 第二个参数，相应地比较函数必须返回一个 0 的整数。 |


## 技术细节


| 返回值： | 返回一个交集数组，该数组包括了所有在被比较的数组（array1）中，同时也在任何其他参数数组（array2 或 array3 等等）中的键名。 |
| --- | --- |
| PHP 版本： | 5.1.0+ |


## 更多实例


## 实例 1


比较三个数组的键名**（使用用户自定义函数比较键名），并返回交集：


```php
<?php
	function myfunction($a,$b){if ($a===$b)  {
	return 0;  }  return ($a>$b)?1:-1;}
	$a1=array("a"=>"red","b"=>"green","c"=>"blue");$a2=array("a"=>"black","b"=>"yellow","d"=>"brown");
	$a3=array("e"=>"purple","f"=>"white","a"=>"gold");$result=array_intersect_ukey($a1,$a2,$a3,"myfunction");
	print_r($result);?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_intersect_ukey2)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_intersect_uassoc() 函数](https://www.runoob.com/func-array-intersect-uassoc.html)
			[PHP array_key_exists() 函数](https://www.runoob.com/func-array-key-exists.html) **













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
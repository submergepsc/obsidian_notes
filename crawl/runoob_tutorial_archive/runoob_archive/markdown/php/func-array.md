# PHP array() 函数

- Source: https://www.runoob.com/php/func-array.html

[![PHP Array 参考手册](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


创建名为 $cars 的数值数组，赋三个元素给它，并打印包含数组值的文本：


```php
<?php
$cars=array("Volvo","BMW","Toyota");
echo "I like " . $cars[0] . ", " . $cars[1] . " and " . $cars[2] . ".";
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array)


---


## 定义和用法


array() 函数用于创建数组。


在 PHP 中，有三种类型的数组：


- **数值数组** - 带有数字 ID 键的数组
- **关联数组** - 带有指定的键的数组，每个键关联一个值
- **多维数组** - 包含一个或多个数组的数组


---


## 语法


数值数组的语法：


	array(*value1,value2,value3,etc.*);


关联数组的语法：


	array(*key=>value,key=>value,key=>value,etc.*);


| 参数 | 描述 |
| --- | --- |
| key | 规定键名（数值或字符串）。 |
| value | 规定键值。 |


## 技术细节


| 返回值： | 返回参数的数组。 |
| --- | --- |
| PHP 版本： | 4+ |
| 更新日志： | 自 PHP 5.4 起，可以使用短数组语法，用 [] 代替 array()。 例如，用 $cars=["Volvo","BMW"]; 代替 $cars=array("Volvo","BMW"); |


---


## 更多实例


## 实例 1


创建名为 $age 的关联数组：


```php
<?php
	$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");echo "Peter is " .
	$age['Peter'] . " years old.";?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array2)


## 实例 2


遍历和打印数值数组的值：


```php
<?php
	$cars=array("Volvo","BMW","Toyota");
	$arrlength=count($cars);for($x=0;$x<$arrlength;$x++)  {
	echo $cars[$x];  echo "<br>";  }?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array3)


## 实例 3


遍历和打印关联数组的值：


```php
<?php$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");foreach($age as $x=>$x_value)  {  echo "Key=" . $x .
	", Value=" . $x_value;  echo "<br>";  }?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array4)


## 实例 4


创建多维数组：


```php
<?php// 一个二维数组$cars=array  (
	array("Volvo",100,96),  array("BMW",60,59),
	array("Toyota",110,100)  );?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array5)


---

[![PHP Array 参考手册](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP 5 Timezones](https://www.runoob.com/php-ref-timezones.html)
			[PHP array_change_key_case() 函数](https://www.runoob.com/func-array-change-key-case.html) **













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
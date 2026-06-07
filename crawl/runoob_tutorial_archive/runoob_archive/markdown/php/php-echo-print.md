# PHP 5 echo 和 print 语句

- Source: https://www.runoob.com/php/php-echo-print.html

---


在 PHP 中有两个基本的输出方式： echo 和 print。


本章节中我们会详细讨论两个语句的用法，并在实例中演示如何使用 echo 和 print。


---


## PHP echo 和 print 语句


echo 和 print 区别:


- echo - 可以输出一个或多个字符串
- print - 只允许输出一个字符串，返回值总为 1


**提示：**echo 输出的速度比 print 快， echo 没有返回值，print有返回值1。


---


## PHP echo 语句


echo 是一个语言结构，使用的时候可以不用加括号，也可以加上括号： echo 或 echo()。


**显示字符串**


下面的实例演示了如何使用 echo 命令输出字符串（字符串可以包含 HTML 标签）：


## 实例


```php
<?php
echo "<h2>PHP 很有趣!</h2>";
echo "Hello world!<br>";
echo "我要学 PHP!<br>";
echo "这是一个", "字符串，", "使用了", "多个", "参数。";
?>
```


**[尝试一下 »](https://www.runoob.com/try/showphp.php?filename=demo_echo1)


显示变量**


下面的实例演示了如何使用 echo 命令输出变量和字符串：


## 实例


```php
<?php
$txt1="学习 PHP";
$txt2="RUNOOB.COM";
$cars=array("Volvo","BMW","Toyota");

echo $txt1;
echo "<br>";
echo "在 $txt2 学习 PHP ";
echo "<br>";
echo "我车的品牌是 {$cars[0]}";
?>
```


**[尝试一下 »](https://www.runoob.com/try/showphp.php?filename=demo_echo2)


---


## PHP print 语句


print 同样是一个语言结构，可以使用括号，也可以不使用括号： print 或 print()。


显示字符串**


下面的实例演示了如何使用 print 命令输出字符串（字符串可以包含 HTML 标签）：


## 实例


```php
<?php
print "<h2>PHP 很有趣!</h2>";
print "Hello world!<br>";
print "我要学习 PHP!";
?>
```


**[尝试一下 »](https://www.runoob.com/try/showphp.php?filename=demo_print1)


显示变量**


下面的实例演示了如何使用 print 命令输出变量和字符串：


## 实例


```php
<?php
$txt1="学习 PHP";
$txt2="RUNOOB.COM";
$cars=array("Volvo","BMW","Toyota");

print $txt1;
print "<br>";
print "在 $txt2 学习 PHP ";
print "<br>";
print "我车的品牌是 {$cars[0]}";
?>
```


[尝试一下 »](https://www.runoob.com/try/showphp.php?filename=demo_print2)








	  AI 思考中...





			** [PDOStatement::setFetchMode](https://www.runoob.com/pdostatement-setfetchmode.html)
			[PHP 数据类型](https://www.runoob.com/php-datatypes.html) **
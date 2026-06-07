# PHP 函数

- Source: https://www.runoob.com/php/php-functions.html

---


PHP 的真正威力源自于它的函数。


在 PHP 中，提供了超过 1000 个内建的函数。


---


## PHP 内建函数


如需查看所有数组函数的完整参考手册和实例，请访问我们的 [PHP 参考手册](https://www.runoob.com/php-ref-array.html)。


---


## PHP 函数


在本章中，我们将为您讲解如何创建自己的函数。


如要在页面加载时执行脚本，您可以把它放到函数里。


函数是通过调用函数来执行的。


你可以在页面的任何位置调用函数。


---


## 创建 PHP 函数


函数是通过调用函数来执行的。


## 语法


```php
<?php
function functionName()
{
    // 要执行的代码
}
?>
```


PHP 函数准则：


- 函数的名称应该提示出它的功能
- 函数名称以字母或下划线开头（不能以数字开头）


### 实例


一个简单的函数，在其被调用时能输出我的名称：


## 实例


```php
<?php
function writeName()
{
    echo "Kai Jim Refsnes";
}

echo "My name is ";
writeName();
?>
```


输出：


```
My name is Kai Jim Refsnes
```


---


## PHP 函数 - 添加参数


为了给函数添加更多的功能，我们可以添加参数，参数类似变量。


参数就在函数名称后面的一个括号内指定。


### 实例 1


下面的实例将输出不同的名字，但姓是相同的：


## 实例


```php
<?php
function writeName($fname)
{
    echo $fname . " Refsnes.<br>";
}

echo "My name is ";
writeName("Kai Jim");
echo "My sister's name is ";
writeName("Hege");
echo "My brother's name is ";
writeName("Stale");
?>
```


输出：


```
My name is Kai Jim Refsnes.
My sister's name is Hege Refsnes.
My brother's name is Stale Refsnes.
```


### 实例 2


下面的函数有两个参数：


## 实例


```php
<?php
function writeName($fname,$punctuation)
{
    echo $fname . " Refsnes" . $punctuation . "<br>";
}

echo "My name is ";
writeName("Kai Jim",".");
echo "My sister's name is ";
writeName("Hege","!");
echo "My brother's name is ";
writeName("Ståle","?");
?>
```


输出：


```
My name is Kai Jim Refsnes.
My sister's name is Hege Refsnes!
My brother's name is Ståle Refsnes?
```


---


## PHP 函数 - 返回值


如需让函数返回一个值，请使用 return 语句。


## 实例


```php
<?php
function add($x,$y)
{
    $total=$x+$y;
    return $total;
}

echo "1 + 16 = " . add(1,16);
?>
```


输出：


```
1 + 16 = 17
```


---


## PHP 变量函数


变量函数是指在 PHP 中，将一个变量作为函数名来调用的函数。


变量函数可以让我们在运行时动态地决定调用哪个函数。


## 实例


```php
<?php
function foo() {
    echo "In foo()<br />\n";
}

function bar($arg = '')
{
    echo "In bar(); argument was '$arg'.<br />\n";
}

// 使用 echo 的包装函数
function echoit($string)
{
    echo $string;
}

$func = 'foo';
$func();        // 调用 foo()

$func = 'bar';
$func('test');  // 调用 bar()

$func = 'echoit';
$func('test');  // 调用 echoit()
?>
```


也可以用变量函数的语法来调用一个对象的方法。


## 实例


```php
<?php
class Foo
{
    function Variable()
    {
        $name = 'Bar';
        $this->$name(); // 调用 Bar() 方法
    }

    function Bar()
    {
        echo "This is Bar";
    }
}

$foo = new Foo();
$funcname = "Variable";
$foo->$funcname();  // 调用 $foo->Variable()

?>
```










	  AI 思考中...





			** [PHP For 循环](https://www.runoob.com/php-looping-for.html)
			[PHP 表单](https://www.runoob.com/php-forms.html) **
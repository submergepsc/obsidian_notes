# PHP Switch 语句

- Source: https://www.runoob.com/php/php-switch.html

---


switch 语句用于根据多个不同条件执行不同动作。


---


## PHP Switch 语句


如果您希望**有选择地执行若干代码块之一**，请使用 switch 语句。


## 语法


```php
<?php
switch (expression) {
    case value1:
        // 代码块1
        break;
    case value2:
        // 代码块2
        break;
    // 更多的 case 语句
    default:
        // 如果没有匹配的值
}
?>
```


**参数说明：**


- `expression` 是要被比较的表达式。
- `case value:` 是可能的值，如果 `expression` 的值等于某个 `case` 的值，就执行相应的代码块。
- `break;` 用于终止 `switch` 语句，防止继续执行下一个 `case`。
- `default:` 是可选的，用于指定当没有匹配的 `case` 时执行的代码块。


**工作原理：**首先对一个简单的表达式 *n*（通常是变量）进行一次计算。将表达式的值与结构中每个 case 的值进行比较。如果存在匹配，则执行与 case 关联的代码。代码执行后，使用 **break** 来阻止代码跳入下一个 case 中继续执行。**default** 语句用于不存在匹配（即没有 case 为真）时执行。


## 实例


```php
<?php
$favcolor="red";
switch ($favcolor)
{
case "red":
    echo "你喜欢的颜色是红色!";
    break;
case "blue":
    echo "你喜欢的颜色是蓝色!";
    break;
case "green":
    echo "你喜欢的颜色是绿色!";
    break;
default:
    echo "你喜欢的颜色不是 红, 蓝, 或绿色!";
}
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_switch)








	  AI 思考中...





			** [PHP If…Else 语句](https://www.runoob.com/php-if-else.html)
			[PHP 数组](https://www.runoob.com/php-arrays.html) **
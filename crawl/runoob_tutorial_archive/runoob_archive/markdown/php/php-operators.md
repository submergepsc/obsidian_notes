# PHP 运算符

- Source: https://www.runoob.com/php/php-operators.html

---


本章节我们将讨论 PHP 中不同运算符的应用。


在 PHP 中，赋值运算符 **=** 用于给变量赋值。


在 PHP 中，算术运算符 **+** 用于把值加在一起。


---


## PHP 算术运算符


| 运算符 | 名称 | 描述 | 实例 | 结果 |
| --- | --- | --- | --- | --- |
| x + y | 加 | x 和 y 的和 | 2 + 2 | 4 |
| x - y | 减 | x 和 y 的差 | 5 - 2 | 3 |
| x * y | 乘 | x 和 y 的积 | 5 * 2 | 10 |
| x / y | 除 | x 和 y 的商 | 15 / 5 | 3 |
| x % y | 模（除法的余数） | x 除以 y 的余数 | 5 % 210 % 810 % 2 | 120 |
| -x | 设置负数 | 取 x 的相反符号 |
```
<?php
$x = 2;
echo -$x;
?>
```
 | -2 |
| ~x | 取反 | x 取反，按二进制位进行"取反"运算。运算规则：
```
~1=-2;
~0=-1;
```
 |
```
<?php
$x = 2;
echo ~$x;
?>
```
 | -3 |
| a . b | 并置 | 连接两个字符串 | "Hi" . "Ha" | HiHa |


以下实例演示了使用不同算术运算符得到的不同结果：


## 实例


```php
<?php
$x=10;
$y=6;
echo ($x + $y); // 输出16
echo '<br>';  // 换行

echo ($x - $y); // 输出4
echo '<br>';  // 换行

echo ($x * $y); // 输出60
echo '<br>';  // 换行

echo ($x / $y); // 输出1.6666666666667
echo '<br>';  // 换行

echo ($x % $y); // 输出4
echo '<br>';  // 换行

echo -$x;
?>
```


**[尝试一下 »](https://www.runoob.com/try/showphp.php?filename=demo_operator_arithmetic)


PHP7+ 版本新增整除运算符 intdiv()**，该函数返回值为第一个参数除于第二个参数的值并取整（向下取整），使用实例：


## 实例



```php
<?php
var_dump(intdiv(10, 3));
?>
```


以上实例会输出：


```
int(3)
```


---


## PHP 赋值运算符


在 PHP 中，基本的赋值运算符是 **=**。它意味着左操作数被设置为右侧表达式的值。也就是说，**$x = 5** 的值是 5。


| 运算符 | 等同于 | 描述 |
| --- | --- | --- |
| x = y | x = y | 左操作数被设置为右侧表达式的值 |
| x += y | x = x + y | 加 |
| x -= y | x = x - y | 减 |
| x *= y | x = x * y | 乘 |
| x /= y | x = x / y | 除 |
| x %= y | x = x % y | 模（除法的余数） |
| a .= b | a = a . b | 连接两个字符串 |


以下实例演示了使用不同赋值运算符得到的不同结果：


## 实例


```php
<?php
$x=10;
echo $x; // 输出10

$y=20;
$y += 100;
echo $y; // 输出120

$z=50;
$z -= 25;
echo $z; // 输出25

$i=5;
$i *= 6;
echo $i; // 输出30

$j=10;
$j /= 5;
echo $j; // 输出2

$k=15;
$k %= 4;
echo $k; // 输出3
?>
```


**[尝试一下 »](https://www.runoob.com/try/showphp.php?filename=demo_operator_assignment)


以下实例演示了使用不同字符串运算符得到的相同结果：


## 实例


```php
<?php
$a = "Hello";
$b = $a . " world!";
echo $b; // 输出Hello world!

$x="Hello";
$x .= " world!";
echo $x; // 输出Hello world!
?>
```


[尝试一下 »](https://www.runoob.com/try/showphp.php?filename=demo_operator_string)


---


## PHP 递增/递减运算符


| 运算符 | 名称 | 描述 |
| --- | --- | --- |
| ++ x | 预递增 | x 加 1，然后返回 x |
| x ++ | 后递增 | 返回 x，然后 x 加 1 |
| -- x | 预递减 | x 减 1，然后返回 x |
| x -- | 后递减 | 返回 x，然后 x 减 1 |


以下实例演示了使用递增/递减运算符得到的结果：


## 实例


```php
<?php
$x=10;
echo ++$x; // 输出11

$y=10;
echo $y++; // 输出10

$z=5;
echo --$z; // 输出4

$i=5;
echo $i--; // 输出5
?>
```


[尝试一下 »](https://www.runoob.com/try/showphp.php?filename=demo_operator_increment)


---


## PHP 比较运算符


比较操作符可以让您比较两个值：


| 运算符 | 名称 | 描述 | 实例 |
| --- | --- | --- | --- |
| x == y | 等于 | 如果 x 等于 y，则返回 true | 5==8 返回 false |
| x === y | 绝对等于 | 如果 x 等于 y，且它们类型相同，则返回 true | 5==="5" 返回 false |
| x != y | 不等于 | 如果 x 不等于 y，则返回 true | 5!=8 返回 true |
| x y | 不等于 | 如果 x 不等于 y，则返回 true | 58 返回 true |
| x !== y | 不绝对等于 | 如果 x 不等于 y，或它们类型不相同，则返回 true | 5!=="5" 返回 true |
| x > y | 大于 | 如果 x 大于 y，则返回 true | 5>8 返回 false |
| x = y | 大于等于 | 如果 x 大于或者等于 y，则返回 true | 5>=8 返回 false |
| x **。组合比较运算符可以轻松实现两个变量的比较，当然不仅限于数值类数据的比较。


语法格式如下：


```
$c = $a <=> $b;
```


解析如下：


- 如果** $a > $b**, 则 **$c** 的值为 **1**。
- 如果 **$a == $b**, 则 **$c** 的值为 **0**。
- 如果 **$a  | 位运算符 |
| 无 | == != === !== | 比较运算符 |
| 左 | & | 位运算符和引用 |
| 左 | ^ | 位运算符 |
| 左 | \| | 位运算符 |
| 左 | && | 逻辑运算符 |
| 左 | \|\| | 逻辑运算符 |
| 左 | ? : | 三元运算符 |
| 右 | = += -= *= /= .= %= &= \|= ^= >= => | 赋值运算符 |
| 左 | and | 逻辑运算符 |
| 左 | xor | 逻辑运算符 |
| 左 | or | 逻辑运算符 |
| 左 | , | 多处用到 |


运算符优先级中，or 和 ||，&& 和 and 都是逻辑运算符，效果一样，但是其优先级却不一样。


## 实例


```php
<?php
// 优先级： &&  >  =  >  and
// 优先级： ||  >  =  >  or

$a = 3;
$b = false;
$c = $a or $b;
var_dump($c);          // 这里的 $c 为 int 值3，而不是 boolean 值 true
$d = $a || $b;
var_dump($d);          //这里的 $d 就是 boolean 值 true
?>
```


以上实例输出结果为：


```
int(3)
bool(true)
```


### 括号的使用


我们通过括号的配对来明确标明运算顺序，而非靠运算符优先级和结合性来决定，通常能够增加代码的可读性。


## 实例


```php
<?php
// 括号优先运算

$a = 1;
$b = 2;
$c = 3;
$d = $a + $b * $c;
echo $d;
echo "\n";
$e = ($a + $b) * $c;  // 使用括号
echo $e;
echo "\n";
?>
```


以上实例输出结果为：


```
7
9
```









	  AI 思考中...





			** [PHP 字符串变量](https://www.runoob.com/php-string.html)
			[PHP If…Else 语句](https://www.runoob.com/php-if-else.html) **
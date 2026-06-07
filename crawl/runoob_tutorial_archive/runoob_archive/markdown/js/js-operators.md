# JavaScript 运算符

- Source: https://www.runoob.com/js/js-operators.html

---


**运算符 = 用于赋值。**


**运算符 + 用于加值。**


---


运算符 = 用于给 JavaScript 变量赋值。


算术运算符 **+** 用于把值加起来。


## 实例


指定变量值，并将值相加：


```javascript
y=5;
z=2;
x=y+z;
```


在以上语句执行后，*x* 的值是：


```javascript
7
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_operators1)


---


## JavaScript 算术运算符


与/或**值之间的算术运算。


| 运算符 | 描述 | 例子 | x 运算结果 | y 运算结果 | 在线实例 | | --- | --- | --- | --- | --- | --- | | + | 加法 | x=y+2 | 7 | 5 | 实例 » | | - | 减法 | x=y-2 | 3 | 5 | 实例 » | | * | 乘法 | x=y*2 | 10 | 5 | 实例 » | | / | 除法 | x=y/2 | 2.5 | 5 | 实例 » | | % | 取模（余数） | x=y%2 | 1 | 5 | 实例 » | | ++ | 自增 | x=++y | 6 | 6 | 实例 » | | x=y++ | 5 | 6 | 实例 » | | | | -- | 自减 | x=--y | 4 | 4 | 实例 » | | x=y-- | 5 | 4 | 实例 » | | | ** --- ## JavaScript 赋值运算符 赋值运算符用于给 JavaScript 变量赋值。


给定 x=10 **和** y=5**，下面的表格解释了赋值运算符：


| 运算符 | 例子 | 等同于 | 运算结果 | 在线实例 |
| --- | --- | --- | --- | --- |
| = | x=y |  | x=5 | 实例 » |
| += | x+=y | x=x+y | x=15 | 实例 » |
| -= | x-=y | x=x-y | x=5 | 实例 » |
| *= | x*=y | x=x*y | x=50 | 实例 » |
| /= | x/=y | x=x/y | x=2 | 实例 » |
| %= | x%=y | x=x%y | x=0 | 实例 » |

**
---


## 用于字符串的 + 运算符


+ 运算符用于把文本值或字符串变量加起来（连接起来）。


如需把两个或多个字符串变量连接起来，请使用 **+** 运算符。


## 实例


如需把两个或多个字符串变量连接起来，请使用 **+** 运算符：


```javascript
txt1="What a very";
txt2="nice day";
txt3=txt1+txt2;
```


*txt3* 运算结果如下:


```javascript
What a verynice day
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_operators2)


要想在两个字符串之间增加空格，需要把空格插入一个字符串之中：


## 实例


```javascript
txt1="What a very ";
txt2="nice day";
txt3=txt1+txt2;
```


在以上语句执行后，变量 *txt3*包含的值是：


```javascript
What a very nice day
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_operators3)


或者把空格插入表达式中：:


## 实例


```javascript
txt1="What a very";
txt2="nice day";
txt3=txt1+" "+txt2;
```


在以上语句执行后，变量*txt3* 包含的值是：


```javascript
What a very nice day
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_operators4)


---


## 对字符串和数字进行加法运算


两个数字相加，返回数字相加的和，如果数字与字符串相加，返回字符串，如下实例：


## 实例


```javascript
x=5+5;
y="5"+5;
z="Hello"+5;
```


*x*,*y*, 和 *z* 输出结果为:


```javascript
10
55
Hello5
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_operators5)


规则:**如果把数字与字符串相加，结果将成为字符串！








	  AI 思考中...





			** [JavaScript 函数](https://www.runoob.com/js-functions.html)
			[JavaScript 比较和逻辑运算符](https://www.runoob.com/js-comparisons.html) **
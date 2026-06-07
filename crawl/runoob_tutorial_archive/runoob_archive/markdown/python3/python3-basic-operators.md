# Python3 运算符

- Source: https://www.runoob.com/python3/python3-basic-operators.html

---

## 什么是运算符？


本章节主要说明 Python 的运算符。


举个简单的例子:


```
4 + 5 = 9
```


例子中，**4** 和 **5** 被称为**操作数**，**+** 称为**运算符**。


Python 语言支持以下类型的运算符:


- 算术运算符
- 比较（关系）运算符
- 赋值运算符
- 逻辑运算符
- 位运算符
- 成员运算符
- 身份运算符
- 运算符优先级


接下来让我们一个个来学习Python的运算符。

---


## Python算术运算符


以下假设变量 **a=10**，变量 **b=21**：


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| + | 加 - 两个对象相加 | a + b 输出结果 31 |
| - | 减 - 得到负数或是一个数减去另一个数 | a - b 输出结果 -11 |
| * | 乘 - 两个数相乘或是返回一个被重复若干次的字符串 | a * b 输出结果 210 |
| / | 除 - x 除以 y | b / a 输出结果 2.1 |
| % | 取模 - 返回除法的余数 | b % a 输出结果 1 |
| ** | 幂 - 返回x的y次幂 | a**b 为10的21次方 |
| // | 取整除 - 往小的方向取整数 |
```
>>> 9//2
4
>>> -9//2
-5
```
 |


以下实例演示了Python所有算术运算符的操作：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

a = 21
b = 10
c = 0

c = a + b
print ("1 - c 的值为：", c)

c = a - b
print ("2 - c 的值为：", c)

c = a * b
print ("3 - c 的值为：", c)

c = a / b
print ("4 - c 的值为：", c)

c = a % b
print ("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print ("6 - c 的值为：", c)

a = 10
b = 5
c = a//b
print ("7 - c 的值为：", c)
```


以上实例输出结果：


```
1 - c 的值为： 31
2 - c 的值为： 11
3 - c 的值为： 210
4 - c 的值为： 2.1
5 - c 的值为： 1
6 - c 的值为： 8
7 - c 的值为： 2
```


---

## Python 比较运算符


以下假设变量 a 为 10，变量 b 为20：


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| == | 等于 - 比较对象是否相等 | (a == b) 返回 False。 |
| != | 不等于 - 比较两个对象是否不相等 | (a != b) 返回 True。 |
| > | 大于 - 返回x是否大于y | (a > b) 返回 False。 |
| = | 大于等于 - 返回x是否大于等于y。 | (a >= b) 返回 False。 |
|  5:`：这是使用海象运算符（`:=`）的写法。海象运算符在表达式中进行赋值操作。`(n := 10)`：将变量 `n` 赋值为 10，同时返回这个赋值结果。
- `> 5`：检查赋值后的 `n` 是否大于 5。如果条件为真，则执行接下来的代码块。
`print(n)`：如果条件为真，打印变量 `n` 的值（即 10）。

**海象运算符的优点：**


- 海象运算符（`:=`）允许在表达式内部进行赋值，这可以减少代码的重复，提高代码的可读性和简洁性。
- 在上述例子中，传统写法需要单独一行来赋值 `n`，然后在 `if` 语句中进行条件检查。而使用海象运算符的写法可以在 `if` 语句中直接进行赋值和条件检查。


---

## Python位运算符


按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：


下表中变量 a 为 60，b 为 13二进制格式如下：


```
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011
```


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| & | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100 |
| \| | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a \| b) 输出结果 61 ，二进制解释： 0011 1101 |
| ^ | 按位异或运算符：当两对应的二进位相异时，结果为1 | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001 |
| ~ | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1 | (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。 |
| > | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数 | a >> 2 输出结果 15 ，二进制解释： 0000 1111 |


以下实例演示了Python所有位运算符的操作：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

a = 60            # 60 = 0011 1100
b = 13            # 13 = 0000 1101
c = 0

c = a & b        # 12 = 0000 1100
print ("1 - c 的值为：", c)

c = a | b        # 61 = 0011 1101
print ("2 - c 的值为：", c)

c = a ^ b        # 49 = 0011 0001
print ("3 - c 的值为：", c)

c = ~a           # -61 = 1100 0011
print ("4 - c 的值为：", c)

c = a << 2       # 240 = 1111 0000
print ("5 - c 的值为：", c)

c = a >> 2       # 15 = 0000 1111
print ("6 - c 的值为：", c)
```


以上实例输出结果：


```
1 - c 的值为： 12
2 - c 的值为： 61
3 - c 的值为： 49
4 - c 的值为： -61
5 - c 的值为： 240
6 - c 的值为： 15
```


---

## Python逻辑运算符


Python语言支持逻辑运算符，以下假设变量 a 为 10, b为 20:


| 运算符 | 逻辑表达式 | 描述 | 实例 |
| --- | --- | --- | --- |
| and | x and y | 布尔"与" - 如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值。 | (a and b) 返回 20。 |
| or | x or y | 布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。 | (a or b) 返回 10。 |
| not | not x | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |


以上实例输出结果：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

a = 10
b = 20

if ( a and b ):
   print ("1 - 变量 a 和 b 都为 true")
else:
   print ("1 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
   print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("2 - 变量 a 和 b 都不为 true")

# 修改变量 a 的值
a = 0
if ( a and b ):
   print ("3 - 变量 a 和 b 都为 true")
else:
   print ("3 - 变量 a 和 b 有一个不为 true")

if ( a or b ):
   print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
else:
   print ("4 - 变量 a 和 b 都不为 true")

if not( a and b ):
   print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
else:
   print ("5 - 变量 a 和 b 都为 true")
```


以上实例输出结果：


```
1 - 变量 a 和 b 都为 true
2 - 变量 a 和 b 都为 true，或其中一个变量为 true
3 - 变量 a 和 b 有一个不为 true
4 - 变量 a 和 b 都为 true，或其中一个变量为 true
5 - 变量 a 和 b 都为 false，或其中一个变量为 false
```


---

## Python成员运算符


除了以上的一些运算符之外，Python还支持成员运算符，测试实例中包含了一系列的成员，包括字符串，列表或元组。


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| in | 如果在指定的序列中找到值返回 True，否则返回 False。 | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。 |
| not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |


以下实例演示了Python所有成员运算符的操作：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

a = 10
b = 20
list = [1, 2, 3, 4, 5 ]

if ( a in list ):
   print ("1 - 变量 a 在给定的列表中 list 中")
else:
   print ("1 - 变量 a 不在给定的列表中 list 中")

if ( b not in list ):
   print ("2 - 变量 b 不在给定的列表中 list 中")
else:
   print ("2 - 变量 b 在给定的列表中 list 中")

# 修改变量 a 的值
a = 2
if ( a in list ):
   print ("3 - 变量 a 在给定的列表中 list 中")
else:
   print ("3 - 变量 a 不在给定的列表中 list 中")
```


以上实例输出结果：


```
1 - 变量 a 不在给定的列表中 list 中
2 - 变量 b 不在给定的列表中 list 中
3 - 变量 a 在给定的列表中 list 中
```


---

## Python身份运算符


身份运算符用于比较两个对象的存储单元


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| is | is 是判断两个标识符是不是引用自一个对象 | x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | x is not y ， 类似 id(x) != id(y)。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |


**注：** [id()](https://www.runoob.com/../python/python-func-id.html) 函数用于获取对象内存地址。


以下实例演示了Python所有身份运算符的操作：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

a = 20
b = 20

if ( a is b ):
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")

if ( id(a) == id(b) ):
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")

if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")
```


以上实例输出结果：


```
1 - a 和 b 有相同的标识
2 - a 和 b 有相同的标识
3 - a 和 b 没有相同的标识
4 - a 和 b 没有相同的标识
```


**

is 与 == 区别：


is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。


```python
>>>a = [1, 2, 3]
>>> b = a
>>> b is a
True
>>> b == a
True
>>> b = a[:]
>>> b is a
False
>>> b == a
True
```


---

## Python运算符优先级


以下表格列出了从最高到最低优先级的所有运算符， 相同单元格内的运算符具有相同优先级。 运算符均指二元运算，除非特别指出。 相同单元格内的运算符从左至右分组（除了幂运算是从右至左分组）：


| 运算符 | 描述 |
| --- | --- |
| (expressions...), [expressions...], {key: value...}, {expressions...} | 圆括号的表达式 |
| x[index], x[index:index], x(arguments...), x.attribute | 读取，切片，调用，属性引用 |
| await x | await 表达式 |
| ** | 乘方(指数) |
| +x, -x, ~x | 正，负，按位非 NOT |
| *, @, /, //, % | 乘，矩阵乘，除，整除，取余 |
| +, - | 加和减 |
| , >> | 移位 |
| & | 按位与 AND |
| ^ | 按位异或 XOR |
| \| | 按位或 OR |
| in,not in, is,is not, , , >, >=, !=, == | 比较运算，包括成员检测和标识号检测 |
| not x | 逻辑非 NOT |
| and | 逻辑与 AND |
| or | 逻辑或 OR |
| if -- else | 条件表达式 |
| lambda | lambda 表达式 |
| := | 赋值表达式 |


以下实例演示了Python所有运算符优先级的操作：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("(a + b) * c / d 运算结果为：",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("((a + b) * c) / d 运算结果为：",  e)

e = (a + b) * (c / d)    # (30) * (15/5)
print ("(a + b) * (c / d) 运算结果为：",  e)

e = a + (b * c) / d      #  20 + (150/5)
print ("a + (b * c) / d 运算结果为：",  e)
```


以上实例输出结果：


```
(a + b) * c / d 运算结果为： 90.0
((a + b) * c) / d 运算结果为： 90.0
(a + b) * (c / d) 运算结果为： 90.0
a + (b * c) / d 运算结果为： 50.0
```


and 拥有更高优先级:


## 实例


```python
x = True
y = False
z = False

print("情况1：默认优先级（先算and）")
if x or y and z:  # 等同于 x or (y and z)
    print("yes")  # 会输出
else:
    print("no")

print("\n情况2：强制改变优先级（先算or）")
if (x or y) and z:  # 人为添加括号改变顺序
    print("yes")  # 不会输出
else:
    print("no")  # 会输出
```


以上实例先计算 **y and z** 并返回 False ，然后 **x or False** 返回 True，输出结果：


```
情况1：默认优先级（先算and）
yes

情况2：强制改变优先级（先算or）
no
```


> 注意：**Python3 已不支持 ****  运算符，可以使用 **!=** 代替，如果你一定要使用这种比较运算符，可以使用以下的方式：
>
>
```
>>> from __future__ import barry_as_FLUFL
>>> 1 <> 2
True
```




---


```
x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")
```


```
x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)
```




课后练习










	  AI 思考中...





			** [Python3 命令行参数](https://www.runoob.com/python3-command-line-arguments.html)
			[Python3 abs() 函数](https://www.runoob.com/python3-func-number-abs.html) **
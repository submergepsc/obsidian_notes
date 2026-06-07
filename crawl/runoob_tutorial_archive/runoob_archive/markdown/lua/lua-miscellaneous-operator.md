# Lua 运算符

- Source: https://www.runoob.com/lua/lua-miscellaneous-operator.html

运算符是一个特殊的符号，用于告诉解释器执行特定的数学或逻辑运算。Lua提供了以下几种运算符类型：


- 算术运算符
- 关系运算符
- 逻辑运算符
- 其他运算符


---


## 算术运算符


下表列出了 Lua 语言中的常用算术运算符，设定 A 的值为10，B 的值为 20：


| 操作符 | 描述 | 实例 |
| --- | --- | --- |
| + | 加法 | A + B 输出结果 30 |
| - | 减法 | A - B 输出结果 -10 |
| * | 乘法 | A * B 输出结果 200 |
| / | 除法 | B / A 输出结果 2 |
| % | 取余 | B % A 输出结果 0 |
| ^ | 乘幂 | A^2 输出结果 100 |
| - | 负号 | -A 输出结果 -10 |
| // | 整除运算符(>=lua5.3) | 5//2 输出结果 2 |


### 实例


我们可以通过以下实例来更加透彻的理解算术运算符的应用：


## 实例


```lua
a = 21
b = 10
c = a + b
print("Line 1 - c 的值为 ", c )
c = a - b
print("Line 2 - c 的值为 ", c )
c = a * b
print("Line 3 - c 的值为 ", c )
c = a / b
print("Line 4 - c 的值为 ", c )
c = a % b
print("Line 5 - c 的值为 ", c )
c = a^2
print("Line 6 - c 的值为 ", c )
c = -a
print("Line 7 - c 的值为 ", c )
```


以上程序执行结果为：


```
Line 1 - c 的值为     31
Line 2 - c 的值为     11
Line 3 - c 的值为     210
Line 4 - c 的值为     2.1
Line 5 - c 的值为     1
Line 6 - c 的值为     441
Line 7 - c 的值为     -21
```


在 lua 中，**/** 用作除法运算，计算结果包含小数部分，**//** 用作整除运算，计算结果不包含小数部分：


## 实例


```lua
a = 5
b = 2

print("除法运算 - a/b 的值为 ", a / b )
print("整除运算 - a//b 的值为 ", a // b )
```


以上程序执行结果为：


```
除法运算 - a/b 的值为   2.5
整除运算 - a//b 的值为  2
```


---


## 关系运算符


下表列出了 Lua 语言中的常用关系运算符，设定 A 的值为10，B 的值为 20：


| 操作符 | 描述 | 实例 |
| --- | --- | --- |
| == | 等于，检测两个值是否相等，相等返回 true，否则返回 false | (A == B) 为 false。 |
| ~= | 不等于，检测两个值是否相等，不相等返回 true，否则返回 false | (A ~= B) 为 true。 |
| > | 大于，如果左边的值大于右边的值，返回 true，否则返回 false | (A > B) 为 false。 |
| = | 大于等于，如果左边的值大于等于右边的值，返回 true，否则返回 false | (A >= B) 返回 false。 |
|







	  AI 思考中...





			** [Lua 函数](https://www.runoob.com/lua-functions.html)
			[Lua 字符串](https://www.runoob.com/lua-strings.html) **
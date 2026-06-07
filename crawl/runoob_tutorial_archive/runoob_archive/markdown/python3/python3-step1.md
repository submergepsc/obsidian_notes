# Python3 编程第一步

- Source: https://www.runoob.com/python3/python3-step1.html

在前面的教程中我们已经学习了一些 Python3 的基本语法知识，接下来我们来尝试一些实例。


打印字符串:


## 实例


```python
print("Hello, world!")
```


输出结果为：


```
Hello, world!
```


输出变量值:


## 实例


```python
i = 256*256
print('i 的值为：', i)
```


输出结果为：


```
i 的值为： 65536
```


定义变量并进行简单的数学运算


## 实例


```python
x = 3
y = 2
z = x + y
print(z)
```


输出结果为：


```
5
```


定义一个列表并打印出其中的元素：


## 实例


```python
my_list = ['google', 'runoob', 'taobao']
print(my_list[0]) # 输出 "google"
print(my_list[1]) # 输出 "runoob"
print(my_list[2]) # 输出 "taobao"
```


输出结果为：


```
google
runoob
taobao
```


使用 for 循环打印数字 0 到 4:


## 实例


```python
for i in range(5):
    print(i)
```


输出结果为：


```
0
1
2
3
4
```


根据条件输出不同的结果:


## 实例


```python
x = 6
if x > 10:
    print("x 大于 10")
else:
    print("x 小于或等于 10")
```


输出结果为：


```
x 小于或等于 10
```


下面我们尝试来写一个斐波纳契数列。


斐波那契数列是一个经典的数学问题，其中每个数字是前两个数字之和。


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
```


其中代码 **a, b = b, a+b** 的计算方式为先计算右边表达式，然后同时赋值给左边，等价于：


```
n=b
m=a+b
a=n
b=m
```


执行以上程序，输出结果为：


```
1
1
2
3
5
8
```


这个例子介绍了几个新特征。


第一行包含了一个复合赋值：变量 a 和 b 同时得到新值 0 和 1。最后一行再次使用了同样的方法，可以看到，右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。


也可以使用 for 循环来实现：


## 实例


```python
n = 10
a, b = 0, 1
for i in range(n):
    print(b)
    a, b = b, a + b
```


### end 关键字


关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符，实例如下：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
```


执行以上程序，输出结果为：


```
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```









	  AI 思考中...





			** [Python3 列表](https://www.runoob.com/python3-list.html)
			[Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html) **
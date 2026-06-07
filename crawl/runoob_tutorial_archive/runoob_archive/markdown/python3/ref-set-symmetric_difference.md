# Python Set symmetric_difference() 方法

- Source: https://www.runoob.com/python3/ref-set-symmetric_difference.html

[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)


---


symmetric_difference() 方法可以用来找到两个集合的对称差。


symmetric_difference() 方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。


## 语法


symmetric_difference() 方法语法：


```
set.symmetric_difference(set)
```


## 参数


- set -- 集合


## 返回值


返回一个新的集合。


## 实例


返回两个集合组成的新集合，但会移除两个集合的重复元素：


## 实例 1


```python
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.symmetric_difference(y)

print(z)
```


输出结果为：


```python
{'google', 'cherry', 'banana', 'runoob'}
```


你还可以使用 **^** 运算符来实现相同的效果：


## 实例


```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = set1 ^ set2
print(result)  # 输出: {1, 2, 5, 6}
```


输出结果为：


```python
{1, 2, 5, 6}
```


[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)








	  AI 思考中...





			** [Python Set remove() 方法](https://www.runoob.com/ref-set-remove.html)
			[Python Set symmetric_difference_update() 方法](https://www.runoob.com/ref-set-symmetric_difference_update.html) **
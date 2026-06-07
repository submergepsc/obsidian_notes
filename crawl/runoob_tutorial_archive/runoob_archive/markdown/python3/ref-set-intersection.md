# Python Set intersection() 方法

- Source: https://www.runoob.com/python3/ref-set-intersection.html

[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)


---


## 描述


intersection() 方法用于返回两个或更多集合中都包含的元素，即交集。


## 语法


intersection() 方法语法：


```
set.intersection(set1, set2 ... etc)
```


## 参数


- set1 -- 必需，要查找相同元素的集合
- set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开


## 返回值


返回一个新的集合。


## 实例


返回一个新集合，该集合的元素既包含在集合 x 又包含在集合 y 中：


## 实例 1


```python
x = {"apple", "banana", "cherry"}
y = {"google", "runoob", "apple"}

z = x.intersection(y)

print(z)
```


输出结果为：


```python
{'apple'}
```


计算多个集合的交集：


## 实例 1


```python
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)
```


输出结果为：


```python
{'c'}
```


[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)








	  AI 思考中...





			** [Python Set discard() 方法](https://www.runoob.com/ref-set-discard.html)
			[Python Set intersection_update() 方法](https://www.runoob.com/ref-set-intersection_update.html) **
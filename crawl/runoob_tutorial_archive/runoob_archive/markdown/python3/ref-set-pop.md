# Python Set pop() 方法

- Source: https://www.runoob.com/python3/ref-set-pop.html

[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)


---


## 描述


pop() 方法用于移除并返回集合中的一个随机元素。如果集合为空，会抛出 KeyError 异常。


## 语法


pop() 方法语法：


```
set.pop()
```


## 参数


- 无


## 返回值


返回移除的元素。


## 实例


随机移除一个元素：


## 实例 1


```python
fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)
```


输出结果为：


```python
{'apple', 'banana'}
```


输出返回值：


## 实例 1


```python
fruits = {"apple", "banana", "cherry"}

x = fruits.pop()

print(x)
```


输出结果为：


```python
banana
```


### 注意事项


- 集合中的元素是无序的，因此每次调用 `pop()` 方法时，被移除的元素是随机的。
- 如果需要移除特定的元素，应该使用 `remove()` 或 `discard()` 方法，而不是 `pop()`。


[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)








	  AI 思考中...





			** [Python Set issuperset() 方法](https://www.runoob.com/ref-set-issuperset.html)
			[Python Set remove() 方法](https://www.runoob.com/ref-set-remove.html) **
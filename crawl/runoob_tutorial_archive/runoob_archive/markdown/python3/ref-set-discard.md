# Python Set discard() 方法

- Source: https://www.runoob.com/python3/ref-set-discard.html

[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)


---


## 描述


discard() 方法用于移除指定的集合元素。


该方法不同于 `remove()` 方法，因为 `remove()` 方法在移除一个不存在的元素时会发生错误，而 `discard()` 方法不会。


## 语法


discard() 方法语法：


```
set.discard(value)
```


## 参数


- value -- 必需，要移除的元素


## 返回值


无。


## 实例


移除集合中的元素 banana：


## 实例 1


```python
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")

print(fruits)
```


输出结果为：


```python
{'cherry', 'apple'}
```


[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)








	  AI 思考中...





			** [Python Set difference_update() 方法](https://www.runoob.com/ref-set-difference_update.html)
			[Python Set intersection() 方法](https://www.runoob.com/ref-set-intersection.html) **
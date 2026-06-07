# Python dict() 函数

- Source: https://www.runoob.com/python3/python-func-dict.html

[![Python 内置函数](https://www.runoob.com/images/up.gif) Python 内置函数](https://www.runoob.com/python-built-in-functions.html)


---


## 描述


**dict()** 函数用于创建一个字典。


## 语法


dict 语法：


```
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)
```


参数说明：


- **kwargs -- 关键字。
- mapping -- 元素的容器，映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。
- iterable -- 可迭代对象。


## 返回值


返回一个字典。


## 实例


以下实例展示了 dict 的使用方法：


```python
>>>dict()                        # 创建空字典
{}
>>> dict(a='a', b='b', t='t')     # 传入关键字
{'a': 'a', 'b': 'b', 't': 't'}
>>> dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典
{'three': 3, 'two': 2, 'one': 1}
>>> dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典
{'three': 3, 'two': 2, 'one': 1}
>>>
```


### 只使用关键字参数创建字典


## 实例


```python
numbers = dict(x=5, y=0)
print('numbers =', numbers)
print(type(numbers))

empty = dict()
print('empty =', empty)
print(type(empty))
```


以上实例输出结果为：


```
numbers = {'y': 0, 'x': 5}
<class 'dict'>
empty = {}
<class 'dict'>
```


### 使用可迭代对象创建字典


## 实例


```python
# 没有设置关键字参数
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

# 设置关键字参数
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

# zip() 创建可迭代对象
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =',numbers3)
```


以上实例输出结果为：


```
numbers1 = {'y': -5, 'x': 5}
numbers2 = {'z': 8, 'y': -5, 'x': 5}
numbers3 = {'z': 3, 'y': 2, 'x': 1}
```


### 使用映射来创建字典

映射类型（Mapping Types）是一种关联式的容器类型，它存储了对象与对象之间的映射关系。


## 实例


```python
numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)

# 以下代码不需要使用 dict()
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)

# 关键字参数会被传递
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)
```


以上实例输出结果为：


```
numbers1 = {'x': 4, 'y': 5}
numbers2 = {'x': 4, 'y': 5}
numbers3 = {'x': 4, 'z': 8, 'y': 5}
```


[![Python 内置函数](https://www.runoob.com/images/up.gif) Python 内置函数](https://www.runoob.com/python-built-in-functions.html)










	  AI 思考中...





			** [Python next() 函数](https://www.runoob.com/../python/python-func-next.html)
			[Python hex() 函数](https://www.runoob.com/../python/python-func-hex.html) **
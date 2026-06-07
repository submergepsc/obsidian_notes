# Python3 List sort()方法

- Source: https://www.runoob.com/python3/python3-att-list-sort.html

[![Python3 列表](https://www.runoob.com/images/up.gif) Python3 列表](https://www.runoob.com/python3-list.html)


---


## 描述


sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。


## 语法


sort()方法语法：


```
list.sort( key=None, reverse=False)
```


## 参数


## 参数


- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse -- 排序规则，**reverse = True** 降序， **reverse = False** 升序（默认）。


## 返回值


该方法没有返回值，但是会对列表的对象进行排序。


## 实例


以下实例展示了 sort() 函数的使用方法：


## 实例



```python
#!/usr/bin/python

aList = ['Google', 'Runoob', 'Taobao', 'Facebook']

aList.sort()
print ( "List : ", aList)
```


以上实例输出结果如下：


```
List :  ['Facebook', 'Google', 'Runoob', 'Taobao']
```


以下实例降序输出列表：


## 实例



```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 列表
vowels = ['e', 'a', 'u', 'o', 'i']

# 降序
vowels.sort(reverse=True)

# 输出结果
print ( '降序输出:', vowels )
```


以上实例输出结果如下：


```
降序输出: ['u', 'o', 'i', 'e', 'a']
```


以下实例演示了通过指定列表中的元素排序来输出列表：


## 实例



```python
#!/usr/bin/python

# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]

# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)

# 输出类别
print ('排序列表：', random)
```


以上实例输出结果如下：


```
排序列表：[(4, 1), (2, 2), (1, 3), (3, 4)]
```


[![Python3 列表](https://www.runoob.com/images/up.gif) Python3 列表](https://www.runoob.com/python3-list.html)








	  AI 思考中...





			** [Python3 List reverse()方法](https://www.runoob.com/python3-att-list-reverse.html)
			[Python3 List clear()方法](https://www.runoob.com/python3-att-list-clear.html) **
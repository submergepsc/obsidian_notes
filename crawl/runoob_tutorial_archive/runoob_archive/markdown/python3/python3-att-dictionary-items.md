# Python3 字典 items() 方法

- Source: https://www.runoob.com/python3/python3-att-dictionary-items.html

[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)


---


## 描述


Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。


[dict.keys()](https://www.runoob.com/python3-att-dictionary-keys.html)、[dict.values()](https://www.runoob.com/python3-att-dictionary-values.html) 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。


视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。


我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。


## 语法


items()方法语法：


```
dict.items()
```


## 参数


- NA。


## 返回值


返回可视图对象。


## 实例


以下实例展示了 items() 方法的使用方法：


## 实例


```python
#!/usr/bin/python3

tinydict = {'Name': 'Runoob', 'Age': 7}

print ("Value : %s" %  tinydict.items())
```


以上实例输出结果为：


```
Value : dict_items([('Age', 7), ('Name', 'Runoob')])
```


---


[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)








	  AI 思考中...





			** [Python3 字典 in 操作符](https://www.runoob.com/python3-att-dictionary-in-html.html)
			[Python3 字典 keys() 方法](https://www.runoob.com/python3-att-dictionary-keys.html) **
# Python3 字典 update() 方法

- Source: https://www.runoob.com/python3/python3-att-dictionary-update.html

[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)


---


## 描述


Python 字典 update() 函数把字典参数 dict2 的 **key/value(键/值)** 对更新到字典 dict 里。


## 语法


update() 方法语法：


```
dict.update(dict2)
```


## 参数


- dict2 -- 添加到指定字典dict里的字典。


## 返回值


该方法没有任何返回值。


## 实例


以下实例展示了 update()函数的使用方法：


## 实例(Python 2.0+)



```python
#!/usr/bin/python3

tinydict = {'Name': 'Runoob', 'Age': 7}
tinydict2 = {'Sex': 'female' }

tinydict.update(tinydict2)
print ("更新字典 tinydict : ", tinydict)
```


以上实例输出结果为：


```
更新字典 tinydict :  {'Name': 'Runoob', 'Age': 7, 'Sex': 'female'}
```


---


[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)








	  AI 思考中...





			** [Python3 字典 setdefault() 方法](https://www.runoob.com/python3-att-dictionary-setdefault.html)
			[Python3 字典 values() 方法](https://www.runoob.com/python3-att-dictionary-values.html) **
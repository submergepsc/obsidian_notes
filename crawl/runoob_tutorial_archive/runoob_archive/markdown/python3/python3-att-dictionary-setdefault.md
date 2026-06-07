# Python3 字典 setdefault() 方法

- Source: https://www.runoob.com/python3/python3-att-dictionary-setdefault.html

[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)


---


## 描述


Python 字典 setdefault() 方法和 [get()方法](https://www.runoob.com/python3-att-dictionary-get.html) 类似, 如果键不存在于字典中，将会添加键并将值设为默认值。


## 语法


setdefault()方法语法：


```
dict.setdefault(key, default=None)
```


## 参数


- key -- 查找的键值。
- default -- 键不存在时，设置的默认键值。


## 返回值


如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。


## 实例


以下实例展示了 setdefault() 方法的使用方法：


## 实例


```python
#!/usr/bin/python3

tinydict = {'Name': 'Runoob', 'Age': 7}

print ("Age 键的值为 : %s" %  tinydict.setdefault('Age', None))
print ("Sex 键的值为 : %s" %  tinydict.setdefault('Sex', None))
print ("新字典为：", tinydict)
```


以上实例输出结果为：


```
Age 键的值为 : 7
Sex 键的值为 : None
新字典为： {'Age': 7, 'Name': 'Runoob', 'Sex': None}
```


---


[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)








	  AI 思考中...





			** [Python3 字典 keys() 方法](https://www.runoob.com/python3-att-dictionary-keys.html)
			[Python3 字典 update() 方法](https://www.runoob.com/python3-att-dictionary-update.html) **
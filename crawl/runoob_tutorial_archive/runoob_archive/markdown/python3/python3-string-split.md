# Python3 split()方法

- Source: https://www.runoob.com/python3/python3-string-split.html

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)


---


## 描述


split() 方法通过指定分隔符对字符串进行切片，该方法将字符串分割成子字符串并返回一个由这些子字符串组成的列表。

如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。


split()方法特别适用于根据特定的分隔符将字符串拆分成多个部分。


## 语法


split() 方法语法：


```
str.split(str="", num=string.count(str))
```


## 参数


- str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
- num -- 分割次数，如果设置了这个参数，则最多分割成 maxsplit+1 个子字符串。默认为 -1, 即分隔所有。


## 返回值


返回分割后的字符串列表。


## 实例


以下实例展示了 split() 函数的使用方法：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

str = "this is string example....wow!!!"
print (str.split())        # 默认以空格为分隔符
print (str.split('i',1))   # 以 i 为分隔符
print (str.split('w'))     # 以 w 为分隔符
```


以上实例输出结果如下：


```
['this', 'is', 'string', 'example....wow!!!']
['th', 's is string example....wow!!!']
['this is string example....', 'o', '!!!']
```


以下实例以 # 号为分隔符，指定第二个参数为 1，返回两个参数列表。


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

txt = "Google#Runoob#Taobao#Facebook"

# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)

print(x)
```


以上实例输出结果如下：


```
['Google', 'Runoob#Taobao#Facebook']
```


---


[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)









	  AI 思考中...





			** [Python3 rstrip() 方法](https://www.runoob.com/python3-string-rstrip.html)
			[Python3 splitlines()方法](https://www.runoob.com/python3-string-splitlines.html) **
# Python3 translate()方法

- Source: https://www.runoob.com/python3/python3-string-translate.html

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)


---


## 描述


translate() 方法根据参数 table 给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 **deletechars** 参数中。


## 语法


translate()方法语法：


```
str.translate(table)
bytes.translate(table[, delete])
bytearray.translate(table[, delete])
```


## 参数


- table -- 翻译表，翻译表是通过 [maketrans()](https://www.runoob.com/python3-string-maketrans.html) 方法转换而来。
- deletechars -- 字符串中要过滤的字符列表。


## 返回值


返回翻译后的字符串,若给出了 delete 参数，则将原来的bytes中的属于delete的字符删除，剩下的字符要按照table中给出的映射来进行映射 。


## 实例


以下实例展示了 translate() 函数的使用方法：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)   # 制作翻译表

str = "this is string example....wow!!!"
print (str.translate(trantab))
```


以上实例输出结果如下：


```
th3s 3s str3ng 2x1mpl2....w4w!!!
```


以下实例演示如何过滤掉的字符 o：


## 实例(Python 3.0+)



```python
#!/usr/bin/python

# 制作翻译表
bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# 转换为大写，并删除字母o
print(b'runoob'.translate(bytes_tabtrans, b'o'))
```


以上实例输出结果：


```
b'RUNB'
```


---


[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)









	  AI 思考中...





			** [Python3 title()方法](https://www.runoob.com/python3-string-title.html)
			[Python3 upper()方法](https://www.runoob.com/python3-string-upper.html) **
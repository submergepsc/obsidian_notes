# Python3 isdigit()方法

- Source: https://www.runoob.com/python3/python3-string-isdigit.html

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)


---


## 描述


Python isdigit() 方法检测字符串是否只由数字组成。


## 语法


isdigit()方法语法：


```
str.isdigit()
```


## 参数


- 无。


## 返回值


如果字符串只包含数字则返回 True 否则返回 False。


## 实例


以下实例展示了isdigit()方法的实例：


## 实例


```python
#!/usr/bin/python3

str = "123456";
print (str.isdigit())

str = "Runoob example....wow!!!"
print (str.isdigit())
```


以上实例输出结果如下：


```
True
False
```


isdigit() 方法只对正整数有效，负数及小数均返回不正确。


可以使用以下函数来解决：


## 实例


```python
# 判断是否为数字
def is_number(s):
    try:    # 如果能运⾏ float(s) 语句，返回 True（字符串 s 是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError 为 Python 的⼀种标准异常，表⽰"传⼊⽆效的参数"
        pass  # 如果引发了 ValueError 这种异常，不做任何事情（pass：不做任何事情，⼀般⽤做占位语句）
    try:
        import unicodedata  # 处理 ASCII 码的包
        unicodedata.numeric(s)  # 把⼀个表⽰数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
        return False

print(is_number(1))
print(is_number(1.0))
print(is_number(0))
print(is_number(-2))
print(is_number(-2.0))
print(is_number("abc"))
```


输出结果为：


```
True
True
True
True
True
False
```


---


[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)









	  AI 思考中...





			** [Python3 isalpha()方法](https://www.runoob.com/python3-string-isalpha.html)
			[Python3 islower()方法](https://www.runoob.com/python3-string-islower.html) **
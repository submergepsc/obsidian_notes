# Python3 endswith()方法

- Source: https://www.runoob.com/python3/python3-string-endswith.html

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)


---


## 描述


endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。


## 语法


endswith()方法语法：


```
str.endswith(suffix[, start[, end]])
```


## 参数


- suffix -- 该参数可以是一个字符串或者是一个元素。
- start -- 字符串中的开始位置。
- end -- 字符中结束位置。


## 返回值


如果字符串含有指定的后缀返回 True，否则返回 False。


## 实例


以下实例展示了endswith()方法的实例：


## 实例


```python
#!/usr/bin/python3

Str='Runoob example....wow!!!'
suffix='!!'
print (Str.endswith(suffix))
print (Str.endswith(suffix,20))
suffix='run'
print (Str.endswith(suffix))
print (Str.endswith(suffix, 0, 19))
```


以上实例输出结果如下：


```
True
True
False
False
```


---


[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)









	  AI 思考中...





			** [Python3 encode()方法](https://www.runoob.com/python3-string-encode.html)
			[Python3 expandtabs()方法](https://www.runoob.com/python3-string-expandtabs.html) **
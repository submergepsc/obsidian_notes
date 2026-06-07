# Python3 count()方法

- Source: https://www.runoob.com/python3/python3-string-count.html

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)


---


## 描述


count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。


## 语法


count()方法语法：


```
str.count(sub, start= 0,end=len(string))
```


## 参数


- sub -- 搜索的子字符串
- start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
- end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。


## 返回值


该方法返回子字符串在字符串中出现的次数。


## 实例


以下实例展示了 count() 方法的实例：


## 实例


```python
#!/usr/bin/python3

str="www.runoob.com"
sub='o'
print ("str.count('o') : ", str.count(sub))

sub='run'
print ("str.count('run', 0, 10) : ", str.count(sub,0,10))
```


以上实例输出结果如下：


```
str.count('o') :  3
str.count('run', 0, 10) :  1
```


---


[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)









	  AI 思考中...





			** [Python3 center()方法](https://www.runoob.com/python3-string-center.html)
			[Python3 bytes.decode()方法](https://www.runoob.com/python3-string-decode.html) **
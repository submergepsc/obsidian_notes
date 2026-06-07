# Python3 zfill()方法

- Source: https://www.runoob.com/python3/python3-string-zfill.html

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)


---


## 描述


Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。


## 语法


zfill()方法语法：


```
str.zfill(width)
```


## 参数


- width -- 指定字符串的长度。原字符串右对齐，前面填充0。


## 返回值


返回指定长度的字符串。


## 实例


以下实例展示了 zfill()函数的使用方法：


```
#!/usr/bin/python3

str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(40))
print ("str.zfill : ",str.zfill(50))
```


以上实例输出结果如下：


```
str.zfill :  this is string example from runoob....wow!!!
str.zfill :  000000this is string example from runoob....wow!!!
```


---


[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)









	  AI 思考中...





			** [Python3 upper()方法](https://www.runoob.com/python3-string-upper.html)
			[Python3 isdecimal()方法](https://www.runoob.com/python3-string-isdecimal.html) **
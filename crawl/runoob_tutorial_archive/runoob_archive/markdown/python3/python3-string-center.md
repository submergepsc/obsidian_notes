# Python3 center()方法

- Source: https://www.runoob.com/python3/python3-string-center.html

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)


center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。


### 语法


center()方法语法：


```
str.center(width[, fillchar])
```


## 参数


- width -- 字符串的总宽度。
- fillchar -- 填充字符。


## 返回值


返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。


## 实例


以下实例展示了center()方法的实例：


## 实例


```python
#!/usr/bin/python3

str = "[runoob]"

print ("str.center(40, '*') : ", str.center(40, '*'))
```


以上实例输出结果如下：


```
str.center(40, '*') :  ****************[runoob]****************
```


---

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)








	  AI 思考中...





			** [Python3 capitalize()方法](https://www.runoob.com/python3-string-capitalize.html)
			[Python3 count()方法](https://www.runoob.com/python3-string-count.html) **
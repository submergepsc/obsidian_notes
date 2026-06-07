# Python3 expandtabs()方法

- Source: https://www.runoob.com/python3/python3-string-expandtabs.html

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)


---


## 描述


expandtabs() 方法把字符串中的 tab 符号 **\t** 转为空格，tab 符号 **\t** 默认的空格数是 8，在第 0、8、16...等处给出制表符位置，如果当前位置到开始位置或上一个制表符位置的字符数不足 8 的倍数则以空格代替。


## 语法


expandtabs() 方法语法：


```
str.expandtabs(tabsize=8)
```


## 参数


- tabsize -- 指定转换字符串中的 tab 符号 **\t** 转为空格的字符数。


## 返回值


该方法返回字符串中的 tab 符号 **\t** 转为空格后生成的新字符串。


## 实例


以下实例展示了 expandtabs() 方法的实例：


## 实例


```python
#!/usr/bin/python3

str = "runoob\t12345\tabc"
print('原始字符串:', str)

# 默认 8 个空格
# runnob 有 6 个字符，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，后面的 \t 填充 3 个空格
print('替换 \\t 符号:', str.expandtabs())

# 2 个空格
# runnob 有 6 个字符，刚好是 2 的 3 倍，后面的 \t 填充 2 个空格
# 12345 有 5 个字符，不是 2 的倍数，后面的 \t 填充 1 个空格
print('使用 2 个空格替换 \\t 符号:', str.expandtabs(2))

# 3 个空格
print('使用 3 个空格:', str.expandtabs(3))

# 4 个空格
print('使用 4 个空格:', str.expandtabs(4))

# 5 个空格
print('使用 5 个空格:', str.expandtabs(5))

# 6 个空格
print('使用 6 个空格:', str.expandtabs(6))
```


以上实例输出结果如下：


```
原始字符串: runoob      12345   abc
替换 \t 符号: runoob  12345   abc
使用 2 个空格替换 \t 符号: runoob  12345 abc
使用 3 个空格: runoob   12345 abc
使用 4 个空格: runoob  12345   abc
使用 5 个空格: runoob    12345     abc
使用 6 个空格: runoob      12345 abc
```


---


[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)









	  AI 思考中...





			** [Python3 endswith()方法](https://www.runoob.com/python3-string-endswith.html)
			[Python3 find()方法](https://www.runoob.com/python3-string-find.html) **
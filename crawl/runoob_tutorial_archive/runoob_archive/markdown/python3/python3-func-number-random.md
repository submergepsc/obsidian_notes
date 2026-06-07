# Python3 random() 函数

- Source: https://www.runoob.com/python3/python3-func-number-random.html

[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)


---


## 描述


**random()** 方法返回随机生成的一个实数，它在[半开放区间](https://www.runoob.com/w3cnote/programming-range.html) **[0,1)** 范围内。

---


## 语法


以下是 random() 方法的语法:


```
import random

random.random()
```


**注意：**random() 是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。


---


## 参数


- 无


---


## 返回值


返回随机生成的一个实数，它在[半开放区间](https://www.runoob.com/w3cnote/programming-range.html) **[0,1)** 范围内。


---


## 实例


以下展示了使用 random() 方法的实例：


## 实例


```python
#!/usr/bin/python3
import random

# 第一个随机数
print ("random() : ", random.random())

# 第二个随机数
print ("random() : ", random.random())
```


以上实例运行后输出结果为：


```
random() :  0.09690599908884856
random() :  0.8732120512570916
```


[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)








	  AI 思考中...





			** [Python3 randrange() 函数](https://www.runoob.com/python3-func-number-randrange.html)
			[Python3 seed() 函数](https://www.runoob.com/python3-func-number-seed.html) **
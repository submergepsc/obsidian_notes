# Python3 randrange() 函数

- Source: https://www.runoob.com/python3/python3-func-number-randrange.html

[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)


---


## 描述


**randrange()** 方法返回指定递增基数集合中的一个随机数，基数默认值为1。

---


## 语法


以下是 randrange() 方法的语法:


```
import random

random.randrange ([start,] stop [,step])
```


**注意：**randrange()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。


---


## 参数


- start -- 指定范围内的开始值，包含在范围内。
- stop -- 指定范围内的结束值，不包含在范围内。
- step -- 指定递增基数。


---


## 返回值

从给定的范围返回随机项。

---


## 实例


以下展示了使用 randrange() 方法的实例：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3
#!/usr/bin/python3
import random

# 从 1-100 中选取一个奇数
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))

# 从 0-99 选取一个随机数
print ("randrange(100) : ", random.randrange(100))
```


以上实例运行后输出结果为：


```
randrange(1,100, 2) :  97
randrange(100) :  42
```


[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)








	  AI 思考中...





			** [Python3 choice() 函数](https://www.runoob.com/python3-func-number-choice.html)
			[Python3 random() 函数](https://www.runoob.com/python3-func-number-random.html) **
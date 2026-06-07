# Python3 shuffle() 函数

- Source: https://www.runoob.com/python3/python3-func-number-shuffle.html

[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)


---


## 描述


**shuffle()** 方法将序列的所有元素随机排序。

---


## 语法


以下是 shuffle() 方法的语法:


```python
import random

random.shuffle (lst )
```


**注意：**shuffle() 是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。


---


## 参数


- lst -- 列表。


---


## 返回值


返回 None。


---


## 实例


以下展示了使用 shuffle() 方法的实例：


## 实例



```python
#!/usr/bin/python3
import random

list = [20, 16, 10, 5];
random.shuffle(list)
print ("随机排序列表 : ",  list)

random.shuffle(list)
print ("随机排序列表 : ",  list)
```


以上实例运行后输出结果为：


```
随机排序列表 :  [20, 5, 16, 10]
随机排序列表 :  [5, 20, 10, 16]
```


[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)








	  AI 思考中...





			** [Python3 seed() 函数](https://www.runoob.com/python3-func-number-seed.html)
			[Python3 uniform() 函数](https://www.runoob.com/python3-func-number-uniform.html) **
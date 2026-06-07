# Python for 循环

- Source: https://www.runoob.com/python3/python3-for.html

[![Python3 循环语句](https://www.runoob.com/images/up.gif) Python3 循环语句](https://www.runoob.com/python3-loop.html)


---


`for` 是 Python 中最常用的循环语句，用于遍历可迭代对象（序列、字典、集合等）。


Python 的 `for` 循环比 C/C++ 等语言更加简洁和强大，不需要手动管理循环变量，直接遍历元素。


**单词释义**： `for` 意为"为、对于"，用于迭代遍历。


---


## 基本语法与参数


### 语法格式


```
for 变量 in 可迭代对象:
    代码块
```


### 语法说明


- **变量**： 每次循环从可迭代对象中取出的元素。
- **可迭代对象**： 列表、元组、字符串、字典、集合、range 等。
- **缩进**： 循环体必须缩进。


### else 子句


- **可选**： for 循环可以有 else 子句。
- **执行时机**： 循环正常结束（未通过 break 退出）时执行。


---


## 实例


### 示例 1：遍历列表


## 实例


```python
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]

for fruit in fruits:
    print(fruit)

# 带索引的遍历
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```


**运行结果预期:**


```
苹果
香蕉
橙子
0: 苹果
1: 香蕉
2: 橙子
```


**代码解析:**


- for 循环直接遍历列表中的每个元素。
- enumerate() 同时提供索引和值。


### 示例 2：遍历字符串和元组


## 实例


```python
# 遍历字符串
for char in "Python":
    print(char, end=" ")
print()  # 换行

# 遍历元组
point = (10, 20)
for value in point:
    print(value, end=" ")
print()
```


**运行结果预期:**


```
P y t h o n
10 20
```


字符串和元组也是可迭代的。


### 示例 3：遍历字典


## 实例


```python
# 遍历字典（默认遍历键）
person = {"name": "Tom", "age": 20, "city": "Beijing"}

for key in person:
    print(key)

print("---")

# 遍历键值对
for key, value in person.items():
    print(f"{key}: {value}")

print("---")

# 只遍历值
for value in person.values():
    print(value)
```


**运行结果预期:**


```
name
age
city
---
name: Tom
age: 20
city: Beijing
---
Tom
20
Beijing
```


字典的 items()、keys()、values() 方法可以遍历不同的部分。


### 示例 4：带 else 的 for 循环


## 实例


```python
# for-else 结构
for i in range(3):
    print(i)
else:
    print("循环正常结束")

print("---")

# break 时 else 不执行
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("这行不会打印")
```


**运行结果预期:**


```
0
1
2
循环正常结束
---
0
1
2
```


for-else 结构的 else 在循环被 break 终止时不执行。


### 示例 5：嵌套循环


## 实例


```python
# 嵌套循环 - 打印九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end="\t")
    print()
```


**运行结果预期:**


```
1*1=1
1*2=2    2*2=4
1*3=3    2*3=6    3*3=9
...
```


嵌套循环可以用于处理多维数据结构或生成表格。


---


[![Python3 循环语句](https://www.runoob.com/images/up.gif) Python3 循环语句](https://www.runoob.com/python3-loop.html)








	  AI 思考中...





			** [Python match 语句](https://www.runoob.com/python3-match-statement.html)
			[Python while 循环](https://www.runoob.com/python3-while.html) **













### 点我分享笔记







				**
取消






					*


					* 分享笔记






- 昵称昵称 (必填)
- 邮箱邮箱 (必填)
- 引用地址引用地址






































**在线实例**

      : ·[HTML 实例](https://www.runoob.com/../html/html-examples.html)

      : ·[CSS 实例](https://www.runoob.com/../css/css-examples.html)

      : ·[JavaScript 实例](https://www.runoob.com/../js/js-examples.html)

      : ·[Ajax 实例](https://www.runoob.com/../ajx/ajax-examples.html)

       : ·[jQuery 实例](https://www.runoob.com/../jquery/jquery-examples.html)

      : ·[XML 实例](https://www.runoob.com/../xml/xml-examples.html)

      : ·[Java 实例](https://www.runoob.com/../java/java-examples.html)





**字符集&工具**

      : · [HTML 字符集设置](https://www.runoob.com/../charsets/html-charsets.html)

      : · [HTML ASCII 字符集](https://www.runoob.com/../tags/html-ascii.html)

     : · [JS 混淆/加密](https://www.jyshare.com/front-end/6939/)

      : · [PNG/JPEG 图片压缩](https://www.jyshare.com/front-end/6232/)

      : · [HTML 拾色器](https://www.runoob.com/../tags/html-colorpicker.html)

      : · [JSON 格式化工具](https://www.jyshare.com/front-end/53)

      : · [随机数生成器](https://www.jyshare.com/front-end/6680/)




**最新更新**

                  : · [VS Code 创建与...](https://www.runoob.com/../skills/vs-code-skill.html)

                      : · [Skills 脚本扩展](https://www.runoob.com/../skills/skills-scripts.html)

                      : · [Skills 描述](https://www.runoob.com/../skills/skills-description.html)

                      : · [SKILL.md 文件](https://www.runoob.com/../skills/skill-md-file.html)

                      : · [使用现有 Skills](https://www.runoob.com/../skills/use-existing-skills.html)

                      : · [Skills 工作原理](https://www.runoob.com/../skills/how-skills-work.html)

                      : · [第一个 Skill](https://www.runoob.com/../skills/skills-first.html)




**站点信息**

      : · [意见反馈](https://www.runoob.com/../cdn-cgi/l/email-protection/index.html)

      : · [免责声明](https://www.runoob.com/../disclaimer/index.html)

      : · [关于我们](https://www.runoob.com/../aboutus/index.html)

      : · [文章归档](https://www.runoob.com/../archives/index.html)







         关注微信**



      ![](https://www.runoob.com/wp-content/themes/runoob/assets/images/qrcode.png)






     Copyright © 2013-2026    **[菜鸟教程](https://www.runoob.com/../index/index.html)**
    **[runoob.com](https://www.runoob.com/../index/index.html)** All Rights Reserved. 备案号：[闽ICP备15012807号-1](https://beian.miit.gov.cn/)



    **
    **
    **
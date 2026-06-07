# Python lambda（匿名函数）

- Source: https://www.runoob.com/python3/python-lambda.html

Python 使用 **lambda** 来创建匿名函数。


lambda 函数是一种小型、匿名的、内联函数，它可以具有任意数量的参数，但只能有一个表达式。


匿名函数不需要使用 **def** 关键字定义完整函数。


lambda 函数通常用于编写简单的、单行的函数，通常在需要函数作为参数传递的情况下使用，例如在 map()、filter()、reduce() 等函数中。


**lambda 函数特点：**


- lambda 函数是匿名的，它们没有函数名称，只能通过赋值给变量或作为参数传递给其他函数来使用。
- lambda 函数通常只包含一行代码，这使得它们适用于编写简单的函数。


**lambda 语法格式：**


```
lambda arguments: expression
```


- `lambda`是 Python 的关键字，用于定义 lambda 函数。
- `arguments` 是参数列表，可以包含零个或多个参数，但必须在冒号(`:`)前指定。
- `expression` 是一个表达式，用于计算并返回函数的结果。


以下的 lambda 函数没有参数：


## 实例


```python
f = lambda: "Hello, world!"
print(f())  # 输出: Hello, world!
```


输出结果为：


```
Hello, world!
```


以下实例使用 lambda 创建匿名函数，设置一个函数参数 a，函数计算参数 a 加 10，并返回结果：


## 实例


```python
x = lambda a : a + 10
print(x(5))
```


输出结果为：


```
15
```


lambda 函数也可以设置多个参数，参数使用逗号 **,** 隔开：


以下实例使用 lambda 创建匿名函数，函数参数 a 与 b 相乘，并返回结果：


## 实例


```python
x = lambda a, b : a * b
print(x(5, 6))
```


输出结果为：


```
30
```


以下实例使用 lambda 创建匿名函数，函数参数 a、b 与 c 相加，并返回结果：


## 实例


```python
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
```


输出结果为：


```
13
```


lambda 函数通常与内置函数如 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作。例如：


## 实例


```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # 输出: [1, 4, 9, 16, 25]
```


输出结果为：


```
[1, 4, 9, 16, 25]
```


使用 lambda 函数与 filter() 一起，筛选偶数：


## 实例


```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 输出：[2, 4, 6, 8]
```


输出结果为：


```
[2, 4, 6, 8]
```


下面是一个使用 reduce() 和 lambda 表达式演示如何计算一个序列的累积乘积：


## 实例


```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# 使用 reduce() 和 lambda 函数计算乘积
product = reduce(lambda x, y: x * y, numbers)

print(product)  # 输出：120
```


输出结果为：


```
120
```


在上面的实例中，reduce() 函数通过遍历 numbers 列表，并使用 lambda 函数将累积的结果不断更新，最终得到了 **1 * 2 * 3 * 4 * 5 = 120** 的结果。








	  AI 思考中...





			** [Python 按字母顺序对列表排序](https://www.runoob.com/python-sort-list-by-alphabetically.html)
			[Python hashlib 模块](https://www.runoob.com/python-hashlib.html) **













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
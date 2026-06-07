# Python 保留关键字

- Source: https://www.runoob.com/python3/python3-keyword.html

[![Python3 基础语法](https://www.runoob.com/images/up.gif) Python3 基础语法](https://www.runoob.com/python3-basic-syntax.html)


Python 关键字（也称为保留字）是 Python 语言中具有特殊含义的单词，它们被 Python 解释器保留用于特定的语法功能。这些关键字不能用作变量名、函数名或其他标识符。


### 特点


- **不可变性**：关键字是语言规范的一部分，不能修改其含义
- **有限性**：Python 的关键字数量是固定的（Python 3.8 有 35 个关键字）
- **大小写敏感**：所有关键字都是小写形式
- **语法功能**：每个关键字都有特定的语法作用


### 查看所有关键字


你可以使用 Python 的 `keyword` 模块查看当前版本的所有关键字：


## 实例


```python
import keyword

print(keyword.kwlist)
```


在 Python 3.8 中，输出结果为：


```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```


---


## 关键字分类与用途


Python关键字可以按照功能分为以下几大类：


### 1. 值关键字


这些关键字代表特定的值：


| 关键字 | 说明 | 示例 |
| --- | --- | --- |
| True | 布尔真值 | flag = True |
| False | 布尔假值 | flag = False |
| None | 表示空值或无值 | result = None |


### 2. 运算符关键字


用于逻辑和布尔运算：


| 关键字 | 说明 | 示例 |
| --- | --- | --- |
| and | 逻辑与 | if x > 0 and x |
| or | 逻辑或 | if x 100: |
| not | 逻辑非 | if not is_valid: |
| is | 对象标识比较 | if x is None: |
| in | 成员测试 | if 'a' in 'apple': |


### 3. 控制流关键字


控制程序执行流程：


| 关键字 | 说明 | 示例 |
| --- | --- | --- |
| if | 条件语句 | if x > 0: print("Positive") |
| elif | 否则如果 | elif x == 0: print("Zero") |
| else | 否则 | else: print("Negative") |
| for | 循环语句 | for i in range(5): |
| while | 循环语句 | while x > 0: |
| break | 跳出循环 | break |
| continue | 继续下一轮循环 | continue |


### 4. 函数与类相关关键字


用于定义和操作函数与类：


| 关键字 | 说明 | 示例 |
| --- | --- | --- |
| def | 定义函数 | def my_func(): |
| return | 函数返回值 | return x + y |
| lambda | 匿名函数 | f = lambda x: x**2 |
| class | 定义类 | class MyClass: |
| pass | 空语句占位符 | pass |


### 5. 异常处理关键字


处理程序中的异常：


| 关键字 | 说明 | 示例 |
| --- | --- | --- |
| try | 尝试执行代码块 | try: |
| except | 捕获异常 | except ValueError: |
| finally | 无论是否异常都执行 | finally: |
| raise | 抛出异常 | raise ValueError("Invalid") |


### 6. 导入与模块关键字


管理模块和导入：


| 关键字 | 说明 | 示例 |
| --- | --- | --- |
| import | 导入模块 | import math |
| from | 从模块导入特定内容 | from math import sqrt |
| as | 别名 | import numpy as np |


### 7. 变量作用域关键字


控制变量作用域：


| 关键字 | 说明 | 示例 |
| --- | --- | --- |
| global | 声明全局变量 | global count |
| nonlocal | 声明非局部变量 | nonlocal x |


### 8. 异步编程关键字


(Python 3.5+新增)：


| 关键字 | 说明 | 示例 |
| --- | --- | --- |
| async | 定义异步函数 | async def fetch(): |
| await | 等待异步操作完成 | await response |


### 9. 其他关键字


| 关键字 | 说明 | 示例 |
| --- | --- | --- |
| del | 删除引用 | del my_list[0] |
| with | 上下文管理 | with open('file') as f: |
| yield | 生成器返回值 | yield x |
| assert | 断言条件为真 | assert x > 0 |


---


## 关键字的正确使用


### 1. 不能作为标识符


尝试使用关键字作为变量名会导致语法错误：


## 实例


```python
# 错误示例
class = "Computer Science"  # SyntaxError
```


### 2. 注意大小写


Python关键字都是小写的，但大小写不同的单词可以作为标识符：


## 实例


```python
# 这是允许的
Class = "Math"  # 不是关键字
```


### 3. 上下文正确性


每个关键字都有特定的使用上下文，错误使用会导致语法错误：


## 实例


```python
# 错误示例
def = 5  # SyntaxError
```


### 4. 组合使用


许多关键字需要组合使用才能发挥完整功能：


## 实例


```python
# if-elif-else组合
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```


---


## 实际应用示例


### 示例1：控制流关键字应用


## 实例


```python
# 判断成绩等级
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'

print(f"成绩等级: {grade}")
```


### 示例2：函数与异常处理


## 实例


```python
# 计算平方根的安全函数
import math

def safe_sqrt(x):
    try:
        result = math.sqrt(x)
    except ValueError:
        print("不能计算负数的平方根")
        result = None
    finally:
        print("计算完成")
    return result

print(safe_sqrt(4))  # 2.0
print(safe_sqrt(-1)) # 不能计算负数的平方根\nNone
```


### 示例3：上下文管理器


## 实例


```python
# 使用with关键字自动管理文件资源
with open('example.txt', 'w') as f:
    f.write("Hello, Python Keywords!")
# 文件会自动关闭，无需手动调用f.close()
```


---


## 常见错误与注意事项


**1、误用关键字作为变量名**


## 实例


```python
# 错误
from = "Beijing"

# 正确
origin = "Beijing"
```


**2、忘记冒号**


## 实例


```python
# 错误
if x > 0
    print("Positive")

# 正确
if x > 0:
    print("Positive")
```


**3、不完整的控制结构**


## 实例


```python
# 错误 - 缺少else或elif
if x > 0:
elif x == 0:

# 正确
if x > 0:
    pass
elif x == 0:
    pass
```


**4、不正确的缩进**


## 实例


```python
# 错误
if x > 0:
print("Positive")  # 缺少缩进

# 正确
if x > 0:
    print("Positive")
```


**5、版本差异**



- Python 2.x 有 print 和 exec 作为关键字
- Python 3.x 中 print 和 exec 是内置函数，不再是关键字
- async 和 await 是 Python 3.5+ 新增的关键字


[![Python3 基础语法](https://www.runoob.com/images/up.gif) Python3 基础语法](https://www.runoob.com/python3-basic-syntax.html)









	  AI 思考中...





			** [Python with 关键字](https://www.runoob.com/python3-with-keyword.html)
			[Python 虚拟环境创建（venv）](https://www.runoob.com/python-venv.html) **













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
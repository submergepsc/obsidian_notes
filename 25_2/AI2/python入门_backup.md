# Python 入门全景指南
Python 是一门**易读、通用、生态丰富**的编程语言，常用于自动化脚本、数据分析、人工智能、Web 开发、爬虫、测试与办公效率工具。Python 官方教程覆盖了语言语法、数据结构、模块、输入输出、异常、类等核心内容；截至 **2026 年 5 月**，Python 官方主页显示最新版为 **Python 3.14.5**。初学者应学习 **Python 3**，不再学习 Python 2。([Python documentation](https://docs.python.org/3/tutorial/index.html?utm_source=chatgpt.com "The Python Tutorial — Python 3.14.5 documentation"))
## 1. 学 Python 到底是在学什么？
学习 Python，可以分为四层： 

| 层次   | 内容              | 目标              |
| ---- | --------------- | --------------- |
| 基础语法 | 变量、判断、循环、函数     | 能写简单程序          |
| 数据处理 | 字符串、列表、字典、文件    | 能处理现实中的数据       |
| 工程能力 | 模块、异常、虚拟环境、调试   | 能写规范的小项目        |
| 应用方向 | 自动化、数据分析、AI、Web | 用 Python 解决实际问题 |

初学阶段最重要的不是背语法，而是形成这条思路：
> **输入数据 → 处理数据 → 输出结果**
例如：读取用户输入的成绩，判断是否及格，再输出提示。
# 2. 安装与运行 Python
## 2.1 安装 Python
从 Python 官方下载页面安装最新版 Python 3。Windows 安装时应勾选 **Add Python to PATH**，方便在终端中直接运行 `python` 或 `py`。官方文档与下载页面均提供了适用于不同操作系统的安装入口。([Python.org](https://www.python.org/downloads/?utm_source=chatgpt.com "Download Python"))
安装后，在终端中检查：
```bash
python --version
```
Windows 也可能使用：
```bash
py --version
```
看到类似以下内容，即表示安装成功：
```text
Python 3.14.5
```
## 2.2 两种运行方式
### 方式一：交互式解释器
在终端输入：
```bash
python
```
然后直接输入代码：
```python
>>> 1 + 2
3
>>> print("Hello, Python!")
Hello, Python!
```
适合快速测试语法。
### 方式二：运行 `.py` 文件
创建文件 `hello.py`：
```python
print("Hello, Python!")
```
运行：
```bash
python hello.py
```
真实项目通常都采用这种方式。
## 2.3 推荐编辑器
初学者常用：

| 工具               | 特点             |
| ---------------- | -------------- |
| IDLE             | Python 自带，简单直接 |
| VS Code          | 轻量、插件丰富，适合长期使用 |
| PyCharm          | 功能完整，适合较大项目    |
| Jupyter Notebook | 适合数据分析和逐段执行代码  |

# 3. 第一个 Python 程序
```python
name = input("请输入你的名字：")
print(f"你好，{name}，欢迎学习 Python！")
```
运行示例：
```text
请输入你的名字：小明
你好，小明，欢迎学习 Python！
```
这里包含三个重要概念：

|代码|含义|
|---|---|
|`name = ...`|把数据保存到变量中|
|`input()`|接收用户输入|
|`print()`|输出结果|
|`f"你好，{name}"`|将变量插入字符串|

# 4. Python 的语法特点
## 4.1 缩进非常重要
Python 使用**缩进**表示代码块，而不是 `{}`。
```python
age = 18
if age >= 18:
    print("你已经成年")
    print("可以独立承担法律责任")
```
错误示例：
```python
if age >= 18:
print("你已经成年")
```
这会触发缩进错误。
通常使用 **4 个空格**进行一级缩进，这也是 Python 社区的标准风格建议。([Python documentation](https://docs.python.org/3/tutorial/index.html?utm_source=chatgpt.com "The Python Tutorial — Python 3.14.5 documentation"))
## 4.2 注释
```python
# 这是单行注释
price = 99  # 商品价格
```
多行说明通常使用三引号字符串：
```python
"""
这是程序说明。
可以写多行内容。
"""
```
# 5. 变量与基本数据类型
变量用于保存数据：
```python
name = "Alice"
age = 20
height = 1.68
is_student = True
```
## 5.1 常见数据类型
```python3
print("hello")
```

| 类型      | 含义  | 示例             |
| ------- | --- | -------------- |
| `int`   | 整数  | `18`、`-3`      |
| `float` | 小数  | `3.14`、`1.68`  |
| `str`   | 字符串 | `"Python"`     |
| `bool`  | 布尔值 | `True`、`False` |
| `None`  | 空值  | `None`         |

查看变量类型：
```python
age = 20
print(type(age))
```
输出：
```text
<class 'int'>
```
## 5.2 变量命名规则
正确示例：
```python
user_name = "Tom"
score1 = 95
total_price = 128.5
```
错误示例：
```python
1score = 95       # 不能数字开头
user-name = "Tom" # 连字符会被当成减号
class = "A"       # class 是关键字
```
推荐使用小写字母与下划线：
```python
student_score = 90
```
# 6. 运算符
## 6.1 算术运算
```python
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3，整除
print(a % b)   # 1，余数
print(a ** b)  # 1000，幂运算
```
## 6.2 比较运算
```python
print(10 > 3)   # True
print(10 == 3)  # False
print(10 != 3)  # True
```
注意：
```python
x = 10   # 赋值
x == 10  # 比较是否相等
```
## 6.3 逻辑运算
```python
age = 20
has_ticket = True
print(age >= 18 and has_ticket)  # True
print(age < 18 or has_ticket)    # True
print(not has_ticket)            # False
```
# 7. 字符串
字符串是文本数据：
```python
text = "Python 入门"
```
## 7.1 字符串操作
```python
name = "Python"
print(name[0])        # P
print(name[-1])       # n
print(name[0:3])      # Pyt
print(len(name))      # 6
print(name.lower())   # python
print(name.upper())   # PYTHON
```
## 7.2 字符串拼接
```python
first_name = "三"
last_name = "张"
full_name = last_name + first_name
print(full_name)  # 张三
```
更推荐使用格式化字符串：
```python
name = "张三"
score = 95
print(f"{name}的成绩是{score}分")
```
## 7.3 常用方法
```python
sentence = "  hello python  "
print(sentence.strip())              # 去除两侧空格
print(sentence.replace("python", "world"))
print("apple,banana,orange".split(","))
```
# 8. 条件判断
条件判断用于根据不同情况执行不同代码。
```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```
执行逻辑：
```text
如果 score >= 90     → 优秀
否则如果 score >= 60 → 及格
否则                 → 不及格
```
## 小案例：判断奇偶数
```python
number = int(input("请输入一个整数："))
if number % 2 == 0:
    print("这是偶数")
else:
    print("这是奇数")
```
注意：`input()` 得到的是字符串，因此需要用 `int()` 转为整数。
# 9. 循环
循环用于重复执行代码。
## 9.1 `for` 循环
```python
for i in range(5):
    print(i)
```
输出：
```text
0
1
2
3
4
```
常见写法：
```python
for i in range(1, 6):
    print(i)
```
输出 1 到 5。
## 9.2 遍历列表
```python
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)
```
## 9.3 `while` 循环
```python
count = 1
while count <= 3:
    print(count)
    count += 1
```
## 9.4 `break` 与 `continue`
```python
for number in range(1, 10):
    if number == 5:
        break
    print(number)
```
输出到 4 后结束。
```python
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
```
跳过 3。
# 10. 列表、元组、字典、集合
这些是 Python 中最重要的数据结构。
## 10.1 列表 `list`
列表可以保存多个数据，并且可以修改。
```python
scores = [90, 85, 76]
print(scores[0])     # 90
scores.append(88)    # 添加元素
scores.remove(85)    # 删除元素
scores[0] = 100      # 修改元素
print(scores)
```
常用操作：
```python
numbers = [3, 1, 4, 2]
print(len(numbers))    # 长度
print(max(numbers))    # 最大值
print(min(numbers))    # 最小值
print(sum(numbers))    # 求和
numbers.sort()
print(numbers)         # [1, 2, 3, 4]
```
## 10.2 元组 `tuple`
元组与列表类似，但创建后通常不可修改。
```python
point = (10, 20)
print(point[0])
```
适合表示固定结构的数据，例如坐标、日期。
## 10.3 字典 `dict`
字典以“键值对”形式保存数据。
```python
student = {
    "name": "小明",
    "age": 18,
    "score": 92
}
print(student["name"])
print(student["score"])
student["score"] = 95
student["city"] = "北京"
```
遍历字典：
```python
for key, value in student.items():
    print(key, value)
```
## 10.4 集合 `set`
集合中的元素不重复。
```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}
```
去重案例：
```python
names = ["张三", "李四", "张三", "王五"]
unique_names = set(names)
print(unique_names)
```
# 11. 函数
函数用于把一段可复用逻辑封装起来。
## 11.1 定义函数
```python
def greet(name):
    print(f"你好，{name}！")
greet("小明")
greet("小红")
```
## 11.2 返回值
```python
def add(a, b):
    return a + b
result = add(3, 5)
print(result)  # 8
```
## 11.3 默认参数
```python
def greet(name, message="你好"):
    print(f"{message}，{name}")
greet("小明")
greet("小红", "欢迎回来")
```
## 11.4 为什么要使用函数？
没有函数时：
```python
price1 = 100
discount_price1 = price1 * 0.8
price2 = 200
discount_price2 = price2 * 0.8
```
使用函数后：
```python
def calculate_discount(price, discount=0.8):
    return price * discount
print(calculate_discount(100))
print(calculate_discount(200))
```
优点是代码更清晰、更容易复用和修改。
# 12. 列表推导式
列表推导式可以简洁地生成列表。
普通写法：
```python
squares = []
for number in range(1, 6):
    squares.append(number ** 2)
print(squares)
```
列表推导式写法：
```python
squares = [number ** 2 for number in range(1, 6)]
print(squares)
```
加入条件：
```python
even_numbers = [number for number in range(1, 11) if number % 2 == 0]
print(even_numbers)
```
初学阶段应先理解普通循环，再逐步使用列表推导式。
# 13. 模块与导入
一个 Python 文件可以导入其他文件或标准库中的功能。
## 13.1 使用标准库
```python
import math
print(math.sqrt(16))  # 4.0
print(math.pi)
```
```python
import random
number = random.randint(1, 10)
print(number)
```
```python
from datetime import datetime
now = datetime.now()
print(now)
```
Python 自带大量标准库，例如数学计算、日期时间、文件处理、JSON、随机数等；官方文档将这些内容集中在标准库参考中。([Python documentation](https://docs.python.org/?utm_source=chatgpt.com "3.14.5 Documentation"))
## 13.2 自己创建模块
创建文件 `calculator.py`：
```python
def add(a, b):
    return a + b
```
另一个文件 `main.py`：
```python
import calculator
print(calculator.add(3, 5))
```
# 14. 文件读写
程序经常需要保存数据或读取文件。
## 14.1 写入文件
```python
with open("note.txt", "w", encoding="utf-8") as file:
    file.write("今天开始学习 Python。\n")
    file.write("坚持练习。")
```
## 14.2 读取文件
```python
with open("note.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)
```
## 14.3 追加内容
```python
with open("note.txt", "a", encoding="utf-8") as file:
    file.write("\n今天学习了文件操作。")
```
`with open(...)` 的好处是代码块结束后会自动关闭文件。
# 15. 异常处理
程序运行时可能出错，例如用户输入了非数字内容。
没有异常处理：
```python
age = int(input("请输入年龄："))
print(age)
```
用户输入 `"abc"` 时，程序会报错退出。
加入异常处理：
```python
try:
    age = int(input("请输入年龄："))
    print(f"你的年龄是 {age}")
except ValueError:
    print("输入错误，请输入整数。")
```
常见异常：

|异常|含义|
|---|---|
|`ValueError`|值的格式不正确|
|`TypeError`|数据类型不匹配|
|`FileNotFoundError`|文件不存在|
|`ZeroDivisionError`|除数为零|
|`KeyError`|字典中没有指定键|

案例：
```python
try:
    a = int(input("请输入被除数："))
    b = int(input("请输入除数："))
    print(a / b)
except ValueError:
    print("必须输入整数")
except ZeroDivisionError:
    print("除数不能为 0")
```
# 16. 面向对象基础
面向对象编程通过“类”和“对象”组织代码。
## 16.1 类与对象
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def introduce(self):
        print(f"我是{self.name}，成绩是{self.score}分")
student1 = Student("小明", 92)
student1.introduce()
```
含义：

|概念|示例|说明|
|---|---|---|
|类|`Student`|学生这种事物的模板|
|对象|`student1`|一个具体学生|
|属性|`name`、`score`|对象的数据|
|方法|`introduce()`|对象能够执行的行为|

## 16.2 什么时候需要类？
小脚本未必需要类。
适合使用类的情况包括：
- 学生管理系统中的学生、课程、成绩；
- 游戏中的玩家、怪物、装备；
- 电商系统中的用户、商品、订单；
- 图书管理系统中的图书、读者、借阅记录。
# 17. 安装第三方库与虚拟环境
Python 强大的重要原因之一，是可以安装大量第三方库，例如：

|方向|常见库|
|---|---|
|数据分析|`pandas`、`numpy`|
|绘图|`matplotlib`|
|网络请求|`requests`|
|Web 开发|`flask`、`django`、`fastapi`|
|人工智能|`pytorch`、`scikit-learn`|

## 17.1 使用 `pip` 安装库
```bash
python -m pip install requests
```
在程序中使用：
```python
import requests
```
## 17.2 为什么要使用虚拟环境？
不同项目可能依赖不同版本的库。虚拟环境可以让每个项目拥有独立的依赖，避免相互冲突。Python Packaging User Guide 推荐使用 `venv` 创建虚拟环境，再使用 `pip` 安装依赖。([Python 打包用户指南](https://packaging.python.org/tutorials/installing-packages/?utm_source=chatgpt.com "Installing Packages - Python Packaging User Guide"))
创建虚拟环境：
```bash
python -m venv .venv
```
激活环境：
**Windows：**
```bash
.venv\Scripts\activate
```
**macOS / Linux：**
```bash
source .venv/bin/activate
```
安装库：
```bash
python -m pip install requests
```
查看已安装库：
```bash
python -m pip list
```
保存项目依赖：
```bash
python -m pip freeze > requirements.txt
```
根据依赖文件安装：
```bash
python -m pip install -r requirements.txt
```
# 18. 一个完整入门项目：成绩统计程序
下面的程序综合使用了输入、列表、循环、判断、函数与异常处理。
```python
def calculate_average(scores):
    return sum(scores) / len(scores)
def get_grade(average):
    if average >= 90:
        return "优秀"
    elif average >= 80:
        return "良好"
    elif average >= 60:
        return "及格"
    else:
        return "不及格"
scores = []
print("请输入三门课程成绩：")
for i in range(3):
    while True:
        try:
            score = float(input(f"第 {i + 1} 门成绩："))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print("成绩必须在 0 到 100 之间。")
        except ValueError:
            print("请输入数字。")
average = calculate_average(scores)
grade = get_grade(average)
print(f"总分：{sum(scores):.1f}")
print(f"平均分：{average:.1f}")
print(f"评价：{grade}")
```
可能的运行结果：
```text
请输入三门课程成绩：
第 1 门成绩：92
第 2 门成绩：88
第 3 门成绩：95
总分：275.0
平均分：91.7
评价：优秀
```
这个项目体现了真实编程中的几个重要原则：
- 使用函数拆分逻辑；
- 验证用户输入；
- 对可能出现的错误进行处理；
- 使用清晰的变量名；
- 输出易读的结果。
# 19. Python 代码规范与调试习惯
## 19.1 良好的命名
不推荐：
```python
a = 95
b = 3
c = a / b
```
推荐：
```python
total_score = 95
subject_count = 3
average_score = total_score / subject_count
```
## 19.2 保持函数职责单一
不推荐把所有逻辑写在一个巨大代码块里。
推荐：
```python
def read_scores():
    pass
def calculate_average(scores):
    pass
def display_result(average):
    pass
```
## 19.3 多使用调试输出
```python
numbers = [1, 2, 3]
print("当前数据：", numbers)
```
也可以使用编辑器的断点调试功能，逐行观察变量变化。
## 19.4 常见代码风格
```python
# 变量和函数使用小写加下划线
student_name = "小明"
def calculate_score():
    pass
# 类名使用大驼峰
class StudentManager:
    pass
```
# 20. 初学者常见错误
|错误|问题|解决方法|
|---|---|---|
|忘记缩进|`IndentationError`|使用统一的 4 空格缩进|
|把 `=` 当作比较|判断结果错误|比较时使用 `==`|
|`input()` 后直接计算|输入是字符串|使用 `int()` 或 `float()` 转换|
|列表索引越界|`IndexError`|注意索引从 `0` 开始|
|文件不存在|`FileNotFoundError`|检查路径或使用异常处理|
|忘记安装库|`ModuleNotFoundError`|使用 `pip install`|
|不使用虚拟环境|项目依赖混乱|每个项目建立 `.venv`|

# 21. 应该按什么顺序学习？
## 第一阶段：基础语法
目标：能看懂并写出简单程序。
学习内容：
1. 安装与运行 Python；
2. 变量、数据类型；
3. 输入输出；
4. 条件判断；
5. 循环；
6. 函数。
练习项目：
- BMI 计算器；
- 猜数字游戏；
- 成绩等级判断；
- 简单计算器。
## 第二阶段：数据处理
目标：能处理成组数据和文件。
学习内容：
1. 字符串；
2. 列表、元组、字典、集合；
3. 文件读写；
4. 异常处理；
5. 模块导入。
练习项目：
- 通讯录程序；
- 单词统计器；
- 记账程序；
- 待办事项清单。
## 第三阶段：工程入门
目标：能组织一个规范的小项目。
学习内容：
1. 类与对象；
2. 第三方库；
3. 虚拟环境；
4. 项目目录结构；
5. 调试；
6. 基础测试；
7. Git 基础。
练习项目：
- 图书管理系统；
- 学生成绩管理系统；
- 自动整理文件工具；
- 简单爬虫或接口请求工具。
## 第四阶段：选择方向
|方向|后续学习内容|
|---|---|
|自动化办公|`pathlib`、`openpyxl`、`python-docx`、邮件处理|
|数据分析|`numpy`、`pandas`、`matplotlib`、Jupyter|
|人工智能|数学基础、`numpy`、`pytorch`、机器学习|
|Web 开发|HTML/CSS、HTTP、`Flask` / `Django` / `FastAPI`|
|网络爬虫|`requests`、HTML、`BeautifulSoup`、浏览器自动化|
|测试开发|`pytest`、接口测试、自动化测试|

# 22. 入门阶段建议掌握的知识清单
学完基础后，应当能够独立写出以下代码：
```python
# 变量
name = "Python"
# 判断
if name == "Python":
    print("正在学习 Python")
# 循环
for number in range(3):
    print(number)
# 列表
numbers = [1, 2, 3]
numbers.append(4)
# 字典
user = {"name": "Alice", "age": 20}
# 函数
def square(number):
    return number ** 2
# 文件读取
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
# 异常处理
try:
    value = int("123")
except ValueError:
    print("转换失败")
# 类
class Person:
    def __init__(self, name):
        self.name = name
```
# 23. 高效学习方法
## 不要只看，要写
阅读一段代码后，立即自己手写一次，并修改其中的数据和逻辑。
例如，学习了判断语句后，不要只看：
```python
if score >= 60:
    print("及格")
```
应立即扩展为：
```python
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("继续努力")
```
## 不要一开始追求大项目
适合初学者的项目应当能在几十行代码内完成：
- 计算器；
- 猜数字；
- 温度转换；
- 成绩统计；
- 待办清单；
- 记账小程序。
## 遇到错误要学会读报错
例如：
```text
ValueError: invalid literal for int()
```
通常意味着：程序尝试把无法转换成整数的字符串交给了 `int()`。
报错信息不是障碍，而是定位问题的入口。
# 24. 一份 14 天入门安排
|天数|学习内容|实践任务|
|---|---|---|
|第 1 天|安装、运行、`print()`、变量|输出个人信息|
|第 2 天|数字、字符串、输入|BMI 计算器|
|第 3 天|比较与逻辑运算|年龄判断程序|
|第 4 天|`if / elif / else`|成绩等级判断|
|第 5 天|`for` 循环|九九乘法表|
|第 6 天|`while` 循环|猜数字游戏|
|第 7 天|列表与字符串|成绩统计|
|第 8 天|字典与集合|通讯录数据结构|
|第 9 天|函数|重构前面的小程序|
|第 10 天|文件读写|保存待办事项|
|第 11 天|异常处理|处理非法输入|
|第 12 天|模块、第三方库|使用 `requests` 或随机模块|
|第 13 天|类与对象|学生类|
|第 14 天|综合项目|命令行待办清单|

# 25. 最重要的结论
Python 入门的核心路线是：
```text
安装环境
  ↓
变量与数据类型
  ↓
判断与循环
  ↓
列表、字典、字符串
  ↓
函数
  ↓
文件与异常
  ↓
模块、虚拟环境
  ↓
面向对象
  ↓
完整小项目
  ↓
选择应用方向
```
你不需要先掌握所有知识再开始项目。最有效的方式是：
> **学一个概念，写一个例子；学几个概念，做一个小项目。**
官方 Python 教程适合作为长期参考；安装第三方库和虚拟环境时，可参考 Python Packaging User Guide 的 `pip` 与 `venv` 指南。([Python documentation](https://docs.python.org/3/tutorial/index.html?utm_source=chatgpt.com "The Python Tutorial — Python 3.14.5 documentation"))
下一步可以直接回复 **“从第一课开始”**，我将从安装、运行与第一个程序开始，带你边学边练。
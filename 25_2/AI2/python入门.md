# Python 入门全景指南
Python 是一门**易读、通用、生态丰富**的编程语言，常用于自动化脚本、数据分析、人工智能、Web 开发、爬虫、测试与办公效率工具。截至 **2026 年 5 月**，Python 官方主页显示最新版为 **Python 3.14.5**。初学者应学习 **Python 3**，不再学习 Python 2。([Python documentation](https://docs.python.org/3/tutorial/index.html "The Python Tutorial"))
Python 的设计哲学是**可读性优先**。在 Python 解释器中输入 `import this` 可以看到「Python 之禅」，其核心包括：
- **优美胜于丑陋**（Beautiful is better than ugly）
- **显式胜于隐式**（Explicit is better than implicit）
- **简单胜于复杂**（Simple is better than complex）
- **可读性很重要**（Readability counts）
这些原则影响着 Python 语言每一个设计决策，也是为什么 Python 代码看起来像「可执行的伪代码」。
### Python 与其他语言对比
| 特性 | Python | C/C++ | Java | JavaScript |
|------|--------|-------|------|------------|
| 类型系统 | 动态类型 | 静态类型 | 静态类型 | 动态类型 |
| 编译方式 | 解释型 | 编译型 | 编译+JIT | JIT编译 |
| 内存管理 | 自动GC | 手动管理 | 自动GC | 自动GC |
| 语法复杂度 | 低 | 高 | 中 | 中 |
| 运行速度 | 较慢 | 很快 | 较快 | 较快 |
| 学习曲线 | 平缓 | 陡峭 | 中等 | 中等 |
| 典型应用 | AI/数据/脚本 | 系统/游戏/嵌入式 | 企业/安卓 | Web全栈 |

## 1. 学 Python 到底是在学什么？
学习 Python，可以分为**四个层次**加一条**贯穿暗线**：

| 层次 | 内容 | 目标 |
| ---- | ---- | ---- |
| 基础语法 | 变量、判断、循环、函数 | 能写简单程序 |
| 数据处理 | 字符串、列表、字典、文件 | 能处理现实中的数据 |
| 工程能力 | 模块、异常、虚拟环境、调试、测试 | 能写规范的小项目 |
| 应用方向 | 自动化、数据分析、AI、Web | 用 Python 解决实际问题 |

**贯穿四层的暗线——编程思维**：
- **分解**：把大问题拆成小步骤，每个步骤用一个函数实现
- **抽象**：识别重复模式，封装成函数和类
- **调试**：用 `print()`、断点、日志定位错误
- **测试**：用不同输入验证代码的正确性
初学阶段最重要的不是背语法，而是形成这条思路：
> **输入数据 → 处理数据 → 输出结果**
例如：读取用户输入的成绩 → 判断是否及格 → 输出提示。几乎所有的程序都在重复这个模式。
### 1.1 一个完整的「输入→处理→输出」示例
```python
# 输入
name = input("请输入你的名字：")
score = float(input("请输入你的成绩："))
# 处理
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
# 输出
print(f"{name}同学，你的成绩是{score}分，等级：{grade}")
```
这个 10 行的程序已经包含了变量、输入、类型转换、条件判断、f-string 格式化输出——入门阶段的核心概念全部在内。
# 2. 安装与运行 Python
## 2.1 安装 Python
### Windows
从 [python.org/downloads](https://www.python.org/downloads/) 下载安装包。安装时**务必勾选** `Add Python to PATH`，这样才能在终端中直接使用 `python` 命令。
验证安装：
```bash
python --version
# 或
py --version
```
### macOS
macOS 自带 Python，但通常是旧版本。推荐使用 Homebrew 安装：
```bash
brew install python@3.14
```
或从官网下载 `.pkg` 安装包。
验证：
```bash
python3 --version
```
### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```
### 多版本管理：pyenv
当你需要在同一台机器上使用多个 Python 版本时（比如同时维护 Python 3.12 和 3.14 项目），推荐使用 `pyenv`：
```bash
# 安装 pyenv
curl https://pyenv.run | bash
# 安装指定版本
pyenv install 3.14.5
# 设置当前目录使用的 Python 版本
pyenv local 3.14.5
```
看到类似以下内容，即表示安装成功：
```text
Python 3.14.5
```
## 2.2 两种运行方式
### 方式一：交互式解释器（REPL）
REPL = Read（读取）→ Evaluate（求值）→ Print（打印）→ Loop（循环）
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
>>> name = "World"
>>> f"Hello, {name}!"
'Hello, World!'
```
适合快速测试语法、探索 API、做简单计算。退出：输入 `exit()` 或按 `Ctrl+D`。
**增强版 REPL**：安装 `ipython` 获得语法高亮、自动补全和历史搜索：
```bash
pip install ipython
ipython
```
### 方式二：运行 `.py` 文件
创建文件 `hello.py`：
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"我的第一个 Python 程序\"\"\"
print("Hello, Python!")
```
运行：
```bash
python hello.py
```
- `#!/usr/bin/env python3`（Shebang）让 Linux/macOS 可以直接 `./hello.py` 运行
- `# -*- coding: utf-8 -*-` 声明文件编码（Python 3 默认 UTF-8，但显式写出来是好习惯）
- `\"\"\"...\"\"\"` 是模块文档字符串（docstring），后面会详细讲
## 2.3 推荐编辑器与 IDE
| 工具 | 特点 | 适合人群 |
| ---- | ---- | -------- |
| IDLE | Python 自带，极简 | 写第一行代码 |
| VS Code + Python 插件 | 轻量、免费、插件丰富 | 绝大多数开发者 |
| PyCharm Community | 免费、智能补全强 | 需要完整 IDE 的开发者 |
| PyCharm Professional | 付费，Web/数据支持完善 | 专业开发者 |
| Jupyter Notebook | 浏览器中逐段执行 | 数据分析、教学演示 |
| JupyterLab | Jupyter 的升级版 | 数据分析、机器学习 |
| Google Colab | 免费云端 GPU | 深度学习入门 |

**推荐搭配**：VS Code + Python 插件 用于日常开发，Jupyter Notebook 用于数据探索。
# 3. 第一个 Python 程序——从零到一
## 3.1 最小程序
```python
name = input("请输入你的名字：")
print(f"你好，{name}，欢迎学习 Python！")
```
运行示例：
```text
请输入你的名字：小明
你好，小明，欢迎学习 Python！
```
这个三行程序包含了四个核心概念：

| 代码 | 概念 | 说明 |
| ---- | ---- | ---- |
| `name = ...` | 变量赋值 | 把数据保存到内存中，起个名字方便后续使用 |
| `input("...")` | 用户输入 | 程序暂停，等待用户键入内容并按回车 |
| `print(...)` | 输出 | 把结果显示到屏幕上 |
| `f"你好，{name}"` | f-string 格式化 | 把变量的值嵌入到字符串中（Python 3.6+） |

## 3.2 理解程序的执行过程
Python 是**解释型语言**：源代码被逐行翻译成字节码，再由 Python 虚拟机执行。
```text
源代码 (.py) → 编译 → 字节码 (.pyc) → PVM 解释执行 → 输出
```
这意味着：
- 不需要编译步骤，写完就能跑
- 错误在执行到那一行时才暴露（不像 C/Java 编译时就检查类型）
- 可以通过 `python -m py_compile hello.py` 手动编译为 `.pyc`
## 3.3 `print()` 深入
```python
# 基本用法
print("Hello")
# 打印多个值（默认空格分隔）
print("答案:", 42, "正确:", True)
# 输出：答案: 42 正确: True
# 自定义分隔符
print("2026", "05", "29", sep="-")
# 输出：2026-05-29
# 自定义结束符（默认换行）
print("Loading", end="...")
print("Done!")
# 输出：Loading...Done!
# 输出到文件
with open("log.txt", "w") as f:
    print("错误信息", file=f)
```
## 3.4 `input()` 深入
```python
# 基本用法
name = input("你的名字：")
# 重要：input() 永远返回字符串！
age = input("你的年龄：")   # 输入 25，得到字符串 "25"
age = int(age)              # 需要手动转换
# 一步到位
age = int(input("你的年龄："))
# 处理空输入
name = input("你的名字（按回车跳过）：") or "匿名用户"
```
## 3.5 f-string 格式化深入
```python
name = "Alice"
score = 95.567
# 基本插值
print(f"姓名：{name}")
# 控制小数位数
print(f"分数：{score:.1f}")     # 95.6
print(f"分数：{score:.2f}")     # 95.57
# 对齐与填充
print(f"[{name:<10}]")   # 左对齐，占10位  [Alice     ]
print(f"[{name:>10}]")   # 右对齐          [     Alice]
print(f"[{name:^10}]")   # 居中            [  Alice   ]
# 千位分隔
n = 1000000
print(f"{n:,}")          # 1,000,000
# 百分比
rate = 0.856
print(f"{rate:.1%}")     # 85.6%
# 表达式
a, b = 3, 5
print(f"{a} + {b} = {a + b}")  # 3 + 5 = 8
# 调用函数
print(f"大写：{name.upper()}")  # 大写：ALICE
# 日期格式化
from datetime import datetime
now = datetime.now()
print(f"{now:%Y-%m-%d %H:%M:%S}")
```
# 4. Python 的语法特点
## 4.1 缩进：Python 的灵魂
Python 使用**缩进**表示代码块，而不是 `{}` 或 `begin/end`。这是 Python 最独特的设计。
```python
age = 18
if age >= 18:
    print("你已经成年")
    print("可以独立承担法律责任")
    if age >= 65:
        print("你已退休")
print("判断结束")  # 这一行不在 if 内部
```
**核心规则**：
- 同一代码块必须有相同的缩进量
- Python 社区标准：**4 个空格**（不要混用 Tab 和空格）
- VS Code / PyCharm 会自动把 Tab 转成 4 空格
错误示例：
```python
if age >= 18:
print("你已经成年")  # IndentationError!
```
```python
if age >= 18:
    print("成年")
   print("OK")  # 缩进不一致 → IndentationError!
```
**建议**：编辑器设置中开启「显示空白字符」，缩进错误一目了然。
## 4.2 注释
```python
# 这是单行注释
price = 99  # 行末注释
# 多行注释通常用连续的单行注释
# 第一行说明
# 第二行说明
```
多行字符串（三引号）常被用作文档字符串（docstring），放在函数/类/模块的开头：
```python
def calculate_discount(price, rate=0.8):
    \"\"\"
    计算折扣价格。
    参数：
        price (float): 原价
        rate (float): 折扣率，默认 0.8
    返回：
        float: 折扣后的价格
    示例：
        >>> calculate_discount(100)
        80.0
    \"\"\"
    return price * rate
```
## 4.3 语句分隔
```python
# 通常一行一条语句
x = 1
y = 2
# 分号可以把多条语句放在一行（不推荐）
x = 1; y = 2
# 长语句用反斜杠续行
total = 1 + 2 + 3 + \\
        4 + 5 + 6
# 括号内可以自动续行（推荐）
total = (1 + 2 + 3 +
         4 + 5 + 6)
# 长字符串用三引号
message = \"\"\"这是一段很长的文字，
可以跨越多行，
非常方便。\"\"\"
```
# 5. 变量与基本数据类型
## 5.1 变量：给数据贴标签
```python
name = "Alice"       # 字符串
age = 20             # 整数
height = 1.68        # 浮点数
is_student = True    # 布尔值
data = None          # 空值
```
Python 是**动态类型**语言：变量不需要声明类型，运行时自动推断。同一个变量可以先后指向不同类型的数据（但不推荐这样写）：
```python
x = 10       # x 是 int
x = "hello"  # 现在是 str（合法但不推荐）
```
**变量赋值的本质**：变量名指向内存中的一个对象。`a = 10` 表示创建整数对象 `10`，并让名字 `a` 指向它。
```python
a = [1, 2, 3]
b = a          # b 指向同一个列表！
b.append(4)
print(a)       # [1, 2, 3, 4] ← a 也被修改了！
```
这是理解 Python 变量行为的关键：**赋值不复制数据，只是多一个名字引用同一对象**。
### 查看对象身份和类型
```python
x = [1, 2, 3]
print(type(x))   # <class 'list'>
print(id(x))     # 对象在内存中的唯一编号
print(isinstance(x, list))  # True，推荐的类型检查方式
```
## 5.2 常见数据类型
| 类型 | 含义 | 示例 | 可变？ |
| ---- | ---- | ---- | ------ |
| `int` | 整数（任意精度） | `18`、`-3`、`10**100` | 不可变 |
| `float` | 双精度浮点数 | `3.14`、`1.68`、`1e-5` | 不可变 |
| `complex` | 复数 | `3+4j` | 不可变 |
| `str` | 字符串 | `"Python"`、`'你好'` | 不可变 |
| `bool` | 布尔值 | `True`、`False` | 不可变 |
| `NoneType` | 空值 | `None` | 不可变 |

**关于「不可变」与「可变」**：
- 不可变对象：创建后内容不能改变。修改操作实际是创建新对象。
- 可变对象（`list`、`dict`、`set`）：内容可以原地修改。
- 这个概念在后面函数传参和默认参数陷阱中非常关键。
### 数字类型深入
```python
# int 是任意精度的（不像 C 有 32/64 位限制）
big = 10 ** 100
print(big)  # 100000000000000000000000000...（100个零）
# 不同进制的表示
bin_num = 0b1010    # 二进制：10
oct_num = 0o12      # 八进制：10
hex_num = 0xA       # 十六进制：10
print(bin(42))      # '0b101010'
print(hex(255))     # '0xff'
# float 是 IEEE 754 双精度（约15位有效数字）
# 注意浮点数精度问题：
print(0.1 + 0.2)           # 0.30000000000000004
print(0.1 + 0.2 == 0.3)    # False!
# 解决方案：使用 decimal 做精确小数运算
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))  # 0.3
# 布尔值是 int 的子类
print(True + True)   # 2
print(True == 1)     # True
print(isinstance(True, int))  # True
```
### 类型转换（强制转换）
```python
int("42")         # 42
int(3.9)          # 3（截断，不四舍五入）
int("1010", 2)    # 10（指定进制）
float("3.14")     # 3.14
str(42)           # "42"
bool(0)           # False
bool([])          # False
bool("hello")     # True
list("abc")       # ['a', 'b', 'c']
```
**「假值」规则**：以下值在布尔上下文中被视为 `False`：
- `False`、`0`、`0.0`、`""`（空字符串）、`[]`（空列表）、`{}`（空字典）、`()`（空元组）、`set()`（空集合）、`None`
其余所有值都是 `True`。
## 5.3 变量命名规则
**合法规则**：
- 只能包含字母（中英文均可）、数字、下划线
- 不能以数字开头
- 不能是 Python 关键字
```python
# 正确
user_name = "Tom"
score1 = 95
数据 = [1, 2, 3]  # 支持中文变量名，但生产代码不推荐
_private = "内部变量"
# 错误
1score = 95       # 数字开头 ❌
user-name = "Tom" # 连字符是减号 ❌
class = "A"       # class 是关键字 ❌
```
**Python 关键字清单**（不能用作变量名）：
```text
False, None, True, and, as, assert, async, await, break,
class, continue, def, del, elif, else, except, finally,
for, from, global, if, import, in, is, lambda, nonlocal,
not, or, pass, raise, return, try, while, with, yield
```
**命名风格规范**（PEP 8）：

| 类型 | 风格 | 示例 |
| ---- | ---- | ---- |
| 变量、函数、方法 | snake_case（小写+下划线） | `student_score`, `calculate_avg` |
| 常量 | UPPER_SNAKE_CASE | `MAX_SIZE`, `DEFAULT_PORT` |
| 类名 | PascalCase（大驼峰） | `StudentManager`, `HttpClient` |
| 私有成员 | 前缀单下划线 `_` | `_internal_method` |
| 名称修饰 | 前缀双下划线 `__` | `__private_attr` |
| 魔术方法 | 双下划线包围 | `__init__`, `__str__` |

```python
# 常量（约定俗成，Python 不做真正强制）
MAX_CONNECTIONS = 100
PI = 3.1415926535
# 有意义的命名胜过简短
# 不好
a, b, c, x1, x2, tmp
# 好
user_age, total_price, average_score, file_path
```
# 6. 运算符
## 6.1 算术运算符
```python
a, b = 10, 3
print(a + b)    # 13  加法
print(a - b)    # 7   减法
print(a * b)    # 30  乘法
print(a / b)    # 3.3333333333333335  除法（总是返回 float）
print(a // b)   # 3   整除（地板除，向下取整）
print(a % b)    # 1   取模（余数）
print(a ** b)   # 1000  幂运算
print(-a)       # -10 取反
```
**`/` vs `//` 的区别**：
```python
print(10 / 3)    # 3.333...（真除法）
print(10 // 3)   # 3（地板除）
# 注意负数：
print(-10 // 3)  # -4（向下取整）
print(-10 // -3) # 3
```
**取模的妙用**：
```python
# 判断奇偶
n % 2 == 0  # 偶数
n % 2 == 1  # 奇数
# 循环索引
for i in range(10):
    print(f"第{i}个，第{i % 3}组")
# 限制范围
minute = total_seconds % 60
```
## 6.2 比较运算符
```python
print(10 > 3)    # True   大于
print(10 >= 3)   # True   大于等于
print(10 < 3)    # False  小于
print(10 <= 3)   # False  小于等于
print(10 == 3)   # False  等于（两个等号！）
print(10 != 3)   # True   不等于
```
**链式比较**（Python 特有）：
```python
x = 5
print(1 < x < 10)    # True，等价于 1 < x and x < 10
print(1 <= x <= 10)  # True
# 常用场景
age = 25
if 18 <= age <= 60:
    print("劳动力年龄")
```
**`is` vs `==`**：
```python
# == 比较「值」是否相等
# is 比较「身份」是否相同（是否同一个对象）
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)  # True  （值相等）
print(a is b)  # False （不同对象）
print(a is c)  # True  （同一个对象）
# 注意：小整数和短字符串会被 Python 缓存
x = 256
y = 256
print(x is y)  # True（Python 缓存了 -5 到 256 的整数）
x = 257
y = 257
print(x is y)  # 可能是 False（超出缓存范围）
# → 判断相等用 ==，不要用 is 判断数值
```
**与 `None` 比较**始终用 `is`：
```python
result = None
if result is None:      # 好
    pass
if result == None:      # 不好（可能被重载）
    pass
```
## 6.3 赋值运算符
```python
x = 10
x += 3    # x = x + 3 → 13
x -= 3    # 10
x *= 2    # 20
x /= 4    # 5.0
x //= 2   # 2
x **= 3   # 8
x %= 3    # 2
```
**海象运算符 `:=`**（Python 3.8+）：
```python
# 在表达式中赋值
# 没有海象运算符时需要两行
n = len(data)
if n > 10:
    print(f"有{n}条数据")
# 海象运算符：一行搞定
if (n := len(data)) > 10:
    print(f"有{n}条数据")
# 另一个常用场景：while 循环
while (line := file.readline().strip()):
    process(line)
```
## 6.4 逻辑运算符
```python
age = 20
has_ticket = True
is_vip = False
# and：两边都为 True 才为 True
print(age >= 18 and has_ticket)   # True
# or：至少一边为 True 即为 True
print(is_vip or has_ticket)       # True
# not：取反
print(not has_ticket)             # False
```
**短路求值**：
```python
# and：左边为 False 就不计算右边
False and 1/0  # 不会报错，因为根本不执行右边
# or：左边为 True 就不计算右边
True or 1/0   # 不会报错
# 利用短路做默认值
name = input("名字：") or "匿名用户"  # 输入为空时用默认值
display_name = name and name.strip()  # name 非空才 strip
```
**逻辑运算符的返回值**（不是 True/False）：
```python
print(3 and 5)    # 5
print(0 and 5)    # 0
print(3 or 5)     # 3
print(0 or 5)     # 5
print(not 3)      # False
```
## 6.5 位运算符（进阶）
```python
a, b = 0b1100, 0b1010  # 12, 10
print(bin(a & b))   # 0b1000  AND
print(bin(a | b))   # 0b1110  OR
print(bin(a ^ b))   # 0b0110  XOR
print(bin(~a))      # 取反
print(bin(a << 1))  # 0b11000 左移 ×2
print(bin(a >> 2))  # 0b11    右移 ÷4
```
位运算常用于权限系统、网络协议、底层优化等场景。
## 6.6 成员运算符 `in`
```python
# 检查元素是否在容器中
print('a' in 'apple')          # True
print('x' not in 'apple')      # True
print(3 in [1, 2, 3])          # True
print('name' in {'name': 'A'}) # True（字典检查键）
# 常见用法
valid_choices = ['y', 'n', 'yes', 'no']
if user_input.lower() in valid_choices:
    process()
```
## 6.7 运算符优先级
从高到低（不要求背诵，拿不准就加括号）：
```text
()                # 括号
**                # 幂
+x, -x, ~x        # 一元
*, /, //, %       # 乘除
+, -              # 加减
<<, >>            # 移位
&                 # 位与
^                 # 位异或
|                 # 位或
==, !=, >, >=, <, <=, is, is not, in, not in  # 比较
not               # 逻辑非
and               # 逻辑与
or                # 逻辑或
:=                # 海象
```
**建议**：不依赖优先级记忆，遇到复杂表达式就用括号明确意图。
# 7. 字符串
字符串是 Python 中最常用的数据类型之一，用于表示文本。Python 的字符串是 **Unicode 编码** 的不可变序列。
## 7.0 字符串的创建与引号
```python
s1 = '单引号'
s2 = "双引号"
s3 = '''三单引号可以跨行'''
s4 = \"\"\"三双引号也可以跨行\"\"\"
# 引号嵌套
quote1 = "他说：'你好'"
quote2 = '他说："你好"'
quote3 = "他说："你好""    # 错误！需要转义
quote4 = "他说：\"你好\""  # 正确，反斜杠转义
```
## 7.1 转义字符
```python
print("第一行\n第二行")     # \n 换行
print("列1\t列2\t列3")     # \t 制表符
print("他说：\"你好\"")     # \" 双引号
print('路径：C:\\Users')    # \\ 反斜杠本身
print("Hello\rWorld")      # \r 回车
# 原始字符串（raw string）：不处理转义
print(r"C:\Users\name")    # 输出 C:\Users\name
path = r"C:\new\text"      # 正则表达式和文件路径常用
```
## 7.2 索引与切片
```python
s = "Python 入门"
# 索引（从 0 开始）
print(s[0])     # P
print(s[1])     # y
print(s[-1])    # 门（倒数第一个）
print(s[-2])    # 入
# 切片 s[start:end:step]
print(s[0:6])     # Python（0到5，不包括6！）
print(s[:6])      # Python（省略 start 默认从 0 开始）
print(s[7:])      # 入门（省略 end 默认到末尾）
print(s[:])       # Python 入门（完整拷贝）
# 步长
print(s[::2])     # Pto 入（每隔一个字符）
print(s[::-1])    # 门入 nohtyP（反转字符串！）
# 索引越界
try:
    print(s[100])
except IndexError as e:
    print(f"索引越界：{e}")
# 切片不会越界（优雅！）
print(s[0:100])   # Python 入门（自动截断）
```
## 7.3 字符串不可变性
```python
s = "hello"
# s[0] = "H"  # ❌ TypeError: 'str' object does not support item assignment
# 正确做法：创建新字符串
s = "H" + s[1:]   # "Hello"
# 如果需要频繁修改字符串，用 list 中转
chars = list(s)
chars[0] = "H"
s = "".join(chars)  # "Hello"
```
## 7.4 字符串拼接
```python
# 方法一：+ 运算符（简单但低效）
name = "张三"
greeting = "你好，" + name
# 方法二：join()（拼接大量字符串时最高效）
words = ["Python", "是", "一门", "好语言"]
sentence = "".join(words)         # "Python是一门好语言"
sentence = " ".join(words)        # "Python 是 一门 好语言"
# 方法三：f-string（最推荐，可读性好）
name = "张三"
score = 95
print(f"{name}的成绩是{score}分")
# 方法四：format()
print("{}的成绩是{}分".format(name, score))
print("{0}的成绩是{1}分，{0}很优秀".format(name, score))  # 复用参数
print("{n}的成绩是{s}分".format(n=name, s=score))        # 命名参数
# 方法五：% 格式化（老式，不推荐新代码使用）
print("%s的成绩是%d分" % (name, score))
```
## 7.5 常用字符串方法
### 大小写转换
```python
print("hello".upper())              # HELLO
print("HELLO".lower())              # hello
print("hello world".title())        # Hello World（每个单词首字母大写）
print("hello world".capitalize())   # Hello world（仅首字母大写）
print("Hello".swapcase())           # hELLO
```
### 空白处理
```python
s = "   hello world   \n"
print(s.strip())        # "hello world"（去除两端空白）
print(s.lstrip())       # 去除左侧空白
print(s.rstrip("\n"))   # 去除右侧指定字符
```
### 查找与替换
```python
s = "hello world, hello python"
print(s.find("hello"))        # 0（首次出现位置，找不到返回 -1）
print(s.rfind("hello"))       # 13（从右查找）
print(s.index("hello"))       # 0（与 find 类似，但找不到会报 ValueError）
print(s.count("hello"))       # 2（出现次数）
print(s.startswith("hello"))  # True
print(s.endswith("python"))   # True
print(s.replace("hello", "hi"))       # "hi world, hi python"
print(s.replace("hello", "hi", 1))    # "hi world, hello python"（只替换 1 次）
```
### 分割与合并
```python
# split()：分割
print("apple,banana,orange".split(","))
# ['apple', 'banana', 'orange']
print("a b   c".split())       # ['a', 'b', 'c']（默认按空格分割，连续空格也合并）
print("line1\nline2\nline3".splitlines())
# ['line1', 'line2', 'line3']
# partition()：三部分分割
before, sep, after = "key=value".partition("=")
print(before, sep, after)     # key = value
# join()：合并
items = ["2026", "05", "29"]
print("-".join(items))        # 2026-05-29
```
### 判断方法
```python
print("123".isdigit())          # True（全是数字）
print("abc".isalpha())          # True（全是字母）
print("abc123".isalnum())       # True（字母或数字）
print("   ".isspace())          # True（全是空白）
print("hello".islower())        # True
print("HELLO".isupper())        # True
```
### 对齐
```python
s = "Python"
print(f"|{s:<10}|")  # |Python    | 左对齐
print(f"|{s:>10}|")  # |    Python| 右对齐
print(f"|{s:^10}|")  # |  Python  | 居中
print(f"|{s:*^10}|") # |**Python**| 居中并填充
# 也可以用方法
print("|" + s.ljust(10) + "|")
print("|" + s.rjust(10) + "|")
print("|" + s.center(10) + "|")
```
## 7.6 字符串编码
```python
# Python 3 中字符串是 Unicode，存储到文件/网络时需要编码为 bytes
s = "你好，世界"
# 编码：str → bytes
utf8_bytes = s.encode("utf-8")
print(utf8_bytes)          # b'\xe4\xbd\xa0\xe5\xa5\xbd\xef\xbc\x8c\xe4\xb8\x96\xe7\x95\x8c'
print(len(utf8_bytes))     # 15（UTF-8 下中文每个 3 字节 + 标点）
gbk_bytes = s.encode("gbk")
print(len(gbk_bytes))      # 10（GBK 下中文每个 2 字节 + 标点）
# 解码：bytes → str
print(utf8_bytes.decode("utf-8"))  # 你好，世界
# 处理编码错误
bad_bytes = b"Hello \xff World"
print(bad_bytes.decode("utf-8", errors="replace"))  # Hello � World
print(bad_bytes.decode("utf-8", errors="ignore"))   # Hello  World
```
## 7.7 高效字符串构建
```python
# ❌ 不好：在循环中反复用 + 拼接（每次都创建新字符串，O(n²)）
result = ""
for i in range(1000):
    result += str(i)
# ✅ 好：用列表收集，最后 join（O(n)）
parts = []
for i in range(1000):
    parts.append(str(i))
result = "".join(parts)
# ✅ 更好：列表推导式 + join
result = "".join(str(i) for i in range(1000))
```
# 8. 条件判断
条件判断用于根据不同情况执行不同代码。这是程序「智能」的基础。
## 8.1 基本语法
```python
if 条件:
    代码块
elif 另一个条件:
    代码块
else:
    代码块
```
```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```
**执行规则**：
1. 从上到下依次检查每个条件
2. 遇到第一个为 `True` 的条件，执行对应代码块，然后跳过剩余的 `elif/else`
3. 如果所有条件都不满足，执行 `else`（如果有的话）
4. `elif` 可以有 0 个或多个，`else` 可有可无
## 8.2 三元表达式（条件表达式）
```python
# 简单 if-else 的紧凑写法
# 普通写法
if score >= 60:
    result = "及格"
else:
    result = "不及格"
# 三元表达式
result = "及格" if score >= 60 else "不及格"
# 可以带多个条件（但可读性下降，慎用）
level = "优秀" if score >= 90 else "良好" if score >= 80 else "及格" if score >= 60 else "不及格"
```
## 8.3 match-case（Python 3.10+）
`match-case` 是模式匹配，比多重 `if-elif` 更适合处理多种离散情况：
```python
# 处理 HTTP 状态码
status = 404
match status:
    case 200:
        print("OK")
    case 301 | 302 | 307:
        print("重定向")
    case 404:
        print("未找到")
    case 500:
        print("服务器错误")
    case _:
        print(f"未知状态码：{status}")  # _ 是默认匹配
# 解构匹配
point = (0, 5)
match point:
    case (0, 0):
        print("原点")
    case (0, y):
        print(f"在 y 轴上，y={y}")
    case (x, 0):
        print(f"在 x 轴上，x={x}")
    case (x, y):
        print(f"点 ({x}, {y})")
# 配合守卫条件
match score:
    case s if s >= 90:
        print("优秀")
    case s if s >= 60:
        print("及格")
    case _:
        print("不及格")
```
## 8.4 条件判断的「真值」规则
```python
# 以下值在 if 中被视为 False：
# False, None, 0, 0.0, "", [], {}, (), set(), range(0)
# 利用真值简化代码
name = input("名字：").strip()
if name:                         # 等价于 if name != ""
    print(f"你好，{name}！")
else:
    print("名字不能为空")
# 列表非空判断
items = get_items()
if items:                       # 等价于 if len(items) > 0
    process(items)
```
## 8.5 常见模式
```python
# 1. 范围判断
if 0 <= value <= 100:
    print("合法范围")
# 2. 包含判断
valid = {"y", "n", "yes", "no"}
if user_input.lower() in valid:
    process()
# 3. 多条件短路
if user and user.is_active and user.has_permission("write"):
    allow_access()
# 4. 提前返回/守卫模式（减少嵌套）
def process_order(order):
    if not order:
        return "订单为空"
    if not order.is_paid:
        return "订单未支付"
    if order.is_shipped:
        return "已发货"
    # 真正的处理逻辑
    return ship_order(order)
```
## 8.6 小案例：判断奇偶数
```python
number = int(input("请输入一个整数："))
if number % 2 == 0:
    print("这是偶数")
else:
    print("这是奇数")
```
# 9. 循环
循环用于重复执行代码，是程序处理大量数据的基础。
## 9.1 `for` 循环
`for` 循环用于遍历可迭代对象（iterable）：字符串、列表、元组、字典、集合、`range()` 等。
### range() 深入
```python
# range(stop)：0 到 stop-1
for i in range(5):
    print(i)
# 输出：0 1 2 3 4
# range(start, stop)：start 到 stop-1
for i in range(1, 6):
    print(i)
# 输出：1 2 3 4 5
# range(start, stop, step)：带步长
for i in range(0, 10, 2):
    print(i)
# 输出：0 2 4 6 8
# range 是惰性的：不占用大量内存
r = range(10**9)  # 不会创建 10 亿个整数！
print(r[999])     # 用时计算，O(1)
```
### 遍历各种容器
```python
# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(fruit)
# 同时获取索引和值：enumerate()
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 输出：
# 0: 苹果
# 1: 香蕉
# 2: 橙子
# 自定义起始索引
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
# 遍历字典
student = {"name": "小明", "age": 18, "score": 92}
for key in student:
    print(key)            # name age score
for value in student.values():
    print(value)
for key, value in student.items():
    print(f"{key}: {value}")
# 同时遍历多个列表：zip()
names = ["小明", "小红", "小刚"]
scores = [92, 88, 95]
for name, score in zip(names, scores):
    print(f"{name}: {score}分")
# 长度不等时，以最短的为准（可用 itertools.zip_longest 补全）
```
## 9.2 `while` 循环
当不确定循环次数，只知道「满足条件就继续」时使用。
```python
# 基本形式
count = 1
while count <= 3:
    print(count)
    count += 1
# 无限循环（需要 break 退出）
while True:
    user_input = input("输入 q 退出：")
    if user_input == "q":
        break
    print(f"你输入了：{user_input}")
```
**`for` vs `while` 选择**：
- 知道循环次数或遍历集合 → `for`
- 不确定次数，等待条件满足 → `while`
## 9.3 `break`、`continue` 和 `else`
```python
# break：立即退出循环
for i in range(10):
    if i == 5:
        break     # 执行到 5 就结束
    print(i)
# continue：跳过当前迭代，继续下一次
for i in range(6):
    if i == 3:
        continue  # 跳过 3
    print(i)      # 输出：0 1 2 4 5
# 循环的 else 子句（Python 特有）
# 当循环正常结束（没有被 break 打断）时执行
for i in range(5):
    if i == 10:
        break
else:
    print("循环正常结束，没有遇到 break")
# 典型应用：查找
def find_user(name):
    for user in users:
        if user.name == name:
            print(f"找到了：{user}")
            break
    else:
        print(f"没有找到用户 {name}")
```
## 9.4 列表推导式（预览）
```python
# 普通循环
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
# 列表推导式：一行搞定
squares = [i ** 2 for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
# 带条件的列表推导式
evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
# 三元表达式在推导式中
labels = ["偶数" if i % 2 == 0 else "奇数" for i in range(1, 6)]
print(labels)  # ['奇数', '偶数', '奇数', '偶数', '奇数']
# 嵌套循环在推导式中
pairs = [(a, b) for a in "AB" for b in "12"]
print(pairs)   # [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]
```
## 9.5 循环性能技巧
```python
import timeit
# ❌ 不好的做法：在循环中重复计算
for i in range(len(items)):     # len() 每次循环都调用
    print(items[i])
# ✅ 好：用 enumerate
for i, item in enumerate(items):
    print(item)
# ❌ 不好：在循环中拼接字符串
result = ""
for item in items:
    result += str(item)   # 每次都创建新字符串！
# ✅ 好：用 join
result = "".join(str(item) for item in items)
# ❌ 不好：用循环做查找
for item in items:
    if item == target:
        break
# ✅ 好：用 in / index / set
if target in items_set:  # set 的查找是 O(1)
    pass
```
跳过 3。
# 10. 列表、元组、字典、集合
这四种是 Python 中最核心的内置数据结构。理解它们的特性和适用场景，是写好 Python 的基础。
## 10.1 列表 `list`
列表是**有序、可变**的元素序列，用 `[]` 表示。
### 基本操作
```python
scores = [90, 85, 76]
print(scores[0])         # 90
print(scores[-1])        # 76（倒数第一个）
# 修改
scores[0] = 100
# 添加
scores.append(88)        # 在末尾追加
scores.insert(1, 95)     # 在索引 1 处插入 95
scores.extend([70, 80])  # 合并另一个列表
# 删除
scores.remove(85)        # 删除值为 85 的第一个元素
popped = scores.pop()    # 删除并返回最后一个元素
popped = scores.pop(2)   # 删除并返回索引 2 的元素
del scores[0]            # 删除索引 0 的元素
scores.clear()           # 清空整个列表
# 查询
print(len(scores))       # 长度
print(90 in scores)      # 是否存在
print(scores.index(90))  # 查找索引（找不到报 ValueError）
print(scores.count(90))  # 计数
```
### 切片（与字符串相同）
```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])     # [1, 2, 3]
print(nums[:3])      # [0, 1, 2]
print(nums[3:])      # [3, 4, 5]
print(nums[::2])     # [0, 2, 4]（步长）
print(nums[::-1])    # [5, 4, 3, 2, 1, 0]（反转）
```
### 排序
```python
numbers = [3, 1, 4, 1, 5, 9, 2]
# sorted()：返回新列表，原列表不变
sorted_nums = sorted(numbers)
print(sorted_nums)          # [1, 1, 2, 3, 4, 5, 9]
print(sorted(numbers, reverse=True))  # [9, 5, 4, 3, 2, 1, 1]
# .sort()：原地排序，改变原列表
numbers.sort()
print(numbers)              # [1, 1, 2, 3, 4, 5, 9]
# 自定义排序键
words = ["apple", "banana", "kiwi", "pear"]
words.sort(key=len)         # 按长度排序
print(words)                # ['kiwi', 'pear', 'apple', 'banana']
# 按对象的某属性排序
students = [
    {"name": "小明", "score": 92},
    {"name": "小红", "score": 88},
    {"name": "小刚", "score": 95},
]
students.sort(key=lambda s: s["score"], reverse=True)
print(students)
```
### 列表的复制陷阱
```python
# 浅拷贝 vs 深拷贝
a = [1, 2, [3, 4]]
# 赋值：同一个对象
b = a
b[0] = 99
print(a[0])  # 99 ← a 也变了！
# 浅拷贝：外层独立，内层共享
c = a.copy()      # 或 a[:] 或 list(a)
c[0] = 100        # a 不受影响
c[2][0] = 999     # 但内层列表是共享的！
print(a[2])       # [999, 4] ← a 的内层也变了！
# 深拷贝：完全独立
import copy
d = copy.deepcopy(a)
d[2][0] = 888
print(a[2])       # [999, 4] ← a 不受影响
```
## 10.2 元组 `tuple`
元组是**有序、不可变**的序列，用 `()` 表示。
```python
point = (10, 20)
person = ("小明", 18, "北京")
# 单元素元组：注意逗号！
single = (42,)    # 是元组
not_tuple = (42)  # 是整数！
# 元组解包
x, y = point          # x=10, y=20
x, y = y, x           # 交换变量（Python 特有！）
name, age, city = person
# 用 _ 忽略不需要的值
_, age, _ = person
# 扩展解包（Python 3）
first, *middle, last = [1, 2, 3, 4, 5]
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```
**为什么要有元组？**
- 不可变性保证了数据安全（不会被意外修改）
- 可以作为字典的键（列表不行）
- 相比列表占用内存更少、创建更快
- 语义上适合表示「记录」（如坐标、日期、配置）
```python
# 元组作为字典键
location = {(10, 20): "北京", (30, 40): "上海"}
print(location[(10, 20)])  # 北京
# 函数返回多个值（实际是返回元组）
def min_max(items):
    return min(items), max(items)
lo, hi = min_max([3, 1, 4, 1, 5])
```
## 10.3 字典 `dict`
字典是**键值对**的集合，Python 3.7+ 保序。用 `{}` 表示。
### 基本操作
```python
student = {
    "name": "小明",
    "age": 18,
    "score": 92
}
# 访问
print(student["name"])          # 小明
print(student.get("city"))       # None（不存在不报错）
print(student.get("city", "未知")) # 未知（带默认值）
# 修改与添加
student["score"] = 95           # 修改
student["city"] = "北京"         # 添加
# 删除
del student["age"]
score = student.pop("score")    # 删除并返回值
student.pop("missing", None)    # 安全删除（不存在返回默认值）
# 合并字典
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = {**d1, **d2}           # Python 3.5+: {'a': 1, 'b': 3, 'c': 4}
d1.update(d2)                    # d1 原地更新
```
### 遍历字典
```python
student = {"name": "小明", "age": 18, "score": 92}
# 遍历键
for key in student:
    print(key)
# 遍历值
for value in student.values():
    print(value)
# 遍历键值对（最常用）
for key, value in student.items():
    print(f"{key}: {value}")
```
### 字典推导式
```python
# 从序列创建字典
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# 反转字典（键值互换）
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)  # {1: 'a', 2: 'b', 3: 'c'}
# 带条件的字典推导式
passed = {name: score for name, score in students.items() if score >= 60}
```
### defaultdict 与 Counter
```python
from collections import defaultdict, Counter
# defaultdict：访问不存在的键时自动创建默认值
word_count = defaultdict(int)     # 默认值 0
for word in ["a", "b", "a", "c", "b", "a"]:
    word_count[word] += 1
print(word_count)  # defaultdict(<class 'int'>, {'a': 3, 'b': 2, 'c': 1})
# Counter：统计计数
counter = Counter(["a", "b", "a", "c", "b", "a"])
print(counter)                    # Counter({'a': 3, 'b': 2, 'c': 1})
print(counter.most_common(2))     # [('a', 3), ('b', 2)]
# Counter 运算
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)
print(c1 + c2)    # Counter({'a': 4, 'b': 3})
print(c1 - c2)    # Counter({'a': 2})
print(c1 & c2)    # Counter({'a': 1, 'b': 1})（取最小值）
print(c1 | c2)    # Counter({'a': 3, 'b': 2})（取最大值）
```
## 10.4 集合 `set`
集合是**无序、不重复**的元素集合，用 `{}` 表示（空集合用 `set()`）。
```python
# 创建
fruits = {"苹果", "香蕉", "橙子"}
empty = set()            # 注意：{} 是空字典！
numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}（自动去重）
# 基本操作
fruits.add("葡萄")        # 添加
fruits.remove("香蕉")     # 删除（元素不存在会报错）
fruits.discard("西瓜")   # 删除（不存在也不报错）
popped = fruits.pop()    # 随机删除并返回一个元素
# 集合运算
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)    # {1, 2, 3, 4, 5, 6}  并集
print(a & b)    # {3, 4}               交集
print(a - b)    # {1, 2}               差集（a 有 b 没有）
print(a ^ b)    # {1, 2, 5, 6}         对称差集（只在一方存在的）
# 替代方法
print(a.union(b))           # 并集
print(a.intersection(b))    # 交集
print(a.difference(b))      # 差集
# 子集判断
print({1, 2} <= {1, 2, 3})   # True（子集）
print({1, 2} < {1, 2})       # False（真子集）
```
### 集合推导式
```python
squares = {x**2 for x in range(10)}
unique_lengths = {len(word) for word in ["a", "bb", "ccc", "dd", "a"]}
```
## 10.5 数据结构选择指南
| 场景 | 推荐数据结构 | 原因 |
|------|-------------|------|
| 按顺序存储多个值，需要修改 | `list` | 有序、可变 |
| 存储固定记录（坐标、日期） | `tuple` | 不可变，安全 |
| 键值查找 | `dict` | O(1) 查找 |
| 去重、集合运算 | `set` | 自动去重，O(1) 查找 |
| 需要计数 | `Counter` | 专为计数设计 |
| 序列化到 JSON | `list`/`dict` | JSON 原生类型 |
| 函数参数传递 | `tuple`/`list` | 解包语法灵活 |

## 10.6 嵌套结构
```python
# 列表的列表（矩阵）
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # 6（第2行第3列）
# 字典的列表
users = [
    {"name": "小明", "age": 18},
    {"name": "小红", "age": 20},
]
# 字典的字典
config = {
    "database": {"host": "localhost", "port": 5432},
    "cache": {"host": "localhost", "port": 6379},
}
# 任何深度的嵌套都可以，但过深嵌套应考虑用类来组织
```
# 11. 函数
函数是组织代码的基本单元。好的函数应该「只做一件事，并且把它做好」。
## 11.1 定义与调用
```python
def greet(name):
    \"\"\"向指定用户打招呼。\"\"\"
    print(f"你好，{name}！")
greet("小明")
greet("小红")
```
### 返回值
```python
def add(a, b):
    return a + b
# return 不写或写 return None 效果相同
def log(message):
    print(f"[LOG] {message}")
    # 隐式返回 None
# 返回多个值（实际是返回元组）
def min_max_avg(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)
lo, hi, avg = min_max_avg([1, 2, 3, 4, 5])
print(lo, hi, avg)  # 1 5 3.0
```
## 11.2 参数
### 位置参数 vs 关键字参数
```python
def describe_person(name, age, city="未知"):
    print(f"{name}，{age}岁，来自{city}")
# 位置参数
describe_person("小明", 18)            # city 用默认值
# 关键字参数
describe_person(age=20, name="小红")   # 顺序可以任意
# 混合（位置参数必须在关键字参数之前）
describe_person("小明", city="北京", age=18)
```
### 默认参数的陷阱
```python
# ❌ 不要用可变对象做默认参数！
def add_item(item, items=[]):
    items.append(item)
    return items
print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] ← 同一个列表！
print(add_item(3))  # [1, 2, 3] ← 列表在多次调用间共享
# ✅ 正确做法
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```
### `*args` 与 `**kwargs`
```python
# *args：接收任意数量的位置参数（打包成元组）
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4))  # 10
print(sum_all())              # 0
# **kwargs：接收任意数量的关键字参数（打包成字典）
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="小明", age=18, city="北京")
# 结合使用
def universal_function(*args, **kwargs):
    print(f"位置参数：{args}")
    print(f"关键字参数：{kwargs}")
universal_function(1, 2, 3, name="小明", score=95)
# 位置参数：(1, 2, 3)
# 关键字参数：{'name': '小明', 'score': 95}
```
### 强制关键字参数（Python 3+）
```python
# * 后面的参数必须用关键字传递
def configure(host, port, *, timeout=30, retries=3):
    pass
configure("localhost", 8080, timeout=10)       # OK
configure("localhost", 8080, 10, 3)            # ❌ 错误
# / 前面的参数只能用位置传递（Python 3.8+）
def point(x, y, /, *, label=""):
    pass
point(1, 2, label="home")   # OK
point(x=1, y=2, label="home")  # ❌ x, y 不能做关键字
```
## 11.3 作用域与 LEGB 规则
Python 查找变量名时按 LEGB 顺序：
1. **L**ocal：当前函数内部
2. **E**nclosing：外层函数
3. **G**lobal：模块（文件）级别
4. **B**uilt-in：Python 内置
```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(f"inner: {x}")  # local
    inner()
    print(f"outer: {x}")      # enclosing
outer()
print(f"global: {x}")         # global
```
### global 与 nonlocal
```python
# global：在函数内修改全局变量
total = 0
def increment():
    global total
    total += 1
# nonlocal：在内层函数修改外层函数的变量
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
```
## 11.4 Lambda 表达式（匿名函数）
```python
# 普通函数
def square(x):
    return x ** 2
# lambda 等效写法
square = lambda x: x ** 2
# lambda 主要用于「需要一个简单函数但不值得单独命名」的场景
# 常见用法：sort、filter、map 的 key 参数
students = [
    {"name": "小明", "score": 92},
    {"name": "小红", "score": 88},
]
students.sort(key=lambda s: s["score"])
print(students)
# filter：过滤序列
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]
# map：对序列每个元素应用函数
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25, 36]
# lambda 限制：只能包含单个表达式，不能有语句
# ❌ lambda x: print(x)        # 不能有 print
# ❌ lambda x: x = 1           # 不能有赋值
```
## 11.5 函数是一等公民
函数可以作为参数传递、从函数返回、赋值给变量。
```python
# 函数作为参数（回调）
def apply(func, value):
    return func(value)
result = apply(abs, -5)    # 5
result = apply(str, 42)    # "42"
# 函数作为返回值（工厂函数/闭包）
def make_multiplier(factor):
    return lambda x: x * factor
double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15
```
## 11.6 类型提示（Type Hints）
Python 3.5+ 支持可选的类型标注，帮助 IDE 和工具检查错误。
```python
def greet(name: str) -> None:
    print(f"你好，{name}！")
def calculate_average(scores: list[float]) -> float:
    if not scores:
        return 0.0
    return sum(scores) / len(scores)
from typing import Optional
def find_user(name: str) -> Optional[dict]:
    \"\"\"查找用户，找不到返回 None。\"\"\"
    if name in db:
        return db[name]
    return None
```
类型提示**不影响运行时行为**，但强烈推荐在项目中启用（配合 mypy / pyright 做静态检查）。
## 11.7 递归
函数调用自身称为递归。
```python
def factorial(n: int) -> int:
    \"\"\"计算阶乘。递归实现。\"\"\"
    if n <= 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # 120
```
递归要点：
- 必须有**终止条件**（base case），否则无限递归
- Python 默认递归深度限制约 1000 层（`sys.getrecursionlimit()`）
- 对于简单递归，能用循环替代就用循环
# 12. 列表推导式与生成器表达式
## 12.1 列表推导式
列表推导式是 Python 中创建列表的简洁方式。
```python
# 普通循环写法
squares = []
for number in range(1, 6):
    squares.append(number ** 2)
# 列表推导式：一行搞定
squares = [number ** 2 for number in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
# 完整语法：[expression for item in iterable if condition]
# 带条件过滤
evens = [number for number in range(1, 11) if number % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]
# if-else 在表达式部分（注意位置！）
labels = ["偶数" if i % 2 == 0 else "奇数" for i in range(1, 6)]
print(labels)  # ['奇数', '偶数', '奇数', '偶数', '奇数']
# 嵌套循环
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)  # [(0,0), (0,1), (1,0), (1,1), (2,0), (2,1)]
```
## 12.2 字典推导式
```python
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
# 反转键值对
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
# 条件过滤
passed = {name: score for name, score in scores.items() if score >= 60}
```
## 12.3 集合推导式
```python
# 所有二次幂的最后一位数字的去重集合
last_digits = {n**2 % 10 for n in range(100)}
print(last_digits)  # {0, 1, 4, 5, 6, 9}
# 去重
words = ["apple", "banana", "apple", "kiwi"]
unique_lengths = {len(w) for w in words}
```
## 12.4 生成器表达式
用小括号替代方括号，得到一个**惰性求值**的生成器，不立即创建整个列表。
```python
# 列表推导式：立即创建全部元素（占用内存）
squares_list = [x**2 for x in range(10**6)]
# 生成器表达式：用时才计算（几乎不占内存）
squares_gen = (x**2 for x in range(10**6))
print(next(squares_gen))  # 0
print(next(squares_gen))  # 1
# 典型用法：sum、max、any、all
total = sum(x**2 for x in range(10**6))  # 不需要临时列表
# 检查是否有偶数
has_even = any(x % 2 == 0 for x in range(1, 11))
```
## 12.5 推导式 vs 传统循环的选择
```python
# ✅ 适合用推导式：简单映射、过滤
names = [user.name for user in users if user.active]
# ❌ 不适合用推导式：逻辑复杂、有副作用、嵌套过深
# 这种情况用传统循环更可读
result = []
for user in users:
    if user.active:
        name = process_name(user.name)
        log_processing(user.id)
        result.append(name)
```
# 13. 模块与导入
## 13.1 模块是什么
任何 `.py` 文件都是一个模块。模块是 Python 组织代码的基本单元。
```python
# calculator.py
\"\"\"一个简单的计算器模块。\"\"\"
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
# main.py
import calculator
print(calculator.add(3, 5))  # 8
```
## 13.2 导入方式
```python
# 方式一：import 模块名
import math
print(math.sqrt(16))  # 4.0
# 方式二：from 模块 import 具体名字
from math import sqrt, pi
print(sqrt(16), pi)
# 方式三：from 模块 import *（不推荐，污染命名空间）
from math import *
# 方式四：别名
import numpy as np
import pandas as pd
from datetime import datetime as dt
```
## 13.3 常用标准库
```python
# 数学
import math
print(math.pi, math.e, math.sqrt(2), math.sin(math.pi/2))
# 随机数
import random
print(random.randint(1, 10))          # [1, 10] 随机整数
print(random.random())                # [0, 1) 随机浮点数
print(random.choice(["苹果", "香蕉"]))  # 随机选一个
random.shuffle(items)                 # 打乱列表（原地）
# 日期时间
from datetime import datetime, timedelta, date
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 格式化
future = now + timedelta(days=7)          # 7 天后
print((future - now).days)               # 计算天数差
# JSON
import json
data = {"name": "小明", "age": 18}
json_str = json.dumps(data, ensure_ascii=False, indent=2)
print(json_str)
parsed = json.loads(json_str)
print(parsed["name"])
# 操作系统接口
import os
print(os.getcwd())          # 当前工作目录
print(os.listdir("."))      # 目录列表
print(os.path.exists("file.txt"))
print(os.path.join("dir", "subdir", "file.txt"))
```
## 13.4 模块搜索路径
```python
import sys
print(sys.path)  # Python 查找模块的所有路径
# 临时添加搜索路径
sys.path.insert(0, "/path/to/my/modules")
```
## 13.5 `if __name__ == "__main__"`
```python
# utils.py
def helper():
    return "useful"
print("utils 模块被加载了")
if __name__ == "__main__":
    # 这段代码只在直接运行此文件时执行
    # 被 import 时不执行
    print("直接运行 utils.py")
    print(helper())
```
## 13.6 包（Package）
包含 `__init__.py` 的目录就是包。
```text
my_package/
├── __init__.py
├── core.py
└── utils/
    ├── __init__.py
    └── helpers.py
```
```python
# 导入包中的模块
from my_package import core
from my_package.utils import helpers
```
# 14. 文件读写
## 14.1 `with` 语句（上下文管理器）
```python
# 推荐：with 自动关闭文件
with open("note.txt", "w", encoding="utf-8") as file:
    file.write("Hello, Python!")
# 不推荐：需要手动 close()
file = open("note.txt", "w", encoding="utf-8")
try:
    file.write("Hello, Python!")
finally:
    file.close()
```
### 文件模式
| 模式 | 含义 | 文件不存在时 |
|------|------|------------|
| `"r"` | 只读 | 报错 |
| `"w"` | 只写（覆盖） | 创建 |
| `"a"` | 追加 | 创建 |
| `"x"` | 排他创建 | 报错 |
| `"r+"` | 读写 | 报错 |
| `"b"` | 二进制模式 | - |
| `"t"` | 文本模式（默认） | - |

```python
# 二进制读写
with open("image.jpg", "rb") as f:
    data = f.read()
# 组合模式
with open("data.bin", "wb") as f:
    f.write(b"binary data")
```
## 14.2 读取方式
```python
# 读取全部内容
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()            # 整个文件作为一个字符串
# 按行读取
with open("file.txt", "r", encoding="utf-8") as f:
    for line in f:                 # 逐行迭代（内存友好）
        print(line.strip())
# 读所有行到列表
with open("file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()          # 小文件可用
# 读取指定字节数
with open("file.txt", "r", encoding="utf-8") as f:
    chunk = f.read(1024)           # 读 1024 个字符
```
## 14.3 写入与追加
```python
# 覆盖写入
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("第一行\n")
    f.write("第二行\n")
    f.writelines(["第三行\n", "第四行\n"])
# 追加写入
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("追加的内容\n")
```
## 14.4 pathlib：现代化的路径处理
```python
from pathlib import Path
# 创建路径对象
p = Path("/home/user/docs/readme.txt")
# 路径信息
print(p.name)        # readme.txt
print(p.stem)        # readme
print(p.suffix)      # .txt
print(p.parent)      # /home/user/docs
print(p.parts)       # ('/', 'home', 'user', 'docs', 'readme.txt')
# 路径操作
new_path = p.parent / "config.json"  # / 运算符拼接路径
# 文件操作
content = Path("file.txt").read_text(encoding="utf-8")
Path("output.txt").write_text("Hello", encoding="utf-8")
# 检查
print(Path("file.txt").exists())
print(Path("dir").is_dir())
print(Path("file.txt").is_file())
# 遍历目录
for item in Path(".").iterdir():
    print(item.name)
# 递归 glob
for py_file in Path(".").rglob("*.py"):
    print(py_file)
```
## 14.5 CSV 文件处理
```python
import csv
# 写入 CSV
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["姓名", "年龄", "分数"])
    writer.writerow(["小明", 18, 92])
    writer.writerow(["小红", 20, 88])
# 读取 CSV
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['姓名']}: {row['分数']}分")
```
# 15. 异常处理
异常不是程序的失败，而是程序必须面对的现实：文件可能不存在、网络可能断开、用户可能输入非法数据。
## 15.1 基本语法
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("除数不能为零！")
```
### 捕获多种异常
```python
try:
    value = int(input("输入整数："))
    result = 100 / value
except ValueError:
    print("请输入有效的整数")
except ZeroDivisionError:
    print("不能除以零")
except (TypeError, KeyError):
    print("类型错误或键不存在")
except Exception as e:
    print(f"未知错误：{type(e).__name__}: {e}")
```
## 15.2 `else` 与 `finally`
```python
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("文件不存在")
else:
    # 没有异常时执行
    content = file.read()
    file.close()
finally:
    # 不论是否有异常，始终执行
    print("清理工作完成")
```
## 15.3 自定义异常
```python
class InvalidScoreError(ValueError):
    \"\"\"无效分数的异常。\"\"\"
    def __init__(self, score, message="分数必须在 0-100 之间"):
        self.score = score
        self.message = f"{message}，收到：{score}"
        super().__init__(self.message)
# 使用自定义异常
def validate_score(score):
    if not 0 <= score <= 100:
        raise InvalidScoreError(score)
    return score
try:
    validate_score(150)
except InvalidScoreError as e:
    print(e)  # 分数必须在 0-100 之间，收到：150
```
## 15.4 异常链
```python
try:
    data = json.loads(user_input)
except json.JSONDecodeError as e:
    raise ValueError("配置文件格式错误") from e
```
## 15.5 常见异常速查
| 异常 | 原因 | 示例 |
|------|------|------|
| `ValueError` | 值不正确 | `int("abc")` |
| `TypeError` | 类型不对 | `"2" + 2` |
| `IndexError` | 列表索引越界 | `[1][10]` |
| `KeyError` | 字典键不存在 | `{}["key"]` |
| `AttributeError` | 对象没有该属性 | `None.upper()` |
| `FileNotFoundError` | 文件未找到 | `open("不存在")` |
| `ZeroDivisionError` | 除以零 | `1/0` |
| `ImportError` | 模块未找到 | `import xxx` |
| `NameError` | 变量未定义 | 拼写错误 |
| `StopIteration` | 迭代结束 | 生成器耗尽 |

## 15.6 LBYL vs EAFP
Python 推荐「请求宽恕比请求许可更容易」（EAFP）——先尝试，失败再处理。
```python
# LBYL：三思而后行（提前检查）
if "key" in d:
    value = d["key"]
# EAFP：先斩后奏（Python 风格，推荐）
try:
    value = d["key"]
except KeyError:
    value = default
```
# 16. 面向对象基础
面向对象编程（OOP）通过「类」和「对象」组织代码，是构建大型程序的核心范式。
## 16.1 类与对象
```python
class Student:
    \"\"\"学生类。\"\"\"
    # 类属性（所有实例共享）
    school = "第一中学"
    # 初始化方法（构造器）
    def __init__(self, name: str, score: int):
        # 实例属性（每个实例独有）
        self.name = name
        self.score = score
    # 实例方法
    def introduce(self) -> str:
        grade = self._calculate_grade()
        return f"我是{self.name}，{self.school}，成绩{self.score}分，等级{grade}"
    # 私有方法（前缀 _ 表示「约定私有」）
    def _calculate_grade(self) -> str:
        if self.score >= 90:
            return "优秀"
        elif self.score >= 60:
            return "及格"
        else:
            return "不及格"
    # 特殊方法（魔术方法）
    def __str__(self) -> str:
        return f"Student({self.name}, {self.score})"
    def __repr__(self) -> str:
        return f"Student(name={self.name!r}, score={self.score!r})"
# 创建对象（实例化）
s1 = Student("小明", 92)
s2 = Student("小红", 88)
print(s1.introduce())   # 我是小明，第一中学，成绩92分，等级优秀
print(s1)               # Student(小明, 92)  ← 调用 __str__
print(repr(s1))         # Student(name='小明', score=92)  ← 调用 __repr__
```
## 16.2 `self` 的含义
- `self` 代表当前实例对象本身
- 在方法内部通过 `self` 访问属性和其他方法
- 调用时 Python 自动传入 `self`，不需要手动传
- 名字 `self` 只是约定，可以用其他名字（但强烈不建议）
```python
# 等价理解：s1.introduce() 实际上是 Student.introduce(s1)
print(Student.introduce(s1))  # 与 s1.introduce() 完全相同
```
## 16.3 继承
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        return f"你好，我是{self.name}"
class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)  # 调用父类 __init__
        self.score = score
    # 方法重写（override）
    def greeting(self):
        return f"{super().greeting()}，我的成绩是{self.score}分"
s = Student("小明", 18, 92)
print(s.greeting())  # 你好，我是小明，我的成绩是92分
```
## 16.4 `@property`（属性装饰器）
让方法像属性一样访问。
```python
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    @property
    def area(self):
        \"\"\"面积（只读属性）。\"\"\"
        return self._width * self._height
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("宽度必须为正数")
        self._width = value
r = Rectangle(10, 5)
print(r.area)    # 50（像属性一样访问，不需要括号）
r.width = 20
print(r.area)    # 100
```
## 16.5 `@classmethod` 与 `@staticmethod`
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    @classmethod
    def from_string(cls, date_str: str):
        \"\"\"从字符串创建（替代构造函数）。\"\"\"
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)
    @staticmethod
    def is_valid_date(year, month, day):
        \"\"\"工具方法，不依赖实例。\"\"\"
        return 1 <= month <= 12 and 1 <= day <= 31
# 使用
d1 = Date(2026, 5, 29)
d2 = Date.from_string("2026-05-29")
print(Date.is_valid_date(2026, 13, 1))  # False
```
## 16.6 数据类（dataclass，Python 3.7+）
减少模板代码，自动生成 `__init__`、`__repr__`、`__eq__` 等。
```python
from dataclasses import dataclass, field
@dataclass
class Student:
    name: str
    score: int
    grade: str = ""          # 有默认值
    tags: list[str] = field(default_factory=list)  # 可变默认值
    def __post_init__(self):
        \"\"\"初始化后自动调用。\"\"\"
        if self.score >= 90:
            self.grade = "优秀"
        elif self.score >= 60:
            self.grade = "及格"
        else:
            self.grade = "不及格"
s1 = Student("小明", 92)
s2 = Student("小明", 92)
print(s1)            # Student(name='小明', score=92, grade='优秀', tags=[])
print(s1 == s2)      # True（自动比较属性）
```
## 16.7 什么时候用类？
| 场景 | 建议 |
|------|------|
| 简单脚本（< 50 行） | 不需要类 |
| 几个相关函数 | 模块（.py 文件）即可 |
| 数据和操作绑定 | 用类（如学生+成绩操作） |
| 有状态的行为 | 用类（如游戏角色、银行账户） |
| 需要继承和多态 | 用类 |
| 数据容器 | 优先 dataclass 或 namedtuple |

**原则**：不要为了面向对象而面向对象。Python 支持多范式——函数、模块、类按需混用。
# 17. 第三方库与虚拟环境
## 17.1 pip：Python 的包管理器
```bash
# 安装包
pip install requests
# 或
python -m pip install requests
# 安装特定版本
pip install requests==2.28.0
# 升级包
pip install --upgrade requests
# 卸载
pip uninstall requests
# 列出已安装
pip list
pip list --outdated
# 查看包信息
pip show requests
```
## 17.2 虚拟环境
不同项目可能依赖不同版本的同一个库。虚拟环境让每个项目拥有**独立的 Python 和依赖**。
```bash
# 创建虚拟环境
python -m venv .venv
# 激活
# Linux / macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
# 激活后，pip install 的包只存在于该环境中
pip install requests
# 退出
deactivate
```
## 17.3 requirements.txt
```bash
# 导出依赖
pip freeze > requirements.txt
# 安装依赖
pip install -r requirements.txt
```
`requirements.txt` 示例：
```text
requests==2.28.0
flask==3.0.0
numpy>=1.24,<2.0
```
## 17.4 现代替代方案：uv 与 Poetry
```bash
# uv（Rust 实现，极快）
pip install uv
uv venv
uv pip install requests
# Poetry（带依赖解析和锁文件）
pip install poetry
poetry new my-project
poetry add requests
poetry install
```
## 17.5 推荐项目结构
```text
my_project/
├── .venv/              # 虚拟环境（不提交到 Git）
├── src/                # 源代码
│   └── my_package/
│       ├── __init__.py
│       └── main.py
├── tests/              # 测试
│   └── test_main.py
├── requirements.txt    # 或 pyproject.toml
├── .gitignore
└── README.md
```
`.gitignore` 中应包含：
```gitignore
.venv/
__pycache__/
*.pyc
.env
```
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
# 19. Python 代码规范与调试习惯
## 19.1 良好的命名
```python
# ❌ 不推荐
a = 95
b = 3
c = a / b
tmp = []
for x in data:
    tmp.append(f(x))
# ✅ 推荐
total_score = 95
subject_count = 3
average_score = total_score / subject_count
processed_items = [process(item) for item in original_data]
```
## 19.2 保持函数职责单一
每个函数应只做一件事。判断标准：能否用一个简洁的句子描述这个函数做什么？
```python
# ❌ 一个函数做太多事
def process_data(data):
    # 验证、清洗、计算、格式化、保存...
    pass
# ✅ 拆成多个小函数
def validate(data): ...
def clean(data): ...
def analyze(data): ...
def format_results(results): ...
def save(path, content): ...
```
## 19.3 调试技巧
### print 调试（最常用）
```python
print(f"DEBUG: value={value}, type={type(value).__name__}")
```
### logging 模块（推荐用于正式项目）
```python
import logging
logging.basicConfig(level=logging.DEBUG)
def process(item):
    logging.debug(f"处理中: {item}")
    # ...
    logging.info(f"处理完成: {result}")
```
### pdb 断点调试
```python
import pdb; pdb.set_trace()  # 运行到此处暂停，进入交互调试
# Python 3.7+ 更简洁的写法
breakpoint()
```
## 19.4 编写 docstring
```python
def calculate_discount(price: float, rate: float = 0.8) -> float:
    \"\"\"
    计算折扣价格。
    Args:
        price: 原价（元）
        rate: 折扣率，默认 0.8
    Returns:
        float: 折扣后价格
    Raises:
        ValueError: 价格或折扣率小于 0
    Example:
        >>> calculate_discount(100)
        80.0
        >>> calculate_discount(100, 0.5)
        50.0
    \"\"\"
    if price < 0 or rate < 0:
        raise ValueError("价格和折扣率必须 >= 0")
    return price * rate
```
# 20. 初学者常见错误与进阶常见错误
## 初学常见错误
| 错误 | 症状 | 解决方法 |
|------|------|---------|
| 缩进错误 | `IndentationError` | 统一使用 4 空格缩进 |
| `=` vs `==` | 判断结果错误 | 比较用 `==`，赋值用 `=` |
| `input()` 返回值 | 输入是字符串 | `int()` 或 `float()` 转换 |
| 列表索引越界 | `IndexError` | 索引从 0 开始 |
| 可变默认参数 | 多次调用共享同一个对象 | 用 `None` 做默认值 |
| `is` vs `==` | 判断行为异常 | 比较值用 `==`，与 `None` 比较用 `is` |
| 忘记 `self` | `NameError` | 类方法第一个参数是 `self` |

## 进阶常见错误
| 错误 | 说明 | 如何避免 |
|------|------|---------|
| 可变默认参数 | `def f(lst=[])` | 改为 `def f(lst=None)` |
| 闭包中的循环变量 | lambda 捕获的是变量名，不是值 | 用默认参数绑定：`lambda x, i=i: x*i` |
| `try` 块过大 | 掩盖了意外的错误 | 只包裹可能出错的代码 |
| 全局状态 | 函数隐式依赖全局变量 | 显式传参 |
| 未关闭文件/连接 | 资源泄漏 | 使用 `with` 语句 |
| 循环中修改遍历的列表 | 跳过元素或无限循环 | 遍历副本：`for x in list[:]` |

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
# 26. 生成器与迭代器（进阶）
## 26.1 迭代器协议
任何实现了 `__iter__()` 和 `__next__()` 的对象都是迭代器。
```python
class CountDown:
    \"\"\"倒计时迭代器。\"\"\"
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
for n in CountDown(3):
    print(n)   # 3, 2, 1, 0
```
## 26.2 生成器 `yield`
生成器是最简洁的迭代器创建方式。
```python
# 生成器函数
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
# 使用
for n in countdown(3):
    print(n)   # 3, 2, 1, 0
# 生成器是惰性的：一次只生成一个值，不占用大量内存
def fibonacci():
    \"\"\"无限斐波那契数列。\"\"\"
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci()
print([next(fib) for _ in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
## 26.3 `yield from`（委托生成器）
```python
def chain_generators(*generators):
    for gen in generators:
        yield from gen    # 等价于 for item in gen: yield item
```
## 26.4 生成器表达式
```python
# 列表推导式：立即求值
squares_list = [x**2 for x in range(10**6)]
# 生成器表达式：惰性求值
squares_gen = (x**2 for x in range(10**6))
# 常见用法
total = sum(x**2 for x in range(10**6))   # 不需要临时列表
max_square = max(x**2 for x in range(100))
```
## 26.5 生成器 vs 列表
| 特性 | 生成器 | 列表 |
|------|--------|------|
| 内存 | O(1) | O(n) |
| 访问 | 只能遍历一次 | 可多次访问 |
| 索引 | ❌ | ✅ |
| 长度 | ❌ | ✅ |
| 适用 | 大数据流、管道 | 需要索引和多次访问 |

# 27. 装饰器（进阶）
装饰器在**不修改原函数代码**的情况下，给函数添加额外功能。是 Python 中最优雅的设计模式之一。
## 27.1 函数装饰器基础
```python
def log_call(func):
    \"\"\"记录函数调用的装饰器。\"\"\"
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用 {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} 返回 {result}")
        return result
    return wrapper
@log_call
def add(a, b):
    return a + b
print(add(3, 5))
# 输出：
# [LOG] 调用 add((3, 5), {})
# [LOG] add 返回 8
# 8
```
## 27.2 常见装饰器模式
### 计时装饰器
```python
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} 执行用时：{elapsed:.4f} 秒")
        return result
    return wrapper
@timer
def slow_function():
    time.sleep(0.5)
slow_function()
# slow_function 执行用时：0.5001 秒
```
### 缓存（记忆化）装饰器
```python
from functools import lru_cache
@lru_cache(maxsize=128)   # 内置缓存装饰器！
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(100))     # 瞬间完成，不会指数爆炸
```
### 带参数的装饰器
```python
def repeat(times):
    \"\"\"重复执行 times 次。\"\"\"
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator
@repeat(3)
def say_hello():
    print("Hello!")
say_hello()
# Hello!
# Hello!
# Hello!
```
## 27.3 `@staticmethod`、`@classmethod`、`@property`
这三个是 Python 最常用的内置装饰器（详见第 16 章面向对象）。
## 27.4 保留原函数元信息
使用 `@wraps` 防止装饰器覆盖原函数的 `__name__` 和 docstring：
```python
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
# 28. 并发编程基础
## 28.1 GIL：全局解释器锁
CPython（标准 Python 实现）有一个全局解释器锁（GIL），同一时刻只有一个线程执行 Python 字节码。这意味着：
- **多线程**对 CPU 密集型任务**不会提速**（甚至更慢）
- **多线程**对 I/O 密集型任务（网络、文件、等待）**有效**
- CPU 密集型应用用**多进程**（`multiprocessing`）
- I/O 密集型应用用**多线程**或 **asyncio**
## 28.2 threading（多线程）
```python
import threading
import time
def download(url):
    print(f"开始下载：{url}")
    time.sleep(2)   # 模拟 I/O 等待
    print(f"下载完成：{url}")
# 创建并启动线程
threads = []
for url in ["url1", "url2", "url3"]:
    t = threading.Thread(target=download, args=(url,), daemon=True)
    threads.append(t)
    t.start()
# 等待所有线程完成
for t in threads:
    t.join(timeout=5)
print("全部下载完成")
```
## 28.3 asyncio（异步 I/O）
Python 3.5+ 引入 `async/await`，适合大量 I/O 并发的场景。
```python
import asyncio
async def fetch_data(url: str) -> str:
    print(f"开始获取：{url}")
    await asyncio.sleep(1)  # 模拟网络请求
    print(f"获取完成：{url}")
    return f"数据来自 {url}"
async def main():
    # 并发执行三个请求
    results = await asyncio.gather(
        fetch_data("api/users"),
        fetch_data("api/posts"),
        fetch_data("api/comments"),
    )
    print(f"所有结果：{results}")
# 运行
asyncio.run(main())
```
### asyncio vs threading
| 场景 | 推荐 | 理由 |
|------|------|------|
| 大量网络请求 | asyncio | 单线程、低开销 |
| 文件 I/O | threading | asyncio 的文件 I/O 有限 |
| CPU 密集 | multiprocessing | 绕过 GIL |
| 简单并发 | threading | 学习曲线低 |

## 28.4 concurrent.futures
```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# 线程池
with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(download, urls)
# 进程池（CPU 密集型）
with ProcessPoolExecutor(max_workers=4) as executor:
    results = executor.map(heavy_computation, data)
```
# 29. 常用标准库快速参考
| 模块 | 用途 | 关键函数 |
|------|------|---------|
| `os` | 操作系统接口 | `getcwd()`, `listdir()`, `environ`, `path.join()` |
| `sys` | 系统参数 | `argv`, `path`, `exit()`, `version` |
| `math` | 数学函数 | `sqrt()`, `sin()`, `pi`, `e`, `ceil()`, `floor()` |
| `random` | 随机数 | `randint()`, `choice()`, `shuffle()`, `random()` |
| `datetime` | 日期时间 | `datetime.now()`, `timedelta`, `strftime()` |
| `json` | JSON 处理 | `json.dumps()`, `json.loads()`, `json.dump()`, `json.load()` |
| `re` | 正则表达式 | `re.search()`, `re.match()`, `re.findall()`, `re.sub()` |
| `collections` | 高级容器 | `Counter`, `defaultdict`, `OrderedDict`, `namedtuple`, `deque` |
| `itertools` | 迭代器工具 | `chain()`, `groupby()`, `permutations()`, `product()` |
| `functools` | 函数工具 | `lru_cache`, `reduce()`, `partial()`, `wraps` |
| `argparse` | 命令行参数 | 构建命令行工具 |
| `logging` | 日志 | 替代 `print` 的生产级日志 |
| `pathlib` | 路径处理 | 面向对象的路径操作 |
| `subprocess` | 外部进程 | `run()`, `Popen` |
| `hashlib` | 哈希 | `md5()`, `sha256()` |
| `base64` | Base64 编码 | `b64encode()`, `b64decode()` |
| `csv` | CSV 文件 | `csv.reader()`, `csv.writer()` |
| `sqlite3` | SQLite 数据库 | 轻量级内置数据库 |
| `urllib` | URL 处理 | `urlopen()`, `parse` |
| `email` | 邮件 | 解析和构造邮件 |

## 实用组合示例
### 命令行工具模板
```python
#!/usr/bin/env python3
import argparse
def main():
    parser = argparse.ArgumentParser(description="工具描述")
    parser.add_argument("input", help="输入文件路径")
    parser.add_argument("-o", "--output", default="output.txt", help="输出文件路径")
    parser.add_argument("-v", "--verbose", action="store_true", help="详细输出")
    args = parser.parse_args()
    if args.verbose:
        print(f"处理：{args.input} → {args.output}")
if __name__ == "__main__":
    main()
```
### 正则表达式快速参考
```python
import re
text = "联系电话：13812345678，邮箱：user@example.com"
# 查找模式
phone = re.search(r"1[3-9]\d{9}", text)
email = re.search(r"[\w.-]+@[\w.-]+\.\w+", text)
# 提取所有匹配
numbers = re.findall(r"\d+", text)
# 替换
masked = re.sub(r"\d{4}$", "****", "13812345678")  # 1381234****
```
# 30. 下一步：从入门到熟练
## 30.1 技能自检
完成本指南后，你应该能够：
- [ ] 写出包含函数、类、异常处理的 100-300 行程序
- [ ] 使用 `pip` 安装第三方库，用 `venv` 管理项目依赖
- [ ] 读写文件、处理 CSV/JSON 数据
- [ ] 使用列表/字典推导式简化代码
- [ ] 阅读并理解 Python 报错信息，独立排查问题
- [ ] 编写带类型提示的代码
- [ ] 理解装饰器、生成器、异步的基本概念
## 30.2 推荐资源
### 书籍
- 《Python 编程：从入门到实践》（项目驱动，适合初学者）
- 《流畅的 Python》（深入理解 Python 语言特性，进阶必读）
- 《Effective Python》（90 个 Python 最佳实践）
### 在线资源
- [Python 官方教程](https://docs.python.org/3/tutorial/) — 最权威
- [Real Python](https://realpython.com/) — 大量高质量教程
- [LeetCode](https://leetcode.cn/) — 用 Python 刷算法题
### 练习平台
- 写一个命令行待办事项（Todo）程序
- 写一个爬虫，提取网页内容保存到文件
- 用 Flask/FastAPI 写一个简单的 Web API
- 用 `pandas` 分析一份 CSV 数据并绘图
- 参与一个开源项目的 good-first-issue
## 30.3 最重要的心态
1. **不要试图一次学完所有东西**：本指南的内容可能需要数月消化
2. **项目驱动学习**：每学一个概念就做一个小项目
3. **善用官方文档**：`help()`, `dir()`, [docs.python.org](https://docs.python.org)
4. **阅读优秀代码**：GitHub 上找 Python 项目看源码
5. **写就对了**：编程是手艺活，动手比阅读更重要
> **学一个概念，写一个例子。学几个概念，做一个小项目。**
> 你不需要先掌握所有知识再开始项目。今天的你就已经可以写出有用的程序了。

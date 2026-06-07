# Python complex() 函数

- Source: https://www.runoob.com/python3/python3-func-complex.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`complex()` 是 Python 中用于创建复数（complex number）的内置函数。


复数由实部和虚部组成，在数学和工程领域有广泛应用，如信号处理、物理模拟等。Python 原生支持复数类型，使得复杂计算更加方便。


**单词释义**： `complex` 意为"复数的"，表示包含实部和虚部的数。


---


## 基本语法与参数


`complex()` 是一个内置函数，可以直接调用。


### 语法格式


```
complex(real)
complex(real, imag)
complex(string)
```


### 参数说明


- **参数 real**： 类型： 数字（整数或浮点数）
- 描述： 复数的实部。如果只有这一个参数，它可以是实数或表示复数的字符串。


**参数 imag**（可选）：
- 类型： 数字（整数或浮点数）
- 描述： 复数的虚部。


**参数 string**：
- 类型： 字符串
- 描述： 表示复数的字符串，如 "3+4j" 或 "3+4i"。


### 函数说明


- **返回值**： 返回一个复数对象，形式为 real + imag*j。
- **虚数单位**： Python 中使用 `j` 表示虚数单位（而不是物理中常用的 `i`）。


---


## 实例


让我们通过例子掌握 `complex()` 的用法。


### 示例 1：基础用法 - 创建复数


## 实例


```python
# 使用两个参数创建复数：实部和虚部
c1 = complex(3, 4)
print(c1)          # 输出: (3+4j)

# 虚部为0
c2 = complex(5, 0)
print(c2)          # 输出: (5+0j)

# 实部为0
c3 = complex(0, 2)
print(c3)          # 输出: 2j

# 负数虚部
c4 = complex(1, -2)
print(c4)          # 输出: (1-2j)
```


**运行结果预期:**


```
(3+4j)
(5+0j)
2j
(1-2j)
```


**代码解析:**


- `complex(3, 4)` 创建一个实部为 3，虚部为 4 的复数。
- Python 使用 `j` 而不是 `i` 来表示虚数单位。
- 可以创建纯虚数（实部为 0）或纯实数（虚部为 0）。


### 示例 2：从字符串创建复数


## 实例


```python
# 从字符串创建复数
c1 = complex("3+4j")
print(c1)          # 输出: (3+4j)

# 带空格也可以
c2 = complex("  1 + 2j  ")
print(c2)          # 输出: (1+2j)

# 使用 i 代替 j（仅在字符串中）
c3 = complex("3+4j")  # Python 只认 j，不认 i
print(c3)          # 输出: (3+4j)
```


**运行结果预期:**


```
(3+4j)
(1+2j)
(3+4j)
```


**代码解析:**


- 字符串格式的复数可以直接传给 `complex()` 函数。
- 字符串中可以有空格。
- 注意：Python 复数只支持 `j`，不支持 `i`。


### 示例 3：复数的运算


## 实例


```python
# 创建复数
a = complex(3, 4)
b = complex(1, 2)

# 加法
print(f"a + b = {a + b}")  # 输出: a + b = (4+6j)

# 减法
print(f"a - b = {a - b}")  # 输出: a - b = (2+2j)

# 乘法
print(f"a * b = {a * b}")  # 输出: a * b = (-5+10j)

# 除法
print(f"a / b = {a / b}")  # 输出: a / b = (2.2-0.4j)

# 共轭复数
print(f"共轭: {a.conjugate()}")  # 输出: 共轭: (3-4j)

# 模（绝对值）
print(f"模: {abs(a)}")  # 输出: 模: 5.0
```


**运行结果预期:**


```
a + b = (4+6j)
a - b = (2+2j)
a * b = (-5+10j)
a / b = (2.2-0.4j)
共轭: (3-4j)
模: 5.0
```


这个例子展示了复数的基本运算，包括加、减、乘、除、共轭和模。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python float() 函数](https://www.runoob.com/python3-func-float.html)
			[Python bin() 函数](https://www.runoob.com/python3-func-bin.html) **













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
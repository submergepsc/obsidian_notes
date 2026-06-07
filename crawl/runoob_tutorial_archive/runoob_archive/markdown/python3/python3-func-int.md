# Python int() 函数

- Source: https://www.runoob.com/python3/python3-func-int.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`int()` 是 Python 中最常用的内置函数之一，用于将其他类型的数据转换为整数类型。


在编程中，我们经常需要将字符串、浮点数或其他类型的数据转换为整数来进行数值计算或比较。`int()` 函数可以帮助我们轻松完成这个转换。


**单词释义**： `int` 是 `integer`（整数）的缩写，表示整数类型。


---


## 基本语法与参数


`int()` 是一个内置函数，可以直接调用，不需要导入任何模块。


### 语法格式


```
int(x)
int(x, base)
```


### 参数说明


- **参数 x**： 类型： 字符串、数字或其他可转换为整数的对象
- 描述： 要转换为整数的值。如果 x 是字符串，可以在 base 参数中指定进制。


**参数 base**（可选）：
- 类型： 整数（2, 8, 10, 16）
- 描述： x 的进制，默认为 10（十进制）。仅当 x 是字符串时有效。


### 函数说明


- **返回值**： 返回一个整数对象。
- **特殊情况**： `int()` 不带参数返回 0
- 浮点数会向下取整（向零方向截断）
- 字符串必须是有效的数字表示


---


## 实例


让我们通过一系列从简单到复杂的例子，彻底掌握 `int()` 的用法。


### 示例 1：基础用法 - 转换数字


## 实例


```python
# 从浮点数转换
print(int(3.7))      # 输出: 3
print(int(-3.7))     # 输出: -3

# 从布尔值转换
print(int(True))     # 输出: 1
print(int(False))    # 输出: 0

# 从字符串转换
print(int("42"))     # 输出: 42
print(int("  10  ")) # 输出: 10（自动去除空格）
```


**运行结果预期:**


```
3
-3
1
0
42
10
```


**代码解析:**


- 浮点数转换为整数时，会直接截断小数部分（向零取整），而不是四舍五入。
- 布尔值 `True` 转换为 1，`False` 转换为 0。
- 字符串转换时，会自动去除首尾的空白字符。


### 示例 2：进制转换


`int()` 支持将不同进制的字符串转换为十进制整数。


## 实例


```python
# 二进制字符串（以 0b 开头）
print(int("1010", 2))   # 输出: 10

# 八进制字符串（以 0o 开头）
print(int("12", 8))     # 输出: 10

# 十六进制字符串（以 0x 开头）
print(int("a", 16))     # 输出: 10
print(int("FF", 16))    # 输出: 255

# 带前缀的字符串
print(int("0b1010", 2)) # 输出: 10
print(int("0o12", 8))   # 输出: 10
print(int("0xff", 16))  # 输出: 255
```


**运行结果预期:**


```
10
10
10
255
10
10
255
```


**代码解析:**


- 第二个参数指定了字符串的数字进制：2 表示二进制，8 表示八进制，16 表示十六进制。
- 字符串可以带前缀（如 `0b`, `0o`, `0x`），也可以不带。
- 十六进制中，a-f 可以是大写或小写。


### 示例 3：常见应用场景


`int()` 在实际编程中有很多应用场景，比如用户输入处理、数据清洗等。


## 实例


```python
# 处理用户输入（input 返回字符串）
# 假设用户输入了 "100"
user_input = "100"
price = int(user_input)
print(f"商品价格: {price} 元")  # 输出: 商品价格: 100 元

# 从文件读取的数字字符串
numbers_str = ["10", "20", "30"]
numbers = [int(n) for n in numbers_str]
print(numbers)  # 输出: [10, 20, 30]

# 计算总和
total = sum(numbers)
print(f"总和: {total}")  # 输出: 总和: 60

# 处理带小数的字符串（先转float再转int）
price_str = "19.99"
price = int(float(price_str))
print(f"价格（取整）: {price} 元")  # 输出: 价格（取整）: 19 元
```


**运行结果预期:**


```
商品价格: 100 元
[10, 20, 30]
总和: 60
价格（取整）: 19 元
```


这个例子展示了 `int()` 在实际应用中的常见用法，包括处理用户输入、批量转换数据等。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python re.fullmatch() 方法](https://www.runoob.com/python-re-fullmatch.html)
			[Python float() 函数](https://www.runoob.com/python3-func-float.html) **













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
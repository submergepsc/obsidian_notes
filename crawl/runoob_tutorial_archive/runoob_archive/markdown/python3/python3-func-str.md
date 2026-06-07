# Python str() 函数

- Source: https://www.runoob.com/python3/python3-func-str.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`str()` 是 Python 中最常用的内置函数之一，用于将其他类型的数据转换为字符串类型。


字符串是 Python 中最常用的数据类型之一，`str()` 函数可以帮助我们将数字、列表、元组等转换为字符串，方便输出和拼接。


**单词释义**： `str` 是 `string`（字符串）的缩写。


---


## 基本语法与参数


`str()` 是一个内置函数，可以直接调用。


### 语法格式


```
str(object)
str(object, encoding)
str(object, errors)
```


### 参数说明


- **参数 object**： 类型： 任意对象
- 描述： 要转换为字符串的对象。


**参数 encoding**（可选）：
- 类型： 字符串
- 描述： 编码格式（如 'utf-8', 'gbk'）。


**参数 errors**（可选）：
- 类型： 字符串
- 描述： 错误处理方式，默认为 'strict'（抛出异常）。其他选项：'ignore', 'replace'。


### 函数说明


- **返回值**： 返回字符串对象。
- **默认行为**： 不带参数返回空字符串 `""`。


---


## 实例


让我们通过例子掌握 `str()` 的用法。


### 示例 1：基础用法 - 转换各种类型


## 实例


```python
# 整数转字符串
print(str(123))           # 输出: 123
print(type(str(123)))     # 输出: <class 'str'>

# 浮点数转字符串
print(str(3.14159))       # 输出: 3.14159

# 布尔值转字符串
print(str(True))          # 输出: True
print(str(False))         # 输出: False

# 列表转字符串
print(str([1, 2, 3]))     # 输出: [1, 2, 3]

# 元组转字符串
print(str((1, 2, 3)))     # 输出: (1, 2, 3)

# 字典转字符串
print(str({"name": "Tom", "age": 20}))  # 输出: {'name': 'Tom', 'age': 20}

# 空参数
print(str())              # 输出: （空行）
```


**运行结果预期:**


```
123
<class 'str'>
3.14159
True
False
[1, 2, 3]
(1, 2, 3)
{'name': 'Tom', 'age': 20}
```


**代码解析:**


- 数字转换为字符串时，保持原来的数字表示。
- 布尔值转换为字符串时，首字母大写。
- 列表、元组、字典等容器类型会转换为它们的字符串表示。


### 示例 2：字符串拼接


## 实例


```python
name = "Tom"
age = 20
height = 1.75

# 使用 str() 转换后拼接
info = name + " " + str(age) + "岁 " + str(height) + "米"
print(info)  # 输出: Tom 20岁 1.75米

# 使用 f-string（推荐方式）
info = f"{name} {age}岁 {height}米"
print(info)  # 输出: Tom 20岁 1.75米

# 格式化输出
print("姓名: " + str(name))  # 输出: 姓名: Tom
```


**运行结果预期:**


```
Tom 20岁 1.75米
Tom 20岁 1.75米
姓名: Tom
```


**代码解析:**


- `str()` 转换后可以使用加号进行字符串拼接。
- 现代 Python 推荐使用 f-string 进行字符串格式化，更简洁易读。


### 示例 3：处理字节和编码


## 实例


```python
# 字节串转字符串（需要指定编码）
data = b"Hello"
s = str(data, encoding='utf-8')
print(s)  # 输出: Hello

# 处理编码错误
data = b"Hello\x80"
s = str(data, encoding='utf-8', errors='ignore')
print(s)  # 输出: Hello（忽略非法字节）

s = str(data, encoding='utf-8', errors='replace')
print(s)  # 输出: Hello（用替换符代替）
```


**运行结果预期:**


```
Hello
Hello
Hello
```


这个例子展示了 `str()` 在处理字节和编码时的用法。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python set() 函数](https://www.runoob.com/python3-func-set.html)
			[Python help() 函数](https://www.runoob.com/python3-func-help.html) **













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
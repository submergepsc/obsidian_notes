# Python3 enumerate() 函数

- Source: https://www.runoob.com/python3/python3-func-enumerate.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)


---


`enumerate()` 是 Python 中用于在遍历可迭代对象时同时获取索引和值的内置函数。


使用 `enumerate()` 可以方便地同时获取元素的索引（位置）和元素本身，避免使用额外的计数器变量。


**单词释义**： `enumerate` 意为"枚举"，表示逐一列举。


---


## 基本语法与参数


### 语法格式


```
enumerate(iterable, start=0)
```


### 参数说明


- **参数 iterable**： 类型： 可迭代对象
- 描述： 要枚举的可迭代对象。


**参数 start**（可选）：
- 类型： 整数
- 描述： 索引起始值，默认为 0。


### 函数说明


- **返回值**： 返回一个 enumerate 对象（迭代器）。
- **输出**： 每次迭代返回 (index, value) 元组。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 基础 enumerate 用法
fruits = ["苹果", "香蕉", "橙子"]

# 获取索引和值
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 默认从 0 开始
print("---")
for index, fruit in enumerate(fruits):
    print(fruit)
```


**运行结果预期:**


```
0: 苹果
1: 香蕉
2: 橙子
---
0: 苹果
1: 香蕉
2: 橙子
```


**代码解析:**


- enumerate 返回 (索引, 值) 元组。
- 默认索引从 0 开始。


### 示例 2：指定起始索引


## 实例


```python
# 从 1 开始编号
fruits = ["苹果", "香蕉", "橙子"]

for i, fruit in enumerate(fruits, start=1):
    print(f"第{i}个水果: {fruit}")

# 从 10 开始
print("---")
for i, fruit in enumerate(fruits, start=10):
    print(f"索引 {i}: {fruit}")
```


**运行结果预期:**


```
第1个水果: 苹果
第2个水果: 香蕉
第3个水果: 橙子
---
索引 10: 苹果
索引 11: 香蕉
索引 12: 橙子
```


start 参数可以指定起始索引。


### 示例 3：转换为列表


## 实例


```python
# 转换为列表
fruits = ["苹果", "香蕉", "橙子"]
result = list(enumerate(fruits))
print(result)  # 输出: [(0, '苹果'), (1, '香蕉'), (2, '橙子')]

# 转换为字典（如果值是字符串）
result = dict(enumerate(fruits))
print(result)  # 输出: {0: '苹果', 1: '香蕉', 2: '橙子'}

# 配合列表推导式
squares = [x**2 for x in range(5)]
indexed_squares = [(i, v) for i, v in enumerate(squares)]
print(indexed_squares)  # 输出: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]
```


**运行结果预期:**


enumerate 可以方便地转换为列表或字典。


### 示例 4：实际应用


## 实例


```python
# 查找元素的索引
fruits = ["苹果", "香蕉", "橙子", "香蕉", "苹果"]
target = "香蕉"

for index, fruit in enumerate(fruits):
    if fruit == target:
        print(f"找到 {target} 在索引 {index}")
        break

# 配合条件查找所有匹配项
print("\n所有香蕉的位置:")
for index, fruit in enumerate(fruits):
    if fruit == "香蕉":
        print(index, end=" ")  # 输出: 1 3

# 字符串中查找字符位置
text = "hello"
for i, c in enumerate(text):
    print(f"'{c}' 在位置 {i}")
```


**运行结果预期:**


enumerate 常用于需要索引的场景，如查找、替换等操作。


### 示例 5：与字典配合


## 实例


```python
# 字典的 enumerate
person = {"name": "Tom", "age": 20, "city": "Beijing"}

# 遍历字典的键值对（需要 items）
for index, (key, value) in enumerate(person.items()):
    print(f"{index}: {key} = {value}")

# 创建带序号的字典
items = ["a", "b", "c"]
numbered = {i+1: v for i, v in enumerate(items)}
print(numbered)  # 输出: {1: 'a', 2: 'b', 3: 'c'}
```


**运行结果预期:**


enumerate 与字典配合使用时需要使用 items() 方法。

---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)








	  AI 思考中...





			** [Python3 ascii() 函数](https://www.runoob.com/python3-func-ascii.html)
			[Python3 exec 函数](https://www.runoob.com/python3-func-exec.html) **













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
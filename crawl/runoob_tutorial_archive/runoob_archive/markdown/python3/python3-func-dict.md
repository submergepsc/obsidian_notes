# Python dict() 函数

- Source: https://www.runoob.com/python3/python3-func-dict.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`dict()` 是 Python 中用于创建字典（dictionary）的内置函数。


字典是 Python 中的键值对（key-value）数据结构，每个键对应一个值。`dict()` 函数可以以多种方式创建字典。


**单词释义**： `dict` 是 `dictionary`（字典）的缩写。


---


## 基本语法与参数


### 语法格式


```
dict()
dict(mapping)
dict(**kwargs)
dict(iterable, **kwargs)
```


### 参数说明


- **参数 mapping**： 类型： 映射对象（如字典）
- 描述： 从映射对象创建新字典。


**参数 kwargs**：
- 类型： 关键字参数
- 描述： 使用关键字参数创建字典。


**参数 iterable**：
- 类型： 可迭代对象
- 描述： 元素为键值对的可迭代对象。


### 函数说明


- **返回值**： 返回一个字典对象。
- **特点**： 字典的键必须是不可变类型（如字符串、数字、元组）。


---


## 实例


### 示例 1：创建字典


## 实例


```python
# 空字典
d = dict()
print(d)  # 输出: {}

# 关键字参数（最常用）
d = dict(name="Tom", age=20)
print(d)  # 输出: {'name': 'Tom', 'age': 20}

# 从映射对象创建
d1 = {"name": "Tom"}
d2 = dict(d1)
print(d2)  # 输出: {'name': 'Tom'}

# 从可迭代对象创建（元素为键值对）
pairs = [("name", "Tom"), ("age", 20)]
d = dict(pairs)
print(d)  # 输出: {'name': 'Tom', 'age': 20}

# 从zip创建
keys = ["name", "age", "city"]
values = ["Tom", 20, "Beijing"]
d = dict(zip(keys, values))
print(d)  # 输出: {'name': 'Tom', 'age': 20, 'city': 'Beijing'}
```


**运行结果预期:**


```
{}
{'name': 'Tom', 'age': 20}
{'name': 'Tom'}
{'name': 'Tom', 'age': 20}
{'name': 'Tom', 'age': 20, 'city': 'Beijing'}
```


**代码解析:**


- 关键字参数是最常用的创建方式。
- 可迭代对象的元素必须是键值对（tuple 或 list）。
- `dict(zip())` 是合并两个列表为字典的常用技巧。


### 示例 2：字典操作


## 实例


```python
# 访问值
d = {"name": "Tom", "age": 20}
print(d["name"])     # 输出: Tom
print(d.get("age"))   # 输出: 20

# 添加/修改
d["city"] = "Beijing"
d["age"] = 21
print(d)  # 输出: {'name': 'Tom', 'age': 21, 'city': 'Beijing'}

# 删除
del d["age"]
print(d)  # 输出: {'name': 'Tom', 'city': 'Beijing'}

# 遍历
for key, value in d.items():
    print(f"{key}: {value}")
```


**运行结果预期:**


```
Tom
20
{'name': 'Tom', 'age': 21, 'city': 'Beijing'}
{'name': 'Tom', 'city': 'Beijing'}
name: Tom
city: Beijing
```


字典支持丰富的操作：访问、添加、修改、删除、遍历等。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python bytearray() 函数](https://www.runoob.com/python3-func-bytearray.html)
			[Python eval() 函数](https://www.runoob.com/python3-func-eval.html) **













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
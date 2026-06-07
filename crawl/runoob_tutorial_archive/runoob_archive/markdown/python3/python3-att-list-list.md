# Python list() 函数

- Source: https://www.runoob.com/python3/python3-att-list-list.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`list()` 是 Python 中用于将序列转换为列表（list）的内置函数。


列表是 Python 中最常用的可变序列类型，可以随时添加、删除或修改元素。`list()` 函数可以将元组、字符串、字典、集合等可迭代对象转换为列表。


**单词释义**： `list` 意为"列表"，是 Python 中的可变序列类型。


---


## 基本语法与参数


### 语法格式


```
list(iterable)
```


### 参数说明


- **参数 iterable**： 类型： 可迭代对象（元组、字符串、字典、集合等）
- 描述： 要转换为列表的可迭代对象。


### 函数说明


- **返回值**： 返回一个列表。
- **特殊值**： 不带参数返回空列表 `[]`。


---


## 实例


### 示例 1：从其他序列转换


## 实例


```python
# 从元组转换为列表
t = (1, 2, 3, 4, 5)
lst = list(t)
print(lst)        # 输出: [1, 2, 3, 4, 5]

# 从字符串转换
s = "hello"
lst = list(s)
print(lst)        # 输出: ['h', 'e', 'l', 'l', 'o']

# 从字典转换（只取键）
d = {"a": 1, "b": 2, "c": 3}
lst = list(d)
print(lst)        # 输出: ['a', 'b', 'c']

# 从集合转换
s = {3, 1, 2}
lst = list(s)
print(lst)        # 输出: [1, 2, 3]（自动排序）

# 空列表
lst = list()
print(lst)        # 输出: []
```


**运行结果预期:**


```
[1, 2, 3, 4, 5]
['h', 'e', 'l', 'l', 'o']
['a', 'b', 'c']
[1, 2, 3]
[]
```


**代码解析:**


- 元组转换为列表，保持元素顺序。
- 字符串转换时，每个字符成为列表的一个元素。
- 字典转换只包含键。


### 示例 2：列表的常用操作


## 实例


```python
# 创建列表后可以修改
lst = list((1, 2, 3))
lst.append(4)    # 添加元素
lst.insert(0, 0)  # 插入元素
print(lst)        # 输出: [0, 1, 2, 3, 4]

# 列表推导式（更简洁的方式）
lst = [x * 2 for x in range(5)]
print(lst)        # 输出: [0, 2, 4, 6, 8]

# 复制列表
original = [1, 2, 3]
copy = list(original)
print(copy)       # 输出: [1, 2, 3]
```


**运行结果预期:**


```
[0, 1, 2, 3, 4]
[0, 2, 4, 6, 8]
[1, 2, 3]
```


列表是可变的，创建后可以随时添加、删除或修改元素。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python3 List min()方法](https://www.runoob.com/python3-att-list-min.html)
			[Python3 List append()方法](https://www.runoob.com/python3-att-list-append.html) **













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
# Python set() 函数

- Source: https://www.runoob.com/python3/python3-func-set.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`set()` 是 Python 中用于创建可变集合（set）的内置函数。


集合是无序且不重复的元素集合，类似于数学中的集合概念。`set()` 函数可以从其他可迭代对象创建集合，常用于去重、集合运算等场景。


**单词释义**： `set` 意为"集合"，是 Python 中的无序不重复元素集合。


---


## 基本语法与参数


### 语法格式


```
set(iterable)
```


### 参数说明


- **参数 iterable**： 类型： 可迭代对象
- 描述： 要转换为集合的可迭代对象。


### 函数说明


- **返回值**： 返回一个可变集合。
- **特殊值**： 不带参数返回空集合 `set()`（注意：`{}` 创建的是空字典）。


---


## 实例


### 示例 1：创建集合


## 实例


```python
# 从列表创建（自动去重）
lst = [1, 2, 2, 3, 3, 3, 4]
s = set(lst)
print(s)        # 输出: {1, 2, 3, 4}

# 从字符串创建
s = set("hello")
print(s)        # 输出: {'h', 'e', 'l', 'o'}

# 从元组创建
t = (1, 2, 3, 2, 1)
s = set(t)
print(s)        # 输出: {1, 2, 3}

# 从字典创建（只取键）
d = {"a": 1, "b": 2, "c": 3}
s = set(d)
print(s)        # 输出: {'a', 'b', 'c'}

# 空集合
s = set()
print(s)        # 输出: set()
print(type(s))  # 输出: <class 'set'>
```


**运行结果预期:**


```
{1, 2, 3, 4}
{'h', 'e', 'l', 'o'}
{1, 2, 3}
{'a', 'b', 'c'}
set()
<class 'set'>
```


**代码解析:**


- 集合会自动去除重复元素。
- 集合是无序的，元素顺序可能不同。
- 注意：`{}` 创建的是空字典，不是空集合。


### 示例 2：集合运算


## 实例


```python
# 创建两个集合
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 并集
print(A | B)      # 输出: {1, 2, 3, 4, 5, 6}
print(A.union(B)) # 输出: {1, 2, 3, 4, 5, 6}

# 交集
print(A & B)      # 输出: {3, 4}
print(A.intersection(B))  # 输出: {3, 4}

# 差集（A - B）
print(A - B)      # 输出: {1, 2}
print(A.difference(B))   # 输出: {1, 2}

# 对称差集
print(A ^ B)      # 输出: {1, 2, 5, 6}
print(A.symmetric_difference(B))  # 输出: {1, 2, 5, 6}
```


**运行结果预期:**


```
{1, 2, 3, 4, 5, 6}
{1, 2, 3, 4, 5, 6}
{3, 4}
{3, 4}
{1, 2}
{1, 2}
{1, 2, 5, 6}
{1, 2, 5, 6}
```


集合支持丰富的集合运算：并集、交集、差集、对称差集。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python repr() 函数](https://www.runoob.com/python3-func-repr.html)
			[Python str() 函数](https://www.runoob.com/python3-func-str.html) **













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
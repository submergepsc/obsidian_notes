# Python frozenset() 函数

- Source: https://www.runoob.com/python3/python3-func-frozenset.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`frozenset()` 是 Python 中用于创建不可变集合（frozenset）的内置函数。


frozenset 与 set 的区别在于：frozenset 是不可变的，创建后不能添加、删除或修改元素。由于其不可变性，frozenset 可以用作字典的键或集合的元素。


**单词释义**： `frozenset` 是"冻结集合"的缩写，表示不可变的集合。


---


## 基本语法与参数


### 语法格式


```
frozenset(iterable)
```


### 参数说明


- **参数 iterable**： 类型： 可迭代对象
- 描述： 要转换为不可变集合的可迭代对象。


### 函数说明


- **返回值**： 返回一个 frozenset 对象。
- **特殊值**： 不带参数返回空 frozenset。


---


## 实例


### 示例 1：创建 frozenset


## 实例


```python
# 从列表创建
lst = [1, 2, 3, 2, 1]
fs = frozenset(lst)
print(fs)        # 输出: frozenset({1, 2, 3})

# 从字符串创建
s = "hello"
fs = frozenset(s)
print(fs)        # 输出: frozenset({'h', 'e', 'l', 'o'})

# 从字典创建（取键）
d = {"a": 1, "b": 2}
fs = frozenset(d)
print(fs)        # 输出: frozenset({'a', 'b'})

# 空 frozenset
fs = frozenset()
print(fs)        # 输出: frozenset()
```


**运行结果预期:**


```
frozenset({1, 2, 3})
frozenset({'h', 'e', 'l', 'o'})
frozenset({'a', 'b'})
frozenset()
```


**代码解析:**


- frozenset 会自动去重。
- 可以和各种可迭代对象一起使用。
- frozenset 是不可变的，没有 add、remove 等方法。


### 示例 2：frozenset 的用途


## 实例


```python
# frozenset 可以作为字典的键
d = {frozenset([1, 2]): "A", frozenset([3, 4]): "B"}
print(d)  # 输出: {frozenset({1, 2}): 'A', frozenset({3, 4}): 'B'}

# frozenset 可以作为集合的元素
s = {frozenset([1, 2]), frozenset([3, 4])}
print(s)  # 输出: {frozenset({1, 2}), frozenset({3, 4})}

# frozenset 支持集合运算（但不修改原集合）
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([2, 3, 4])
print(fs1 & fs2)  # 输出: frozenset({2, 3}) 交集
print(fs1 | fs2)  # 输出: frozenset({1, 2, 3, 4}) 并集
```


**运行结果预期:**


```
{frozenset({1, 2}): 'A', frozenset({3, 4}): 'B'}
{frozenset({1, 2}), frozenset({3, 4})}
frozenset({2, 3})
frozenset({1, 2, 3, 4})
```


frozenset 的主要用途是作为字典的键或集合的元素。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python eval() 函数](https://www.runoob.com/python3-func-eval.html)
			[Python memoryview() 函数](https://www.runoob.com/python3-func-memoryview.html) **













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
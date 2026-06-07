# Python repr() 函数

- Source: https://www.runoob.com/python3/python3-func-repr.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`repr()` 是 Python 中用于获取对象可打印表示的内置函数。


`repr()` 返回一个对象的官方字符串表示，通常可以用来重新创建该对象。它与 `str()` 的区别在于，`repr()` 更侧重于调试和开发，而 `str()` 侧重于用户友好。


**单词释义**： `repr` 是 `representation`（表示）的缩写。


---


## 基本语法与参数


### 语法格式


```
repr(object)
```


### 参数说明


- **参数 object**： 类型： 任意对象
- 描述： 要获取其字符串表示的对象。


### 函数说明


- **返回值**： 返回一个字符串，通常是可以表示该对象的字符串。
- **特殊方法**： 对象可以通过定义 `__repr__` 方法自定义返回值。


---


## 实例


### 示例 1：repr() vs str()


## 实例


```python
# 字符串的区别
s = "hello"
print(f"str: '{str(s)}'")    # 输出: str: 'hello'
print(f"repr: '{repr(s)}'")  # 输出: repr: 'hello'

# 日期时间的区别
from datetime import datetime
dt = datetime.now()
print(f"str: {str(dt)}")
print(f"repr: {repr(dt)}")

# 自定义类的区别
class Person:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person: {self.name}"
    def __repr__(self):
        return f"Person(name='{self.name}')"

p = Person("Tom")
print(f"str: {str(p)}")
print(f"repr: {repr(p)}")
```


**运行结果预期:**


```
str: 'hello'
repr: 'hello'
str: 2024-01-15 10:30:45.123456
repr: datetime.datetime(2024, 1, 15, 10, 30, 45, 123456)
str: Person: Tom
repr: Person(name='Tom')
```


**代码解析:**


- 对于简单字符串，两者结果相同。
- 对于日期时间，`repr()` 返回可以重建对象的表达式。
- 自定义类可以分别定义 `__str__` 和 `__repr__` 方法。


### 示例 2：使用 repr() 调试


## 实例


```python
# 显示隐藏字符
s = "hello\nworld"
print(f"str: {str(s)}")
print(f"repr: {repr(s)}")

# 显示引号
text = "She said 'hello'"
print(f"str: {str(text)}")
print(f"repr: {repr(text)}")

# 在交互式环境中
# 直接输入变量名会调用 repr()
```


**运行结果预期:**


```
str: hello
world
repr: 'hello\nworld'
str: She said 'hello'
repr: "She said 'hello'"
```


`repr()` 可以显示隐藏字符（如换行符）和引号，方便调试。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python memoryview() 函数](https://www.runoob.com/python3-func-memoryview.html)
			[Python set() 函数](https://www.runoob.com/python3-func-set.html) **













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
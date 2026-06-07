# Python match...case 语句

- Source: https://www.runoob.com/python3/python-match-case.html

[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)


**match...case** 提供了一种更强大的模式匹配方法。

模式匹配是一种在编程中处理数据结构的方式，可以使代码更简洁、易读。

**match...case** 是 Python 3.10 版本引入的新语法。


**match...case** 语法结构如下：


```
match expression:
    case pattern1:
        # 处理pattern1的逻辑
    case pattern2 if condition:
        # 处理pattern2并且满足condition的逻辑
    case _:
        # 处理其他情况的逻辑
```


**参数说明：**


- `match`语句后跟一个表达式，然后使用`case`语句来定义不同的模式。
- `case`后跟一个模式，可以是具体值、变量、通配符等。
- 可以使用`if`关键字在`case`中添加条件。
- `_`通常用作通配符，匹配任何值。


![](https://www.runoob.com/wp-content/uploads/2023/12/match-case.png)


### 实例


**1. 简单的值匹配**


## 实例


```python
def match_example(value):
    match value:
        case 1:
            print("匹配到值为1")
        case 2:
            print("匹配到值为2")
        case _:
            print("匹配到其他值")

match_example(1)  # 输出: 匹配到值为1
match_example(2)  # 输出: 匹配到值为2
match_example(3)  # 输出: 匹配到其他值
```


以上代码中，**match** 语句用于匹配 **value** 的不同情况，每个 **case** 语句表示一种可能的匹配情况，**_** 通配符表示其他情况。


输出结果为：


```
匹配到值为1
匹配到值为2
匹配到其他值
```


**2. 使用变量**


## 实例


```python
def match_example(item):
    match item:
        case (x, y) if x == y:
            print(f"匹配到相等的元组: {item}")
        case (x, y):
            print(f"匹配到元组: {item}")
        case _:
            print("匹配到其他情况")

match_example((1, 1))  # 输出: 匹配到相等的元组: (1, 1)
match_example((1, 2))  # 输出: 匹配到元组: (1, 2)
match_example("other") # 输出: 匹配到其他情况
```


输出结果为：


```
匹配到相等的元组: (1, 1)
匹配到元组: (1, 2)
匹配到其他情况
```


**3. 类型匹配**


## 实例


```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

def match_shape(shape):
    match shape:
        case Circle(radius=1):
            print("匹配到半径为1的圆")
        case Rectangle(width=1, height=2):
            print("匹配到宽度为1，高度为2的矩形")
        case _:
            print("匹配到其他形状")

match_shape(Circle(radius=1))          # 输出: 匹配到半径为1的圆
match_shape(Rectangle(width=1, height=2)) # 输出: 匹配到宽度为1，高度为2的矩形
match_shape("other")                    # 输出: 匹配到其他形状
```


输出结果为：


```
匹配到半径为1的圆
匹配到宽度为1，高度为2的矩形
匹配到其他形状
```


[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)










	  AI 思考中...





			** [Python 创建一个简单的任务清单（to-do list）](https://www.runoob.com/python-to-do-list.html)
			[Python 量化](https://www.runoob.com/python-qt.html) **













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
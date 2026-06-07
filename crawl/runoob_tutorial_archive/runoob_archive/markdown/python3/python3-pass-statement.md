# Python pass 语句

- Source: https://www.runoob.com/python3/python3-pass-statement.html

[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)

---


`pass` 是 Python 中的空语句，也称为占位语句。


它什么都不做，只是作为一个占位符，保证代码的语法完整性。`pass` 常用在暂时不想写具体实现的代码块中，或者需要在某个位置放置一个语句但什么都不做。


**单词释义**： `pass` 意为"通过"，表示什么也不做，直接跳过。


---


## 基本语法与参数


`pass` 是一个独立的语句，不需要任何参数。


### 语法格式


```
pass
```


### 使用场景


- **空代码块**： 需要代码块但暂时不想写任何代码。
- **函数占位**： 定义函数时暂不实现函数体。
- **类占位**： 定义类时暂不实现方法。
- **条件占位**： 条件分支暂不执行任何操作。


---


## 实例


### 示例 1：if 语句中使用


## 实例


```python
# 条件分支暂不处理
age = 20

if age >= 18:
    pass  # TODO: 需要添加年龄验证逻辑
else:
    print("未成年")

print("程序继续执行")
```


**运行结果预期:**


```
程序继续执行
```


**代码解析:**


- age >= 18 为 True，但 pass 不执行任何操作。
- 如果不加 pass，代码块为空会报错。


### 示例 2：函数中使用


## 实例


```python
# 定义空函数
def placeholder_function():
    pass

# 调用函数
placeholder_function()
print("函数已调用")

# 带条件的空函数
def process_data(data):
    if not data:
        pass  # 数据为空，暂不处理
        return
    # 实际的处理逻辑
    return data.upper()

print(process_data("hello"))  # 输出: HELLO
print(process_data(""))       # 输出: None
```


**运行结果预期:**


```
函数已调用
HELLO
None
```


函数定义时，如果函数体暂时为空，必须使用 pass 占位。


### 示例 3：类中使用


## 实例


```python
# 定义空类
class EmptyClass:
    pass

# 实例化
obj = EmptyClass()
print(obj)  # 输出: <__main__.EmptyClass object at ...>

# 类中定义空方法
class TodoClass:
    def method1(self):
        pass

    def method2(self):
        return "已完成"

obj = TodoClass()
print(obj.method2())  # 输出: 已完成
```


**运行结果预期:**


空类或空方法可以使用 pass 占位，后续再实现具体功能。


### 示例 4：循环中使用


## 实例


```python
# 遍历但什么都不做
for i in range(5):
    pass  # 暂时不处理

print("循环完成")

# 配合条件使用
for i in range(10):
    if i % 2 == 0:
        pass  # 偶数不处理
    else:
        print(i, end=" ")
# 输出: 1 3 5 7 9
```


**运行结果预期:**


```
循环完成
1 3 5 7 9
```


`pass` 在循环中也可以作为占位符使用。


---


[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)








	  AI 思考中...





			** [Python else 语句](https://www.runoob.com/python3-else-statement.html)
			[Python match 语句](https://www.runoob.com/python3-match-statement.html) **













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
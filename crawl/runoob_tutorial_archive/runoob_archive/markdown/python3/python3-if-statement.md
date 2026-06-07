# Python if 语句

- Source: https://www.runoob.com/python3/python3-if-statement.html

[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)

---


在 Python 编程中，`if` 语句是最基本也是最重要的条件控制结构。它用于根据条件的真假来决定是否执行特定的代码块。


Python 的 `if` 语句非常直观易读，通过缩进来定义代码块，这是 Python 区别于其他语言的一大特色。


**单词释义**： `if` 意为"如果"，是条件判断的入口。


---


## 基本语法与参数


`if` 语句是独立的代码块，需要配合条件表达式使用。


### 语法格式


```
if 条件表达式:
    代码块
```


### 语法说明


- **条件表达式**： 任何返回布尔值的表达式（非零、非空字符串、非空容器等视为真）。
- **冒号**： 条件表达式后必须加冒号。
- **缩进**： 代码块必须缩进（通常 4 个空格），缩进的代码属于 if 语句的子块。


### 返回值/效果


- **无返回值**： if 语句是控制流语句，不返回任何值。
- **效果**： 当条件为 True 时执行缩进的代码块，否则跳过。


---


## 实例


让我们通过一系列从简单到复杂的例子，彻底掌握 `if` 语句的用法。


### 示例 1：基础用法 - 判断数字大小


## 实例


```python
# 基础 if 语句
age = 18

if age >= 18:
    print("成年人")

print("程序结束")
```


**运行结果预期:**


```
成年人
程序结束
```


**代码解析:**


- `age >= 18` 是条件表达式，返回 True。
- 因为条件成立，执行 `print("成年人")`。
- `print("程序结束")` 不在 if 的缩进块内，无论条件如何都会执行。


### 示例 2：判断字符串是否为空


## 实例


```python
# 判断字符串
name = ""

# 字符串为空时为 False
if name:
    print(f"你好, {name}")
else:
    print("请输入名字")

# 非空字符串
name = "Tom"
if name:
    print(f"你好, {name}")
```


**运行结果预期:**


```
请输入名字
你好, Tom
```


**代码解析:**


- Python 中空字符串、空列表、空字典等在条件判断时视为 False。
- 非空字符串视为 True。


### 示例 3：多个条件判断


## 实例


```python
# 复合条件判断
score = 85

# 使用逻辑运算符
if score >= 60 and score < 90:
    print("及格了")

# 判断多个条件（简化写法）
if 60 <= score < 90:  # Python 特有的链式比较
    print("成绩在 60-90 之间")

# 使用 in 判断
colors = ["red", "green", "blue"]
if "red" in colors:
    print("包含红色")
```


**运行结果预期:**


```
及格了
成绩在 60-90 之间
包含红色
```


**代码解析:**


- Python 支持链式比较，如 `60







	  AI 思考中...





			** [Python hash() 函数](https://www.runoob.com/python3-func-hash.html)
			[Python elif 语句](https://www.runoob.com/python3-elif-statement.html) **













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
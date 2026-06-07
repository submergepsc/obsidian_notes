# Python match 语句

- Source: https://www.runoob.com/python3/python3-match-statement.html

[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)

---


`match` 是 Python 3.10 引入的结构化模式匹配语句，类似于其他语言中的 `switch-case`，但功能更强大。


match 语句可以匹配数据结构的模式，不仅可以是常量值，还可以是类型、序列、字典等复杂模式。


**单词释义**： `match` 意为"匹配"，用于模式匹配。


---


## 基本语法与参数


match 语句是 Python 3.10+ 的新特性，用于替代复杂的多分支 if-elif 结构。


### 语法格式


```
match 变量:
    case 模式1:
        代码块1
    case 模式2:
        代码块2
    case _:
        默认代码块
```


### 模式类型


- **常量模式**： 匹配具体的值。
- **通配符模式**： `case _` 匹配任何值，相当于 default。
- **类型模式**： 匹配数据类型。
- **序列模式**： 匹配列表、元组等序列。
- **字典模式**： 匹配字典。
- **带条件的模式**： 使用 `if` 添加额外条件。


---


## 实例


### 示例 1：基础用法（类似 switch）


## 实例


```python
# Python 版本要求 3.10+
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"

print(http_status(200))   # 输出: OK
print(http_status(404))   # 输出: Not Found
print(http_status(999))   # 输出: Unknown
```


**运行结果预期:**


```
OK
Not Found
Unknown
```


**代码解析:**


- `case _` 是通配符，匹配所有未匹配的情况。
- 类似于 switch-case 中的 default。


### 示例 2：多值匹配


## 实例


```python
# 多个值匹配同一结果
def color_name(code):
    match code:
        case "r" | "R":
            return "红色"
        case "g" | "G":
            return "绿色"
        case "b" | "B":
            return "蓝色"
        case _:
            return "未知"

print(color_name("r"))  # 输出: 红色
print(color_name("G"))  # 输出: 绿色
print(color_name("x"))  # 输出: 未知
[/mycode]</div>
</div>

<p><strong>运行结果预期:</strong></p>
<pre>红色
绿色
未知
</pre>
<p>使用 <code>|</code> 可以将多个值组合到同一个 case。</p>
<h3>示例 3：序列模式匹配</h3>

<div class="example">
<h2 class="example">实例</h2>
<div class="example_code">[mycode4 type="python"]
# 序列模式匹配
def describe_point(point):
    match point:
        case (0, 0):
            return "原点"
        case (x, 0):
            return f"X轴上的点 ({x}, 0)"
        case (0, y):
            return f"Y轴上的点 (0, {y})"
        case (x, y):
            return f"平面上的点 ({x}, {y})"
        case _:
            return "无效坐标"

print(describe_point((0, 0)))      # 输出: 原点
print(describe_point((5, 0)))      # 输出: X轴上的点 (5, 0)
print(describe_point((3, 4)))      # 输出: 平面上的点 (3, 4)
```


**运行结果预期:**


```
原点
X轴上的点 (5, 0)
平面上的点 (3, 4)
```


match 可以解构元组/列表，提取其中的值。


### 示例 4：字典模式匹配


## 实例


```python
# 字典模式匹配
def process_user(user):
    match user:
        case {"name": name, "age": age}:
            return f"用户: {name}, 年龄: {age}"
        case {"name": name}:
            return f"用户: {name}"
        case _:
            return "无效用户"

print(process_user({"name": "Tom", "age": 20}))
print(process_user({"name": "Jerry"}))
print(process_user({"role": "admin"}))
```


**运行结果预期:**


```
用户: Tom, 年龄: 20
用户: Jerry
无效用户
```


字典模式可以提取特定键的值。


### 示例 5：带条件的模式


## 实例


```python
# 带条件的模式匹配
def classify_number(n):
    match n:
        case n if n > 0:
            return f"正数 ({n})"
        case n if n < 0:
            return f"负数 ({n})"
        case 0:
            return "零"

print(classify_number(10))   # 输出: 正数 (10)
print(classify_number(-5))    # 输出: 负数 (-5)
print(classify_number(0))     # 输出: 零

# 复杂条件
def describe_list(lst):
    match lst:
        case []:
            return "空列表"
        case [x]:
            return f"单个元素: {x}"
        case [x, y]:
            return f"两个元素: {x}, {y}"
        case [x, *rest]:
            return f"第一个: {x}, 其余: {rest}"

print(describe_list([]))
print(describe_list([1]))
print(describe_list([1, 2, 3, 4]))
```


**运行结果预期:**


```
正数 (10)
负数 (-5)
零
空列表
单个元素: 1
第一个: 1, 其余: [2, 3, 4]
```


使用 `case 变量 if 条件` 可以添加额外的匹配条件。


---


[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)








	  AI 思考中...





			** [Python pass 语句](https://www.runoob.com/python3-pass-statement.html)
			[Python for 循环](https://www.runoob.com/python3-for.html) **













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
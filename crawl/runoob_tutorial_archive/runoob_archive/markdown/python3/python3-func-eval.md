# Python eval() 函数

- Source: https://www.runoob.com/python3/python3-func-eval.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`eval()` 是 Python 中用于执行字符串中的 Python 表达式的内置函数。


`eval()` 接收一个字符串，将其作为 Python 代码来执行，并返回执行结果。它是一个强大的功能，但使用不当会带来安全风险。


**单词释义**： `eval` 是 `evaluate`（求值）的缩写。


---


## 基本语法与参数


### 语法格式


```
eval(expression, globals, locals)
```


### 参数说明


- **参数 expression**： 类型： 字符串
- 描述： 要执行的 Python 表达式。


**参数 globals**（可选）：
- 类型： 字典
- 描述： 全局命名空间。


**参数 locals**（可选）：
- 类型： 字典
- 描述： 局部命名空间。


### 函数说明


- **返回值**： 返回表达式的执行结果。
- **安全警告**： 不要对不可信的输入使用 `eval()`，可能导致代码注入攻击。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 计算数学表达式
result = eval("1 + 2 + 3")
print(result)  # 输出: 6

# 使用变量
x = 10
result = eval("x * 2")
print(result)  # 输出: 20

# 复杂表达式
result = eval("2 ** 3 + 4 * 5")
print(result)  # 输出: 28

# 函数调用
result = eval("len('hello')")
print(result)  # 输出: 5
```


**运行结果预期:**


```
6
20
28
5
```


**代码解析:**


- `eval()` 可以执行算术表达式。
- 可以引用已定义的变量。
- 可以调用内置函数。


### 示例 2：受限环境


## 实例


```python
# 限制可用的函数和变量
x = 10
y = 20

# 创建一个受限的全局字典
safe_dict = {"x": x, "y": y, "abs": abs}

result = eval("x + y", safe_dict)
print(result)  # 输出: 30

# 不允许访问危险函数
try:
    eval("__import__('os').system('ls')", {})
except NameError as e:
    print(f"安全限制: {e}")
```


**运行结果预期:**


```
30
安全限制: name '__import__' is not defined
```


这个例子展示了如何通过限制 globals 字典来提高 `eval()` 的安全性。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python dict() 函数](https://www.runoob.com/python3-func-dict.html)
			[Python frozenset() 函数](https://www.runoob.com/python3-func-frozenset.html) **













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
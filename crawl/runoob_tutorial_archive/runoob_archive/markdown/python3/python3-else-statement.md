# Python else 语句

- Source: https://www.runoob.com/python3/python3-else-statement.html

[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)

---


`else` 是 Python 中用于处理其他所有情况的关键字。


`else` 语句与 `if` 和 `elif` 配合使用，当所有前面的条件都不满足时，执行 `else` 代码块中的代码。


**单词释义**： `else` 意为"其他"，表示所有条件都不满足时的情况。


---


## 基本语法与参数


`else` 必须与 `if` 配合使用，作为整个条件判断结构的收尾。


### 语法格式


```
if 条件:
    代码块1
else:
    代码块2
```


### 语法说明


- **位置**： `else` 必须是 if-elif 链的最后一个分支。
- **无需条件**： `else` 后面不需要跟条件表达式。
- **必然执行**： 如果前面的所有条件都不满足，else 代码块必然会执行。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 简单的二选一
age = 15

if age >= 18:
    print("成年人")
else:
    print("未成年人")

# 偶数奇数判断
num = 7
if num % 2 == 0:
    print(f"{num} 是偶数")
else:
    print(f"{num} 是奇数")
```


**运行结果预期:**


```
未成年人
7 是奇数
```


**代码解析:**


- age = 15，不满足 age >= 18，执行 else 分支。
- 7 % 2 = 1，不等于 0，执行 else 分支。


### 示例 2：与 elif 配合


## 实例


```python
# 完整的 if-elif-else 结构
score = 55

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"分数: {score}, 等级: {grade}")
# 输出: 分数: 55, 等级: F
```


**运行结果预期:**


```
分数: 55, 等级: F
```


else 作为最后的"兜底"分支，处理所有不满足前面条件的情况。


### 示例 3：处理异常情况


## 实例


```python
# 登录验证示例
username = "admin"
password = "wrong"

if username == "admin" and password == "123456":
    print("登录成功")
else:
    print("登录失败，请检查用户名或密码")

# 处理列表为空的情况
items = []
if items:
    print(f"列表有 {len(items)} 个元素")
else:
    print("列表为空")

# 文件操作中的 else
try:
    result = 10 / 2
except ZeroDivisionError:
    print("不能除以零")
else:
    print(f"计算结果: {result}")
```


**运行结果预期:**


```
登录失败，请检查用户名或密码
列表为空
计算结果: 5.0
```


else 还可以用于 try-except 结构，表示没有异常时的处理。


---


[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)








	  AI 思考中...





			** [Python elif 语句](https://www.runoob.com/python3-elif-statement.html)
			[Python pass 语句](https://www.runoob.com/python3-pass-statement.html) **













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
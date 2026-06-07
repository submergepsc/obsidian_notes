# Python elif 语句

- Source: https://www.runoob.com/python3/python3-elif-statement.html

[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)

---


`elif` 是 Python 中用于多条件判断的关键字，它是 "else if" 的缩写。


当需要处理多个条件时，`elif` 允许我们串联多个条件判断，形成完整的分支结构。


**单词释义**： `elif` 是 "else if" 的缩写，意为"其他的如果"。


---


## 基本语法与参数


`elif` 必须与 `if` 配合使用，不能单独存在。


### 语法格式


```
if 条件1:
    代码块1
elif 条件2:
    代码块2
elif 条件3:
    代码块3
else:
    代码块4
```


### 语法说明


- **条件判断顺序**： 从上到下依次判断，遇到第一个 True 条件时执行对应代码块，然后跳过其余分支。
- **数量限制**： `elif` 数量没有限制，可以根据需要添加任意多个。
- **可选 else**： `else` 是可选的，当所有条件都不满足时执行。


---


## 实例


### 示例 1：基础多条件判断


## 实例


```python
# 成绩分级系统
score = 85

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

print(f"成绩等级: {grade}")  # 输出: 成绩等级: B
```


**运行结果预期:**


```
成绩等级: B
```


**代码解析:**


- score = 85，首先检查 `score >= 90`（False）。
- 继续检查 `score >= 80`（True），执行对应代码块。
- 一旦匹配成功，立即跳出整个 if-elif 链。


### 示例 2：字符串匹配


## 实例


```python
# 简单的菜单选择
choice = "2"

if choice == "1":
    print("你选择了新建文件")
elif choice == "2":
    print("你选择了打开文件")
elif choice == "3":
    print("你选择了保存文件")
elif choice == "4":
    print("你选择了退出")
else:
    print("无效选择")
```


**运行结果预期:**


```
你选择了打开文件
```


**代码解析:**


- elif 用于多选项的分支判断。
- 每个分支互斥，只执行第一个匹配的条件。


### 示例 3：复杂的条件组合


## 实例


```python
# 多条件组合判断
age = 25
income = 5000

if age < 18:
    print("未成年人")
elif age >= 18 and income < 3000:
    print("成年人，低收入")
elif age >= 18 and income >= 3000 and income < 10000:
    print("成年人，中等收入")
elif age >= 18 and income >= 10000:
    print("成年人，高收入")

# 使用 elif 实现更清晰的逻辑
status = "error"
if status == "success":
    print("操作成功")
elif status == "error":
    print("操作失败")
elif status == "warning":
    print("警告")
elif status == "info":
    print("信息")
```


**运行结果预期:**


```
成年人，中等收入
操作失败
```


elif 使得多条件分支的代码更加清晰易读。


---


[![Python3 条件控制](https://www.runoob.com/images/up.gif) Python3 条件控制](https://www.runoob.com/python3-conditional-statements.html)








	  AI 思考中...





			** [Python if 语句](https://www.runoob.com/python3-if-statement.html)
			[Python else 语句](https://www.runoob.com/python3-else-statement.html) **













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
# Python for-else 循环

- Source: https://www.runoob.com/python3/python3-for-else.html

[![Python3 循环语句](https://www.runoob.com/images/up.gif) Python3 循环语句](https://www.runoob.com/python3-loop.html)

---


在 Python 中，`for` 循环可以带有一个 `else` 子句，这是 Python 特有的语法，与大多数其他编程语言不同。


`for-else` 结构表示：当循环正常完成（即没有被 `break` 中断）时，执行 `else` 中的代码。


**单词释义**： `else` 意为"其他"，在这里表示"循环正常结束后的处理"。


---


## 基本语法与参数


### 语法格式


```
for 变量 in 可迭代对象:
    循环体
else:
    循环正常结束时的处理
```


### 执行逻辑


- **正常完成**： 循环遍历完所有元素后，执行 else 子句。
- **被 break 终止**： 如果循环被 break 中断，则不执行 else 子句。
- **异常终止**： 如果循环中发生异常，else 也不执行。


---


## 实例


### 示例 1：基础用法 - 搜索失败时执行


## 实例


```python
# 查找列表中的偶数，找到则打印，没找到则执行 else
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print(f"找到偶数: {num}")
        break
else:
    print("未找到偶数")

print("---")

# 列表中有偶数的情况
numbers = [1, 3, 6, 7, 9]
for num in numbers:
    if num % 2 == 0:
        print(f"找到偶数: {num}")
        break
else:
    print("未找到偶数")
```


**运行结果预期:**


```
未找到偶数
---
找到偶数: 6
```


**代码解析:**


- 第一个例子：遍历完整个列表（没有执行 break），执行 else。
- 第二个例子：找到偶数后执行 break，跳过 else。


### 示例 2：常见应用 - 查找质数


## 实例


```python
# 判断一个数是否为质数
def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print(f"{n} 不是质数，能被 {i} 整除")
            return False
    else:
        # 循环正常结束，说明没有找到因数
        print(f"{n} 是质数")
        return True

# 测试
is_prime(7)   # 输出: 7 是质数
is_prime(10)  # 输出: 10 不是质数，能被 2 整除
```


**运行结果预期:**


```
7 是质数
10 不是质数，能被 2 整除
```


这是 for-else 最经典的用法之一：搜索遍历完成后，如果没找到目标执行 else。


### 示例 3：与 break 对比


## 实例


```python
# 场景：遍历列表查找特定元素
fruits = ["apple", "banana", "orange", "grape"]

# 使用 for-else
print("=== 使用 for-else ===")
for fruit in fruits:
    if fruit == "orange":
        print(f"找到: {fruit}")
        break
    print(f"检查: {fruit}")
else:
    print("未找到目标")

print("\n=== 不使用 break ===")
# 另一种写法（不使用 else）
found = False
for fruit in fruits:
    if fruit == "orange":
        print(f"找到: {fruit}")
        found = True
        break
    print(f"检查: {fruit}")

if not found:
    print("未找到目标")
```


**运行结果预期:**


```
=== 使用 for-else ===
检查: apple
检查: banana
找到: orange

=== 不使用 else ===
检查: apple
检查: banana
找到: orange
```


for-else 语法更加简洁，不需要额外的标志变量。


### 示例 4：处理循环结束


## 实例


```python
# 场景：验证所有元素是否满足条件
scores = [85, 90, 78, 92, 88]

# 检查是否有不及格的
print("=== 检查是否有不及格 ===")
for score in scores:
    if score < 60:
        print(f"发现不及格: {score}")
        break
    print(f"{score} 分，合格")
else:
    print("所有成绩都及格")

# 另一种场景：完成所有处理后执行清理
print("\n=== 处理完成后清理 ===")
files = ["a.txt", "b.txt", "c.txt"]

for file in files:
    print(f"处理文件: {file}")
else:
    print("所有文件处理完成，执行清理工作")
    print("--- 清理完成 ---")
```


**运行结果预期:**


```
=== 检查是否有不及格 ===
85 分，合格
90 分，合格
78 分，合格
92 分，合格
88 分，合格
所有成绩都及格

=== 处理完成后清理 ===
处理文件: a.txt
处理文件: b.txt
处理文件: c.txt
所有文件处理完成，执行清理工作
--- 清理完成 ---
```


for-else 还可以用于"完成后执行清理"的场景。


### 示例 5：实际应用 - 登录验证


## 实例


```python
# 模拟登录尝试
def try_login(username, password):
    valid_users = {
        "admin": "123456",
        "user": "password",
        "guest": "guest"
    }

    print(f"尝试登录: {username}")

    for user, pwd in valid_users.items():
        if user == username and pwd == password:
            print("登录成功！")
            return True

    else:
        # 遍历完所有用户都没匹配
        print("用户名或密码错误")
        return False

# 测试
try_login("admin", "123456")  # 输出: 登录成功
print("---")
try_login("admin", "wrong")    # 输出: 用户名或密码错误
```


**运行结果预期:**


```
尝试登录: admin
登录成功！
---
尝试登录: admin
用户名或密码错误
```


for-else 在遍历搜索场景中非常有用，可以清晰表达"没找到"的逻辑。


### 注意事项


- `else` 不是 `if` 的一部分，而是 `for` 的一部分。
- 不要把 `else` 和 `if` 混淆使用。
- 这种语法是 Python 特有的，其他语言没有。


---


[![Python3 循环语句](https://www.runoob.com/images/up.gif) Python3 循环语句](https://www.runoob.com/python3-loop.html)

---








	  AI 思考中...





			** [Python continue 语句](https://www.runoob.com/python3-continue.html)
			[Python math.cbrt() 函数](https://www.runoob.com/ref-math-cbrt.html) **













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
# Python continue 语句

- Source: https://www.runoob.com/python3/python3-continue.html

[![Python3 循环语句](https://www.runoob.com/images/up.gif) Python3 循环语句](https://www.runoob.com/python3-loop.html)

---


`continue` 是 Python 中用于跳过本次循环、进入下一次迭代的关键字。


与 `break` 不同，`continue` 不会终止整个循环，只是跳过当前这一次循环的剩余代码。


**单词释义**： `continue` 意为"继续"，跳过当前迭代，进入下一次。


---


## 基本语法与参数


`continue` 是一个独立的语句，不需要任何参数。


### 语法格式


```
for item in iterable:
    if 跳过条件:
        continue
    # 处理代码
```


### 使用场景


- **跳过特定元素**： 满足条件时跳过处理。
- **过滤数据**： 排除不符合条件的数据。
- **简化逻辑**： 将"不处理"的条件提前，减少嵌套。


---


## 实例


### 示例 1：跳过偶数


## 实例


```python
# 打印 1-10 的奇数
for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i, end=" ")
print()
# 输出: 1 3 5 7 9
```


**运行结果预期:**


```
1 3 5 7 9
```


**代码解析:**


- 当 i 是偶数时，执行 continue，跳过后面的 print。
- 当 i 是奇数时，正常执行 print。


### 示例 2：过滤列表元素


## 实例


```python
# 过滤掉空值和 None
data = ["apple", None, "", "banana", " ", "cherry"]

# 方式1：使用 continue
result = []
for item in data:
    if not item:  # 空字符串或 None 为 False
        continue
    result.append(item)

print(result)  # 输出: ['apple', 'banana', ' ', 'cherry']

# 方式2：只处理有效的
print("有效数据：")
for item in data:
    if item:  # 非空非 None
        print(f"- {item}")
```


**运行结果预期:**


```
['apple', 'banana', ' ', 'cherry']
有效数据：
- apple
- banana
-
- cherry
```


continue 可以用于过滤数据，排除不需要的元素。


### 示例 3：在 while 循环中使用


## 实例


```python
# 模拟跳过特定数字
n = 0
while n < 10:
    n += 1
    if n == 5 or n == 7:
        continue  # 跳过 5 和 7
    print(n, end=" ")
print()
# 输出: 1 2 3 4 6 8 9 10
```


**运行结果预期:**


```
1 2 3 4 6 8 9 10
```


continue 在 while 循环中的作用相同。


### 示例 4：简化代码逻辑


## 实例


```python
# 使用 continue 简化逻辑
numbers = [1, 2, -3, 4, -5, 6, -7]

# 不使用 continue（嵌套较深）
print("正数（方式1）：")
for n in numbers:
    if n > 0:
        print(n)

print("\n正数（方式2）- 使用 continue）：")
for n in numbers:
    if n <= 0:
        continue
    print(n)

print("\n负数：")
for n in numbers:
    if n >= 0:
        continue
    print(n)
```


**运行结果预期:**


使用 continue 可以使代码更扁平，减少嵌套。


### 示例 5：嵌套循环中的 continue


## 实例


```python
# continue 只影响当前循环
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue  # 跳过内层本次迭代
        print(f"({i},{j})", end=" ")
    print()
```


**运行结果预期:**


```
(1,1) (1,3)
(2,1) (2,3)
(3,1) (3,3)
```


continue 只跳过包含它的最内层循环的当前迭代。


---


[![Python3 循环语句](https://www.runoob.com/images/up.gif) Python3 循环语句](https://www.runoob.com/python3-loop.html)

---








	  AI 思考中...





			** [Python break 语句](https://www.runoob.com/python3-break.html)
			[Python for-else 循环](https://www.runoob.com/python3-for-else.html) **













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
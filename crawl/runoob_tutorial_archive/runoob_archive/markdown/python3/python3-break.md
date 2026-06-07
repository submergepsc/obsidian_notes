# Python break 语句

- Source: https://www.runoob.com/python3/python3-break.html

[![Python3 循环语句](https://www.runoob.com/images/up.gif) Python3 循环语句](https://www.runoob.com/python3-loop.html)

---


`break` 是 Python 中用于立即终止循环的关键字。


当程序执行到 `break` 时，会立即跳出当前的循环结构（无论是 for 还是 while），不再执行循环中剩余的代码。


**单词释义**： `break` 意为"打破、中断"，用于终止循环。


---


## 基本语法与参数


`break` 是一个独立的语句，不需要任何参数。


### 语法格式


```
while 条件:
    if 退出条件:
        break
    # 其他代码
```


### 使用场景


- **提前退出**： 满足特定条件时立即退出循环。
- **搜索终止**： 找到目标后退出搜索。
- **无限循环退出**： 配合 while True 使用，通过 break 退出。


---


## 实例


### 示例 1：在 for 循环中使用


## 实例


```python
# 在列表中查找第一个偶数
numbers = [1, 3, 5, 6, 7, 8, 9]

for num in numbers:
    if num % 2 == 0:
        print(f"找到第一个偶数: {num}")
        break

print("搜索结束")
```


**运行结果预期:**


```
找到第一个偶数: 6
搜索结束
```


**代码解析:**


- 遍历列表，找到第一个偶数后立即退出。
- 不再继续遍历后面的元素。


### 示例 2：在 while 循环中使用


## 实例


```python
# 累加直到超过 100
total = 0
i = 1

while True:
    total += i
    if total > 100:
        print(f"当 i = {i} 时，总和首次超过 100")
        break
    i += 1

print(f"总和: {total}")  # 输出: 总和: 105
```


**运行结果预期:**


当总和超过 100 时立即退出循环。


### 示例 3：嵌套循环中的 break


## 实例


```python
# 嵌套循环：break 只退出内层循环
for i in range(1, 4):
    for j in range(1, 4):
        if i == 2 and j == 2:
            break  # 只退出内层循环
        print(f"({i}, {j})", end=" ")
    print()  # 换行
```


**运行结果预期:**


```
(1, 1) (1, 2) (1, 3)
(2, 1) (2, 3)
(3, 1) (3, 2) (3, 3)
```


**代码解析:**


- break 只退出包含它的最内层循环。
- 外层循环继续执行。


### 示例 4：配合 else 使用


## 实例


```python
# break 导致 else 不执行
for i in range(5):
    if i == 3:
        print("找到目标，提前退出")
        break
    print(i)
else:
    print("循环正常结束，未找到目标")

print("---")

# 正常结束（未 break）
for i in range(5):
    print(i)
else:
    print("循环正常结束，else 执行")
```


**运行结果预期:**


```
0
1
2
找到目标，提前退出
---
0
1
2
3
4
循环正常结束，else 执行
```


for-else 或 while-else 结构中，break 会导致 else 不执行。


---


[![Python3 循环语句](https://www.runoob.com/images/up.gif) Python3 循环语句](https://www.runoob.com/python3-loop.html)

---








	  AI 思考中...





			** [Python while 循环](https://www.runoob.com/python3-while.html)
			[Python continue 语句](https://www.runoob.com/python3-continue.html) **













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
# Python while 循环

- Source: https://www.runoob.com/python3/python3-while.html

[![Python3 循环语句](https://www.runoob.com/images/up.gif) Python3 循环语句](https://www.runoob.com/python3-loop.html)

---


`while` 是 Python 中的条件循环语句，只要条件为 True，就会持续执行循环体。


与 `for` 不同，`while` 循环更适合于不确定循环次数、需要根据条件退出的场景。


**单词释义**： `while` 意为"当...时"，表示在条件为真时持续执行。


---


## 基本语法与参数


### 语法格式


```
while 条件:
    # 循环体（必须缩进）
    语句1
    语句2
    ...
else:
    # 可选，当循环“正常结束”时执行
    语句1
    语句2
    ...
```


### 语法说明


- **条件**： 每次循环开始前判断的条件表达式。
- **执行逻辑**： 为 True 时执行循环体，然后重新判断条件。
- **退出条件**： 条件为 False 时退出循环。


### else 子句


- **可选**： 与 for 类似，while 也可以有 else。
- **执行时机**： 条件变为 False 时执行（正常退出）。


![](https://www.runoob.com/wp-content/uploads/2026/04/python-while-else-runoob-tutorial.png)


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 基本的 while 循环
count = 0

while count < 5:
    print(count)
    count += 1

print("循环结束")
```


**运行结果预期:**


```
0
1
2
3
4
循环结束
```


**代码解析:**


- 当 count







	  AI 思考中...





			** [Python for 循环](https://www.runoob.com/python3-for.html)
			[Python break 语句](https://www.runoob.com/python3-break.html) **













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
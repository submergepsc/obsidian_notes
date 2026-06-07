# Python bool() 函数

- Source: https://www.runoob.com/python3/python3-func-bool.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`bool()` 是 Python 中用于将值转换为布尔值的内置函数。


布尔值只有两个可能：`True`（真）或 `False`（假）。


**单词释义**： `bool` 是 boolean（布尔）的缩写，表示逻辑值类型。


---


## 基本语法与参数


### 语法格式


```
bool(x)
```


### 参数说明


- **参数 x**： 类型： 任意值
- 描述： 要转换为布尔值的值。


### 函数说明


- **返回值**： 返回 `True` 或 `False`。
- **假值**： 以下值在布尔转换时为 False：`None`、`False`、0、""、()、[]、{}、`frozenset()`。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 从各种类型转换
print(bool(1))          # 输出: True
print(bool(0))          # 输出: False
print(bool(-1))         # 输出: True

print(bool(""))         # 输出: False
print(bool("hello"))    # 输出: True

print(bool([]))         # 输出: False
print(bool([1, 2]))     # 输出: True

print(bool(None))       # 输出: False

print(bool(True))       # 输出: True
print(bool(False))      # 输出: False
```


**运行结果预期:**


```
True
False
True
False
True
False
True
False
True
False
```


**代码解析:**


- 数字 0 为 False，非 0 为 True。
- 空字符串为 False，非空为 True。
- 空列表为 False，非空列表为 True。


### 示例 2：常见应用


## 实例


```python
# 判断列表是否为空
items = []
if bool(items):
    print("列表不为空")
else:
    print("列表为空")  # 输出: 列表为空

# 判断字符串是否有内容
name = ""
if bool(name.strip()):
    print(f"你好, {name}")
else:
    print("请输入名字")  # 输出: 请输入名字

# 判断值是否存在
data = {"name": "Tom"}
if bool(data.get("email")):
    print("有邮箱")
else:
    print("无邮箱")  # 输出: 无邮箱
```


**运行结果预期:**


```
列表为空
请输入名字
无邮箱
```


`bool()` 常用于条件判断，检查值是否存在或是否有内容。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python bin() 函数](https://www.runoob.com/python3-func-bin.html)
			[Python bytearray() 函数](https://www.runoob.com/python3-func-bytearray.html) **













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
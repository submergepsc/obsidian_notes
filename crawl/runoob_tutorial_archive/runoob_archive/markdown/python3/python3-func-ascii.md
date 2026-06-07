# Python ascii() 函数

- Source: https://www.runoob.com/python3/python3-func-ascii.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`ascii()` 是 Python 中用于返回对象的 ASCII 表示的内置函数。


`ascii()` 返回一个字符串，类似于 `repr()`，但它会将非 ASCII 字符转义为 ASCII 字符。这对于调试和日志记录非常有用。


**单词释义**： `ascii` 是 American Standard Code for Information Interchange（美国信息交换标准代码）的缩写。


---


## 基本语法与参数


### 语法格式


```
ascii(object)
```


### 参数说明


- **参数 object**： 类型： 任意对象
- 描述： 要获取 ASCII 表示的对象。


### 函数说明


- **返回值**： 返回一个字符串。
- **特点**： 非 ASCII 字符会被转义为 `\x`、`\u` 或 `\U` 形式。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 纯 ASCII 字符串
s = "Hello"
print(ascii(s))   # 输出: 'Hello'

# 包含非 ASCII 字符
s = "你好"
print(ascii(s))   # 输出: '\xe4\xbd\xa0\xe5\xa5\xbd'

# 中文和英文字符混合
s = "Hello 你好"
print(ascii(s))   # 输出: 'Hello \xe4\xbd\xa0\xe5\xa5\xbd'

# 其他非 ASCII 字符
s = "café"
print(ascii(s))   # 输出: 'caf\xc3\xa9'
```


**运行结果预期:**


```
'Hello'
'\xe4\xbd\xa0\xe5\xa5\xbd'
'Hello \xe4\xbd\xa0\xe5\xa5\xbd'
'caf\xc3\xa9'
```


**代码解析:**


- 纯 ASCII 字符保持不变。
- 非 ASCII 字符会被转义。
- 中文字符使用 `\x` 十六进制转义。


### 示例 2：与 repr() 对比


## 实例


```python
# repr vs ascii
s = "中文"
print(f"repr: {repr(s)}")   # 输出: repr: '中文'
print(f"ascii: {ascii(s)}") # 输出: ascii: '\xe4\xb8\xad\xe6\x96\x87'

# 列表
lst = ["Hello", "你好", "café"]
print(repr(lst))   # 输出: ['Hello', '你好', 'café']
print(ascii(lst))  # 输出: ['Hello', '\xe4\xbd\xa0\xe5\xa5\xbd', 'caf\xc3\xa9']

# 用于打印（避免编码错误）
import sys
print(ascii("测试"))  # 输出: '\xe6\xb5\x8b\xe8\xaf\x95'
```


**运行结果预期:**


```
repr: '中文'
ascii: '\xe4\xb8\xad\xe6\x96\x87'
['Hello', '你好', 'café']
['Hello', '\xe4\xbd\xa0\xe5\xa5\xbd', 'caf\xc3\xa9']
'\xe6\xb5\x8b\xe8\xaf\x95'
```


`ascii()` 对于需要在纯 ASCII 环境中显示或记录非 ASCII 字符非常有用。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)
			[Python3 enumerate() 函数](https://www.runoob.com/python3-func-enumerate.html) **













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
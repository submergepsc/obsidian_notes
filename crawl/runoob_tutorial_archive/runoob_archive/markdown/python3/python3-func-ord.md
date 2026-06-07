# Python ord() 函数

- Source: https://www.runoob.com/python3/python3-func-ord.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`ord()` 是 Python 中用于获取字符 Unicode 码点的内置函数。


`ord()` 接收一个字符（长度为 1 的字符串），返回其对应的 Unicode 码点（整数）。它是 `chr()` 的逆函数。


**单词释义**： `ord` 是 `ordinal`（序数）的缩写。


---


## 基本语法与参数


### 语法格式


```
ord(c)
```


### 参数说明


- **参数 c**： 类型： 字符（长度为 1 的字符串）
- 描述： 要获取 Unicode 码点的字符。


### 函数说明


- **返回值**： 返回一个整数，表示字符的 Unicode 码点。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 英文字母
print(ord('A'))   # 输出: 65
print(ord('Z'))   # 输出: 90
print(ord('a'))   # 输出: 97
print(ord('z'))   # 输出: 122

# 数字
print(ord('0'))   # 输出: 48
print(ord('9'))   # 输出: 57

# 常见符号
print(ord('!'))   # 输出: 33
print(ord('@'))   # 输出: 64

# 中文
print(ord('中'))  # 输出: 20013
print(ord('文'))  # 输出: 25991
print(ord('你'))  # 输出: 20320

# 空格
print(ord(' '))   # 输出: 32
```


**运行结果预期:**


```
65
90
97
122
48
57
33
64
20013
25991
20320
32
```


**代码解析:**


- 大写字母 A-Z 的 Unicode 码点是 65-90。
- 小写字母 a-z 的 Unicode 码点是 97-122。
- 中文汉字的 Unicode 码点通常大于 19968（0x4E00）。


### 示例 2：与 chr() 配合


## 实例


```python
# ord() 是 chr() 的逆函数
print(chr(ord('A')))  # 输出: A
print(ord(chr(65)))   # 输出: 65

# 字符偏移计算
char = 'A'
offset = 3
new_char = chr(ord(char) + offset)
print(new_char)  # 输出: D

# 凯撒密码示例
def caesar_encode(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

print(caesar_encode("ABC", 3))  # 输出: DEF
print(caesar_encode("XYZ", 3)) # 输出: ABC
```


**运行结果预期:**


```
A
65
D
DEF
ABC
```


`ord()` 和 `chr()` 配合可以用于字符编码转换、密码学等场景。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python3 os.path() 模块](https://www.runoob.com/python3-os-path.html)
			[Python3 chr() 函数](https://www.runoob.com/python3-func-chr-html.html) **













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
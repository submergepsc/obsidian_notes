# Python chr() 函数

- Source: https://www.runoob.com/python3/python3-func-chr.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`chr()` 是 Python 中用于将整数转换为对应字符的内置函数。


`chr()` 接收一个 Unicode 码点（整数），返回对应的字符。它是 `ord()` 的逆函数。


**单词释义**： `chr` 是 `character`（字符）的缩写。


---


## 基本语法与参数


### 语法格式


```
chr(i)
```


### 参数说明


- **参数 i**： 类型： 整数（Unicode 码点，0 到 1,114,111）
- 描述： 要转换为字符的 Unicode 码点。


### 函数说明


- **返回值**： 返回一个长度为 1 的字符串，即对应的字符。
- **范围**： 有效的 Unicode 码点范围是 0 到 1,114,111（0x10FFFF）。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 基本英文字符
print(chr(65))   # 输出: A
print(chr(90))   # 输出: Z
print(chr(97))   # 输出: a
print(chr(122))  # 输出: z

# 数字字符
print(chr(48))   # 输出: 0
print(chr(57))   # 输出: 9

# 常见符号
print(chr(33))   # 输出: !
print(chr(64))   # 输出: @
print(chr(32))   # 输出: 空格

# 中文
print(chr(20013))  # 输出: 中
print(chr(25991))  # 输出: 文
```


**运行结果预期:**


```
A
Z
a
z
0
9
!
@

中
文
```


**代码解析:**


- 65-90 是大写字母 A-Z 的 Unicode 码点。
- 97-122 是小写字母 a-z 的 Unicode 码点。
- 48-57 是数字 0-9 的 Unicode 码点。


### 示例 2：与 ord() 配合使用


## 实例


```python
# ord() 是 chr() 的逆函数
print(ord('A'))    # 输出: 65
print(chr(65))     # 输出: A
print(chr(ord('A') + 1))  # 输出: B

# 遍历大写字母
for i in range(65, 91):
    print(chr(i), end=" ")
print()  # 输出: A B C ... Z

# 生成字符画
pattern = []
for i in range(0, 256, 16):
    row = ''.join(chr(j) for j in range(i, min(i+16, 256)))
    pattern.append(row)
print(pattern[0])  # 输出:  !"#$%&'()*+,-./
```


**运行结果预期:**


```
65
A
B
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
 !"#$%&'()*+,-./
```


`chr()` 和 `ord()` 是互逆的函数，常一起使用处理字符编码。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python3 ord() 函数](https://www.runoob.com/python3-func-ord.html)
			[Python3 hex() 函数](https://www.runoob.com/python3-func-hex.html) **













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
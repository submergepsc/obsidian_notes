# Python hex() 函数

- Source: https://www.runoob.com/python3/python3-func-hex.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`hex()` 是 Python 中用于将整数转换为十六进制字符串的内置函数。


十六进制（Hexadecimal）是计算机中常用的进制表示方法，数字 0-9 和字母 a-f 表示 10-15。`hex()` 函数常用于调试、颜色代码、内存地址等场景。


**单词释义**： `hex` 是 hexadecimal（十六进制）的缩写。


---


## 基本语法与参数


### 语法格式


```
hex(x)
```


### 参数说明


- **参数 x**： 类型： 整数
- 描述： 要转换为十六进制的整数。


### 函数说明


- **返回值**： 返回一个以 "0x" 开头的十六进制字符串。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 基本转换
print(hex(10))     # 输出: 0xa
print(hex(255))    # 输出: 0xff
print(hex(256))    # 输出: 0x100

# 负数（会显示负号）
print(hex(-10))    # 输出: -0xa
print(hex(-255))   # 输出: -0xff

# 零
print(hex(0))      # 输出: 0x0

# 大数
print(hex(16))     # 输出: 0x10
print(hex(255))    # 输出: 0xff
print(hex(4096))   # 输出: 0x1000
```


**运行结果预期:**


```
0xa
0xff
0x100
-0xa
-0xff
0x0
0x10
0xff
0x1000
```


**代码解析:**


- 返回的字符串以 "0x" 开头，表示十六进制。
- 字母默认使用小写（a-f）。
- 负数会显示负号。


### 示例 2：实际应用


## 实例


```python
# 颜色代码转换
r, g, b = 255, 128, 0
color = f"#{hex(r)[2:]:0>2}{hex(g)[2:]:0>2}{hex(b)[2:]:0>2}"
print(color)  # 输出: #ff8000

# 使用格式化
print(f"{10:#x}")    # 输出: 0xa
print(f"{255:#x}")   # 输出: 0xff
print(f"{255:x}")   # 输出: ff

# 去除 0x 前缀
s = hex(255)
print(s[2:])         # 输出: ff
print(s.replace("0x", ""))  # 输出: ff
```


**运行结果预期:**


```
#ff8000
0xa
0xff
ff
ff
ff
```


十六进制常用于颜色代码、调试输出等场景。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python3 chr() 函数](https://www.runoob.com/python3-func-chr-html.html)
			[Python 约瑟夫生者死者小游戏](https://www.runoob.com/python-joseph-life-dead-game.html) **













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
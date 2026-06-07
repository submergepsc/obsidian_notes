# Python oct() 函数

- Source: https://www.runoob.com/python3/python3-func-oct.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`oct()` 是 Python 中用于将整数转换为八进制字符串的内置函数。


八进制（Octal）是计算机中常用的进制表示方法，数字 0-7 表示值。`oct()` 函数返回以 "0o" 开头的八进制字符串。


**单词释义**： `oct` 是 octal（八进制）的缩写。


---


## 基本语法与参数


### 语法格式


```
oct(x)
```


### 参数说明


- **参数 x**： 类型： 整数
- 描述： 要转换为八进制的整数。


### 函数说明


- **返回值**： 返回一个以 "0o" 开头的八进制字符串。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 基本转换
print(oct(8))      # 输出: 0o10
print(oct(9))      # 输出: 0o11
print(oct(64))     # 输出: 0o100
print(oct(255))    # 输出: 0o377

# 负数
print(oct(-8))     # 输出: -0o10

# 零
print(oct(0))      # 输出: 0o0

# 1-7
for i in range(1, 8):
    print(f"{i} -> {oct(i)}")
# 输出: 1 -> 0o1, 2 -> 0o2, ..., 7 -> 0o7
```


**运行结果预期:**


```
0o10
0o11
0o100
0o377
-0o10
0o0
1 -> 0o1
2 -> 0o2
3 -> 0o3
4 -> 0o4
5 -> 0o5
6 -> 0o6
7 -> 0o7
```


**代码解析:**


- 返回的字符串以 "0o" 开头（小写字母 o），表示八进制。
- 八进制每位可以表示 0-7 八个值。


### 示例 2：与十六进制、二进制对比


## 实例


```python
n = 64

# 不同进制表示
print(f"十进制: {n}")
print(f"二进制: {bin(n)}")
print(f"八进制: {oct(n)}")
print(f"十六进制: {hex(n)}")

# 去除前缀
print(f"八进制(无前缀): {oct(n)[2:]}")
print(f"十六进制(无前缀): {hex(n)[2:]}")
```


**运行结果预期:**


```
十进制: 64
二进制: 0b1000000
八进制: 0o100
十六进制: 0x40
```


Python 提供了 `bin()`、`oct()`、`hex()` 三个函数来转换不同进制。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python3 os.pardir 方法](https://www.runoob.com/python3-os-pardir.html)
			[Python3 map() 函数](https://www.runoob.com/python3-func-map.html) **













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
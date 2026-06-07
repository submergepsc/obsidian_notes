# Python bin() 函数

- Source: https://www.runoob.com/python3/python3-func-bin.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`bin()` 是 Python 中用于将整数转换为二进制字符串的内置函数。


二进制（Binary）是计算机中最基本的进制表示方法，只有 0 和 1 两个数字。`bin()` 函数返回以 "0b" 开头的二进制字符串。


**单词释义**： `bin` 是 binary（二进制）的缩写。


---


## 基本语法与参数


### 语法格式


```
bin(x)
```


### 参数说明


- **参数 x**： 类型： 整数
- 描述： 要转换为二进制的整数。


### 函数说明


- **返回值**： 返回一个以 "0b" 开头的二进制字符串。


---


## 实例


### 示例 1：基础用法


## 实例


```python
# 基本转换
print(bin(0))      # 输出: 0b0
print(bin(1))      # 输出: 0b1
print(bin(2))      # 输出: 0b10
print(bin(8))      # 输出: 0b1000
print(bin(255))    # 输出: 0b11111111

# 负数
print(bin(-5))     # 输出: -0b101

# 常见数的二进制
print(bin(10))     # 输出: 0b1010
print(bin(16))     # 输出: 0b10000
print(bin(100))    # 输出: 0b1100100
```


**运行结果预期:**


```
0b0
0b1
0b10
0b1000
0b11111111
-0b101
0b1010
0b10000
0b1100100
```


**代码解析:**


- 返回的字符串以 "0b" 开头，表示二进制。
- 负数会显示负号。


### 示例 2：实际应用


## 实例


```python
# 去除前缀
n = 42
print(bin(n)[2:])   # 输出: 101010

# 使用格式化
print(f"{n:b}")     # 输出: 101010

# 二进制运算
a = 0b1010  # 10
b = 0b0101  # 5
print(f"a & b = {bin(a & b)}")  # 输出: a & b = 0b0
print(f"a | b = {bin(a | b)}")  # 输出: a | b = 0b1111
print(f"a ^ b = {bin(a ^ b)}")  # 输出: a ^ b = 0b1111

# 检查位
n = 8  # 0b1000
if n & 8:
    print("第4位是1")  # 输出: 第4位是1
```


**运行结果预期:**


101010 101010 a & b = 0b0 a & b = 0b1111 a ^ b = 0b1111 第4位是1


二进制常用于位运算、权限控制、算法优化等场景。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python complex() 函数](https://www.runoob.com/python3-func-complex.html)
			[Python bool() 函数](https://www.runoob.com/python3-func-bool.html) **













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
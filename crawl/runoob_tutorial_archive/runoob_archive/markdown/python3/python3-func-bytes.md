# Python bytes() 函数

- Source: https://www.runoob.com/python3/python3-func-bytes.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`bytes()` 是 Python 中用于创建不可变字节序列的内置函数。


字节序列（bytes）是 Python 中用于处理二进制数据的基本类型，常用于文件读写、网络传输、图像处理等场景。bytes 是不可变的，创建后不能修改。


**单词释义**： `bytes` 意为"字节"，是 Python 中的二进制数据类型。


---


## 基本语法与参数


### 语法格式


```
bytes(source)
bytes(source, encoding)
bytes(source, encoding, errors)
```


### 参数说明


- **参数 source**： 类型： 整数、可迭代对象、字符串
- 描述： 用于初始化字节序列的源数据。


**参数 encoding**（可选）：
- 类型： 字符串
- 描述： 字符串的编码格式（如 'utf-8'）。


**参数 errors**（可选）：
- 类型： 字符串
- 描述： 编码错误处理方式。


### 函数说明


- **返回值**： 返回一个不可变的 bytes 对象。
- **特点**： bytes 中的每个元素是 0-255 的整数。


---


## 实例


### 示例 1：创建 bytes


## 实例


```python
# 创建指定长度的 bytes
b = bytes(5)
print(b)           # 输出: b'\x00\x00\x00\x00\x00'

# 从可迭代对象创建
b = bytes([72, 101, 108, 108, 111])
print(b)           # 输出: b'Hello'

# 从字符串创建（需要编码）
b = bytes("你好", encoding='utf-8')
print(b)          # 输出: b'\xe4\xbd\xa0\xe5\xa5\xbd'

# 使用字面量
b = b"Hello"
print(b)          # 输出: b'Hello'
```


**运行结果预期:**


```
b'\x00\x00\x00\x00\x00'
b'Hello'
b'\xe4\xbd\xa0\xe5\xa5\xbd'
b'Hello'
```


**代码解析:**


- bytes(5) 创建 5 个零字节。
- 可迭代对象的元素必须是 0-255 的整数。
- 字符串转换需要指定编码格式。


### 示例 2：bytes 操作


## 实例


```python
# 访问字节
b = b"Hello"
print(b[0])       # 输出: 72
print(b[1])       # 输出: 101

# 切片
print(b[1:4])     # b'ell'

# 遍历
for byte in b"ABC":
    print(byte, end=" ")
print()  # 输出: 65 66 67

# 转换回字符串
b = b"Hello"
s = b.decode('utf-8')
print(s)  # 输出: Hello

# bytes 是不可变的
# b[0] = 65  # 这会抛出 TypeError
```


**运行结果预期:**


```
72
101
b'ell'
65 66 67
Hello
```


bytes 支持索引、切片、遍历等操作，但不能修改元素。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python3 exec 函数](https://www.runoob.com/python3-func-exec.html)
			[Python3 tuple 函数](https://www.runoob.com/python3-func-tuple.html) **













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
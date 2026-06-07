# Python bytearray() 函数

- Source: https://www.runoob.com/python3/python3-func-bytearray.html

[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---


`bytearray()` 是 Python 中用于创建可变字节序列的内置函数。


bytearray 与 bytes 非常相似，但有一个关键区别：bytearray 是可变的，可以随时修改其中的字节。这使得它在需要频繁修改二进制数据的场景中非常有用。


**单词释义**： `bytearray` 意为"字节数组"，是可变的字节序列。


---


## 基本语法与参数


### 语法格式


```
bytearray(source)
bytearray(source, encoding)
bytearray(source, encoding, errors)
```


### 参数说明


- **参数 source**： 类型： 整数、可迭代对象、字符串
- 描述： 用于初始化字节数组的源数据。


### 函数说明


- **返回值**： 返回一个可变的 bytearray 对象。
- **特点**： 可以修改其中的字节元素。


---


## 实例


### 示例 1：创建 bytearray


## 实例


```python
# 创建指定长度的 bytearray
b = bytearray(5)
print(b)           # 输出: bytearray(b'\x00\x00\x00\x00\x00')

# 从可迭代对象创建
b = bytearray([72, 101, 108, 108, 111])
print(b)           # 输出: bytearray(b'Hello')

# 从字符串创建
b = bytearray("你好", encoding='utf-8')
print(b)          # 输出: bytearray(b'\xe4\xbd\xa0\xe5\xa5\xbd')

# 空 bytearray
b = bytearray()
print(b)          # 输出: bytearray(b'')
```


**运行结果预期:**


```
bytearray(b'\x00\x00\x00\x00\x00')
bytearray(b'Hello')
bytearray(b'\xe4\xbd\xa0\xe5\xa5\xbd')
bytearray(b'')
```


**代码解析:**


- 创建方式与 bytes 类似。
- bytearray 可以通过多种方式初始化。


### 示例 2：修改 bytearray


## 实例


```python
# bytearray 是可变的
b = bytearray("Hello", encoding='utf-8')
print(b)          # 输出: bytearray(b'Hello')

# 修改单个字节
b[0] = 74  # 'J' 的 ASCII 码
print(b)          # 输出: bytearray(b'Jello')

# 追加字节
b.append(33)  # '!' 的 ASCII 码
print(b)          # 输出: bytearray(b'Jello!')

# 扩展
b.extend([33, 33])
print(b)          # 输出: bytearray(b'Jello!!!')

# 删除
del b[0]
print(b)          # 输出: bytearray(b'ello!!!')
```


**运行结果预期:**


```
bytearray(b'Hello')
bytearray(b'Jello')
bytearray(b'Jello!')
bytearray(b'Jello!!!')
bytearray(b'ello!!!')
```


bytearray 支持丰富的修改操作：索引赋值、append、extend、del 等。


---


[![Python3 内置函数](https://www.runoob.com/images/up.gif) Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html)

---








	  AI 思考中...





			** [Python bool() 函数](https://www.runoob.com/python3-func-bool.html)
			[Python dict() 函数](https://www.runoob.com/python3-func-dict.html) **













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
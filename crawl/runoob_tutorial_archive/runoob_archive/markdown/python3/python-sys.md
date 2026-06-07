# Python sys 模块

- Source: https://www.runoob.com/python3/python-sys.html

`sys` 是 Python 标准库中的一个模块，提供了与 Python 解释器及其环境交互的功能。

通过 `sys` 库，你可以访问与 Python 解释器相关的变量和函数，例如命令行参数、标准输入输出、程序退出等。


### 导入 sys 库


在使用 `sys` 库之前，你需要先导入它。导入方式如下：


```
import sys
```


## 实例


```python
import sys

# 列出 os 模块的所有属性和方法
print(dir(os))
```


---


## sys 库的常用功能


### 1. 命令行参数


`sys.argv` 是一个包含命令行参数的列表。`sys.argv[0]` 是脚本的名称，后续元素是传递给脚本的参数。


**示例代码：**


## 实例


```python
import sys

print("脚本名称:", sys.argv[0])
print("参数列表:", sys.argv[1:])
```


**运行方式：**


```
python script.py arg1 arg2
```


**输出结果：**


```
脚本名称: script.py
参数列表: ['arg1', 'arg2']
```


### 2. 程序退出


`sys.exit()` 用于退出程序。你可以传递一个整数作为退出状态码，通常 `0` 表示成功，非零值表示错误。


**示例代码：**


## 实例


```python
import sys

print("程序开始")
sys.exit(0)
print("这行代码不会执行")
```


### 3. 标准输入输出


`sys.stdin`、`sys.stdout` 和 `sys.stderr` 分别代表标准输入、标准输出和标准错误流。你可以重定向这些流以实现自定义的输入输出行为。


**示例代码：**


## 实例


```python
import sys

# 重定向标准输出到文件
with open('output.txt', 'w') as f:
    sys.stdout = f
    print("这行内容将写入 output.txt")

# 恢复标准输出
sys.stdout = sys.__stdout__
print("这行内容将显示在控制台")
```


### 4. Python 版本信息


`sys.version` 和 `sys.version_info` 提供了当前 Python 解释器的版本信息。


**示例代码：**


## 实例


```python
import sys

print("Python 版本:", sys.version)
print("版本信息:", sys.version_info)
```


**输出结果：**


```
<code>Python 版本: 3.9.7 (default, Aug 31 2021, 13:28:12)
[GCC 7.5.0]
版本信息: sys.version_info(major=3, minor=9, micro=7, releaselevel=&#39;final&#39;, serial=0)
</code>
```


### 5. 模块搜索路径


`sys.path` 是一个列表，包含了 Python 解释器在导入模块时搜索的路径。你可以修改这个列表来添加自定义的模块搜索路径。


**示例代码：**


## 实例


```python
import sys

print("模块搜索路径:", sys.path)
sys.path.append('/custom/path')
print("更新后的模块搜索路径:", sys.path)
```


---


## sys 模块常用属性

| 属性 | 说明 |
| --- | --- |
| sys.argv | 命令行参数列表，sys.argv[0] 是脚本名称 |
| sys.path | Python 模块搜索路径（PYTHONPATH） |
| sys.modules | 已加载模块的字典 |
| sys.platform | 操作系统平台标识（如 'win32', 'linux', 'darwin'） |
| sys.version | Python 解释器版本信息 |
| sys.executable | Python 解释器的绝对路径 |
| sys.stdin | 标准输入流（文件对象） |
| sys.stdout | 标准输出流（文件对象） |
| sys.stderr | 标准错误流（文件对象） |
| sys.byteorder | 字节序（'little' 或 'big'） |
| sys.maxsize | 最大整数值（2**31-1 或 2**63-1） |


---


## sys 模块常用方法


| 方法 | 说明 |
| --- | --- |
| sys.exit([status]) | 退出程序，status=0 表示正常退出 |
| sys.getsizeof(obj) | 返回对象占用的内存字节数 |
| sys.getdefaultencoding() | 获取默认字符串编码（通常 'utf-8'） |
| sys.setrecursionlimit(limit) | 设置递归深度限制（默认 1000） |
| sys.getrecursionlimit() | 获取当前递归深度限制 |
| sys.getrefcount(obj) | 返回对象的引用计数 |
| sys.exc_info() | 获取当前异常信息（(type, value, traceback)） |
| sys.settrace(tracefunc) | 设置调试跟踪函数 |
| sys.setprofile(profilefunc) | 设置性能分析函数 |








	  AI 思考中...





			** [Python Markdown 生成 HTML](https://www.runoob.com/python-markdown2html.html)
			[Python Pickle 模块](https://www.runoob.com/python-pickle.html) **













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
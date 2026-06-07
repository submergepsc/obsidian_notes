# Python3 reload() 函数

- Source: https://www.runoob.com/python3/python3-func-reload.html

[![Python 内置函数](https://www.runoob.com/images/up.gif) Python 内置函数](https://www.runoob.com/python3-built-in-functions.html)


---


## 描述


**reload()** 用于重新载入之前载入的模块。


**
在 Python2.x 版本中 reload()** 是内置函数，可以直接使用，参见 [Python2.x reload() 函数](https://www.runoob.com/../python/python-func-reload.html)。在 **Python2.x ~ Python3.3** 版本移到 **imp** 包中(Python2.x 也可以导入 imp 包使用)，Python3.4 之后到版本移到了 **importlib** 包中。


## 语法


**Python2.x ~ Python3.3 之前版本：**


```
import imp
imp.reload(module)
```


或


```
from imp import reload
reload(module)
```


**Python3.4 之后到版本**：


```
import importlib
importlib.reload(module)
```


或


```
from importlib import reload
reload(module)
```


## 参数


- module -- 模块对象。


## 返回值


返回模块对象。


## 实例


以下实例展示了 reload() 的使用方法。


### 实例 1


## 重新载入 sys 模块


```python
>>> import sys, importlib
>>> importlib.reload(sys)
<module 'sys' (built-in)>
```


### 实例 2


首先我们在当前目录下创建一个 runoob.py :


## runoob.py 文件


```python
# runoob.py 文件测试代码
site = "RUNOOB"
```


在当前目录下启动 Python 交互式命令窗口：


## 实例


```python
>>>import runoob
>>> runoob.site
'RUNOOB'
```


然后在另外一个窗口编辑 runoob.py 文件（不要关闭以上的 Python 交互式命令窗口），修改为以下代码：


## 修改后的 runoob.py 文件


```python
# runoob.py 文件测试代码
site = "GOOGLE"
```


然后回到 Python 交互式命令窗口：


## 实例


```python
>>> runoob.site    # 输出结果没有变化
'RUNOOB'
>>> from importlib import reload  # Python 3.4+
>>> reload(runoob)    # 重新载入修改后的 runoob.py 文件
<module 'runoob' from '/Users/RUNOOB/runoob-test/runoob.py'>
>>> runoob.site    # 输出结果正常了
'GOOGLE'
```


[![Python 内置函数](https://www.runoob.com/images/up.gif) Python 内置函数](https://www.runoob.com/python3-built-in-functions.html)










	  AI 思考中...





			** [Python 推导式](https://www.runoob.com/python-comprehensions.html)
			[Python 简单的银行系统](https://www.runoob.com/python-bank-system.html) **













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
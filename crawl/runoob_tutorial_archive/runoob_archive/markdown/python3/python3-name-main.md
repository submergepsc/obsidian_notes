# Python __name__ 与 __main__

- Source: https://www.runoob.com/python3/python3-name-main.html

平时我们经常会看到这样的 Python 代码：


```
if __name__ == "__main__":
    main()
```


在 Python 中，**__name__** 和 **__main__** 是两个与模块和脚本执行相关的特殊变量。

**__name__** 和 **__main_**_ 通常用于控制代码的执行方式，尤其是在模块既可以作为独立脚本运行，也可以被其他模块导入时。


### 1. __name__ 变量

**__name__ **是一个内置变量，用于表示当前模块的名称。


**__name__ ** 的值取决于模块是如何被使用的：


当模块作为主程序运行时：**__name__** 的值被设置为 **"__main__"**。


当模块被导入时：**__name__** 的值被设置为模块的文件名（不包括 **.py** 扩展名）。


假设有一个 module.py 文件：


```
print(f"模块的 __name__ 值: {__name__}")
```


输出会是：


```
模块的 __name__ 值: __main__
```


### 2. __main__ 的含义

**__main__** 是一个特殊的字符串，用于表示当前模块是作为主程序运行的。


**__main__** 通常与 __name__ 变量一起使用，以确定模块是被导入还是作为独立脚本运行。


### 3. 使用 if __name__ == "__main__": 的常见模式


在 Python 中，常见的做法是在模块的末尾添加以下代码块：


## 实例


```python
if __name__ == "__main__":
    # 这里的代码只有在模块作为主程序运行时才会执行
    main()
```


这种模式允许模块在被导入时不会执行某些代码，而只有在作为独立脚本运行时才会执行这些代码。

---


## 实例

假设我们有一个名为 example.py 的模块：


## example.py 文件模块：


```python
def greet():
    print("来自 example 模块的问候！")

if __name__ == "__main__":
    print("该脚本正在直接运行。")
    greet()
else:
    print("该脚本作为模块被导入。")
```


### 直接运行 example.py

如果你直接运行 example.py，输出将是：


```
该脚本正在直接运行。
来自 example 模块的问候！
```


在这种情况下，**__name__** 的值是 "__main__"，所以 **if __name__ == "__main__"**: 块中的代码会被执行。


### 导入 example.py

如果你在另一个脚本中导入 example.py，例如：


## 实例


```python
# another_script.py

import example

example.greet()
```


输出将是：


```
该脚本作为模块被导入。
来自 example 模块的问候！
```


在这种情况下，**__name__** 的值是 **"example"（模块名）**，所以 **if __name__ == "__main__":** 块中的代码不会被执行。


### 总结


- `__name__` 是一个内置变量，表示当前模块的名称。
- 当模块作为主程序运行时，`__name__` 的值是 `"__main__"`。
- 当模块被导入时，`__name__` 的值是模块的文件名。
- 使用 `if __name__ == "__main__":` 可以控制模块在被导入时不会执行某些代码，而只有在作为独立脚本运行时才会执行这些代码。








	  AI 思考中...





			** [Python 统计一个字符串中的元音字母数量](https://www.runoob.com/python-vowel-count.html)
			[Python Markdown 生成 HTML](https://www.runoob.com/python-markdown2html.html) **













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
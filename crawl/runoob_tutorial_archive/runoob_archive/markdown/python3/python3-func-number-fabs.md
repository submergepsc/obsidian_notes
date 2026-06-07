# Python3 fabs() 函数

- Source: https://www.runoob.com/python3/python3-func-number-fabs.html

[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)


---


## 描述


fabs() 方法以浮点数形式返回数字的绝对值，如 math.fabs(-10) 返回10.0。


fabs() 函数类似于 abs() 函数，但是他有两点区别:


- abs() 是内置函数。 fabs() 函数在 math 模块中定义。
- fabs() 函数只对浮点型跟整型数值有效。 abs() 还可以运用在复数中。


---


## 语法


以下是 fabs() 方法的语法:


```
import math

math.fabs( x )
```


**注意：**fabs()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。


---


## 参数


- x -- 数值表达式，可以是整数、浮点数等，函数返回值为 x 的绝对值，即一个非负数。。


---


## 返回值

返回数字的绝对值。

---


## 实例


以下展示了使用 fabs() 方法的实例：


## 实例 1


```python
import math

x = -1.5
y = math.fabs(x)
print(y) # 输出 1.5

x = 10
y = math.fabs(x)
print(y) # 输出 10.0
```


以上实例中，**fabs(-1.5)** 返回了 -1.5 的绝对值 1.5， **fabs(10)** 返回了 10 的绝对值 10.0。注意，返回值总是一个浮点数，即使传入的参数是整数。


以上实例运行后输出结果为：


```
1.5
10.0
```


## 实例 2


```python
#!/usr/bin/python3
import math   # 导入 math 模块

print ("math.fabs(-45.17) : ", math.fabs(-45.17))
print ("math.fabs(100.12) : ", math.fabs(100.12))
print ("math.fabs(100.72) : ", math.fabs(100.72))
print ("math.fabs(math.pi) : ", math.fabs(math.pi))
```


以上实例运行后输出结果为：


```
math.fabs(-45.17) :  45.17
math.fabs(100.12) :  100.12
math.fabs(100.72) :  100.72
math.fabs(math.pi) :  3.141592653589793
```


[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)








	  AI 思考中...





			** [Python3 exp() 函数](https://www.runoob.com/python3-func-number-exp.html)
			[Python3 floor() 函数](https://www.runoob.com/python3-func-number-floor.html) **













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
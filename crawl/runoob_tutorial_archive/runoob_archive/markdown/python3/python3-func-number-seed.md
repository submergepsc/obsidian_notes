# Python3 seed() 函数

- Source: https://www.runoob.com/python3/python3-func-number-seed.html

[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)


---


## 描述


**seed()** 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。

---


## 语法


以下是 seed() 方法的语法:


```
import random

random.seed ( [x] )
```


我们调用 random.random() 生成随机数时，每一次生成的数都是随机的。但是，当我们预先使用 random.seed(x) 设定好种子之后，其中的 x 可以是任意数字，如10，这个时候，先调用它的情况下，使用 random() 生成的随机数将会是同一个。


**注意：**seed()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。


---


## 参数


- x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。


---


## 返回值


本函数没有返回值。


---


## 实例


以下展示了使用 seed(() 方法的实例：


## 实例


```python
#!/usr/bin/python3
import random

random.seed()
print ("使用默认种子生成随机数：", random.random())
print ("使用默认种子生成随机数：", random.random())

random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())
random.seed(10)
print ("使用整数 10 种子生成随机数：", random.random())

random.seed("hello",2)
print ("使用字符串种子生成随机数：", random.random())
```


以上实例运行后输出结果为：


```
使用默认种子生成随机数： 0.7908102856355441
使用默认种子生成随机数： 0.81038961519195
使用整数 10 种子生成随机数： 0.5714025946899135
使用整数 10 种子生成随机数： 0.5714025946899135
使用字符串种子生成随机数： 0.3537754404730722
```


[![Python3 数字](https://www.runoob.com/images/up.gif) Python3 数字](https://www.runoob.com/python3-number.html)








	  AI 思考中...





			** [Python3 random() 函数](https://www.runoob.com/python3-func-number-random.html)
			[Python3 shuffle() 函数](https://www.runoob.com/python3-func-number-shuffle.html) **













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
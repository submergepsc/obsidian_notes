# Python3 rstrip() 方法

- Source: https://www.runoob.com/python3/python3-string-rstrip.html

[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)


---


## 描述


rstrip() 删除 string 字符串末尾的指定字符，默认为空白符，包括空格、换行符、回车符、制表符。


## 语法


rstrip()方法语法：


```
str.rstrip([chars])
```


## 参数


- chars -- 指定删除的字符（默认为空白符）


## 返回值


返回删除 string 字符串末尾的指定字符后生成的新字符串。


## 实例


以下实例展示了 rstrip() 函数的使用方法：


## 实例


```python
#!/usr/bin/python3

random_string = 'this is good    '

# 字符串末尾的空格会被删除
print(random_string.rstrip())

# 'si oo' 不是尾随字符，因此不会删除任何内容
print(random_string.rstrip('si oo'))

# 在 'sid oo' 中 'd oo' 是尾随字符，'ood' 从字符串中删除
print(random_string.rstrip('sid oo'))

# 'm/' 是尾随字符，没有找到 '.' 号的尾随字符, 'm/' 从字符串中删除
website = 'www.runoob.com/'
print(website.rstrip('m/.'))

# 移除逗号(,)、点号(.)、字母 s、q 或 w，这几个都是尾随字符
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)
# 删除尾随字符 *
str = "*****this is string example....wow!!!*****"
print (str.rstrip('*'))
```


以上实例输出结果如下：


```
this is good
this is good
this is g
www.runoob.co
banana
*****this is string example....wow!!!
```


---


[![Python3 字符串](https://www.runoob.com/images/up.gif) Python3 字符串](https://www.runoob.com/python3-string.html)









	  AI 思考中...





			** [Python3 rjust()方法](https://www.runoob.com/python3-string-rjust.html)
			[Python3 split() 方法](https://www.runoob.com/python3-string-split.html) **













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
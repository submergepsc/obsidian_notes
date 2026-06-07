# Python3 字典 get() 方法

- Source: https://www.runoob.com/python3/python3-att-dictionary-get.html

[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)


---


## 描述


Python 字典 **get()** 函数返回指定键的值。


## 语法


get()方法语法：


```
dict.get(key[, value])
```


## 参数


- key -- 字典中要查找的键。
- value -- 可选，如果指定键的值不存在时，返回该默认值。


## 返回值


返回指定键的值，如果键不在字典中返回默认值，如果不指定默认值，则返回 **None**。


## 实例


以下实例展示了 **get()** 函数的使用方法：


## 实例


```python
#!/usr/bin/python

tinydict = {'Name': 'Runoob', 'Age': 27}

print ("Age : ", tinydict.get('Age'))

# 没有设置 Sex，也没有设置默认的值，输出 None
print ("Sex : ", tinydict.get('Sex'))

# 没有设置 Salary，输出默认的值  0.0
print ('Salary: ', tinydict.get('Salary', 0.0))
```


以上实例输出结果为：


```
Age : 27
Sex : None
Salary: 0.0
```


### get() 方法 Vs dict[key] 访问元素区别


**get(key) ** 方法在 key（键）不在字典中时，可以返回默认值 **None** 或者设置的默认值。


**dict[key]** 在 key（键）不在字典中时，会触发 **KeyError** 异常。


## 实例


```python
>>> runoob = {}
>>> print('URL: ', runoob.get('url'))     # 返回 None
URL:  None

>>> print(runoob['url'])     # 触发 KeyError
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'url'
>>>
```


### 嵌套字典使用


**get()** 方法对嵌套字典的使用方法如下：


## 实例


```python
#!/usr/bin/python

tinydict = {'RUNOOB' : {'url' : 'www.runoob.com'}}

res = tinydict.get('RUNOOB', {}).get('url')
# 输出结果
print("RUNOOB url 为 : ", str(res))
```


以上实例输出结果为：


```
RUNOOB url 为 :  www.runoob.com
```


---


[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)








	  AI 思考中...





			** [Python3 字典 fromkeys() 方法](https://www.runoob.com/python3-att-dictionary-fromkeys.html)
			[Python3 字典 in 操作符](https://www.runoob.com/python3-att-dictionary-in-html.html) **













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
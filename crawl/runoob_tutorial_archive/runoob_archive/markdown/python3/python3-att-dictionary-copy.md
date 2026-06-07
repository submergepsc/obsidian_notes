# Python3 字典 copy()方法

- Source: https://www.runoob.com/python3/python3-att-dictionary-copy.html

[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)


---


## 描述


Python 字典 copy() 函数返回一个字典的浅复制。


## 语法


copy()方法语法：


```
dict.copy()
```


## 参数


- NA。


## 返回值


返回一个字典的浅复制。


## 实例


以下实例展示了 copy()函数的使用方法：


## 实例



```python
#!/usr/bin/python3

dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict2 = dict1.copy()
print ("新复制的字典为 : ",dict2)
```


以上实例输出结果为：


```
新复制的字典为 :  {'Age': 7, 'Name': 'Runoob', 'Class': 'First'}
```


---


## 直接赋值和 copy 的区别


可以通过以下实例说明：


## 实例



```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict1 =  {'user':'runoob','num':[1,2,3]}

dict2 = dict1          # 浅拷贝: 引用对象
dict3 = dict1.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用

# 修改 data 数据
dict1['user']='root'
dict1['num'].remove(1)

# 输出结果
print(dict1)
print(dict2)
print(dict3)
```


实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。


```
{'user': 'root', 'num': [2, 3]}
{'user': 'root', 'num': [2, 3]}
{'user': 'runoob', 'num': [2, 3]}
```


### 知识扩展


[Python 直接赋值、浅拷贝和深度拷贝解析](https://www.runoob.com/w3cnote/python-understanding-dict-copy-shallow-or-deep.html)


---


[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)








	  AI 思考中...





			** [Python3 字典 clear()方法](https://www.runoob.com/python3-att-dictionary-clear.html)
			[Python3 字典 fromkeys() 方法](https://www.runoob.com/python3-att-dictionary-fromkeys.html) **













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
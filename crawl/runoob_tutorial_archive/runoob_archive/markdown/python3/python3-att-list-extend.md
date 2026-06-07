# Python3 List extend()方法

- Source: https://www.runoob.com/python3/python3-att-list-extend.html

[![Python3 列表](https://www.runoob.com/images/up.gif) Python3 列表](https://www.runoob.com/python3-list.html)


---


## 描述


extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。


## 语法


extend()方法语法：


```
list.extend(seq)
```


## 参数


- seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。


## 返回值


该方法没有返回值，但会在已存在的列表中添加新的列表内容。


## 实例


以下实例展示了 extend()函数的使用方法：


## 实例


```python
#!/usr/bin/python3

list1 = ['Google', 'Runoob', 'Taobao']
list2=list(range(5)) # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print ("扩展后的列表：", list1)
```


以上实例输出结果如下：


```
扩展后的列表： ['Google', 'Runoob', 'Taobao', 0, 1, 2, 3, 4]
```


不同数据类型：


## 实例


```python
#!/usr/bin/python3

# 语言列表
language = ['French', 'English', 'German']

# 元组
language_tuple = ('Spanish', 'Portuguese')

# 集合
language_set = {'Chinese', 'Japanese'}

# 添加元组元素到列表末尾
language.extend(language_tuple)

print('新列表: ', language)

# 添加集合元素到列表末尾
language.extend(language_set)

print('新列表: ', language)
```


```
新列表:  ['French', 'English', 'German', 'Spanish', 'Portuguese']
新列表:  ['French', 'English', 'German', 'Spanish', 'Portuguese', 'Chinese', 'Japanese']
```


[![Python3 列表](https://www.runoob.com/images/up.gif) Python3 列表](https://www.runoob.com/python3-list.html)








	  AI 思考中...





			** [Python3 List count()方法](https://www.runoob.com/python3-att-list-count.html)
			[Python3 List index()方法](https://www.runoob.com/python3-att-list-index.html) **













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
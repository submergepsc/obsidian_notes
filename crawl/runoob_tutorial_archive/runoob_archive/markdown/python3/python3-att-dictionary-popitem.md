# Python3 字典 popitem() 方法

- Source: https://www.runoob.com/python3/python3-att-dictionary-popitem.html

[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)


---


## 描述


Python 字典 popitem() 方法随机返回并删除字典中的最后一对键和值。


如果字典已经为空，却调用了此方法，就报出 KeyError 异常。


## 语法


popitem()方法语法：


```
popitem()
```


## 参数


- 无


## 返回值


返回最后插入键值对(key, value 形式)，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。


**注意：**在 Python3.7 之前，popitem() 方法删除并返回任意插入字典的键值对。


## 实例


以下实例展示了 popitem() 方法的使用方法：


## 实例


```python
#!/usr/bin/python3

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}

# ('url': 'www.runoob.com') 最后插入会被删除
result = site.popitem()

print('返回值 = ', result)
print('site = ', site)

# 插入新元素
site['nickname'] = 'Runoob'
print('site = ', site)

# 现在 ('nickname', 'Runoob') 是最后插入的元素
result = site.popitem()

print('返回值 = ', result)
print('site = ', site)
```


输出结果为：


```
返回值 =  ('url', 'www.runoob.com')
site =  {'name': '菜鸟教程', 'alexa': 10000}
site =  {'name': '菜鸟教程', 'alexa': 10000, 'nickname': 'Runoob'}
返回值 =  ('nickname', 'Runoob')
site =  {'name': '菜鸟教程', 'alexa': 10000}
```


---


[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)








	  AI 思考中...





			** [Python3 字典 pop() 方法](https://www.runoob.com/python3-att-dictionary-pop.html)
			[Python3 内置函数](https://www.runoob.com/python3-built-in-functions.html) **













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
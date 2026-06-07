# Python3 字典 in 操作符

- Source: https://www.runoob.com/python3/python3-att-dictionary-in.html

[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)


---


## 描述


Python 字典 **in** 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true，否则返回 false。


而 **not in** 操作符刚好相反，如果键在字典 dict 里返回 false，否则返回 true。


## 语法


in 操作符语法：


```
key in dict
```


## 参数


- key -- 要在字典中查找的键。


## 返回值


如果键在字典里返回true，否则返回false。


## 实例


以下实例展示了 in 操作符在字典中的使用方法：


## 实例(Python 3.0+)



```python
#!/usr/bin/python3

thisdict = {'Name': 'Runoob', 'Age': 7}

# 检测键 Age 是否存在
if  'Age' in thisdict:
    print("键 Age 存在")
else :
    print("键 Age 不存在")

# 检测键 Sex 是否存在
if  'Sex' in thisdict:
    print("键 Sex 存在")
else :
    print("键 Sex 不存在")

# not in

# 检测键 Age 是否不存在
if  'Age' not in thisdict:
    print("键 Age 不存在")
else :
    print("键 Age 存在")
```


以上实例输出结果为：


```
键 Age 存在
键 Sex 不存在
键 Age 存在
```


---


[![Python3 字典](https://www.runoob.com/images/up.gif) Python3 字典](https://www.runoob.com/python3-dictionary.html)








	  AI 思考中...





			** [Python3 字典 get() 方法](https://www.runoob.com/python3-att-dictionary-get.html)
			[Python3 字典 items() 方法](https://www.runoob.com/python3-att-dictionary-items.html) **













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
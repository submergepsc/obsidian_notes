# Python3 List index()方法

- Source: https://www.runoob.com/python3/python3-att-list-index.html

[![Python3 列表](https://www.runoob.com/images/up.gif) Python3 列表](https://www.runoob.com/python3-list.html)


---


## 描述


index() 函数用于从列表中找出某个值第一个匹配项的索引位置。


## 语法


index()方法语法：


```
list.index(x[, start[, end]])
```


## 参数


- x-- 查找的对象。
- start-- 可选，查找的起始位置。
- end-- 可选，查找的结束位置。


## 返回值


该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。


## 实例


以下实例展示了 index()函数的使用方法：


## 实例 1


```python
#!/usr/bin/python3

list1 = ['Google', 'Runoob', 'Taobao']
print ('Runoob 索引值为', list1.index('Runoob'))
print ('Taobao 索引值为', list1.index('Taobao'))
```


以上实例输出结果如下：


```
Runoob 索引值为 1
Taobao 索引值为 2
```


## 实例 2


```python
#!/usr/bin/python3

list1 = ['Google', 'Runoob', 'Taobao', 'Facebook', 'QQ']
# 从指定位置开始搜索
print ('Runoob 索引值为', list1.index('Runoob',1))
```


以上实例输出结果如下：


```
Runoob 索引值为 1
```


[![Python3 列表](https://www.runoob.com/images/up.gif) Python3 列表](https://www.runoob.com/python3-list.html)








	  AI 思考中...





			** [Python3 List extend()方法](https://www.runoob.com/python3-att-list-extend.html)
			[Python3 List insert()方法](https://www.runoob.com/python3-att-list-insert.html) **













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
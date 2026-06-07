# Python Set add()方法

- Source: https://www.runoob.com/python3/ref-set-add.html

[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)


---


## 描述


add() 方法用于给集合添加元素，如果添加的元素在集合中已存在，则不执行任何操作。


## 语法


add()方法语法：


```
set.add(elmnt)
```


## 参数


- elmnt -- 必需，要添加的元素。


## 返回值


无。


## 实例


以下实例展示了 add() 方法的使用：


## 实例 1


```python
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
```


输出结果为：


```python
{'apple', 'banana', 'orange', 'cherry'}
```


已存在的元素，则不执行添加操作：


## 实例 2


```python
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)
```


输出结果为：


```python
{'apple', 'banana', 'cherry'}
```


[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)








	  AI 思考中...





			** [Python3 open() 函数](https://www.runoob.com/python3-func-open.html)
			[Python Set clear()方法](https://www.runoob.com/ref-set-clear.html) **













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
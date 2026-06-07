# Python 按字母顺序对列表排序

- Source: https://www.runoob.com/python3/python-sort-list-by-alphabetically.html

[![Document 对象参考手册](https://www.runoob.com/images/up.gif) Python3 实例](https://www.runoob.com/python3-examples.html)


Python 按字母顺序对列表排序，可以使用以下两个方法：


- [sort() 方法](https://www.runoob.com/python3-att-list-sort.html) -- 即直接修改原始列表，不创建新的排序副本，该方法会改变原列表的顺序，不返回新的排序列表。
- [sorted() 函数](https://www.runoob.com/python3-func-sorted.html) -- 创建一个新的已排序列表，不修改原始列表，该函数返回一个新的已排序列表，原列表保持不变。


sort() 方法实例：


## 实例


```python
my_list = ["apple", "banana", "cherry", "date"]
my_list.sort()  # 按字母顺序排序
print(my_list)
```


以上代码执行输出结果如下：


```
['apple', 'banana', 'cherry', 'date']
```


sorted() 函数实例：

## 实例


```python
my_list = ["apple", "banana", "cherry", "date"]
sorted_list = sorted(my_list)  # 创建一个新的已排序列表
print(sorted_list)
```


以上代码执行输出结果如下：


```
['apple', 'banana', 'cherry', 'date']
```


无论你选择哪种方法，都可以按字母顺序对列表进行排序。如果你希望按字母顺序的反向顺序排序（降序），可以在 sort() 方法或 sorted() 函数中传递 **reverse=True** 参数。


sort() 方法：


## 实例


```python
my_list = ["apple", "banana", "cherry", "date"]
my_list.sort(reverse=True)  # 按字母顺序降序排序
print(my_list)
```


sorted() 函数：


## 实例


```python
my_list = ["apple", "banana", "cherry", "date"]
sorted_list = sorted(my_list, reverse=True)  # 创建一个新的已排序列表，按字母顺序降序排序
print(sorted_list)
```


[![Document 对象参考手册](https://www.runoob.com/images/up.gif) Python3 实例](https://www.runoob.com/python3-examples.html)










	  AI 思考中...





			** [Python 删除字符串首尾的空格](https://www.runoob.com/python-trim-whitespace-from-a-string.html)
			[Python lambda（匿名函数）](https://www.runoob.com/python-lambda.html) **













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
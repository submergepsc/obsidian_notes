# Python Set intersection_update() 方法

- Source: https://www.runoob.com/python3/ref-set-intersection_update.html

[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)


---


## 描述


`intersection_update()` 方法用于获取两个或更多集合中都重叠的元素，即计算交集。


`intersection_update()` 方法不同于 `intersection()` 方法，因为 `intersection()` 方法是返回一个新的集合，而 `intersection_update()` 方法是在原始的集合上移除不重叠的元素。


## 语法


intersection_update() 方法语法：


```
set.intersection_update(set1, set2 ... etc)
```


## 参数


- set1 -- 必需，要查找相同元素的集合
- set2 -- 可选，其他要查找相同元素的集合，可以多个，多个使用逗号 , 隔开


## 返回值


无。


## 实例


移除 x 集合中不存在于 y 集合中的元素：


## 实例 1


```python
x = {"apple", "banana", "cherry"}  # y 集合不包含 banana 和 cherry，被移除
y = {"google", "runoob", "apple"}

x.intersection_update(y)

print(x)
```


输出结果为：


```python
{'apple'}
```


计算多个集合的交集：


## 实例 1


```python
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

x.intersection_update(y, z)

print(x)
```


输出结果为：


```python
{'c'}
```


[![Python3 列表](https://www.runoob.com/images/up.gif) Python 集合](https://www.runoob.com/python3-set.html)








	  AI 思考中...





			** [Python Set intersection() 方法](https://www.runoob.com/ref-set-intersection.html)
			[Python Set isdisjoint() 方法](https://www.runoob.com/ref-set-isdisjoint.html) **













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
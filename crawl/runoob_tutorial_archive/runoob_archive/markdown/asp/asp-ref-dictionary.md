# ASP Dictionary 对象

- Source: https://www.runoob.com/asp/asp-ref-dictionary.html

---


Dictionary 对象用于在名称/值对中存储信息。


---


![Examples](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例


[指定的键存在吗？](https://www.runoob.com/try/showasp.php?filename=demo_exists)** 本例演示如何创建一个 Dictionary 对象，然后使用 Exists 方法来检查指定的键是否存在。


[返回一个所有项目的数组](https://www.runoob.com/try/showasp.php?filename=demo_items) 本例演示如何使用 Items 方法来返回一个所有项目的数组。


[返回一个所有键的数组](https://www.runoob.com/try/showasp.php?filename=demo_keys) 本例演示如何使用 Keys 方法来返回一个所有键的数组。


[返回一个项目的值](https://www.runoob.com/try/showasp.php?filename=demo_item) 本例演示如何使用 Item 属性来返回一个项目的值。


[设置一个键](https://www.runoob.com/try/showasp.php?filename=demo_key) 本例演示如何使用 Key 属性来在 Dictionary 对象中设置一个键。


[返回键/项目对的数量](https://www.runoob.com/try/showasp.php?filename=demo_count) 本例演示如何使用 Count 属性来返回键/项目对的数量。


---


## Dictionary 对象


Dictionary 对象用于在名称/值对（等同于键和项目）中存储信息。Dictionary 对象看似比数组更为简单，然而，Dictionary 对象却是更令人满意的处理关联数据的解决方案。


比较 Dictionaries 和数组：


- 键用于识别 Dictionary 对象中的项目
- 您无需调用 ReDim 来改变 Dictionary 对象的尺寸
- 当从 Dictionary 中删除一个项目时，其余的项目会自动上移
- Dictionary 不是多维，而数组是多维
- Dictionary 比数组带有更多的内建函数
- Dictionary 在频繁地访问随机元素时，比数组工作得更好
- Dictionary 在根据它们的内容定位项目时，比数组工作得更好


下面的实例创建了一个 Dictionary 对象，并向对象添加了一些键/项目对，然后取回了键 gr 的项目值：


<%

Dim d

Set d=Server.CreateObject("Scripting.Dictionary")

d.Add "re","Red"

d.Add "gr","Green"

d.Add "bl","Blue"

d.Add "pi","Pink"

Response.Write("The value of key gr is: " & d.Item("gr"))

%>


输出：


The value of key gr is: Green


Dictionary 对象的属性和方法描述如下：


### 属性


| 属性 | 描述 |
| --- | --- |
| CompareMode | 设置或返回用于在 Dictionary 对象中比较键的比较模式。 |
| Count | 返回 Dictionary 对象中键/项目对的数目。 |
| Item | 设置或返回 Dictionary 对象中一个项目的值。 |
| Key | 为 Dictionary 对象中已有的键值设置新的键值。 |


### 方法


| 方法 | 描述 |
| --- | --- |
| Add | 向 Dictionary 对象添加新的键/项目对。 |
| Exists | 返回一个布尔值，这个值指示指定的键是否存在于 Dictionary 对象中。 |
| Items | 返回 Dictionary 对象中所有项目的一个数组。 |
| Keys | 返回 Dictionary 对象中所有键的一个数组。 |
| Remove | 从 Dictionary 对象中删除指定的键/项目对。 |
| RemoveAll | 删除 Dictionary 对象中所有的键/项目对。 |










	  AI 思考中...





			** [ASP Folder 对象](https://www.runoob.com/asp-ref-folder.html)
			[ASP ADO](https://www.runoob.com/asp-ado.html) **













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
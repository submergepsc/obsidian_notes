# 案例研究 - 原型

- Source: https://www.runoob.com/appml/appml-case-prototyping.html

---


此案例研究演示了如何构建一个完整的  互联网应用程序，具有针对数据库中的若干表进行信息列举、编辑和搜索的功能。


---


## 原型


在本章中，我们将为数据库中的每个表建立一个原型模型。


原型是非常便于使用的开发应用程序的起点。


---


## 原型模型


首先，为原型创建一个文件夹。该文件夹命名为 Prototypes。


然后，为数据库中的每个表创建一个原型模型。


使用 SELECT * from 每个表，并保存模型为 XML 文件：


## 模型：Proto_Customers.xml


```
<appml>
<datasource>
  <database>
  <connection>Demo</connection>
  <sql>SELECT * FROM Customers</sql>
  </database>
</datasource>
</appml>
```


**
## 模型：Proto_Suppliers.xml


```
<appml>
<datasource>
  <database>
  <connection>Demo</connection>
  <sql>SELECT * FROM Suppliers</sql>
  </database>
</datasource>
</appml>
```


## 模型：Proto_Products.xml


```
<appml>
<datasource>
  <database>
  <connection>Demo</connection>
  <sql>SELECT * FROM Products</sql>
  </database>
</datasource>
</appml>
```


---


## 原型视图


创建一个原型视图，把它保存为 Demo_Prototype.html，并尝试一下：


## 视图：Demo_Prototype.htm


```
<h1>Customers</h1><div id="List01"></div><script src="appml.js"></script>
	<script>customers=new
	AppML("appml.php","Prototypes/Customers");customers.run("List01");</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=Demo_Prototype)


---


## 现在把所有的合并在一起


最后，通过少量 JavaScript 编码，为所有原型模型创建一个简单的原型页面：


## Demo_Prototype_Views.htm


```
<!DOCTYPE html><html><head><link rel="stylesheet"
	href="appml.css" /></head><body><h1>Demo Applications</h1><button onclick='myOpen("Customers")'>Customers</button><button
	onclick='myOpen("Products")'>Products</button><button
	onclick='myOpen("Suppliers")'>Suppliers</button><button
	onclick='myOpen("Shippers")'>Shippers</button><button
	onclick='myOpen("Categories")'>Categories</button><button
	onclick='myOpen("Employees")'>Employees</button><button
	onclick='myOpen("Orders")'>Orders</button><button
	onclick='myOpen("OrderDetails")'>OrderDetails</button><br><br><div id="Place01"></div><script src="appml.js"></script>
	<script>function myOpen(pname){var app_objapp_obj=new
	AppML("appml.php","Prototypes/" + pname);app_obj.run("Place01");}
	</script></body></html>
```


[显示结果 »](https://www.runoob.com/try/appml/Demo.htm)










	  AI 思考中...





			** [AppML 案例简介](https://www.runoob.com/appml-case-intro.html)
			[AppML 案例模型](https://www.runoob.com/appml-case-models.html) **













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
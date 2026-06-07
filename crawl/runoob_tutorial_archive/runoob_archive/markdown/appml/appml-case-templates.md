# 案例研究 - HTML 模板

- Source: https://www.runoob.com/appml/appml-case-templates.html

---


此案例研究演示了如何构建一个完整的  互联网应用程序，具有针对数据库中的若干表进行信息列举、编辑和搜索的功能。


---


## 添加 HTML 模板


在本章中，我们将演示如何向 HTML 页面添加 HTML 模板。


---


## 列出客户


## HTML - View


```
<h1>Customers</h1><div id="List01"></div><br><table
id="Template01" class="appmltable" style="display:none"><tr>

<th>Customer</th>  <th>City</th>  <th>Country</th></tr>
<tr id="appml_row">  <td>#CustomerName#</td>  <td>#City#</td>

<td>#Country#</td></tr></table> <script src="appml.js"></script>
	<script>var customers
	customers=new AppML("appml.php","Models/Customers");
	customers.run("List01","Template01");</script>
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=App_Customers_List)


---


## 列出客户和客户表单


通过巧妙地使用模板，可以很容易添加  列表对象和  表单之间的链接：


## HTML - View


```
<h1>Customers</h1><div id="Form01"></div><br><div
id="List01"></div><br><table id="Template01" class="appmltable"
style="width:100%;display:none"><tr><th></th><th>Customer</th>
<th>City</th><th>Country</th></tr><tr id="appml_row"><td
style="cursor:pointer" onclick="openForm('#CustomerID#')"><img
src="images/appmlFolder.png"></td><td>#CustomerName#</td><td>#City#</td>
<td>#Country#</td></tr></table> <script
src="appml.js"></script><script>var customers,customerForm;
customers=new AppML("appml.php","Models/Customers");
customers.run("List01","Template01");function openForm(id){
customerForm=new AppML("appml.php","Models/Customers");
customerForm.displayType="form";customerForm.run("Form01","",id);}
</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=App_Customers_Form)


---


## 列出客户和客户订单


通过巧妙地使用模板，可以很容易添加  列表对象和所链接的列表之间的链接：


## HTML - View


```
<h1>Customers</h1><div id="List01"></div><br><div
id="Orders01"></div><br><table id="Template01" class="appmltable"
style="width:100%;display:none"><tr><th>Customer</th>
<th>City</th><th>Country</th><th></th></tr><tr
id="appml_row"><td>#CustomerName#</td><td>#City#</td>
<td>#Country#</td><td><a href=''
onclick='openOrders("#CustomerID#");return false;'>Orders</a></td></tr>
</table> <table id="Template02" class="appmltable"
style="width:100%;display:none"><tr><th>Customer</th>
<th>Date</th><th>Salesperson</th><th>Shipper</th></tr><tr
id="appml_row"><td>#CustomerName#</td><td>#OrderDate#</td>
<td>#Salesperson#</td><td>#ShipperName#</td></tr></table> <script src="appml.js"></script><script>var customers,orders;
customers=new AppML("appml.php","Models/Customers");
customers.run("List01","Template01");function openOrders(id){
orders=new AppML("appml.php","Models/Orders");
orders.setQuery("orders.customerid",id);orders.commands=false;
orders.run("Orders01","Template02");}</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=App_Customers_Orders)


---


## 现在把所有的合并在一起


最后，通过少量代码复制，我们就可以完成项目。


## 客户列表、表单和订单


```
<h1>Customers</h1><div id="List01"><table id="appml_list"
class="appmllist"><tr><th>Customer</th><th>City</th>
<th>Country</th><th></th></tr><tr id="appml_row">
<td>#CustomerName#</td><td>#City#</td><td>#Country#</td><td><a
href='' onclick='openOrders("#CustomerID#");return false;'>Orders</a></td>
</tr></table> </div><div
id="List02"></div><script src="appml.js"></script>
	<script>var Customers,Orders
Customers=new AppML("appml.php","Models/Customers");Customers.run("List01");function openOrders(id){var Orders=new
AppML("appml.php","Models/Orders");Orders.setQuery("orders.customerid",id);
Orders.commands=false;
Orders.run("List02");}</script>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=App_Customers)


在接下来的章节中，您可以看到更多带有完整源代码的应用程序。


---










	  AI 思考中...





			** [AppML 案例模型](https://www.runoob.com/appml-case-models.html)
			[AppML 案例 Employees](https://www.runoob.com/appml-case-employees.html) **













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
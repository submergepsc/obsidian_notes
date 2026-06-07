# Products - 完整的应用程序

- Source: https://www.runoob.com/appml/appml-case-products.html

---


**
|  | Product Name | Category | Supplier |
| --- | --- | --- | --- |
|  | #ProductName# | #CategoryName# | #SupplierName# |


ProductName:*
Supplier:


Category:


Unit:
Price:



## 源代码


## HTML 源代码


```
<html><body><h1>Products</h1>
	<div id="Form01"></div><div id="List01"></div><br><table
	id="Template01" class="appmltable" style="width:100%;display:none"><tr>
	<th></th><th>Product Name</th><th>Category</th><th>Supplier</th>
	</tr><tr id="appml_row"><td style="cursor:pointer"
	onclick="productForm.run('Form01','Template02','#ProductID#')"><img
	src="Images/appmlPlus.png"></td><td>#ProductName#</td>
	<td>#CategoryName#</td><td>#SupplierName#</td></tr></table><div id="Template02" class="appmlform" style="width:100%;display:none">
	<label>ProductName:</label><input id="ProductName">
	<label>Supplier:</label><select id="SupplierID"
	data-appmlapplication="Models/Dropdown_Suppliers"></select>
	<label>Category:</label><select id="CategoryID"
	data-appmlapplication="Models/Dropdown_Categories"></select>
	<label>Unit:</label><input id="Unit"><label>Price:</label><input
	id="Price"></div> <script src="appml.js"></script><script>
	var products,productFormproducts=new
	AppML("appml.php","Models/Products");
	products.run("List01","Template01");productForm=new
	AppML("appml.php","Models/Products");productForm.displayType="form";</script></body></html>
```










	  AI 思考中...





			* [AppML 案例 Customers](https://www.runoob.com/appml-case-customers.html)
			[AppML 未来的应用程序](https://www.runoob.com/appml-webstandards.html) **













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
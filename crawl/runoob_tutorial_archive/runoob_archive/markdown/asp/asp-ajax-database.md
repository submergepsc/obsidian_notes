# AJAX 数据库实例

- Source: https://www.runoob.com/asp/asp-ajax-database.html

---


AJAX 可用来与数据库进行交互式通信。


---


## AJAX 数据库实例


下面的实例将演示网页如何通过 AJAX 从数据库读取信息：


## 实例



Select a customer:
Alfreds Futterkiste
North/South
Wolski Zajazd


**Customer info will be listed here...


---


## 实例解释 - HTML 页面


当用户在上面的下拉列表中选择某位客户时，会执行名为 "showCustomer()" 的函数。该函数由 "onchange" 事件触发：



	<!DOCTYPE html>
<html>

<head>

<script>

function showCustomer(str)

{

if (str=="")

  {

  document.getElementById("txtHint").innerHTML="";

  return;

  }

if (window.XMLHttpRequest)

  {// code for IE7+, Firefox, Chrome, Opera, Safari

  xmlhttp=new XMLHttpRequest();

  }

else

  {// code for IE6, IE5

  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");

  }

xmlhttp.onreadystatechange=function()

  {

  if (xmlhttp.readyState==4 && xmlhttp.status==200)

    {

    document.getElementById("txtHint").innerHTML=xmlhttp.responseText;

    }

  }

xmlhttp.open("GET","getcustomer.asp?q="+str,true);

xmlhttp.send();

}

</script>

</head

<body>


<form>

<select name="customers" onchange="showCustomer(this.value)">

<option value="">Select a customer:</option>

<option value="ALFKI">Alfreds Futterkiste</option>

<option value="NORTS ">North/South</option>

<option value="WOLZA">Wolski Zajazd</option>

</select>

</form>

<br>

<div id="txtHint">Customer info will be listed here...</div>


</body>

</html>


源代码解释：


如果没有选择客户（str.length==0），那么该函数会清空 txtHint 占位符，然后退出该函数。


如果已选择一位客户，则 showCustomer() 函数会执行以下步骤：


- 创建 XMLHttpRequest 对象
- 创建在服务器响应就绪时执行的函数
- 向服务器上的文件发送请求
- 请注意添加到 URL 末端的参数（q）（包含下拉列表的内容）


---


## ASP 文件


上面这段通过 JavaScript 调用的服务器页面是名为 "getcustomer.asp" 的 ASP 文件。


"getcustomer.asp" 中的源代码会运行一次针对数据库的查询，然后在 HTML 表格中返回结果：


<%

response.expires=-1

sql="SELECT * FROM CUSTOMERS WHERE CUSTOMERID="

sql=sql & "'" & request.querystring("q") & "'"


set conn=Server.CreateObject("ADODB.Connection")

conn.Provider="Microsoft.Jet.OLEDB.4.0"

conn.Open(Server.Mappath("/db/northwind.mdb"))

set rs=Server.CreateObject("ADODB.recordset")

rs.Open sql,conn


response.write("<table>")

do until rs.EOF


  for each x in rs.Fields


    response.write("<tr><td><b>" & x.name & "</b></td>")


    response.write("<td>" & x.value & "</td></tr>")


  next


  rs.MoveNext

loop
response.write("</table>")

%>









	  AI 思考中...





			** [ASP – AJAX 与 ASP](https://www.runoob.com/asp-ajax-asp.html)
			[ASP 快速参考](https://www.runoob.com/asp-quickref.html) **













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
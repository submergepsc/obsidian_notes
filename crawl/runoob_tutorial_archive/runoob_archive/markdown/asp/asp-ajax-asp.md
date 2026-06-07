# ASP - AJAX 与 ASP

- Source: https://www.runoob.com/asp/asp-ajax-asp.html

---


AJAX 被用于创建交互性更强的应用程序。


---


## AJAX ASP 实例


下面的实例将演示当用户在输入框中键入字符时，网页如何与 Web 服务器进行通信：


## 实例


**Start typing a name in the input field below:**



First name: *


Suggestions:



**
---


## 实例解释 - HTML 页面


当用户在上面的输入框中键入字符时，会执行 "showHint()" 函数。该函数由 "onkeyup" 事件触发：



	<!DOCTYPE html>
<html>

<head>

<script>

function showHint(str)

{

if (str.length==0)

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

xmlhttp.open("GET","gethint.asp?q="+str,true);

xmlhttp.send();

}

</script>

</head

<body>


<p><b>Start typing a name in the input field below:</b></p>

<form>

First name: <input type="text" onkeyup="showHint(this.value)" size="20">

</form>

<p>Suggestions: <span id="txtHint"></span></p>


</body>

</html>


源代码解释：


如果输入框是空的（str.length==0），该函数会清空 txtHint 占位符的内容，并退出该函数。


如果输入框不是空的，那么 showHint() 会执行以下步骤：


- 创建 XMLHttpRequest 对象
- 创建在服务器响应就绪时执行的函数
- 向服务器上的文件发送请求
- 请注意添加到 URL 末端的参数（q）（包含输入框的内容）


---


## ASP 文件


上面这段通过 JavaScript 调用的服务器页面是名为 "gethint.asp" 的 ASP 文件。


"gethint.asp" 中的源代码会检查姓名数组，然后向浏览器返回对应的姓名：


<%

response.expires=-1

dim a(30)

'Fill up array with names

a(1)="Anna"

a(2)="Brittany"

a(3)="Cinderella"

a(4)="Diana"

a(5)="Eva"

a(6)="Fiona"

a(7)="Gunda"

a(8)="Hege"

a(9)="Inga"

a(10)="Johanna"

a(11)="Kitty"

a(12)="Linda"

a(13)="Nina"

a(14)="Ophelia"

a(15)="Petunia"

a(16)="Amanda"

a(17)="Raquel"

a(18)="Cindy"

a(19)="Doris"

a(20)="Eve"

a(21)="Evita"

a(22)="Sunniva"

a(23)="Tove"

a(24)="Unni"

a(25)="Violet"

a(26)="Liza"

a(27)="Elizabeth"

a(28)="Ellen"

a(29)="Wenche"

a(30)="Vicky"


'get the q parameter from URL

q=ucase(request.querystring("q"))


'lookup all hints from array if length of q>0

if len(q)>0 then


  hint=""


  for i=1 to 30


    if q=ucase(mid(a(i),1,len(q))) then


      if hint="" then


        hint=a(i)


      else


        hint=hint & " , " & a(i)


      end if


    end if


  next

end if


'Output "no suggestion" if no hint were found

'or output the correct values

if hint="" then


  response.write("no suggestion")

else


  response.write(hint)

end if

%>

解释：如果 JavaScript 发送了任何文本（即 strlen($q) > 0），则会发生：


- 查找匹配 JavaScript 发送的字符的姓名
- 如果未找到匹配，则将响应字符串设置为 "no suggestion"
- 如果找到一个或多个匹配姓名，则用所有姓名设置响应字符串
- 把响应发送到 "txtHint" 占位符










	  AI 思考中...





			* [AJAX 简介](https://www.runoob.com/asp-ajax-intro.html)
			[AJAX 数据库](https://www.runoob.com/asp-ajax-database.html) **













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
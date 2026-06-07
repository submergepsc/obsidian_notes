# ASP.NET Razor - C# 循环和数组

- Source: https://www.runoob.com/aspnet/razor-cs-loops.html

---


语句在循环中会被重复执行。


---


## For 循环


如果您需要重复执行相同的语句，您可以设定一个循环。


如果您知道要循环的次数，您可以使用 **for 循环**。这种类型的循环在向上计数或向下计数时特别有用：


## 实例


```csharp
<html><body>@for(var i = 10; i < 21; i++)    {<p>Line @i</p>}</body></html>
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_cs_005)


---


## For Each 循环


如果您使用的是集合或者数组，您会经常用到 for each 循环**。


集合是一组相似的对象，for each 循环可以遍历集合直到完成。


下面的实例中，遍历 ASP.NET Request.ServerVariables 集合。


## 实例


```csharp
<html><body><ul>@foreach (var x in
Request.ServerVariables)    {<li>@x</li>}</ul>
</body></html>
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_cs_006)


---


## While 循环


while 循环**是一个通用的循环。


while 循环以 while 关键字开始，后面紧跟着括号，您可以在括号里规定循环将持续多久，然后是重复执行的代码块。


while 循环通常会设定一个递增或者递减的变量用来计数。


下面的实例中，+= 运算符在每执行一次循环时给变量 i 的值加 1。


## 实例


```csharp
<html><body>@{var i = 0;while (i < 5)
{    i += 1;    <p>Line @i</p>
}}</body></html>
```


**[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_cs_007)


---


## 数组


当您要存储多个相似变量但又不想为每个变量都创建一个独立的变量时，可以使用数组来存储：


## 实例


```csharp
@{string[] members = {"Jani", "Hege", "Kai",
	"Jim"};int i = Array.IndexOf(members, "Kai")+1;int len =
	members.Length;string x = members[2-1];}<html><body><h3>Members</h3>@foreach (var person in
	members){<p>@person</p>}<p>The number of names
	in Members are @len</p><p>The person at
	position 2 is @x</p><p>Kai is now in
	position @i</p></body></html>
```


[运行实例 »](https://www.runoob.com/try/showfile_c.php?filename=try_razor_cs_008)










	  AI 思考中...





			** [ASP.NET Razor C# 变量](https://www.runoob.com/razor-cs-variables.html)
			[ASP.NET Razor C# 逻辑](https://www.runoob.com/razor-cs-logic.html) **













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
# ASP.NET Razor - VB 逻辑条件

- Source: https://www.runoob.com/aspnet/razor-vb-logic.html

---


编程逻辑：根据条件执行代码。


---


## If 条件


VB 允许根据条件执行代码。


使用 **if 语句**来判断条件。根据判断结果，if 语句返回 true 或者 false：


- if 语句开始一个代码块
- 条件写在 if 和 then 之间
- 如果条件为真，if ... then 和 end if 之间的代码被执行


## 实例


```csharp
@CodeDim
	price=50End Code<html><body>@If price>30
	Then    @<p>The price is too high.</p>End
	If</body></html>
```


**[运行实例 »](https://www.runoob.com/try/showfile_vb.php?filename=try_razor_vb_010)


---


## Else 条件


if 语句可以包含 else 条件**。


else 条件定义了当条件为假时被执行的代码。


## 实例


```csharp
@CodeDim
	price=20End Code<html><body>@if price>30 then    @<p>The price is too high.</p>
	Else    @<p>The price is OK.</p>End If </body></htmlV>
```


**[运行实例 »](https://www.runoob.com/try/showfile_vb.php?filename=try_razor_vb_011)


注释：**在上面的实例中，如果第一个条件为真，if 块的代码将会被执行。else 条件覆盖了除 if 条件之外的"其他所有情况"。


---


## ElseIf 条件


多个条件判断可以使用 **elseif 条件**：


## 实例


```csharp
@CodeDim
	price=25End Code<html><body>@If price>=30 Then    @<p>The price is
	high.</p>ElseIf price>20 And price<30
	    @<p>The price is OK.</p>Else
	@<p>The price is low.</p>End If    </body></html>
```


**[运行实例 »](https://www.runoob.com/try/showfile_vb.php?filename=try_razor_vb_012)


在上面的实例中，如果第一个条件为真，if 块的代码将会被执行。


如果第一个条件不为真且第二个条件为真，elseif 块的代码将会被执行。


elseif 条件的数量不受限制。


如果 if 和 elseif 条件都不为真，最后的 else 块（不带条件）覆盖了"其他所有情况"。


---


## Select 条件


select 块**可以用来测试一些单独的条件：


## 实例


```csharp
@CodeDim weekday=DateTime.Now.DayOfWeekDim day=weekday.ToString()Dim message=""End Code<html><body>
	@Select Case dayCase "Monday"    message="This is the first
	weekday."Case "Thursday"    message="Only one day before weekend."
	Case "Friday"    message="Tomorrow is weekend!"Case Else
	message="Today is " & dayEnd Select<p>@message</p></body></html>
```


**[运行实例 »](https://www.runoob.com/try/showfile_vb.php?filename=try_razor_vb_013)


"Select Case" 后面紧跟着测试值（day）。每个单独的测试条件都有一个 case 值和任意数量的代码行。如果测试值与 case 值相匹配，相应的代码行被执行。


select 块有一个默认的情况（Case Else），当所有的指定的情况都不匹配时，它覆盖了"其他所有情况"。










	  AI 思考中...





			** [ASP.NET Razor VB 循环和数组](https://www.runoob.com/razor-vb-loops.html)
			[ASP.NET MVC 简介](https://www.runoob.com/mvc-intro.html) **













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
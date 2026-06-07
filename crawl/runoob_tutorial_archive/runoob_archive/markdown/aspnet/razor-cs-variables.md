# ASP.NET Razor - C# 变量

- Source: https://www.runoob.com/aspnet/razor-cs-variables.html

---


变量是用来存储数据的命名实体。


---


## 变量


变量是用来存储数据的。


一个变量的名称必须以字母字符开头，并且不能包含空格或者保留字符。** 一个变量可以是一个指定的类型，表示它所存储的数据类型。string 变量存储字符串值（"Welcome to RUNOOB.COM"），integer 变量存储数字值（103），date 变量存储日期值，等等。 变量使用 var 关键字声明，或通过使用类型（如果您想声明类型）声明，但是 ASP.NET 通常能自动确定数据类型。


## 实例


```csharp
//
	Using the var keyword:var greeting = "Welcome to RUNOOB.COM";var
	counter = 103;var today = DateTime.Today;// Using data types:
	string greeting = "Welcome to RUNOOB.COM";int counter = 103;DateTime
	today = DateTime.Today;
```


---


## 数据类型


下面列出了常用的数据类型：


| 类型 | 描述 | 实例 |
| --- | --- | --- |
| int | 整数（全数字） | 103, 12, 5168 |
| float | 浮点数 | 3.14, 3.4e38 |
| decimal | 十进制数字（高精度） | 1037.196543 |
| bool | 布尔值 | true, false |
| string | 字符串 | "Hello RUNOOB.COM", "John" |


---


## 运算符


运算符告诉 ASP.NET 在表达式中执行什么样的命令。


C# 语言支持多种运算符。下面列出了常用的运算符：


| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| = | 给一个变量赋值。 | i=6 |
| +-*/ | 加上一个值或者一个变量。减去一个值或者一个变量。乘以一个值或者一个变量。除以一个值或者一个变量。 | i=5+5i=5-5i=5*5i=5/5 |
| +=-= | 变量递增。变量递减。 | i += 1i -= 1 |
| == | 相等。如果值相等则返回 true。 | if (i==10) |
| != | 不等。如果值不等则返回 true。 | if (i!=10) |
| >>= | 小于。大于。小于等于。大于等于。 | if (iif (i>10)if (iif (i>=10) |
| + | 连接字符串（一系列互相关联的事物）。 | "run" + "oob" |
| . | 点号。分隔对象和方法。 | DateTime.Hour |
| () | 圆括号。将值进行分组。 | (i+5) |
| () | 圆括号。传递参数。 | x=Add(i,5) |
| [] | 中括号。访问数组或者集合的值。 | name[3] |
| ! | 非。真/假取反。 | if (!ready) |
| &&\|\| | 逻辑与。逻辑或。 | if (ready && clear)if (ready \|\| clear) |


---


## 转换数据类型


从一种数据类型转换到另一种数据类型，有时候是很有用的。 最常见的例子是将字符串输入转换为另一种类型，如整数或者日期。


一般规则下，都是将用户输入看做字符串处理，即使用户输入了数字。因此数值输入必须被转换成数字，然后才能将其用于计算。


下面列出了常用的转换方法：


| 方法 | 描述 | 实例 |
| --- | --- | --- |
| AsInt()IsInt() | 转换字符串为整数。 | if (myString.IsInt()) {myInt=myString.AsInt();} |
| AsFloat()IsFloat() | 转换字符串为浮点数。 | if (myString.IsFloat()) {myFloat=myString.AsFloat();} |
| AsDecimal()IsDecimal() | 转换字符串为十进制数。 | if (myString.IsDecimal()) {myDec=myString.AsDecimal();} |
| AsDateTime()IsDateTime() | 转换字符串为 ASP.NET DateTime 类型。 | myString="10/10/2012";myDate=myString.AsDateTime(); |
| AsBool()IsBool() | 转换字符串为布尔值。 | myString="True";myBool=myString.AsBool(); |
| ToString() | 转换任何数据类型为字符串。 | myInt=1234;myString=myInt.ToString(); |










	  AI 思考中...





			** [ASP.NET Razor 语法](https://www.runoob.com/razor-syntax.html)
			[ASP.NET Razor C# 循环和数组](https://www.runoob.com/razor-cs-loops.html) **













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
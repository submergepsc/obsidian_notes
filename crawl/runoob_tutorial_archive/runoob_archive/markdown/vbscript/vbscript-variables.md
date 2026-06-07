# VBScript 变量

- Source: https://www.runoob.com/vbscript/vbscript-variables.html

---


变量是存储信息的"容器"。


---


![实例](https://www.runoob.com/images/tryitimg.gif)
## 尝试一下 - 实例（只适用于 IE）


[创建和改变变量](https://www.runoob.com/try/try.php?filename=vbdemo_variable)** 如何创建一个变量，并为它赋值，然后再改变它的值。


[在一段文本中插入变量值](https://www.runoob.com/try/try.php?filename=vbdemo_variable2) 如何在一段文本中插入变量值。


[创建数组](https://www.runoob.com/try/try.php?filename=vbdemo_array) 数组用来存储一系列相关的数据项。本例演示如何创建一个存储名字的数组。


---


## 还记得在学校里学过的代数吗？


还记得在学校里学过的代数吗？x=5，y=6，z=x+y


还记得吗？一个字母（比如 x）可以保存一个值（比如 5)，并且可以使用上面的信息计算出 z 的值是 11。


这些字母称为变量**，变量可用于保存值（x=5）或表达式（z=x+y）。


---


## VBScript 变量


与代数相比，VBScript 变量用于保存值或表达式。


变量可以有一个短的名称，如 x，或一个更具描述性的名称，如 carname。


VBScript 变量名称的规则：


- 必须以字母开头
- 不能包含点号（.）
- 不能超过 255 个字符


在 VBScript 中，所有的变量都与类型 *variant* 相关，可存储不同类型的数据。


---


## 声明（创建）VBScript 变量


在 VBScript 创建变量通常指"声明"变量。


您可以通过 Dim、Public 或 Private 语句声明 VBScript 变量。如下所示：


Dim x**
Dim carname


现在您已经创建了两个变量。变量的名称是 "x" 和 "carname"。


您也可以在脚本中通过使用它的名称来声明变量。如下所示：


carname="Volvo"


现在您又创建了一个变量。变量的名称是 "carname"。然后，这个做法不是一个好习惯，因为您可能会在脚本中拼错变量名，那样可能会在脚本运行时引起奇怪的结果。


如果您拼错变量名，比如 "carname" 变量错拼为 "carnime"，脚本会自动创建一个名为 "carnime" 的新变量。为了防止脚本这样做，您可以使用 Option Explicit 语句。如果您使用这个语句，就必须使用 dim、public 或 private 语句来声明所有的变量。


把 Option Explicit 语句放置于脚本的顶端，如下所示：


Option Explicit

Dim carname

carname=some value


---


## 为变量赋值


您可以为某个变量赋值，如下所示：



carname="Volvo"

x=10


变量名是在表达式的左侧，需要赋给变量的值在表达式的右侧。现在变量 "carname" 的值是 "Volvo"，变量 "x" 的值是 "10"。


---


## 变量的生存期


变量的生存期指的是它可以存在的时长。


当您在一个子程序中声明变量时，变量只能在此程序内进行访问。当退出此程序时，变量也会失效。这样的变量称为本地变量。您可以在不同的子程序中使用名称相同的本地变量，因为每个变量只能在声明它的程序内得到识别。


如果您在子程序以外声明了一个变量，在您的页面上的所有子程序都可以访问它。这类变量的生存期始于它们被声明，止于页面被关闭。


---


## VBScript 数组变量


数组变量用于在一个单一的变量中存储多个值。


在下面的实例中，声明了一个包含 3 个元素的数组：


Dim names(2)


括号内显示的数字是 2。数组的下标以 0 开始，因此该数组包含 3 个元素。这是容量固定的数组。您可以为数组的每个元素分配数据，如下所示：


names(0)="Tove"

names(1)="Jani"

names(2)="Stale"


同样地，通过使用特定数组元素的下标号，您可以取回任何元素的值。如下所示：


mother=names(0)


您可以在一个数组中使用多达 60 个维数。声明多维数组的方法是在括号中用逗号来分隔数字。这里，我们声明了一个包含 5 行 7 列的 2 维数组：


Dim table(4,6)


为二维数组赋值：


## 实例（仅适用于 IE）


```
<html>
<body>
<script type="text/vbscript">
Dim x(2,2)
x(0,0)="Volvo"
x(0,1)="BMW"
x(0,2)="Ford"
x(1,0)="Apple"
x(1,1)="Orange"
x(1,2)="Banana"
x(2,0)="Coke"
x(2,1)="Pepsi"
x(2,2)="Sprite"
for i=0 to 2

document.write("<p>")

for j=0 to 2

document.write(x(i,j) & "<br />")

next

document.write("</p>")
next
</script>
</body>
</html>
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_twodimensionalarray)










	  AI 思考中...





			** [VBScript 用法](https://www.runoob.com/vbscript-howto.html)
			[VBScript 程序](https://www.runoob.com/vbscript-procedures.html) **













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
# JavaScript 语句

- Source: https://www.runoob.com/js/js-statements.html

---


JavaScript 语句向浏览器发出的命令。语句的作用是告诉浏览器该做什么。


---


## JavaScript 语句


JavaScript 语句是发给浏览器的命令。


这些命令的作用是告诉浏览器要做的事情。


下面的 JavaScript 语句向 id="demo" 的 HTML 元素输出文本 "你好 Dolly" ：


## 实例


```javascript
document.getElementById("demo").innerHTML = "你好 Dolly";
```


**[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_statement)


---


## 分号 ;


分号用于分隔 JavaScript 语句。


通常我们在每条可执行的语句结尾添加分号。


使用分号的另一用处是在一行中编写多条语句。


实例:


```javascript
a = 5;
b = 6;
c = a + b;
```


以上实例也可以这么写:


```javascript
a = 5; b = 6; c = a + b;
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_semicolon)


|  | 您也可能看到不带有分号的案例。 在 JavaScript 中，用分号来结束语句是可选的。 |
| --- | --- |


---


## JavaScript 代码


JavaScript 代码是 JavaScript 语句的序列。


浏览器按照编写顺序依次执行每条语句。


本例向网页输出一个标题和两个段落：


## 实例


```javascript
document.getElementById("demo").innerHTML="你好 Dolly";
document.getElementById("myDIV").innerHTML="你最近怎么样?";
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_statements)


---


## JavaScript 代码块


JavaScript 可以分批地组合起来。


代码块以左花括号开始，以右花括号结束。


代码块的作用是一并地执行语句序列。


本例向网页输出一个标题和两个段落：


## 实例


```javascript
function myFunction()
{
    document.getElementById("demo").innerHTML="你好Dolly";
    document.getElementById("myDIV").innerHTML="你最近怎么样?";
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_blocks)


您将在稍后的章节学到更多有关函数的知识。

---


## JavaScript 语句标识符


JavaScript 语句通常以一个 语句标识符** 为开始，并执行该语句。


语句标识符是保留关键字不能作为变量名使用。


下表列出了 JavaScript 语句标识符 (关键字) ：


| 语句 | 描述 |
| --- | --- |
| break | 用于跳出循环。 |
| catch | 语句块，在 try 语句块执行出错时执行 catch 语句块。 |
| continue | 跳过循环中的一个迭代。 |
| do ... while | 执行一个语句块，在条件语句为 true 时继续执行该语句块。 |
| for | 在条件语句为 true 时，可以将代码块执行指定的次数。 |
| for ... in | 用于遍历数组或者对象的属性（对数组或者对象的属性进行循环操作）。 |
| function | 定义一个函数 |
| if ... else | 用于基于不同的条件来执行不同的动作。 |
| return | 返回结果，并退出函数 |
| switch | 用于基于不同的条件来执行不同的动作。 |
| throw | 抛出（生成）错误 。 |
| try | 实现错误处理，与 catch 一同使用。 |
| var | 声明一个变量。 |
| while | 当条件语句为 true 时，执行语句块。 |


---


## 空格


JavaScript 会忽略多余的空格。您可以向脚本添加空格，来提高其可读性。下面的两行代码是等效的：


```
var person="runoob";
var person = "runoob";
```


**
---


## 对代码行进行折行


您可以在文本字符串中使用反斜杠对代码行进行换行。下面的例子会正确地显示：


## 实例


```javascript
document.write("你好 \
世界!");
```


[尝试一下 »](https://www.runoob.com/try/tryit.php?filename=tryjs_statement-dw)


不过，您不能像这样执行：


```
document.write \
("你好世界!");
```


![](https://www.runoob.com/wp-content/uploads/2013/08/145E915E-6317-4F1B-8735-47FB4CA6E501.jpg)


知识点：**JavaScript 是脚本语言，浏览器会在读取代码时，逐行地执行脚本代码。而对于传统编程来说，会在执行前对所有代码进行编译。








	  AI 思考中...





			** [JavaScript 输出](https://www.runoob.com/js-output.html)
			[JavaScript 注释](https://www.runoob.com/js-comments.html) **













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

      : ·[JavaScript 实例](https://www.runoob.com/js-examples.html)

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
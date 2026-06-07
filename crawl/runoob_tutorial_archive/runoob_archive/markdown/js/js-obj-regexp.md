# JavaScript RegExp 对象

- Source: https://www.runoob.com/js/js-obj-regexp.html

---


RegExp：是正则表达式（regular expression）的简写。


---


## 完整 RegExp 对象参考手册


请查看我们的 [JavaScript RegExp 对象的参考手册](https://www.runoob.com/../jsref/jsref-obj-regexp.html)，其中提供了可以与字符串对象一同使用的所有的属性和方法。


这个手册包含的关于每个属性和方法的用法的详细描述和实例。


---


## 什么是 RegExp？


正则表达式描述了字符的模式对象。


当您检索某个文本时，可以使用一种模式来描述要检索的内容。RegExp 就是这种模式。


简单的模式可以是一个单独的字符。


更复杂的模式包括了更多的字符，并可用于解析、格式检查、替换等等。


您可以规定字符串中的检索位置，以及要检索的字符类型，等等。


## 语法


var patt=new RegExp(pattern,modifiers);**

或更简单的方法


var patt=/pattern/modifiers;


- 模式描述了一个表达式模型。
- 修饰符(modifiers)描述了检索是否是全局，区分大小写等。


> 注意：**当使用构造函数创造正则对象时，需要常规的字符转义规则（在前面加反斜杠 \）。比如，以下是等价的：
>
>
>
```
var re = new RegExp("\\w+");
var re = /\w+/;
```


---


## RegExp 修饰符


修饰符用于执行不区分大小写和全文的搜索。


**i** - 修饰符是用来执行不区分大小写的匹配。


**g** - 修饰符是用于执行全文的搜索（而不是在找到第一个就停止查找,而是找到所有的匹配）。


## 实例 1


在字符串中不区分大小写找"runoob"


```javascript
var str = "Visit RUnoob";
var patt1 = /runoob/i;
```


以下**标记**的文本是获得的匹配的表达式：


```javascript
Visit  RUnoob
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_regexp_i)


## 实例 2


全文查找 "is"


```javascript
var str="Is this all there is?";
var patt1=/is/g;
```


以下**标记**的文本是获得的匹配的表达式：


```javascript
Is this all there is?
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_regexp_g)


## 实例 3


全文查找和不区分大小写搜索 "is"


```javascript
var str="Is this all there is?";
var patt1=/is/gi;
```


以下 **标记**的文本是获得的匹配的表达式：


```javascript
Is this all there is?
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjsref_regexp_g_2)


---


## test()


test()方法搜索字符串指定的值，根据结果并返回真或假。


下面的示例是从字符串中搜索字符 "e" ：


## 实例


```javascript
var patt1=new RegExp("e");
document.write(patt1.test("The best things in life are free"));
```


由于该字符串中存在字母 "e"，以上代码的输出将是：


```javascript
true
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_regexp_test)


当使用构造函数创造正则对象时，需要常规的字符转义规则（在前面加反斜杠 \） ## 实例
```javascript
var re = new RegExp("\\w+");
```
 [尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_regexp_test1) --- ## exec() exec() 方法检索字符串中的指定值。返回值是被找到的值。如果没有发现匹配，则返回 null。


下面的示例是从字符串中搜索字符 "e" ：


## 实例 1


```javascript
var patt1=new RegExp("e");
document.write(patt1.exec("The best things in life are free"));
```


由于该字符串中存在字母 "e"，以上代码的输出将是：


```javascript
e
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=tryjs_regexp_exec)








	  AI 思考中...





			** [JavaScript Math（算数）对象](https://www.runoob.com/js-obj-math.html)
			[JavaScript Window](https://www.runoob.com/js-window.html) **













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
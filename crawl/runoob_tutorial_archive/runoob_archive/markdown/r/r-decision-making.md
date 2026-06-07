# R 判断语句

- Source: https://www.runoob.com/r/r-decision-making.html

判断结构要求程序员指定一个或多个要评估或测试的条件，以及条件为真时要执行的语句（必需的）和条件为假时要执行的语句（可选的）。


下面是大多数编程语言中典型的判断结构的一般形式：


![](https://www.runoob.com/wp-content/uploads/2015/12/if.png)


R 语言提供了以下类型的判断语句：


- if 语句
- if...else 语句
- switch 语句


### if 语句


一个 if 语句 由一个布尔表达式后跟一个或多个语句组成。

语法格式如下：


```
if(boolean_expression) {
    // 布尔表达式为真将执行的语句
}
```


如果布尔表达式 boolean_expression 为 ture 执行这里面的代码，如果 为 false 则不执行。


## 实例


```r
x <- 50L
if(is.integer(x)) {
   print("X 是一个整数")
}
```


执行以上代码，输出结果为：


```
[1] "X 是一个整数"
```


### if...else 语句


一个 if 语句 后可跟一个可选的 else 语句，else 语句在布尔表达式为假时执行。


语法格式如下：


```
if(boolean_expression) {
    // 如果布尔表达式为真将执行的语句
} else {
    // 如果布尔表达式为假将执行的语句
}
```


如果布尔表达式 boolean_expression 为 true，则执行 if 块内的代码。如果布尔表达式为 false，则执行 else 块内的代码。


## 实例


```r
x <- c("google","runoob","taobao")

if("runoob" %in% x) {
   print("包含 runoob")
} else {
   print("不包含 runoob")
}
```


执行以上代码，输出结果为：


```
[1] "包含 runoob"
```


如果有多个条件判断，可以使用 if...else if...else：


```
if(boolean_expression 1) {
    // 如果布尔表达式 boolean_expression 1 为真将执行的语句
} else if( boolean_expression 2) {
    // 如果布尔表达式 boolean_expression 2 为真将执行的语句
} else if( boolean_expression 3) {
    // 如果布尔表达式 boolean_expression 3 为真将执行的语句
} else {
    // 以上所有的布尔表达式都为 false 时执行
}
```


## 实例


```r
x <- c("google","runoob","taobao")

if("weibo" %in% x) {
   print("第一个 if 包含 weibo")
} else if ("runoob" %in% x) {
   print("第二个 if 包含 runoob")
} else {
   print("没有找到")
}
```


执行以上代码，输出结果为：


```
[1] "第二个 if 包含 runoob"
```


### switch 语句


一个 switch 语句允许测试一个变量等于多个值时的情况。每个值称为一个 case。

语法格式如下：


```
switch(expression, case1, case2, case3....)
```


**switch** 语句必须遵循下面的规则：


- **switch** 语句中的 **expression** 是一个常量表达式，可以是整数或字符串，如果是整数则返回对应的 case 位置值，如果整数不在位置的范围内则返回 NULL。
- 如果匹配到多个值则返回第一个。
- **expression**如果是字符串，则对应的是 case 中的变量名对应的值，没有匹配则没有返回值。
- switch 没有默认参数可用。

以下实例返回第三个值：


## 实例


```r
x <- switch(
   3,
   "google",
   "runoob",
   "taobao",
   "weibo"
)
print(x)
```


执行以上代码，输出结果为：


```
[1] "taobao"
```


如果是字符串返回字符串变量对应的值：


## 实例


```r
you.like<-"runoob"
switch(you.like, google="www.google.com", runoob = "www.runoob.com", taobao = "www.taobao.com")
```


执行以上代码，输出结果为：


```
[1] "www.runoob.com"
```


如果整数不在范围内的则返回 NULL


## 实例


```r
> x <- switch(4,"google","runoob","taobao")
> x
NULL
> x <- switch(4,"google","runoob","taobao")
> x
NULL
```









	  AI 思考中...





			** [R 数据类型](https://www.runoob.com/r-data-types.html)
			[R 循环](https://www.runoob.com/r-loop.html) **













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
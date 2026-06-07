# Scala IF...ELSE 语句

- Source: https://www.runoob.com/scala/scala-if-else.html

Scala IF...ELSE 语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。

可以通过下图来简单了解条件语句的执行过程:


![](https://www.runoob.com/wp-content/uploads/2015/12/if.png) --- ## if 语句 if 语句有布尔表达式及之后的语句块组成。


### 语法


if 语句的语法格式如下：


```
if(布尔表达式)
{
   // 如果布尔表达式为 true 则执行该语句块
}
```


如果布尔表达式为 true 则执行大括号内的语句块，否则跳过大括号内的语句块，执行大括号之后的语句块。


### 实例


## 实例


```scala
object Test {
   def main(args: Array[String]) {
      var x = 10;

      if( x < 20 ){
         println("x < 20");
      }
   }
}
```

**[运行实例 »](https://www.runoob.com/try/runcode.php?filename=TestIf&type=scala)


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
x < 20
```


---


## if...else 语句


if 语句后可以紧跟 else 语句，else 内的语句块可以在布尔表达式为 false 的时候执行。


### 语法


if...else 的语法格式如下：


```
if(布尔表达式){
   // 如果布尔表达式为 true 则执行该语句块
}else{
   // 如果布尔表达式为 false 则执行该语句块
}
```


### 实例


## 实例


```scala
object Test {
   def main(args: Array[String]) {
      var x = 30;

      if( x < 20 ){
         println("x 小于 20");
      }else{
         println("x 大于等于 20");
      }
   }
}
```


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
x 大于等于 20
```


---


## if...else if...else 语句


if 语句后可以紧跟 else if...else 语句，在多个条件判断语句的情况下很有用。


### 语法


if...else if...else 语法格式如下：


```
if(布尔表达式 1){
   // 如果布尔表达式 1 为 true 则执行该语句块
}else if(布尔表达式 2){
   // 如果布尔表达式 2 为 true 则执行该语句块
}else if(布尔表达式 3){
   // 如果布尔表达式 3 为 true 则执行该语句块
}else {
   // 如果以上条件都为 false 执行该语句块
}
```


### 实例


## 实例


```scala
object Test {
   def main(args: Array[String]) {
      var x = 30;

      if( x == 10 ){
         println("X 的值为 10");
      }else if( x == 20 ){
         println("X 的值为 20");
      }else if( x == 30 ){
         println("X 的值为 30");
      }else{
         println("无法判断 X 的值");
      }
   }
}
```


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
X 的值为 30
```


---


## if...else 嵌套语句


if...else 嵌套语句可以实现在 if 语句内嵌入一个或多个 if 语句。


### 语法


if...else 嵌套语句语法格式如下：


```
if(布尔表达式 1){
   // 如果布尔表达式 1 为 true 则执行该语句块
   if(布尔表达式 2){
      // 如果布尔表达式 2 为 true 则执行该语句块
   }
}
```


else if...else 的嵌套语句 类似 if...else 嵌套语句。


### 实例


## 实例


```scala
object Test {
   def main(args: Array[String]) {
        var x = 30;
        var y = 10;

         if( x == 30 ){
            if( y == 10 ){
            println("X = 30 , Y = 10");
         }
      }
   }
}
```


执行以上代码，输出结果为：


```
$ scalac Test.scala
$ scala Test
X = 30 , Y = 10
```









	  AI 思考中...





			** [Scala 运算符](https://www.runoob.com/scala-operators.html)
			[Scala 循环](https://www.runoob.com/scala-loop-types.html) **













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
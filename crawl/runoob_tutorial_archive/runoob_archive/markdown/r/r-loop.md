# R 循环

- Source: https://www.runoob.com/r/r-loop.html

有的时候，我们可能需要多次执行同一块代码。一般情况下，语句是按顺序执行的：函数中的第一个语句先执行，接着是第二个语句，依此类推。


编程语言提供了更为复杂执行路径的多种控制结构。


循环语句允许我们多次执行一个语句或语句组，下面是大多数编程语言中循环语句的流程图：

![循环结构](https://www.runoob.com/wp-content/uploads/2015/12/loop.png)


R 语言提供的循环类型有:


- repeat 循环
- while 循环
- for 循环


R 语言提供的循环控制语句有：

- break 语句
- Next 语句


循环控制语句改变你代码的执行顺序，通过它你可以实现代码的跳转。


## 循环类型


### repeat


repeat 循环会一直执行代码，直到条件语句为 true 时才退出循环，退出要使用到 break 语句。


语法格式如下：


```
repeat {
    // 相关代码
    if(condition) {
       break
    }
}
```


以下实例在变量 cnt 为 5 时退出循环，cnt 为计数变量：


## 实例


```r
v <- c("Google","Runoob")
cnt <- 2

repeat {
   print(v)
   cnt <- cnt+1

   if(cnt > 5) {
      break
   }
}
```


执行以上代码，输入结果为：


```
[1] "Google" "Runoob"
[1] "Google" "Runoob"
[1] "Google" "Runoob"
[1] "Google" "Runoob"
```


### while


只要给定的条件为 true，R 语言中的 while 循环语句会重复执行一个目标语句。


语法格式如下：


```
while(condition)
{
   statement(s);
}
```


在这里，statement(s) 可以是一个单独的语句，也可以是几个语句组成的代码块。


condition 可以是任意的表达式，当为任意非零值时都为 true。当条件为 true 时执行循环。 当条件为 false 时，退出循环，程序流将继续执行紧接着循环的下一条语句。


以下实例在在变量 cnt 小于 7 时输出 while 语句块中的内容，cnt 为计数变量：


## 实例


```r
v <- c("Google","Runoob")
cnt <- 2

while (cnt < 7) {
   print(v)
   cnt = cnt + 1
}
```


执行以上代码，输入结果为：


```
[1] "Google" "Runoob"
[1] "Google" "Runoob"
[1] "Google" "Runoob"
[1] "Google" "Runoob"
[1] "Google" "Runoob"
```


### for


R 编程语言中 for 循环语句可以重复执行指定语句，重复次数可在 for 语句中控制。


语法格式如下：


```
for (value in vector) {
    statements
}
```


R 语言的 for 循环特别灵活，不仅可以循环整数变量，还可以对字符向量，逻辑向量，列表等数据类型进行迭代。


以下实例输出 26 个字母对前面四个字母：


## 实例


```r
v <- LETTERS[1:4]
for ( i in v) {
   print(i)
}
```


执行以上代码，输入结果为：


```
[1] "A"
[1] "B"
[1] "C"
[1] "D"
```


---


## 循环控制


### break


R 语言的 break 语句插入在循环体中，用于退出当前循环或语句，并开始脚本执行紧接着的语句。

如果你使用循环嵌套，break 语句将停止最内层循环的执行，并开始执行的外层的循环语句。

break 也常用于 switch 语句中。

语法格式如下：


```
break
```


以下实例在变量 cnt 为 5 时使用 break 退出循环，cnt 为计数变量：


## 实例


```r
v <- c("Google","Runoob")
cnt <- 2

repeat {
   print(v)
   cnt <- cnt+1

   if(cnt > 5) {
      break
   }
}
```


执行以上代码，输入结果为：


```
[1] "Google" "Runoob"
[1] "Google" "Runoob"
[1] "Google" "Runoob"
[1] "Google" "Runoob"
```


### next


next 语句用于跳过当前循环，开始下一次循环（类似其他语言的 continue）。


语法格式如下：


```
next
```


以下实例输出 26 个字母的前面 6 个字母，在字母为 D 的时候跳过当前的循环，进行下一次循环：


## 实例


```r
v <- LETTERS[1:6]
for ( i in v) {

   if (i == "D") {  # D 不会输出，跳过这次循环，进入下一次
      next
   }
   print(i)
}
```


执行以上代码，输入结果为：


```
[1] "A"
[1] "B"
[1] "C"
[1] "E"
[1] "F"
```









	  AI 思考中...





			** [R 判断语句](https://www.runoob.com/r-decision-making.html)
			[R 函数](https://www.runoob.com/r-functions.html) **













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
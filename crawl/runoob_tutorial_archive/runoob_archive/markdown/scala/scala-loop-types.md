# Scala 循环

- Source: https://www.runoob.com/scala/scala-loop-types.html

有的时候，我们可能需要多次执行同一块代码。一般情况下，语句是按顺序执行的：函数中的第一个语句先执行，接着是第二个语句，依此类推。

编程语言提供了更为复杂执行路径的多种控制结构。

循环语句允许我们多次执行一个语句或语句组，下面是大多数编程语言中循环语句的流程图：


![循环结构](https://www.runoob.com/wp-content/uploads/2015/12/loop.png)


---


## 循环类型


Scala 语言提供了以下几种循环类型。点击链接查看每个类型的细节。


| 循环类型 | 描述 |
| --- | --- |
| while 循环 | 运行一系列语句，如果条件为true，会重复运行，直到条件变为false。 |
| do...while 循环 | 类似 while 语句区别在于判断循环条件之前，先执行一次循环的代码块。 |
| for 循环 | 用来重复执行一系列语句直到达成特定条件达成，一般通过在每次循环完成后增加计数器的值来实现。 |


---


## 循环控制语句


循环控制语句改变你代码的执行顺序，通过它你可以实现代码的跳转。Scala 以下几种循环控制语句：


Scala 不支持 break 或 continue 语句，但从 2.8 版本后提供了一种中断循环的方式，点击以下链接查看详情。


| 控制语句 | 描述 |
| --- | --- |
| break 语句 | 中断循环 |


---


## 无限循环

如果条件永远为 true，则循环将变成无限循环。我们可以使用 while 语句来实现无限循环：


## 实例


```scala
object Test {
   def main(args: Array[String]) {
      var a = 10;
      // 无限循环
      while( true ){
         println( "a 的值为 : " + a );
      }
   }
}
```


以上代码执行后循环会永久执行下去，你可以使用 Ctrl + C 键来中断无限循环。








	  AI 思考中...





			** [Scala IF…ELSE 语句](https://www.runoob.com/scala-if-else.html)
			[Scala while 循环](https://www.runoob.com/scala-while-loop.html) **













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
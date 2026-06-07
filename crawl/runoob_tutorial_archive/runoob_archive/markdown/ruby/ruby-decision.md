# Ruby 判断

- Source: https://www.runoob.com/ruby/ruby-decision.html

Ruby 提供了几种很常见的条件结构。在这里，我们将解释所有的条件语句和 Ruby 中可用的修饰符。


## Ruby if...else 语句


## 语法


```ruby
if conditional [then]
      code...
[elsif conditional [then]
      code...]...
[else
      code...]
end
```


*if* 表达式用于条件执行。值 *false* 和 *nil* 为假，其他值都为真。请注意，Ruby 使用 elsif，不是使用 else if 和 elif。


如果 *conditional* 为真，则执行 *code*。如果 *conditional* 不为真，则执行 else 子句中指定的 *code*。

通常我们省略保留字 then 。若想在一行内写出完整的 if 式，则必须以 then 隔开条件式和程式区块。如下所示:


```ruby
if a == 4 then a = 7 end
```


## 实例


```ruby
#!/usr/bin/ruby
# -*- coding: UTF-8 -*-

x=1
if x > 2
   puts "x 大于 2"
elsif x <= 2 and x!=0
   puts "x 是 1"
else
   puts "无法得知 x 的值"
end
```


**
[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=if_demo&type=ruby)


以上实例输出结果：


```
x 是 1
```


## Ruby if 修饰符


## 语法


```ruby
code if condition
```


if修饰词组表示当 if 右边之条件成立时才执行 if 左边的式子。即如果 *conditional* 为真，则执行 *code*。


## 实例


```ruby
#!/usr/bin/ruby

$debug=1
print "debug\n" if $debug
```


[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=if_demo2&type=ruby)


以上实例输出结果：


```
debug
```


## Ruby unless 语句


## 语法


```ruby
unless conditional [then]
   code
[else
   code ]
end
```


unless式和 if式作用相反，即如果 *conditional* 为假，则执行 *code*。如果 *conditional* 为真，则执行 else 子句中指定的 *code*。


## 实例


```ruby
#!/usr/bin/ruby
# -*- coding: UTF-8 -*-

x=1
unless x>2
   puts "x 小于或等于 2"
 else
  puts "x 大于 2"
end
```


[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=unless_demo&type=ruby)


以上实例输出结果为：


```
x 小于或等于 2
```


## Ruby unless 修饰符


## 语法


```ruby
code unless conditional
```


如果 *conditional* 为假，则执行 *code*。


## 实例


```ruby
#!/usr/bin/ruby
# -*- coding: UTF-8 -*-

$var =  1
print "1 -- 这一行输出\n" if $var
print "2 -- 这一行不输出\n" unless $var

$var = false
print "3 -- 这一行输出\n" unless $var
```


[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=unless_demo2&type=ruby)


以上实例输出结果：


```
1 -- 这一行输出
3 -- 这一行输出
```


## Ruby case 语句


## 语法


```ruby
case expression
[when expression [, expression ...] [then]
   code ]...
[else
   code ]
end
```


case先对一个 *expression* 进行匹配判断，然后根据匹配结果进行分支选择。


它使用 ===**运算符比较 **when** 指定的 *expression*，若一致的话就执行 **when** 部分的内容。


通常我们省略保留字 then 。若想在一行内写出完整的 when 式，则必须以 then 隔开条件式和程式区块。如下所示:


```ruby
when a == 4 then a = 7 end
```


因此：


```ruby
case expr0
when expr1, expr2
   stmt1
when expr3, expr4
   stmt2
else
   stmt3
end
```


基本上类似于：


```ruby
_tmp = expr0
if expr1 === _tmp || expr2 === _tmp
   stmt1
elsif expr3 === _tmp || expr4 === _tmp
   stmt2
else
   stmt3
end
```


## 实例


```ruby
#!/usr/bin/ruby
# -*- coding: UTF-8 -*-

$age =  5
case $age
when 0 .. 2
    puts "婴儿"
when 3 .. 6
    puts "小孩"
when 7 .. 12
    puts "child"
when 13 .. 18
    puts "少年"
else
    puts "其他年龄段的"
end
```


**
[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=case_demo&type=ruby)


以上实例输出结果为：


```
小孩
```


当case的"表达式"部分被省略时，将计算第一个when条件部分为真的表达式。


```ruby
foo = false
bar = true
quu = false

case
when foo then puts 'foo is true'
when bar then puts 'bar is true'
when quu then puts 'quu is true'
end
# 显示 "bar is true"
```










	  AI 思考中...





			** [Ruby 注释](https://www.runoob.com/ruby-comment.html)
			[Ruby 循环](https://www.runoob.com/ruby-loop.html) **













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
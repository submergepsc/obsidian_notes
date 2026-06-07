# Ruby 块

- Source: https://www.runoob.com/ruby/ruby-block.html

您已经知道 Ruby 如何定义方法以及您如何调用方法。类似地，Ruby 有一个块的概念。


- 块由大量的代码组成。
- 您需要给块取个名称。
- 块中的代码总是包含在大括号 {} 内。
- 块总是从与其具有相同名称的函数调用。这意味着如果您的块名称为 *test*，那么您要使用函数 *test* 来调用这个块。
- 您可以使用 *yield* 语句来调用块。


## 语法


```ruby
block_name{
   statement1
   statement2
   ..........
}
```


在这里，您将学到如何使用一个简单的 *yield* 语句来调用块。您也将学到如何使用带有参数的 *yield* 语句来调用块。在实例中，您将看到这两种类型的 *yield* 语句。


## yield 语句


让我们看一个 yield 语句的实例：


## 实例


```ruby
#!/usr/bin/ruby
# -*- coding: UTF-8 -*-

def test
   puts "在 test 方法内"
   yield
   puts "你又回到了 test 方法内"
   yield
end
test {puts "你在块内"}
```


**
[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=yield_demo&type=ruby)


以上实例运行结果为：


```
在 test 方法内
你在块内
你又回到了 test 方法内
你在块内
```


您也可以传递带有参数的 yield 语句。下面是一个实例：


## 实例


```ruby
#!/usr/bin/ruby
# -*- coding: UTF-8 -*-

def test
   yield 5
   puts "在 test 方法内"
   yield 100
end
test {|i| puts "你在块 #{i} 内"}
```


[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=yield_demo2&type=ruby)


以上实例运行结果为：


```
你在块 5 内
在 test 方法内
你在块 100 内
```


在这里，*yield* 语句后跟着参数。您甚至可以传递多个参数。在块中，您可以在两个竖线之间放置一个变量来接受参数。因此，在上面的代码中，yield 5 语句向 test 块传递值 5 作为参数。


现在，看下面的语句：


```ruby
test {|i| puts "你在块 #{i} 内"}
```


在这里，值 5 会在变量 i 中收到。现在，观察下面的 puts 语句：


```ruby
puts "你在块 #{i} 内"
```


这个 puts 语句的输出是：


```ruby
你在块5 内
```


如果您想要传递多个参数，那么 *yield* 语句如下所示：


```ruby
yield a, b
```


此时，块如下所示：


```ruby
test {|a, b| statement}
```


参数使用逗号分隔。


## 块和方法


您已经看到块和方法之间是如何相互关联的。您通常使用 yield 语句从与其具有相同名称的方法调用块。因此，代码如下所示：


## 实例


```ruby
#!/usr/bin/ruby

def test
  yield
end
test{ puts "Hello world"}
```


本实例是实现块的最简单的方式。您使用 *yield* 语句调用 test 块。


但是如果方法的最后一个参数前带有 &，那么您可以向该方法传递一个块，且这个块可被赋给最后一个参数。如果 * 和 & 同时出现在参数列表中，& 应放在后面。


## 实例


```ruby
#!/usr/bin/ruby

def test(&block)
   block.call
end
test { puts "Hello World!"}
```


[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=yield_demo3&type=ruby)


以上实例运行结果为：


```
Hello World!
```


## BEGIN 和 END 块


每个 Ruby 源文件可以声明当文件被加载时要运行的代码块（BEGIN 块），以及程序完成执行后要运行的代码块（END 块）。


## 实例


```ruby
#!/usr/bin/ruby

BEGIN {
  # BEGIN 代码块
  puts "BEGIN 代码块"
}

END {
  # END 代码块
  puts "END 代码块"
}
  # MAIN 代码块
puts "MAIN 代码块"
```


一个程序可以包含多个 BEGIN 和 END 块。BEGIN 块按照它们出现的顺序执行。END 块按照它们出现的相反顺序执行。当执行时，上面的程序输出以下结果：


```
BEGIN 代码块
MAIN 代码块
END 代码块
```









	  AI 思考中...





			** [Ruby 方法](https://www.runoob.com/ruby-method.html)
			[Ruby 模块（Module）](https://www.runoob.com/ruby-module.html) **













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
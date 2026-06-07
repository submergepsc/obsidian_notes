# Ruby 语法

- Source: https://www.runoob.com/ruby/ruby-syntax.html

让我们编写一个简单的 Ruby 程序。所有的 Ruby 文件扩展名都是 **.rb**。所以，把下面的源代码放在 test.rb 文件中。


## 实例


```ruby
#!/usr/bin/ruby -w

puts "Hello, Ruby!";
```


**[运行实例 »](https://www.runoob.com/try/showrb.php?filename=HelloRuby)


在这里，假设您的 /usr/bin 目录下已经有可用的 Ruby 解释器。现在，尝试运行这个程序，如下所示：


```
$ ruby test.rb
```


这将会产生下面的结果：


```
Hello, Ruby!
```


您已经看到了一个简单的 Ruby 程序，现在让我们看看一些 Ruby 语法相关的基本概念：


## Ruby 程序中的空白


在 Ruby 代码中的空白字符，如空格和制表符一般会被忽略，除非当它们出现在字符串中时才不会被忽略。然而，有时候它们用于解释模棱两可的语句。当启用 -w 选项时，这种解释会产生警告。


实例：**


```
a + b 被解释为 a+b （这是一个局部变量）
a  +b 被解释为 a(+b) （这是一个方法调用）
```


## Ruby 程序中的行尾


Ruby 把分号和换行符解释为语句的结尾。但是，如果 Ruby 在行尾遇到运算符，比如 +、- 或反斜杠，它们表示一个语句的延续。


## Ruby 标识符


标识符是变量、常量和方法的名称。Ruby 标识符是大小写敏感的。这意味着 Ram 和 RAM 在 Ruby 中是两个不同的标识符。


Ruby 标识符的名称可以包含字母、数字和下划线字符（ _ ）。


## 保留字


下表列出了 Ruby 中的保留字。这些保留字不能作为常量或变量的名称。但是，它们可以作为方法名。


| BEGIN | do | next | then |
| --- | --- | --- | --- |
| END | else | nil | true |
| alias | elsif | not | undef |
| and | end | or | unless |
| begin | ensure | redo | until |
| break | false | rescue | when |
| case | for | retry | while |
| class | if | return | yield |
| def | in | self | __FILE__ |
| defined? | module | super | __LINE__ |


## Ruby 中的 Here Document


"Here Document" 是指建立多行字符串。在







	  AI 思考中...





			** [Ruby 环境变量](https://www.runoob.com/ruby-environment-variables.html)
			[Ruby 类和对象](https://www.runoob.com/ruby-class.html) **
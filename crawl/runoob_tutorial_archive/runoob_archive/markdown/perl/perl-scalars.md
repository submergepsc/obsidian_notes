# Perl 标量

- Source: https://www.runoob.com/perl/perl-scalars.html

标量是一个简单的数据单元。


标量可以是一个整数，浮点数，字符，字符串，段落或者一个完整的网页。


以下实例演示了标量的简单应用：


## 实例



```perl
#!/usr/bin/perl

$age = 20;             # 整数赋值
$name = "Runoob";   # 字符串
$salary = 130.50;     # 浮点数

print "Age = $age\n";
print "Name = $name\n";
print "Salary = $salary\n";
```


执行以上程序，输出结果为：


```
Age = 20
Name = Runoob
Salary = 130.5
```


---


## 数字标量


标量通常是一个数字或字符串，以下实例演示了不同类型的数字标量的使用：


## 实例



```perl
#!/usr/bin/perl

$integer = 200;
$negative = -300;
$floating = 200.340;
$bigfloat = -1.2E-23;

# 八进制 377 , 十进制为 255
$octal = 0377;

# 十六进制 FF, 十进制为 255
$hexa = 0xff;

print "integer = $integer\n";
print "negative = $negative\n";
print "floating = $floating\n";
print "bigfloat = $bigfloat\n";
print "octal = $octal\n";
print "hexa = $hexa\n";
```


执行以上程序，输出结果为：


```
integer = 200
negative = -300
floating = 200.34
bigfloat = -1.2e-23
octal = 255
hexa = 255
```


---


## 字符串标量


以下实例演示了不同类型的字符串标量的使用，注意单引号和双引号的使用区别：


## 实例



```perl
#!/usr/bin/perl

$var = "字符串标量 - 菜鸟教程!";
$quote = '我在单引号内 - $var';
$double = "我在双引号内 - $var";

$escape = "转义字符使用 -\tHello, World!";

print "var = $var\n";
print "quote = $quote\n";
print "double = $double\n";
print "escape = $escape\n";
```


执行以上程序，输出结果为：


```
var = 字符串标量 - 菜鸟教程!
quote = 我在单引号内 - $var
double = 我在双引号内 - 字符串标量 - 菜鸟教程!
escape = 转义字符使用 -    Hello, World!
```


---


## 标量运算


以下实例演示了标量的简单运算：


## 实例



```perl
#!/usr/bin/perl

$str = "hello" . "world";       # 字符串连接
$num = 5 + 10;                  # 两数相加
$mul = 4 * 5;                   # 两数相乘
$mix = $str . $num;             # 连接字符串和数字

print "str = $str\n";
print "num = $num\n";
print "mix = $mix\n";
```


执行以上程序，输出结果为：


```
str = helloworld
num = 15
mix = helloworld15
```


---


## 多行字符串


我们可以使用单引号来输出多行字符串，如下所示：


## 实例



```perl
#!/usr/bin/perl

$string = '
菜鸟教程
    —— 学的不仅是技术，更是梦想！
';

print "$string\n";
```


执行以上程序，输出结果为：


```
菜鸟教程
    —— 学的不仅是技术，更是梦想！
```


你也可以使用 "here" document 的语法格式来输出多行：


## 实例



```perl
#!/usr/bin/perl

print <<EOF;
菜鸟教程
    —— 学的不仅是技术，更是梦想！
EOF
```


执行以上程序，输出结果为：


```
菜鸟教程
    —— 学的不仅是技术，更是梦想！
```


---


## 特殊字符


以下我们将演示 Perl 中特殊字符的应用，如 __FILE__, __LINE__, 和 __PACKAGE__ 分别表示当前执行脚本的文件名，行号，包名。


**注意**： **__** 是两条下划线，**__FILE__** 前后各两条下划线。


这些特殊字符是单独的标记，不能写在字符串中，例如：


## 实例



```perl
#!/usr/bin/perl

print "文件名 ". __FILE__ . "\n";
print "行号 " . __LINE__ ."\n";
print "包名 " . __PACKAGE__ ."\n";

# 无法解析
print "__FILE__ __LINE__ __PACKAGE__\n";
```


执行以上程序，输出结果为：


```
文件名 test.pl
行号 4
包名 main
__FILE__ __LINE__ __PACKAGE__
```


---


## v 字符串


一个以 v 开头,后面跟着一个或多个用句点分隔的整数,会被当作一个字串文本。

当你想为每个字符 直接声明其数字值时,v-字串提供了一种更清晰的构造这类字串的方法，而不像 "\x{1}\x{14}\x{12c}\x{fa0}" 这种不易于理解，我们可以看下面的实例：


## 实例



```perl
#!/usr/bin/perl

$smile  = v9786;
$foo    = v102.111.111;
$martin = v77.97.114.116.105.110;

print "smile = $smile\n";
print "foo = $foo\n";
print "martin = $martin\n";
```


执行以上程序，输出结果为：


```
Wide character in print at test.pl line 7.
smile = &#x263a;
foo = foo
martin = Martin
```










	  AI 思考中...





			** [Perl 变量](https://www.runoob.com/perl-variables.html)
			[Perl 数组](https://www.runoob.com/perl-arrays.html) **













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
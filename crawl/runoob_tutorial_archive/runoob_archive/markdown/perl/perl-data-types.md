# Perl 数据类型

- Source: https://www.runoob.com/perl/perl-data-types.html

Perl 是一种弱类型语言，所以变量不需要指定类型，Perl 解释器会根据上下文自动选择匹配类型。


Perl 有三个基本的数据类型：标量、数组、哈希。以下是这三种数据类型的说明：


| 序号 | 类型和描述 |
| --- | --- |
| 1 | 标量 标量是 Perl 语言中最简单的一种数据类型。这种数据类型的变量可以是数字，字符串，浮点数，不作严格的区分。在使用时在变量的名字前面加上一个 $，表示是标量。例如：
```
$myfirst=123;　    #数字123　

$mysecond="123";   #字符串123
```
 |
| 2 | 数组 数组变量以字符 @ 开头，索引从 0 开始，如：@arr=(1,2,3)
```
@arr=(1,2,3)
```
 |
| 3 | 哈希 哈希是一个无序的 key/value 对集合。可以使用键作为下标获取值。哈希变量以字符 % 开头。
```
%h=('a'=>1,'b'=>2);
```
 |


---


## 数字字面量


### 一、整型


Perl 实际上把整数存在你的计算机中的浮点寄存器中，所以实际上被当作浮点数看待。

在多数计算机中，浮点寄存器可以存贮约 16 位数字，长于此的被丢弃。整数实为浮点数的特例。


整型变量及运算：


```
$x = 12345;
if (1217 + 116 == 1333) {
    # 执行代码语句块
}
```


8 进制和 16 进制数：8 进制以 0 开始，16 进制以 0x 开始。例如：


```
$var1 = 047;    # 等于十进制的39
$var2 = 0x1f;   # 等于十进制的31
```


### 二、浮点数


浮点数数据如：11.4 、 -0.3 、.3 、 3. 、 54.1e+02 、 5.41e03。


浮点寄存器通常不能精确地存贮浮点数，从而产生误差，在运算和比较中要特别注意。指数的范围通常为 -309 到 +308。


## 实例



```perl
#!/usr/bin/perl

$value = 9.01e+21 + 0.01 - 9.01e+21;
print ("第一个值为：", $value, "\n");
$value = 9.01e+21 - 9.01e+21 + 0.01;
print ("第二个值为:", $value, "\n");
```


执行以上程序，输出结果为：


```
第一个值为：0
第二个值为:0.01
```


### 三、字符串

Perl 中的字符串使用一个标量来表示，定义方式和 c 很像，但是在 Perl 里面字符串不是用 \0 来表示结束的。


Perl 双引号和单引号的区别: 双引号可以正常解析一些转义字符与变量，而单引号无法解析会原样输出。 但是用单引号定义可以使用多行文本，如下所示：


```
#!/usr/bin/perl

$var='这是一个使用

多行字符串文本

的例子';

print($var);
```


执行以上程序，输出结果为：


```
这是一个使用

多行字符串文本

的例子
```


Perl 语言中常用的一些转义字符如下表所示：


| 转义字符 | 含义 |
| --- | --- |
| \\ | 反斜线 |
| \' | 单引号 |
| \" | 双引号 |
| \a | 系统响铃 |
| \b | 退格 |
| \f | 换页符 |
| \n | 换行 |
| \r | 回车 |
| \t | 水平制表符 |
| \v | 垂直制表符 |
| \0nn | 创建八进制格式的数字 |
| \xnn | 创建十六进制格式的数字 |
| \cX | 控制字符，x可以是任何字符 |
| \u | 强制下一个字符为大写 |
| \l | 强制下一个字符为小写 |
| \U | 强制将所有字符转换为大写 |
| \L | 强制将所有的字符转换为小写 |
| \Q | 将到\E为止的非单词（non-word）字符加上反斜线 |
| \E | 结束\L、\U、\Q |


### 实例


接下来让我们来具体看看单引号和双引号及转义字符的使用：


## 实例



```perl
#!/usr/bin/perl

# 换行 \n 位于双引号内，有效
$str = "菜鸟教程  \nwww.runoob.com";
print "$str\n";

# 换行 \n 位于单引号内，无效
$str = '菜鸟教程  \nwww.runoob.com';
print "$str\n";

# 只有 R 会转换为大写
$str = "\urunoob";
print "$str\n";

# 所有的字母都会转换为大写
$str = "\Urunoob";
print "$str\n";

# 指定部分会转换为大写
$str = "Welcome to \Urunoob\E.com!";
print "$str\n";

# 将到\E为止的非单词（non-word）字符加上反斜线
$str = "\QWelcome to runoob's family";
print "$str\n";
```


以上实例执行输出结果为：


![](https://www.runoob.com/wp-content/uploads/2016/06/57846A1E-EABF-4BCA-BE76-8EB22B831779.jpg)









	  AI 思考中...





			** [Perl 基础语法](https://www.runoob.com/perl-syntax.html)
			[Perl 变量](https://www.runoob.com/perl-variables.html) **













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
# Perl 条件语句

- Source: https://www.runoob.com/perl/perl-conditions.html

Perl 条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。

可以通过下图来简单了解条件语句的执行过程:


![](https://www.runoob.com/wp-content/uploads/2016/06/Q1hUjVgberLytG0p.png)

**
注意，数字 **0**, 字符串 **'0'** 、 **""** , 空 **list()** , 和 **undef** 为 false** ，其他值均为 **true**。 true 前面使用 **!** 或 **not**则返回 false 。


Perl 提供了下列条件语句：


| 语句 | 描述 |
| --- | --- |
| if 语句 | 一个 if 语句 由一个布尔表达式后跟一个或多个语句组成。 |
| if...else 语句 | 一个 if 语句 后可跟一个可选的 else 语句，else 语句在布尔表达式为假时执行。 |
| if...elsif...else 语句 | 您可以在一个 if 语句后可跟一个可选的 elsif 语句，然后再跟另一个 else 语句。 |
| unless 语句 | 一个 unless 语句 由一个布尔表达式后跟一个或多个语句组成。 |
| unless...else 语句。 | 一个 unless 语句 后可跟一个可选的 else 语句。 |
| unless...elsif..else statement | 一个 unless 语句 后可跟一个可选的 elsif 语句，然后再跟另一个 else 语句。 |
| switch 语句 | 在最新版本的 Perl 中，我们可以使用 switch 语句。它根据不同的值执行对应的代码块。 |


---


## 三元运算符 ? :


我们可以使用 **条件运算 ? :** 来简化 **if...else** 语句的操作。通常格式为：


```
Exp1 ? Exp2 : Exp3;
```


如果 Exp1 表达式为 true ，则返回 Exp2 表达式计算结果，否则返回 Exp3。


实例如下所示：


## 实例



```perl
#!/usr/local/bin/perl

$name = "菜鸟教程";
$favorite = 10;     # 喜欢数

$status = ($favorite > 60 )? "热门网站" : "不是热门网站";

print "$name - $status\n";
```


执行以上程序，输出结果为：


```
菜鸟教程 - 不是热门网站
```










	  AI 思考中...





			** [Perl 哈希](https://www.runoob.com/perl-hashes.html)
			[Perl IF 语句](https://www.runoob.com/perl-if-statement.html) **













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
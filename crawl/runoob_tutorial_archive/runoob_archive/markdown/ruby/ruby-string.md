# Ruby 字符串（String）

- Source: https://www.runoob.com/ruby/ruby-string.html

Ruby 中的 String 对象用于存储或操作一个或多个字节的序列。


Ruby 字符串分为单引号字符串（'）和双引号字符串（"），区别在于双引号字符串能够支持更多的转义字符。


### 单引号字符串


最简单的字符串是单引号字符串，即在单引号内存放字符串：


```ruby
'这是一个 Ruby 程序的字符串'
```


如果您需要在单引号字符串内使用单引号字符，那么需要在单引号字符串使用反斜杠(\)，这样 Ruby 解释器就不会认为这个单引号字符是字符串的终止符号：


```ruby
'Won\'t you read O\'Reilly\'s book?'
```


反斜杠也能转义另一个反斜杠，这样第二个反斜杠本身不会解释为转义字符。


以下是 Ruby 中字符串相关的特性。


### 双引号字符串


在双引号字符串中我们可以使用 **#{}** 井号和大括号来计算表达式的值：


字符串中嵌入变量：


## 实例


```ruby
#!/usr/bin/ruby
# -*- coding: UTF-8 -*-

name1 = "Joe"
name2 = "Mary"
puts "你好 #{name1},  #{name2} 在哪?"
```


**
[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=strobj_demo&type=ruby)


以上实例输出运行输出结果为：


```
你好 Joe,  Mary 在哪?
```


字符串中进行数学运算：


## 实例


```ruby
#!/usr/bin/ruby
# -*- coding: UTF-8 -*-

x, y, z = 12, 36, 72
puts "x 的值为 #{ x }"
puts "x + y 的值为 #{ x + y }"
puts "x + y + z 的平均值为 #{ (x + y + z)/3 }"
```


[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=strobj_demo2&type=ruby)


以上实例输出运行输出结果为：


```
x 的值为 12
x + y 的值为 48
x + y + z 的平均值为 40
```


Ruby 中还支持一种采用 %q 和 %Q 来引导的字符串变量，%q 使用的是单引号引用规则，而 %Q 是双引号引用规则，后面再接一个 (! [ { 等等的开始界定符和与 } ] ) 等等的末尾界定符。


跟在 q 或 Q 后面的字符是分界符.分界符可以是任意一个非字母数字的单字节字符.如:[,{,(,







	  AI 思考中...





			** [Ruby 模块（Module）](https://www.runoob.com/ruby-module.html)
			[Ruby 数组（Array）](https://www.runoob.com/ruby-array.html) **













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
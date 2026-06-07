# Ruby CGI 编程

- Source: https://www.runoob.com/ruby/ruby-cgi.html

Ruby 是一门通用的语言，不仅仅是一门应用于WEB开发的语言，但 Ruby 在WEB应用及WEB工具中的开发是最常见的。

使用Ruby您不仅可以编写自己的SMTP服务器，FTP程序，或Ruby Web服务器，而且还可以使用Ruby进行CGI编程。

接下来，让我们花点时间来学习Ruby的CGI编辑。


---

## 网页浏览


为了更好的了解CGI是如何工作的，我们可以从在网页上点击一个链接或URL的流程：


- 1、使用你的浏览器访问URL并连接到HTTP web 服务器。
- 2、Web服务器接收到请求信息后会解析URL，并查找访问的文件在服务器上是否存在，如果存在返回文件的内容，否则返回错误信息。
- 3、浏览器从服务器上接收信息，并显示接收的文件或者错误信息。


CGI程序可以是 Ruby 脚本，Python 脚本，PERL 脚本，SHELL 脚本，C 或者 C++ 程序等。


---


## CGI架构图


![cgiarch](https://www.runoob.com/wp-content/uploads/2013/11/cgiarch1.gif)


---


## Web服务器支持及配置


在你进行CGI编程前，确保您的Web服务器支持CGI及已经配置了CGI的处理程序。


Apache 支持CGI 配置：


设置好CGI目录：


```
ScriptAlias /cgi-bin/ /var/www/cgi-bin/
```


所有的HTTP服务器执行CGI程序都保存在一个预先配置的目录。这个目录被称为CGI目录，并按照惯例，它被命名为/var/www/cgi-bin目录。

CGI文件的扩展名为.cgi，Ruby 也可以使用 .rb 扩展名。

默认情况下，Linux服务器配置运行的cgi-bin目录中为/var/www。

如果你想指定其他运行CGI脚本的目录，可以修改httpd.conf配置文件，如下所示：


```
<Directory "/var/www/cgi-bin">
   AllowOverride None
   Options +ExecCGI
   Order allow,deny
   Allow from all
</Directory>
```


在 AddHandler 中添加 .rb 后缀，这样我们就可以访问 .rb 结尾的 Ruby 脚本文件：


```
AddHandler cgi-script .cgi .pl .rb
```


---


## 编写 CGI 脚本


最基本的 Ruby CGI 代码如下所示：


```
#!/usr/bin/ruby

puts "Content-type: text/html\n\n"
puts "<html><body>This is a test</body></html>"
```


你可以将该代码保持到 test.cgi 文件中，上次到服务器并赋予足够权限，即可作为 CGI 脚本执行。


如果你站的的地址为http://www.example.com/ ，即可用过http://www.example.com/test.cgi 访问该程序，输出结果为： "This is a test."。


浏览器访问该网址后，Web 服务器会在站点目录下找到 test.cgi文件，然后通过Ruby解析器来解析脚本代码并访问HTML文档。


---


## 使用 cgi.rb


Ruby 可以调用 CGI 库来编写更复杂的CGI脚本。


以下代码调用了 CGI 库来创建一个脚本的CGI脚本。


```
#!/usr/bin/ruby

require 'cgi'

cgi = CGI.new
puts cgi.header
puts "<html><body>This is a test</body></html>"
```


以下代码中，创建了CGI 对象并打印头部信息。


---


## 表单处理


使用CGI库可以通过两种方式获取表单提交（或URL中的参数）的数据， 例如URL：/cgi-bin/test.cgi?FirstName=Zara&LastName;=Ali。


你可以使用 CGI#[] 来直接获取参数FirstName和LastName：


```
#!/usr/bin/ruby

require 'cgi'
cgi = CGI.new
cgi['FirstName'] # =>  ["Zara"]
cgi['LastName']  # =>  ["Ali"]
```


另外一种获取表单数据的方法：


```
#!/usr/bin/ruby

require 'cgi'
cgi = CGI.new
h = cgi.params  # =>  {"FirstName"=>["Zara"],"LastName"=>["Ali"]}
h['FirstName']  # =>  ["Zara"]
h['LastName']   # =>  ["Ali"]
```


以下代码用于检索所有的键值：


```
#!/usr/bin/ruby

require 'cgi'
cgi = CGI.new
cgi.keys         # =>  ["FirstName", "LastName"]
```


如果表单包含了多个相同名称的字段，则该相同字段的值将保存在数组中。


以下实例中，指定表单中三个相同的字段"name"，值分别为 "Zara", "Huma" 和 "Nuha":


```
#!/usr/bin/ruby

require 'cgi'
cgi = CGI.new
cgi['name']        # => "Zara"
cgi.params['name'] # => ["Zara", "Huma", "Nuha"]
cgi.keys           # => ["name"]
cgi.params         # => {"name"=>["Zara", "Huma", "Nuha"]}
```


**注意：**Ruby 会自动判断 GET 和 POST 方法，所以无需对两种方法区别对待。


以下是相关的HML代码：


```
<html>
<body>
<form method="POST" action="http://www.example.com/test.cgi">
First Name :<input type="text" name="FirstName" value="" />
<br />
Last Name :<input type="text" name="LastName" value="" />

<input type="submit" value="Submit Data" />
</form>
</body>
</html>
```


---


## 创建 Form 表单和 HTML


CGI 包含了大量的方法来创建 HTML，每个HTML标签都有相对应的方法。 在使用这些方法前，比必须通过 CGI.new 来创建 CGI 对象。


为了使标签的嵌套更加的简单，这些方法将内容作为了代码块，代码块将返回字符串作为标签的内容。如下所示：


```
#!/usr/bin/ruby

require "cgi"
cgi = CGI.new("html4")
cgi.out{
   cgi.html{
      cgi.head{ "\n"+cgi.title{"This Is a Test"} } +
      cgi.body{ "\n"+
         cgi.form{"\n"+
            cgi.hr +
            cgi.h1 { "A Form: " } + "\n"+
            cgi.textarea("get_text") +"\n"+
            cgi.br +
            cgi.submit
         }
      }
   }
}
```


---


## 字符串转义


当你在处理 URL 中的参数或者 HTML 表单数据时，需要对指定的特殊字符进行转义，如：引号（"）,反斜杠(/)。


Ruby CGI 对象提供了CGI.escape 和 CGI.unescape 方法来处理这些特殊字符的转义：


```
#!/usr/bin/ruby

require 'cgi'
puts CGI.escape(Zara Ali/A Sweet & Sour Girl")
```


以上代码执行结果如下：


```
#!/usr/bin/ruby

require 'cgi'
puts CGI.escape(Zara Ali/A Sweet & Sour Girl")
```


另一组实例：


```
#!/usr/bin/ruby

require 'cgi'
puts CGI.escapeHTML('<h1>Zara Ali/A Sweet & Sour Girl</h1>')
```


以上代码执行结果如下：


```
&lt;h1&gt;Zara Ali/A Sweet & Sour Girl&lt;/h1&gt;'
```


---


## CGI 类中常用的方法


以下是Ruby中完整的CGI类的相关方法


- [Ruby CGI](https://www.runoob.com/ruby-cgi-methods.html) - 标准 CGI 库相关方法


---


## Cookies 和 Sessions


- [Ruby CGI Cookies](https://www.runoob.com/ruby-cgi-cookies.html) - 如何处理 CGI Cookies.
- [Ruby CGI Sessions](https://www.runoob.com/ruby-cgi-sessions.html) - 如何处理 CGI sessions.








	  AI 思考中...





			** [Ruby DBI Read 操作](https://www.runoob.com/ruby-dbi-read.html)
			[Ruby CGI方法](https://www.runoob.com/ruby-cgi-methods.html) **













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
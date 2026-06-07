# Ruby 发送邮件 - SMTP

- Source: https://www.runoob.com/ruby/ruby-sending-email.html

SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。


Ruby提供了 Net::SMTP 来发送邮件，并提供了两个方法 new 和 start:


**new** 方法有两个参数：


- *server name* 默认为 localhost
- *port number* 默认为 25


**start** 方法有以下参数：


- *server* - SMTP 服务器 IP, 默认为 localhost
- *port* - 端口号，默认为 25
- *domain* - 邮件发送者域名，默认为 ENV["HOSTNAME"]
- *account* - 用户名，默认为 nil
- *password* - 用户密码，默认为nil
- *authtype* - 验证类型，默认为 *cram_md5*


SMTP 对象实例化方法调用了 sendmail, 参数如下：



- *source* - 一个字符串或数组或每个迭代器在任一时间中返回的任何东西。
- *sender* -一个字符串，出现在 email 的表单字段。
- *recipients* - 一个字符串或字符串数组，表示收件人的地址。


### 实例


以下提供了简单的Ruby脚本来发送邮件:


## 实例


```ruby
require 'net/smtp'

message = <<MESSAGE_END
From: Private Person <me@fromdomain.com>
To: A Test User <test@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
MESSAGE_END

Net::SMTP.start('localhost') do |smtp|
  smtp.send_message message, '[email protected]',
                             '[email protected]'
end
```


在以上实例中，你已经设置了一个基本的电子邮件消息，注意正确的标题格式。一个电子邮件要要From，To和Subject，文本内容与头部信息间需要一个空行。

使用Net::SMTP连接到本地机器上的SMTP服务器，使用send_message方法来发送邮件，方法参数为发送者邮件与接收者邮件。


如果你没有运行在本机上的SMTP服务器，您可以使用Net::SMTP与远程SMTP服务器进行通信。如果使用网络邮件服务（如Hotmail或雅虎邮件），您的电子邮件提供者会为您提供发送邮件服务器的详细信息:


```ruby
Net::SMTP.start('mail.your-domain.com')
```


以上代码将连接主机为 mail.your-domain.com，端口号为 25的邮件服务器，如果需要填写用户名密码，则代码如下：


```ruby
Net::SMTP.start('mail.your-domain.com',
                25,
                'localhost',
                'username', 'password', :plain)
```


以上实例使用了指定的用户名密码连接到主机为 mail.your-domain.com，端口号为 25的邮件服务器。


---


## 使用 Ruby 发送 HTML 邮件


Net::SMTP同样提供了支持发送 HTML 格式的邮件。


发送电子邮件时你可以设置MIME版本，文档类型，字符集来发送HTML格式的邮件。


### 实例


以下实例用于发送 HTML 格式的邮件：


## 实例


```ruby
require 'net/smtp'

message = <<MESSAGE_END
From: Private Person <me@fromdomain.com>
To: A Test User <test@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
MESSAGE_END

Net::SMTP.start('localhost') do |smtp|
  smtp.send_message message, '[email protected]',
                             '[email protected]'
end
```


---


## 发送带附件的邮件


如果需要发送混合内容的电子邮件，需要设置Content-type为multipart/mixed。 这样就可以在邮件中添加附件内容。


附件在传输前需要使用 **pack("m")** 函数将其内容转为 base64 格式。


### 实例


以下实例将发送附件为 /tmp/test.txt 的邮件：


## 实例


```ruby
require 'net/smtp'

filename = "/tmp/test.txt"
# 读取文件并编码为base64格式
filecontent = File.read(filename)
encodedcontent = [filecontent].pack("m")   # base64

marker = "AUNIQUEMARKER"

body =<<EOF
This is a test email to send an attachement.
EOF

# 定义主要的头部信息
part1 =<<EOF
From: Private Person <me@fromdomain.net>
To: A Test User <test@todmain.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=#{marker}
--#{marker}
EOF

# 定义消息动作
part2 =<<EOF
Content-Type: text/plain
Content-Transfer-Encoding:8bit

#{body}
--#{marker}
EOF

# 定义附件部分
part3 =<<EOF
Content-Type: multipart/mixed; name=\"#{filename}\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename="#{filename}"

#{encodedcontent}
--#{marker}--
EOF

mailtext = part1 + part2 + part3

# 发送邮件
begin
  Net::SMTP.start('localhost') do |smtp|
     smtp.sendmail(mailtext, '[email protected]',
                          ['[email protected]'])
  end
rescue Exception => e
  print "Exception occured: " + e
end
```


**注意：**你可以指定多个发送的地址，但需要使用逗号隔开。








	  AI 思考中...





			** [Ruby CGI Session](https://www.runoob.com/ruby-cgi-sessions.html)
			[Ruby Socket 编程](https://www.runoob.com/ruby-socket-programming.html) **













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
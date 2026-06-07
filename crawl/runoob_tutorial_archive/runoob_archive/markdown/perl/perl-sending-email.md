# Perl 发送邮件

- Source: https://www.runoob.com/perl/perl-sending-email.html

如果你的程序在 Linux/Unix 系统上运行，你就可以在 Perl 中使用 **sendmail** 工具来发送邮件。


以下是一个简单的脚本实例用于发送邮件：


## 实例



```perl
#!/usr/bin/perl

# 接收邮箱，这里我设置为我的 QQ 邮箱，你需要修改它为你自己的邮箱
$to = '[email protected]';
#发送者邮箱
$from = '[email protected]';
#标题
$subject = '菜鸟教程 Perl 发送邮件测试';
$message = '这是一封使用 Perl 发送的邮件。';

open(MAIL, "|/usr/sbin/sendmail -t");

# 邮件头部
print MAIL "To: $to\n";
print MAIL "From: $from\n";
print MAIL "Subject: $subject\n\n";
# 邮箱信息
print MAIL $message;

close(MAIL);
print "邮件发送成功\n";
```


执行以上程序，输出结果为：


```
邮件发送成功
```


**

正常情况下，以上邮件会被 QQ 邮箱拦截，我么可以把它加入白名单，操作方式可以点击：[https://kf.qq.com/faq/120322fu63YV130805rYRFzu.html](https://kf.qq.com/faq/120322fu63YV130805rYRFzu.html)


加入白名单后就可以正常接收邮件了。


![](https://www.runoob.com/wp-content/uploads/2016/06/FAA63A9E-9AE1-4217-B440-FCA908900B1E.jpg)


### 发送 HTML 格式邮件


我们可以在邮件头部添加 Content-type: text/html\n** 来发送 HTML 格式的邮件，实例如下：


## 实例



```perl
#!/usr/bin/perl

# 接收邮箱，这里我设置为我的 QQ 邮箱，你需要修改它为你自己的邮箱
$to = '[email protected]';
#发送者邮箱
$from = '[email protected]';
#标题
$subject = '菜鸟教程 Perl 发送邮件测试';
$message = '<h1>这是一封使用 Perl 发送的邮件<h1><p>你好，我来自菜鸟教程，地址是:http://www.runoob.com。</p>';

open(MAIL, "|/usr/sbin/sendmail -t");

# 邮件头部
print MAIL "To: $to\n";
print MAIL "From: $from\n";
print MAIL "Subject: $subject\n";
print MAIL "Content-type: text/html\n";
# 邮箱信息
print MAIL $message;

close(MAIL);
print "邮件发送成功\n";
```


执行成功后，查看邮件内容，如下所示：


![](https://www.runoob.com/wp-content/uploads/2016/06/FAA63A9E-9AE1-4217-B440-FCA908900B1E.jpg)


---


## 使用 MIME::Lite 模块


如果你使用的是 window 系统，没有 sendmail 工具。这时你就可以使用 perl 的 MIME:Lite 模块作为邮件客户端来发送邮件。


MIME:Lite 模块 下载地址为：[MIME-Lite-3.030.tar.gz](http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/MIME-Lite-3.030.tar.gz)。


这里我们直接用 cpan 来安装(需要 root 权限)，不用下载：


```
$ cpan -i MIME::Lite
……
  /usr/bin/make install  -- OK
```


安装成功后，我们来演示一个实例：


## 实例



```perl
#!/usr/bin/perl
use MIME::Lite;

# 接收邮箱，这里我设置为我的 QQ 邮箱，你需要修改它为你自己的邮箱
$to = '[email protected]';
# 抄送者，多个使用逗号隔开
# $cc = '[email protected], [email protected]';

#发送者邮箱
$from = '[email protected]';
#标题
$subject = '菜鸟教程 Perl 发送邮件测试';
$message = '这是一封使用 Perl 发送的邮件，使用了 MIME::Lite 模块。';

$msg = MIME::Lite->new(
                 From     => $from,
                 To       => $to,
                 Cc       => $cc,
                 Subject  => $subject,
                 Data     => $message
                 );

$msg->send;
print "邮件发送成功\n";
```


执行成功后，查看邮件内容，如下所示：


![](https://www.runoob.com/wp-content/uploads/2016/06/71DCF087-EB4E-4D43-B077-0E7E9FE8EEFD.jpg)


### 发送 HTML 格式邮件


我们可以在邮件头部添加 **Content-type: text/html\n** 来发送 HTML 格式的邮件，实例如下：


## 实例



```perl
#!/usr/bin/perl
use MIME::Lite;

# 接收邮箱，这里我设置为我的 QQ 邮箱，你需要修改它为你自己的邮箱
$to = '[email protected]';
# 抄送者，多个使用逗号隔开
# $cc = '[email protected], [email protected]';

#发送者邮箱
$from = '[email protected]';
#标题
$subject = '菜鸟教程 Perl 发送邮件测试';
$message = '<h1>这是一封使用 Perl 发送的邮件<h1><p>使用了 MIME::Lite 模块。</p><p>来自菜鸟教程，地址是:http://www.runoob.com。</p>';

$msg = MIME::Lite->new(
                 From     => $from,
                 To       => $to,
                 Cc       => $cc,
                 Subject  => $subject,
                 Data     => $message
                 );

# 添加头部信息
$msg->attr("content-type" => "text/html");
$msg->send;
print "邮件发送成功\n";
```


执行成功后，查看邮件内容，如下所示：


![](https://www.runoob.com/wp-content/uploads/2016/06/F9C72C91-8226-4A1B-9E17-F172261FAE12.jpg)


### 发送带有附件的邮件


发送带有附件的邮件实例如下：


## 实例



```perl
#!/usr/bin/perl
use MIME::Lite;

# 接收邮箱，这里我设置为我的 QQ 邮箱，你需要修改它为你自己的邮箱
$to = '[email protected]';
# 抄送者，多个使用逗号隔开
# $cc = '[email protected], [email protected]';

#发送者邮箱
$from = '[email protected]';
#标题
$subject = '菜鸟教程 Perl 发送邮件测试';
$message = '这是一封使用 Perl 发送的邮件，使用了 MIME::Lite 模块，包含了附件。';

$msg = MIME::Lite->new(
                 From     => $from,
                 To       => $to,
                 Cc       => $cc,
                 Subject  => $subject,
                 Type     => 'multipart/mixed'   # 附件标记
                 );

$msg->attach (
              Type => 'TEXT',
              Data => $message
);# 指定附件信息
$msg->attach(Type        => 'TEXT',
             Path        => './runoob.txt',   # 当前目录下
             Filename    => 'runoob.txt',
             Disposition => 'attachment'
            );
$msg->send;
print "邮件发送成功\n";
```


执行成功后，查看邮件内容，如下所示：


![](https://www.runoob.com/wp-content/uploads/2016/06/39897BBF-6B5A-467C-9F6C-ABD36752EDF3.jpg)


你可以通过使用多个 $msg->attach 来添加多个附件。









	  AI 思考中...





			** [Perl 正则表达式](https://www.runoob.com/perl-regular-expressions.html)
			[Perl Socket 编程](https://www.runoob.com/perl-socket-programming.html) **













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
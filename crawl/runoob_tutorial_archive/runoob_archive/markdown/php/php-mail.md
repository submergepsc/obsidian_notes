# PHP 发送电子邮件

- Source: https://www.runoob.com/php/php-mail.html

---


PHP 允许您从脚本直接发送电子邮件。


---


## PHP mail() 函数


PHP mail() 函数用于从脚本中发送电子邮件。


**语法**


mail(to,subject,message,headers,parameters)


**
| 参数 | 描述 |
| --- | --- |
| to | 必需。规定 email 接收者。 |
| subject | 必需。规定 email 的主题。注释：该参数不能包含任何新行字符。 |
| message | 必需。定义要发送的消息。应使用 LF (\n) 来分隔各行。每行应该限制在 70 个字符内。 |
| headers | 可选。规定附加的标题，比如 From、Cc 和 Bcc。应当使用 CRLF (\r\n) 分隔附加的标题。 |
| parameters | 可选。对邮件发送程序规定额外的参数。 |


注释：**PHP 运行邮件函数需要一个已安装且正在运行的邮件系统(如：sendmail、postfix、qmail等)。所用的程序通过在 php.ini 文件中的配置设置进行定义。请在我们的 [PHP Mail 参考手册](https://www.runoob.com/php-ref-mail.html) 阅读更多内容。


---


## PHP 简易 E-Mail


通过 PHP 发送电子邮件的最简单的方式是发送一封文本 email。


在下面的实例中，我们首先声明变量($to, $subject, $message, $from, $headers)，然后我们在 mail() 函数中使用这些变量来发送了一封 E-mail：


```
<?php
$to = "[email protected]";         // 邮件接收者
$subject = "参数邮件";                // 邮件标题
$message = "Hello! 这是邮件的内容。";  // 邮件正文
$from = "[email protected]";   // 邮件发送者
$headers = "From:" . $from;         // 头部信息设置
mail($to,$subject,$message,$headers);
echo "邮件已发送";
?>
```


**
---


## PHP Mail 表单


通过 PHP，您能够在自己的站点制作一个反馈表单。下面的实例向指定的 e-mail 地址发送了一条文本消息：


```
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<?php
if (isset($_REQUEST['email'])) { // 如果接收到邮箱参数则发送邮件
    // 发送邮件
    $email = $_REQUEST['email'] ;
    $subject = $_REQUEST['subject'] ;
    $message = $_REQUEST['message'] ;
    mail("[email protected]", $subject,
    $message, "From:" . $email);
    echo "邮件发送成功";
} else { // 如果没有邮箱参数则显示表单
    echo "<form method='post' action='mailform.php'>
    Email: <input name='email' type='text'><br>
    Subject: <input name='subject' type='text'><br>
    Message:<br>
    <textarea name='message' rows='15' cols='40'>
    </textarea><br>
    <input type='submit'>
    </form>";
}
?>

</body>
</html>
```


实例解释：
- 首先，检查是否填写了邮件输入框
- 如果未填写（比如在页面被首次访问时），输出 HTML 表单
- 如果已填写（在表单被填写后），从表单发送电子邮件
- 当填写完表单点击提交按钮后，页面重新载入，可以看到邮件输入被重置，同时显示邮件发送成功的消息


注释：**这个简易发送 e-mail 不安全，在本教程的下一章中，您将阅读到更多关于电子邮件脚本中的安全隐患，我们将为您讲解如何验证用户输入使它更安全。


---


## PHP Mail 参考手册


如需查看更多关于 PHP mail() 函数的信息，请访问我们的 [PHP Mail 参考手册](https://www.runoob.com/php-ref-mail.html)。








	  AI 思考中...





			** [PHP Session](https://www.runoob.com/php-sessions.html)
			[PHP 安全 E-mail](https://www.runoob.com/php-secure-mail.html) **













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
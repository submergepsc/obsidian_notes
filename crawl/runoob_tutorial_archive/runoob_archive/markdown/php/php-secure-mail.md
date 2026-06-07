# PHP Secure E-mails

- Source: https://www.runoob.com/php/php-secure-mail.html

---


在上一节中的 PHP e-mail 脚本中，存在着一个漏洞。


---


## PHP E-mail 注入


首先，请看上一章中的 PHP 代码：


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


以上代码存在的问题是，未经授权的用户可通过输入表单在邮件头部插入数据。


假如用户在表单中的输入框内加入如下文本到电子邮件中，会出现什么情况呢？


```
[email protected]%0ACc:[email protected]
%0ABcc:[email protected],[email protected],
[email protected],[email protected]
%0ABTo:[email protected]
```


与往常一样，mail() 函数把上面的文本放入邮件头部，那么现在头部有了额外的 Cc:、Bcc: 和 To: 字段。当用户点击提交按钮时，这封 e-mail 会被发送到上面所有的地址！


---


## PHP 防止 E-mail 注入


防止 e-mail 注入的最好方法是对输入进行验证。


下面的代码与上一章中的类似，不过这里我们已经增加了检测表单中 email 字段的输入验证程序：


```
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
<?php
function spamcheck($field)
{
    // filter_var() 过滤 e-mail
    // 使用 FILTER_SANITIZE_EMAIL
    $field=filter_var($field, FILTER_SANITIZE_EMAIL);

    //filter_var() 过滤 e-mail
    // 使用 FILTER_VALIDATE_EMAIL
    if(filter_var($field, FILTER_VALIDATE_EMAIL))
    {
        return TRUE;
    }
    else
    {
        return FALSE;
    }
}

if (isset($_REQUEST['email']))
{
    // 如果接收到邮箱参数则发送邮件

    // 判断邮箱是否合法
    $mailcheck = spamcheck($_REQUEST['email']);
    if ($mailcheck==FALSE)
    {
        echo "非法输入";
    }
    else
    {
        // 发送邮件
        $email = $_REQUEST['email'] ;
        $subject = $_REQUEST['subject'] ;
        $message = $_REQUEST['message'] ;
        mail("[email protected]", "Subject: $subject",
        $message, "From: $email" );
        echo "Thank you for using our mail form";
    }
}
else
{
    // 如果没有邮箱参数则显示表单
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


在上面的代码中，我们使用了 PHP 过滤器来对输入进行验证：


- FILTER_SANITIZE_EMAIL 过滤器从字符串中删除电子邮件的非法字符
- FILTER_VALIDATE_EMAIL 过滤器验证电子邮件地址的值


您可以在我们的 [PHP Filter](https://www.runoob.com/php-filter.html) 中阅读更多关于过滤器的知识。**








	  AI 思考中...





			** [PHP 邮件](https://www.runoob.com/php-mail.html)
			[PHP 错误处理](https://www.runoob.com/php-error.html) **













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
# PHP Cookie

- Source: https://www.runoob.com/php/php-cookies.html

---


cookie 常用于识别用户。


---


## Cookie 是什么？


cookie 常用于识别用户。cookie 是一种服务器留在用户计算机上的小文件。每当同一台计算机通过浏览器请求页面时，这台计算机将会发送 cookie。通过 PHP，您能够创建并取回 cookie 的值。


---


## 如何创建 Cookie？


setcookie() 函数用于设置 cookie。


**注释：**setcookie() 函数必须位于  标签之前。


### 语法


```
setcookie(name, value, expire, path, domain);
```


### 实例 1


在下面的例子中，我们将创建名为 "user" 的 cookie，并为它赋值 "runoob"。我们也规定了此 cookie 在一小时后过期：


```
<?php
setcookie("user", "runoob", time()+3600);
?>

<html>
.....
```


**注释：**在发送 cookie 时，cookie 的值会自动进行 URL 编码，在取回时进行自动解码。（为防止 URL 编码，请使用 setrawcookie() 取而代之。）


### 实例 2


您还可以通过另一种方式设置 cookie 的过期时间。这也许比使用秒表示的方式简单。


```
<?php
$expire=time()+60*60*24*30;
setcookie("user", "runoob", $expire);
?>

<html>
.....
```


在上面的实例中，过期时间被设置为一个月（*60 秒 * 60 分 * 24 小时 * 30 天*）。


---


## 如何取回 Cookie 的值？


PHP 的 $_COOKIE 变量用于取回 cookie 的值。

在下面的实例中，我们取回了名为 "user" 的 cookie 的值，并把它显示在了页面上：


```
<?php
// 输出 cookie 值
echo $_COOKIE["user"];

// 查看所有 cookie
print_r($_COOKIE);
?>
```


在下面的实例中，我们使用 isset() 函数来确认是否已设置了 cookie：


```
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<?php
if (isset($_COOKIE["user"]))
    echo "欢迎 " . $_COOKIE["user"] . "!<br>";
else
    echo "普通访客!<br>";
?>

</body>
</html>
```


**
---


## 如何删除 Cookie？


当删除 cookie 时，您应当使过期日期变更为过去的时间点。


删除的实例：


```
<?php
// 设置 cookie 过期时间为过去 1 小时
setcookie("user", "", time()-3600);
?>
```


---


## 如果浏览器不支持 Cookie 该怎么办？


如果您的应用程序需要与不支持 cookie 的浏览器打交道，那么您不得不使用其他的办法在您的应用程序中的页面之间传递信息。一种方式是通过表单传递数据（有关表单和用户输入的内容，在本教程的前面章节中我们已经介绍过了）。


下面的表单在用户单点击 "Submit" 按钮时，向 "welcome.php" 提交了用户输入：


```
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<form action="welcome.php" method="post">
名字: <input type="text" name="name">
年龄: <input type="text" name="age">
<input type="submit">
</form>

</body>
</html>
```


取回 "welcome.php" 文件中的值，如下所示：


```
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

欢迎 <?php echo $_POST["name"]; ?>.<br>
你 <?php echo $_POST["age"]; ?> 岁了。

</body>
</html>
```









	  AI 思考中...





			** [PHP 文件上传](https://www.runoob.com/php-file-upload.html)
			[PHP Session](https://www.runoob.com/php-sessions.html) **













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
# PHP $_POST 变量

- Source: https://www.runoob.com/php/php-post.html

---


在 PHP 中，预定义的 $_POST 变量用于收集来自 method="post" 的表单中的值。


---


## $_POST 变量


预定义的 $_POST 变量用于收集来自 method="post" 的表单中的值。


从带有 POST 方法的表单发送的信息，对任何人都是不可见的（不会显示在浏览器的地址栏），并且对发送信息的量也没有限制。


**注释：**然而，默认情况下，POST 方法的发送信息的量最大值为 8 MB（可通过设置 php.ini 文件中的 post_max_size 进行更改）。


### 实例


**form.html** 文件代码如下：


```
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<form action="welcome.php" method="post">
名字: <input type="text" name="fname">
年龄: <input type="text" name="age">
<input type="submit" value="提交">
</form>

</body>
</html>
```


当用户点击 "提交" 按钮时，URL 类似如下所示：


```
http://www.runoob.com/welcome.php
```


"welcome.php" 文件现在可以通过 $_POST 变量来收集表单数据了（请注意，表单域的名称会自动成为 $_POST 数组中的键）：


```
欢迎 <?php echo $_POST["fname"]; ?>!<br>
你的年龄是 <?php echo $_POST["age"]; ?>  岁。
```


通过浏览器访问演示如下：


![](https://www.runoob.com/wp-content/uploads/2013/08/form1.gif)

**
---


## 何时使用 method="post"？


从带有 POST 方法的表单发送的信息，对任何人都是不可见的，并且对发送信息的量也没有限制。


然而，由于变量不显示在 URL 中，所以无法把页面加入书签。


---


## PHP $_REQUEST 变量


预定义的 $_REQUEST 变量包含了 $_GET、$_POST 和 $_COOKIE 的内容。


$_REQUEST 变量可用来收集通过 GET 和 POST 方法发送的表单数据。


### 实例


你可以将 "welcome.php" 文件修改为如下代码，它可以接受 $_GET、$_POST等数据。


```
欢迎 <?php echo $_REQUEST["fname"]; ?>!<br>
你的年龄是 <?php echo $_REQUEST["age"]; ?>  岁。
```









	  AI 思考中...





			** [PHP $_GET 变量](https://www.runoob.com/php-get.html)
			[PHP 多维数组](https://www.runoob.com/php-arrays-multi.html) **













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
# PHP 表单 - 必需字段

- Source: https://www.runoob.com/php/php-form-required.html

---


本章节我们将介绍如何设置表单必需字段及错误信息。


---


## PHP - 必需字段


在上一章节我们已经介绍了表的验证规则，我们可以看到"名字", "E-mail", 和 "性别" 字段是必需的，各字段不能为空。


| 字段 | 验证规则 |
| --- | --- |
| 名字 | 必需。 + 只能包含字母和空格 |
| E-mail | 必需。 + 必需包含一个有效的电子邮件地址（包含"@"和"."） |
| 网址 | 可选。 如果存在，它必需包含一个有效的URL |
| 备注 | 可选。多行字段（文本域）。 |
| 性别 | 必需。必需选择一个。 |


如果在前面的章节中，所有输入字段都是可选的。


在以下代码中我们加入了一些新的变量: $nameErr, $emailErr, $genderErr, 和 $websiteErr.。这些错误变量将显示在必需字段上。 我们还为每个$_POST变量增加了一个if else语句。 这些语句将检查 $_POST 变量是 否为空（使用php的 empty() 函数）。如果为空，将显示对应的错误信息。 如果不为空，数据将传递给test_input() 函数：


```
<?php
// 定义变量并默认设为空值
$nameErr = $emailErr = $genderErr = $websiteErr = "";
$name = $email = $gender = $comment = $website = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "名字是必需的。";
  } else {
    $name = test_input($_POST["name"]);
  }

  if (empty($_POST["email"])) {
    $emailErr = "邮箱是必需的。";
  } else {
    $email = test_input($_POST["email"]);
  }

  if (empty($_POST["website"])) {
    $website = "";
  } else {
    $website = test_input($_POST["website"]);
  }

  if (empty($_POST["comment"])) {
    $comment = "";
  } else {
    $comment = test_input($_POST["comment"]);
  }

  if (empty($_POST["gender"])) {
    $genderErr = "性别是必需的。";
  } else {
    $gender = test_input($_POST["gender"]);
  }
}
?>
```


---


## PHP - 显示错误信息


在以下的HTML实例表单中，我们为每个字段中添加了一些脚本， 各个脚本会在信息输入错误时显示错误信息。(如果用户未填写信息就提交表单则会输出错误信息):


```
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
   名字: <input type="text" name="name">
   <span class="error">* <?php echo $nameErr;?></span>
   <br><br>
   E-mail: <input type="text" name="email">
   <span class="error">* <?php echo $emailErr;?></span>
   <br><br>
   网址: <input type="text" name="website">
   <span class="error"><?php echo $websiteErr;?></span>
   <br><br>
   备注: <textarea name="comment" rows="5" cols="40"></textarea>
   <br><br>
   性别:
   <input type="radio" name="gender" value="female">女
   <input type="radio" name="gender" value="male">男
   <span class="error">* <?php echo $genderErr;?></span>
   <br><br>
   <input type="submit" name="submit" value="Submit">
</form>
```


[查看代码 »](https://www.runoob.com/try/showphp.php?filename=demo_form_validation_required)








	  AI 思考中...





			** [PHP curl_version函数](https://www.runoob.com/func-curl_version.html)
			[PHP 表单 – 验证邮件和URL](https://www.runoob.com/php-form-url-email.html) **













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
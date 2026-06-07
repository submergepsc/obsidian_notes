# PHP 文件上传

- Source: https://www.runoob.com/php/php-file-upload.html

---


通过 PHP，可以把文件上传到服务器。


本章节实例在 test 项目下完成，目录结构为：


```
test
|-----upload             # 文件上传的目录
|-----form.html          # 表单文件
|-----upload_file.php    # php 上传代码
```


[源码下载](https://www.runoob.com/wp-content/uploads/2013/08/runoob-file-uplaod-demo.zip) --- ## 创建一个文件上传表单 允许用户从表单上传文件是非常有用的。


请看下面这个供上传文件的 HTML 表单：


```
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>

<form action="upload_file.php" method="post" enctype="multipart/form-data">
    <label for="file">文件名：</label>
    <input type="file" name="file" id="file"><br>
    <input type="submit" name="submit" value="提交">
</form>

</body>
</html>
```


将以上代码保存到 form.html 文件中。


有关上面的 HTML 表单的一些注意项列举如下：


- **** 标签的 **enctype** 属性规定了在提交表单时要使用哪种内容类型。在表单需要二进制数据时，比如文件内容，请使用 "**multipart/form-data**"。
- ***** 标签的 **type="file"** 属性规定了应该把输入作为文件来处理。举例来说，当在浏览器中预览时，会看到输入框旁边有一个浏览按钮。


**注释：**允许用户上传文件是一个巨大的安全风险。请仅仅允许可信的用户执行文件上传操作。


---


## 创建上传脚本


"upload_file.php" 文件含有供上传文件的代码：


```
<?php
if ($_FILES["file"]["error"] > 0)
{
    echo "错误：" . $_FILES["file"]["error"] . "<br>";
}
else
{
    echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
    echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
    echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
    echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"];
}
?>
```


通过使用 PHP 的全局数组 $_FILES，你可以从客户计算机向远程服务器上传文件。


第一个参数是表单的 input name，第二个下标可以是 "name"、"type"、"size"、"tmp_name" 或 "error"。如下所示：


- $_FILES["file"]["name"] - 上传文件的名称
- $_FILES["file"]["type"] - 上传文件的类型
- $_FILES["file"]["size"] - 上传文件的大小，以字节计
- $_FILES["file"]["tmp_name"] - 存储在服务器的文件的临时副本的名称
- $_FILES["file"]["error"] - 由文件上传导致的错误代码


这是一种非常简单文件上传方式。基于安全方面的考虑，您应当增加有关允许哪些用户上传文件的限制。


---


## 上传限制


在这个脚本中，我们增加了对文件上传的限制。用户只能上传 .gif、.jpeg、.jpg、.png 文件，文件大小必须小于 200 kB：


```
<?php
// 允许上传的图片后缀
$allowedExts = array("gif", "jpeg", "jpg", "png");
$temp = explode(".", $_FILES["file"]["name"]);
$extension = end($temp);        // 获取文件后缀名
if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/jpg")
|| ($_FILES["file"]["type"] == "image/pjpeg")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "image/png"))
&& ($_FILES["file"]["size"] < 204800)    // 小于 200 kb
&& in_array($extension, $allowedExts))
{
    if ($_FILES["file"]["error"] > 0)
    {
        echo "错误：: " . $_FILES["file"]["error"] . "<br>";
    }
    else
    {
        echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
        echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
        echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
        echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"];
    }
}
else
{
    echo "非法的文件格式";
}
?>
```


---


## 保存被上传的文件


上面的实例在服务器的 PHP 临时文件夹中创建了一个被上传文件的临时副本。


这个临时的副本文件会在脚本结束时消失。要保存被上传的文件，我们需要把它拷贝到另外的位置：


```
<?php
// 允许上传的图片后缀
$allowedExts = array("gif", "jpeg", "jpg", "png");
$temp = explode(".", $_FILES["file"]["name"]);
echo $_FILES["file"]["size"];
$extension = end($temp);     // 获取文件后缀名
if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/jpg")
|| ($_FILES["file"]["type"] == "image/pjpeg")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "image/png"))
&& ($_FILES["file"]["size"] < 204800)   // 小于 200 kb
&& in_array($extension, $allowedExts))
{
    if ($_FILES["file"]["error"] > 0)
    {
        echo "错误：: " . $_FILES["file"]["error"] . "<br>";
    }
    else
    {
        echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
        echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
        echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
        echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"] . "<br>";

        // 判断当前目录下的 upload 目录是否存在该文件
        // 如果没有 upload 目录，你需要创建它，upload 目录权限为 777
        if (file_exists("upload/" . $_FILES["file"]["name"]))
        {
            echo $_FILES["file"]["name"] . " 文件已经存在。 ";
        }
        else
        {
            // 如果 upload 目录不存在该文件则将文件上传到 upload 目录下
            move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $_FILES["file"]["name"]);
            echo "文件存储在: " . "upload/" . $_FILES["file"]["name"];
        }
    }
}
else
{
    echo "非法的文件格式";
}
?>
```


上面的脚本检测了文件是否已存在，如果不存在，则把文件拷贝到名为 "upload" 的目录下。


文件上传演示操作如下所示：


![](https://www.runoob.com/wp-content/uploads/2013/08/upload-form.gif)








	  AI 思考中...





			* [PHP 文件](https://www.runoob.com/php-file.html)
			[PHP Cookie](https://www.runoob.com/php-cookies.html) **
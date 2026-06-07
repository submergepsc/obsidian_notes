# PHP 实例 - AJAX 投票

- Source: https://www.runoob.com/php/php-ajax-poll.html

---


## AJAX 投票


在下面的实例中，我们将演示一个投票程序，通过它，投票结果在网页不进行刷新的情况下被显示。


### 你喜欢 PHP 和 AJAX 吗?


是:
*
**
否:


---


## 实例解释 - HTML 页面


当用户选择上面的某个选项时，会执行名为 "getVote()" 的函数。该函数由 "onclick" 事件触发。


poll.html** 文件代码如下：


```
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
<script>
function getVote(int) {
  if (window.XMLHttpRequest) {
    // IE7+, Firefox, Chrome, Opera, Safari 执行代码
    xmlhttp=new XMLHttpRequest();
  } else {
    // IE6, IE5 执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
      document.getElementById("poll").innerHTML=xmlhttp.responseText;
    }
  }
  xmlhttp.open("GET","poll_vote.php?vote="+int,true);
  xmlhttp.send();
}
</script>
</head>
<body>

<div id="poll">
<h3>你喜欢 PHP 和 AJAX 吗?</h3>
<form>
是:
<input type="radio" name="vote" value="0" onclick="getVote(this.value)">
<br>否:
<input type="radio" name="vote" value="1" onclick="getVote(this.value)">
</form>
</div>

</body>
</html>
```


getVote() 函数会执行以下步骤：


- 创建 XMLHttpRequest 对象
- 创建在服务器响应就绪时执行的函数
- 向服务器上的文件发送请求
- 请注意添加到 URL 末端的参数（q）（包含下拉列表的内容）


---


## PHP 文件


上面这段通过 JavaScript 调用的服务器页面是名为 "**poll_vote.php**" 的 PHP 文件：


```
<?php
$vote = htmlspecialchars($_REQUEST['vote']);

// 获取文件中存储的数据
$filename = "poll_result.txt";
$content = file($filename);

// 将数据分割到数组中
$array = explode("||", $content[0]);
$yes = $array[0];
$no = $array[1];

if ($vote == 0)
{
  $yes = $yes + 1;
}

if ($vote == 1)
{
  $no = $no + 1;
}

// 插入投票数据
$insertvote = $yes."||".$no;
$fp = fopen($filename,"w");
fputs($fp,$insertvote);
fclose($fp);
?>

<h2>结果:</h2>
<table>
  <tr>
  <td>是:</td>
  <td>
  <span style="display: inline-block; background-color:green;
      width:<?php echo(100*round($yes/($no+$yes),2)); ?>px;
      height:20px;" ></span>
  <?php echo(100*round($yes/($no+$yes),2)); ?>%
  </td>
  </tr>
  <tr>
  <td>否:</td>
  <td>
  <span style="display: inline-block; background-color:red;
      width:<?php echo(100*round($no/($no+$yes),2)); ?>px;
      height:20px;"></span>
  <?php echo(100*round($no/($no+$yes),2)); ?>%
  </td>
  </tr>
</table>
```


当所选的值从 JavaScript 发送到 PHP 文件时，将发生：


- 获取 "poll_result.txt" 文件的内容
- 把文件内容放入变量，并向被选变量累加 1
- 把结果写入 "poll_result.txt" 文件
- 输出图形化的投票结果


---


## 文本文件


文本文件（**poll_result.txt**）中存储来自投票程序的数据。


它存储的数据如下所示：


```
3||4
```


第一个数字表示 "Yes" 的投票数，第二个数字表示 "No" 的投票数。


**注释：**请记得只允许您的 Web 服务器来编辑该文本文件。**不要**让其他人获得访问权，除了 Web 服务器 (PHP)。








	  AI 思考中...





			* [PHP 实例 AJAX RSS 阅读器](https://www.runoob.com/php-ajax-rss-reader.html)
			[PHP 5 Timezones](https://www.runoob.com/php-ref-timezones.html) **
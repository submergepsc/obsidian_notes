# PHP - AJAX 与 PHP

- Source: https://www.runoob.com/php/php-ajax-php.html

---


AJAX (Asynchronous JavaScript and XML) 是一种用于在不刷新整个页面的情况下，与服务器交换数据的技术。


AJAX 是一种在无需重新加载整个页面的情况下，能够更新部分网页的技术，它通过在后台与服务器交换数据，并能够更新部分网页内容。


AJAX 允许网页动态更新部分内容，提供更快的用户体验。

AJAX 通常使用 XMLHttpRequest 对象在后台与服务器进行通信，尽管它也可以使用 fetch API 等现代方法。


更多内容可以参考：[AJAX 教程](https://www.runoob.com/../ajax/ajax-tutorial.html)


### AJAX 的工作原理


- **发送请求**：用户通过某种方式（如点击按钮）触发 AJAX 请求。
- **创建请求**：JavaScript 创建一个 XMLHttpRequest 对象，用于与服务器进行通信。
- **发送请求**：通过 XMLHttpRequest 对象发送请求到服务器。
- **服务器处理**：服务器接收到请求后，进行数据处理。
- **返回响应**：服务器将处理结果返回给客户端。
- **更新页面**：JavaScript 接收到服务器的响应后，更新网页的相应部分。


### PHP 中使用 AJAX 的步骤

**1、前端：**JavaScript 发起 AJAX 请求。


使用 XMLHttpRequest 或 fetch 向 PHP 服务器发送请求。


**2、后端：**PHP 接收并处理请求。


PHP 获取 AJAX 请求的数据，并返回结果。


**3、前端：**处理 PHP 返回的数据。


使用 JavaScript 解析和显示从 PHP 接收到的响应数据。


![](https://www.runoob.com/wp-content/uploads/2013/08/ajax-php-request.png)


### 在 PHP 中使用 AJAX


**1、创建 HTML 和 JavaScript**：首先，你需要一个HTML页面和JavaScript代码来发送AJAX请求。


## 实例


```php
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>AJAX Example</title>
    <script>
        function sendRequest() {
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    document.getElementById("result").innerHTML = xhr.responseText;
                }
            };
            xhr.open("GET", "your_php_file.php?param=value", true);
            xhr.send();
        }
    </script>
</head>
<body>
    <button onclick="sendRequest()">Send AJAX Request</button>
    <div id="result"></div>
</body>
</html>
```


**2、编写PHP脚本：**在服务器端，你需要一个PHP文件来处理请求并返回数据。


## 实例


```php
<?php
if (isset($_GET['param'])) {
    // 处理请求参数
    $param = $_GET['param'];
    // 执行一些操作...
    // 返回响应
    echo "Received parameter: " . $param;
}
?>
```


**3、发送请求：**当用户点击按钮时，JavaScript 函数 sendRequest 会被调用，它创建一个 XMLHttpRequest 对象并发送请求到服务器。


**4、处理响应：**服务器处理请求后，将结果返回给客户端。客户端的 JavaScript 代码会检查响应状态，并在状态为 200（即请求成功）时更新页面内容。


---


## AJAX PHP 实例


下面的实例将演示当用户在输入框中键入字符时，网页如何与 Web 服务器进行通信：


## 实例


**尝试在输入框中输入一个名字，如：Anna:**



姓名: *


返回值:


**


---


## 实例解释 - HTML 页面


当用户在上面的输入框中键入字符时，会执行 "showHint()" 函数。该函数由 "onkeyup" 事件触发：



## 实例


```php
<html>
<head>
<script>
function showHint(str)
{
        if (str.length==0)
        {
                document.getElementById("txtHint").innerHTML="";
                return;
        }
        if (window.XMLHttpRequest)
        {
                // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行的代码
                xmlhttp=new XMLHttpRequest();
        }
        else
        {
                //IE6, IE5 浏览器执行的代码
                xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
        }
        xmlhttp.onreadystatechange=function()
        {
                if (xmlhttp.readyState==4 && xmlhttp.status==200)
                {
                        document.getElementById("txtHint").innerHTML=xmlhttp.responseText;
                }
        }
        xmlhttp.open("GET","gethint.php?q="+str,true);
        xmlhttp.send();
}
</script>
</head>
<body>

<p><b>在输入框中输入一个姓名:</b></p>
<form>
姓名: <input type="text" onkeyup="showHint(this.value)">
</form>
<p>返回值: <span id="txtHint"></span></p>

</body>
</html>
```


源代码解释：


如果输入框是空的（str.length==0），该函数会清空 txtHint 占位符的内容，并退出该函数。


如果输入框不是空的，那么 showHint() 会执行以下步骤：


- 创建 XMLHttpRequest 对象
- 创建在服务器响应就绪时执行的函数
- 向服务器上的文件发送请求
- 请注意添加到 URL 末端的参数（q）（包含输入框的内容）


上面这段通过 JavaScript 调用的服务器页面是名为 "gethint.php" 的 PHP 文件。


"gethint.php" 中的源代码会检查姓名数组，然后向浏览器返回对应的姓名：


## 实例


```php
<?php
// 将姓名填充到数组中
$a[]="Anna";
$a[]="Brittany";
$a[]="Cinderella";
$a[]="Diana";
$a[]="Eva";
$a[]="Fiona";
$a[]="Gunda";
$a[]="Hege";
$a[]="Inga";
$a[]="Johanna";
$a[]="Kitty";
$a[]="Linda";
$a[]="Nina";
$a[]="Ophelia";
$a[]="Petunia";
$a[]="Amanda";
$a[]="Raquel";
$a[]="Cindy";
$a[]="Doris";
$a[]="Eve";
$a[]="Evita";
$a[]="Sunniva";
$a[]="Tove";
$a[]="Unni";
$a[]="Violet";
$a[]="Liza";
$a[]="Elizabeth";
$a[]="Ellen";
$a[]="Wenche";
$a[]="Vicky";

//从请求URL地址中获取 q 参数
$q=$_GET["q"];

//查找是否由匹配值， 如果 q>0
if (strlen($q) > 0)
{
        $hint="";
        for($i=0; $i<count($a); $i++)
        {
                if (strtolower($q)==strtolower(substr($a[$i],0,strlen($q))))
                {
                        if ($hint=="")
                        {
                                $hint=$a[$i];
                        }
                        else
                        {
                                $hint=$hint." , ".$a[$i];
                        }
                }
        }
}

// 如果没有匹配值设置输出为 "no suggestion"
if ($hint == "")
{
        $response="no suggestion";
}
else
{
        $response=$hint;
}

//输出返回值
echo $response;
?>
```


解释：如果 JavaScript 发送了任何文本（即 strlen($q) > 0），则会发生：


- 查找匹配 JavaScript 发送的字符的姓名
- 如果未找到匹配，则将响应字符串设置为 "no suggestion"
- 如果找到一个或多个匹配姓名，则用所有姓名设置响应字符串
- 把响应发送到 "txtHint" 占位符

### 使用 fetch 和 PHP 实现 AJAX


HTML + JavaScript:


## 实例


```php
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AJAX with PHP Example</title>
</head>
<body>

<h1>AJAX Example</h1>
<button id="ajaxButton">Get Data from PHP</button>
<div id="result"></div>

<script>
    document.getElementById('ajaxButton').addEventListener('click', function() {
        // 发送 AJAX 请求
        fetch('server.php', {
            method: 'POST', // 使用 POST 请求
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: "Hello from client" })
        })
        .then(response => response.json()) // 解析为 JSON
        .then(data => {
            document.getElementById('result').innerHTML = data.response; // 更新页面
        })
        .catch(error => console.error('Error:', error));
    });
</script>

</body>
</html>
```


PHP 服务器 (server.php):


## 实例


```php
<?php
// 设置响应头以支持 JSON
header('Content-Type: application/json');

// 获取 AJAX 请求的输入数据
$request = json_decode(file_get_contents("php://input"), true);

// 处理数据并返回响应
if ($request['message'] === "Hello from client") {
    $response = array('response' => 'Hello from PHP server!');
} else {
    $response = array('response' => 'Invalid message');
}

// 将结果返回给客户端
echo json_encode($response);
?>
```


说明：**


- **前端**：当用户点击按钮时，JavaScript 使用 `fetch()` 发送一个 POST 请求到 `server.php`，并发送了一段 JSON 数据。
- **后端**：PHP 服务器读取客户端发送的请求，处理后返回一个 JSON 响应。
- **响应处理**：JavaScript 接收到 PHP 服务器的响应后，更新页面内容。


### PHP Ajax 跨域问题解决方案


如果你的异步请求需要跨域可以查看：[PHP Ajax 跨域问题解决方案](https://www.runoob.com/w3cnote/php-ajax-cross-border.html)。









	  AI 思考中...





			* [AJAX 简介](https://www.runoob.com/php-ajax-intro.html)
			[PHP 实例 AJAX 与 MySQL](https://www.runoob.com/php-ajax-database.html) **













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
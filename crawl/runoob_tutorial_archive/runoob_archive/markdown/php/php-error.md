# PHP 错误处理

- Source: https://www.runoob.com/php/php-error.html

---


在 PHP 中，默认的错误处理很简单。一条错误消息会被发送到浏览器，这条消息带有文件名、行号以及描述错误的消息。


---


## PHP 错误处理


在创建脚本和 Web 应用程序时，错误处理是一个重要的部分。如果您的代码缺少错误检测编码，那么程序看上去很不专业，也为安全风险敞开了大门。


本教程介绍了 PHP 中一些最为重要的错误检测方法。


我们将为您讲解不同的错误处理方法：


- 简单的 "die()" 语句
- 自定义错误和错误触发器
- 错误报告


---


## 基本的错误处理：使用 die() 函数


第一个实例展示了一个打开文本文件的简单脚本：


```
<?php
$file=fopen("welcome.txt","r");
?>
```


如果文件不存在，您会得到类似这样的错误：


```
Warning: fopen(welcome.txt) [function.fopen]: failed to open stream:
No such file or directory in /www/runoob/test/test.php on line 2
```


为了避免用户得到类似上面的错误消息，我们在访问文件之前检测该文件是否存在：


```
<?php
if(!file_exists("welcome.txt"))
{
    die("文件不存在");
}
else
{
    $file=fopen("welcome.txt","r");
}
?>
```


现在，如果文件不存在，您会得到类似这样的错误消息：


```
文件不存在
```


相比之前的代码，上面的代码更有效，这是由于它采用了一个简单的错误处理机制在错误之后终止了脚本。


然而，简单地终止脚本并不总是恰当的方式。让我们研究一下用于处理错误的备选的 PHP 函数。


---


## 创建自定义错误处理器


创建一个自定义的错误处理器非常简单。我们很简单地创建了一个专用函数，可以在 PHP 中发生错误时调用该函数。


该函数必须有能力处理至少两个参数 (error level 和 error message)，但是可以接受最多五个参数（可选的：file, line-number 和 error context）：


## 语法


```
error_function(error_level,error_message,
error_file,error_line,error_context)
```


| 参数 | 描述 |
| --- | --- |
| error_level | 必需。为用户定义的错误规定错误报告级别。必须是一个数字。参见下面的表格：错误报告级别。 |
| error_message | 必需。为用户定义的错误规定错误消息。 |
| error_file | 可选。规定错误发生的文件名。 |
| error_line | 可选。规定错误发生的行号。 |
| error_context | 可选。规定一个数组，包含了当错误发生时在用的每个变量以及它们的值。 |


## 错误报告级别


这些错误报告级别是用户自定义的错误处理程序处理的不同类型的错误：


| 值 | 常量 | 描述 |
| --- | --- | --- |
| 2 | E_WARNING | 非致命的 run-time 错误。不暂停脚本执行。 |
| 8 | E_NOTICE | run-time 通知。在脚本发现可能有错误时发生，但也可能在脚本正常运行时发生。 |
| 256 | E_USER_ERROR | 致命的用户生成的错误。这类似于程序员使用 PHP 函数 trigger_error() 设置的 E_ERROR。 |
| 512 | E_USER_WARNING | 非致命的用户生成的警告。这类似于程序员使用 PHP 函数 trigger_error() 设置的 E_WARNING。 |
| 1024 | E_USER_NOTICE | 用户生成的通知。这类似于程序员使用 PHP 函数 trigger_error() 设置的 E_NOTICE。 |
| 4096 | E_RECOVERABLE_ERROR | 可捕获的致命错误。类似 E_ERROR，但可被用户定义的处理程序捕获。（参见 set_error_handler()） |
| 8191 | E_ALL | 所有错误和警告。（在 PHP 5.4 中，E_STRICT 成为 E_ALL 的一部分） |


现在，让我们创建一个处理错误的函数：


```
function customError($errno, $errstr)
{
    echo "<b>Error:</b> [$errno] $errstr<br>";
    echo "脚本结束";
    die();
}
```


上面的代码是一个简单的错误处理函数。当它被触发时，它会取得错误级别和错误消息。然后它会输出错误级别和消息，并终止脚本。


现在，我们已经创建了一个错误处理函数，我们需要确定在何时触发该函数。


---


## 设置错误处理程序


PHP 的默认错误处理程序是内建的错误处理程序。我们打算把上面的函数改造为脚本运行期间的默认错误处理程序。


可以修改错误处理程序，使其仅应用到某些错误，这样脚本就能以不同的方式来处理不同的错误。然而，在本例中，我们打算针对所有错误来使用我们自定义的错误处理程序：


```
set_error_handler("customError");
```


由于我们希望我们的自定义函数能处理所有错误，set_error_handler() 仅需要一个参数，可以添加第二个参数来规定错误级别。


## 实例


通过尝试输出不存在的变量，来测试这个错误处理程序：


```
<?php
// 错误处理函数
function customError($errno, $errstr)
{
    echo "<b>Error:</b> [$errno] $errstr";
}

// 设置错误处理函数
set_error_handler("customError");

// 触发错误
echo($test);
?>
```


以上代码的输出如下所示：


```
Error: [8] Undefined variable: test
```


**
---


## 触发错误


在脚本中用户输入数据的位置，当用户的输入无效时触发错误是很有用的。在 PHP 中，这个任务由 trigger_error() 函数完成。


## 实例


在本例中，如果 "test" 变量大于 "1"，就会发生错误：


```
<?php
$test=2;
if ($test>1)
{
    trigger_error("变量值必须小于等于 1");
}
?>
```


以上代码的输出如下所示：


```
Notice: 变量值必须小于等于 1
in /www/test/runoob.php on line 5
```


您可以在脚本中任何位置触发错误，通过添加的第二个参数，您能够规定所触发的错误类型。


可能的错误类型：


- E_USER_ERROR - 致命的用户生成的 run-time 错误。错误无法恢复。脚本执行被中断。
- E_USER_WARNING - 非致命的用户生成的 run-time 警告。脚本执行不被中断。
- E_USER_NOTICE - 默认。用户生成的 run-time 通知。在脚本发现可能有错误时发生，但也可能在脚本正常运行时发生。


## 实例


在本例中，如果 "test" 变量大于 "1"，则发生 E_USER_WARNING 错误。如果发生了 E_USER_WARNING，我们将使用我们自定义的错误处理程序并结束脚本：


```
<?php
// 错误处理函数
function customError($errno, $errstr)
{
    echo "<b>Error:</b> [$errno] $errstr<br>";
    echo "脚本结束";
    die();
}

// 设置错误处理函数
set_error_handler("customError",E_USER_WARNING);

// 触发错误
$test=2;
if ($test>1)
{
    trigger_error("变量值必须小于等于 1",E_USER_WARNING);
}
?>
```


以上代码的输出如下所示：


```
Error: [512] 变量值必须小于等于 1
脚本结束
```


现在，我们已经学习了如何创建自己的 error，以及如何触发它们，接下来我们研究一下错误记录。


---


## 错误记录


在默认的情况下，根据在 php.ini 中的 error_log 配置，PHP 向服务器的记录系统或文件发送错误记录。通过使用 error_log() 函数，您可以向指定的文件或远程目的地发送错误记录。


通过电子邮件向您自己发送错误消息，是一种获得指定错误的通知的好办法。


## 通过 E-Mail 发送错误消息


在下面的例子中，如果特定的错误发生，我们将发送带有错误消息的电子邮件，并结束脚本：


```
<?php
// 错误处理函数
function customError($errno, $errstr)
{
    echo "<b>Error:</b> [$errno] $errstr<br>";
    echo "已通知网站管理员";
    error_log("Error: [$errno] $errstr",1,
    "[email protected]","From: [email protected]");
}

// 设置错误处理函数
set_error_handler("customError",E_USER_WARNING);

// 触发错误
$test=2;
if ($test>1)
{
    trigger_error("变量值必须小于等于 1",E_USER_WARNING);
}
?>
```


以上代码的输出如下所示：


```
Error: [512] 变量值必须小于等于 1
已通知网站管理员
```


接收自以上代码的邮件如下所示：


```
Error: [512] 变量值必须小于等于 1
```


这个方法不适合所有的错误。常规错误应当通过使用默认的 PHP 记录系统在服务器上进行记录。








	  AI 思考中...





			** [PHP 安全 E-mail](https://www.runoob.com/php-secure-mail.html)
			[PHP 异常处理](https://www.runoob.com/php-exception.html) **













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
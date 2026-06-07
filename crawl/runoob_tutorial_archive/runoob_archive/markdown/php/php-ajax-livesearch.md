# PHP 实例 - AJAX 实时搜索

- Source: https://www.runoob.com/php/php-ajax-livesearch.html

---


AJAX 可为用户提供更友好、交互性更强的搜索体验。


---


## AJAX Live Search


在下面的实例中，我们将演示一个实时的搜索，在您键入数据的同时即可得到搜索结果。


实时的搜索与传统的搜索相比，具有很多优势：


- 当键入数据时，就会显示出匹配的结果
- 当继续键入数据时，对结果进行过滤
- 如果结果太少，删除字符就可以获得更宽的范围


在下面的文本框中输入 "HTML"，搜索包含 HTML 的页面：


*


上面实例中的结果在一个 XML 文件（[links.xml](https://www.runoob.com/try/demo_source/links.xml)）中进行查找。为了让这个例子小而简单，我们只提供 6 个结果。


---


## 实例解释 - HTML 页面


当用户在上面的输入框中键入字符时，会执行 "showResult()" 函数。该函数由 "onkeyup" 事件触发：



```
<html>
<head>
<script>
function showResult(str)
{
    if (str.length==0)
    {
        document.getElementById("livesearch").innerHTML="";
        document.getElementById("livesearch").style.border="0px";
        return;
    }
    if (window.XMLHttpRequest)
    {// IE7+, Firefox, Chrome, Opera, Safari 浏览器执行
        xmlhttp=new XMLHttpRequest();
    }
    else
    {// IE6, IE5 浏览器执行
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            document.getElementById("livesearch").innerHTML=xmlhttp.responseText;
            document.getElementById("livesearch").style.border="1px solid #A5ACB2";
        }
    }
    xmlhttp.open("GET","livesearch.php?q="+str,true);
    xmlhttp.send();
}
</script>
</head>
<body>

<form>
<input type="text" size="30" onkeyup="showResult(this.value)">
<div id="livesearch"></div>
</form>

</body>
</html>
```


源代码解释：


如果输入框是空的（str.length==0），该函数会清空 livesearch 占位符的内容，并退出该函数。


如果输入框不是空的，那么 showResult() 会执行以下步骤：


- 创建 XMLHttpRequest 对象
- 创建在服务器响应就绪时执行的函数
- 向服务器上的文件发送请求
- 请注意添加到 URL 末端的参数（q）（包含输入框的内容）


---


## PHP 文件


上面这段通过 JavaScript 调用的服务器页面是名为 "livesearch.php" 的 PHP 文件。


"livesearch.php" 中的源代码会搜索 XML 文件中匹配搜索字符串的标题，并返回结果：


```
<?php
$xmlDoc=new DOMDocument();
$xmlDoc->load("links.xml");

$x=$xmlDoc->getElementsByTagName('link');

// 从 URL 中获取参数 q 的值
$q=$_GET["q"];

// 如果 q 参数存在则从 xml 文件中查找数据
if (strlen($q)>0)
{
    $hint="";
    for($i=0; $i<($x->length); $i++)
    {
        $y=$x->item($i)->getElementsByTagName('title');
        $z=$x->item($i)->getElementsByTagName('url');
        if ($y->item(0)->nodeType==1)
        {
            // 找到匹配搜索的链接
            if (stristr($y->item(0)->childNodes->item(0)->nodeValue,$q))
            {
                if ($hint=="")
                {
                    $hint="<a href='" .
                    $z->item(0)->childNodes->item(0)->nodeValue .
                    "' target='_blank'>" .
                    $y->item(0)->childNodes->item(0)->nodeValue . "</a>";
                }
                else
                {
                    $hint=$hint . "<br /><a href='" .
                    $z->item(0)->childNodes->item(0)->nodeValue .
                    "' target='_blank'>" .
                    $y->item(0)->childNodes->item(0)->nodeValue . "</a>";
                }
            }
        }
    }
}

// 如果没找到则返回 "no suggestion"
if ($hint=="")
{
    $response="no suggestion";
}
else
{
    $response=$hint;
}

// 输出结果
echo $response;
?>
```


如果 JavaScript 发送了任何文本（即 strlen($q) > 0），则会发生：


- 加载 XML 文件到新的 XML DOM 对象
- 遍历所有的  元素，以便找到匹配 JavaScript 所传文本
- 在 "$response" 变量中设置正确的 URL 和标题。如果找到多于一个匹配，所有的匹配都会添加到变量。
- 如果没有找到匹配，则把 $response 变量设置为 "no suggestion"。








	  AI 思考中...





			* [PHP 实例 AJAX 与 XML](https://www.runoob.com/php-ajax-xml.html)
			[PHP 实例 AJAX RSS 阅读器](https://www.runoob.com/php-ajax-rss-reader.html) **













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
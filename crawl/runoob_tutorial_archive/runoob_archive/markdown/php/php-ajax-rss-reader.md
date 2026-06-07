# PHP 实例 - AJAX RSS 阅读器

- Source: https://www.runoob.com/php/php-ajax-rss-reader.html

---


RSS 阅读器用于阅读 RSS Feed。


---


## AJAX RSS 阅读器


在下面的实例中，我们将演示一个 RSS 阅读器，通过它，来自 RSS 的内容在网页不进行刷新的情况下被载入：


选择一个 RSS-feed:
读取 RSS 数据


**RSS-feed 数据列表...

---


## 实例解释 - HTML 页面


当用户在上面的下拉列表中选择某个 RSS-feed 时，会执行名为 "showRSS()" 的函数。该函数由 "onchange" 事件触发：



## 实例


```php
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
<script>
function showRSS(str)
{
    if (str.length==0)
    {
        document.getElementById("rssOutput").innerHTML="";
        return;
        }
    if (window.XMLHttpRequest)
    {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp=new XMLHttpRequest();
    }
    else
    {
        // IE6, IE5 浏览器执行代码
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
        if (xmlhttp.readyState==4 && xmlhttp.status==200)
        {
            document.getElementById("rssOutput").innerHTML=xmlhttp.responseText;
        }
    }
    xmlhttp.open("GET","getrss.php?q="+str,true);
    xmlhttp.send();
}
</script>
</head>
<body>

<form>
<select onchange="showRSS(this.value)">
<option value="">选择一个 RSS-feed:</option>
<option value="rss">读取 RSS 数据</option>
</select>
</form>
<br>
<div id="rssOutput">RSS-feed 数据列表...</div>
</body>
</html>
```


showRSS() 函数会执行以下步骤：


- 检查是否有 RSS-feed 被选择
- 创建 XMLHttpRequest 对象
- 创建在服务器响应就绪时执行的函数
- 向服务器上的文件发送请求
- 请注意添加到 URL 末端的参数（q）（包含下拉列表的内容）


---


## PHP 文件


文件 [rss_demo.xml](https://www.runoob.com/try/demo_source/rss_demo.xml)。


上面这段通过 JavaScript 调用的服务器页面是名为 "getrss.php" 的 PHP 文件：


## 实例


```php
<?php
// rss 文件
$xml="rss_demo.xml";

$xmlDoc = new DOMDocument();
$xmlDoc->load($xml);

// 从 "<channel>" 中读取元素
$channel=$xmlDoc->getElementsByTagName('channel')->item(0);
$channel_title = $channel->getElementsByTagName('title')
->item(0)->childNodes->item(0)->nodeValue;
$channel_link = $channel->getElementsByTagName('link')
->item(0)->childNodes->item(0)->nodeValue;
$channel_desc = $channel->getElementsByTagName('description')
->item(0)->childNodes->item(0)->nodeValue;

// 输出 "<channel>" 中的元素
echo("<p><a href='" . $channel_link
  . "'>" . $channel_title . "</a>");
echo("<br>");
echo($channel_desc . "</p>");

// 输出 "<item>" 中的元素
$x=$xmlDoc->getElementsByTagName('item');
for ($i=0; $i<=1; $i++) {
    $item_title=$x->item($i)->getElementsByTagName('title')
    ->item(0)->childNodes->item(0)->nodeValue;
    $item_link=$x->item($i)->getElementsByTagName('link')
    ->item(0)->childNodes->item(0)->nodeValue;
    $item_desc=$x->item($i)->getElementsByTagName('description')
    ->item(0)->childNodes->item(0)->nodeValue;
    echo ("<p><a href='" . $item_link
    . "'>" . $item_title . "</a>");
    echo ("<br>");
    echo ($item_desc . "</p>");
}
?>
```


当 RSS feed 的请求从 JavaScript 发送到 PHP 文件时，将发生：


- 检查哪个 RSS feed 被选中
- 创建一个新的 XML DOM 对象
- 在 xml 变量中加载 RSS 文档
- 从 channel 元素中提取并输出元素
- 从 item 元素中提取并输出元素








	  AI 思考中...





			** [PHP 实例 AJAX 实时搜索](https://www.runoob.com/php-ajax-livesearch.html)
			[PHP 实例 AJAX 投票](https://www.runoob.com/php-ajax-poll.html) **













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
# PHP 高级过滤器

- Source: https://www.runoob.com/php/php-filter-advanced.html

---


## 检测一个数字是否在一个范围内


以下实例使用了 filter_var() 函数来检测一个 INT 型的变量是否在 1 到 200 内:


## 实例


```php
<?php
$int = 122;
$min = 1;
$max = 200;

if (filter_var($int, FILTER_VALIDATE_INT, array("options" => array("min_range"=>$min, "max_range"=>$max))) === false) {
    echo("变量值不在合法范围内");
} else {
    echo("变量值在合法范围内");
}
?>
```


**[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=demo_filter_adv1&type=php)


---


## 检测 IPv6 地址


以下实例使用了 filter_var() 函数来检测一个 $ip 变量是否是 IPv6 地址:


## 实例


```php
<?php
$ip = "2001:0db8:85a3:08d3:1319:8a2e:0370:7334";

if (!filter_var($ip, FILTER_VALIDATE_IP, FILTER_FLAG_IPV6) === false) {
    echo("$ip 是一个 IPv6 地址");
} else {
    echo("$ip 不是一个 IPv6 地址");
}
```


[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=demo_filter_adv2&type=php)


---


## 检测 URL - 必须包含QUERY_STRING（查询字符串）


以下实例使用了 filter_var() 函数来检测 $url 是否包含查询字符串：


## 实例


```php
<?php
$url = "http://www.runoob.com";

if (!filter_var($url, FILTER_VALIDATE_URL, FILTER_FLAG_QUERY_REQUIRED) === false) {
    echo("$url 是一个合法的 URL");
} else {
    echo("$url 不是一个合法的 URL");
}

?>
```


[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=demo_filter_adv3&type=php)


---


## 移除 ASCII 值大于 127 的字符


以下实例使用了 filter_var() 函数来移除字符串中 ASCII 值大于 127 的字符，同样它也能移除 HTML 标签：


## 实例


```php
<?php
$str = "<h1>Hello WorldÆØÅ!</h1>";

$newstr = filter_var($str, FILTER_SANITIZE_STRING, FILTER_FLAG_STRIP_HIGH);
echo $newstr;
?>
```


[尝试一下 »](https://www.runoob.com/try/runcode.php?filename=demo_filter_adv4&type=php)


---


## PHP 过滤器参考手册


你也可以通过访问本站的 [PHP 过滤器参考手册](https://www.runoob.com/php-ref-filter.html) 来查看过滤器的具体应用。


参考手册中包含了过滤器参数的简要说明和使用例子！









	  AI 思考中...





			** [PHP imagecolortransparent – 将某个颜色定义为透明色](https://www.runoob.com/php-imagecolortransparent.html)
			[PHP RESTful](https://www.runoob.com/php-restful.html) **













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
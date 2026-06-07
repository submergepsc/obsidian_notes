# PHP array_walk_recursive() 函数

- Source: https://www.runoob.com/php/func-array-walk-recursive.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


对数组中的每个元素应用用户自定义函数：


```php
<?php
	function myfunction($value,$key){echo "The key $key has the value
	$value<br>";}$a1=array("a"=>"red","b"=>"green");
	$a2=array($a1,"1"=>"blue","2"=>"yellow");array_walk_recursive($a2,"myfunction");
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_walk_recursive)


---


## 定义和用法


array_walk_recursive() 函数对数组中的每个元素应用用户自定义函数。在函数中，数组的键名和键值是参数。该函数与 [array_walk()](https://www.runoob.com/func-array-walk.html) 函数的不同在于可以操作更深的数组（一个数组中包含另一个数组）。


---


## 语法


array_walk_recursive(*array,myfunction,parameter...*)


| 参数 | 描述 |
| --- | --- |
| array | 必需。规定数组。 |
| myfunction | 必需。用户自定义函数的名称。 |
| parameter,... | 可选。规定用户自定义函数的参数，您可以为函数设置一个或多个参数。 |


## 技术细节


| 返回值： | 如果成功则返回 TRUE，否则返回 FALSE。 |
| --- | --- |
| PHP 版本： | 5+ |


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_walk() 函数](https://www.runoob.com/func-array-walk.html)
			[PHP arsort() 函数](https://www.runoob.com/func-array-arsort.html) **













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
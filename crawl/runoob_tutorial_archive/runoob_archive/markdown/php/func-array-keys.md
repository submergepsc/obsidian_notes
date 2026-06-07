# PHP array_keys() 函数

- Source: https://www.runoob.com/php/func-array-keys.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


返回包含数组中所有键名的一个新数组：


```php
<?php
	$a=array("Volvo"=>"XC90","BMW"=>"X5","Toyota"=>"Highlander");print_r(array_keys($a));
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_keys)


---


## 定义和用法


array_keys() 函数返回包含数组中所有键名的一个新数组。


---


## 语法


array_keys(*array,value,strict*)


| 参数 | 描述 |
| --- | --- |
| array | 必需。规定数组。 |
| value | 可选。您可以指定键值，然后只有该键值对应的键名会被返回。 |
| strict | 可选。与 value 参数一起使用。可能的值： true - 返回带有指定键值的键名。依赖类型，数字 5 与字符串 "5" 是不同的。 false - 默认值。不依赖类型，数字 5 与字符串 "5" 是相同的。 |


## 技术细节


| 返回值： | 返回包含数组中所有键名的一个新数组。 |
| --- | --- |
| PHP 版本： | 4+ |
| 更新日志： | strict 参数是在 PHP 5.0 中新增的。 |


---


## 更多实例


## 实例 1


使用 value 参数：


```php
<?php
	$a=array("Volvo"=>"XC90","BMW"=>"X5","Toyota"=>"Highlander");print_r(array_keys($a,"Highlander"));?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_keys2)


## 实例 2


使用 strict 参数 (false)：


```php
<?php
	$a=array(10,20,30,"10");print_r(array_keys($a,"10",false));?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_keys3)


## 实例 3


使用 strict 参数 (true)：


```php
<?php$a=array(10,20,30,"10");print_r(array_keys($a,"10",true));?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_keys4)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_key_exists() 函数](https://www.runoob.com/func-array-key-exists.html)
			[PHP array_map() 函数](https://www.runoob.com/func-array-map.html) **













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
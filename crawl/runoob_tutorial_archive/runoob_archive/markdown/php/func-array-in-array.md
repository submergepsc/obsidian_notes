# PHP in_array() 函数

- Source: https://www.runoob.com/php/func-array-in-array.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


在数组中搜索值 "Runoob" ，并输出一些文本：


```php
<?php
$sites = array("Google", "Runoob", "Taobao", "Facebook");

if (in_array("Runoob", $sites))
{
    echo "找到匹配项！";
}
else
{
    echo "没有找到匹配项！";
}
?>
```


**[运行实例 »](https://www.runoob.com/try/runcode.php?filename=demo_func_in_array&type=php)


---


## 定义和用法


in_array() 函数搜索数组中是否存在指定的值。

---


## 语法


```
bool in_array ( mixed $needle , array $haystack [, bool $strict = FALSE ] )
```


| 参数 | 描述 |
| --- | --- |
| needle | 必需。规定要在数组搜索的值。 |
| haystack | 必需。规定要搜索的数组。 |
| strict | 可选。如果该参数设置为 TRUE，则 in_array() 函数检查搜索的数据与数组的值的类型是否相同。 |


## 技术细节


| 返回值： | 如果在数组中找到值则返回 TRUE，否则返回 FALSE。 |
| --- | --- |
| PHP 版本： | 4+ |
| 更新日志 | 自 PHP 4.2 起，search 参数可以是一个数组。 |


---


## 更多实例


## 实例 1


使用所有的参数：


```php
<?php
$people = array("Peter", "Joe", "Glenn", "Cleveland", 23);

if (in_array("23", $people, TRUE))
{
    echo "Match found<br>";
}
else
{
    echo "Match not found<br>";
}
if (in_array("Glenn",$people, TRUE))
{
    echo "Match found<br>";
}
else
{
    echo "Match not found<br>";
}

if (in_array(23,$people, TRUE))
{
    echo "Match found<br>";
}
else
{
    echo "Match not found<br>";
}
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_in_array2)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP extract() 函数](https://www.runoob.com/func-array-extract.html)
			[PHP key() 函数](https://www.runoob.com/func-array-key.html) **













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
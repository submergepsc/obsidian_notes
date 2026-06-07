# PHP array_shift() 函数

- Source: https://www.runoob.com/php/func-array-shift.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


删除数组中的第一个元素（red），并返回被删除的元素：


```php
<?php
$a=array("a"=>"red","b"=>"green","c"=>"blue");
echo array_shift($a);
print_r ($a);
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_shift)


---


## 定义和用法


array_shift() 函数用于删除数组中的第一个元素，并返回被删除的元素。


注释：**如果键名是数字的，所有元素都将获得新的键名，从 0 开始，并以 1 递增（参见下面实例）。


---


## 语法


array_shift(*array*)

**
| 参数 | 描述 |
| --- | --- |
| array | 必需。规定数组。 |


## 技术细节


| 返回值： | 返回从数组中删除元素的值，如果数组为空则返回 NULL。 |
| --- | --- |
| PHP 版本： | 4+ |


---


## 更多实例


## 实例 1


使用数字键名，所有元素都将获得新的键名：


```php
<?php
$a=array(0=>"red",1=>"green",2=>"blue");
echo array_shift($a);
print_r ($a);
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_shift2)


如果要保留数字键的索引可以使用以下方法：


## 实例


```php
<?php
$arr = array('1'=>1,'2'=>2,'3'=>'3');

function array_kshift(&$arr)
{
  list($k) = array_keys($arr);
  $r  = array($k=>$arr[$k]);
  unset($arr[$k]);
  return $r;
}
array_kshift($arr);
print_r($arr);
?>
```


以上实例输出结果为：


```
Array
(
    [2] => 2
    [3] => 3
)
```


> 更多内容：[PHP 删除数组的第一个元素](https://www.runoob.com/func-array-shift.html)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_search() 函数](https://www.runoob.com/func-array-search.html)
			[PHP array_slice() 函数](https://www.runoob.com/func-array-slice.html) **













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
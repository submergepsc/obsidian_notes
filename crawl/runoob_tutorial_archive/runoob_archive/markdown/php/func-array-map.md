# PHP array_map() 函数

- Source: https://www.runoob.com/php/func-array-map.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


将函数作用到数组中的每个值上，每个值都乘以本身，并返回带有新的值的数组：


```php
<?php
function myfunction($num)
{
   return($num*$num);
}

$a=array(1,2,3,4,5);
print_r(array_map("myfunction",$a));
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_map)


---


## 定义和用法


array_map() 函数将用户自定义函数作用到数组中的每个值上，并返回用户自定义函数作用后的带有新的值的数组。


提示：**您可以向函数输入一个或者多个数组。


---


## 语法


array_map(*myfunction,array1,array2,array3*...)

**
| 参数 | 描述 |
| --- | --- |
| myfunction | 必需。用户自定义函数的名称，或者是 null。 |
| array1 | 必需。规定数组。 |
| array2 | 可选。规定数组。 |
| array3 | 可选。规定数组。 |


## 技术细节


| 返回值： | 返回包含用户自定义函数作用后的 array1 的值的数组。 |
| --- | --- |
| PHP 版本： | 4.0.6+ |


---


## 更多实例


## 实例 1


使用一个用户自定义函数来改变数组的值：


```php
<?php
function myfunction($v)
{
    if ($v==="Dog")
    {
        return "Fido";
    }
    return $v;
}

$a=array("Horse","Dog","Cat");
print_r(array_map("myfunction",$a));
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_map2)


## 实例 2


使用两个数组：


```php
<?php
function myfunction($v1,$v2)
{
    if ($v1===$v2)
    {
       return "same";
    }
    return "different";
}

$a1=array("Horse","Dog","Cat");
$a2=array("Cow","Dog","Rat");
print_r(array_map("myfunction",$a1,$a2));
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_map3)


## 实例 3


将数组中值的所有字母改为大写：


```php
<?php
function myfunction($v)
{
    $v=strtoupper($v);
    return $v;
}

$a=array("Animal" => "horse", "Type" => "mammal");
print_r(array_map("myfunction",$a));
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_map4)


## 实例 4


将函数名赋值为 null 时：


```php
<?php
$a1=array("Dog","Cat");
$a2=array("Puppy","Kitten");
print_r(array_map(null,$a1,$a2));
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_map5)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_keys() 函数](https://www.runoob.com/func-array-keys.html)
			[PHP array_merge() 函数](https://www.runoob.com/func-array-merge.html) **













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
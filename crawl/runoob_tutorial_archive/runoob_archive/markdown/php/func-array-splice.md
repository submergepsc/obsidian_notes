# PHP array_splice() 函数

- Source: https://www.runoob.com/php/func-array-splice.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


从数组中移除元素，并用新元素取代它：


```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow");
$a2=array("a"=>"purple","b"=>"orange");
array_splice($a1,0,2,$a2);
print_r($a1);
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_splice)


---


## 定义和用法


array_splice() 函数从数组中移除选定的元素，并用新元素取代它。函数也将返回被移除元素的数组。


提示：**如果函数没有移除任何元素（length=0），则替代数组将从 start 参数的位置插入（参见实例 2）。


**注释：**不保留替代数组中的键名。


---


## 语法


array_splice(*array1,start,length,array2*)

**
| 参数 | 描述 |
| --- | --- |
| array1 | 必需。规定数组。 |
| start | 必需。数值。规定删除元素的开始位置。 0 = 第一个元素。 如果该值设置为正数，则从数组中该值指定的偏移量开始移除。如果该值设置为负数，则从数组末端倒数该值指定的偏移量开始移除。 -2 意味着从数组的倒数第二个元素开始。 |
| length | 可选。数值。规定被移除的元素个数，也是被返回数组的长度。 如果该值设置为正数，则移除该数量的元素。如果该值设置为负数，则移除从 start 到数组末端倒数 length 为止中间所有的元素。如果该值未设置，则移除从 start 参数设置的位置开始直到数组末端的所有元素。 |
| array2 | 可选。规定带有要插入原始数组中元素的数组。如果只有一个元素，则可以设置为字符串，不需要设置为数组。 |


## 技术细节


| 返回值： | 返回包含被提取元素的数组。 |
| --- | --- |
| PHP 版本： | 4+ |


---


## 更多实例


## 实例 1


与本页前面部分的实例相同，但是输出返回的数组：


```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow");
$a2=array("a"=>"purple","b"=>"orange");
print_r(array_splice($a1,0,2,$a2));
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_splice2)


## 实例 2


带有设置为 0 的 length 参数：


```php
<?php
$a1=array("0"=>"red","1"=>"green");
$a2=array("0"=>"purple","1"=>"orange");
array_splice($a1,1,0,$a2);
print_r($a1);
?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_splice3)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_slice() 函数](https://www.runoob.com/func-array-slice.html)
			[PHP array_sum() 函数](https://www.runoob.com/func-array-sum.html) **













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
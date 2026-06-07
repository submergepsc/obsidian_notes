# PHP array_chunk() 函数

- Source: https://www.runoob.com/php/func-array-chunk.html

[![PHP Array 参考手册](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


把数组分割为带有两个元素的数组块：


```php
<?php
$cars=array("Volvo","BMW","Toyota","Honda","Mercedes","Opel");
	print_r(array_chunk($cars,2));?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_chunk)


---


## 定义和用法


array_chunk() 函数把一个数组分割为新的数组块。


---


## 语法


array_chunk(*array*,*size*,*preserve_keys*);


| 参数 | 描述 |
| --- | --- |
| array | 必需。规定要使用的数组。 |
| size | 必需。一个整数，规定每个新数组块包含多少个元素。 |
| preserve_key | 可选。可能的值： true - 保留原始数组中的键名。 false - 默认。每个新数组块使用从零开始的索引。 |


## 技术细节


| 返回值： | 返回一个多维的数值数组，从 0 开始，每个维度都包含 size 元素。 |
| --- | --- |
| PHP 版本： | 4.2+ |


---


## 更多实例


## 实例 1


把数组分割为带有两个元素的数组块，并保留原始数组中的键名：


```php
<?php
	$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43","Harry"=>"50");print_r(array_chunk($age,2,true));?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_chunk2)


---

[![PHP Array 参考手册](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_change_key_case() 函数](https://www.runoob.com/func-array-change-key-case.html)
			[PHP array_combine() 函数](https://www.runoob.com/func-array-combine.html) **













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
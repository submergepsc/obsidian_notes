# PHP array_column() 函数

- Source: https://www.runoob.com/php/func-array-column.html

[![PHP Array 参考手册](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


从记录集中取出 last_name 列：


```php
<?php// 可能从数据库中返回数组$a = array(  array(    'id' => 5698,
	'first_name' => 'Peter',    'last_name' => 'Griffin',
	),  array(    'id' => 4767,
	'first_name' => 'Ben',    'last_name' => 'Smith',
	),  array(    'id' => 3809,
	'first_name' => 'Joe',    'last_name' => 'Doe',
	));$last_names =
	array_column($a, 'last_name');print_r($last_names);?>
```


输出：


```php
Array(  [0] => Griffin
	[1] => Smith  [2] => Doe)
```


**


---


## 定义和用法


array_column() 返回输入数组中某个单一列的值。


---


## 语法


array_column(*array*,*column_key*,*index_key*);


| 参数 | 描述 |
| --- | --- |
| array | 必需。指定要使用的多维数组（记录集）。 |
| column_key | 必需。需要返回值的列。可以是索引数组的列的整数索引，或者是关联数组的列的字符串键值。该参数也可以是 NULL，此时将返回整个数组（配合index_key 参数来重置数组键的时候，非常管用）。 |
| index_key | 可选。作为返回数组的索引/键的列。 |


## 技术细节


| 返回值： | 返回一个数组，数组的值为输入数组中某个单一列的值。 |
| --- | --- |
| PHP 版本： | 5.5+ |


---


## 更多实例


## 实例 1


从记录集中取出 last_name 列，用相应的 "id" 列作为键值：


```php
<?php// 可能从数据库中返回数组$a = array(  array(    'id' => 5698,
	'first_name' => 'Peter',    'last_name' => 'Griffin',
	),  array(    'id' => 4767,
	'first_name' => 'Ben',    'last_name' => 'Smith',
	),  array(    'id' => 3809,
	'first_name' => 'Joe',    'last_name' => 'Doe',
	));$last_names = array_column($a, 'last_name', 'id');print_r($last_names);
	?>
```


输出：


```php
Array(  [5698] => Griffin
	[4767] => Smith  [3809] => Doe)
```


---

[![PHP Array 参考手册](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)








	  AI 思考中...





			** [PHP 表单验证](https://www.runoob.com/php-form-validation.html)
			[PHP array_replace() 函数](https://www.runoob.com/func-array-replace.html) **













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
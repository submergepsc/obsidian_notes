# PHP array_unique() 函数

- Source: https://www.runoob.com/php/func-array-unique.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


移除数组中重复的值：


```php
<?php
	$a=array("a"=>"red","b"=>"green","c"=>"red");print_r(array_unique($a));
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_array_unique)


---


## 定义和用法


array_unique() 函数用于移除数组中重复的值。如果两个或更多个数组值相同，只保留第一个值，其他的值被移除。


注释：**被保留的数组将保持**第一个**数组项的键名类型。


---


## 语法


array_unique(*array*)

**
| 参数 | 描述 |
| --- | --- |
| array | 必需。规定数组。 |
| sortingtype | 可选。规定排序类型。可能的值： SORT_STRING - 默认。把每一项作为字符串来处理。 SORT_REGULAR - 把每一项按常规顺序排列（Standard ASCII，不改变类型）。 SORT_NUMERIC - 把每一项作为数字来处理。 SORT_LOCALE_STRING - 把每一项作为字符串来处理，基于当前区域设置（可通过 setlocale() 进行更改）。 |


## 技术细节


| 返回值： | 返回过滤后的数组。 |
| --- | --- |
| PHP 版本： | 4.0.1+ |
| 更新日志： | 在 PHP 5.2.10 中，sortingtype 的默认值改回 SORT_STRING。在 PHP 5.2.9 中，sortingtype 的默认值改为 SORT_REGULAR。在这之前的版本，sortingtype 的默认值为 SORT_STRING。 |


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP array_uintersect_uassoc() 函数](https://www.runoob.com/func-array-uintersect-uassoc.html)
			[PHP array_unshift() 函数](https://www.runoob.com/func-array-unshift.html) **













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
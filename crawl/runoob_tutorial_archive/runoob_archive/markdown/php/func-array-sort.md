# PHP sort() 函数

- Source: https://www.runoob.com/php/func-array-sort.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


对数组 $cars 中的元素按字母进行升序排序：


```php
<?php
$cars=array("Volvo","BMW","Toyota");
sort($cars);
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_sort)


---


## 定义和用法


sort() 函数对数值数组进行升序排序。


提示：**请使用 [rsort()](https://www.runoob.com/func-array-rsort.html) 函数对数值数组进行降序排序。


## 语法


sort(*array,sortingtype*);

**
| 参数 | 描述 |
| --- | --- |
| array | 必需。规定要进行排序的数组。 |
| sortingtype | 可选。规定如何排列数组的元素/项目。可能的值： 0 = SORT_REGULAR - 默认。把每一项按常规顺序排列（Standard ASCII，不改变类型）。 1 = SORT_NUMERIC - 把每一项作为数字来处理。 2 = SORT_STRING - 把每一项作为字符串来处理。 3 = SORT_LOCALE_STRING - 把每一项作为字符串来处理，基于当前区域设置（可通过 setlocale() 进行更改）。 4 = SORT_NATURAL - 把每一项作为字符串来处理，使用类似 natsort() 的自然排序。 5 = SORT_FLAG_CASE - 可以结合（按位或）SORT_STRING 或 SORT_NATURAL 对字符串进行排序，不区分大小写。 |


## 技术细节


| 返回值： | 如果成功则返回 TRUE，如果失败则返回 FALSE。 |
| --- | --- |
| PHP 版本： | 4+ |


---


## 更多实例


## 实例 1


对数组 $numbers 中的元素按数字进行升序排序：


```php
<?php
	$numbers=array(4,6,2,22,11);sort($numbers);?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_sort2)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP sizeof() 函数](https://www.runoob.com/func-array-sizeof.html)
			[PHP uasort() 函数](https://www.runoob.com/func-array-uasort.html) **













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
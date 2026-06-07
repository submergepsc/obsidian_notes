# PHP range() 函数

- Source: https://www.runoob.com/php/func-array-range.html

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)


## 实例


创建一个包含从 "0" 到 "5" 之间的元素的数组：


```php
<?php
$number = range(0,5);
print_r ($number);
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_range)


---


## 定义和用法


range() 函数创建一个包含指定范围的元素的数组。


该函数返回一个包含从 low 到 high 之间的元素的数组。


注释：**如果 low 参数大于 high 参数，则创建的数组将是从 high 到 low。


---


## 语法


range(*low,high,step*)

**
| 参数 | 描述 |
| --- | --- |
| low | 必需。规定数组元素的最小值。 |
| high | 必需。规定数组元素的最大值。 |
| step | 可选。规定元素之间的步进制。默认是 1。 |


## 技术细节


| 返回值： | 返回一个包含从 low 到 high 的元素的数组。 |
| --- | --- |
| PHP 版本： | 4+ |
| 更新日志： | step 参数是在 PHP 5.0 中新增的。在 PHP 4.1.0 到 4.3.2 版本中，该函数将数字字符串看作字符串而不是整数。数字字符串将被用于字符序列，例如，"5252" 被看作 "5"。支持字符序列和递减数组是在 PHP 4.1.0 中新增的。字符序列的值被限制在一个长度。如果长度大于一个，只使用第一个字符。在该版本之前，range() 只生成递增的整数数组。 |


---


## 更多实例


## 实例 1


返回一个包含从 "0" 到 "50" 之间并以 10 递增的元素的数组：


```php
<?php
$number = range(0,50,10);
print_r ($number);?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_range2)


## 实例 2


使用字母 - 返回一个包含从 "a" 到 "d" 之间的元素的数组：


```php
<?php
$letter = range("a","d");
print_r ($letter);?>
```


[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_func_range3)


---

[![PHP Array Reference](https://www.runoob.com/images/up.gif)完整的 PHP Array 参考手册](https://www.runoob.com/php-ref-array.html)







	  AI 思考中...





			** [PHP prev() 函数](https://www.runoob.com/func-array-prev.html)
			[PHP reset() 函数](https://www.runoob.com/func-array-reset.html) **













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
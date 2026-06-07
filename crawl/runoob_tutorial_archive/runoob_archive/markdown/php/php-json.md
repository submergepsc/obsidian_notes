# PHP JSON

- Source: https://www.runoob.com/php/php-json.html

本章节我们将为大家介绍如何使用 PHP 语言来编码和解码 JSON 对象。


---


## 环境配置


在 php5.2.0 及以上版本已经内置 JSON 扩展。


---


## JSON 函数


| 函数 | 描述 |
| --- | --- |
| json_encode | 对变量进行 JSON 编码 |
| json_decode | 对 JSON 格式的字符串进行解码，转换为 PHP 变量 |
| json_last_error | 返回最后发生的错误 |


---


## json_encode


PHP json_encode() 用于对变量进行 JSON 编码，该函数如果执行成功返回 JSON 数据，否则返回 FALSE 。


### 语法


```
string json_encode ( $value [, $options = 0 ] )
```


### 参数


- **value**: 要编码的值。该函数只对 UTF-8 编码的数据有效。
- **options**:由以下常量组成的二进制掩码 JSON_HEX_QUOT, JSON_HEX_TAG, JSON_HEX_AMP, JSON_HEX_APOS, JSON_NUMERIC_CHECK, JSON_PRETTY_PRINT, JSON_UNESCAPED_SLASHES, JSON_FORCE_OBJECT, JSON_PRESERVE_ZERO_FRACTION, JSON_UNESCAPED_UNICODE, JSON_PARTIAL_OUTPUT_ON_ERROR。 要注意的是 JSON_UNESCAPED_UNICODE 选项，如果我们不希望中文被编码，可以添加该选项。


### 实例


以下实例演示了如何将 PHP 数组转换为 JSON 格式数据：


```
<?php
   $arr = array('a' => 1, 'b' => 2, 'c' => 3, 'd' => 4, 'e' => 5);
   echo json_encode($arr);
?>
```


以上代码执行结果为：


```
{"a":1,"b":2,"c":3,"d":4,"e":5}
```


以下实例演示了如何将 PHP 对象转换为 JSON 格式数据：


## 实例


```php
<?php
   class Emp {
       public $name = "";
       public $hobbies  = "";
       public $birthdate = "";
   }
   $e = new Emp();
   $e->name = "sachin";
   $e->hobbies  = "sports";
   $e->birthdate = date('m/d/Y h:i:s a', "8/5/1974 12:20:03 p");
   $e->birthdate = date('m/d/Y h:i:s a', strtotime("8/5/1974 12:20:03"));

   echo json_encode($e);
?>
```


以上代码执行结果为：


```
{"name":"sachin","hobbies":"sports","birthdate":"08\/05\/1974 12:20:03 pm"}
```


## 使用 JSON_UNESCAPED_UNICODE 选项


```php
<?php
   $arr = array('runoob' => '菜鸟教程', 'taobao' => '淘宝网');
   echo json_encode($arr); // 编码中文
   echo PHP_EOL;  // 换行符
   echo json_encode($arr, JSON_UNESCAPED_UNICODE);  // 不编码中文
?>
```


以上代码执行结果为：


```
{"runoob":"\u83dc\u9e1f\u6559\u7a0b","taobao":"\u6dd8\u5b9d\u7f51"}
{"runoob":"菜鸟教程","taobao":"淘宝网"}
```


---


## json_decode


PHP json_decode() 函数用于对 JSON 格式的字符串进行解码，并转换为 PHP 变量。


### 语法


```
mixed json_decode ($json_string [,$assoc = false [, $depth = 512 [, $options = 0 ]]])
```


### 参数


- **json_string**: 待解码的 JSON 字符串，必须是 UTF-8 编码数据
- **assoc**: 当该参数为 TRUE 时，将返回数组，FALSE 时返回对象。
- **depth**: 整数类型的参数，它指定递归深度
- **options**: 二进制掩码，目前只支持 JSON_BIGINT_AS_STRING 。


### 实例


以下实例演示了如何解码 JSON 数据：


## 实例


```php
<?php
   $json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';

   var_dump(json_decode($json));
   var_dump(json_decode($json, true));
?>
```


以上代码执行结果为：


```
object(stdClass)#1 (5) {
    ["a"] => int(1)
    ["b"] => int(2)
    ["c"] => int(3)
    ["d"] => int(4)
    ["e"] => int(5)
}

array(5) {
    ["a"] => int(1)
    ["b"] => int(2)
    ["c"] => int(3)
    ["d"] => int(4)
    ["e"] => int(5)
}
```









	  AI 思考中...





			** [PHP 常量](https://www.runoob.com/php-constants.html)
			[PHP MySQL 插入多条数据](https://www.runoob.com/php-mysql-insert-multiple.html) **













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
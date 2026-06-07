# PHP 语法

- Source: https://www.runoob.com/php/php-syntax.html

---


PHP 脚本在服务器上执行，然后将纯 HTML 结果发送回浏览器。


PHP 使用 **** 包裹代码。


---


## 基本的 PHP 语法


PHP 脚本可以放在文档中的任何位置。


PHP 脚本以 **** 结束：


```
<?php
// PHP 代码
?>
```


PHP 文件的默认文件扩展名是 **.php**。


PHP 文件通常包含 HTML 标签和一些 PHP 脚本代码。


## 实例


```php
<?php
// PHP 代码写在 <?php 和 ?> 中间
echo "Hello, PHP!";
?>
```



- **** 是标准 PHP 标签。
- echo 用于输出内容。
- 每条语句末尾要加 **;**。


下面，我们提供了一个简单的 PHP 文件实例，它可以向浏览器输出文本 "Hello World!"：


```php
<!DOCTYPE html>
<html>
<body>

<h1>My first PHP page</h1>

<?php
echo "Hello World!";
?>

</body>
</html>
```


PHP 中的每个代码行都必须以分号结束。分号是一种分隔符，用于把指令集区分开来。


通过 PHP，有两种在浏览器输出文本的基础指令：**echo** 和 **print**。


---


## PHP 中的注释


在 PHP 中，注释用来解释代码的作用，不会被执行，也不会输出到页面上。


注释主要有三种形式：


### 1、单行注释（2 种写法）


使用 **//**


```
<?php
// 这是单行注释
echo "Hello"; // 也可以放在语句后面
?>
```


使用 **#**


```
<?php
# 这是另一种单行注释
echo "World";
?>
```


**特点：**


- 从 **//** 或 **#** 开始，到本行结束为止。
- 常用于简短说明。


### 2、多行注释（块注释）


使用 **/* ... */
```
<?php
/*
这是多行注释
可以写多行文字
不会被执行
*/
echo "PHP";
?>
```
 特点：


- 以 **/*** 开始，***/** 结束。
- 可以跨多行书写。
- 常用于较长的代码说明、函数注释等。


### 3、文档注释（DocBlock 注释）


这是多行注释的特殊形式，用于生成 API 文档，适合描述类、函数等。


```
<?php
/**
 * 打印问候语
 *
 * @param string $name 用户名
 * @return string 返回问候语
 */
function sayHello($name) {
    return "Hello, $name!";
}
?>
```


特点：


- 用 `/** ... */` 包裹（注意两个星号）
- 支持 @param、@return、@var、@author
- 常用于配合 IDE 或文档生成工具（如 phpDocumentor）


| 用途 | 推荐注释形式 | 示例 |
| --- | --- | --- |
| 简单说明一行代码 | // 或 # | // 输出信息 |
| 说明一段代码块 | /* ... */ | 用于逻辑分块的注释 |
| 函数/类文档说明 | /** ... */ DocBlock | 用于描述参数、返回值、用途等 |


## 实例


```php
<!DOCTYPE html>
<html>
<body><?php
// 这是 PHP 单行注释
/*
这是
PHP 多行
注释
*/
?>
</body>
</html>
```


**[运行实例 »](https://www.runoob.com/try/showphp2.php?filename=demo_syntax_comments)










	  AI 思考中...





			** [PHP 安装](https://www.runoob.com/php-install.html)
			[PHP 变量](https://www.runoob.com/php-variables.html) **













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
# PHP 循环 - While 循环

- Source: https://www.runoob.com/php/php-looping.html

---


循环执行代码块指定的次数，或者当指定的条件为真时循环执行代码块。


---


## PHP 循环


在您编写代码时，您经常需要让相同的代码块一次又一次地重复运行。我们可以在代码中使用循环语句来完成这个任务。


在 PHP 中，提供了下列循环语句：


- **while **- 只要指定的条件成立，则循环执行代码块
- **do...while** - 首先执行一次代码块，然后在指定的条件成立时重复这个循环
- **for **- 循环执行代码块指定的次数
- **foreach **- 根据数组中每个元素来循环代码块


---


## while 循环


while 循环将重复执行代码块，直到指定的条件不成立。


### 语法


```
while (条件)
{
    要执行的代码;
}
```


### 实例


下面的实例首先设置变量 *i* 的值为 1 ($i=1;)。


然后，只要 *i* 小于或者等于 5，while 循环将继续运行。循环每运行一次，*i* 就会递增 1：


```
<html>
<body>

<?php
$i=1;
while($i<=5)
{
    echo "The number is " . $i . "<br>";
    $i++;
}
?>

</body>
</html>
```


输出：


The number is 1**
The number is 2

The number is 3

The number is 4

The number is 5


---


## do...while 语句


do...while 语句会至少执行一次代码，然后检查条件，只要条件成立，就会重复进行循环。


### 语法


```
do
{
    要执行的代码;
}
while (条件);
```


### 实例


下面的实例首先设置变量 *i* 的值为 1 ($i=1;)。


然后，开始 do...while 循环。循环将变量 *i* 的值递增 1，然后输出。先检查条件（*i* 小于或者等于 5），只要 *i* 小于或者等于 5，循环将继续运行：


```
<html>
<body>

<?php
$i=1;
do
{
    $i++;
    echo "The number is " . $i . "<br>";
}
while ($i<=5);
?>

</body>
</html>
```


输出：


The number is 2

The number is 3

The number is 4

The number is 5

The number is 6


for 循环和 foreach 循环将在下一章进行讲解。








	  AI 思考中...





			** [PHP 数组排序](https://www.runoob.com/php-arrays-sort.html)
			[PHP For 循环](https://www.runoob.com/php-looping-for.html) **













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
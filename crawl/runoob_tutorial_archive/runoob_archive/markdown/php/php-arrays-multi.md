# PHP 多维数组

- Source: https://www.runoob.com/php/php-arrays-multi.html

---

多维数组是包含一个或多个数组的数组。


在多维数组中，主数组中的每一个元素也可以是一个数组，子数组中的每一个元素也可以是一个数组。


一个数组中的值可以是另一个数组，另一个数组的值也可以是一个数组，依照这种方式，我们可以创建二维或者三维数组。


二维数组语法格式：


```
array (
    array (elements...),
    array (elements...),
    ...
)
```


![](https://www.runoob.com/wp-content/uploads/2013/08/two-d.png)


以上数组的元素会自动分配键值，从 **0** 开始：


## 实例


```php
<?php
// 二维数组:
$cars = array
(
    array("Volvo",100,96),
    array("BMW",60,59),
    array("Toyota",110,100)
);
?>
```


**[运行实例 »](https://www.runoob.com/try/showphp.php?filename=demo_array_multi)


---


以下实例，我们创建了指定键（关联数组）的二维数组：


## 实例


```php
<?php
$sites = array
(
    "runoob"=>array
    (
        "菜鸟教程",
        "http://www.runoob.com"
    ),
    "google"=>array
    (
        "Google 搜索",
        "http://www.google.com"
    ),
    "taobao"=>array
    (
        "淘宝",
        "http://www.taobao.com"
    )
);
print("<pre>"); // 格式化输出数组
print_r($sites);
print("</pre>");
?>
```


上面的数组将输出如下：


![](https://www.runoob.com/wp-content/uploads/2013/08/198533EB-73EE-4AA7-8025-A6C0F778D4F0.jpg)


让我们试着显示上面数组中的某个值：


```
echo $sites['runoob'][0] . '地址为：' . $sites['runoob'][1];
```


上面的代码将输出：


![](https://www.runoob.com/wp-content/uploads/2013/08/11B02D8A-8855-4BCE-9DE9-5DA9BB4AE936.jpg)


---


## 三维数组

三维数组是在二维数组的基础上再嵌套一层数组，格式如下：


```
array (
    array (
        array (elements...),
        array (elements...),
        ...
    ),
    array (
        array (elements...),
        array (elements...),
        ...
    ),
    ...
)
```


![](https://www.runoob.com/wp-content/uploads/2013/08/3D-array.jpeg)


## 实例


```php
<?php
// 创建三维数组
$myarray = array(
    array(
        array(1, 2),
        array(3, 4),
    ),
    array(
        array(5, 6),
        array(7, 8),
    ),
);

// 输出数组信息
print_r($myarray);
?>
```


上面的数组将输出如下：


```
Array
(
    [0] => Array
        (
            [0] => Array
                (
                    [0] => 1
                    [1] => 2
                )

            [1] => Array
                (
                    [0] => 3
                    [1] => 4
                )

        )

    [1] => Array
        (
            [0] => Array
                (
                    [0] => 5
                    [1] => 6
                )

            [1] => Array
                (
                    [0] => 7
                    [1] => 8
                )

        )

)
```










	  AI 思考中...





			** [PHP $_POST 变量](https://www.runoob.com/php-post.html)
			[PHP date() 函数](https://www.runoob.com/php-date.html) **













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
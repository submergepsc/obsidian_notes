# PHP 图像处理

- Source: https://www.runoob.com/php/php-image-gd.html

PHP 提供了丰富的图像处理函数，主要包括：


| 函数 | 描述 |
| --- | --- |
| gd_info() | 取得当前安装的 GD 库的信息 |
| getimagesize() | 获取图像信息 |
| getimagesizefromstring() | 获取图像信息 |
| image_type_to_extension() | 获取图片后缀 |
| image_type_to_mime_type() | 返回图像的 MIME 类型 |
| image2wbmp() | 输出WBMP图片 |
| imageaffine() | 返回经过仿射变换后的图像 |
| imageaffinematrixconcat() | 连接两个矩阵 |
| imageaffinematrixget() | 获取矩阵 |
| imagealphablending() | 设定图像的混色模式 |
| imageantialias() | 是否使用抗锯齿（antialias）功能 |
| imagearc() | 画椭圆弧 |
| imagechar() | 写出横向字符 |
| imagecharup() | 垂直地画一个字符 |
| imagecolorallocate() | 为一幅图像分配颜色 |
| imagecolorallocatealpha() | 为一幅图像分配颜色和透明度 |
| imagecolorat() | 取得某像素的颜色索引值 |
| imagecolorclosest() | 取得与指定的颜色最接近的颜色的索引值 |
| imagecolorclosestalpha() | 取得与指定的颜色加透明度最接近的颜色的索引 |
| imagecolorclosesthwb() | 取得与指定的颜色最接近的色度的黑白色的索引 |
| imagesx() 、imagesy() | 获取图像宽度与高度 |


## GD 库


使用 PHP 图像处理函数，需要加载 GD 支持库。请确定 php.ini 加载了 GD 库： Window 服务器上：


```
extension = php_gd2.dll
```


Linux 和 Mac 系统上:


```
extension = php_gd2.so
```


使用 gd_info() 函数可以查看当前安装的 GD 库的信息：


```
<?php
var_dump(gd_info());
?>
```


输出大致如下：


```
array(12) {
  ["GD Version"]=>
  string(26) "bundled (2.1.0 compatible)"
  ["FreeType Support"]=>
  bool(true)
  ["FreeType Linkage"]=>
  string(13) "with freetype"
  ["T1Lib Support"]=>
  bool(false)
  ["GIF Read Support"]=>
  bool(true)
  ["GIF Create Support"]=>
  bool(true)
  ["JPEG Support"]=>
  bool(true)
  ["PNG Support"]=>
  bool(true)
  ["WBMP Support"]=>
  bool(true)
  ["XPM Support"]=>
  bool(false)
  ["XBM Support"]=>
  bool(true)
  ["JIS-mapped Japanese Font Support"]=>
  bool(false)
}
```









	  AI 思考中...





			** [PHP MySQL 预处理语句](https://www.runoob.com/php-mysql-prepared-statements.html)
			[php getimagesize 函数 – 获取图像信息](https://www.runoob.com/php-getimagesize.html) **













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
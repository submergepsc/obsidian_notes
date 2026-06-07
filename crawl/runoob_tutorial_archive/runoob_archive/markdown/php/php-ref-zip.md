# PHP Zip File 函数

- Source: https://www.runoob.com/php/php-ref-zip.html

---


## PHP Zip File 简介


Zip File 函数允许您读取压缩文件。


---


## 安装


如需在服务器上运行 Zip File 函数，必须安装这些库：


- Guido Draheim 的 ZZIPlib 库： [下载 ZZIPlib 库](http://zziplib.sourceforge.net/download.html)
- Zip PELC 扩展：[下载 Zip PELC 扩展](http://snaps.php.net/)


**在 Linux 系统上安装**


**PHP 5+：**Zip 函数和 Zip 库默认不会启用，必须从上面的链接下载。请使用 *--with-zip=DIR* 配置选项来包含 Zip 支持。


**在 Windows 系统上安装**


**PHP 5+：**Zip 函数默认不会启用，必须从上面的链接下载 php_zip.dll 和 ZZIPlib 库。必须在 php.ini 中启用 php_zip.dll。


如需启用任何 PHP 扩展，PHP extension_dir 设置（在 php.ini 文件中）应该设置为该 PHP 扩展所在的目录。举例 extension_dir 的值可能是 c:\php\ext。


---


## PHP Zip File 函数


**PHP**：指示支持该函数的最早的 PHP 版本。


| 函数 | 描述 | PHP |
| --- | --- | --- |
| zip_close() | 关闭 ZIP 文件。 | 4 |
| zip_entry_close() | 关闭 ZIP 文件中的一个项目。 | 4 |
| zip_entry_compressedsize() | 返回 ZIP 文件中的一个项目的被压缩尺寸。 | 4 |
| zip_entry_compressionmethod() | 返回 ZIP 文件中的一个项目的压缩方法。 | 4 |
| zip_entry_filesize() | 返回 ZIP 文件中的一个项目的实际文件尺寸。 | 4 |
| zip_entry_name() | 返回 ZIP 文件中的一个项目的名称。 | 4 |
| zip_entry_open() | 打开 ZIP 文件中的一个项目以供读取。 | 4 |
| zip_entry_read() | 读取 ZIP 文件中的一个打开的项目。 | 4 |
| zip_open() | 打开 ZIP 文件。 | 4 |
| zip_read() | 读取 ZIP 文件中的下一个项目。 | 4 |

**
---


## PHP Zip File 常量


无。








	  AI 思考中...





			** [PHP XML 函数](https://www.runoob.com/php-ref-xml.html)
			[PHP 教程](https://www.runoob.com/php-tutorial.html) **













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
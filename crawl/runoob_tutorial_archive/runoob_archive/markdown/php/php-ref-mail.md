# PHP Mail 函数

- Source: https://www.runoob.com/php/php-ref-mail.html

---


## PHP Mail 简介


mail() 函数允许您从脚本中直接发送电子邮件。


---


## 需求


要使邮件函数可用，PHP 需要已安装且正在运行的邮件系统。要使用的程序是由 php.ini 文件中的配置设置定义的。


---


## 安装


Mail 函数是 PHP 核心的组成部分。无需安装即可使用这些函数。


---


## Runtime 配置


Mail 函数的行为受 php.ini 文件中的设置的影响。


Mail 配置选项：


| 名称 | 默认 | 描述 | 可更改 |
| --- | --- | --- | --- |
| SMTP | "localhost" | Windows 专用：SMTP 服务器的 DNS 名称或 IP 地址。 | PHP_INI_ALL |
| smtp_port | "25" | Windows 专用：SMTP 端口号。自 PHP 4.3 起可用。 | PHP_INI_ALL |
| sendmail_from | NULL | Windows 专用：规定在由 PHP 发送的电子邮件中使用的 "from" 地址。 | PHP_INI_ALL |
| sendmail_path | NULL | Unix 系统专用：规定 sendmail 程序的路径（通常 /usr/sbin/sendmail 或 /usr/lib/sendmail）。 | PHP_INI_SYSTEM |

**
---


## PHP Mail 函数


PHP**：指示支持该函数的最早的 PHP 版本。


| 函数 | 描述 | PHP |
| --- | --- | --- |
| ezmlm_hash() | 计算 EZMLM 邮件列表系统所需的散列值。 | 3 |
| mail() | 允许您从脚本中直接发送电子邮件。 | 3 |

**
---


## PHP Mail 常量


无。****








	  AI 思考中...





			** [PHP Libxml 函数](https://www.runoob.com/php-ref-libxml.html)
			[PHP 5 Math 函数](https://www.runoob.com/php-ref-math.html) **













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
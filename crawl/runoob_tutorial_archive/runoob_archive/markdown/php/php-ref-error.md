# PHP Error 和 Logging 函数

- Source: https://www.runoob.com/php/php-ref-error.html

---


## PHP Error 和 Logging 简介


Error 和 Logging 函数允许您对错误进行处理和记录。


Error 函数允许用户定义错误处理规则，并修改记录错误的方式。


Logging 函数允许用户对应用程序进行日志记录，并把日志消息发送到电子邮件、系统日志或其他的机器。


---

## 执行配置


error 函数受 php.ini 配置文件影响。


错误和日志配置选项：


| 参数 | 默认值 | 描述 | 可修改范围 |
| --- | --- | --- | --- |
| error_reporting | NULL | 设置 PHP 的报错级别并返回当前级别(数字或常量)。 | PHP_INI_ALL |
| display_errors | "1" | 该选项设置是否将错误信息作为输出的一部分显示到屏幕，或者对用户隐藏而不显示。 注意： 该特性不要在上线生产环境中使用 (在开发测试过程中使用) | PHP_INI_ALL |
| display_startup_errors | "0" | 即使 display_errors 设置为开启, PHP 启动过程中的错误信息也不会被显示。强烈建议除了调试目的以外，将 display_startup_errors 设置为关闭。 | PHP_INI_ALL |
| log_errors | "0" | 设置是否将脚本运行的错误信息记录到服务器错误日志或者error_log之中。注意，这是与服务器相关的特定配置项。 | PHP_INI_ALL |
| log_errors_max_len | "1024" | 设置 log_errors 的最大字节数. 在 error_log 会添加有关错误源的信息。默认值为1024，如果设置为0表示不限长度。该长度设置对记录的错误，显示的错误，以及 $php_errormsg都会有限制作用。 | PHP_INI_ALL |
| ignore_repeated_errors | "0" | 不记录重复的信息。重复的错误必须出现在同一个文件中的同一行代码上，除非 ignore_repeated_source 设置为true。 | PHP_INI_ALL |
| ignore_repeated_source | "0" | 忽略重复消息时，也忽略消息的来源。当该设置开启时，重复信息将不会记录它是由不同的文件还是不同的源代码行产生的。 | PHP_INI_ALL |
| report_memleaks | "1" | 如果这个参数设置为Off，则内存泄露信息不会显示 (在 stdout 或者日志中)。 | PHP_INI_ALL |
| track_errors | "0" | 如果开启，最后的一个错误将永远存在于变量 $php_errormsg 中。 | PHP_INI_ALL |
| html_errors | "1" | 在错误信息中关闭HTML标签。 | PHP_INI_ALLPHP_INI_SYSTEM in PHP







	  AI 思考中...





			** [PHP 5 Directory 函数](https://www.runoob.com/php-ref-directory.html)
			[PHP 5 Filesystem 函数](https://www.runoob.com/php-ref-filesystem.html) **













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
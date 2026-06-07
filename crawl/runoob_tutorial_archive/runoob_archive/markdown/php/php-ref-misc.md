# PHP 杂项 函数

- Source: https://www.runoob.com/php/php-ref-misc.html

---


## PHP 杂项函数简介


我们把不属于其他类别的函数归纳到杂项函数类别。


---


## 安装


杂项函数是 PHP 核心的组成部分。无需安装即可使用这些函数。


---


## Runtime 配置


杂项函数的行为受 php.ini 文件中的设置的影响。


杂项配置选项：


| 名称 | 默认 | 描述 | 可更改 |
| --- | --- | --- | --- |
| ignore_user_abort | "0" | FALSE 指示只要脚本在客户机终止连接后尝试进行输出，脚本将被终止。 | PHP_INI_ALL |
| highlight.string | "#DD0000" | 供突出显示符合 PHP 语法的字符串而使用的颜色。 | PHP_INI_ALL |
| highlight.comment | "#FF8000" | 供突出显示 PHP 注释而使用的颜色。 | PHP_INI_ALL |
| highlight.keyword | "#007700" | 供语法高亮显示 PHP 关键词而使用的颜色（比如圆括号和分号）。 | PHP_INI_ALL |
| highlight.bg | "#FFFFFF" | 背景颜色。 | PHP_INI_ALL |
| highlight.default | "#0000BB" | PHP 语法的默认颜色。 | PHP_INI_ALL |
| highlight.html | "#000000" | HTML 代码的颜色。 | PHP_INI_ALL |
| browscap | NULL | 浏览器性能文件（例如：browscap.ini）的名称和位置。 | PHP_INI_SYSTEM |

**
---


## PHP 杂项函数


PHP**：指示支持该函数的最早的 PHP 版本。


| 函数 | 描述 | PHP |
| --- | --- | --- |
| connection_aborted() | 检查是否断开客户机。 | 3 |
| connection_status() | 返回当前的连接状态。 | 3 |
| connection_timeout() | 在 PHP 4.0.5 中不赞成使用。检查脚本是否超时。 | 3 |
| constant() | 返回一个常量的值。 | 4 |
| define() | 定义一个常量。 | 3 |
| defined() | 检查某常量是否存在。 | 3 |
| die() | 输出一条消息，并退出当前脚本。 | 3 |
| eval() | 把字符串当成 PHP 代码来计算。 | 3 |
| exit() | 输出一条消息，并退出当前脚本。 | 3 |
| get_browser() | 返回用户浏览器的性能。 | 3 |
| highlight_file() | 对文件进行 PHP 语法高亮显示。 | 4 |
| highlight_string() | 对字符串进行 PHP 语法高亮显示。 | 4 |
| ignore_user_abort() | 设置与远程客户机断开是否会终止脚本的执行。 | 3 |
| pack() | 把数据装入一个二进制字符串。 | 3 |
| php_check_syntax() | 在 PHP 5.0.5 中不赞成使用。 | 5 |
| php_strip_whitespace() | 返回已删除 PHP 注释以及空白字符的源代码文件。 | 5 |
| show_source() | highlight_file() 的别名。 | 4 |
| sleep() | 延迟代码执行若干秒。 | 3 |
| time_nanosleep() | 延迟代码执行若干秒和纳秒。 | 5 |
| time_sleep_until() | 延迟代码执行直到指定的时间。 | 5 |
| uniqid() | 生成唯一的 ID。 | 3 |
| unpack() | 从二进制字符串对数据进行解包。 | 3 |
| usleep() | 延迟代码执行若干微秒。 | 3 |

**
---


## PHP 杂项常量


PHP**：指示支持该常量的最早的 PHP 版本。


| 常量 | 描述 | PHP |
| --- | --- | --- |
| CONNECTION_ABORTED |  |  |
| CONNECTION_NORMAL |  |  |
| CONNECTION_TIMEOUT |  |  |
| __COMPILER_HALT_OFFSET__ |  | 5 |








	  AI 思考中...





			** [PHP 5 Math 函数](https://www.runoob.com/php-ref-math.html)
			[PHP 5 MySQLi 函数](https://www.runoob.com/php-ref-mysqli.html) **













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
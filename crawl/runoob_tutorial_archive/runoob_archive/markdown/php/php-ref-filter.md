# PHP Filter 函数

- Source: https://www.runoob.com/php/php-ref-filter.html

---


## PHP Filter 简介


PHP 过滤器用于对来自非安全来源的数据（比如用户输入）进行验证和过滤。


---


## 安装


Filter 函数是 PHP 核心的组成部分。无需安装即可使用这些函数。


---


## PHP Filter 函数


**PHP**：指示支持该函数的最早的 PHP 版本。


| 函数 | 描述 | PHP |
| --- | --- | --- |
| filter_has_var() | 检查是否存在指定输入类型的变量。 | 5 |
| filter_id() | 返回指定过滤器的 ID 号。 | 5 |
| filter_input() | 从脚本外部获取输入，并进行过滤。 | 5 |
| filter_input_array() | 从脚本外部获取多项输入，并进行过滤。 | 5 |
| filter_list() | 返回包含所有得到支持的过滤器的一个数组。 | 5 |
| filter_var_array() | 获取多个变量，并进行过滤。 | 5 |
| filter_var() | 获取一个变量，并进行过滤。 | 5 |

**
---


## PHP 过滤器


| ID 名称 | 描述 |
| --- | --- |
| FILTER_CALLBACK | 调用用户自定义函数来过滤数据。 |
| FILTER_SANITIZE_STRING | 去除标签，去除或编码特殊字符。 |
| FILTER_SANITIZE_STRIPPED | "string" 过滤器的别名。 |
| FILTER_SANITIZE_ENCODED | URL-encode 字符串，去除或编码特殊字符。 |
| FILTER_SANITIZE_SPECIAL_CHARS | HTML 转义字符 '"& 以及 ASCII 值小于 32 的字符。 |
| FILTER_SANITIZE_EMAIL | 删除所有字符，除了字母、数字以及 !#$%&'*+-/=?^_`{\|}~@.[] |
| FILTER_SANITIZE_URL | 删除所有字符，除了字母、数字以及 $-_.+!*'(),{}\|\^~[]`#%";/?:@&= |
| FILTER_SANITIZE_NUMBER_INT | 删除所有字符，除了数字和 +- |
| FILTER_SANITIZE_NUMBER_FLOAT | 删除所有字符，除了数字、+- 以及 .,eE |
| FILTER_SANITIZE_MAGIC_QUOTES | 应用 addslashes()。 |
| FILTER_UNSAFE_RAW | 不进行任何过滤，去除或编码特殊字符。 |
| FILTER_VALIDATE_INT | 把值作为整数来验证。 |
| FILTER_VALIDATE_BOOLEAN | 把值作为布尔选项来验证。如果是 "1"、"true"、"on" 和 "yes"，则返回 TRUE。如果是 "0"、"false"、"off"、"no" 和 ""，则返回 FALSE。否则返回 NULL。 |
| FILTER_VALIDATE_FLOAT | 把值作为浮点数来验证。 |
| FILTER_VALIDATE_REGEXP | 根据 regexp（一种兼容 Perl 的正则表达式）来验证值。 |
| FILTER_VALIDATE_URL | 把值作为 URL 来验证。 |
| FILTER_VALIDATE_EMAIL | 把值作为 e-mail 地址来验证。 |
| FILTER_VALIDATE_IP | 把值作为 IP 地址来验证，只限 IPv4 或 IPv6 或 不是来自私有或者保留的范围。 |








	  AI 思考中...





			** [PHP 5 Filesystem 函数](https://www.runoob.com/php-ref-filesystem.html)
			[PHP FTP 函数](https://www.runoob.com/php-ref-ftp.html) **













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
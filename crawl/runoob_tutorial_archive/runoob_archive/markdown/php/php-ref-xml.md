# PHP XML Parser 函数

- Source: https://www.runoob.com/php/php-ref-xml.html

---


## PHP XML Parser 简介


XML 函数允许您解析 XML 文档，但无法对其进行验证。


XML 是一种用于标准结构化文档交换的数据格式。您可以在我们的 XML 教程 中找到更多有关 XML 的信息。


该扩展使用 Expat XML 解析器。


Expat 是一种基于事件的解析器，它把 XML 文档视为一系列事件。当某个事件发生时，它调用一个指定的函数处理它。


Expat 是无验证的解析器，忽略任何链接到文档的 DTD。但是，如果文档的形式不好，则会以一个错误消息结束。


由于它是一种基于事件，且无验证的解析器，Expat 具有快速并适合 Web 应用程序的特性。


XML 解析器函数允许您创建 XML 解析器，并为 XML 事件定义句柄。


---


## 安装


XML Parser 函数是 PHP 核心的组成部分。无需安装即可使用这些函数。


---


## PHP XML Parser 函数


**PHP**：指示支持该函数的最早的 PHP 版本。


| 函数 | 描述 | PHP |
| --- | --- | --- |
| utf8_decode() | 把 UTF-8 字符串解码为 ISO-8859-1。 | 3 |
| utf8_encode() | 把 ISO-8859-1 字符串编码为 UTF-8。 | 3 |
| xml_error_string() | 获取 XML 解析器的错误字符串。 | 3 |
| xml_get_current_byte_index() | 获取 XML 解析器的当前字节索引。 | 3 |
| xml_get_current_column_number() | 获取 XML 解析器的当前列号。 | 3 |
| xml_get_current_line_number() | 获取 XML 解析器的当前行号。 | 3 |
| xml_get_error_code() | 获取 XML 解析器的错误代码。 | 3 |
| xml_parse() | 解析 XML 文档。 | 3 |
| xml_parse_into_struct() | 把 XML 数据解析到数组中。 | 3 |
| xml_parser_create_ns() | 创建带有命名空间支持的 XML 解析器。 | 4 |
| xml_parser_create() | 创建 XML 解析器。 | 3 |
| xml_parser_free() | 释放 XML 解析器。 | 3 |
| xml_parser_get_option() | 从 XML 解析器获取选项。 | 3 |
| xml_parser_set_option() | 为 XML 解析器设置选项。 | 3 |
| xml_set_character_data_handler() | 建立字符数据处理器。 | 3 |
| xml_set_default_handler() | 建立默认处理器。 | 3 |
| xml_set_element_handler() | 建立起始和终止元素处理器。 | 3 |
| xml_set_end_namespace_decl_handler() | 建立终止命名空间声明处理器。 | 4 |
| xml_set_external_entity_ref_handler() | 建立外部实体处理器。 | 3 |
| xml_set_notation_decl_handler() | 建立符号声明处理器。 | 3 |
| xml_set_object() | 在对象中使用 XML 解析器。 | 4 |
| xml_set_processing_instruction_handler() | 建立处理指令（PI）处理器。 | 3 |
| xml_set_start_namespace_decl_handler() | 建立起始命名空间声明处理器。 | 4 |
| xml_set_unparsed_entity_decl_handler() | 建立未解析实体声明处理器。 | 3 |

**
---


## PHP XML Parser 常量


| 常量 |
| --- |
| XML_ERROR_NONE (integer) |
| XML_ERROR_NO_MEMORY (integer) |
| XML_ERROR_SYNTAX (integer) |
| XML_ERROR_NO_ELEMENTS (integer) |
| XML_ERROR_INVALID_TOKEN (integer) |
| XML_ERROR_UNCLOSED_TOKEN (integer) |
| XML_ERROR_PARTIAL_CHAR (integer) |
| XML_ERROR_TAG_MISMATCH (integer) |
| XML_ERROR_DUPLICATE_ATTRIBUTE (integer) |
| XML_ERROR_JUNK_AFTER_DOC_ELEMENT (integer) |
| XML_ERROR_PARAM_ENTITY_REF (integer) |
| XML_ERROR_UNDEFINED_ENTITY (integer) |
| XML_ERROR_RECURSIVE_ENTITY_REF (integer) |
| XML_ERROR_ASYNC_ENTITY (integer) |
| XML_ERROR_BAD_CHAR_REF (integer) |
| XML_ERROR_BINARY_ENTITY_REF (integer) |
| XML_ERROR_ATTRIBUTE_EXTERNAL_ENTITY_REF (integer) |
| XML_ERROR_MISPLACED_XML_PI (integer) |
| XML_ERROR_UNKNOWN_ENCODING (integer) |
| XML_ERROR_INCORRECT_ENCODING (integer) |
| XML_ERROR_UNCLOSED_CDATA_SECTION (integer) |
| XML_ERROR_EXTERNAL_ENTITY_HANDLING (integer) |
| XML_OPTION_CASE_FOLDING (integer) |
| XML_OPTION_TARGET_ENCODING (integer) |
| XML_OPTION_SKIP_TAGSTART (integer) |
| XML_OPTION_SKIP_WHITE (integer) |








	  AI 思考中...





			** [PHP 5 String 函数](https://www.runoob.com/php-ref-string.html)
			[PHP Zip File 函数](https://www.runoob.com/php-ref-zip.html) **













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
# PHP 5 String 函数

- Source: https://www.runoob.com/php/php-ref-string.html

---


## PHP 5 String 函数


PHP String 函数是 PHP 核心的组成部分。无需安装即可使用这些函数。


---


| 函数 | 描述 |
| --- | --- |
| addcslashes() | 返回在指定的字符前添加反斜杠的字符串。 |
| addslashes() | 返回在预定义的字符前添加反斜杠的字符串。 |
| bin2hex() | 把 ASCII 字符的字符串转换为十六进制值。 |
| chop() | 移除字符串右侧的空白字符或其他字符。 |
| chr() | 从指定 ASCII 值返回字符。 |
| chunk_split() | 把字符串分割为一连串更小的部分。 |
| convert_cyr_string() | 把字符串由一种 Cyrillic 字符集转换成另一种。 |
| convert_uudecode() | 对 uuencode 编码的字符串进行解码。 |
| convert_uuencode() | 使用 uuencode 算法对字符串进行编码。 |
| count_chars() | 返回字符串所用字符的信息。 |
| crc32() | 计算一个字符串的 32 位 CRC（循环冗余校验）。 |
| crypt() | 单向的字符串加密法（hashing）。 |
| echo() | 输出一个或多个字符串。 |
| explode() | 把字符串打散为数组。 |
| fprintf() | 把格式化的字符串写入到指定的输出流。 |
| get_html_translation_table() | 返回 htmlspecialchars() 和 htmlentities() 使用的翻译表。 |
| hebrev() | 把希伯来（Hebrew）文本转换为可见文本。 |
| hebrevc() | 把希伯来（Hebrew）文本转换为可见文本，并把新行（\n）转换为 。 |
| hex2bin() | 把十六进制值的字符串转换为 ASCII 字符。 |
| html_entity_decode() | 把 HTML 实体转换为字符。 |
| htmlentities() | 把字符转换为 HTML 实体。 |
| htmlspecialchars_decode() | 把一些预定义的 HTML 实体转换为字符。 |
| htmlspecialchars() | 把一些预定义的字符转换为 HTML 实体。 |
| implode() | 返回一个由数组元素组合成的字符串。 |
| join() | implode() 的别名。 |
| lcfirst() | 把字符串中的首字符转换为小写。 |
| levenshtein() | 返回两个字符串之间的 Levenshtein 距离。 |
| localeconv() | 返回本地数字及货币格式信息。 |
| ltrim() | 移除字符串左侧的空白字符或其他字符。 |
| md5() | 计算字符串的 MD5 散列。 |
| md5_file() | 计算文件的 MD5 散列。 |
| metaphone() | 计算字符串的 metaphone 键。 |
| money_format() | 返回格式化为货币字符串的字符串。 |
| nl_langinfo() | 返回指定的本地信息。 |
| nl2br() | 在字符串中的每个新行之前插入 HTML 换行符。 |
| number_format() | 通过千位分组来格式化数字。 |
| ord() | 返回字符串中第一个字符的 ASCII 值。 |
| parse_str() | 把查询字符串解析到变量中。 |
| print() | 输出一个或多个字符串。 |
| printf() | 输出格式化的字符串。 |
| quoted_printable_decode() | 把 quoted-printable 字符串转换为 8 位字符串。 |
| quoted_printable_encode() | 把 8 位字符串转换为 quoted-printable 字符串。 |
| quotemeta() | 引用元字符。 |
| rtrim() | 移除字符串右侧的空白字符或其他字符。 |
| setlocale() | 设置地区信息（地域信息）。 |
| sha1() | 计算字符串的 SHA-1 散列。 |
| sha1_file() | 计算文件的 SHA-1 散列。 |
| similar_text() | 计算两个字符串的相似度。 |
| soundex() | 计算字符串的 soundex 键。 |
| sprintf() | 把格式化的字符串写入一个变量中。 |
| sscanf() | 根据指定的格式解析来自一个字符串的输入。 |
| str_getcsv() | 把 CSV 字符串解析到数组中。 |
| str_ireplace() | 替换字符串中的一些字符（大小写不敏感）。 |
| str_pad() | 把字符串填充为新的长度。 |
| str_repeat() | 把字符串重复指定的次数。 |
| str_replace() | 替换字符串中的一些字符（大小写敏感）。 |
| str_rot13() | 对字符串执行 ROT13 编码。 |
| str_shuffle() | 随机地打乱字符串中的所有字符。 |
| str_split() | 把字符串分割到数组中。 |
| str_word_count() | 计算字符串中的单词数。 |
| strcasecmp() | 比较两个字符串（大小写不敏感）。 |
| strchr() | 查找字符串在另一字符串中的第一次出现。（strstr() 的别名。） |
| strcmp() | 比较两个字符串（大小写敏感）。 |
| strcoll() | 比较两个字符串（根据本地设置）。 |
| strcspn() | 返回在找到任何指定的字符之前，在字符串查找的字符数。 |
| strip_tags() | 剥去字符串中的 HTML 和 PHP 标签。 |
| stripcslashes() | 删除由 addcslashes() 函数添加的反斜杠。 |
| stripslashes() | 删除由 addslashes() 函数添加的反斜杠。 |
| stripos() | 返回字符串在另一字符串中第一次出现的位置（大小写不敏感）。 |
| stristr() | 查找字符串在另一字符串中第一次出现的位置（大小写不敏感）。 |
| strlen() | 返回字符串的长度。中文字符串的处理使用 mb_strlen() 函数。 |
| strnatcasecmp() | 使用一种"自然排序"算法来比较两个字符串（大小写不敏感）。 |
| strnatcmp() | 使用一种"自然排序"算法来比较两个字符串（大小写敏感）。 |
| strncasecmp() | 前 n 个字符的字符串比较（大小写不敏感）。 |
| strncmp() | 前 n 个字符的字符串比较（大小写敏感）。 |
| strpbrk() | 在字符串中搜索指定字符中的任意一个。 |
| strpos() | 返回字符串在另一字符串中第一次出现的位置（大小写敏感）。 |
| strrchr() | 查找字符串在另一个字符串中最后一次出现。 |
| strrev() | 反转字符串。 |
| strripos() | 查找字符串在另一字符串中最后一次出现的位置(大小写不敏感)。 |
| strrpos() | 查找字符串在另一字符串中最后一次出现的位置(大小写敏感)。 |
| strspn() | 返回在字符串中包含的特定字符的数目。 |
| strstr() | 查找字符串在另一字符串中的第一次出现（大小写敏感）。 |
| strtok() | 把字符串分割为更小的字符串。 |
| strtolower() | 把字符串转换为小写字母。 |
| strtoupper() | 把字符串转换为大写字母。 |
| strtr() | 转换字符串中特定的字符。 |
| substr() | 返回字符串的一部分。 |
| mb_substr() | 返回中文字符串的一部分。 |
| substr_compare() | 从指定的开始位置（二进制安全和选择性区分大小写）比较两个字符串。 |
| substr_count() | 计算子串在字符串中出现的次数。 |
| substr_replace() | 把字符串的一部分替换为另一个字符串。 |
| trim() | 移除字符串两侧的空白字符和其他字符。 |
| ucfirst() | 把字符串中的首字符转换为大写。 |
| ucwords() | 把字符串中每个单词的首字符转换为大写。 |
| vfprintf() | 把格式化的字符串写到指定的输出流。 |
| vprintf() | 输出格式化的字符串。 |
| vsprintf() | 把格式化字符串写入变量中。 |
| wordwrap() | 按照指定长度对字符串进行折行处理。 |








	  AI 思考中...





			** [PHP 5 SimpleXML 函数](https://www.runoob.com/php-ref-simplexml.html)
			[PHP XML 函数](https://www.runoob.com/php-ref-xml.html) **













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
# HTML ANSI（Windows-1252） 参考手册

- Source: https://www.runoob.com/charsets/ref-html-ansi.html

---


## ANSI（Windows-1252）


ANSI 是 Windows 95 及其之前的 Windows 系统中默认的字符集。


ANSI 也称为 Windows-1252。


---


## 重要提示


ANSI 和 ISO-8859-1 非常相似，唯一的不同是在 32 个字符上。


在 ANSI 中，从 128 到 159 的字符用于一些有用的字符，比如欧元符号。


在 ISO-8859-1 中，这些字符映射为在 HTML 中不起作用的控制字符。


许多 Web 开发者声明 ISO-8859-1，并使用这 32 个值，就像它们使用的是 Windows-1252。


由于这种常见的误解，当 ISO-8859-1 被声明时，浏览器将更改为 Windows-1252。这对以下文档类型都适用：HTML4、HTML5 和 XHTML。


---


## ANSI 和 ASCII


ANSI 的第一部分（实体编号 0-127）是原来的 ASCII 字符集。它包含数字、大小写英文字母和一些特殊字符。


如需深入了解 ASCII，请查看[完整的 ASCII 参考手册](https://www.runoob.com/ref-html-ascii.html)。


---


## ANSI 字符集


| 字符 | 编号 | 实体名称 | 描述 |
| --- | --- | --- | --- |
|  | 32 |  | 空格（space） |
| ! | 33 |  | 感叹号（exclamation mark） |
| " | 34 | " | 引号（quotation mark） |
| # | 35 |  | 数字符号（number sign） |
| $ | 36 |  | 美元符号（dollar sign） |
| % | 37 |  | 百分比符号（percent sign） |
| & | 38 | & | & 符号（ampersand） |
| ' | 39 |  | 撇号（apostrophe） |
| ( | 40 |  | 左括号（left parenthesis） |
| ) | 41 |  | 右括号（right parenthesis） |
| * | 42 |  | 星号（asterisk） |
| + | 43 |  | 加号（plus sign） |
| , | 44 |  | 逗号（comma） |
| - | 45 |  | 连字符（hyphen-minus） |
| . | 46 |  | 句号（full stop） |
| / | 47 |  | 斜线（solidus） |
| 0 | 48 |  | 数字 0（digit zero） |
| 1 | 49 |  | 数字 1（digit one） |
| 2 | 50 |  | 数字 2（digit two） |
| 3 | 51 |  | 数字 3（digit three） |
| 4 | 52 |  | 数字 4（digit four） |
| 5 | 53 |  | 数字 5（digit five） |
| 6 | 54 |  | 数字 6（digit six） |
| 7 | 55 |  | 数字 7（digit seven） |
| 8 | 56 |  | 数字 8（digit eight） |
| 9 | 57 |  | 数字 9（digit nine） |
| : | 58 |  | 冒号（colon） |
| ; | 59 |  | 分号（semicolon） |
|  | 62 | > | 大于号（greater-than sign） |
| ? | 63 |  | 问号（question mark） |
| @ | 64 |  | @ 符号（commercial at） |
| A | 65 |  | 拉丁文大写字母 A |
| B | 66 |  | 拉丁文大写字母 B |
| C | 67 |  | 拉丁文大写字母 C |
| D | 68 |  | 拉丁文大写字母 D |
| E | 69 |  | 拉丁文大写字母 E |
| F | 70 |  | 拉丁文大写字母 F |
| G | 71 |  | 拉丁文大写字母 G |
| H | 72 |  | 拉丁文大写字母 H |
| I | 73 |  | 拉丁文大写字母 I |
| J | 74 |  | 拉丁文大写字母 J |
| K | 75 |  | 拉丁文大写字母 K |
| L | 76 |  | 拉丁文大写字母 L |
| M | 77 |  | 拉丁文大写字母 M |
| N | 78 |  | 拉丁文大写字母 N |
| O | 79 |  | 拉丁文大写字母 O |
| P | 80 |  | 拉丁文大写字母 P |
| Q | 81 |  | 拉丁文大写字母 Q |
| R | 82 |  | 拉丁文大写字母 R |
| S | 83 |  | 拉丁文大写字母 S |
| T | 84 |  | 拉丁文大写字母 T |
| U | 85 |  | 拉丁文大写字母 U |
| V | 86 |  | 拉丁文大写字母 V |
| W | 87 |  | 拉丁文大写字母 W |
| X | 88 |  | 拉丁文大写字母 X |
| Y | 89 |  | 拉丁文大写字母 Y |
| Z | 90 |  | 拉丁文大写字母 Z |
| [ | 91 |  | 左方括号（left square bracket） |
| \ | 92 |  | 反斜线（reverse solidus） |
| ] | 93 |  | 右方括号（right square bracket） |
| ^ | 94 |  | 插入符号（circumflex accent） |
| _ | 95 |  | 下划线（low line） |
| ` | 96 |  | 重音符（grave accent） |
| a | 97 |  | 拉丁文小写字母 a |
| b | 98 |  | 拉丁文小写字母 b |
| c | 99 |  | 拉丁文小写字母 c |
| d | 100 |  | 拉丁文小写字母 d |
| e | 101 |  | 拉丁文小写字母 e |
| f | 102 |  | 拉丁文小写字母 f |
| g | 103 |  | 拉丁文小写字母 g |
| h | 104 |  | 拉丁文小写字母 h |
| i | 105 |  | 拉丁文小写字母 i |
| j | 106 |  | 拉丁文小写字母 j |
| k | 107 |  | 拉丁文小写字母 k |
| l | 108 |  | 拉丁文小写字母 l |
| m | 109 |  | 拉丁文小写字母 m |
| n | 110 |  | 拉丁文小写字母 n |
| o | 111 |  | 拉丁文小写字母 o |
| p | 112 |  | 拉丁文小写字母 p |
| q | 113 |  | 拉丁文小写字母 q |
| r | 114 |  | 拉丁文小写字母 r |
| s | 115 |  | 拉丁文小写字母 s |
| t | 116 |  | 拉丁文小写字母 t |
| u | 117 |  | 拉丁文小写字母 u |
| v | 118 |  | 拉丁文小写字母 v |
| w | 119 |  | 拉丁文小写字母 w |
| x | 120 |  | 拉丁文小写字母 x |
| y | 121 |  | 拉丁文小写字母 y |
| z | 122 |  | 拉丁文小写字母 z |
| { | 123 |  | 左花括号（left curly bracket） |
| \| | 124 |  | 竖线（vertical line） |
| } | 125 |  | 右花括号（right curly bracket） |
| ~ | 126 |  | 波浪线（tilde） |
|  | 127 |  | 未使用（NOT USED） |
| € | 128 | € | 欧元符号（euro sign） |
|  | 129 |  | 未使用（NOT USED） |
| ‚ | 130 | ‚ | 下单引号（single low-9 quotation mark） |
| ƒ | 131 | ƒ | 带钩的拉丁文小写字母 f |
| „ | 132 | „ | 下双引号（double low-9 quotation mark） |
| … | 133 | … | 水平省略号（horizontal ellipsis） |
| † | 134 | † | 剑号（dagger） |
| ‡ | 135 | ‡ | 双剑号（double dagger） |
| ˆ | 136 | ˆ | 修饰字母抑扬音（modifier letter circumflex accent） |
| ‰ | 137 | ‰ | 千分比符号（per mille sign） |
| Š | 138 | Š | 带有 caron 的拉丁文大写字母 S |
| ‹ | 139 | ‹ | 左单角引号（single left-pointing angle quotation mark） |
| Œ | 140 | Œ | 拉丁文大写连字 OE |
|  | 141 |  | 未使用（NOT USED） |
| Ž | 142 | Ž | 带有 caron 的拉丁文大写字母 Z |
|  | 143 |  | 未使用（NOT USED） |
|  | 144 |  | 未使用（NOT USED） |
| ' | 145 | ‘ | 左单引号（left single quotation mark） |
| ' | 146 | ’ | 右单引号（right single quotation mark） |
| " | 147 | “ | 左双引号（left double quotation mark） |
| " | 148 | ” | 右双引号（right double quotation mark） |
| • | 149 | • | 着重号（bullet） |
| – | 150 | – | 短破折号/连字符（en dash） |
| — | 151 | — | 长破折号（em dash） |
| ˜ | 152 | ˜ | 小波浪线（small tilde） |
| ™ | 153 | ™ | 贸易标记符号（trade mark sign） |
| š | 154 | š | 带有 caron 的拉丁文小写字母 s |
| › | 155 | › | 右单角引号（single right-pointing angle quotation mark） |
| œ | 156 | œ | 拉丁文小写连字 oe |
|  | 157 |  | 未使用（NOT USED） |
| ž | 158 | ž | 带有 caron 的拉丁文小写字母 z |
| Ÿ | 159 | Ÿ | 带有分音符（diaeresis）的拉丁文大写字母 Y |
|  | 160 |   | 不换行空格（no-break space） |
| ¡ | 161 | ¡ | 倒置感叹号（inverted exclamation mark） |
| ¢ | 162 | ¢ | 美分符号（cent sign） |
| £ | 163 | £ | 英镑符号（pound sign） |
| ¤ | 164 | ¤ | 货币符号（currency sign） |
| ¥ | 165 | ¥ | 日元符号（yen sign） |
| ¦ | 166 | ¦ | 间断的竖杠（broken bar） |
| § | 167 | § | 小节号（section sign） |
| ¨ | 168 | ¨ | 分音符号（diaeresis） |
| © | 169 | © | 版权所有（copyright sign） |
| ª | 170 | ª | 阴性序数记号（feminine ordinal indicator） |
| « | 171 | « | 左双角引号（left-pointing double angle quotation mark） |
| ¬ | 172 | ¬ | 否定符号（not sign） |
| ­ | 173 | ­ | 软连字符（soft hyphen） |
| ® | 174 | ® | 注册商标（registered sign） |
| ¯ | 175 | ¯ | 长音符号（macron） |
| ° | 176 | ° | 度符号（degree sign） |
| ± | 177 | ± | 加减号/正负号（plus-minus sign） |
| ² | 178 | ² | 上标 2（superscript two） |
| ³ | 179 | ³ | 上标 3（superscript three） |
| ´ | 180 | ´ | 尖音符号（acute accent） |
| µ | 181 | µ | 微米符号（micro sign） |
| ¶ | 182 | ¶ | 段落符号（pilcrow sign） |
| · | 183 | · | 中间点（middle dot） |
| ¸ | 184 | ¸ | 变音符号（cedilla） |
| ¹ | 185 | ¹ | 上标 1（superscript one） |
| º | 186 | º | 阳性序数记号（masculine ordinal indicator） |
| » | 187 | » | 右双角引号（right-pointing double angle quotation mark） |
| ¼ | 188 | ¼ | 1/4 分数（vulgar fraction one quarter） |
| ½ | 189 | ½ | 1/2 分数（vulgar fraction one half） |
| ¾ | 190 | ¾ | 3/4 分数（vulgar fraction three quarters） |
| ¿ | 191 | ¿ | 倒置问号（inverted question mark） |
| À | 192 | À | 带有重音符号（grave）的拉丁文大写字母 A |
| Á | 193 | Á | 带有尖音符号（acute）的拉丁文大写字母 A |
| Â | 194 | Â | 带有抑扬音符号（circumflex）的拉丁文大写字母 A |
| Ã | 195 | Ã | 带有波浪线的拉丁文大写字母 A |
| Ä | 196 | Ä | 带有分音符（diaeresis）的拉丁文大写字母 A |
| Å | 197 | Å | 带有上圆圈的拉丁文大写字母 A |
| Æ | 198 | Æ | 拉丁文大写字母 AE |
| Ç | 199 | Ç | 带有变音符号（cedilla）的拉丁文大写字母 C |
| È | 200 | È | 带有重音符号（grave）的拉丁文大写字母 E |
| É | 201 | É | 带有尖音符号（acute）的拉丁文大写字母 E |
| Ê | 202 | Ê | 带有抑扬符号（circumflex）的拉丁文大写字母 E |
| Ë | 203 | Ë | 带有分音符（diaeresis）的拉丁文大写字母 E |
| Ì | 204 | Ì | 带有重音符号（grave）的拉丁文大写字母 I |
| Í | 205 | Í | 带有尖音符号（acute）的拉丁文大写字母 I |
| Î | 206 | Î | 带有抑扬音符号（circumflex）的拉丁文大写字母 I |
| Ï | 207 | Ï | 带有分音符（diaeresis）的拉丁文大写字母 I |
| Ð | 208 | Ð | 拉丁文大写字母 Eth |
| Ñ | 209 | Ñ | 带有波浪线的拉丁文大写字母 N |
| Ò | 210 | Ò | 带有重音符号（grave）的拉丁文大写字母 O |
| Ó | 211 | Ó | 带有尖音符号（acute）的拉丁文大写字母 O |
| Ô | 212 | Ô | 带有抑扬音符号（circumflex）的拉丁文大写字母 O |
| Õ | 213 | Õ | 带有波浪线的拉丁文大写字母 O |
| Ö | 214 | Ö | 带有分音符（diaeresis）的拉丁文大写字母 O |
| × | 215 | × | 乘号（multiplication sign） |
| Ø | 216 | Ø | 带有删除线的拉丁文大写字母 O |
| Ù | 217 | Ù | 带有重音符号（grave）的拉丁文大写字母 U |
| Ú | 218 | Ú | 带有尖音符号（acute）的拉丁文大写字母 U |
| Û | 219 | Û | 带有抑扬音符号（circumflex）的拉丁文大写字母 U |
| Ü | 220 | Ü | 带有分音符（diaeresis）的拉丁文大写字母 U |
| Ý | 221 | Ý | 带有尖音符号（acute）的拉丁文大写字母 Y |
| Þ | 222 | Þ | 拉丁文大写字母 Thorn |
| ß | 223 | ß | 拉丁文小写字母 sharp s |
| à | 224 | à | 带有重音符号（grave）的拉丁文小写字母 a |
| á | 225 | á | 带有尖音符号（acute）的拉丁文小写字母 a |
| â | 226 | â | 带有抑扬音符号（circumflex）的拉丁文小写字母 a |
| ã | 227 | ã | 带有波浪线的拉丁文小写字母 a |
| ä | 228 | ä | 带有分音符（diaeresis）的拉丁文小写字母 a |
| å | 229 | å | 带有上圆圈的拉丁文小写字母 a |
| æ | 230 | æ | 拉丁文小写字母 ae |
| ç | 231 | ç | 带有变音符号（cedilla）的拉丁文小写字母 c |
| è | 232 | è | 带有重音符号（grave）的拉丁文小写字母 e |
| é | 233 | é | 带有尖音符号（acute）的拉丁文小写字母 e |
| ê | 234 | ê | 带有抑扬音符号（circumflex）的拉丁文小写字母 e |
| ë | 235 | ë | 带有分音符（diaeresis）的拉丁文小写字母 e |
| ì | 236 | ì | 带有重音符号（grave）的拉丁文小写字母 i |
| í | 237 | í | 带有尖音符号（acute）的拉丁文小写字母 i |
| î | 238 | î | 带有抑扬音符号（circumflex）的拉丁文小写字母 i |
| ï | 239 | ï | 带有分音符（diaeresis）的拉丁文小写字母 i |
| ð | 240 | ð | 拉丁文小写字母 eth |
| ñ | 241 | ñ | 带有波浪线的拉丁文小写字母 n |
| ò | 242 | ò | 带有重音符号（grave）的拉丁文小写字母 o |
| ó | 243 | ó | 带有尖音符号（acute）的拉丁文小写字母 o |
| ô | 244 | ô | 带有抑扬音符号（circumflex）的拉丁文小写字母 o |
| õ | 245 | õ | 带有波浪线的拉丁文小写字母 o |
| ö | 246 | ö | 带有分音符（diaeresis）的拉丁文小写字母 o |
| ÷ | 247 | ÷ | 除号（division sign） |
| ø | 248 | ø | 带有删除线的拉丁文小写字母 o |
| ù | 249 | ù | 带有重音符号（grave）的拉丁文小写字母 u |
| ú | 250 | ú | 带有尖音符号（acute）的拉丁文小写字母 u |
| û | 251 | û | 带有抑扬音符号（circumflex）的拉丁文小写字母 u |
| ü | 252 | ü | 带有分音符（diaeresis）的拉丁文小写字母 u |
| ý | 253 | ý | 带有尖音符号（acute）的拉丁文小写字母 y |
| þ | 254 | þ | 拉丁文小写字母 thorn |
| ÿ | 255 | ÿ | 带有分音符（diaeresis）的拉丁文小写字母 y |

**

---


## ANSI 控制字符


ANSI 控制字符（00-31，加上 127）最初被设计用来控制诸如打印机和磁带驱动器之类的硬件设备。


控制字符（除了水平制表符、换行、回车之外）在 HTML 文档中不起任何作用。


| 字符 | 编号 | 描述 |
| --- | --- | --- |
| NUL | 00 | 空字符（null character） |
| SOH | 01 | 标题开始（start of header） |
| STX | 02 | 正文开始（start of text） |
| ETX | 03 | 正文结束（end of text） |
| EOT | 04 | 传输结束（end of transmission） |
| ENQ | 05 | 请求（enquiry） |
| ACK | 06 | 收到通知/响应（acknowledge） |
| BEL | 07 | 响铃（bell） |
| BS | 08 | 退格（backspace） |
| HT | 09 | 水平制表符（horizontal tab） |
| LF | 10 | 换行（line feed） |
| VT | 11 | 垂直制表符（vertical tab） |
| FF | 12 | 换页（form feed） |
| CR | 13 | 回车（carriage return） |
| SO | 14 | 不用切换（shift out） |
| SI | 15 | 启用切换（shift in） |
| DLE | 16 | 数据链路转义（data link escape） |
| DC1 | 17 | 设备控制 1（device control 1） |
| DC2 | 18 | 设备控制 2（device control 2） |
| DC3 | 19 | 设备控制 3（device control 3） |
| DC4 | 20 | 设备控制 4（device control 4） |
| NAK | 21 | 拒绝接收/无响应（negative acknowledge） |
| SYN | 22 | 同步空闲（synchronize） |
| ETB | 23 | 传输块结束（end transmission block） |
| CAN | 24 | 取消（cancel） |
| EM | 25 | 已到介质末端/介质存储已满（end of medium） |
| SUB | 26 | 替补/替换（substitute） |
| ESC | 27 | 溢出/逃离/取消（escape） |
| FS | 28 | 文件分隔符（file separator） |
| GS | 29 | 组分隔符（group separator） |
| RS | 30 | 记录分隔符（record separator） |
| US | 31 | 单元分隔符（unit separator） |
|  |  |  |
| DEL | 127 | 删除（delete） |








	  AI 思考中...





			** [HTML ASCII 参考手册](https://www.runoob.com/ref-html-ascii.html)
			[HTML ISO-8859-1 参考手册](https://www.runoob.com/ref-html-8859.html) **













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

      : · [HTML 字符集设置](https://www.runoob.com/html-charsets.html)

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
# VBScript GetLocale 函数

- Source: https://www.runoob.com/vbscript/func-getlocale.html

---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)

---


GetLocale 函数返回当前的 locale ID。


locale 是用户参考信息集合，比如语言、国家、地区和文化习俗。locale 决定键盘布局、字母排序顺序、日期、时间、数字与货币格式等等。


返回值可以是任意一个 32 位的值，如Locale ID 表所示。


**提示：**请使用 SetLocale 函数来设置本地 ID。


### 语法


GetLocale()


## 实例


## 实例（仅适用于 IE）


```
<script type="text/vbscript">
document.write(GetLocale)
</script>
```


以上实例输出结果：


```
document.write(GetLocale)
```


**[尝试一下 »](https://www.runoob.com/try/try.php?filename=vbdemo_getlocale_func)


---


### Locale ID 表


| Locale 描述 | 简写 | 十六进制值 | 十进制值 |
| --- | --- | --- | --- |
| Afrikaans | af | 0x0436 | 1078 |
| Albanian | sq | 0x041C | 1052 |
| Arabic – United Arab Emirates | ar-ae | 0x3801 | 14337 |
| Arabic - Bahrain | ar-bh | 0x3C01 | 15361 |
| Arabic - Algeria | ar-dz | 0x1401 | 5121 |
| Arabic - Egypt | ar-eg | 0x0C01 | 3073 |
| Arabic - Iraq | ar-iq | 0x0801 | 2049 |
| Arabic - Jordan | ar-jo | 0x2C01 | 11265 |
| Arabic - Kuwait | ar-kw | 0x3401 | 13313 |
| Arabic - Lebanon | ar-lb | 0x3001 | 12289 |
| Arabic - Libya | ar-ly | 0x1001 | 4097 |
| Arabic - Morocco | ar-ma | 0x1801 | 6145 |
| Arabic - Oman | ar-om | 0x2001 | 8193 |
| Arabic - Qatar | ar-qa | 0x4001 | 16385 |
| Arabic - Saudi Arabia | ar-sa | 0x0401 | 1025 |
| Arabic - Syria | ar-sy | 0x2801 | 10241 |
| Arabic - Tunisia | ar-tn | 0x1C01 | 7169 |
| Arabic - Yemen | ar-ye | 0x2401 | 9217 |
| Armenian | hy | 0x042B | 1067 |
| Azeri – Latin | az-az | 0x042C | 1068 |
| Azeri – Cyrillic | az-az | 0x082C | 2092 |
| Basque | eu | 0x042D | 1069 |
| Belarusian | be | 0x0423 | 1059 |
| Bulgarian | bg | 0x0402 | 1026 |
| Catalan | ca | 0x0403 | 1027 |
| Chinese - China | zh-cn | 0x0804 | 2052 |
| Chinese - Hong Kong S.A.R. | zh-hk | 0x0C04 | 3076 |
| Chinese – Macau S.A.R | zh-mo | 0x1404 | 5124 |
| Chinese - Singapore | zh-sg | 0x1004 | 4100 |
| Chinese - Taiwan | zh-tw | 0x0404 | 1028 |
| Croatian | hr | 0x041A | 1050 |
| Czech | cs | 0x0405 | 1029 |
| Danish | da | 0x0406 | 1030 |
| Dutch – The Netherlands | nl-nl | 0x0413 | 1043 |
| Dutch - Belgium | nl-be | 0x0813 | 2067 |
| English - Australia | en-au | 0x0C09 | 3081 |
| English - Belize | en-bz | 0x2809 | 10249 |
| English - Canada | en-ca | 0x1009 | 4105 |
| English – Carribbean | en-cb | 0x2409 | 9225 |
| English - Ireland | en-ie | 0x1809 | 6153 |
| English - Jamaica | en-jm | 0x2009 | 8201 |
| English - New Zealand | en-nz | 0x1409 | 5129 |
| English – Phillippines | en-ph | 0x3409 | 13321 |
| English - South Africa | en-za | 0x1C09 | 7177 |
| English - Trinidad | en-tt | 0x2C09 | 11273 |
| English - United Kingdom | en-gb | 0x0809 | 2057 |
| English - United States | en-us | 0x0409 | 1033 |
| Estonian | et | 0x0425 | 1061 |
| Farsi | fa | 0x0429 | 1065 |
| Finnish | fi | 0x040B | 1035 |
| Faroese | fo | 0x0438 | 1080 |
| French - France | fr-fr | 0x040C | 1036 |
| French - Belgium | fr-be | 0x080C | 2060 |
| French - Canada | fr-ca | 0x0C0C | 3084 |
| French - Luxembourg | fr-lu | 0x140C | 5132 |
| French - Switzerland | fr-ch | 0x100C | 4108 |
| Gaelic – Ireland | gd-ie | 0x083C | 2108 |
| Gaelic - Scotland | gd | 0x043C | 1084 |
| German - Germany | de-de | 0x0407 | 1031 |
| German - Austria | de-at | 0x0C07 | 3079 |
| German - Liechtenstein | de-li | 0x1407 | 5127 |
| German - Luxembourg | de-lu | 0x1007 | 4103 |
| German - Switzerland | de-ch | 0x0807 | 2055 |
| Greek | el | 0x0408 | 1032 |
| Hebrew | he | 0x040D | 1037 |
| Hindi | hi | 0x0439 | 1081 |
| Hungarian | hu | 0x040E | 1038 |
| Icelandic | is | 0x040F | 1039 |
| Indonesian | id | 0x0421 | 1057 |
| Italian - Italy | it-it | 0x0410 | 1040 |
| Italian - Switzerland | it-ch | 0x0810 | 2064 |
| Japanese | ja | 0x0411 | 1041 |
| Korean | ko | 0x0412 | 1042 |
| Latvian | lv | 0x0426 | 1062 |
| Lithuanian | lt | 0x0427 | 1063 |
| FYRO Macedonian | mk | 0x042F | 1071 |
| Malay - Malaysia | ms-my | 0x043E | 1086 |
| Malay – Brunei | ms-bn | 0x083E | 2110 |
| Maltese | mt | 0x043A | 1082 |
| Marathi | mr | 0x044E | 1102 |
| Norwegian - Bokmål | no-no | 0x0414 | 1044 |
| Norwegian – Nynorsk | no-no | 0x0814 | 2068 |
| Polish | pl | 0x0415 | 1045 |
| Portuguese - Portugal | pt-pt | 0x0816 | 2070 |
| Portuguese - Brazil | pt-br | 0x0416 | 1046 |
| Raeto-Romance | rm | 0x0417 | 1047 |
| Romanian - Romania | ro | 0x0418 | 1048 |
| Romanian - Moldova | ro-mo | 0x0818 | 2072 |
| Russian | ru | 0x0419 | 1049 |
| Russian - Moldova | ru-mo | 0x0819 | 2073 |
| Sanskrit | sa | 0x044F | 1103 |
| Serbian - Cyrillic | sr-sp | 0x0C1A | 3098 |
| Serbian – Latin | sr-sp | 0x081A | 2074 |
| Setsuana | tn | 0x0432 | 1074 |
| Slovenian | sl | 0x0424 | 1060 |
| Slovak | sk | 0x041B | 1051 |
| Sorbian | sb | 0x042E | 1070 |
| Spanish - Spain | es-es | 0x0C0A | 1034 |
| Spanish - Argentina | es-ar | 0x2C0A | 11274 |
| Spanish - Bolivia | es-bo | 0x400A | 16394 |
| Spanish - Chile | es-cl | 0x340A | 13322 |
| Spanish - Colombia | es-co | 0x240A | 9226 |
| Spanish - Costa Rica | es-cr | 0x140A | 5130 |
| Spanish - Dominican Republic | es-do | 0x1C0A | 7178 |
| Spanish - Ecuador | es-ec | 0x300A | 12298 |
| Spanish - Guatemala | es-gt | 0x100A | 4106 |
| Spanish - Honduras | es-hn | 0x480A | 18442 |
| Spanish - Mexico | es-mx | 0x080A | 2058 |
| Spanish - Nicaragua | es-ni | 0x4C0A | 19466 |
| Spanish - Panama | es-pa | 0x180A | 6154 |
| Spanish - Peru | es-pe | 0x280A | 10250 |
| Spanish - Puerto Rico | es-pr | 0x500A | 20490 |
| Spanish - Paraguay | es-py | 0x3C0A | 15370 |
| Spanish - El Salvador | es-sv | 0x440A | 17418 |
| Spanish - Uruguay | es-uy | 0x380A | 14346 |
| Spanish - Venezuela | es-ve | 0x200A | 8202 |
| Sutu | sx | 0x0430 | 1072 |
| Swahili | sw | 0x0441 | 1089 |
| Swedish - Sweden | sv-se | 0x041D | 1053 |
| Swedish - Finland | sv-fi | 0x081D | 2077 |
| Tamil | ta | 0x0449 | 1097 |
| Tatar | tt | 0X0444 | 1092 |
| Thai | th | 0x041E | 1054 |
| Turkish | tr | 0x041F | 1055 |
| Tsonga | ts | 0x0431 | 1073 |
| Ukrainian | uk | 0x0422 | 1058 |
| Urdu | ur | 0x0420 | 1056 |
| Uzbek – Cyrillic | uz-uz | 0x0843 | 2115 |
| Uzbek – Latin | uz-uz | 0x0443 | 1091 |
| Vietnamese | vi | 0x042A | 1066 |
| Xhosa | xh | 0x0434 | 1076 |
| Yiddish | yi | 0x043D | 1085 |
| Zulu | zu | 0x0435 | 1077 |


---

[![VBScript 参考手册](https://www.runoob.com/images/up.gif) 完整的 VBScript 参考手册](https://www.runoob.com/vbscript-ref-functions.html)







	  AI 思考中...





			** [VBScript Eval 函数](https://www.runoob.com/func-eval.html)
			[VBScript GetObject 函数](https://www.runoob.com/func-getobject.html) **













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
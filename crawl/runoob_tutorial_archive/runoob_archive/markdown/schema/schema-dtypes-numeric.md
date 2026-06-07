# XSD 数值数据类型

- Source: https://www.runoob.com/schema/schema-dtypes-numeric.html

---


--- ## 十进制数据类型 十进制数据类型用于规定一个数值。


下面是一个关于某个 scheme 中十进制数声明的例子。


<xs:element name="prize" type="xs:decimal"/>


文档中的元素看上去应该类似这样：


<prize>999.50</prize>


或者类似这样：


<prize>+999.5450</prize>


或者类似这样：


<prize>-999.5230</prize>


或者类似这样：


<prize>0</prize>


或者类似这样：


<prize>14</prize>


**注意：** 您可规定的十进制数字的最大位数是 18 位。


---


## 整数数据类型


整数数据类型用于规定无小数成分的数值。


下面是一个关于某个 scheme 中整数声明的例子。


<xs:element name="prize" type="xs:integer"/>


文档中的元素看上去应该类似这样：


<prize>999</prize>


或者类似这样：


<prize>+999</prize>


或者类似这样：


<prize>-999</prize>


或者类似这样：


<prize>0</prize>

**
---


## 数值数据类型


请注意，下面所有的数据类型均源自于十进制数据类型（除 decimal 本身以外）！


| 名字 | 秒数 |
| --- | --- |
| byte | 有正负的 8 位整数 |
| decimal | 十进制数 |
| int | 有正负的 32 位整数 |
| integer | 整数值 |
| long | 有正负的 64 位整数 |
| negativeInteger | 仅包含负值的整数 ( .., -2, -1.) |
| nonNegativeInteger | 仅包含非负值的整数 (0, 1, 2, ..) |
| nonPositiveInteger | 仅包含非正值的整数 (.., -2, -1, 0) |
| positiveInteger | 仅包含正值的整数 (1, 2, ..) |
| short | 有正负的 16 位整数 |
| unsignedLong | 无正负的 64 位整数 |
| unsignedInt | 无正负的 32 位整数 |
| unsignedShort | 无正负的 16 位整数 |
| unsignedByte | 无正负的 8 位整数 |


---


## 对数值数据类型的限定（Restriction）


可与数值数据类型一同使用的限定：


- enumeration
- fractionDigits
- maxExclusive
- maxInclusive
- minExclusive
- minInclusive
- pattern
- totalDigits
- whiteSpace








	  AI 思考中...





			** [XML Schema 日期/时间 数据类型](https://www.runoob.com/schema-dtypes-date.html)
			[XML Schema 杂项数据类型](https://www.runoob.com/schema-dtypes-misc.html) **













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
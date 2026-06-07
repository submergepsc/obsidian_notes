# XSLT 元素参考手册

- Source: https://www.runoob.com/xsl/xsl-w3celementref.html

---


源自于 W3C 推荐标准（XSLT Version 1.0）的 XSLT 元素。


---


## XSLT 元素


如果您需要有关下列元素的更详细的信息，请点击元素列中的链接。


| 元素 | 描述 |
| --- | --- |
| apply-imports | 应用来自导入样式表中的模版规则。 |
| apply-templates | 向当前元素或当前元素的子节点应用模板规则。 |
| attribute | 添加属性。 |
| attribute-set | 定义命名的属性集。 |
| call-template | 调用一个指定的模板。 |
| choose | 与 以及 协同使用，来表达多重条件测试。 |
| comment | 在结果树中创建注释节点。 |
| copy | 创建当前节点的一个副本（无子节点及属性）。 |
| copy-of | 创建当前节点的一个副本（带有子节点及属性）。 |
| decimal-format | 定义当通过 format-number() 函数把数字转换为字符串时，所要使用的字符和符号。 |
| element | 在输出文档中创建一个元素节点。 |
| fallback | 假如处理器不支持某个 XSLT 元素，规定一段替代代码来运行。 |
| for-each | 循环遍历指定的节点集中的每个节点。 |
| if | 包含一个模板，仅当某个指定的条件成立时应用此模板。 |
| import | 用于把一个样式表中的内容导入另一个样式表中。 注意：被导入的样式表的优先级低于导出的样式表。 |
| include | 把一个样式表中的内容包含到另一个样式表中。注意： 被包含的样式表（included style sheet）拥有与包含的样式表（including style sheet）相同的优先级。 |
| key | 声明一个命名的键，该键通过 key() 函数在样式表中使用。 |
| message | 向输出写一条消息（用于报告错误）。 |
| namespace-alias | 把样式表中的命名空间替换为输出中不同的命名空间。 |
| number | 测定当前节点的整数位置，并对数字进行格式化。 |
| otherwise | 规定 元素的默认动作。 |
| output | 定义输出文档的格式。 |
| param | 声明一个局部或全局参数。 |
| preserve-space | 定义保留空白的元素。 |
| processing-instruction | 向输出写一条处理指令，即生成处理指令节点。 |
| sort | 对输出进行排序。 |
| strip-space | 定义应当删除空白字符的元素。 |
| stylesheet | 定义样式表的根元素。 |
| template | 当指定的节点被匹配时所应用的规则。 |
| text | 向输出写文本，即通过样式表生成文本节点。 |
| transform | 定义样式表的根元素。 |
| value-of | 提取选定节点的值。 |
| variable | 声明局部或者全局的变量。 |
| when | 规定 元素的动作。 |
| with-param | 规定传递给模板的参数的值。 |

**








	  AI 思考中...





			** [XSLT  元素](https://www.runoob.com/el-with-param.html)
			[XSLT current() 函数](https://www.runoob.com/func-current.html) **













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
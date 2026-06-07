# PHP 5 SimpleXML 函数

- Source: https://www.runoob.com/php/php-ref-simplexml.html

---


## PHP SimpleXML 简介


SimpleXML 扩展提供了一种获取 XML 元素的名称和文本的简单方式，只要您知道 XML 文档的布局。


SimpleXML 转换 XML 文档到 SimpleXMLElement 对象。


通过正常的属性选择器和数组迭代器，这个对象能够像其他对象一样被处理。


**提示：**与 DOM 或者 Expat 解析器比较，SimpleXML 只需要几行代码就能读取元素中的文本数据。


---


## 安装


SimpleXML 扩展需要 PHP 5 支持。


自 PHP 5 起，SimpleXML 函数是 PHP 核心的组成部分。无需安装即可使用这些函数。


---


## PHP 5 SimpleXML 函数


| 函数 | 描述 |
| --- | --- |
| __construct() | 创建一个新的 SimpleXMLElement 对象。 |
| addAttribute() | 给 SimpleXML 元素添加一个属性。 |
| addChild() | 给 SimpleXML 元素添加一个子元素。 |
| asXML() | 格式化 XML（版本 1.0）中的 SimpleXML 对象的数据。 |
| attributes() | 返回 XML 标签的属性和值。 |
| children() | 查找指定节点的子节点。 |
| count() | 计算指定节点的子节点个数。 |
| getDocNamespaces() | 返回文档中的声明的命名空间。 |
| getName() | 返回 SimpleXML 元素引用的 XML 标签的名称。 |
| getNamespaces() | 返回文档中使用的命名空间。 |
| registerXPathNamespace() | 为下一个 XPath 查询创建命名空间上下文。 |
| saveXML() | asXML() 的别名。 |
| simplexml_import_dom() | 从 DOM 节点返回 SimpleXMLElement 对象。 |
| simplexml_load_file() | 转换 XML 文件为 SimpleXMLElement 对象。 |
| simplexml_load_string() | 转换 XML 字符串为 SimpleXMLElement 对象。 |
| xpath() | 运行对 XML 数据的 XPath 查询。 |


## PHP 5 SimpleXML 迭代函数


| 函数 | 描述 |
| --- | --- |
| current() | 返回当前元素。 |
| getChildren() | 返回当前元素的子元素。 |
| hasChildren() | 检查当前元素是否有子元素。 |
| key() | 返回当前键。 |
| next() | 移动到下一个元素。 |
| rewind() | 倒回到第一个元素。 |
| valid() | 检查当前元素是否有效。 |








	  AI 思考中...





			** [PHP 5 MySQLi 函数](https://www.runoob.com/php-ref-mysqli.html)
			[PHP 5 String 函数](https://www.runoob.com/php-ref-string.html) **













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
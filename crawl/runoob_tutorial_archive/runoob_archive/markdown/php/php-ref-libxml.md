# PHP Libxml 函数

- Source: https://www.runoob.com/php/php-ref-libxml.html

---


## PHP Libxml 简介


Libxml 函数和常量与 SimpleXML、XSLT 以及 DOM 函数一起使用。


---


## 安装


这些函数需要 Libxml 程序包。 [在 xmlsoft.org 下载](http://www.xmlsoft.org/downloads.html)


---


## PHP Libxml 函数


**PHP**：指示支持该函数的最早的 PHP 版本。


| 函数 | 描述 | PHP |
| --- | --- | --- |
| libxml_clear_errors() | 清空 Libxml 错误缓冲。 | 5 |
| libxml_get_errors() | 检索错误数组。 | 5 |
| libxml_get_last_error() | 从 Libxml 检索最后的错误。 | 5 |
| libxml_set_streams_context() | 为下一次 Libxml 文档加载或写入设置流环境。 | 5 |
| libxml_use_internal_errors() | 禁用 Libxml 错误，允许用户按需读取错误信息。 | 5 |

**
---


## PHP Libxml 常量


| 函数 | 描述 | PHP |
| --- | --- | --- |
| LIBXML_COMPACT | 设置小型节点分配优化。会改善应用程序的性能。 | 5 |
| LIBXML_DTDATTR | 设置默认 DTD 属性。 | 5 |
| LIBXML_DTDLOAD | 加载外部子集。 | 5 |
| LIBXML_DTDVALID | 通过 DTD 进行验证。 | 5 |
| LIBXML_NOBLANKS | 删除空节点。 | 5 |
| LIBXML_NOCDATA | 把 CDATA 设置为文本节点。 | 5 |
| LIBXML_NOEMPTYTAG | 更改空标签（比如 改为 ）。仅在 DOMDocument->save() 和 DOMDocument->saveXML() 函数中可用。 | 5 |
| LIBXML_NOENT | 替代实体。 | 5 |
| LIBXML_NOERROR | 不显示错误报告。 | 5 |
| LIBXML_NONET | 在加载文档时停止网络访问。 | 5 |
| LIBXML_NOWARNING | 不显示警告报告。 | 5 |
| LIBXML_NOXMLDECL | 在保存文档时，撤销 XML 声明。 | 5 |
| LIBXML_NSCLEAN | 删除额外的命名空间声明。 | 5 |
| LIBXML_XINCLUDE | 使用 XInclude 置换。 | 5 |
| LIBXML_ERR_ERROR | 获得可恢复的错误。 | 5 |
| LIBXML_ERR_FATAL | 获得致命的错误。 | 5 |
| LIBXML_ERR_NONE | 获得无错误。 | 5 |
| LIBXML_ERR_WARNING | 获得简单警告。 | 5 |
| LIBXML_VERSION | 获得 Libxml 版本（例如：20605 或 20617）Get libxml version (e.g. 20605 or 20617) | 5 |
| LIBXML_DOTTED_VERSION | 获得有点号的 Libxml 版本（例如：2.6.5 或 2.6.17）。 | 5 |








	  AI 思考中...





			** [PHP HTTP 函数](https://www.runoob.com/php-ref-http.html)
			[PHP Mail 函数](https://www.runoob.com/php-ref-mail.html) **













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
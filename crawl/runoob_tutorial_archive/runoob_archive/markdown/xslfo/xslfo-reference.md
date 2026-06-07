# XSL-FO 参考手册

- Source: https://www.runoob.com/xslfo/xslfo-reference.html

---


## XSL 格式化对象参考手册


将描述转换为呈现的过程被称为格式化（formatting）。


| 对象 | 描述 |
| --- | --- |
| basic-link | 代表一个链接的起始资源。 |
| bidi-override | 重写默认 Unicode BIDI 的方向。 |
| block | 定义一个输出块（比如段落和标题）。 |
| block-container | 定义一个块级的引用区域（reference-area）。 |
| character | 规定将被映射为供呈现的字形的字符。 |
| color-profile | 定义样式表的一个颜色配置文件。 |
| conditional-page-master-reference | 规定一个当所定义的条件成立时使用的 page-master。 |
| declarations | 组合一个样式表的全局声明。 |
| external-graphic | 用于图像数据位于 XML 结果树之外的某个图形。 |
| float | 通常用于在页面起始处的一个单独区域里定位图像，或者通过将内容沿图像的一侧流动来定位图像到一侧。 |
| flow | 包含要打印到页面的所有元素。 |
| footnote | 定义在页面的 region-body 内部的一个脚注。 |
| footnote-body | 定义脚注的内容。 |
| initial-property-set | 格式化 的第一行。 |
| inline | 通过背景属性或将其嵌入一个边框来定义文本的一部分格式。 |
| inline-container | 定义一个内联参考域（reference-area）。 |
| instream-foreign-object | 用于内联图形或 "generic" 类对象。在其中，对象的数据以 的后代形式存在。 |
| layout-master-set | 保存所有在文档中使用的宿主（master）。 |
| leader | 用于生成 "." 符号来分隔内容表格中页面数字的标题，或创建表单中的输入字段，或创建水平规则。 |
| list-block | 定义列表。 |
| list-item | 包含列表中的每个项。 |
| list-item-body | 包含了 list-item 的内容/主体。 |
| list-item-label | 包含了 list-item 标签（通常是数字、字符等）。 |
| marker | 与 一起使用来创建运行的页眉或页脚。 |
| multi-case | 包含 XSL-FO 对象的每个供选择的子树（在 内部）。父元素 会选择要显示的那个选项并隐藏其余的选项。 |
| multi-properties | 用于两个或多个属性集之间切换。 |
| multi-property-set | 规定一个根据用户代理状态进行应用的可选的属性集。 |
| multi-switch | 保留一个或多个 对象，控制它们（由 触发）彼此之间的转换。 |
| multi-toggle | 用于切换到另一个 。 |
| page-number | 表示当前页码。 |
| page-number-citation | 为页面引用页码，此页面包含由被引用对象返回的第一个正常区域。 |
| page-sequence | 页面输出元素的容器。每个页面布局将有一个 对象。 |
| page-sequence-master | 规定要使用的 simple-page-masters 以及使用顺序。 |
| region-after | 定义页脚。 |
| region-before | 定义页眉。 |
| region-body | 定义页面主题。 |
| region-end | 定义页面的右侧栏。 |
| region-start | 定义页面的左侧栏。 |
| repeatable-page-master-alternatives | 规定一组 simple-page-master 的副本。 |
| repeatable-page-master-reference | 规定单个 simple-page-master 的副本。 |
| retrieve-marker | 与 一起使用来创建运行的页眉或页脚。 |
| root | XSL-FO 文档的根（顶级）节点。 |
| simple-page-master | 定义一个页面的尺寸和形状。 |
| single-page-master-reference | 规定用在页面序列的给定点中的 page-master。 |
| static-content | 对象包含了静态内容（如：页眉和页脚），该静态内容将在多个页面中重复调用。 |
| table | 格式化表格的表格式材料。 |
| table-and-caption | 格式化表格及其标题。 |
| table-body | 包含表格行和表格单元格的容器。 |
| table-caption | 包含表格的标题。 |
| table-cell | 定义表格单元格。 |
| table-column | 格式化表格的列。 |
| table-footer | 定义表格的页脚。 |
| table-header | 定义表格的页眉。 |
| table-row | 定义表格行。 |
| title | 为一个 page-sequence 定义一个标题。 |
| wrapper | 为一组 XSL-FO 对象规定 inherited[继承] 属性。 |

**








	  AI 思考中...





			** [XSL-FO wrapper 对象](https://www.runoob.com/obj-wrapper.html)
			[XSL-FO azimuth 属性](https://www.runoob.com/prop-azimuth.html) **













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
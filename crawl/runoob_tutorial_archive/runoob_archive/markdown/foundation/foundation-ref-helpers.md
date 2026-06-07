# Foundation CSS 参考手册

- Source: https://www.runoob.com/foundation/foundation-ref-helpers.html

---


## Foundation 默认设置


Foundation 使用浏览器默认字体大小 (`font-size:100%`)。对于大多数桌面设备的浏览器来说，字体大小默认为 16px。对于移动设备的浏览器，字体默认大小为 12px。 默认的字体为 `"Helvetica Neue"`， line-height 默认为 `1.5`。


这些设置是适用于 `` 元素内的元素。


此外， `` 元素与底部的外边距(margin-bottom) 为 1.25rem , line-height 为 1.6。


---


## 文本


以下的 HTML 元素，Foundation 设置了独立的样式渲染它，不会采用浏览器默认样式。点击 "尝试一下" 查看在线实例。


| 元素 | 描述 | 在线实例 |
| --- | --- | --- |
| - | h1 - h6 标题 | 尝试一下 |
|  | 浅蓝色的链接，鼠标移动到链接会有下划线 | 尝试一下 |
|  | 浅灰色的副标题文本 | 尝试一下 |
|  | 引用内容模块 | 尝试一下 |
|  | 加粗文本 | 尝试一下 |
|  | 斜体 | 尝试一下 |
|  | 指定单词的缩写，使用该元素文本出现虚线下划线，鼠标移动上去会有提示信息 | 尝试一下 |
|  | 接收键盘输入指令: CTRL + P | 尝试一下 |
|  | 水平线 | 尝试一下 |
|  | 代码片段 | 尝试一下 |
|  | 无序列表 | 尝试一下 |
|  | 有序列表 | 尝试一下 |
|  | 描述性列表 | 尝试一下 |


---


## 文本对齐


使用 CSS 类来修改文本的对齐方式：


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .text-left | 左对齐文本 | 尝试一下 |
| .text-right | 右对齐文本 | 尝试一下 |
| .text-center | 居中 | 尝试一下 |
| .text-justify | 两端对齐 | 尝试一下 |


---


## 不同尺寸屏幕的对齐


使用 CSS 类来修改文本的不同尺寸屏幕的对齐方式：


| 类 | 描述 | 实例 |
| --- | --- | --- |
| 左对齐 |  |  |
| .small-text-left | 所有尺寸屏幕左对齐 | 尝试一下 |
| .small-only-text-left | 小尺寸屏幕左对齐(宽度小于 40em ) | 尝试一下 |
| .medium-text-left | 宽度大于 40.0625em 尺寸屏幕左对齐 | 尝试一下 |
| .medium-only-text-left | 宽度在 40.0625em 到 64em 尺寸的屏幕左对齐 | 尝试一下 |
| .large-text-left | 宽度大于 64.0625em 尺寸屏幕左对齐 | 尝试一下 |
| .large-only-text-left | 宽度在 64.0625em 到 90em 尺寸的屏幕左对齐 | 尝试一下 |
| .xlarge-text-left | 宽度大于 90.0625em 尺寸屏幕左对齐 | 尝试一下 |
| .xlarge-only-text-left | 宽度在 90.0625em 到 120em 尺寸的屏幕左对齐 | 尝试一下 |
| .xxlarge-text-left | 宽度大于 120em 尺寸屏幕左对齐 | 尝试一下 |
|  |  |  |
| 右对齐 |  |  |
| .small-text-right | 所有尺寸屏幕右对齐 | 尝试一下 |
| .small-only-text-right | 小尺寸屏幕右对齐(宽度小于 40em ) | 尝试一下 |
| .medium-text-right | 宽度大于 40.0625em 尺寸屏幕右对齐 | 尝试一下 |
| .medium-only-text-right | 宽度在 40.0625em 到 64em 尺寸的屏幕右对齐 | 尝试一下 |
| .large-text-right | 宽度大于 64.0625em 尺寸屏幕右对齐 | 尝试一下 |
| .large-only-text-right | 宽度在 64.0625em 到 90em 尺寸的屏幕右对齐 | 尝试一下 |
| .xlarge-text-right | 宽度大于 90.0625em 尺寸屏幕右对齐 | 尝试一下 |
| .xlarge-only-text-right | 宽度在 90.0625em 到 120em 尺寸的屏幕右对齐 | 尝试一下 |
| .xxlarge-text-right | 宽度大于 120em 尺寸屏幕右对齐 | 尝试一下 |
|  |  |  |
| 居中对齐 |  |  |
| .small-text-center | 所有尺寸屏幕居中对齐 | 尝试一下 |
| .small-only-text-center | 小尺寸屏幕居中对齐(宽度小于 40em ) | 尝试一下 |
| .medium-text-center | 宽度大于 40.0625em 尺寸屏幕居中对齐 | 尝试一下 |
| .medium-only-text-center | 宽度在 40.0625em 到 64em 尺寸的屏幕居中对齐 | 尝试一下 |
| .large-text-center | 宽度大于 64.0625em 尺寸屏幕居中对齐 | 尝试一下 |
| .large-only-text-center | 宽度在 64.0625em 到 90em 尺寸的屏幕居中对齐 | 尝试一下 |
| .xlarge-text-center | 宽度大于 90.0625em 尺寸屏幕居中对齐 | 尝试一下 |
| .xlarge-only-text-center | 宽度在 90.0625em 到 120em 尺寸的屏幕居中对齐 | 尝试一下 |
| .xxlarge-text-center | 宽度大于 120em 尺寸屏幕居中对齐 | 尝试一下 |
|  |  |  |
| 两端对齐 |  |  |
| .small-text-justify | 所有尺寸屏幕都两端对齐 | 尝试一下 |
| .small-only-text-justify | 小尺寸屏幕两端对齐(宽度小于 40em ) | 尝试一下 |
| .medium-text-justify | 宽度大于 40.0625em 尺寸屏幕两端对齐 | 尝试一下 |
| .medium-only-text-justify | 宽度在 40.0625em 到 64em 尺寸的屏幕两端对齐 | 尝试一下 |
| .large-text-justify | 宽度大于 64.0625em 尺寸屏幕两端对齐 | 尝试一下 |
| .large-only-text-justify | 宽度在 64.0625em 到 90em 尺寸的屏幕两端对齐 | 尝试一下 |
| .xlarge-text-justify | 宽度大于 90.0625em 尺寸屏幕两端对齐 | 尝试一下 |
| .xlarge-only-text-justify | 宽度在 90.0625em 到 120em 尺寸的屏幕两端对齐 | 尝试一下 |
| .xxlarge-text-justify | 宽度大于 120em 尺寸屏幕两端对齐 | 尝试一下 |


---


## 其他


| 类 | 描述 | 实例 |
| --- | --- | --- |
| .left | 元素向左浮动 | 尝试一下 |
| .right | 元素向右浮动 | 尝试一下 |
| .clearfix | 清除浮动 - 必须添加在浮动元素的父元素上 |  |
| .hide | 隐藏元素 (CSS display: none) | 尝试一下 |
| .list-inline | 将所有元素设置在同一行 | 尝试一下 |
| .lead | 让 元素更突出 | 尝试一下 |
| .subheader | 设置浅色的 - 元素 | 尝试一下 |









	  AI 思考中...





			** [Foundation 图标参考手册](https://www.runoob.com/foundation-ref-icons.html)
			[Foundation CSS 可见性](https://www.runoob.com/foundation-ref-visibility.html) **













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
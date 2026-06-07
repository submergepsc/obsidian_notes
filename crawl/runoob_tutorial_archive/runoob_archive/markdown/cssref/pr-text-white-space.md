# CSS white-space 属性

- Source: https://www.runoob.com/cssref/pr-text-white-space.html

**
## 实例


规定段落中的文本不进行换行：


```css
p {
    white-space:nowrap;
}
```


[尝试一下 »](https://www.runoob.com/try/try.php?filename=trycss_text_white-space)


---


## 属性定义及使用说明


white-space属性指定元素内的空白怎样处理。


| 默认值： | normal |
| --- | --- |
| 继承： | yes |
| 版本： | CSS1 |
| JavaScript 语法： | object.style.whiteSpace="pre" |


---


## 浏览器支持


表格中的数字表示支持该属性的第一个浏览器版本号。


| 属性 |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| white-space | 1.0 | 5.5 | 3.5 | 3.0 | 9.5 |


---


## 语法


```
/* 值 */
white-space: normal;
white-space: nowrap;
white-space: pre;
white-space: pre-wrap;
white-space: pre-line;
white-space: break-spaces;

/* 全局值 */
white-space: inherit;
white-space: initial;
white-space: revert;
white-space: revert-layer;
white-space: unset;
```


---


## 属性值


| 值 | 描述 |
| --- | --- |
| normal | 默认。空白会被浏览器忽略。 |
| pre | 空白会被浏览器保留。其行为方式类似 HTML 中的 标签。 |
| nowrap | 文本不会换行，文本会在在同一行上继续，直到遇到 标签为止。 |
| pre-wrap | 保留空白符序列，但是正常地进行换行。 |
| pre-line | 合并空白符序列，但是保留换行符。 |
| inherit | 规定应该从父元素继承 white-space 属性的值。 |


各种 white-space 值的行为：


|  | 换行符 | 空格和制表符 | 文字换行 | 行尾空格 |
| --- | --- | --- | --- | --- |
| normal | 合并 | 合并 | 换行 | 删除 |
| nowrap | 合并 | 合并 | 不换行 | 删除 |
| pre | 保留 | 保留 | 不换行 | 保留 |
| pre-wrap | 保留 | 保留 | 换行 | 挂起 |
| pre-line | 保留 | 合并 | 换行 | 删除 |
| break-spaces | 保留 | 保留 | 换行 | 换行 |


---


## 相关文章


CSS 教程: [CSS Text](https://www.runoob.com/../css/css-text.html)









	  AI 思考中...





			** [CSS width 属性](https://www.runoob.com/pr-dim-width.html)
			[CSS word-spacing 属性](https://www.runoob.com/pr-text-word-spacing.html) **













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